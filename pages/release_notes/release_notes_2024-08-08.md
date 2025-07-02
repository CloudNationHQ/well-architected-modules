---
title: Releases for 2024-08-08
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 02, 2025
summary: "Releases of the Terraform Well Architected Modules 2024-08-08"
sidebar: mydoc_sidebar
permalink: release_notes_20240808.html
folder: release_notes
---

# Release Notes for 2024-08-08

## azure-ca
### v1.0.0 (v1.0.0)
**Published at:** 2024-08-08T12:21:03Z

## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-ca/compare/v0.4.0...v1.0.0) (2024-08-08)


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

## azure-mysql
### v0.2.0 (v0.2.0)
**Published at:** 2024-08-08T13:33:54Z

## [0.2.0](https://github.com/CloudNationHQ/terraform-azure-mysql/compare/v0.1.0...v0.2.0) (2024-08-08)


### Features

* update documentation ([#4](https://github.com/CloudNationHQ/terraform-azure-mysql/issues/4)) ([2862a14](https://github.com/CloudNationHQ/terraform-azure-mysql/commit/2862a14fcc27cc65db04cf2bcb17b814b737bf84))

---

## azure-mysql
### v0.1.0 (v0.1.0)
**Published at:** 2024-08-08T11:45:37Z

## 0.1.0 (2024-08-08)


### Features

* add initial resources ([#2](https://github.com/CloudNationHQ/terraform-azure-mysql/issues/2)) ([b0ffbb8](https://github.com/CloudNationHQ/terraform-azure-mysql/commit/b0ffbb81f101d8e9a8c2dce0ba6cd16060a147e8))

---

