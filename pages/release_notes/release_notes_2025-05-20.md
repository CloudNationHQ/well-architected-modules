---
title: Release Notes for 2025-05-20
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250520.html
folder: release_notes
---

## Module: azure-bastion
## [4.0.0](https://github.com/CloudNationHQ/terraform-azure-bastion/releases/tag/v4.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* add type definitions ([#78](https://github.com/CloudNationHQ/terraform-azure-bastion/issues/78)) ([1615ca4](https://github.com/CloudNationHQ/terraform-azure-bastion/commit/1615ca419e0b1a1834a626628ab28cf8291d0a69))

### Upgrade from v3.2.0 to v4.0.0:

- Update module reference to: `version = "~> 4.0"`
- The property and variable resource_group is renamed to resource_group_name

---

## Module: azure-rsv
## [2.1.0](https://github.com/CloudNationHQ/terraform-azure-rsv/releases/tag/v2.1.0)


### Features

* implement flexible resource naming ([#53](https://github.com/CloudNationHQ/terraform-azure-rsv/issues/53)) ([57bd89f](https://github.com/CloudNationHQ/terraform-azure-rsv/commit/57bd89ffc49f9da3219dcf6ae12b94818f3bbe3e))

---

