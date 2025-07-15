---
title: Release Notes for 2024-10-04
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20241004.html
folder: release_notes
---

## Module: azure-vmss
## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-vmss/releases/tag/v1.0.0)


### ⚠ BREAKING CHANGES

* data structure has changed due to renaming of properties.

### Features

* aligned several properties ([#39](https://github.com/CloudNationHQ/terraform-azure-vmss/issues/39)) ([8e6b5b4](https://github.com/CloudNationHQ/terraform-azure-vmss/commit/8e6b5b4c0d16535344b20011a0289335c8c84800))

### Upgrade from v0.8.0 to v1.0.0:

- Update module reference to: `version = "~> 1.0"`
- Rename properties in vmss object:
  - resourcegroup -> resource_group
- Rename variable (optional):
  - resourcegroup -> resource_group

---

**Published at:** 2024-10-04T09:14:52Z

