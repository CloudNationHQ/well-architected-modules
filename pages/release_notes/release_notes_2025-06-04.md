---
title: Release Notes for 2025-06-04
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250604.html
folder: release_notes
---

## Module: azure-vwan
## [5.0.0](https://github.com/CloudNationHQ/terraform-azure-vwan/releases/tag/v5.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#110](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/110)) ([cc1158b](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/cc1158be75f75de8ae8ca521f57a5fc159c19b16))

### Upgrade from v4.5.0 to v5.0.0:

- Update module reference to: `version = "~> 5.0"`
- The property and variable resource_group is renamed to resource_group_name
- The property address_prefix is renamed to address_cidrs in vpn sites
- The default is changed for device_model in vpn sites
- The routing block structure is changed in connections
- The traffic selector policy block structure is changed in connections

For detailed reference look in the examples

---

