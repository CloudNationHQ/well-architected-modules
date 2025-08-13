---
title: Release Notes for 2024-08-14
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20240814.html
folder: release_notes
---

## Module: azure-law
## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-law/releases/tag/v1.0.0)


### ⚠ BREAKING CHANGES

* data structure has changed due to renaming of properties and output variables.

### Features

* aligned several properties ([#65](https://github.com/CloudNationHQ/terraform-azure-law/issues/65)) ([8e86489](https://github.com/CloudNationHQ/terraform-azure-law/commit/8e864898915358c812d1d44d7a477c9d9232dc7e))

### Upgrade from v0.12.0 to v1.0.0:

- Update module reference to: `version = "~> 1.0"`
- Instance object has changed to workspace
- Rename properties in instance object:
  - resourcegroup -> resource_group
- Rename variable (optional):
  - resourcegroup -> resource_group
- Rename output variable:
  - subscriptionId -> subscription_id'

---

## Module: azure-cosmosdb
## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/releases/tag/v1.0.0)


### ⚠ BREAKING CHANGES

* data structure has changed due to renaming of properties and output variables.

### Features

* aligned several properties ([#52](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/issues/52)) ([eae958d](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/commit/eae958d3a21710ab4a1d79d4a18d4701ff3aa751))

### Upgrade from v0.11.0 to v1.0.0:

- Update module reference to: `version = "~> 1.0"`
- cosmosdb object name has changed to account
- Rename properties in account object:
  - resourcegroup -> resource_group
  - unique_key_paths -> partition_key_paths
- Rename variable (optional):
  - resourcegroup -> resource_group
- Rename output variable:
  - subscriptionId -> subscription_id'
- Support for multiple unique_key configurations
  - The static unique_key block has been replaced with a dynamic block to support multiple unique_key configurations in cosmosdb sql containers.

---

## Module: azure-cosmosdb
## [0.11.0](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/releases/tag/v0.11.0)


### Features

* added code of conduct and security documentation ([#49](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/issues/49)) ([98cd2b6](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/commit/98cd2b615e1acd8748333d907be760430ef18cdc))

---

## Module: azure-cosmosdb
## [0.10.0](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/releases/tag/v0.10.0)


### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#47](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/issues/47)) ([71d2ab4](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/commit/71d2ab4abf11244218825c4b197371f9c63321fd))
* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#48](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/issues/48)) ([17ec059](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/commit/17ec0596f830aed714fe96d88568bf5e1b3684fa))
* update contribution docs ([#45](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/issues/45)) ([7c0670f](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/commit/7c0670f850cad43a60d9616c3b5bea77dc5f9c9d))

---

## Module: azure-bastion
## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-bastion/releases/tag/v1.0.0)


### ⚠ BREAKING CHANGES

* data structure has changed due to renaming of properties and output variables.

### Features

* aligned several properties ([#46](https://github.com/CloudNationHQ/terraform-azure-bastion/issues/46)) ([4388103](https://github.com/CloudNationHQ/terraform-azure-bastion/commit/4388103380715033f5e3f0c513bf28e92af762e4))

### Upgrade from v0.11.0 to v1.0.0:

- Update module reference to: `version = "~> 1.0"`
- Rename properties in host object:
  - resourcegroup -> resource_group
- Rename variable:
  - resourcegroup -> resource_group
- Rename output variable:
  - subscriptionId -> subscription_id'

---

## Module: azure-bastion
## [0.11.0](https://github.com/CloudNationHQ/terraform-azure-bastion/releases/tag/v0.11.0)


### Features

* added code of conduct and security documentation ([#43](https://github.com/CloudNationHQ/terraform-azure-bastion/issues/43)) ([8a03000](https://github.com/CloudNationHQ/terraform-azure-bastion/commit/8a03000bb9d8acfca309125a6cf54f439be7f1d9))

---

## Module: azure-mysql
## [0.2.1](https://github.com/CloudNationHQ/terraform-azure-mysql/releases/tag/v0.2.1)


### Bug Fixes

* fix wrong module references ([#8](https://github.com/CloudNationHQ/terraform-azure-mysql/issues/8)) ([7ae0cba](https://github.com/CloudNationHQ/terraform-azure-mysql/commit/7ae0cba010e0a2728df6d6fe7067f3f2e280e46a))

---

## Module: azure-plan
## 1.0.0 (2024-08-14)


### Features

* add initial resources ([8811c68](https://github.com/CloudNationHQ/terraform-azure-plan/releases/tag/v1.0.0))

---

