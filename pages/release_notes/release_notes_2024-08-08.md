---
title: Release Notes for 2024-08-08
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20240808.html
folder: release_notes
---

## Module: azure-ca
## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-ca/releases/tag/v1.0.0)


### ⚠ BREAKING CHANGES

* replaced azapi resources for container app jobs with native azurerm_container_app_job native resource

### Features

* update jobs to native azurerm resources ([#27](https://github.com/CloudNationHQ/terraform-azure-ca/issues/27)) ([03f344b](https://github.com/CloudNationHQ/terraform-azure-ca/commit/03f344b5bd2f0c457ecc0b7db7ac01bfe757c4b3))

### Bug Fixes
* make sure that registry block is not required and only create role assignments if scope within registry block is defined

### Upgrade from v0.4.0 to v1.0.0

- Update **module reference** to: `version = "~> 1.0"`
- Rename properties in **environment** object:
   * resourcegroup -> resource_group
   * init_container -> template.init_container
- Rename **variable** (optional):
   * resourcegroup -> resource_group

---

## Module: azure-mysql
## [0.2.0](https://github.com/CloudNationHQ/terraform-azure-mysql/releases/tag/v0.2.0)


### Features

* update documentation ([#4](https://github.com/CloudNationHQ/terraform-azure-mysql/issues/4)) ([2862a14](https://github.com/CloudNationHQ/terraform-azure-mysql/commit/2862a14fcc27cc65db04cf2bcb17b814b737bf84))

---

## Module: azure-mysql
## 0.1.0 (2024-08-08)


### Features

* add initial resources ([#2](https://github.com/CloudNationHQ/terraform-azure-mysql/releases/tag/v0.1.0)) ([b0ffbb8](https://github.com/CloudNationHQ/terraform-azure-mysql/commit/b0ffbb81f101d8e9a8c2dce0ba6cd16060a147e8))

---

