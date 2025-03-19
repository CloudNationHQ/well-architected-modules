import requests
import os
from datetime import datetime
from collections import defaultdict

# Terraform Registry API base URL for the namespace
API_URL = "https://registry.terraform.io/v1/modules?namespace=CloudNationHQ"

# Directory to store the release notes
RELEASE_NOTES_DIR = "pages/release_notes"

# Function to fetch all modules with pagination
def fetch_all_modules(api_url):
    modules = []
    offset = 0
    limit = 15  # Default limit per page
    headers = {"User-Agent": "request"}  # Add User-Agent header

    while True:
        response = requests.get(f"{api_url}&offset={offset}&limit={limit}", headers=headers)
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
    headers = {"User-Agent": "request"}  # Add User-Agent header
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch releases for {provider_name}-{module_name}: {response.status_code}")
    return response.json()

# Function to generate a Markdown file for combined release notes
def generate_combined_release_notes(releases_by_date):
    # Ensure the release notes directory exists
    if not os.path.exists(RELEASE_NOTES_DIR):
        os.makedirs(RELEASE_NOTES_DIR)

    for release_date, releases in releases_by_date.items():
        file_path = os.path.join(RELEASE_NOTES_DIR, f"release_notes_{release_date}.md")

        # Check if the file already exists
        if os.path.exists(file_path):
            print(f"Release notes for {release_date} already exist. Skipping...")
            continue

        # Write the combined release notes to the file
        with open(file_path, "w") as file:
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