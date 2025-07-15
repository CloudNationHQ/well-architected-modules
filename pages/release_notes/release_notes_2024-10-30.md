---
title: Release Notes for 2024-10-30
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20241030.html
folder: release_notes
---

## Module: azure-naming
## [0.19.1](https://github.com/CloudNationHQ/terraform-azure-naming/releases/tag/v0.19.1)


### Bug Fixes

* add support for sql managed instance naming ([#64](https://github.com/CloudNationHQ/terraform-azure-naming/issues/64)) ([f977cd3](https://github.com/CloudNationHQ/terraform-azure-naming/commit/f977cd3f2be8f68acb450690647f5bc8b99464af))

---

## Module: azure-psql
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-psql/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* update provider azuread to new major version, renamed properties.  ([#40](https://github.com/CloudNationHQ/terraform-azure-psql/issues/40))
- Updated provider AzureAD to major version ~> 3.0
- Renamed the following properties to align with the azurerm provider:
  * 'restore_time_utc' to 'point_in_time_restore_time_in_utc
  * 'geo_redundant_backup' to 'geo_redundant_backup_enabled'
  * 'admin_password' to 'administrator_password'
  * 'cmk' to 'customer_managed_key'
  * 'enabled' to 'authentication'
  * 'enabled.pw_auth' to 'authentication.password_auth_enabled'
  * 'enabled.ad_auth' to 'authentication.active_directory_auth_enabled'
  * 'network.delegated_subnet_id' to 'delegated_subnet_id'
  * 'network. private_dns_zone_id' to 'private_dns_zone_id'
  * 'maintenance' to 'maintenance_window'
- Renamed output variable 'instance' to 'server' to align with the mysql module.
- Updated psql version to latest version 16. 
- Added logic to generate random password only if password_auth_enabled is set to True. 
- Updated all readme's to include Types notation. 
- Updated examples to reflect all property changes and upgrade to new 3.0 module version. 
- Updated 'vnet-integrated' and 'complete' example with stand-alone private-dns module instead of submodule. 
- Renamed example 'maintentance' folder to 'maintenance' and 'deploy.go' test file to 'deploy_test.go'. 
- Renamed 'local.tf' files to 'naming.tf' files

### Features

* update provider azuread to new major version, renamed properties.  ([#40](https://github.com/CloudNationHQ/terraform-azure-psql/issues/40)) ([506a9c8](https://github.com/CloudNationHQ/terraform-azure-psql/commit/506a9c83cc0b20c8548b0266fa062de8ffa2edc1))

---

## Module: azure-pdns
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-pdns/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* the data structure has been enhanced to accommodate both public and private dns zones

### Features

* add support for public dns zones and record types ([#36](https://github.com/CloudNationHQ/terraform-azure-pdns/issues/36)) ([2e11725](https://github.com/CloudNationHQ/terraform-azure-pdns/commit/2e117251a16c237f3e925aa4508e71cd455e7887))

### Upgrade from v2.1.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- Restructure the zones object:
  - within zones either private or public is required now to categorize the zone types
- Added output variables:
  - private_zones and public_zones

---

## Module: azure-pe
## [1.1.3](https://github.com/CloudNationHQ/terraform-azure-pe/releases/tag/v1.1.3)


### Bug Fixes

* fix locals to include request message ([#21](https://github.com/CloudNationHQ/terraform-azure-pe/issues/21)) ([d1e252e](https://github.com/CloudNationHQ/terraform-azure-pe/commit/d1e252ef8ce0d2e52e97f43e4e9bb139c2ca6752))

---

## Module: azure-pe
## [1.1.2](https://github.com/CloudNationHQ/terraform-azure-pe/releases/tag/v1.1.2)


### Bug Fixes

* add request message parameter to private service connection ([#19](https://github.com/CloudNationHQ/terraform-azure-pe/issues/19)) ([68165c2](https://github.com/CloudNationHQ/terraform-azure-pe/commit/68165c2096feac9e4b67a91ff04fb1fc49206d3f))

---

## Module: azure-pe
## [1.1.1](https://github.com/CloudNationHQ/terraform-azure-pe/releases/tag/v1.1.1)


### Bug Fixes

* fixed manual connection property in private service connection ([#17](https://github.com/CloudNationHQ/terraform-azure-pe/issues/17)) ([41dc14e](https://github.com/CloudNationHQ/terraform-azure-pe/commit/41dc14eb63dbdad72a5448ad7c8086baff630341))

---

