---
title: Release Notes for 2025-07-09
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250709.html
folder: release_notes
---

## Module: azure-vnet
## [9.2.3](https://github.com/CloudNationHQ/terraform-azure-vnet/releases/tag/v9.2.3)


### Bug Fixes

* provide fallback for if var.naming.network_security_group_rule is not set, so that it no longer ignores nsg rules when only names are provided due to the coalesce function ([#163](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/163)) ([2ced5cc](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/2ced5cc581e01c7e76f527502d76f41f29141ec4))

---

## Module: infoblox-allocation
## [1.2.1](https://github.com/CloudNationHQ/terraform-infoblox-allocation/releases/tag/v1.2.1)


### Bug Fixes

* parent cidr reference ([#10](https://github.com/CloudNationHQ/terraform-infoblox-allocation/issues/10)) ([89c531b](https://github.com/CloudNationHQ/terraform-infoblox-allocation/commit/89c531b1417191b6964a52ebd219473acc2c7ff0))

---

## Module: infoblox-allocation
## [1.2.0](https://github.com/CloudNationHQ/terraform-infoblox-allocation/releases/tag/v1.2.0)

### Bug Fixes

* remove unused outputs ([#5](https://github.com/CloudNationHQ/terraform-infoblox-allocation/issues/5)) ([9840095](https://github.com/CloudNationHQ/terraform-infoblox-allocation/commit/9840095a6e0486838b403cfcd17b970ecd76e2df))
* remove unused variables ([#7](https://github.com/CloudNationHQ/terraform-infoblox-allocation/issues/7)) ([098bf97](https://github.com/CloudNationHQ/terraform-infoblox-allocation/commit/098bf97fc995d7dd30bd9975a5c3157621188946))

---

## Module: infoblox-allocation
## [1.1.1](https://github.com/CloudNationHQ/terraform-infoblox-allocation/releases/tag/v1.1.1)


### Bug Fixes

* remove unused outputs ([#5](https://github.com/CloudNationHQ/terraform-infoblox-allocation/issues/5)) ([9840095](https://github.com/CloudNationHQ/terraform-infoblox-allocation/commit/9840095a6e0486838b403cfcd17b970ecd76e2df))

---

## Module: infoblox-allocation
## [1.1.0](https://github.com/CloudNationHQ/terraform-infoblox-allocation/releases/tag/v1.1.0)


### Features

* update documentation ([#3](https://github.com/CloudNationHQ/terraform-infoblox-allocation/issues/3)) ([271a09c](https://github.com/CloudNationHQ/terraform-infoblox-allocation/commit/271a09c48541b99050919309cbc340023369c291))

---

## Module: infoblox-allocation
## 1.0.0 (2025-07-09)


### Features

* add initial files ([#1](https://github.com/CloudNationHQ/terraform-infoblox-allocation/releases/tag/v1.0.0)) ([bd8e978](https://github.com/CloudNationHQ/terraform-infoblox-allocation/commit/bd8e978c401f79bfad13d4432e6722d2c9dda8a5))

---

