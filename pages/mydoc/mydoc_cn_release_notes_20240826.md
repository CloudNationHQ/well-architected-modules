---
title: August 2024 Releases 
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: August 26, 2024
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: mydoc_cn_release_notes_20240826.html
folder: mydoc
---

## Terraform Azure Web App ( App services )

### [Release v1.1.0 Features](https://github.com/CloudNationHQ/terraform-azure-dnspr/releases/tag/v1.0.1) 
### Features
- Features
• added code of conduct and security documentation (33dbbfe)
• fix linting issues (48def4f)
• increment module versions (f23dfdf)

## Terraform Azure Private DNS Resolver

### [Release v1.0.1 Features](https://github.com/CloudNationHQ/terraform-azure-dnspr/releases/tag/v1.0.1) 
### Bug Fixes
- fix some usage module references (#3) (68accba)

## Terraform Azure Dcr ( Data Collection Rule)

### [Release v1.0.1 Features](https://github.com/CloudNationHQ/terraform-azure-dcr/releases/tag/v1.0.1) 
### Bug Fixes
- fix module references (#3) (1b0044d)

## Terraform Azure Acr

### [Release v1.6.0 Features](https://github.com/CloudNationHQ/terraform-azure-acr/releases/tag/v1.6.0) 
### Features

- deps: bump github.com/gruntwork-io/terratest in /tests (#55) (38227f2)
- update contribution docs (#53) (f7a2f8a)


## Terraform Azure AKS

### [Release v1.0.0 Features](https://github.com/CloudNationHQ/terraform-azure-aks/releases/tag/v1.0.0) 
### Features
- aligned several properties (#85) (b46f077)
### Upgrade from v0.12.0 to v1.0.0:

- Update module reference to: version = "~> 1.0"
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
    - default_node_pool.config.kubelet -> default_node_pool.kubelet_config
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

### [Release v12.0.0 Features](https://github.com/CloudNationHQ/terraform-azure-aks/releases/tag/v0.12.0) 
Features
- deps: bump github.com/gruntwork-io/terratest in /tests (#83) (fe80dbe)
- update contribution docs (#80) (22734ee)

## Terraform Azure RBAC

### [Release v0.5.0 Features](https://github.com/CloudNationHQ/terraform-azure-rbac/releases/tag/v0.5.0) 
Features
- added support for custom role definitions (#23) (2ced7c2)

### [Release v0.4.0 Features](https://github.com/CloudNationHQ/terraform-azure-rbac/releases/tag/v0.4.0) 
Features
- deps: bump github.com/gruntwork-io/terratest in /tests (#21) (dbb5605)
- update contribution docs (#18) (afe9fe9)

