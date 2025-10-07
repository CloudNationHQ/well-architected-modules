---
title: Release Notes for 2025-09-30
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250930.html
folder: release_notes
---

## Module: azure-fd
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-fd/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* this change causes recreates

### Features

* add type definitions and changed data structure ([#22](https://github.com/CloudNationHQ/terraform-azure-fd/issues/22)) ([7e1e3c6](https://github.com/CloudNationHQ/terraform-azure-fd/commit/7e1e3c6e0e32729c20361168b5c588b120146f6a))

### Upgrade from v1.4.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The property and variable resource_group is renamed to resource_group_name

---

