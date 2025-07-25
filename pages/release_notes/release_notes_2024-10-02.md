---
title: Release Notes for 2024-10-02
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20241002.html
folder: release_notes
---

## Module: azure-vnet
## [5.0.0](https://github.com/CloudNationHQ/terraform-azure-vnet/releases/tag/v5.0.0)


### ⚠ BREAKING CHANGES

* Make use of an already existing vnet ([#86](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/86))

### Features

* Make use of an already existing vnet ([#86](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/86)) ([3e001ff](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/3e001ff44081accbbde466842cbe9239d1c991c4))

### Upgrade from v4.0.0 to v5.0.0:

- Update module reference to: `version = "~> 5.0"`
- The following keys in the statefile will change (update accordingly):
  - module.network.azurerm_virtual_network.vnet
  - module.network.azurerm_virtual_network_dns_servers.dns

---

