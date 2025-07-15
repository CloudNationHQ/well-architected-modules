---
title: Release Notes for 2025-05-22
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250522.html
folder: release_notes
---

## Module: azure-vwan
## [4.4.0](https://github.com/CloudNationHQ/terraform-azure-vwan/releases/tag/v4.4.0)


### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#101](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/101)) ([5dd1350](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/5dd13501b379d76e1e1010bb4210f0f5e3eb3b37))

---

## Module: azure-vgw
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-vgw/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#64](https://github.com/CloudNationHQ/terraform-azure-vgw/issues/64)) ([784cfa2](https://github.com/CloudNationHQ/terraform-azure-vgw/commit/784cfa2ab2284974a5291be9a46884af68f867c6))

### Upgrade from v1.4.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The property and variable resource_group is renamed to resource_group_name

---

