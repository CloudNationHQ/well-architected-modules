---
title: Release Notes for 2025-05-14
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250514.html
folder: release_notes
---

## Module: azure-evh
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-evh/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#65](https://github.com/CloudNationHQ/terraform-azure-evh/issues/65)) ([5eea02c](https://github.com/CloudNationHQ/terraform-azure-evh/commit/5eea02c39068261b2adfc4e31dcacfd16069bbe6))

### Upgrade from v2.4.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- The property and variable resource_group is renamed to resource_group_name

---

## Module: azure-rsv
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-rsv/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#51](https://github.com/CloudNationHQ/terraform-azure-rsv/issues/51)) ([03847c8](https://github.com/CloudNationHQ/terraform-azure-rsv/commit/03847c8f2d0990747333f5dbe87023913ab12827))

### Upgrade from v1.6.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The property and variable resource_group is renamed to resource_group_name

---

