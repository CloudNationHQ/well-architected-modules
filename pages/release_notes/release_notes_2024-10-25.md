---
title: Release Notes for 2024-10-25
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20241025.html
folder: release_notes
---

## Module: azure-vnet
## [7.0.0](https://github.com/CloudNationHQ/terraform-azure-vnet/releases/tag/v7.0.0)


### ⚠ BREAKING CHANGES

* corrected vnet output and made several improvements ([#96](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/96))

### Features

* corrected vnet output and made several improvements ([#96](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/96)) ([a369dfc](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/a369dfce51a730f7d33cdc9a3ba841131d181d10))

### Upgrade from v6.1.0 to v7.0.0:

- Update module reference to: `version = "~> 7.0"`
- Several keys are changed in the data structure :
  - vnet name is removed as key in the vnet resource and data source
  - several keys are changed in subresources
  - made improvements in individual and shared network security groups
  - made improvements in individual and shared route tables

---

**Published at:** 2024-10-25T13:15:09Z

