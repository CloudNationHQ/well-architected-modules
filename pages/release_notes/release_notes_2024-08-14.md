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

## Module: azure-plan
## 1.0.0 (2024-08-14)


### Features

* add initial resources ([8811c68](https://github.com/CloudNationHQ/terraform-azure-plan/releases/tag/v1.0.0))

---

