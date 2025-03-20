---
title: Releases for 2025-03-20
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Mar 20, 2025
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20250320.html
folder: release_notes
---

# Release Notes for 2025-03-20

## azure-sub
### v2.0.0 (v2.0.0)
**Published at:** 2025-03-20T07:28:06Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-sub/compare/v1.2.0...v2.0.0) (2025-03-20)


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

