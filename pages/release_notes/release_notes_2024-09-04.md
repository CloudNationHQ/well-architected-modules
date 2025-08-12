---
title: Release Notes for 2024-09-04
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20240904.html
folder: release_notes
---

## Module: azure-acr
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-acr/releases/tag/v2.0.0)


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

## Module: azure-evh
## [1.2.0](https://github.com/CloudNationHQ/terraform-azure-evh/releases/tag/v1.2.0)


### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#38](https://github.com/CloudNationHQ/terraform-azure-evh/issues/38)) ([e89daaf](https://github.com/CloudNationHQ/terraform-azure-evh/commit/e89daaff00706707e5b93fca788f0386771a1dbd))

---

## Module: azure-evh
## [1.1.1](https://github.com/CloudNationHQ/terraform-azure-evh/releases/tag/v1.1.1)


### Bug Fixes

* added zone_redundant  property for event hub namespace ([#40](https://github.com/CloudNationHQ/terraform-azure-evh/issues/40)) ([7f57ca9](https://github.com/CloudNationHQ/terraform-azure-evh/commit/7f57ca956e6517cfe211f8af1cf4149d38a1858b))

---

