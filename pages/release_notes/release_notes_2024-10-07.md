---
title: Release Notes for 2024-10-07
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20241007.html
folder: release_notes
---

## Module: azure-aks
## [3.1.1](https://github.com/CloudNationHQ/terraform-azure-aks/releases/tag/v3.1.1)


### Bug Fixes

* increment versioning in usages ([#101](https://github.com/CloudNationHQ/terraform-azure-aks/issues/101)) ([62604fe](https://github.com/CloudNationHQ/terraform-azure-aks/commit/62604fed8f5412f031705aae8c768c5401cb0469))

---

**Published at:** 2024-10-07T08:54:02Z

## Module: azure-aks
## [3.1.0](https://github.com/CloudNationHQ/terraform-azure-aks/releases/tag/v3.1.0)


### Features

* small refactor ([#99](https://github.com/CloudNationHQ/terraform-azure-aks/issues/99)) ([9a27b69](https://github.com/CloudNationHQ/terraform-azure-aks/commit/9a27b699a6cb7211c9cb4e4a78c760cdd94d7da0))

---

**Published at:** 2024-10-07T08:28:46Z

## Module: azure-app
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-app/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

*  Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#13](https://github.com/CloudNationHQ/terraform-azure-app/issues/13)) ([3a614c2](https://github.com/CloudNationHQ/terraform-azure-app/commit/3a614c2866e9c79cec4cbd3d59fa489b0fdae8e4))

### Upgrade from v1.2.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- Deprecated properties in instance object:
  - auto_heal_enabled -> deprecated
  - docker_container_name -> deprecated
  - docker_container_tag -> deprecated

---

**Published at:** 2024-10-07T13:00:03Z

## Module: azure-app
## [1.2.0](https://github.com/CloudNationHQ/terraform-azure-app/releases/tag/v1.2.0)


### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#10](https://github.com/CloudNationHQ/terraform-azure-app/issues/10)) ([74f50de](https://github.com/CloudNationHQ/terraform-azure-app/commit/74f50dee485ecb7908119fee9fc4a3345df48a75))


### Bug Fixes

* sanitize go testing ([#8](https://github.com/CloudNationHQ/terraform-azure-app/issues/8)) ([f508150](https://github.com/CloudNationHQ/terraform-azure-app/commit/f508150220264f323bffcb43d1f00c4a9a51741a))

---

**Published at:** 2024-10-07T07:09:03Z

