---
title: Release Notes for 2025-06-10
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250610.html
folder: release_notes
---

## Module: azure-dnspr
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-dnspr/releases/tag/v3.0.0)


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

**Published at:** 2025-06-10T08:48:09Z

