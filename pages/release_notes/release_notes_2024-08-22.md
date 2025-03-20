---
title: Releases for 2024-08-22
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Mar 20, 2025
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20240822.html
folder: release_notes
---

# Release Notes for 2024-08-22

## azure-acr
### v1.6.0 (v1.6.0)
**Published at:** 2024-08-22T08:15:59Z

## [1.6.0](https://github.com/CloudNationHQ/terraform-azure-acr/compare/v1.5.0...v1.6.0) (2024-08-22)


### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#55](https://github.com/CloudNationHQ/terraform-azure-acr/issues/55)) ([38227f2](https://github.com/CloudNationHQ/terraform-azure-acr/commit/38227f27ff124ca39724fc3424bd16e0eaa699c2))
* update contribution docs ([#53](https://github.com/CloudNationHQ/terraform-azure-acr/issues/53)) ([f7a2f8a](https://github.com/CloudNationHQ/terraform-azure-acr/commit/f7a2f8a4e07ba9c9803a66315cb8565979053c46))

---

## azure-aks
### v1.0.0 (v1.0.0)
**Published at:** 2024-08-22T14:43:17Z

## [1.0.0](https://github.com/CloudNationHQ/terraform-azure-aks/compare/v0.12.0...v1.0.0) (2024-08-22)


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

## azure-rbac
### v0.5.0 (v0.5.0)
**Published at:** 2024-08-22T15:12:32Z

## [0.5.0](https://github.com/CloudNationHQ/terraform-azure-rbac/compare/v0.4.0...v0.5.0) (2024-08-22)


### Features

* added support for custom role definitions ([#23](https://github.com/CloudNationHQ/terraform-azure-rbac/issues/23)) ([2ced7c2](https://github.com/CloudNationHQ/terraform-azure-rbac/commit/2ced7c2d0f9fce483d93432ea65bad6ebeb5ba6e))

---

## azure-rbac
### v0.4.0 (v0.4.0)
**Published at:** 2024-08-22T15:04:14Z

## [0.4.0](https://github.com/CloudNationHQ/terraform-azure-rbac/compare/v0.3.0...v0.4.0) (2024-08-22)


### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#21](https://github.com/CloudNationHQ/terraform-azure-rbac/issues/21)) ([dbb5605](https://github.com/CloudNationHQ/terraform-azure-rbac/commit/dbb5605bfb3caadb07d78afd10380e91aee637e6))
* update contribution docs ([#18](https://github.com/CloudNationHQ/terraform-azure-rbac/issues/18)) ([afe9fe9](https://github.com/CloudNationHQ/terraform-azure-rbac/commit/afe9fe9fbefbfd98119528d9fb6df2afab273cb4))

---

