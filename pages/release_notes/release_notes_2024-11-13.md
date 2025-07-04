---
title: Releases for 2024-11-13
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 04, 2025
summary: "Releases of the Terraform Well Architected Modules 2024-11-13"
sidebar: mydoc_sidebar
permalink: release_notes_20241113.html
folder: release_notes
---

# Release Notes for 2024-11-13

## azure-law
### v2.2.1 (v2.2.1)
**Published at:** 2024-11-13T16:41:07Z

## [2.2.1](https://github.com/CloudNationHQ/terraform-azure-law/compare/v2.2.0...v2.2.1) (2024-11-13)


### Bug Fixes

* fix submodule documentation generation ([#83](https://github.com/CloudNationHQ/terraform-azure-law/issues/83)) ([8b558c8](https://github.com/CloudNationHQ/terraform-azure-law/commit/8b558c8867e1a2a507cabb540cacfffad72aed04))

---

## azure-vnet
### v8.0.2 (v8.0.2)
**Published at:** 2024-11-13T17:04:34Z

## [8.0.2](https://github.com/CloudNationHQ/terraform-azure-vnet/compare/v8.0.1...v8.0.2) (2024-11-13)


### Bug Fixes

* remove time provider ([#109](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/109)) ([2c87fcd](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/2c87fcd4e837ce3c09d6e0fd0d8e6c0e4fce6013))

---

## azure-vnet
### v8.0.1 (v8.0.1)
**Published at:** 2024-11-13T13:18:53Z

## [8.0.1](https://github.com/CloudNationHQ/terraform-azure-vnet/compare/v8.0.0...v8.0.1) (2024-11-13)


### Bug Fixes

* revert several symbolic names and fixed the documentation generation of submodules ([#106](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/106)) ([e77c10e](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/e77c10e65bfeed416cc1f15f3574b79984fa6f0e))

---

## azure-vnet
### v8.0.0 (v8.0.0)
**Published at:** 2024-11-13T11:00:41Z

## [8.0.0](https://github.com/CloudNationHQ/terraform-azure-vnet/compare/v7.1.0...v8.0.0) (2024-11-13)


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

## azure-acr
### v3.2.1 (v3.2.1)
**Published at:** 2024-11-13T16:38:29Z

## [3.2.1](https://github.com/CloudNationHQ/terraform-azure-acr/compare/v3.2.0...v3.2.1) (2024-11-13)


### Bug Fixes

* fix submodule documentation generation ([#72](https://github.com/CloudNationHQ/terraform-azure-acr/issues/72)) ([37eddce](https://github.com/CloudNationHQ/terraform-azure-acr/commit/37eddced492540efa769ae6696f8e3e9f21dbec6))

---

## azure-vm
### v4.2.1 (v4.2.1)
**Published at:** 2024-11-13T16:40:22Z

## [4.2.1](https://github.com/CloudNationHQ/terraform-azure-vm/compare/v4.2.0...v4.2.1) (2024-11-13)


### Bug Fixes

* fix submodule documentation generation ([#148](https://github.com/CloudNationHQ/terraform-azure-vm/issues/148)) ([b391f15](https://github.com/CloudNationHQ/terraform-azure-vm/commit/b391f15461e32eaf821c4c13a62cbcfa4897283b))

---

## azure-vwan
### v3.4.1 (v3.4.1)
**Published at:** 2024-11-13T16:37:02Z

## [3.4.1](https://github.com/CloudNationHQ/terraform-azure-vwan/compare/v3.4.0...v3.4.1) (2024-11-13)


### Bug Fixes

* fix submodule documentation generation ([#75](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/75)) ([186c8ab](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/186c8ab0d2b6083af6922372e8811cc8e7b5b81a))

---

## azure-vwan
### v3.4.0 (v3.4.0)
**Published at:** 2024-11-13T10:42:59Z

## [3.4.0](https://github.com/CloudNationHQ/terraform-azure-vwan/compare/v3.3.0...v3.4.0) (2024-11-13)


### Features

* add vhub-connection submodule including example ([#73](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/73)) ([dc40769](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/dc40769d583f3cd8c9f79237b01e04e9036cced5))

---

## azure-vgw
### v1.2.1 (v1.2.1)
**Published at:** 2024-11-13T16:37:42Z

## [1.2.1](https://github.com/CloudNationHQ/terraform-azure-vgw/compare/v1.2.0...v1.2.1) (2024-11-13)


### Bug Fixes

* fix submodule documentation generation ([#42](https://github.com/CloudNationHQ/terraform-azure-vgw/issues/42)) ([450ec62](https://github.com/CloudNationHQ/terraform-azure-vgw/commit/450ec6250336fce2e3c4f004ac93536e0ae135a3))

---

## azure-aa
### v2.4.1 (v2.4.1)
**Published at:** 2024-11-13T16:39:35Z

## [2.4.1](https://github.com/CloudNationHQ/terraform-azure-aa/compare/v2.4.0...v2.4.1) (2024-11-13)


### Bug Fixes

* fix submodule documentation generation ([#31](https://github.com/CloudNationHQ/terraform-azure-aa/issues/31)) ([219bf70](https://github.com/CloudNationHQ/terraform-azure-aa/commit/219bf7012ff89c5ce05112da1631ca7522b40238))

---

## azure-sqlmi
### v1.3.0 (v1.3.0)
**Published at:** 2024-11-13T11:07:43Z

## [1.3.0](https://github.com/CloudNationHQ/terraform-azure-sqlmi/compare/v1.2.0...v1.3.0) (2024-11-13)


### Features

* add ad admin support ([#12](https://github.com/CloudNationHQ/terraform-azure-sqlmi/issues/12)) ([9af4896](https://github.com/CloudNationHQ/terraform-azure-sqlmi/commit/9af4896ecd075f9e2d39105e9c5c9408df4fdd86))

---

## azure-wafwp
### v1.0.1 (v1.0.1)
**Published at:** 2024-11-13T09:41:17Z

## [1.0.1](https://github.com/CloudNationHQ/terraform-azure-wafwp/compare/v1.0.0...v1.0.1) (2024-11-13)


### Bug Fixes

* fix module references ([#4](https://github.com/CloudNationHQ/terraform-azure-wafwp/issues/4)) ([fca726c](https://github.com/CloudNationHQ/terraform-azure-wafwp/commit/fca726cbcae9afb3bed9bb08fb858a96a9bdcec0))

---

## azure-wafwp
### v1.0.0 (v1.0.0)
**Published at:** 2024-11-13T09:33:14Z

## 1.0.0 (2024-11-13)


### Features

* add initial resources ([#2](https://github.com/CloudNationHQ/terraform-azure-wafwp/issues/2)) ([5e8827d](https://github.com/CloudNationHQ/terraform-azure-wafwp/commit/5e8827d9db2916ed20ca7aabce2bf50c2eb442e5))

---

