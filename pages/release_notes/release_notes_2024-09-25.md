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

## Module: azure-law
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-law/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#74](https://github.com/CloudNationHQ/terraform-azure-law/issues/74)) ([bfb9950](https://github.com/CloudNationHQ/terraform-azure-law/commit/bfb995066519b342afb5ac704e8acb874aeb0d11))

### Upgrade from v1.2.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

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

## Module: azure-vwan
## [2.0.1](https://github.com/CloudNationHQ/terraform-azure-vwan/releases/tag/v2.0.1)


### Bug Fixes

* fix global tags and updated documentation ([#54](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/54)) ([8da21d7](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/8da21d7ccc221be21981610b186137c384a217db))

---

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

## Module: azure-syn
## [1.0.1](https://github.com/CloudNationHQ/terraform-azure-syn/releases/tag/v1.0.1)


### Bug Fixes

* fix global tags and updated documentation ([#24](https://github.com/CloudNationHQ/terraform-azure-syn/issues/24)) ([fac5831](https://github.com/CloudNationHQ/terraform-azure-syn/commit/fac58310e08e9fe043deb2896275cee495301bec))

---

## Module: azure-dcr
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-dcr/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#6](https://github.com/CloudNationHQ/terraform-azure-dcr/issues/6)) ([385fc1b](https://github.com/CloudNationHQ/terraform-azure-dcr/commit/385fc1b2db97862a55adb6d399e2629e10839724))

### Upgrade from v1.0.1 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

## Module: azure-redis
## [2.0.1](https://github.com/CloudNationHQ/terraform-azure-redis/releases/tag/v2.0.1)


### Bug Fixes

* fix global tags and updated documentation ([#11](https://github.com/CloudNationHQ/terraform-azure-redis/issues/11)) ([f5dd69d](https://github.com/CloudNationHQ/terraform-azure-redis/commit/f5dd69d39d01fa9ce66b0c38bc0bd84602cec0a1))

---

## Module: azure-dbw
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-dbw/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#3](https://github.com/CloudNationHQ/terraform-azure-dbw/issues/3)) ([dcc98fb](https://github.com/CloudNationHQ/terraform-azure-dbw/commit/dcc98fbf90527b1c459f9cedb660c51c7fc6e9cb))

### Upgrade from v1.0.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

## Module: azure-pip
## [2.0.1](https://github.com/CloudNationHQ/terraform-azure-pip/releases/tag/v2.0.1)


### Bug Fixes

* added additional optional config for public ip ([#10](https://github.com/CloudNationHQ/terraform-azure-pip/issues/10)) ([3250c84](https://github.com/CloudNationHQ/terraform-azure-pip/commit/3250c84e0f52ccdc7102cd877245492e3ed7e689))

---

## Module: azure-pip
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-pip/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#8](https://github.com/CloudNationHQ/terraform-azure-pip/issues/8)) ([60a466f](https://github.com/CloudNationHQ/terraform-azure-pip/commit/60a466fc94d353d9a7e0fab601e7176ac6e52469))

### Upgrade from v1.1.1 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

## Module: azure-appi
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-appi/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([3987c09](https://github.com/CloudNationHQ/terraform-azure-appi/commit/3987c0967d4f6285a20a4ee2dbfb505b601fca90))

### Upgrade from v1.0.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

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

## Module: azure-apim
## [2.0.1](https://github.com/CloudNationHQ/terraform-azure-apim/releases/tag/v2.0.1)


### Bug Fixes

* Global tags and cleanup naming suffixes ([#6](https://github.com/CloudNationHQ/terraform-azure-apim/issues/6)) ([d62dc62](https://github.com/CloudNationHQ/terraform-azure-apim/commit/d62dc62f3fd26739bde1de1a97040f8b6acef6c2))

---

## Module: azure-apim
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-apim/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#4](https://github.com/CloudNationHQ/terraform-azure-apim/issues/4)) ([33551be](https://github.com/CloudNationHQ/terraform-azure-apim/commit/33551be4216fbe055c29e8524c4bee2793580700))

### Upgrade from v1.0.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

