---
title: Release Notes for 2025-05-12
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250512.html
folder: release_notes
---

## Module: azure-eg
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-eg/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#28](https://github.com/CloudNationHQ/terraform-azure-eg/issues/28)) ([cc28500](https://github.com/CloudNationHQ/terraform-azure-eg/commit/cc285008cbb452ef7ee06132ab66e4b225b8384c))

### Upgrade from v1.5.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The property and variable resource_group is renamed to resource_group_name

---

