---
title: Release Notes for 2025-03-11
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250311.html
folder: release_notes
---

## Module: azure-vwan
## [4.1.0](https://github.com/CloudNationHQ/terraform-azure-vwan/releases/tag/v4.1.0)


### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#85](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/85)) ([37cd714](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/37cd714cdf667aca1c039ec86a851eff16e070c3))


### Bug Fixes

* fix typo routing intent module reference ([#88](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/88)) ([1d08b5d](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/1d08b5de0f51040efb061252b99849634f5d5254))

---

## Module: azure-vwan
## [4.0.0](https://github.com/CloudNationHQ/terraform-azure-vwan/releases/tag/v4.0.0)


### ⚠ BREAKING CHANGES

* The key in vpn site links has changed. This change will cause a recreate on existing resources. Also the vhub connection submodule now supports multiple connections within a single configuration. This will also cause a recreate and change in the data structure. See the examples as a reference

### Features

* add missing properties and functionality ([#86](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/86)) ([9710ca6](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/9710ca63a12c14a886cbcedaaacff1fd8c393195))

### Upgrade from v3.5.0 to v4.0.0:

- Update module reference to: `version = "~> 4.0"`

---

