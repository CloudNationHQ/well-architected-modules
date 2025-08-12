---
title: Release Notes for 2025-06-16
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250616.html
folder: release_notes
---

## Module: azure-pdns
## [3.5.0](https://github.com/CloudNationHQ/terraform-azure-pdns/releases/tag/v3.5.0)


### Features

* add mx record support public dns ([#58](https://github.com/CloudNationHQ/terraform-azure-pdns/issues/58)) ([a0003f2](https://github.com/CloudNationHQ/terraform-azure-pdns/commit/a0003f25384c8269a3d6d206f6ec2bac81584123))
* **deps:** bump golang.org/x/net in /tests in the go_modules group ([#54](https://github.com/CloudNationHQ/terraform-azure-pdns/issues/54)) ([8acc037](https://github.com/CloudNationHQ/terraform-azure-pdns/commit/8acc03799b235ef580099fa208d88156678a4b98))

---

## Module: azure-alerts
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-alerts/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#16](https://github.com/CloudNationHQ/terraform-azure-alerts/issues/16)) ([5082194](https://github.com/CloudNationHQ/terraform-azure-alerts/commit/50821940f6a33a5c7185bb895602fbf321bd7e3f))

### Upgrade from v1.2.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The property and variable resource_group is renamed to resource_group_name
- The submodule is renamed to monitor-workspace

Details can be found in the example usages

---

## Module: azure-costs
## [1.5.0](https://github.com/CloudNationHQ/terraform-azure-costs/releases/tag/v1.5.0)


### Features

* replace deployment code with improved go package ([#21](https://github.com/CloudNationHQ/terraform-azure-costs/issues/21)) ([8e96692](https://github.com/CloudNationHQ/terraform-azure-costs/commit/8e966922f09537f26f34c77be2057ccdb75fb4da))

---

## Module: azure-sub
## [2.3.0](https://github.com/CloudNationHQ/terraform-azure-sub/releases/tag/v2.3.0)


### Features

* update documentation ([#22](https://github.com/CloudNationHQ/terraform-azure-sub/issues/22)) ([285b7ee](https://github.com/CloudNationHQ/terraform-azure-sub/commit/285b7ee3daa3bfc414805194c7a744ca52539777))

---

