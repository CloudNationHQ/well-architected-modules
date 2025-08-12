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

