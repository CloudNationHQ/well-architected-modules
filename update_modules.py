import requests

# Filepath to the Markdown file
MARKDOWN_FILE = "pages/mydoc/mydoc_cn_terraform_resource_modules.md"

# Terraform Registry API base URL for the namespace
API_URL = "https://registry.terraform.io/v1/modules?namespace=CloudNationHQ"

# Function to fetch all modules with pagination
def fetch_all_modules(api_url):
    modules = []
    offset = 0
    limit = 15  # Default limit per page

    while True:
        response = requests.get(f"{api_url}&offset={offset}&limit={limit}")
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

# Fetch all modules
modules = fetch_all_modules(API_URL)

# Sort modules alphabetically by name
modules = sorted(modules, key=lambda x: x["name"])

# Header content to add at the beginning of the Markdown file
header_content = """---
title: Terraform Resource Modules
sidebar: mydoc_sidebar
permalink: terraform_resource_modules.html
folder: mydoc
---

## Module catalog

The following table shows the number of all available Terraform Resource Modules. 

"""

# Generate the Markdown table
markdown_table = """
<table>
<colgroup>
<col width="30%" />
<col width="70%" />
</colgroup>
<thead>
<tr class="header">
<th>Module name</th>
<th>Description</th>
<th>Latest version</th>
<th>Link</th>
</tr>
</thead>
<tbody>
"""

for module in modules:
    name = module["name"]
    provider = module["provider"]
    description = module["description"]
    version = module["version"]  # Latest version
    source = module["source"]  # GitHub repo link

    markdown_table += f"""
<tr>
<td markdown="span">{name}</td>
<td markdown="span">{provider}</td>
<td markdown="span">{description}.</td> 
<td markdown="span">{version}</td>
<td markdown="span"><a href="{source}" target="_blank">Github repo {name}</a></td>
</tr>
"""

markdown_table += """
</tbody>
</table>
"""

# Add the total number of modules at the end
total_modules = len(modules)
markdown_table += f"\n\n<span class='total-modules'>**Total Modules:** {total_modules}\n</span>"

# Combine the header and the table
final_markdown = header_content + markdown_table

# Overwrite the Markdown file with the new content
with open(MARKDOWN_FILE, "w") as file:
    file.write(final_markdown)

print(f"Markdown file updated successfully! Total modules: {total_modules}")