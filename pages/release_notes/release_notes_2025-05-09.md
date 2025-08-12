---
title: Release Notes for 2025-05-09
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250509.html
folder: release_notes
---

## Module: azure-vm
## [6.2.0](https://github.com/CloudNationHQ/terraform-azure-vm/releases/tag/v6.2.0)


### Features

* replace deployment test code with module consumption and fix tags property idempotence ([#197](https://github.com/CloudNationHQ/terraform-azure-vm/issues/197)) ([c6418b3](https://github.com/CloudNationHQ/terraform-azure-vm/commit/c6418b32aac10cb69d586ca820e0cac49b8c5b47))

---

## Module: azure-sb
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-sb/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#23](https://github.com/CloudNationHQ/terraform-azure-sb/issues/23)) ([8a30da5](https://github.com/CloudNationHQ/terraform-azure-sb/commit/8a30da5a4b75441b0727f703ea2d0c6ef6bf2ba7))

### Upgrade from v1.3.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The property and variable resource_group is renamed to resource_group_name

---

## Module: azure-mcf
## [1.1.0](https://github.com/CloudNationHQ/terraform-azure-mcf/releases/tag/v1.1.0)


### Features

* **deps:** bump golang.org/x/net from 0.34.0 to 0.38.0 in /tests ([#4](https://github.com/CloudNationHQ/terraform-azure-mcf/issues/4)) ([4265f41](https://github.com/CloudNationHQ/terraform-azure-mcf/commit/4265f41ded697e2ff3a0e38a342f08f022bb64f0))
* replace deployment test code with module consumption and fix tags property idempotence ([#7](https://github.com/CloudNationHQ/terraform-azure-mcf/issues/7)) ([65fc7e4](https://github.com/CloudNationHQ/terraform-azure-mcf/commit/65fc7e45287bd4c9e689a1b97c133d9252b92f08))

---

