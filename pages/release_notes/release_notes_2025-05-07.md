---
title: Release Notes for 2025-05-07
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250507.html
folder: release_notes
---

## Module: azure-sa
## [4.0.0](https://github.com/CloudNationHQ/terraform-azure-sa/releases/tag/v4.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#170](https://github.com/CloudNationHQ/terraform-azure-sa/issues/170)) ([a0a2dd8](https://github.com/CloudNationHQ/terraform-azure-sa/commit/a0a2dd8f86d1c112af8f7fee501fabe281d2eab4))

### Upgrade from v3.7.1 to v4.0.0:

- Update module reference to: `version = "~> 4.0"`
- The user assigned identity is removed from the module.
  - For identity we created a separate module as shown in the examples.
- The property and variable resource_group is renamed to resource_group_name

---

## Module: azure-sql
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-sql/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* add type definitions and small refactor ([#73](https://github.com/CloudNationHQ/terraform-azure-sql/issues/73)) ([7a21e2f](https://github.com/CloudNationHQ/terraform-azure-sql/commit/7a21e2f77bd7c3958b9611d8eb49c65d375563e5))

### Upgrade from v1.5.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The user assigned identity is removed from the module.
  - For identity we created a separate module as shown in the examples.
- The property and variable resource_group is renamed to resource_group_name

---

