---
title: Releases for 2024-08-15
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 09, 2025
summary: "Releases of the Terraform Well Architected Modules 2024-08-15"
sidebar: mydoc_sidebar
permalink: release_notes_20240815.html
folder: release_notes
---

# Release Notes for 2024-08-15

## azure-vnet
### v3.0.0 (v3.0.0)
**Published at:** 2024-08-15T10:21:12Z

## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-vnet/compare/v2.9.0...v3.0.0) (2024-08-15)


### ⚠ BREAKING CHANGES

* data structure has changed due to renaming of properties and output variables.

### Features

* aligned several properties ([#78](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/78)) ([d28b39a](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/d28b39aa54fed5d2c8a8ffddda4eeeeb3e8bdc53))

### Upgrade from v2.9.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- Rename properties in vnet object:
  - resourcegroup -> resource_group
  - private_endpoint_network_policies_enabled -> private_endpoint_network_policies
- Rename variable (optional):
  - resourcegroup -> resource_group
- Rename output variable:
  - subscriptionId -> subscription_id'
  - nsg -> network_security_group

---

## azure-sa
### v1.1.0 (v1.1.0)
**Published at:** 2024-08-15T08:44:00Z

## [1.1.0](https://github.com/CloudNationHQ/terraform-azure-sa/compare/v1.0.0...v1.1.0) (2024-08-15)


### Features

* added code of conduct and security documentation ([#103](https://github.com/CloudNationHQ/terraform-azure-sa/issues/103)) ([755bc3a](https://github.com/CloudNationHQ/terraform-azure-sa/commit/755bc3a342573f140e2b8b6485e301a30297f2d4))

---

## azure-kv
### v1.0.0 (v1.0.0)
**Published at:** 2024-08-15T08:14:52Z

## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-kv/compare/v0.14.0...v1.0.0) (2024-08-15)


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

## azure-plan
### v1.1.1 (v1.1.1)
**Published at:** 2024-08-15T05:57:27Z

## [1.1.1](https://github.com/CloudNationHQ/terraform-azure-plan/compare/v1.1.0...v1.1.1) (2024-08-15)


### Bug Fixes

* wrong module reference ([4c44230](https://github.com/CloudNationHQ/terraform-azure-plan/commit/4c44230a22ec8a5b1be2cdef9a73e8ef52ce5c80))

---

## azure-plan
### v1.1.0 (v1.1.0)
**Published at:** 2024-08-15T05:43:29Z

## [1.1.0](https://github.com/CloudNationHQ/terraform-azure-plan/compare/v1.0.0...v1.1.0) (2024-08-15)

### Bug Fixes

* fixed resource group and location conditions ([437f345](https://github.com/CloudNationHQ/terraform-azure-plan/commit/437f3451412d3073678d33e1108c751619ebf126))

---

