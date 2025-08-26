---
title: Release Notes for 2025-08-26
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250826.html
folder: release_notes
---

## Module: azure-aa
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-aa/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* this change causes recreates

### Features

* small refactor and changed data structure ([#53](https://github.com/CloudNationHQ/terraform-azure-aa/issues/53)) ([86b46f9](https://github.com/CloudNationHQ/terraform-azure-aa/commit/86b46f9a05a804721b41930b1dcb1c73dbcd314f))

### Upgrade from v2.7.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- The property and variable resource_group is renamed to resource_group_name

---

## Module: azure-eg
## [2.3.0](https://github.com/CloudNationHQ/terraform-azure-eg/releases/tag/v2.3.0)


### Features

* **deps:** bump github.com/cloudnationhq/az-cn-go-validor in /tests ([#43](https://github.com/CloudNationHQ/terraform-azure-eg/issues/43)) ([d4d035c](https://github.com/CloudNationHQ/terraform-azure-eg/commit/d4d035c1f4831bf6c23ec3ed89adff80c20e9986))
* update source_resource_id property ([#44](https://github.com/CloudNationHQ/terraform-azure-eg/issues/44)) ([05ce0f6](https://github.com/CloudNationHQ/terraform-azure-eg/commit/05ce0f6291d761f182d47bf7e1aed1b19092bf75))

---

