---
title: Releases for 2025-06-25
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 04, 2025
summary: "Releases of the Terraform Well Architected Modules 2025-06-25"
sidebar: mydoc_sidebar
permalink: release_notes_20250625.html
folder: release_notes
---

# Release Notes for 2025-06-25

## azure-sqlmi
### v2.0.0 (v2.0.0)
**Published at:** 2025-06-25T12:47:09Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-sqlmi/compare/v1.4.0...v2.0.0) (2025-06-25)


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

