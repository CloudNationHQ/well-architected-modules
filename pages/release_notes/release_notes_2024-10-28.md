---
title: Release Notes for 2024-10-28
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20241028.html
folder: release_notes
---

## Module: azure-vnet
## [7.0.1](https://github.com/CloudNationHQ/terraform-azure-vnet/releases/tag/v7.0.1)


### Bug Fixes

* remove parallelism limitation from tests ([#98](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/98)) ([c969d29](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/c969d29baeab7c90c7a294c7fbc5870a1d4bc072))

---

## Module: azure-vwan
## [3.1.0](https://github.com/CloudNationHQ/terraform-azure-vwan/releases/tag/v3.1.0)


### Features

* add virtual hub security partner provider support ([#66](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/66)) ([dc0dcb6](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/dc0dcb6890140d59153598ba7a23cc03a3f4b5a8))
* add vpn gateway nat rules support ([#68](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/68)) ([270b549](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/270b549f03103f3aef5647d9a7bcae93b6650cd1))

---

## Module: azure-vwan
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-vwan/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* the data structure has been updated to reflect changes in vpn functionality

### Features

* add point to site vpn support ([#64](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/64)) ([88190e6](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/88190e611a1870672c5f678a6693c5a802f31dd6))

### Upgrade from v2.1.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- Rename properties in vwan object:
  - within virtual hubs, vpn_gateway has been renamed to site_to_site_vpn to accommodate the option of utilizing point_to_site_vpn as well

---

## Module: azure-alerts
## [1.0.1](https://github.com/CloudNationHQ/terraform-azure-alerts/releases/tag/v1.0.1)


### Bug Fixes

* removed the provider in modules([#5](https://github.com/CloudNationHQ/terraform-azure-alerts/issues/5)) ([2300953](https://github.com/CloudNationHQ/terraform-azure-alerts/commit/2300953d7c895e61a6e0f3a91b5b786c87c9d715))

---

