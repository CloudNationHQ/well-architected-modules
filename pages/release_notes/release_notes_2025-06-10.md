---
title: Releases for 2025-06-10
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 01, 2025
summary: "Releases of the Terraform Well Architected Modules 2025-06-10"
sidebar: mydoc_sidebar
permalink: release_notes_20250610.html
folder: release_notes
---

# Release Notes for 2025-06-10

## azure-dnspr
### v3.0.0 (v3.0.0)
**Published at:** 2025-06-10T08:48:09Z

## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-dnspr/compare/v2.3.0...v3.0.0) (2025-06-10)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#30](https://github.com/CloudNationHQ/terraform-azure-dnspr/issues/30)) ([04104c3](https://github.com/CloudNationHQ/terraform-azure-dnspr/commit/04104c3fd026bd7f783f17489f6b05c57cc94689))
* Type definitions are added.
*  Several naming improvements

### Upgrade from v2.3.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- The property and variable resource_group is renamed to resource_group_name

---

