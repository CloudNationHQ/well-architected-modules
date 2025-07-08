---
title: Releases for 2025-05-28
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 08, 2025
summary: "Releases of the Terraform Well Architected Modules 2025-05-28"
sidebar: mydoc_sidebar
permalink: release_notes_20250528.html
folder: release_notes
---

# Release Notes for 2025-05-28

## azure-law
### v3.1.0 (v3.1.0)
**Published at:** 2025-05-28T08:26:29Z

## [3.1.0](https://github.com/CloudNationHQ/terraform-azure-law/compare/v3.0.0...v3.1.0) (2025-05-28)


### Features

* update documentation ([#98](https://github.com/CloudNationHQ/terraform-azure-law/issues/98)) ([1a7c1ef](https://github.com/CloudNationHQ/terraform-azure-law/commit/1a7c1ef5237dab8d8e533c4550eabcdfb6969256))

---

## azure-vnet
### v9.1.1 (v9.1.1)
**Published at:** 2025-05-28T08:19:59Z

## [9.1.1](https://github.com/CloudNationHQ/terraform-azure-vnet/compare/v9.1.0...v9.1.1) (2025-05-28)


### Bug Fixes

* increment usage module versions ([#151](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/151)) ([88b8f5a](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/88b8f5a1233c549370e771ee84ee8a50053a913b))

---

## azure-plan
### v3.0.0 (v3.0.0)
**Published at:** 2025-05-28T09:45:05Z

## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-plan/compare/v2.2.0...v3.0.0) (2025-05-28)


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

