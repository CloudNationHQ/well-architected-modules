---
title: Release Notes for 2025-06-25
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250625.html
folder: release_notes
---

## Module: azure-sqlmi
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-sqlmi/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#25](https://github.com/CloudNationHQ/terraform-azure-sqlmi/issues/25)) ([849eea4](https://github.com/CloudNationHQ/terraform-azure-sqlmi/commit/849eea4968e10fa434a5b8c4b3f2ee75a8dfb03f))

### Upgrade from v1.4.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The property and variable resource_group is renamed to resource_group_name
- The data structure changed for long_term_retention_policy and point_in_time_restore regarding databases

For more details see the usage examples

---

**Published at:** 2025-06-25T12:47:09Z

