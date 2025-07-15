---
title: Release Notes for 2025-05-26
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250526.html
folder: release_notes
---

## Module: azure-law
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-law/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#96](https://github.com/CloudNationHQ/terraform-azure-law/issues/96)) ([9cd1015](https://github.com/CloudNationHQ/terraform-azure-law/commit/9cd1015ec7d8d72d386882dca053136a12552736))

### Upgrade from v2.3.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- The user assigned identity is removed from the module and it is not set to system assigned default anymore as well.
  - For identity we created a separate module as shown in the examples.
- The property and variable resource_group is renamed to resource_group_name

---

