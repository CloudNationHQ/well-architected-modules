---
title: Release Notes for 2024-09-18
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20240918.html
folder: release_notes
---

## Module: azure-vwan
## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-vwan/releases/tag/v1.0.0)


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

