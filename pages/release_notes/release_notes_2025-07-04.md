---
title: Releases for 2025-07-04
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 08, 2025
summary: "Releases of the Terraform Well Architected Modules 2025-07-04"
sidebar: mydoc_sidebar
permalink: release_notes_20250704.html
folder: release_notes
---

# Release Notes for 2025-07-04

## azure-sub
### v3.0.0 (v3.0.0)
**Published at:** 2025-07-04T12:54:11Z

## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-sub/compare/v2.3.1...v3.0.0) (2025-07-04)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* add support for existing subscriptions ([#28](https://github.com/CloudNationHQ/terraform-azure-sub/issues/28)) ([8cd4750](https://github.com/CloudNationHQ/terraform-azure-sub/commit/8cd475044e6ae45c522b01a0e98a3af7f51f1c3f))

### Upgrade from v2.3.1 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
  - The keys on some resources changed, which will cause recreates.

---

