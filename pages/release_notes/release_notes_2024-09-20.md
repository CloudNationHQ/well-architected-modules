---
title: Releases for 2024-09-20
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 08, 2025
summary: "Releases of the Terraform Well Architected Modules 2024-09-20"
sidebar: mydoc_sidebar
permalink: release_notes_20240920.html
folder: release_notes
---

# Release Notes for 2024-09-20

## azure-aa
### v1.0.0 (v1.0.0)
**Published at:** 2024-09-20T11:38:16Z

## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-aa/compare/v0.4.0...v1.0.0) (2024-09-20)


### ⚠ BREAKING CHANGES

* data structure has changed due to renaming of properties.

### Features

* aligned several properties ([#16](https://github.com/CloudNationHQ/terraform-azure-aa/issues/16)) ([f769253](https://github.com/CloudNationHQ/terraform-azure-aa/commit/f769253f72fa721572ed55f7a1021a5a93c2818e))

### Upgrade from v0.4.0 to v1.0.0:

- Update module reference to: `version = "~> 1.0"`
- Rename object account to config
- Rename properties in config object:
  - resourcegroup -> resource_group
- Rename variable:
  - resourcegroup -> resource_group
- Rename output variable:
  - account -> config

---

