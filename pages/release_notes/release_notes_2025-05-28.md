---
title: Release Notes for 2025-05-28
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250528.html
folder: release_notes
---

## Module: azure-law
## [3.1.0](https://github.com/CloudNationHQ/terraform-azure-law/releases/tag/v3.1.0)


### Features

* update documentation ([#98](https://github.com/CloudNationHQ/terraform-azure-law/issues/98)) ([1a7c1ef](https://github.com/CloudNationHQ/terraform-azure-law/commit/1a7c1ef5237dab8d8e533c4550eabcdfb6969256))

---

## Module: azure-vnet
## [9.1.1](https://github.com/CloudNationHQ/terraform-azure-vnet/releases/tag/v9.1.1)


### Bug Fixes

* increment usage module versions ([#151](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/151)) ([88b8f5a](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/88b8f5a1233c549370e771ee84ee8a50053a913b))

---

## Module: azure-plan
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-plan/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#23](https://github.com/CloudNationHQ/terraform-azure-plan/issues/23)) ([205a9cd](https://github.com/CloudNationHQ/terraform-azure-plan/commit/205a9cdefff5cf94d16d7c2ffbf49f832141ea8a))
* updated documentation
* added type definitions
* added submodule app service environment
* added multiple example usages

### Upgrade from v2.2.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- The property and variable resource_group is renamed to resource_group_name

---

