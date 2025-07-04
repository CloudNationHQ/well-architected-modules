---
title: Releases for 2025-06-08
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 04, 2025
summary: "Releases of the Terraform Well Architected Modules 2025-06-08"
sidebar: mydoc_sidebar
permalink: release_notes_20250608.html
folder: release_notes
---

# Release Notes for 2025-06-08

## azure-redis
### v3.0.0 (v3.0.0)
**Published at:** 2025-06-08T15:01:33Z

## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-redis/compare/v2.3.0...v3.0.0) (2025-06-06)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#30](https://github.com/CloudNationHQ/terraform-azure-redis/issues/30)) ([6619305](https://github.com/CloudNationHQ/terraform-azure-redis/commit/661930584150fc74d09b0f7edddd0f43d2777beb))

### Upgrade from v2.3.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- The user assigned identity is removed from the module.
  - For identity we created a separate module.
- The property and variable resource_group is renamed to resource_group_name

---

