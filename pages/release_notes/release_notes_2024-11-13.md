---
title: Release Notes for 2024-11-13
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20241113.html
folder: release_notes
---

## Module: azure-law
## [2.2.1](https://github.com/CloudNationHQ/terraform-azure-law/releases/tag/v2.2.1)


### Bug Fixes

* fix submodule documentation generation ([#83](https://github.com/CloudNationHQ/terraform-azure-law/issues/83)) ([8b558c8](https://github.com/CloudNationHQ/terraform-azure-law/commit/8b558c8867e1a2a507cabb540cacfffad72aed04))

---

## Module: azure-vnet
## [8.0.2](https://github.com/CloudNationHQ/terraform-azure-vnet/releases/tag/v8.0.2)


### Bug Fixes

* remove time provider ([#109](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/109)) ([2c87fcd](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/2c87fcd4e837ce3c09d6e0fd0d8e6c0e4fce6013))

---

## Module: azure-vnet
## [8.0.1](https://github.com/CloudNationHQ/terraform-azure-vnet/releases/tag/v8.0.1)


### Bug Fixes

* revert several symbolic names and fixed the documentation generation of submodules ([#106](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/106)) ([e77c10e](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/e77c10e65bfeed416cc1f15f3574b79984fa6f0e))

---

## Module: azure-vnet
## [8.0.0](https://github.com/CloudNationHQ/terraform-azure-vnet/releases/tag/v8.0.0)


### ⚠ BREAKING CHANGES

  - updated `cidr` attribute to `address_space` for vnet
  - updated `cidr` attribute to `address_prefixes` for subnet
  - removed submodule vhub-connection
  - added submodule vnet-peering
  - updated README's and examples accordingly. 
 ([#104](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/104))

**Upgrade from v7 to v8**
- Update module reference to: `version = "~> 8.0"`
- Rename property in `var.vnet` object:
`cidr` -> `address_space`
- Rename property in `var.vnet.subnets` object:
`cidr `-> `address_prefixes`
- Remove any reference to vhub-connection submodule which can be found under the vwan module now.

---

## Module: azure-vm
## [4.2.1](https://github.com/CloudNationHQ/terraform-azure-vm/releases/tag/v4.2.1)


### Bug Fixes

* fix submodule documentation generation ([#148](https://github.com/CloudNationHQ/terraform-azure-vm/issues/148)) ([b391f15](https://github.com/CloudNationHQ/terraform-azure-vm/commit/b391f15461e32eaf821c4c13a62cbcfa4897283b))

---

## Module: azure-vwan
## [3.4.1](https://github.com/CloudNationHQ/terraform-azure-vwan/releases/tag/v3.4.1)


### Bug Fixes

* fix submodule documentation generation ([#75](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/75)) ([186c8ab](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/186c8ab0d2b6083af6922372e8811cc8e7b5b81a))

---

## Module: azure-vwan
## [3.4.0](https://github.com/CloudNationHQ/terraform-azure-vwan/releases/tag/v3.4.0)


### Features

* add vhub-connection submodule including example ([#73](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/73)) ([dc40769](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/dc40769d583f3cd8c9f79237b01e04e9036cced5))

---

## Module: azure-vgw
## [1.2.1](https://github.com/CloudNationHQ/terraform-azure-vgw/releases/tag/v1.2.1)


### Bug Fixes

* fix submodule documentation generation ([#42](https://github.com/CloudNationHQ/terraform-azure-vgw/issues/42)) ([450ec62](https://github.com/CloudNationHQ/terraform-azure-vgw/commit/450ec6250336fce2e3c4f004ac93536e0ae135a3))

---

## Module: azure-sqlmi
## [1.3.0](https://github.com/CloudNationHQ/terraform-azure-sqlmi/releases/tag/v1.3.0)


### Features

* add ad admin support ([#12](https://github.com/CloudNationHQ/terraform-azure-sqlmi/issues/12)) ([9af4896](https://github.com/CloudNationHQ/terraform-azure-sqlmi/commit/9af4896ecd075f9e2d39105e9c5c9408df4fdd86))

---

