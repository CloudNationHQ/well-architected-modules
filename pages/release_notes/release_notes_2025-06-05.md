---
title: Release Notes for 2025-06-05
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250605.html
folder: release_notes
---

## Module: azure-mysql
## [3.1.1](https://github.com/CloudNationHQ/terraform-azure-mysql/releases/tag/v3.1.1)


### Bug Fixes

* Change default values for create_mode and version ([#37](https://github.com/CloudNationHQ/terraform-azure-mysql/issues/37)) ([0748e96](https://github.com/CloudNationHQ/terraform-azure-mysql/commit/0748e96c2570f7d936529e5eeaaef018ef272503))

---

## Module: azure-fwp
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-fwp/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#18](https://github.com/CloudNationHQ/terraform-azure-fwp/issues/18)) ([63643d5](https://github.com/CloudNationHQ/terraform-azure-fwp/commit/63643d5998a3aee6a81e1decd92bb99c83d3efe5))
* enhance role assignment with additional parameters and tags ([#19](https://github.com/CloudNationHQ/terraform-azure-fwp/issues/19)) ([e6df8aa](https://github.com/CloudNationHQ/terraform-azure-fwp/commit/e6df8aaba63c7a66462a5ca29f0d7256583df50b))
* small refactor ([#27](https://github.com/CloudNationHQ/terraform-azure-fwp/issues/27)) ([558106d](https://github.com/CloudNationHQ/terraform-azure-fwp/commit/558106d8b9edb1e4782b8b25838970583d079cac))

### Upgrade from v2.3.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- The property and variable resource_group is renamed to resource_group_name
- The user assigned identity resource is removed, there is a dedicated module for this

---

## Module: azure-wafwp
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-wafwp/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#26](https://github.com/CloudNationHQ/terraform-azure-wafwp/issues/26)) ([3fba466](https://github.com/CloudNationHQ/terraform-azure-wafwp/commit/3fba466d993e315f81121d4819e8c27bcd751e1c))

### Upgrade from v1.3.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The property and variable resource_group is renamed to resource_group_name
- The rule set version default is changed. It should be set in the config now, since we support different types

---

