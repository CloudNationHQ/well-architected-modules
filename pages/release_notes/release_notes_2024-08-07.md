---
title: Release Notes for 2024-08-07
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20240807.html
folder: release_notes
---

## Module: azure-sa
## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-sa/releases/tag/v1.0.0)


### ⚠ BREAKING CHANGES

* data structure has changed due to renaming of properties and (output) variables

### Features

* add filesystems adls gen2 and filesystems paths, renaming of properties ([#100](https://github.com/CloudNationHQ/terraform-azure-sa/issues/100)) ([c90774c](https://github.com/CloudNationHQ/terraform-azure-sa/commit/c90774cc50f0c3a6ffda035deb661cd5f57f637c))

### Upgrade from v0.23.x to v1.0

- Update **module reference** to: `version = "~> 1.0"`
- Rename properties in **storage** object:
    * resourcegroup -> resource_group
    * enable_https_traffic_only -> https_traffic_only_enabled
- Rename **variable** (optional):
   * resourcegroup -> resource_group
- Rename **output variable**:
   * subscriptionId -> subscription_id

---

**Published at:** 2024-08-07T08:20:49Z

## Module: azure-vm
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-vm/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* data structure has changed due to renaming of properties and (output) variables.

### Features

* align and remove several deprecated properties ([#132](https://github.com/CloudNationHQ/terraform-azure-vm/issues/132)) ([8415daa](https://github.com/CloudNationHQ/terraform-azure-vm/commit/8415daad1c36d0e6ce59677547d77110496c6ddb))
* align source image reference blocks ([#130](https://github.com/CloudNationHQ/terraform-azure-vm/issues/130)) ([489cf70](https://github.com/CloudNationHQ/terraform-azure-vm/commit/489cf704c46e9b0b20411ad9079ce2a7621f49c1))

### Upgrade from v2.4.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- Rename properties in instance object:
  - resourcegroup -> resource_group
  - image -> source_image_reference
  - enable_accelerated_networking -> accelerated_networking_enabled
  - enable_ip_forwarding -> ip_forwarding_enabled
  - ultra_ssd_enabled -> additional_capabilities.ultra_ssd_enabled
  - boot_diags.storage_uri -> boot_diagnostics.storage_account_uri
- Rename variable (optional):
  - resourcegroup -> resource_group
- Rename output variable:
  - subscriptionId -> subscription_id'

---

**Published at:** 2024-08-07T12:41:41Z

## Module: azure-psql
## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-psql/releases/tag/v1.0.0)


### ⚠ BREAKING CHANGES

* update of data structure as variable got renamed
    * feat: add psql flexible server configurations, including example and updated docs
    * feat: update module versions to 1.0

### Upgrade from v0.7.0 to v1.0.0

- Update **module reference** to: `version = "~> 1.0"`
- Rename **variable** (optional):
   * resourcegroup -> resource_group

### Features

* add psql flexible server configurations ([#29](https://github.com/CloudNationHQ/terraform-azure-psql/issues/29)) ([912abc0](https://github.com/CloudNationHQ/terraform-azure-psql/commit/912abc0df8a4e095ba8d83d876ee94b559b05b8d))

---

**Published at:** 2024-08-07T14:14:46Z

## Module: azure-psql
## [0.7.0](https://github.com/CloudNationHQ/terraform-azure-psql/releases/tag/v0.7.0)


### Features

* update contribution docs ([#25](https://github.com/CloudNationHQ/terraform-azure-psql/issues/25)) ([3353451](https://github.com/CloudNationHQ/terraform-azure-psql/commit/3353451751741f2cda17ca106114c6ce69723c75))

---

**Published at:** 2024-08-07T13:57:44Z

## Module: azure-syn
## 0.1.0 (2024-08-07)


### Features

* create initial resources ([be76cae](https://github.com/CloudNationHQ/terraform-azure-syn/releases/tag/v0.1.0))
* **deps:** Bump github.com/Azure/azure-sdk-for-go/sdk/azidentity ([#6](https://github.com/CloudNationHQ/terraform-azure-syn/issues/6)) ([ced4840](https://github.com/CloudNationHQ/terraform-azure-syn/commit/ced4840f0dd119a2b3f1709eccbb844dfde2038b))
* **deps:** Bump github.com/gruntwork-io/terratest in /tests ([#7](https://github.com/CloudNationHQ/terraform-azure-syn/issues/7)) ([9a7da9d](https://github.com/CloudNationHQ/terraform-azure-syn/commit/9a7da9d00b1118daac4fee5f90761e8311b713ed))

---

**Published at:** 2024-08-07T13:46:04Z

