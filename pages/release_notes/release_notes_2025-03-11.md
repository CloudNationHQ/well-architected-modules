---
title: Releases for 2025-03-11
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 14, 2025
summary: "Releases of the Terraform Well Architected Modules 2025-03-11"
sidebar: mydoc_sidebar
permalink: release_notes_20250311.html
folder: release_notes
---

# Release Notes for 2025-03-11

## azure-vwan
### v4.1.0 (v4.1.0)
**Published at:** 2025-03-11T16:01:10Z

## [4.1.0](https://github.com/CloudNationHQ/terraform-azure-vwan/compare/v4.0.0...v4.1.0) (2025-03-11)


### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#85](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/85)) ([37cd714](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/37cd714cdf667aca1c039ec86a851eff16e070c3))


### Bug Fixes

* fix typo routing intent module reference ([#88](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/88)) ([1d08b5d](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/1d08b5de0f51040efb061252b99849634f5d5254))

---

## azure-vwan
### v4.0.0 (v4.0.0)
**Published at:** 2025-03-11T14:28:09Z

## [4.0.0](https://github.com/CloudNationHQ/terraform-azure-vwan/compare/v3.5.0...v4.0.0) (2025-03-11)


### ⚠ BREAKING CHANGES

* The key in vpn site links has changed. This change will cause a recreate on existing resources. Also the vhub connection submodule now supports multiple connections within a single configuration. This will also cause a recreate and change in the data structure. See the examples as a reference

### Features

* add missing properties and functionality ([#86](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/86)) ([9710ca6](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/9710ca63a12c14a886cbcedaaacff1fd8c393195))

### Upgrade from v3.5.0 to v4.0.0:

- Update module reference to: `version = "~> 4.0"`

---

