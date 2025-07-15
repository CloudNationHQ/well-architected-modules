---
title: Release Notes for 2025-05-02
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250502.html
folder: release_notes
---

## Module: azure-kv
## [4.0.0](https://github.com/CloudNationHQ/terraform-azure-kv/releases/tag/v4.0.0)


### ⚠ BREAKING CHANGES

* add type definitions, updated properties ([#103](https://github.com/CloudNationHQ/terraform-azure-kv/issues/103))

### Features

* add type definitions, updated properties ([#103](https://github.com/CloudNationHQ/terraform-azure-kv/issues/103)) ([156bb73](https://github.com/CloudNationHQ/terraform-azure-kv/commit/156bb73a5f865eb67b42169cba61840e7ef098f3))

### Upgrade from v3.x to v4.0.0:
* Update module reference to: `version = "~> 4.0"`
* The property and variable `resource_group` is renamed to `resource_group_name`
* To prevent the `Key Vault Administrator` role assignment from being assigned, set `enable_role_assignment = false`
* See access policies example, to use the Key Vault Access policies instead of RBAC.

---

## Module: azure-mysql
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-mysql/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* add missing properties ([#32](https://github.com/CloudNationHQ/terraform-azure-mysql/issues/32)) ([7ce4a0f](https://github.com/CloudNationHQ/terraform-azure-mysql/commit/7ce4a0f4e348b39248d898ff72792e7de0d122a5))
* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#24](https://github.com/CloudNationHQ/terraform-azure-mysql/issues/24)) ([50f9e8d](https://github.com/CloudNationHQ/terraform-azure-mysql/commit/50f9e8d6367daeb565ad9a91f4023f7a36fb129a))
* **deps:** bump golang.org/x/crypto from 0.31.0 to 0.35.0 in /tests ([#27](https://github.com/CloudNationHQ/terraform-azure-mysql/issues/27)) ([ad25c27](https://github.com/CloudNationHQ/terraform-azure-mysql/commit/ad25c271b52da350cd414f4ec74d871367c3d64e))
* **deps:** bump golang.org/x/net from 0.33.0 to 0.38.0 in /tests ([#28](https://github.com/CloudNationHQ/terraform-azure-mysql/issues/28)) ([f20a007](https://github.com/CloudNationHQ/terraform-azure-mysql/commit/f20a007d2010327fa4bcdf1bc4a01c5ad0cb0862))

---

## Module: azure-mysql
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-mysql/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* add type definitions and small refactor ([#29](https://github.com/CloudNationHQ/terraform-azure-mysql/issues/29)) ([251c641](https://github.com/CloudNationHQ/terraform-azure-mysql/commit/251c6419ac8389b235893dd4ca419c3f002b02f0))

### Upgrade from v1.2.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The user assigned identity is removed from the module.
  - For identity we created a separate module as shown in the examples.
- The property and variable resource_group is renamed to resource_group_name

---

