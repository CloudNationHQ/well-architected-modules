---
title: Release Notes for 2024-09-25
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20240925.html
folder: release_notes
---

## Module: azure-law
## [2.0.1](https://github.com/CloudNationHQ/terraform-azure-law/releases/tag/v2.0.1)


### Bug Fixes

* global tags and updated examples ([#76](https://github.com/CloudNationHQ/terraform-azure-law/issues/76)) ([5a2b8b1](https://github.com/CloudNationHQ/terraform-azure-law/commit/5a2b8b16f2c7392c0d25f29f3b91563ce650109f))

---

**Published at:** 2024-09-25T12:27:38Z

## Module: azure-law
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-law/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#74](https://github.com/CloudNationHQ/terraform-azure-law/issues/74)) ([bfb9950](https://github.com/CloudNationHQ/terraform-azure-law/commit/bfb995066519b342afb5ac704e8acb874aeb0d11))

### Upgrade from v1.2.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

**Published at:** 2024-09-25T09:45:00Z

## Module: azure-sql
## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-sql/releases/tag/v1.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#50](https://github.com/CloudNationHQ/terraform-azure-sql/issues/50)) ([92fa56b](https://github.com/CloudNationHQ/terraform-azure-sql/commit/92fa56ba6aebb67f038f186190689c1f75ea861e))

### Upgrade from v0.10.0 to v1.0.0:

- Update module reference to: `version = "~> 1.0"`
- Change properties in instance object:
  - resourcegroup -> resource_group
  - immutable_backups_enabled -> deprecated
- Rename variable:
  - resourcegroup -> resource_group

---

**Published at:** 2024-09-25T07:22:05Z

## Module: azure-aks
## [2.1.0](https://github.com/CloudNationHQ/terraform-azure-aks/releases/tag/v2.1.0)


### Features

* add node soak duration and drain timout in minutes support ([#92](https://github.com/CloudNationHQ/terraform-azure-aks/issues/92)) ([63f7fa5](https://github.com/CloudNationHQ/terraform-azure-aks/commit/63f7fa59486dbaa8601baddf6e5e98053aea958b))

---

**Published at:** 2024-09-25T15:18:19Z

## Module: azure-aks
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-aks/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#89](https://github.com/CloudNationHQ/terraform-azure-aks/issues/89)) ([b003a3a](https://github.com/CloudNationHQ/terraform-azure-aks/commit/b003a3a29cf4b5c6a775fac8c438c23f7c646c12))

### Upgrade from v1.0.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- Changed properties in cluster object:
  - automatic_channel_upgrade -> automatic_upgrade_channel
  - node_os_channel_upgrade -> node_os_upgrade_channel
  - azure_active_directory_role_based_access_control.managed -> removed
  - network_profile.outbound_ip_prefix_ids -> removed
  - network_profile.outbound_ip_address_ids -> removed
  - enable_auto_scaling -> auto_scaling_enabled
  - enable_host_encryption -> host_encryption_enabled
  - enable_node_public_ip -> node_public_ip_enabled

---

**Published at:** 2024-09-25T10:12:39Z

## Module: azure-vwan
## [2.0.1](https://github.com/CloudNationHQ/terraform-azure-vwan/releases/tag/v2.0.1)


### Bug Fixes

* fix global tags and updated documentation ([#54](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/54)) ([8da21d7](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/8da21d7ccc221be21981610b186137c384a217db))

---

**Published at:** 2024-09-25T12:56:41Z

## Module: azure-evh
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-evh/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#43](https://github.com/CloudNationHQ/terraform-azure-evh/issues/43)) ([baafa02](https://github.com/CloudNationHQ/terraform-azure-evh/commit/baafa0215d0fffed9257682bbb1563321acd1f3c))

### Upgrade from v1.2.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- Changed properties in namespace object:
  - namespace.zone_redundant -> deprecated

---

**Published at:** 2024-09-25T09:55:47Z

## Module: azure-rsv
## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-rsv/releases/tag/v1.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#22](https://github.com/CloudNationHQ/terraform-azure-rsv/issues/22)) ([89944bf](https://github.com/CloudNationHQ/terraform-azure-rsv/commit/89944bfe2dbaa27a74ac54d614c10a6c722db0b9))

### Upgrade from v0.6.0 to v1.0.0:

- Update module reference to: `version = "~> 1.0"`
- Change properties in vault object:
  - resourcegroup -> resource_group
- Rename variable:
  - resourcegroup -> resource_group

---

**Published at:** 2024-09-25T07:25:21Z

## Module: azure-vgw
## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-vgw/releases/tag/v1.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#35](https://github.com/CloudNationHQ/terraform-azure-vgw/issues/35)) ([893aa76](https://github.com/CloudNationHQ/terraform-azure-vgw/commit/893aa76d917aaa8c0dcfc5359c4516abc892ae7a))

### Upgrade from v0.9.0 to v1.0.0:

- Update module reference to: `version = "~> 1.0"`
- Change properties in gateway object:
  - resourcegroup -> resource_group
- Rename variable:
  - resourcegroup -> resource_group

---

**Published at:** 2024-09-25T07:31:20Z

## Module: azure-ca
## [2.0.1](https://github.com/CloudNationHQ/terraform-azure-ca/releases/tag/v2.0.1)


### Bug Fixes

* global tags and examples update ([#35](https://github.com/CloudNationHQ/terraform-azure-ca/issues/35)) ([eaacb43](https://github.com/CloudNationHQ/terraform-azure-ca/commit/eaacb435b30baae893dd51fb108f6fc1a0bb482b))

---

**Published at:** 2024-09-25T12:16:51Z

## Module: azure-syn
## [1.0.1](https://github.com/CloudNationHQ/terraform-azure-syn/releases/tag/v1.0.1)


### Bug Fixes

* fix global tags and updated documentation ([#24](https://github.com/CloudNationHQ/terraform-azure-syn/issues/24)) ([fac5831](https://github.com/CloudNationHQ/terraform-azure-syn/commit/fac58310e08e9fe043deb2896275cee495301bec))

---

**Published at:** 2024-09-25T12:50:24Z

## Module: azure-dcr
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-dcr/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#6](https://github.com/CloudNationHQ/terraform-azure-dcr/issues/6)) ([385fc1b](https://github.com/CloudNationHQ/terraform-azure-dcr/commit/385fc1b2db97862a55adb6d399e2629e10839724))

### Upgrade from v1.0.1 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

**Published at:** 2024-09-25T09:58:46Z

## Module: azure-redis
## [2.0.1](https://github.com/CloudNationHQ/terraform-azure-redis/releases/tag/v2.0.1)


### Bug Fixes

* fix global tags and updated documentation ([#11](https://github.com/CloudNationHQ/terraform-azure-redis/issues/11)) ([f5dd69d](https://github.com/CloudNationHQ/terraform-azure-redis/commit/f5dd69d39d01fa9ce66b0c38bc0bd84602cec0a1))

---

**Published at:** 2024-09-25T12:48:38Z

## Module: azure-dbw
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-dbw/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#3](https://github.com/CloudNationHQ/terraform-azure-dbw/issues/3)) ([dcc98fb](https://github.com/CloudNationHQ/terraform-azure-dbw/commit/dcc98fbf90527b1c459f9cedb660c51c7fc6e9cb))

### Upgrade from v1.0.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

**Published at:** 2024-09-25T10:00:57Z

## Module: azure-pip
## [2.0.1](https://github.com/CloudNationHQ/terraform-azure-pip/releases/tag/v2.0.1)


### Bug Fixes

* added additional optional config for public ip ([#10](https://github.com/CloudNationHQ/terraform-azure-pip/issues/10)) ([3250c84](https://github.com/CloudNationHQ/terraform-azure-pip/commit/3250c84e0f52ccdc7102cd877245492e3ed7e689))

---

**Published at:** 2024-09-25T12:34:44Z

## Module: azure-pip
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-pip/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#8](https://github.com/CloudNationHQ/terraform-azure-pip/issues/8)) ([60a466f](https://github.com/CloudNationHQ/terraform-azure-pip/commit/60a466fc94d353d9a7e0fab601e7176ac6e52469))

### Upgrade from v1.1.1 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

**Published at:** 2024-09-25T07:10:24Z

## Module: azure-appi
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-appi/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([3987c09](https://github.com/CloudNationHQ/terraform-azure-appi/commit/3987c0967d4f6285a20a4ee2dbfb505b601fca90))

### Upgrade from v1.0.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

**Published at:** 2024-09-25T10:22:21Z

## Module: azure-fwp
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-fwp/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#4](https://github.com/CloudNationHQ/terraform-azure-fwp/issues/4)) ([18ec3fc](https://github.com/CloudNationHQ/terraform-azure-fwp/commit/18ec3fcc38e5dee9b0870f26d4a78e734582577d))

### Upgrade from v1.0.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- Rename variable in submodule ip-groups:
  - resourcegroup -> resource_group

---

**Published at:** 2024-09-25T09:51:26Z

## Module: azure-mag
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-mag/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#5](https://github.com/CloudNationHQ/terraform-azure-mag/issues/5)) ([aff5845](https://github.com/CloudNationHQ/terraform-azure-mag/commit/aff584593bb4a57477a26d6d8384250f04c7d508))

### Upgrade from v1.1.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

**Published at:** 2024-09-25T07:12:43Z

## Module: azure-apim
## [2.0.1](https://github.com/CloudNationHQ/terraform-azure-apim/releases/tag/v2.0.1)


### Bug Fixes

* Global tags and cleanup naming suffixes ([#6](https://github.com/CloudNationHQ/terraform-azure-apim/issues/6)) ([d62dc62](https://github.com/CloudNationHQ/terraform-azure-apim/commit/d62dc62f3fd26739bde1de1a97040f8b6acef6c2))

---

**Published at:** 2024-09-25T12:11:51Z

## Module: azure-apim
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-apim/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#4](https://github.com/CloudNationHQ/terraform-azure-apim/issues/4)) ([33551be](https://github.com/CloudNationHQ/terraform-azure-apim/commit/33551be4216fbe055c29e8524c4bee2793580700))

### Upgrade from v1.0.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

**Published at:** 2024-09-25T07:15:01Z

