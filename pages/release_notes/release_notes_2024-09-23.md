---
title: Release Notes for 2024-09-23
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20240923.html
folder: release_notes
---

## Module: azure-pdns
## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-pdns/releases/tag/v1.0.0)


### ⚠ BREAKING CHANGES

* data structure has changed due to renaming of properties.

### Features

* aligned several properties and simplified tests ([#29](https://github.com/CloudNationHQ/terraform-azure-pdns/issues/29)) ([e5d6c13](https://github.com/CloudNationHQ/terraform-azure-pdns/commit/e5d6c13ad03791fc9e90b1e349a8ca89c8ecbece))

### Upgrade from v0.6.0 to v1.0.0:

- Update module reference to: `version = "~> 1.0"`
- Rename properties in zones object:
  - resourcegroup -> resource_group
- Rename variable (optional):
  - resourcegroup -> resource_group

---

## Module: azure-apim
## 1.0.0 (2024-09-23)


### Features

* add initial resources ([#2](https://github.com/CloudNationHQ/terraform-azure-apim/releases/tag/v1.0.0)) ([abbdf22](https://github.com/CloudNationHQ/terraform-azure-apim/commit/abbdf22b5ac04eb8dbf6c69c7a31937c97529f7a))

---

