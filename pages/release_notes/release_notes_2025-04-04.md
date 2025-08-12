---
title: Release Notes for 2025-04-04
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250404.html
folder: release_notes
---

## Module: azure-pip
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-pip/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* prefix resources is removed from main module

### Features

* move prefixes to submodule ([#37](https://github.com/CloudNationHQ/terraform-azure-pip/issues/37)) ([e38d700](https://github.com/CloudNationHQ/terraform-azure-pip/commit/e38d700d1692b65bb340f0f8b3f0d958ccbbfbe3))

### Upgrade from v2.7.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- New submodule for prefixes
  - Update data structure to support public ip's with prefixes as shown in the examples.

---

## Module: azure-ng
## [1.1.1](https://github.com/CloudNationHQ/terraform-azure-ng/releases/tag/v1.1.1)


### Bug Fixes

* fix prefixes module reference in usage ([#5](https://github.com/CloudNationHQ/terraform-azure-ng/issues/5)) ([c7d3804](https://github.com/CloudNationHQ/terraform-azure-ng/commit/c7d3804542adf98cb37977fe9b7bc392ad700fae))

---

## Module: azure-ng
## [1.1.0](https://github.com/CloudNationHQ/terraform-azure-ng/releases/tag/v1.1.0)


### Features

* **deps:** bump golang.org/x/net from 0.34.0 to 0.36.0 in /tests ([#3](https://github.com/CloudNationHQ/terraform-azure-ng/issues/3)) ([29c9d2c](https://github.com/CloudNationHQ/terraform-azure-ng/commit/29c9d2ce7aa9f8842c8c706b8de6a0ebf24c0da2))

---

## Module: azure-ng
## 1.0.0 (2025-04-04)


### Features

* add initial files ([#1](https://github.com/CloudNationHQ/terraform-azure-ng/releases/tag/v1.0.0)) ([9c4f06b](https://github.com/CloudNationHQ/terraform-azure-ng/commit/9c4f06b895fbd0e002d862cc6f27ed5f29c0641e))

---

