---
title: Releases for 2024-10-10
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Mar 20, 2025
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20241010.html
folder: release_notes
---

# Release Notes for 2024-10-10

## azure-vnet
### v6.0.0 (v6.0.0)
**Published at:** 2024-10-10T10:44:12Z

## [6.0.0](https://github.com/CloudNationHQ/terraform-azure-vnet/compare/v5.0.1...v6.0.0) (2024-10-10)


### ⚠ BREAKING CHANGES

* data structure has changed due to renaming of properties.

### Features

* aligned route table properties ([#92](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/92)) ([5a61ce4](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/5a61ce4b244b32dfc06474a192be38a36f487d3b))

### Upgrade from v5.0.1 to v6.0.0:

- Update module reference to: `version = "~> 6.0"`
- Rename properties in vnet object:
  - within subnets the shared route_table property has been renamed to route_table_shared
  - within subnets the individual route property has been renamed to route_table

---

## azure-vnet
### v5.0.1 (v5.0.1)
**Published at:** 2024-10-10T08:27:43Z

## [5.0.1](https://github.com/CloudNationHQ/terraform-azure-vnet/compare/v5.0.0...v5.0.1) (2024-10-10)


### Bug Fixes

* fix vnet dependency order for proper destruction ([#90](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/90)) ([e07d0df](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/e07d0df24e573ec6971bc5d1aeefa54c1973aab6))

---

