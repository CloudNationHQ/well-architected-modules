---
title: Release Notes for 2025-05-08
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250508.html
folder: release_notes
---

## Module: azure-rg
## [2.6.0](https://github.com/CloudNationHQ/terraform-azure-rg/releases/tag/v2.6.0)


### Features

* replace deployment test code with module consumption and fix tags property idempotence ([#55](https://github.com/CloudNationHQ/terraform-azure-rg/issues/55)) ([d24e591](https://github.com/CloudNationHQ/terraform-azure-rg/commit/d24e59195d86992f5211cd9ee359bb6a1aa43f16))

---

## Module: azure-kv
## [4.1.0](https://github.com/CloudNationHQ/terraform-azure-kv/releases/tag/v4.1.0)


### Features

* replace deployment test code with module consumption and generated documentation ([#107](https://github.com/CloudNationHQ/terraform-azure-kv/issues/107)) ([3f861fa](https://github.com/CloudNationHQ/terraform-azure-kv/commit/3f861fabae03430c10a4a061b3e94cec21eefca7))

---

## Module: azure-evh
## [2.4.0](https://github.com/CloudNationHQ/terraform-azure-evh/releases/tag/v2.4.0)


### Features

* add missing properties ([#60](https://github.com/CloudNationHQ/terraform-azure-evh/issues/60)) ([df0330f](https://github.com/CloudNationHQ/terraform-azure-evh/commit/df0330f95e0c0a2a5b86f5788f71224fc9b12486))
* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#57](https://github.com/CloudNationHQ/terraform-azure-evh/issues/57)) ([b721759](https://github.com/CloudNationHQ/terraform-azure-evh/commit/b721759bde80bb7f284644e8ededdd1c9926bbd0))
* **deps:** bump golang.org/x/crypto from 0.31.0 to 0.35.0 in /tests ([#59](https://github.com/CloudNationHQ/terraform-azure-evh/issues/59)) ([f7f719a](https://github.com/CloudNationHQ/terraform-azure-evh/commit/f7f719ab198fa48de42c0f90c1e8f7baab3c4cd7))
* **deps:** bump golang.org/x/net from 0.33.0 to 0.38.0 in /tests ([#61](https://github.com/CloudNationHQ/terraform-azure-evh/issues/61)) ([a1bb84a](https://github.com/CloudNationHQ/terraform-azure-evh/commit/a1bb84a22a34fc1b758795c959d6b6dc6d6e74b1))

---

## Module: azure-aa
## [2.7.0](https://github.com/CloudNationHQ/terraform-azure-aa/releases/tag/v2.7.0)


### Features

* add missing functionality ([#45](https://github.com/CloudNationHQ/terraform-azure-aa/issues/45)) ([53000f3](https://github.com/CloudNationHQ/terraform-azure-aa/commit/53000f33e0dce4bce76c8cb4e57e8e15e206c947))
* **deps:** bump golang.org/x/net from 0.36.0 to 0.38.0 in /tests ([#46](https://github.com/CloudNationHQ/terraform-azure-aa/issues/46)) ([b29d674](https://github.com/CloudNationHQ/terraform-azure-aa/commit/b29d6746cea10115fe6459d4a92d3141c358a8b5))

---

## Module: azure-app
## [4.0.1](https://github.com/CloudNationHQ/terraform-azure-app/releases/tag/v4.0.1)


### Bug Fixes

* remove sequential entry in makefile ([#41](https://github.com/CloudNationHQ/terraform-azure-app/issues/41)) ([1009359](https://github.com/CloudNationHQ/terraform-azure-app/commit/1009359990a05b716195fc43ee201cbcc03df638))

---

## Module: azure-pip
## [4.0.0](https://github.com/CloudNationHQ/terraform-azure-pip/releases/tag/v4.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#40](https://github.com/CloudNationHQ/terraform-azure-pip/issues/40)) ([5fe6c0f](https://github.com/CloudNationHQ/terraform-azure-pip/commit/5fe6c0f6fbba154bf34b8ab11aee83fdbdd29deb))

### Upgrade from v3.0.0 to v4.0.0:

- Update module reference to: `version = "~> 4.0"`
- The property and variable resource_group is renamed to resource_group_name

---

## Module: azure-fw
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-fw/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#38](https://github.com/CloudNationHQ/terraform-azure-fw/issues/38)) ([3b9d55b](https://github.com/CloudNationHQ/terraform-azure-fw/commit/3b9d55b4b864fc14c0226c81e51d1278b6370f3e))

### Upgrade from v2.5.2 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- The property and variable resource_group is renamed to resource_group_name

---

## Module: azure-lb
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-lb/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#24](https://github.com/CloudNationHQ/terraform-azure-lb/issues/24)) ([895ca86](https://github.com/CloudNationHQ/terraform-azure-lb/commit/895ca869d8c8d3bbb30651225243c32bab4d030b))

### Upgrade from v1.5.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The property and variable resource_group is renamed to resource_group_name

---

## Module: azure-lb
## [1.5.0](https://github.com/CloudNationHQ/terraform-azure-lb/releases/tag/v1.5.0)


### Features

* **deps:** bump golang.org/x/net from 0.36.0 to 0.38.0 in /tests ([#23](https://github.com/CloudNationHQ/terraform-azure-lb/issues/23)) ([a861042](https://github.com/CloudNationHQ/terraform-azure-lb/commit/a86104252935593e591997c3e3f548b68babfd30))

---

## Module: azure-uai
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-uai/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#9](https://github.com/CloudNationHQ/terraform-azure-uai/issues/9)) ([5bd1ebb](https://github.com/CloudNationHQ/terraform-azure-uai/commit/5bd1ebbc2831e161edfead600fd2c5a65d0f7537))

### Upgrade from v1.1.1 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The property and variable resource_group is renamed to resource_group_name

---

## Module: azure-ng
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-ng/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#10](https://github.com/CloudNationHQ/terraform-azure-ng/issues/10)) ([321d878](https://github.com/CloudNationHQ/terraform-azure-ng/commit/321d878e3c4764236cea7e4e7c2460845750721b))

### Upgrade from v1.1.2 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The property and variable resource_group is renamed to resource_group_name

---

## Module: azure-cog
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-cog/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#11](https://github.com/CloudNationHQ/terraform-azure-cog/issues/11)) ([ad8c3a9](https://github.com/CloudNationHQ/terraform-azure-cog/commit/ad8c3a94f69ad08f678a52aa7ff6ae25a7dd6eac))

### Upgrade from v1.1.1 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The property and variable resource_group is renamed to resource_group_name

---

