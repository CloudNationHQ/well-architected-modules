---
title: Release Notes for 2025-09-24
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250924.html
folder: release_notes
---

## Module: azure-sa
## [4.2.0](https://github.com/CloudNationHQ/terraform-azure-sa/releases/tag/v4.2.0)


### Features

* improve type definitions and added container immutability policy support ([#184](https://github.com/CloudNationHQ/terraform-azure-sa/issues/184)) ([8391909](https://github.com/CloudNationHQ/terraform-azure-sa/commit/839190945e17515cec7ee12c17e25fc456712da0))

---

## Module: azure-pdns
## [4.0.0](https://github.com/CloudNationHQ/terraform-azure-pdns/releases/tag/v4.0.0)


### ⚠ BREAKING CHANGES

* this change causes recreates

### Features

* add type definitions and changed data structure ([#71](https://github.com/CloudNationHQ/terraform-azure-pdns/issues/71)) ([b24c540](https://github.com/CloudNationHQ/terraform-azure-pdns/commit/b24c540927c8bf92888ad65c162915548b1dd5f2))

### Upgrade from v3.6.0 to v4.0.0:

- Update module reference to: `version = "~> 4.0"`
- The property and variable resource_group is renamed to resource_group_name

---

