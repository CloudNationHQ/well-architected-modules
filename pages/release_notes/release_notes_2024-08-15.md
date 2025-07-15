---
title: Release Notes for 2024-08-15
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20240815.html
folder: release_notes
---

## Module: azure-sa
## [1.1.0](https://github.com/CloudNationHQ/terraform-azure-sa/releases/tag/v1.1.0)


### Features

* added code of conduct and security documentation ([#103](https://github.com/CloudNationHQ/terraform-azure-sa/issues/103)) ([755bc3a](https://github.com/CloudNationHQ/terraform-azure-sa/commit/755bc3a342573f140e2b8b6485e301a30297f2d4))

---

**Published at:** 2024-08-15T08:44:00Z

## Module: azure-kv
## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-kv/releases/tag/v1.0.0)


### ⚠ BREAKING CHANGES

* data structure has changed due to renaming of properties and output variables.

### Features

* aligned several properties ([#60](https://github.com/CloudNationHQ/terraform-azure-kv/issues/60)) ([17499ee](https://github.com/CloudNationHQ/terraform-azure-kv/commit/17499ee05026d38d943b7e65868adc7db72f2d34))

### Upgrade from v0.14.0 to v1.0.0:

- Update module reference to: `version = "~> 1.0"`
- Rename properties in vault object:
  - resourcegroup -> resource_group
  - sku -> sku_name
- Rename variable:
  - resourcegroup -> resource_group
- Rename output variable:
  - subscriptionId -> subscription_id'

---

**Published at:** 2024-08-15T08:14:52Z

## Module: azure-plan
## [1.1.1](https://github.com/CloudNationHQ/terraform-azure-plan/releases/tag/v1.1.1)


### Bug Fixes

* wrong module reference ([4c44230](https://github.com/CloudNationHQ/terraform-azure-plan/commit/4c44230a22ec8a5b1be2cdef9a73e8ef52ce5c80))

---

**Published at:** 2024-08-15T05:57:27Z

## Module: azure-plan
## [1.1.0](https://github.com/CloudNationHQ/terraform-azure-plan/releases/tag/v1.1.0)

### Bug Fixes

* fixed resource group and location conditions ([437f345](https://github.com/CloudNationHQ/terraform-azure-plan/commit/437f3451412d3073678d33e1108c751619ebf126))

---

**Published at:** 2024-08-15T05:43:29Z

