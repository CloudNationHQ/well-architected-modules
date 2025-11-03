---
title: Release Notes for 2025-10-22
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20251022.html
folder: release_notes
---

## Module: azure-ca
## [4.0.0](https://github.com/CloudNationHQ/terraform-azure-ca/releases/tag/v4.0.0)


### ⚠ BREAKING CHANGES

* major version refactor ([#78](https://github.com/CloudNationHQ/terraform-azure-ca/issues/78))

### Features


### 1. Identity Configuration
The `identity` block now requires a `principal_id` field when using automatic role assignments, the identity is no longer created within the module, but can be created using externally, either using the UAI module of CN or in another way:

```hcl
# ❌ Before (v3.x) Identity was implicit (module created UAI internally)
# No identity block needed

# ✅ After (v4.0)
identity = {
  type         = "UserAssigned"
  identity_ids = [module.uai.config.id]
  principal_id = module.uai.config.principal_id  # Required for role assignments
}

#  Create UAI explicitly
module "uai" {
  source  = "cloudnationhq/uai/azure"
  version = "~> 2.0"

  config = {
    name                = "uai-myapp"
    location            = "westeurope"
    resource_group_name = "rg-demo"
  }
}
```
# Why this change?

Greater flexibility - bring your own UAI from any source, use of separate module
Cross-subscription support - UAI can exist in different subscriptions
Better control - explicit identity management for security and governance
Cleaner separation of concerns - identity lifecycle managed separately

### 2. Registry Configuration
```hcl
Added new optional properties for automatic ACR pull role assignments:
registry = {
  server                  = "myacr.azurecr.io"
  scope                   = module.acr.registry.id             
  role_assignment_enabled = true                            # NEW: Opt-out flag (default: true)
  identity_id             = module.uai.config.id            # Must be set if scope is set
}
```
**Opt-out:** Set `role_assignment_enabled = false ` to manage ACR permissions externally

### 3. Key Vault Secrets Configuration
Added new optional properties for automatic Key Vault Secrets User role assignments:
```hcl
# Top-level scope applies to all Key Vault secrets
key_vault_scope                   = module.kv.vault.id       # renamed from kv_scope
key_vault_role_assignment_enabled = true                     # NEW: Opt-out flag (default: true)

secrets = {
  my-secret = {
    key_vault_secret_id = module.kv.secrets.secret1.versionless_id
    identity_id         = module.uai.config.id                # Must be provided if key_vault_scope is set
  }
}
```

**Opt-out:** Set `key_vault_role_assignment_enabled = false` to manage Key Vault permissions externally

### 4. Use Existing Container App Environment
Added use_existing property to reference an existing Container App Environment instead of creating a new one:
```hcl
environment = {
  name                = "existing-cae-name"
  resource_group_name = "existing-rg"
  use_existing        = true  # NEW: Reference existing CAE
  
  container_apps = {
    # ... your apps
  }
}
```

### 5. Variable Type Definitions
Updated to include strict type definitions with improved structure:

Identity object: Added optional `principal_id` field (string)
Registry object: Added optional `role_assignment_enabled` (bool, default: true)
Root app / job: Added optional `key_vault_role_assignment_enabled` (bool, default: true)
Root environment: Added optional `use_existing` (bool, default: false)  
Deprecated `kv_scope` property (use key_vault_scope instead)

### 6. Added missing properties
_azurerm_container_app_environment_: missing optional block `identity` in root (resource)
_azurerm_container_app_: missing optional property `initial_delay` in template.container.startup_probe (resource)
_azurerm_container_app_: missing optional block `cors` in ingress (resource)

## 📖 Migration Guide

### Step 1: Create User-Assigned Identity Explicitly
In v3.x, the module created identities automatically. In v4.0, you must create them explicitly using the UAI module or another method.

### Step 2: Add Identity Block to Container Apps/Jobs
Add explicit identity configuration to each container app and job that requires managed identity access to ACR or Key Vault.

### Step 3: Update Registry Configuration (if using ACR with managed identity)
Choose one of two approaches:
- **Option A**: Enable automatic role assignments by adding the `scope` property
- **Option B**: Manage role assignments externally by setting `role_assignment_enabled = false`

### Step 4: Update Key Vault Secrets Configuration (if using Key Vault)
- Rename `kv_scope` to `key_vault_scope`
- Choose one of two approaches:
  - **Option A**: Enable automatic role assignments by adding `key_vault_scope` at the container app/job level
  - **Option B**: Manage role assignments externally by setting `key_vault_role_assignment_enabled = false`

### Step 5: Add Moved Block for Container App Environment
Due to the resource key change to support `use_existing`, add a `moved` block to prevent resource recreation:

```hcl
moved {
  from = module.ca.azurerm_container_app_environment.cae["{your-previous-key}"]
  to   = module.ca.azurerm_container_app_environment.cae["cae"]
}
```

### Step 6: Update Module Version
```hcl
module "ca" {
  source  = "cloudnationhq/ca/azure"
  version = "~> 4.0"
  
  # ... your configuration
}
```

---

## Module: azure-vnm
## 1.0.0 (2025-10-22)


### Features

* add initial structure ([ba7a836](https://github.com/CloudNationHQ/terraform-azure-vnm/releases/tag/v1.0.0))
* **deps:** bump github.com/cloudnationhq/az-cn-go-validor in /tests ([#2](https://github.com/CloudNationHQ/terraform-azure-vnm/issues/2)) ([3580f5e](https://github.com/CloudNationHQ/terraform-azure-vnm/commit/3580f5e28c7cbcb907feb66f2ccd5ba95a855505))
* **deps:** bump github.com/ulikunitz/xz from 0.5.10 to 0.5.14 in /tests ([#4](https://github.com/CloudNationHQ/terraform-azure-vnm/issues/4)) ([f0ec99b](https://github.com/CloudNationHQ/terraform-azure-vnm/commit/f0ec99b2fc5b03bdf9bd48df0120c30d8647cd2c))
* initial commit for vnm module ([cddc01f](https://github.com/CloudNationHQ/terraform-azure-vnm/commit/cddc01f441067f34f1303a57d758d0a7f3969bbe))
* small adjustments ([#3](https://github.com/CloudNationHQ/terraform-azure-vnm/issues/3)) ([b998687](https://github.com/CloudNationHQ/terraform-azure-vnm/commit/b9986875c6e013052d9ba4042db148f552a93a9d))

---

