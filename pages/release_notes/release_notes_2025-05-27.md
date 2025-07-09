---
title: Releases for 2025-05-27
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 09, 2025
summary: "Releases of the Terraform Well Architected Modules 2025-05-27"
sidebar: mydoc_sidebar
permalink: release_notes_20250527.html
folder: release_notes
---

# Release Notes for 2025-05-27

## azure-vnet
### v9.1.0 (v9.1.0)
**Published at:** 2025-05-27T14:58:37Z

## [9.1.0](https://github.com/CloudNationHQ/terraform-azure-vnet/compare/v9.0.0...v9.1.0) (2025-05-27)


### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#147](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/147)) ([3617092](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/36170923ee91c07d0e2555fcb4118a217a8c32c6))

---

## azure-vnet
### v9.0.0 (v9.0.0)
**Published at:** 2025-05-27T14:55:09Z

## [9.0.0](https://github.com/CloudNationHQ/terraform-azure-vnet/compare/v8.5.0...v9.0.0) (2025-05-27)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#148](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/148)) ([f41cfee](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/f41cfee39502a094f2d598979555a9b482c8e5f7))
* type definitions are added
* documentation is updated
* some logic is simplified regarding existing virtual network

### Upgrade from v8.5.0 to v9.0.0:

- Update module reference to: `version = "~> 9.0"`
- The property and variable resource_group is renamed to resource_group_name
- The fallback peering names are changed in the submodule peering

---

## azure-func
### v2.1.0 (v2.1.0)
**Published at:** 2025-05-27T14:58:04Z

## [2.1.0](https://github.com/CloudNationHQ/terraform-azure-func/compare/v2.0.0...v2.1.0) (2025-05-27)


### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#51](https://github.com/CloudNationHQ/terraform-azure-func/issues/51)) ([6c0e1a9](https://github.com/CloudNationHQ/terraform-azure-func/commit/6c0e1a9b208e4497ac47aecae029bf15ef375beb))

---

## azure-func
### v2.0.0 (v2.0.0)
**Published at:** 2025-05-27T11:17:38Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-func/compare/v1.8.1...v2.0.0) (2025-05-27)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#52](https://github.com/CloudNationHQ/terraform-azure-func/issues/52)) ([4a5f61e](https://github.com/CloudNationHQ/terraform-azure-func/commit/4a5f61e121e048520d849e119a2438ac65cf5e9a))
- updated documentation
- added missing properties in type definition
- corrected some mistakes in the usages
- added 3 tier strategy naming

### Upgrade from v1.8.1 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The property and variable resource_group is renamed to resource_group_name

---

