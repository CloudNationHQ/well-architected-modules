---
title: Release Notes for 2024-10-10
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20241010.html
folder: release_notes
---

## Module: azure-vnet
## [6.0.0](https://github.com/CloudNationHQ/terraform-azure-vnet/releases/tag/v6.0.0)


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

**Published at:** 2024-10-10T10:44:12Z

## Module: azure-vnet
## [5.0.1](https://github.com/CloudNationHQ/terraform-azure-vnet/releases/tag/v5.0.1)


### Bug Fixes

* fix vnet dependency order for proper destruction ([#90](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/90)) ([e07d0df](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/e07d0df24e573ec6971bc5d1aeefa54c1973aab6))

---

**Published at:** 2024-10-10T08:27:43Z

