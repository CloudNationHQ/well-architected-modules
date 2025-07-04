---
title: Releases for 2025-04-04
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 04, 2025
summary: "Releases of the Terraform Well Architected Modules 2025-04-04"
sidebar: mydoc_sidebar
permalink: release_notes_20250404.html
folder: release_notes
---

# Release Notes for 2025-04-04

## azure-app
### v3.0.0 (v3.0.0)
**Published at:** 2025-04-04T12:51:24Z

## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-app/compare/v2.4.0...v3.0.0) (2025-04-04)


### ⚠ BREAKING CHANGES

* removed system assigned identity default

### Features

* add type definitions and made identity fully optional ([#31](https://github.com/CloudNationHQ/terraform-azure-app/issues/31)) ([c13fdb6](https://github.com/CloudNationHQ/terraform-azure-app/commit/c13fdb6cba5d73146bcb899d535477552349f18e))

### Upgrade from v2.4.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- The user assigned identity is removed from the module and it is not set to system assigned default anymore as well.
  - For identity we created a separate module as shown in the examples.

---

## azure-pip
### v3.0.0 (v3.0.0)
**Published at:** 2025-04-04T09:11:14Z

## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-pip/compare/v2.7.0...v3.0.0) (2025-04-04)


### ⚠ BREAKING CHANGES

* prefix resources is removed from main module

### Features

* move prefixes to submodule ([#37](https://github.com/CloudNationHQ/terraform-azure-pip/issues/37)) ([e38d700](https://github.com/CloudNationHQ/terraform-azure-pip/commit/e38d700d1692b65bb340f0f8b3f0d958ccbbfbe3))

### Upgrade from v2.7.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- New submodule for prefixes
  - Update data structure to support public ip's with prefixes as shown in the examples.

---

## azure-ng
### v1.1.1 (v1.1.1)
**Published at:** 2025-04-04T10:09:29Z

## [1.1.1](https://github.com/CloudNationHQ/terraform-azure-ng/compare/v1.1.0...v1.1.1) (2025-04-04)


### Bug Fixes

* fix prefixes module reference in usage ([#5](https://github.com/CloudNationHQ/terraform-azure-ng/issues/5)) ([c7d3804](https://github.com/CloudNationHQ/terraform-azure-ng/commit/c7d3804542adf98cb37977fe9b7bc392ad700fae))

---

## azure-ng
### v1.1.0 (v1.1.0)
**Published at:** 2025-04-04T09:50:15Z

## [1.1.0](https://github.com/CloudNationHQ/terraform-azure-ng/compare/v1.0.0...v1.1.0) (2025-04-04)


### Features

* **deps:** bump golang.org/x/net from 0.34.0 to 0.36.0 in /tests ([#3](https://github.com/CloudNationHQ/terraform-azure-ng/issues/3)) ([29c9d2c](https://github.com/CloudNationHQ/terraform-azure-ng/commit/29c9d2ce7aa9f8842c8c706b8de6a0ebf24c0da2))

---

## azure-ng
### v1.0.0 (v1.0.0)
**Published at:** 2025-04-04T09:46:57Z

## 1.0.0 (2025-04-04)


### Features

* add initial files ([#1](https://github.com/CloudNationHQ/terraform-azure-ng/issues/1)) ([9c4f06b](https://github.com/CloudNationHQ/terraform-azure-ng/commit/9c4f06b895fbd0e002d862cc6f27ed5f29c0641e))

---

