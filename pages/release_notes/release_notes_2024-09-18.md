---
title: Releases for 2024-09-18
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 08, 2025
summary: "Releases of the Terraform Well Architected Modules 2024-09-18"
sidebar: mydoc_sidebar
permalink: release_notes_20240918.html
folder: release_notes
---

# Release Notes for 2024-09-18

## azure-rg
### v1.1.0 (v1.1.0)
**Published at:** 2024-09-18T07:47:58Z

## [1.1.0](https://github.com/CloudNationHQ/terraform-azure-rg/compare/v1.0.0...v1.1.0) (2024-09-18)


### Features

* add type definitions and simplified tests ([#31](https://github.com/CloudNationHQ/terraform-azure-rg/issues/31)) ([88dcdb0](https://github.com/CloudNationHQ/terraform-azure-rg/commit/88dcdb0fe19752ccdcdc9116ff956444209cb929))
* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#28](https://github.com/CloudNationHQ/terraform-azure-rg/issues/28)) ([679a1d9](https://github.com/CloudNationHQ/terraform-azure-rg/commit/679a1d9b6cf658e81e6efaa90c66c440c7befa53))

---

## azure-vwan
### v1.0.0 (v1.0.0)
**Published at:** 2024-09-18T08:01:31Z

## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-vwan/compare/v0.12.0...v1.0.0) (2024-09-18)


### ⚠ BREAKING CHANGES

* data structure has changed due to renaming of properties and removal of resources.

### Features

* aligned several properties and resources ([#47](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/47)) ([f155777](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/f1557774ee77f369689b86dff4818ab3a639b46d))

### Upgrade from v0.12.0 to v1.0.0:

- Update module reference to: `version = "~> 1.0"`
- Rename property in cluster object:
  - resourcegroup -> resource_group
- Rename variable (optional):
  - resourcegroup -> resource_group
- Rename output variable:
  - vhub -> vhubs
- Removed output variables:
  - policy
  - firewall_public_ip_addresses
  - firewall
- Removed resources:
  - azurerm_ip_group
  - azurerm_firewall_policy_rule_collection_group
  - azurerm_firewall_policy

---

## azure-fw
### v1.0.3 (v1.0.3)
**Published at:** 2024-09-18T13:14:05Z

## [1.0.3](https://github.com/CloudNationHQ/terraform-azure-fw/compare/v1.0.2...v1.0.3) (2024-09-18)


### Bug Fixes

* add public ip addresses output ([#10](https://github.com/CloudNationHQ/terraform-azure-fw/issues/10)) ([741fdc9](https://github.com/CloudNationHQ/terraform-azure-fw/commit/741fdc923c06c0ff2324eded82740e8a9dfc6f93))

---

