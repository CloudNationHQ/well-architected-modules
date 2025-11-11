---
title: Release Notes for 2025-11-04
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20251104.html
folder: release_notes
---

## Module: azure-sa
## [4.3.0](https://github.com/CloudNationHQ/terraform-azure-sa/releases/tag/v4.3.0)


### Features

* **deps:** bump github.com/cloudnationhq/az-cn-go-validor in /tests ([#188](https://github.com/CloudNationHQ/terraform-azure-sa/issues/188)) ([6b9f74f](https://github.com/CloudNationHQ/terraform-azure-sa/commit/6b9f74f3b27d59258dc5d058e949a4a7ff649f4b))
* **deps:** bump github.com/ulikunitz/xz from 0.5.10 to 0.5.14 in /tests ([#181](https://github.com/CloudNationHQ/terraform-azure-sa/issues/181)) ([f246a3f](https://github.com/CloudNationHQ/terraform-azure-sa/commit/f246a3f8412d1cd45f0e4854a443c341255594d4))
* simplify role assignment by using each value instead of var reference ([#191](https://github.com/CloudNationHQ/terraform-azure-sa/issues/191)) ([b1c8e13](https://github.com/CloudNationHQ/terraform-azure-sa/commit/b1c8e138100cfa477d1864b344c446781cb9fca2))


### Bug Fixes

* replace deprecated property in storage queue ([#189](https://github.com/CloudNationHQ/terraform-azure-sa/issues/189)) ([86bf0b2](https://github.com/CloudNationHQ/terraform-azure-sa/commit/86bf0b2bc967c202a0a462d4fdbead5e7acfec2d))

---

## Module: azure-pdns
## [4.1.0](https://github.com/CloudNationHQ/terraform-azure-pdns/releases/tag/v4.1.0)


### Features

* add missing tags property existing private dns zone ([#74](https://github.com/CloudNationHQ/terraform-azure-pdns/issues/74)) ([58ba453](https://github.com/CloudNationHQ/terraform-azure-pdns/commit/58ba453ca05c5bb4892b6ede3669b81a88926078))

---

## Module: azure-ca
## [4.0.2](https://github.com/CloudNationHQ/terraform-azure-ca/releases/tag/v4.0.2)


### Bug Fixes

* rules and auth dynamic blocks ([#83](https://github.com/CloudNationHQ/terraform-azure-ca/issues/83)) ([4ffdf18](https://github.com/CloudNationHQ/terraform-azure-ca/commit/4ffdf188cd99be2958a6b88b02c6855fde0bc7f0))

---

## Module: azure-ca
## [4.0.1](https://github.com/CloudNationHQ/terraform-azure-ca/releases/tag/v4.0.1)


### Bug Fixes

* type definitions, and non-existent nested paths for scale rules ([#81](https://github.com/CloudNationHQ/terraform-azure-ca/issues/81)) ([f0ffd46](https://github.com/CloudNationHQ/terraform-azure-ca/commit/f0ffd469ae5ad28fa78d1917a972c7fc5ce144c8))

---

## Module: azure-fwp
## [4.0.0](https://github.com/CloudNationHQ/terraform-azure-fwp/releases/tag/v4.0.0)


### ⚠ BREAKING CHANGES

* this change expects to change the existing data structure

### Features

* restructure tls_certificate to include role assignment properties ([#38](https://github.com/CloudNationHQ/terraform-azure-fwp/issues/38)) ([3503be5](https://github.com/CloudNationHQ/terraform-azure-fwp/commit/3503be5a4482e12036bc293b95033fdc8a766f1d))

### Upgrade from v3.2.0 to v4.0.0:

- Update module reference to: version = "~> 4.0"
- The key_vault_id and principal_id properties are moved from config root level into the tls_certificate object.
   - Users must update their variable structure to nest these properties within tls_certificate.

---

## Module: azure-fdfwp
## [2.1.0](https://github.com/CloudNationHQ/terraform-azure-fdfwp/releases/tag/v2.1.0)


### Features

* add missing properties and remove redundant null values ([#28](https://github.com/CloudNationHQ/terraform-azure-fdfwp/issues/28)) ([90f1ed8](https://github.com/CloudNationHQ/terraform-azure-fdfwp/commit/90f1ed840a545d5437d0ac69c122d0c8322585d5))
* **deps:** bump github.com/cloudnationhq/az-cn-go-validor in /tests ([#27](https://github.com/CloudNationHQ/terraform-azure-fdfwp/issues/27)) ([e3c8426](https://github.com/CloudNationHQ/terraform-azure-fdfwp/commit/e3c84263437b2616db3f241d4f2233260dce2f08))

---

## Module: azure-cog
## [2.2.0](https://github.com/CloudNationHQ/terraform-azure-cog/releases/tag/v2.2.0)


### Features

* add missing properties and remove redundant null values ([#26](https://github.com/CloudNationHQ/terraform-azure-cog/issues/26)) ([999eb4a](https://github.com/CloudNationHQ/terraform-azure-cog/commit/999eb4ae47805005c7a3a3e96198320ffce070bb))
* **deps:** bump github.com/cloudnationhq/az-cn-go-validor in /tests ([#19](https://github.com/CloudNationHQ/terraform-azure-cog/issues/19)) ([c7de72a](https://github.com/CloudNationHQ/terraform-azure-cog/commit/c7de72a026b5d71164f99aef8200a4a7f8e839b2))
* **deps:** bump github.com/ulikunitz/xz from 0.5.10 to 0.5.14 in /tests ([#16](https://github.com/CloudNationHQ/terraform-azure-cog/issues/16)) ([dd5e64e](https://github.com/CloudNationHQ/terraform-azure-cog/commit/dd5e64e046c594d2c950fd8cb18ddb56c0063248))

---

## Module: azure-vnm
## [1.1.0](https://github.com/CloudNationHQ/terraform-azure-vnm/releases/tag/v1.1.0)


### Features

* add missing properties for routing rule collections ([#7](https://github.com/CloudNationHQ/terraform-azure-vnm/issues/7)) ([3f92180](https://github.com/CloudNationHQ/terraform-azure-vnm/commit/3f921801b6c88d79df8d9e8c9920ff5deab9018b))

---

