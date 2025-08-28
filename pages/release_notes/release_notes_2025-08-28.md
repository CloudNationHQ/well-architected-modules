---
title: Release Notes for 2025-08-28
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250828.html
folder: release_notes
---

## Module: azure-aks
## [4.0.0](https://github.com/CloudNationHQ/terraform-azure-aks/releases/tag/v4.0.0)


### ⚠ BREAKING CHANGES

* this change causes recreates

### Features

* add type definitions and changed data structure ([#130](https://github.com/CloudNationHQ/terraform-azure-aks/issues/130)) ([6d54751](https://github.com/CloudNationHQ/terraform-azure-aks/commit/6d547513bb5ed6b66af8046d52e66605bbe79a4f))

### Upgrade from v3.7.0 to v4.0.0:

- Update module reference to: `version = "~> 4.0"`
- The property and variable resource_group is renamed to resource_group_name
- The user assigned identity resource is moved to a dedicated module
- The use of credentials changed in the data structure. See the examples for more details

---

