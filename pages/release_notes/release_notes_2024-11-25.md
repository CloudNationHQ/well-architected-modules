---
title: Release Notes for 2024-11-25
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20241125.html
folder: release_notes
---

## Module: azure-vnet
## [8.1.0](https://github.com/CloudNationHQ/terraform-azure-vnet/releases/tag/v8.1.0)


### Features

* ignore inline rules in network security groups and take current subscription as alias in peering usage ([#114](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/114)) ([3a4b634](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/3a4b6345190a0a15cfe5ea87c102cb16d4bfedd6))

---

**Published at:** 2024-11-25T08:09:43Z

## Module: azure-sa
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-sa/releases/tag/v3.0.0)

### ⚠ BREAKING CHANGES

* added missing properties, aligned azure files authentication properties ([#121](https://github.com/CloudNationHQ/terraform-azure-sa/issues/121))

### Upgrade from v2.2.0 to v3.0.0:
* Update module reference to: version = "~> 3.0"

 **Important:** The property `storage_account_name` has been replaced by `storage_account_id` in version 3.0. This update will impact any existing storage account containers or file shares managed by Terraform. If these resources are already part of the Terraform state, applying the upgrade may cause Terraform to attempt a destroy and recreate action, leading to potential data loss.

To avoid this, you need to remove the resources from the state and re-import them. Here’s an **example** of how to do this:

**Remove the container from the state:**
```
removed {
  from = module.storage["tfstate"].azurerm_storage_container.sc

  lifecycle {
    destroy = false
  }
}
```

This block specifies that the storage container should be **removed** from Terraform's state, but **without actually destroying** the resource in Azure.

**Re-import the container with the updated storage_account_id:**
```
import {
  to = module.storage["tfstate"].azurerm_storage_container.sc["tfstate"]
  id = "/subscriptions/<subscription_id>/resourceGroups/<resource_group_name>/providers/Microsoft.Storage/storageAccounts/<storage_account_id>/blobServices/default/containers/<container_name>"
}
```

Replace <subscription_id>, <resource_group_name>, <storage_account_id>, and <container_name> with the actual values for your environment.

By following these steps, you ensure that Terraform won’t destroy or recreate the storage container (or share), allowing for a smooth transition to version 3.0.

### Features

* added missing properties, aligned azure files authentication properties ([#121](https://github.com/CloudNationHQ/terraform-azure-sa/issues/121)) ([cdfc710](https://github.com/CloudNationHQ/terraform-azure-sa/commit/cdfc71015459cb23773cd72c137c1c2e8be8f2be))

---

**Published at:** 2024-11-25T08:34:55Z

## Module: azure-cosmosdb
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* Data structure mongo databases has changed.

### Features

* allow multiple indexes on mongodb collections ([#66](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/issues/66)) ([a6b131c](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/commit/a6b131c2138ae75a29820203f625d7edb8344a2e))

### Upgrade from v2.2.1 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
- If using mongodb collection the data structure is slightly changed :
  - see [examples](https://github.com/CloudNationHQ/terraform-azure-cosmosdb/blob/main/examples/mongodb/main.tf) for the correct usage

---

**Published at:** 2024-11-25T08:42:47Z

## Module: azure-bastion
## [2.4.0](https://github.com/CloudNationHQ/terraform-azure-bastion/releases/tag/v2.4.0)


### Features

* add zones support and fixed required ruleset ([#62](https://github.com/CloudNationHQ/terraform-azure-bastion/issues/62)) ([412f057](https://github.com/CloudNationHQ/terraform-azure-bastion/commit/412f0579e25fb22f926a4a516a56c7ececb0e267))

---

**Published at:** 2024-11-25T08:17:53Z

