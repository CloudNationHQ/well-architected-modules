---
title: Releases for 2025-05-22
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 01, 2025
summary: "Releases of the Terraform Well Architected Modules 2025-05-22"
sidebar: mydoc_sidebar
permalink: release_notes_20250522.html
folder: release_notes
---

# Release Notes for 2025-05-22

## azure-vwan
### v4.4.0 (v4.4.0)
**Published at:** 2025-05-22T13:38:45Z

## [4.4.0](https://github.com/CloudNationHQ/terraform-azure-vwan/compare/v4.3.0...v4.4.0) (2025-05-22)


### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#101](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/101)) ([5dd1350](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/5dd13501b379d76e1e1010bb4210f0f5e3eb3b37))

---

## azure-vgw
### v2.0.0 (v2.0.0)
**Published at:** 2025-05-22T13:26:21Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-vgw/compare/v1.4.0...v2.0.0) (2025-05-22)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#64](https://github.com/CloudNationHQ/terraform-azure-vgw/issues/64)) ([784cfa2](https://github.com/CloudNationHQ/terraform-azure-vgw/commit/784cfa2ab2284974a5291be9a46884af68f867c6))

### Upgrade from v1.4.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The property and variable resource_group is renamed to resource_group_name

---

