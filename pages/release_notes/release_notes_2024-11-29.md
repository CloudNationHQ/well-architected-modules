---
title: Release Notes for 2024-11-29
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20241129.html
folder: release_notes
---

## Module: azure-vnet
## [8.1.1](https://github.com/CloudNationHQ/terraform-azure-vnet/releases/tag/v8.1.1)


### Bug Fixes

* resolved race condition in network security group association ([#116](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/116)) ([9dac66f](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/9dac66f30866097f932590b640beb3ccae806f79))

---

## Module: azure-bastion
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-bastion/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* public ip needs to be used as a seperated module.

### Features

* removed public ip from the module itself ([#64](https://github.com/CloudNationHQ/terraform-azure-bastion/issues/64)) ([fbb0dcf](https://github.com/CloudNationHQ/terraform-azure-bastion/commit/fbb0dcf57ba243eb20fe9c6f02c3a8740b9ccb27))

### Upgrade from v2.4.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
  - see example [usage](https://github.com/CloudNationHQ/terraform-azure-bastion/blob/main/examples/complete/main.tf)

---

## Module: azure-agw
## 1.0.0 (2024-11-29)


### Features

* add initial resources ([#2](https://github.com/CloudNationHQ/terraform-azure-agw/releases/tag/v1.0.0)) ([6feea34](https://github.com/CloudNationHQ/terraform-azure-agw/commit/6feea3497af35a044464df5424c7dd3ccdbcbc07))

---

