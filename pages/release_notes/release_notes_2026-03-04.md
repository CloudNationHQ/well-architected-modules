---
title: Release Notes for 2026-03-04
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20260304.html
folder: release_notes
---

## Module: azure-acr
## [5.2.0](https://github.com/CloudNationHQ/terraform-azure-acr/releases/tag/v5.2.0)


### Features

* **deps:** bump github.com/cloudnationhq/az-cn-go-validor in /tests ([#108](https://github.com/CloudNationHQ/terraform-azure-acr/issues/108)) ([12a413a](https://github.com/CloudNationHQ/terraform-azure-acr/commit/12a413ab5bb4bc9ee990d125da403bc8630dcb50))

---

## Module: azure-naming
## [0.26.2](https://github.com/CloudNationHQ/terraform-azure-naming/releases/tag/v0.26.2)

### Enhancements

* add bvault resource ([#93](https://github.com/CloudNationHQ/terraform-azure-naming/issues/93)) ([810048c](https://github.com/CloudNationHQ/terraform-azure-naming/commit/810048c12c06d1126d5a65839964013d2e553abd))
* add backup_policy resource ([#93](https://github.com/CloudNationHQ/terraform-azure-naming/issues/93)) ([810048c](https://github.com/CloudNationHQ/terraform-azure-naming/commit/810048c12c06d1126d5a65839964013d2e553abd))

---

## Module: azure-dbw
## [2.3.1](https://github.com/CloudNationHQ/terraform-azure-dbw/releases/tag/v2.3.1)


### Bug Fixes

* simplify resource group lookup in main.tf and clean up example READMEs ([#21](https://github.com/CloudNationHQ/terraform-azure-dbw/issues/21)) ([0c0567e](https://github.com/CloudNationHQ/terraform-azure-dbw/commit/0c0567ef6326a47317745239415fb1c8bcbc053b))

---

## Module: azure-dbw
## [2.3.0](https://github.com/CloudNationHQ/terraform-azure-dbw/releases/tag/v2.3.0)


### Features

* feat: add enhanced security compliance configuration to Databricks workspace
* feat: enhance README with requirements, inputs, and outputs sections
* feat: add type definitions, readme updates, full refactor

---

## Module: azure-apim
## [3.1.0](https://github.com/CloudNationHQ/terraform-azure-apim/releases/tag/v3.1.0)


### Features

* add optional connection_string to application_insights and update validation logic ([#38](https://github.com/CloudNationHQ/terraform-azure-apim/issues/38)) ([a8e38d3](https://github.com/CloudNationHQ/terraform-azure-apim/commit/a8e38d3ddbd4a0df945994fa93dcea36bfc1d69d))

---

## Module: azure-lb
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-lb/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* breaking schema validations ([#43](https://github.com/CloudNationHQ/terraform-azure-lb/issues/43))
* The data structure changed, causing a recreate on existing resources.

### Features

* add initial resources ([#2](https://github.com/CloudNationHQ/terraform-azure-lb/issues/2)) ([7e28915](https://github.com/CloudNationHQ/terraform-azure-lb/commit/7e28915dba90a0af36b5873f1ca25d6e2e8e7cc6))
* added functionality in nat pools, rules, loadbalancer probes and remove temporary files when deployment tests fails ([#12](https://github.com/CloudNationHQ/terraform-azure-lb/issues/12)) ([3f1b8a6](https://github.com/CloudNationHQ/terraform-azure-lb/commit/3f1b8a64291209225e7aa094c356115d3eb90f69))
* auto generated docs and refine makefile ([#4](https://github.com/CloudNationHQ/terraform-azure-lb/issues/4)) ([39ccc79](https://github.com/CloudNationHQ/terraform-azure-lb/commit/39ccc793e6e24f8344ed08f91bef60c843e5c3c8))
* breaking schema validations ([#43](https://github.com/CloudNationHQ/terraform-azure-lb/issues/43)) ([1e7f834](https://github.com/CloudNationHQ/terraform-azure-lb/commit/1e7f83456a8b6ee9b164b99589a6a5255e97e944))
* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#11](https://github.com/CloudNationHQ/terraform-azure-lb/issues/11)) ([30ab62f](https://github.com/CloudNationHQ/terraform-azure-lb/commit/30ab62f099d2f65cf4d440f30d35480315952bac))
* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#17](https://github.com/CloudNationHQ/terraform-azure-lb/issues/17)) ([a6a0d04](https://github.com/CloudNationHQ/terraform-azure-lb/commit/a6a0d041153df210564e5cf2914e18d4585452c0))
* **deps:** bump golang.org/x/crypto from 0.29.0 to 0.31.0 in /tests ([#15](https://github.com/CloudNationHQ/terraform-azure-lb/issues/15)) ([2e12c5c](https://github.com/CloudNationHQ/terraform-azure-lb/commit/2e12c5cfff5afc7b2481f192f58f80cf14beb48b))
* **deps:** bump golang.org/x/net from 0.31.0 to 0.33.0 in /tests ([#16](https://github.com/CloudNationHQ/terraform-azure-lb/issues/16)) ([5e1b6d3](https://github.com/CloudNationHQ/terraform-azure-lb/commit/5e1b6d3d117bddff37401a2eacf98331fc7fb346))
* **deps:** bump golang.org/x/net from 0.33.0 to 0.36.0 in /tests ([#18](https://github.com/CloudNationHQ/terraform-azure-lb/issues/18)) ([d137c81](https://github.com/CloudNationHQ/terraform-azure-lb/commit/d137c810f138fe61ae4fd0a01218932d2a8ebd7e))
* **deps:** bump golang.org/x/net from 0.36.0 to 0.38.0 in /tests ([#23](https://github.com/CloudNationHQ/terraform-azure-lb/issues/23)) ([a861042](https://github.com/CloudNationHQ/terraform-azure-lb/commit/a86104252935593e591997c3e3f548b68babfd30))
* enhance testing with sequential, parallel modes and flags for exceptions and skip-destroy ([#6](https://github.com/CloudNationHQ/terraform-azure-lb/issues/6)) ([11b0c5e](https://github.com/CloudNationHQ/terraform-azure-lb/commit/11b0c5ea0efad1e952ae126e69cf82094443049c))
* format documentation to include type definitions ([#19](https://github.com/CloudNationHQ/terraform-azure-lb/issues/19)) ([9164c91](https://github.com/CloudNationHQ/terraform-azure-lb/commit/9164c91b1c500957b5ccbb43f6671bfb6fc2086e))
* rename enable_tcp_reset and enable_floating_ip variables ([#41](https://github.com/CloudNationHQ/terraform-azure-lb/issues/41)) ([d0f392a](https://github.com/CloudNationHQ/terraform-azure-lb/commit/d0f392a8eb9345750c180c1c46e1a2476b8c214c))
* small refactor ([#24](https://github.com/CloudNationHQ/terraform-azure-lb/issues/24)) ([895ca86](https://github.com/CloudNationHQ/terraform-azure-lb/commit/895ca869d8c8d3bbb30651225243c32bab4d030b))


### Bug Fixes

* bounced all modules to latest verion in usages ([#8](https://github.com/CloudNationHQ/terraform-azure-lb/issues/8)) ([5cd2956](https://github.com/CloudNationHQ/terraform-azure-lb/commit/5cd2956f316ac2a2f6ca2fa662944b1bd495041c))
* fix submodule generation from makefile ([#21](https://github.com/CloudNationHQ/terraform-azure-lb/issues/21)) ([be20946](https://github.com/CloudNationHQ/terraform-azure-lb/commit/be2094682b1a5e0290dfe65fd59a0eb1933207ad))
* improve variable type definitions and add validation rules ([#29](https://github.com/CloudNationHQ/terraform-azure-lb/issues/29)) ([71e2bc2](https://github.com/CloudNationHQ/terraform-azure-lb/commit/71e2bc2039d41df96ffb6442df989e120146948b))

---

## Module: azure-pim
## [1.0.1](https://github.com/CloudNationHQ/terraform-azure-pim/releases/tag/v1.0.1)


### Bug Fixes

* correct require_approval property for activation_rules ([fe17efc](https://github.com/CloudNationHQ/terraform-azure-pim/commit/fe17efc5e060cdace33633822833c1e2ec718789))
* correct require_approval property for activation_rules ([35d80e2](https://github.com/CloudNationHQ/terraform-azure-pim/commit/35d80e25fcdec47bfdbbc5d6b3a87fa6bff4ba52))

---

## Module: azure-vnm
## [1.2.0](https://github.com/CloudNationHQ/terraform-azure-vnm/releases/tag/v1.2.0)


### Features

* update naming module version to 0.26 and add member_type to network groups ([#13](https://github.com/CloudNationHQ/terraform-azure-vnm/issues/13)) ([a7b21e5](https://github.com/CloudNationHQ/terraform-azure-vnm/commit/a7b21e557f800b52cf51121fbf38c162fb28a80c))

---

## Module: azure-lt
## 1.0.0 (2026-03-04)


### Features

* update dependabot yaml ([473d843](https://github.com/CloudNationHQ/terraform-azure-lt/releases/tag/v1.0.0))

---

