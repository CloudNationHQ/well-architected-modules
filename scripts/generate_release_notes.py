import requests
import os
import time
from ruamel.yaml import YAML
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
summary: "Releases of the Terraform Well Architected Modules {release_date}"
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

# # Function to update the sidebar YAML file
def update_sidebar(sidebar_entries):
    yaml = YAML()
    yaml.preserve_quotes = True  # Preserve quotes in the YAML file
    yaml.indent(mapping=2, sequence=4, offset=2)
    # Load the existing sidebar YAML file
    with open(SIDEBAR_FILE, "r") as file:
        sidebar_data = yaml.load(file)
    print(sidebar_data)

     # Initialize the YAML structure if the file is empty
    if sidebar_data is None:
        sidebar_data = {"entries": []}

    # Ensure the "entries" key exists
    if "entries" not in sidebar_data:
        sidebar_data["entries"] = []

    # Locate the "Release Notes" section within entries.folders.folderitems
    release_notes_section = None
    for entry in sidebar_data["entries"]:
        if "folders" in entry:
            for folder in entry["folders"]:
                if "folderitems" in folder:
                    for folderitem in folder["folderitems"]:
                        if folderitem.get("title") == "Tag releases overview" and "subfolders" in folderitem:
                            release_notes_section = folderitem
                            break
                if release_notes_section:
                    break
        if release_notes_section:
            break
        
    if not release_notes_section:
        raise Exception("Release Notes section not found in the sidebar YAML file.")

    # Ensure the "subfolders" key exists in the Release Notes section
    if "subfolders" not in release_notes_section:
        release_notes_section["subfolders"] = []
    if release_notes_section["subfolders"] is None:
        release_notes_section["subfolders"] = []

    # Group new entries by quarter
    for release_date, releases in sidebar_entries.items():
        # Parse the release date
        release_date_obj = datetime.strptime(release_date, "%B %Y")
        year = release_date_obj.year
        quarter = (release_date_obj.month - 1) // 3 + 1
        quarter_title = f"Q{quarter} {year}"

        # Find or create the quarter subfolder
        quarter_subfolder = next(
            (subfolder for subfolder in release_notes_section["subfolders"] if subfolder["title"] == quarter_title),
            None
        )
        if not quarter_subfolder:
            quarter_subfolder = {"title": quarter_title, "output": "web, pdf", "subfolderitems": []}
            release_notes_section["subfolders"].append(quarter_subfolder)
        # Add the release entries to the quarter subfolder
        for release in releases:
            release_entry = {
                "title": f"{release['title']}",
                "url": f"{release['url']}",
                "output": "web, pdf"
            }
            # Avoid duplicate entries
            if release_entry not in quarter_subfolder["subfolderitems"]:
                quarter_subfolder["subfolderitems"].append(release_entry)

     # Sort the quarters and releases in descending order by year and ascending order by quarter
    release_notes_section["subfolders"].sort(
        key=lambda x: (int(x["title"].split(" ")[1]), int(x["title"].split(" ")[0][1:])),
        reverse=True  # Ascending order for quarters
    )
    release_notes_section["subfolders"].sort(
        key=lambda x: int(x["title"].split(" ")[1]), reverse=True  # Descending order for years
    )
    for subfolder in release_notes_section["subfolders"]:
        subfolder["subfolderitems"].sort(key=lambda x: x["title"], reverse=True)

    # Save the updated sidebar YAML file
    with open(SIDEBAR_FILE, "w") as file:
        yaml.dump(sidebar_data, file)

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