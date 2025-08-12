---
title: Release Notes for 2024-08-22
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20240822.html
folder: release_notes
---

## Module: azure-aks
## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-aks/releases/tag/v1.0.0)


### ⚠ BREAKING CHANGES

* data structure has changed due to renaming of properties and output variables.

### Features

* aligned several properties ([#85](https://github.com/CloudNationHQ/terraform-azure-aks/issues/85)) ([b46f077](https://github.com/CloudNationHQ/terraform-azure-aks/commit/b46f077a03cad4bc4d18c9daeb3af40a92ea4bdc))

### Upgrade from v0.12.0 to v1.0.0:

- Update module reference to: `version = "~> 1.0"`
- Rename or remove properties in cluster object:
  - resourcegroup -> resource_group
  - custom_ca_trust_certificates_base64 -> deprecated
  - azure_active_directory_role_based_access_control -> several deprecated properties
  - custom_ca_trust_enabled -> deprecated
  - load_balancer -> load_balancer_profile
  - proxy -> http_proxy_config
  - workspace.enable.oms_agent -> oms_agent
  - workspace.enable.defender -> microsoft_defender
  - profile.service_mesh -> service_mesh_profile
  - profile.autoscaler -> workload_autoscaler_profile
  - maintenance.general -> maintenance_window
  - maintenance.node_os -> maintenance_window_node_os
  - maintenance.auto_upgrade -> maintenance_window_auto_upgrade
  - default_node_pool.config.linux_os -> default_node_pool.linux_os_config
  - default_node_pool.config.kubelet ->  default_node_pool.kubelet_config
- Rename variable (optional):
  - resourcegroup -> resource_group
- Rename output variable:
  - subscriptionId -> subscription_id'
- Change defaults:
  - role_based_access_control_enabled now defaults to true
  - local_account_disabled now defaults to false
  - skip_service_principal_aad_check now defaults to false
- Change required properties:
  - identity is now required for all usages

---

