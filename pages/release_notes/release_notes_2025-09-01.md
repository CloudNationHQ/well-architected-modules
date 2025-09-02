---
title: Release Notes for 2025-09-01
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250901.html
folder: release_notes
---

## Module: azure-kv
## [4.2.1](https://github.com/CloudNationHQ/terraform-azure-kv/releases/tag/v4.2.1)


### Bug Fixes

* update to lookup ([#118](https://github.com/CloudNationHQ/terraform-azure-kv/issues/118)) ([7bbffbf](https://github.com/CloudNationHQ/terraform-azure-kv/commit/7bbffbf67ef251b9d55211b18c185e2d1d015dbd))

---

## Module: azure-app
## [4.0.3](https://github.com/CloudNationHQ/terraform-azure-app/releases/tag/v4.0.3)


### Bug Fixes

* correct variable names and type definition ([#50](https://github.com/CloudNationHQ/terraform-azure-app/issues/50)) ([0158bdd](https://github.com/CloudNationHQ/terraform-azure-app/commit/0158bdd15150855e7d8ca3a4670f377288288c6c))

---

## Module: azure-appi
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-appi/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* this change causes recreates

### Features

* add type definitions and changed data structure ([#27](https://github.com/CloudNationHQ/terraform-azure-appi/issues/27)) ([1b4c499](https://github.com/CloudNationHQ/terraform-azure-appi/commit/1b4c499a25bff366595f3651a14f980f2b3f0d88))

### Upgrade from v2.5.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- The property and variable resource_group is renamed to resource_group_name

---

