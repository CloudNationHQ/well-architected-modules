---
title: Release Notes for 2026-01-09
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20260109.html
folder: release_notes
---

## Module: azure-apim
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-apim/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* this change causes recreates

### Features

* add type definitions and changed data structure ([#35](https://github.com/CloudNationHQ/terraform-azure-apim/issues/35)) ([4d8ff5d](https://github.com/CloudNationHQ/terraform-azure-apim/commit/4d8ff5d0758768cc9dd491090057962975f51284))
* updated documentation
* added type definitions
* removed deprecated and added missing properties

### Upgrade from v2.5.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- The property and variable resource_group is renamed to resource_group_name

---

