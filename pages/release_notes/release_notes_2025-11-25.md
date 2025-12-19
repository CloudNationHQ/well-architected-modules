---
title: Release Notes for 2025-11-25
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20251125.html
folder: release_notes
---

## Module: azure-sql
## [2.1.0](https://github.com/CloudNationHQ/terraform-azure-sql/releases/tag/v2.1.0)


### Features

* **deps:** bump github.com/cloudnationhq/az-cn-go-validor in /tests ([#86](https://github.com/CloudNationHQ/terraform-azure-sql/issues/86)) ([28dcd42](https://github.com/CloudNationHQ/terraform-azure-sql/commit/28dcd428e059a20e3ff99f18161cc15d5a82c46f))
* **deps:** bump github.com/ulikunitz/xz from 0.5.10 to 0.5.14 in /tests ([#81](https://github.com/CloudNationHQ/terraform-azure-sql/issues/81)) ([4f857b7](https://github.com/CloudNationHQ/terraform-azure-sql/commit/4f857b7baae2c815c8d9905e5e9155422b89b776))
* increment all module version examples to the latest ([#88](https://github.com/CloudNationHQ/terraform-azure-sql/issues/88)) ([0b40ebf](https://github.com/CloudNationHQ/terraform-azure-sql/commit/0b40ebfc4069f6fc3bb3f9f8e4ef5381426c7d45))

---

## Module: azure-vwan
## [6.0.0](https://github.com/CloudNationHQ/terraform-azure-vwan/releases/tag/v6.0.0)


### ⚠ BREAKING CHANGES

* Virtual WAN resource address changed from azurerm_virtual_wan.vwan to azurerm_virtual_wan.vwan[vwan]

Secure vhub example contains a more complete picture with firewall collection groups and rules

Existing virtual wan is supported now

### Features

* add support for existing virtual wan resource ([#145](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/145)) ([2ba4a5b](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/2ba4a5b29839f3d5d8feae2841c1653586f5d138))
* **deps:** bump golang.org/x/crypto from 0.36.0 to 0.45.0 in /tests ([#143](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/143)) ([99a6105](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/99a61050495f10a8af52088c398da56f412bc827))
* **deps:** bump golang.org/x/crypto from 0.41.0 to 0.45.0 in /tests ([#147](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/147)) ([103427f](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/103427f56b35e2bfb7bf6727ea662e97f2ed7ab0))

### Upgrade from v5.4.1 to v6.0.0:

- Update module reference to: `version = "~> 6.0"`

---

