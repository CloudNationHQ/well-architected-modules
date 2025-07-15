---
title: Release Notes for 2025-02-12
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250212.html
folder: release_notes
---

## Module: azure-vm
## [5.0.1](https://github.com/CloudNationHQ/terraform-azure-vm/releases/tag/v5.0.1)


### Bug Fixes

* fix duplicate interface naming ([#185](https://github.com/CloudNationHQ/terraform-azure-vm/issues/185)) ([24abe02](https://github.com/CloudNationHQ/terraform-azure-vm/commit/24abe02c682d31756a6787c6dc18792d86ef1803))

---

## Module: azure-vm
## [5.0.0](https://github.com/CloudNationHQ/terraform-azure-vm/releases/tag/v5.0.0)


### ⚠ BREAKING CHANGES

* the network interface keys are changed. This change will cause a recreate on existing resources.

### Features

* simplified iteration on network interfaces ([#183](https://github.com/CloudNationHQ/terraform-azure-vm/issues/183)) ([c49303e](https://github.com/CloudNationHQ/terraform-azure-vm/commit/c49303e3a6c9ec08dae8b4bf62d893f99ab59b09))

### Upgrade from v4.5.2 to v5.0.0:

- Update module reference to: `version = "~> 5.0"`

---

## Module: azure-vm
## [4.5.2](https://github.com/CloudNationHQ/terraform-azure-vm/releases/tag/v4.5.2)


### Bug Fixes

* typo settings ([4aba24a](https://github.com/CloudNationHQ/terraform-azure-vm/commit/4aba24a2f8c841c1021a4d93aeaab058da2917e1))

---

## Module: azure-agw
## [1.3.0](https://github.com/CloudNationHQ/terraform-azure-agw/releases/tag/v1.3.0)


### Features

* add network interface backend pool association support ([#26](https://github.com/CloudNationHQ/terraform-azure-agw/issues/26)) ([2fdcbe9](https://github.com/CloudNationHQ/terraform-azure-agw/commit/2fdcbe9279ab98c9f8ef94ce75e3360f400bad8d))
* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#25](https://github.com/CloudNationHQ/terraform-azure-agw/issues/25)) ([d32089e](https://github.com/CloudNationHQ/terraform-azure-agw/commit/d32089e0a5916051c4100fa594ba6c48fad51afe))


### Bug Fixes

* make backend_settings,probe and backend_pools fully optional, add missing properties ([#22](https://github.com/CloudNationHQ/terraform-azure-agw/issues/22)) ([9889f84](https://github.com/CloudNationHQ/terraform-azure-agw/commit/9889f849ff02cfce66fbff2920744a31f987c4c0))

---

