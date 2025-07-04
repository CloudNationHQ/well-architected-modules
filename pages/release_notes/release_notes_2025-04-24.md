---
title: Releases for 2025-04-24
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 04, 2025
summary: "Releases of the Terraform Well Architected Modules 2025-04-24"
sidebar: mydoc_sidebar
permalink: release_notes_20250424.html
folder: release_notes
---

# Release Notes for 2025-04-24

## azure-vm
### v6.1.0 (v6.1.0)
**Published at:** 2025-04-24T13:06:34Z

## [6.1.0](https://github.com/CloudNationHQ/terraform-azure-vm/compare/v6.0.0...v6.1.0) (2025-04-24)


### Features

* **deps:** bump golang.org/x/crypto from 0.32.0 to 0.35.0 in /tests ([#191](https://github.com/CloudNationHQ/terraform-azure-vm/issues/191)) ([8d6ec4c](https://github.com/CloudNationHQ/terraform-azure-vm/commit/8d6ec4c86fa5d637276a11a8d19cc2d6cb138744))
* **deps:** bump golang.org/x/net from 0.34.0 to 0.38.0 in /tests ([#192](https://github.com/CloudNationHQ/terraform-azure-vm/issues/192)) ([650abad](https://github.com/CloudNationHQ/terraform-azure-vm/commit/650abadce5af07a7476448d9603be89408df794e))

---

## azure-vm
### v6.0.0 (v6.0.0)
**Published at:** 2025-04-24T12:55:15Z

## [6.0.0](https://github.com/CloudNationHQ/terraform-azure-vm/compare/v5.2.0...v6.0.0) (2025-04-24)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* add type definitions and small refactor ([#193](https://github.com/CloudNationHQ/terraform-azure-vm/issues/193)) ([c3be1e5](https://github.com/CloudNationHQ/terraform-azure-vm/commit/c3be1e5e76c97251ca9dbab95af52d98b637c427))

### Upgrade from v5.2.0 to v6.0.0:

- Update module reference to: `version = "~> 6.0"`
- The user assigned identity is removed from the module and it is not set to system assigned default anymore as well.
  - For identity we created a separate module as shown in the examples.
- The property and variable resource_group is renamed to resource_group_name
- The property subnet is changed to subnet_id and placed in ip configurations
- The structure changed abit when ssh keys or passwords are generated within the module itself as shown in the examples.

---

