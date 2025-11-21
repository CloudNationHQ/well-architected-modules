---
title: Release Notes for 2025-11-21
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20251121.html
folder: release_notes
---

## Module: azure-vgw
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-vgw/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* this change expects to change the existing data structure

Unneeded null values are removed in the type definitions and sa_datasize, sa_lifetime properties are added to local gateway connections. 

A minimal usage example is added and updated all documentation.

Public ip resource moved to a dedicated module.

### Features

* **deps:** bump github.com/cloudnationhq/az-cn-go-validor in /tests ([#73](https://github.com/CloudNationHQ/terraform-azure-vgw/issues/73)) ([5cbf216](https://github.com/CloudNationHQ/terraform-azure-vgw/commit/5cbf2161d8ecba9aab3e506b1caea5381af68a63))
* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#63](https://github.com/CloudNationHQ/terraform-azure-vgw/issues/63)) ([58b83fe](https://github.com/CloudNationHQ/terraform-azure-vgw/commit/58b83fefa8344f87411f2c580cab45db46ffe6ea))
* **deps:** bump github.com/ulikunitz/xz from 0.5.10 to 0.5.14 in /tests ([#69](https://github.com/CloudNationHQ/terraform-azure-vgw/issues/69)) ([4970ae0](https://github.com/CloudNationHQ/terraform-azure-vgw/commit/4970ae0cda2e42ac4b39a2db460e55468723bc8d))
* **deps:** bump golang.org/x/crypto from 0.36.0 to 0.45.0 in /tests ([#74](https://github.com/CloudNationHQ/terraform-azure-vgw/issues/74)) ([037a66d](https://github.com/CloudNationHQ/terraform-azure-vgw/commit/037a66ddf6b925174099e9879736cc06400a41c5))
* remove public ip resource ([#75](https://github.com/CloudNationHQ/terraform-azure-vgw/issues/75)) ([a859dab](https://github.com/CloudNationHQ/terraform-azure-vgw/commit/a859dab8129041c64ae6c5f5fe9b97b2bbf85016))

### Upgrade from v2.0.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- Public ip resource is moved to a dedicated module. See the usage examples for details

---

