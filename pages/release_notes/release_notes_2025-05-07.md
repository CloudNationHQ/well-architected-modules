---
title: Release Notes for 2025-05-07
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250507.html
folder: release_notes
---

## Module: azure-sa
## [4.0.0](https://github.com/CloudNationHQ/terraform-azure-sa/releases/tag/v4.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#170](https://github.com/CloudNationHQ/terraform-azure-sa/issues/170)) ([a0a2dd8](https://github.com/CloudNationHQ/terraform-azure-sa/commit/a0a2dd8f86d1c112af8f7fee501fabe281d2eab4))

### Upgrade from v3.7.1 to v4.0.0:

- Update module reference to: `version = "~> 4.0"`
- The user assigned identity is removed from the module.
  - For identity we created a separate module as shown in the examples.
- The property and variable resource_group is renamed to resource_group_name

---

## Module: azure-sql
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-sql/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* add type definitions and small refactor ([#73](https://github.com/CloudNationHQ/terraform-azure-sql/issues/73)) ([7a21e2f](https://github.com/CloudNationHQ/terraform-azure-sql/commit/7a21e2f77bd7c3958b9611d8eb49c65d375563e5))

### Upgrade from v1.5.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The user assigned identity is removed from the module.
  - For identity we created a separate module as shown in the examples.
- The property and variable resource_group is renamed to resource_group_name

---

## Module: azure-ca
## [3.2.0](https://github.com/CloudNationHQ/terraform-azure-ca/releases/tag/v3.2.0)


### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#59](https://github.com/CloudNationHQ/terraform-azure-ca/issues/59)) ([43d0f4a](https://github.com/CloudNationHQ/terraform-azure-ca/commit/43d0f4a32496eb777c5397b69ceb859ff1a80c25))
* **deps:** bump golang.org/x/crypto from 0.31.0 to 0.35.0 in /tests ([#66](https://github.com/CloudNationHQ/terraform-azure-ca/issues/66)) ([5fb32a9](https://github.com/CloudNationHQ/terraform-azure-ca/commit/5fb32a9c83727eba0bc35d2861b0cafe7401cc46))
* **deps:** bump golang.org/x/net from 0.33.0 to 0.38.0 in /tests ([#67](https://github.com/CloudNationHQ/terraform-azure-ca/issues/67)) ([9dabf6d](https://github.com/CloudNationHQ/terraform-azure-ca/commit/9dabf6d845b6a5e9cb0e66b0ee11938bcc740221))
* schema validation items for ca ([#68](https://github.com/CloudNationHQ/terraform-azure-ca/issues/68)) ([8cc28aa](https://github.com/CloudNationHQ/terraform-azure-ca/commit/8cc28aaa890f9d8d55a1c810c7d9203ef2669da4))

---

## Module: azure-mysql
## [3.1.0](https://github.com/CloudNationHQ/terraform-azure-mysql/releases/tag/v3.1.0)


### Features

* replace deployment test code with module consumption and fix tags property idempotence ([#33](https://github.com/CloudNationHQ/terraform-azure-mysql/issues/33)) ([47549e9](https://github.com/CloudNationHQ/terraform-azure-mysql/commit/47549e90d87a02112dd2e90f363365a7a4c4e8c1))

---

## Module: azure-app
## [4.0.0](https://github.com/CloudNationHQ/terraform-azure-app/releases/tag/v4.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#39](https://github.com/CloudNationHQ/terraform-azure-app/issues/39)) ([ac7afcf](https://github.com/CloudNationHQ/terraform-azure-app/commit/ac7afcf18eb768449073734907565929b35148ad))

### Upgrade from v3.1.1 to v4.0.0:

- Update module reference to: `version = "~> 4.0"`
- The property and variable resource_group is renamed to resource_group_name

---

