---
title: Releases for 2024-09-24
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 09, 2025
summary: "Releases of the Terraform Well Architected Modules 2024-09-24"
sidebar: mydoc_sidebar
permalink: release_notes_20240924.html
folder: release_notes
---

# Release Notes for 2024-09-24

## azure-vnet
### v4.0.0 (v4.0.0)
**Published at:** 2024-09-24T08:23:44Z

## [4.0.0](https://github.com/CloudNationHQ/terraform-azure-vnet/compare/v3.1.0...v4.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#82](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/82)) ([88dfbce](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/88dfbcebedb6c0812ae66bda15e172c156b76c13))

### Upgrade from v3.1.0 to v4.0.0:

- Update module reference to: `version = "~> 4.0"`
- Rename properties in vnet object:
  - disable_bgp_route_propagation -> bgp_route_propagation_enabled

---

## azure-vnet
### v3.1.0 (v3.1.0)
**Published at:** 2024-09-24T07:58:49Z

## [3.1.0](https://github.com/CloudNationHQ/terraform-azure-vnet/compare/v3.0.0...v3.1.0) (2024-09-24)


### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#80](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/80)) ([fc58d91](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/fc58d9154ca249ef8ff04d94020f396763b956ec))

---

## azure-sa
### v2.0.0 (v2.0.0)
**Published at:** 2024-09-24T10:28:52Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-sa/compare/v1.1.1...v2.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#111](https://github.com/CloudNationHQ/terraform-azure-sa/issues/111)) ([17d5e7f](https://github.com/CloudNationHQ/terraform-azure-sa/commit/17d5e7f216e5eab93720f6ee220a08a7214e0b91))

### Upgrade from v1.1.1 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

## azure-acr
### v3.0.0 (v3.0.0)
**Published at:** 2024-09-24T11:43:28Z

## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-acr/compare/v2.0.0...v3.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#63](https://github.com/CloudNationHQ/terraform-azure-acr/issues/63)) ([c06c825](https://github.com/CloudNationHQ/terraform-azure-acr/commit/c06c825e7b11b8614c78d8d34b35956a0ffbac36))

### Upgrade from v2.0.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- Rename properties in registry object:
  - trust_policy  -> trust_policy_enabled
  - retention_policy -> retention_policy_in_days
  - encryption.enabled -> removed

---

## azure-rg
### v2.0.0 (v2.0.0)
**Published at:** 2024-09-24T07:54:23Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-rg/compare/v1.1.0...v2.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#32](https://github.com/CloudNationHQ/terraform-azure-rg/issues/32)) ([ae4bedc](https://github.com/CloudNationHQ/terraform-azure-rg/commit/ae4bedce18c0da8bb97f4345ce1a156280e33f48))

### Upgrade from v1.1.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

## azure-kv
### v2.0.0 (v2.0.0)
**Published at:** 2024-09-24T09:29:38Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-kv/compare/v1.1.0...v2.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#64](https://github.com/CloudNationHQ/terraform-azure-kv/issues/64)) ([24bc2c1](https://github.com/CloudNationHQ/terraform-azure-kv/commit/24bc2c11f2e71c69f245be871b4071bab01d1dd3))

### Upgrade from v1.1.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

## azure-kv
### v1.1.0 (v1.1.0)
**Published at:** 2024-09-24T09:14:32Z

## [1.1.0](https://github.com/CloudNationHQ/terraform-azure-kv/compare/v1.0.0...v1.1.0) (2024-09-24)


### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#62](https://github.com/CloudNationHQ/terraform-azure-kv/issues/62)) ([7be2e25](https://github.com/CloudNationHQ/terraform-azure-kv/commit/7be2e25af763d32051232c5a867d63a39804f996))

---

## azure-vm
### v4.0.0 (v4.0.0)
**Published at:** 2024-09-24T10:48:01Z

## [4.0.0](https://github.com/CloudNationHQ/terraform-azure-vm/compare/v3.2.0...v4.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#139](https://github.com/CloudNationHQ/terraform-azure-vm/issues/139)) ([0627801](https://github.com/CloudNationHQ/terraform-azure-vm/commit/06278010f0cc7b074d0f50141739696cf9d8e964))
* upgrade azurerm provider to v4 ([#142](https://github.com/CloudNationHQ/terraform-azure-vm/issues/142)) ([5a52ee5](https://github.com/CloudNationHQ/terraform-azure-vm/commit/5a52ee5544e7162b78aa087ba47acacc1f8a9e6f))

### Upgrade from v3.2.0 to v4.0.0:

- Update module reference to: `version = "~> 4.0"`

---

## azure-cosmosdb
### v2.0.0 (v2.0.0)
**Published at:** 2024-09-24T12:08:14Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/compare/v1.1.0...v2.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#57](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/issues/57)) ([bc9a26e](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/commit/bc9a26e6e23ac01047f8460ec3691f5c8ece6210))

### Upgrade from v1.1.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

## azure-bastion
### v2.0.0 (v2.0.0)
**Published at:** 2024-09-24T12:17:55Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-bastion/compare/v1.1.0...v2.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#52](https://github.com/CloudNationHQ/terraform-azure-bastion/issues/52)) ([737ae52](https://github.com/CloudNationHQ/terraform-azure-bastion/commit/737ae529fbfe0e8855e183e1727a9f063621141e))

### Upgrade from v1.1.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

## azure-vwan
### v2.0.0 (v2.0.0)
**Published at:** 2024-09-24T12:44:26Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-vwan/compare/v1.1.0...v2.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#52](https://github.com/CloudNationHQ/terraform-azure-vwan/issues/52)) ([c1eadc6](https://github.com/CloudNationHQ/terraform-azure-vwan/commit/c1eadc61c67735b38f5bc2140259f7b0db6af7c6))

### Upgrade from v1.1.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

## azure-psql
### v2.0.0 (v2.0.0)
**Published at:** 2024-09-24T13:16:07Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-psql/compare/v1.1.0...v2.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#34](https://github.com/CloudNationHQ/terraform-azure-psql/issues/34)) ([ba41165](https://github.com/CloudNationHQ/terraform-azure-psql/commit/ba41165f1c7b2a3b17882a00b2f3d5f02586cd59))

### Upgrade from v1.1.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

## azure-pdns
### v2.0.0 (v2.0.0)
**Published at:** 2024-09-24T12:58:14Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-pdns/compare/v1.0.0...v2.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#31](https://github.com/CloudNationHQ/terraform-azure-pdns/issues/31)) ([27718d7](https://github.com/CloudNationHQ/terraform-azure-pdns/commit/27718d75b0f5b1c46d26367fee542ccfb124d6be))

### Upgrade from v1.0.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

## azure-rbac
### v1.0.0 (v1.0.0)
**Published at:** 2024-09-24T13:00:43Z

## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-rbac/compare/v0.6.1...v1.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#30](https://github.com/CloudNationHQ/terraform-azure-rbac/issues/30)) ([d1b4ff1](https://github.com/CloudNationHQ/terraform-azure-rbac/commit/d1b4ff12757ba6aa5c25ad27d234965286fc9407))

### Upgrade from v0.6.1 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

## azure-pe
### v1.0.0 (v1.0.0)
**Published at:** 2024-09-24T10:09:39Z

## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-pe/compare/v0.4.0...v1.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#12](https://github.com/CloudNationHQ/terraform-azure-pe/issues/12)) ([a0b0dd8](https://github.com/CloudNationHQ/terraform-azure-pe/commit/a0b0dd85b50af9ca57d0c1de5864b70d29e1b1eb))

### Upgrade from v0.4.0 to v1.0.0:

- Update module reference to: `version = "~> 1.0"`
- Rename properties in endpoints object:
  - resourcegroup -> resource_group
- Rename variable:
  - resourcegroup -> resource_group

---

## azure-ca
### v2.0.0 (v2.0.0)
**Published at:** 2024-09-24T08:55:00Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-ca/compare/v1.1.0...v2.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#33](https://github.com/CloudNationHQ/terraform-azure-ca/issues/33)) ([bfdbb44](https://github.com/CloudNationHQ/terraform-azure-ca/commit/bfdbb444dae770afee7669facde976a35b02d1bb))

### Upgrade from v1.1.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

## azure-func
### v1.0.0 (v1.0.0)
**Published at:** 2024-09-24T14:17:04Z

## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-func/compare/v0.5.0...v1.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)


### Features

* upgrade azurerm provider to v4 ([#20](https://github.com/CloudNationHQ/terraform-azure-func/issues/20)) ([e79bc5d](https://github.com/CloudNationHQ/terraform-azure-func/commit/e79bc5de0e5e07cab986c81174bc11b90a353f0a))

### Upgrade from v0.5.0 to v1.0.0:

- Update module reference to: `version = "~> 1.0"`
- Rename properties in instance object:
  - resourcegroup -> resource_group
- Rename variable (optional):
  - resourcegroup -> resource_group

---

## azure-aa
### v2.0.0 (v2.0.0)
**Published at:** 2024-09-24T08:37:50Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-aa/compare/v1.0.0...v2.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#18](https://github.com/CloudNationHQ/terraform-azure-aa/issues/18)) ([afb66e6](https://github.com/CloudNationHQ/terraform-azure-aa/commit/afb66e604b93644f80066c4dd99dd4abb0fc03fc))

### Upgrade from v1.0.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

## azure-nw
### v1.0.0 (v1.0.0)
**Published at:** 2024-09-24T09:52:58Z

## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-nw/compare/v0.2.0...v1.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#8](https://github.com/CloudNationHQ/terraform-azure-nw/issues/8)) ([64a6953](https://github.com/CloudNationHQ/terraform-azure-nw/commit/64a6953c4683308542458fbcce4e769e23aa77a5))

### Upgrade from v0.2.0 to v1.0.0:

- Update module reference to: `version = "~> 1.0"`

---

## azure-syn
### v1.0.0 (v1.0.0)
**Published at:** 2024-09-24T14:43:54Z

## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-syn/compare/v0.6.0...v1.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#22](https://github.com/CloudNationHQ/terraform-azure-syn/issues/22)) ([dac9407](https://github.com/CloudNationHQ/terraform-azure-syn/commit/dac94070045f0defcb3493bd6733c29fad21f866))

### Upgrade from v0.6.0 to v1.0.0:

- Update module reference to: `version = "~> 1.0"`

---

## azure-plan
### v2.0.0 (v2.0.0)
**Published at:** 2024-09-24T13:24:14Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-plan/compare/v1.1.1...v2.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes.

### Features

* upgrade azurerm provider to v4 ([#9](https://github.com/CloudNationHQ/terraform-azure-plan/issues/9)) ([ca2f814](https://github.com/CloudNationHQ/terraform-azure-plan/commit/ca2f81482ab8cf631faf7c9cda2f8ad6fae8f32e))

### Upgrade from v1.1.1 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

## azure-dnspr
### v2.0.0 (v2.0.0)
**Published at:** 2024-09-24T12:29:40Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-dnspr/compare/v1.1.0...v2.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#9](https://github.com/CloudNationHQ/terraform-azure-dnspr/issues/9)) ([8d7f0c6](https://github.com/CloudNationHQ/terraform-azure-dnspr/commit/8d7f0c6f476767f4f88a3654d83c46a75f15e729))

### Upgrade from v1.1.0 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

## azure-redis
### v2.0.0 (v2.0.0)
**Published at:** 2024-09-24T11:53:18Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-redis/compare/v1.0.2...v2.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#9](https://github.com/CloudNationHQ/terraform-azure-redis/issues/9)) ([67da887](https://github.com/CloudNationHQ/terraform-azure-redis/commit/67da887dae373596e8a599be3336fe939e89c686))

### Upgrade from v1.0.2 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

## azure-fw
### v2.0.0 (v2.0.0)
**Published at:** 2024-09-24T09:07:37Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-fw/compare/v1.0.3...v2.0.0) (2024-09-24)


### ⚠ BREAKING CHANGES

* Version 4 of the azurerm provider includes breaking changes. The full list of changes can be found [here](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/guides/4.0-upgrade-guide)

### Features

* upgrade azurerm provider to v4 ([#12](https://github.com/CloudNationHQ/terraform-azure-fw/issues/12)) ([f7fbb98](https://github.com/CloudNationHQ/terraform-azure-fw/commit/f7fbb98c2798336402676f626a3180879aff972f))

### Upgrade from v1.0.3 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`

---

