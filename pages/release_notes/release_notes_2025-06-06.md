---
title: Releases for 2025-06-06
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 09, 2025
summary: "Releases of the Terraform Well Architected Modules 2025-06-06"
sidebar: mydoc_sidebar
permalink: release_notes_20250606.html
folder: release_notes
---

# Release Notes for 2025-06-06

## azure-vwan
### v5.0.1 (v5.0.1)
**Published at:** 2025-06-06T14:28:59Z

## [5.0.1](https://github.com/CloudNationHQ/terraform-azure-vwan/compare/v5.0.0...v5.0.1) (2025-06-06)


### Bug Fixes

* remove vpn link validation condition ([#112](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/112)) ([d6357ee](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/d6357ee9116bd94ec8117db81caa606dc2593ffd))

---

## azure-mag
### v3.1.0 (v3.1.0)
**Published at:** 2025-06-06T14:06:59Z

## [3.1.0](https://github.com/CloudNationHQ/terraform-azure-mag/compare/v3.0.0...v3.1.0) (2025-06-06)


### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#25](https://github.com/CloudNationHQ/terraform-azure-mag/issues/25)) ([396bdf0](https://github.com/CloudNationHQ/terraform-azure-mag/commit/396bdf06658434737ebaee5597399a95f08be4b6))

---

## azure-mag
### v3.0.0 (v3.0.0)
**Published at:** 2025-06-06T14:04:38Z

## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-mag/compare/v2.4.0...v3.0.0) (2025-06-06)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#26](https://github.com/CloudNationHQ/terraform-azure-mag/issues/26)) ([05c04fa](https://github.com/CloudNationHQ/terraform-azure-mag/commit/05c04fae4bd48fe8f0121192e087147fa142c16b))
* type definitions are added

### Upgrade from v2.4.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- The property and variable resource_group is renamed to resource_group_name

---

## azure-fdfwp
### v2.0.0 (v2.0.0)
**Published at:** 2025-06-06T07:02:33Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-fdfwp/compare/v1.3.0...v2.0.0) (2025-06-05)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* small refactor ([#20](https://github.com/CloudNationHQ/terraform-azure-fdfwp/issues/20)) ([9d440cc](https://github.com/CloudNationHQ/terraform-azure-fdfwp/commit/9d440cca5c5ededfbd15f7afb4a4ba5854a5e4f5))

### Upgrade from v1.3.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The property and variable resource_group is renamed to resource_group_name
- The data structure is changed for the properties sku_name, enabled, mode, redirect_url, custom_block_response_status_code, custom_block_response_body and request_body_check_enabled for the frontdoor firewall policy resource

---

