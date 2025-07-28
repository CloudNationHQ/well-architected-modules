---
title: Release Notes for 2025-07-09
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250709.html
folder: release_notes
---

## Module: azure-vnet
## [9.2.3](https://github.com/CloudNationHQ/terraform-azure-vnet/releases/tag/v9.2.3)


### Bug Fixes

* provide fallback for if var.naming.network_security_group_rule is not set, so that it no longer ignores nsg rules when only names are provided due to the coalesce function ([#163](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/163)) ([2ced5cc](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/2ced5cc581e01c7e76f527502d76f41f29141ec4))

---

