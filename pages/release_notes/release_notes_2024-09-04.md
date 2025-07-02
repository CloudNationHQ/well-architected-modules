---
title: Releases for 2024-09-04
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 02, 2025
summary: "Releases of the Terraform Well Architected Modules 2024-09-04"
sidebar: mydoc_sidebar
permalink: release_notes_20240904.html
folder: release_notes
---

# Release Notes for 2024-09-04

## azure-acr
### v2.0.0 (v2.0.0)
**Published at:** 2024-09-04T08:43:11Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-acr/compare/v1.7.0...v2.0.0) (2024-09-04)


### ⚠ BREAKING CHANGES

* data structure has changed due to renaming of properties.

### Features

* aligned several properties ([#60](https://github.com/CloudNationHQ/terraform-azure-acr/issues/60)) ([12cc189](https://github.com/CloudNationHQ/terraform-azure-acr/commit/12cc18929519d0e72b83340459841c05dd7e18b0))

### Upgrade from v1.7.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- Rename or remove properties in registry object:
  - resourcegroup -> resource_group
  - trust_policy.enabled -> trust_policy
  - retention_policy.enabled -> retention_policy
  - replications -> georeplications
  - encryption.enable -> encryption
- Rename variable (optional):
  - resourcegroup -> resource_group
- Rename output variable:
  - subscriptionId -> subscription_id'
  - acr -> registry
- Change defaults:
  - identity is now fully optional 
  - enabled property under trust_policy now defaults to false

---

## azure-evh
### v1.2.0 (v1.2.0)
**Published at:** 2024-09-04T19:28:02Z

## [1.2.0](https://github.com/CloudNationHQ/terraform-azure-evh/compare/v1.1.1...v1.2.0) (2024-09-04)


### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#38](https://github.com/CloudNationHQ/terraform-azure-evh/issues/38)) ([e89daaf](https://github.com/CloudNationHQ/terraform-azure-evh/commit/e89daaff00706707e5b93fca788f0386771a1dbd))

---

## azure-evh
### v1.1.1 (v1.1.1)
**Published at:** 2024-09-04T13:04:20Z

## [1.1.1](https://github.com/CloudNationHQ/terraform-azure-evh/compare/v1.1.0...v1.1.1) (2024-09-04)


### Bug Fixes

* added zone_redundant  property for event hub namespace ([#40](https://github.com/CloudNationHQ/terraform-azure-evh/issues/40)) ([7f57ca9](https://github.com/CloudNationHQ/terraform-azure-evh/commit/7f57ca956e6517cfe211f8af1cf4149d38a1858b))

---

