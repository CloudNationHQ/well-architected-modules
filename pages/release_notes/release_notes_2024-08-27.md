---
title: Release Notes for 2024-08-27
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20240827.html
folder: release_notes
---

## Module: azure-rg
## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-rg/releases/tag/v1.0.0)


### ⚠ BREAKING CHANGES

* aligned properties

### Features

* merge output for newly created and existing groups ([#25](https://github.com/CloudNationHQ/terraform-azure-rg/issues/25)) ([4b488f5](https://github.com/CloudNationHQ/terraform-azure-rg/commit/4b488f5c723d532803b2c148da1dfeb40d927acb))

### Upgrade from v0.9.0 to v1.0

- Update module reference to: `version = "~> 1.0"`
- Rename variable:
   * region -> location
- Rename output variable:
   * groups_existing -> groups

---

**Published at:** 2024-08-27T14:21:34Z

## Module: azure-rg
## [0.9.0](https://github.com/CloudNationHQ/terraform-azure-rg/releases/tag/v0.9.0)


### Features

* update contribution docs ([#23](https://github.com/CloudNationHQ/terraform-azure-rg/issues/23)) ([7b61ef7](https://github.com/CloudNationHQ/terraform-azure-rg/commit/7b61ef758147f84e3778162b8644767c794e8b7b))

---

**Published at:** 2024-08-27T07:31:04Z

