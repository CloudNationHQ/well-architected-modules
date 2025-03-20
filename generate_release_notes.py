import requests
import os
import yaml
import time
from datetime import datetime
from collections import defaultdict

# Terraform Registry API base URL for the namespace
API_URL = "https://registry.terraform.io/v1/modules?namespace=CloudNationHQ"

# Directory to store the release notes
RELEASE_NOTES_DIR = "pages/release_notes"

# GitHub Personal Access Token (replace with your token or load from environment variables)
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN", "your_personal_access_token_here")

# Headers for GitHub API requests
HEADERS = {
    "User-Agent": "request",
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}

# Path to the sidebar YAML file
SIDEBAR_FILE = "_data/sidebars/mydoc_sidebar.yml"

# Function to fetch all modules with pagination
def fetch_all_modules(api_url):
    modules = []
    offset = 0
    limit = 15  # Default limit per page

    while True:
        response = requests.get(f"{api_url}&offset={offset}&limit={limit}", headers=HEADERS)
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from Terraform Registry: {response.status_code}")

        data = response.json()
        modules.extend(data["modules"])  # Add the modules from the current page

        # Check if there are more results
        if "next_offset" not in data["meta"]:
            break

        # Update the offset for the next page
        offset = data["meta"]["next_offset"]

    return modules

# Function to fetch releases for a specific repository
def fetch_releases(module_name, provider_name):
    print(f"Fetching releases for {provider_name}-{module_name}...")
    url = f"https://api.github.com/repos/CloudNationHQ/terraform-{provider_name}-{module_name}/releases"
    
    while True:
        response = requests.get(url, headers=HEADERS)
        
        # Handle rate limit
        if response.status_code == 403 and "X-RateLimit-Remaining" in response.headers:
            reset_time = int(response.headers.get("X-RateLimit-Reset", time.time() + 30))
            wait_time = max(reset_time - int(time.time()), 30)  # Wait at least 30 seconds
            print(f"Rate limit exceeded. Retrying after {wait_time} seconds...")
            time.sleep(wait_time)
            continue  # Retry the request
        
        # Handle other errors
        if response.status_code != 200:
            raise Exception(f"Failed to fetch releases for {provider_name}-{module_name}: {response.status_code}")
        
        # If successful, return the JSON response
        return response.json()

# Function to generate a Markdown file for combined release notes
def generate_combined_release_notes(releases_by_date):
    # Ensure the release notes directory exists
    if not os.path.exists(RELEASE_NOTES_DIR):
        os.makedirs(RELEASE_NOTES_DIR)

    sidebar_entries = defaultdict(list)

    for release_date, releases in releases_by_date.items():
        file_path = os.path.join(RELEASE_NOTES_DIR, f"release_notes_{release_date}.md")

        # Generate dynamic metadata
        title = f"Releases for {release_date}"
        permalink = f"release_notes_{release_date.replace('-', '')}.html"
        last_updated = datetime.now().strftime("%b %d, %Y")

        # Write the combined release notes to the file
        with open(file_path, "w") as file:
            # Add the header content
            file.write(f"""---
title: {title}
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: {last_updated}
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: {permalink}
folder: release_notes
---

""")
            file.write(f"# Release Notes for {release_date}\n\n")
            for release in releases:
                module_name = release["module_name"]
                provider_name = release["provider_name"]
                file.write(f"## {provider_name}-{module_name}\n")
                file.write(f"### {release['name']} ({release['tag_name']})\n")
                file.write(f"**Published at:** {release['published_at']}\n\n")
                file.write(f"{release['body']}\n\n")
                file.write("---\n\n")

        print(f"Combined release notes generated: {file_path}")

        # Add to sidebar entries grouped by month
        month = datetime.strptime(release_date, "%Y-%m-%d").strftime("%B %Y")
        sidebar_entries[month].append({
            "title": f"Release {release_date}",
            "url": f"/{permalink}",
            "output": "web, pdf"
        })

    # Update the sidebar YAML file
    update_sidebar(sidebar_entries)

# Function to update the sidebar YAML file
def update_sidebar(sidebar_entries):
    # Load the existing sidebar YAML file
    with open(SIDEBAR_FILE, "r") as file:
        sidebar_data = yaml.safe_load(file)

    # Find or create the "Release Notes" section
    release_notes_section = next(
        (entry for entry in sidebar_data["entries"] if entry["title"] == "Release Notes"), None
    )
    if not release_notes_section:
        release_notes_section = {"title": "Release Notes", "output": "web, pdf", "folderitems": []}
        sidebar_data["entries"].append(release_notes_section)

    # Add monthly overview pages and individual releases
    for month, releases in sidebar_entries.items():
        # Check if the month already exists in the sidebar
        month_entry = next(
            (item for item in release_notes_section["folderitems"] if item["title"] == month), None
        )
        if not month_entry:
            month_entry = {"title": month, "output": "web, pdf", "folderitems": []}
            release_notes_section["folderitems"].append(month_entry)

        # Add individual releases to the month's folderitems
        month_entry["folderitems"].extend(releases)

    # Save the updated sidebar YAML file
    with open(SIDEBAR_FILE, "w") as file:
        yaml.dump(sidebar_data, file, default_flow_style=False)

    print(f"Sidebar updated with release notes.")

# Main function to fetch and generate release notes
def main():
    # Dynamically fetch repo names from the Terraform Registry
    print("Fetching module repositories from Terraform Registry...")
    modules = fetch_all_modules(API_URL)

    # Group releases by date
    releases_by_date = defaultdict(list)

    for module in modules:
        module_name = module["name"]
        provider_name = module["provider"]

        # Fetch releases for the module
        releases = fetch_releases(module_name, provider_name)
        if releases:
            for release in releases:
                release_date = release["published_at"].split("T")[0]  # Get the date part of the timestamp
                releases_by_date[release_date].append({
                    "module_name": module_name,
                    "provider_name": provider_name,
                    "name": release["name"],
                    "tag_name": release["tag_name"],
                    "published_at": release["published_at"],
                    "body": release["body"]
                })

    # Generate combined release notes
    generate_combined_release_notes(releases_by_date)

if __name__ == "__main__":
    main()