---
title: Releases for 2025-06-16
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 08, 2025
summary: "Releases of the Terraform Well Architected Modules 2025-06-16"
sidebar: mydoc_sidebar
permalink: release_notes_20250616.html
folder: release_notes
---

# Release Notes for 2025-06-16

## azure-pdns
### v3.5.0 (v3.5.0)
**Published at:** 2025-06-16T07:08:02Z

## [3.5.0](https://github.com/CloudNationHQ/terraform-azure-pdns/compare/v3.4.0...v3.5.0) (2025-06-16)


### Features

* add mx record support public dns ([#58](https://github.com/CloudNationHQ/terraform-azure-pdns/issues/58)) ([a0003f2](https://github.com/CloudNationHQ/terraform-azure-pdns/commit/a0003f25384c8269a3d6d206f6ec2bac81584123))
* **deps:** bump golang.org/x/net in /tests in the go_modules group ([#54](https://github.com/CloudNationHQ/terraform-azure-pdns/issues/54)) ([8acc037](https://github.com/CloudNationHQ/terraform-azure-pdns/commit/8acc03799b235ef580099fa208d88156678a4b98))

---

## azure-alerts
### v2.0.0 (v2.0.0)
**Published at:** 2025-06-16T14:06:41Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-alerts/compare/v1.2.0...v2.0.0) (2025-06-16)


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

## azure-costs
### v1.5.0 (v1.5.0)
**Published at:** 2025-06-16T07:28:54Z

## [1.5.0](https://github.com/CloudNationHQ/terraform-azure-costs/compare/v1.4.1...v1.5.0) (2025-06-16)


### Features

* replace deployment code with improved go package ([#21](https://github.com/CloudNationHQ/terraform-azure-costs/issues/21)) ([8e96692](https://github.com/CloudNationHQ/terraform-azure-costs/commit/8e966922f09537f26f34c77be2057ccdb75fb4da))

---

## azure-sub
### v2.3.0 (v2.3.0)
**Published at:** 2025-06-16T14:53:49Z

## [2.3.0](https://github.com/CloudNationHQ/terraform-azure-sub/compare/v2.2.0...v2.3.0) (2025-06-16)


### Features

* update documentation ([#22](https://github.com/CloudNationHQ/terraform-azure-sub/issues/22)) ([285b7ee](https://github.com/CloudNationHQ/terraform-azure-sub/commit/285b7ee3daa3bfc414805194c7a744ca52539777))

---

