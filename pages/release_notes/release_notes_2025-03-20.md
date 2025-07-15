---
title: Release Notes for 2025-03-20
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250320.html
folder: release_notes
---

## Module: azure-aa
## [2.6.0](https://github.com/CloudNationHQ/terraform-azure-aa/releases/tag/v2.6.0)


### Features

* add missing functionality runbooks ([#43](https://github.com/CloudNationHQ/terraform-azure-aa/issues/43)) ([73a2524](https://github.com/CloudNationHQ/terraform-azure-aa/commit/73a2524a02dc52bec0d0e4a5c5879095305a3cb3))
* **deps:** bump golang.org/x/net from 0.33.0 to 0.36.0 in /tests ([#42](https://github.com/CloudNationHQ/terraform-azure-aa/issues/42)) ([24b738b](https://github.com/CloudNationHQ/terraform-azure-aa/commit/24b738bcdac14bca9cf1b607dae2165a31bd21ba))

---

**Published at:** 2025-03-20T08:40:00Z

## Module: azure-pip
## [2.6.0](https://github.com/CloudNationHQ/terraform-azure-pip/releases/tag/v2.6.0)


### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#31](https://github.com/CloudNationHQ/terraform-azure-pip/issues/31)) ([78690c5](https://github.com/CloudNationHQ/terraform-azure-pip/commit/78690c5c563c3f2863652acc41154dd800bdc1c8))
* **deps:** bump golang.org/x/net from 0.33.0 to 0.36.0 in /tests ([#32](https://github.com/CloudNationHQ/terraform-azure-pip/issues/32)) ([3b4b081](https://github.com/CloudNationHQ/terraform-azure-pip/commit/3b4b081debbc35db6f857ac9ff18df966e8e26aa))
* format documentation to include type definitions ([#33](https://github.com/CloudNationHQ/terraform-azure-pip/issues/33)) ([aac976e](https://github.com/CloudNationHQ/terraform-azure-pip/commit/aac976eb94c600be1c5c4f0b11015e961049237d))

---

**Published at:** 2025-03-20T14:27:18Z

## Module: azure-lb
## [1.4.0](https://github.com/CloudNationHQ/terraform-azure-lb/releases/tag/v1.4.0)


### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#17](https://github.com/CloudNationHQ/terraform-azure-lb/issues/17)) ([a6a0d04](https://github.com/CloudNationHQ/terraform-azure-lb/commit/a6a0d041153df210564e5cf2914e18d4585452c0))
* **deps:** bump golang.org/x/net from 0.33.0 to 0.36.0 in /tests ([#18](https://github.com/CloudNationHQ/terraform-azure-lb/issues/18)) ([d137c81](https://github.com/CloudNationHQ/terraform-azure-lb/commit/d137c810f138fe61ae4fd0a01218932d2a8ebd7e))
* format documentation to include type definitions ([#19](https://github.com/CloudNationHQ/terraform-azure-lb/issues/19)) ([9164c91](https://github.com/CloudNationHQ/terraform-azure-lb/commit/9164c91b1c500957b5ccbb43f6671bfb6fc2086e))

---

**Published at:** 2025-03-20T12:21:00Z

## Module: azure-costs
## [1.4.0](https://github.com/CloudNationHQ/terraform-azure-costs/releases/tag/v1.4.0)


### Features

* add missing functionalty anomaly alerts and budgets ([#15](https://github.com/CloudNationHQ/terraform-azure-costs/issues/15)) ([6ffa8a4](https://github.com/CloudNationHQ/terraform-azure-costs/commit/6ffa8a47364927acddb0bbc937d87e143174dbed))

---

**Published at:** 2025-03-20T08:39:00Z

## Module: azure-sub
## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-sub/releases/tag/v2.0.0)


### ⚠ BREAKING CHANGES

* refactor to single resource without a for_each ([#10](https://github.com/CloudNationHQ/terraform-azure-sub/issues/10))

### Upgrade from v1.0.0 to v2.0.0
* Update module reference to: version = "~> 2.0"
* Update the map variable 'subscriptions' (multiple subs) to an object variable 'subscription' (single sub). 
#### From:
```
subscriptions = {
  demo = {
   name = "sub-demo"
   }
}
```
#### To: 
```
subscriptions = {
   name = "sub-demo"
}
```
* Add the required moved blocks, as the keys have changed:
#### Example:
```
moved {
  from = module.sub.azurerm_management_group_subscription_association.subs["demo"]
  to   = module.sub.azurerm_management_group_subscription_association.sub["default"]
}

moved {
  from = module.sub.azurerm_subscription.subs["demo"]
  to   = module.sub.azurerm_subscription.sub
}
```
* If you want to create multiple subscriptions, use a `for_each` on the module, see example "mca".

---

**Published at:** 2025-03-20T07:28:06Z

