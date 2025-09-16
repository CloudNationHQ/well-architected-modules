---
title: Release Notes for 2025-09-10
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250910.html
folder: release_notes
---

## Module: azure-vnet
## [9.5.0](https://github.com/CloudNationHQ/terraform-azure-vnet/releases/tag/v9.5.0)


### Features

* increment validor package and update documentation ([#191](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/191)) ([b9ef6bb](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/b9ef6bbfe371d8c1e380b788927228b74a68418f))


### Bug Fixes

* allow same NSG rule priority across different directions ([#194](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/194)) ([9989cbd](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/9989cbddf11e1ae71d39d573df7d05f99ff44fd0))

---

## Module: azure-cosmosdb
## [4.0.0](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/releases/tag/v4.0.0)


### ⚠ BREAKING CHANGES

* this change causes recreates

### Features

* add type definitions and changed data structure ([#95](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/issues/95)) ([2ca31fd](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/commit/2ca31fd8d9088017f4975d445ab287cc6dbd86be))
* **deps:** bump github.com/ulikunitz/xz from 0.5.10 to 0.5.14 in /tests ([#94](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/issues/94)) ([93c49ba](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/commit/93c49baab720255748123bdee370e2aa10602c03))

### Upgrade from v3.6.0 to v4.0.0:

- Update module reference to: `version = "~> 4.0"`
- The property and variable resource_group is renamed to resource_group_name

---

