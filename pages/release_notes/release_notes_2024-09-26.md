---
title: Releases for 2024-09-26
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 08, 2025
summary: "Releases of the Terraform Well Architected Modules 2024-09-26"
sidebar: mydoc_sidebar
permalink: release_notes_20240926.html
folder: release_notes
---

# Release Notes for 2024-09-26

## azure-vnet
### v4.0.1 (v4.0.1)
**Published at:** 2024-09-26T07:11:24Z

## [4.0.1](https://github.com/CloudNationHQ/terraform-azure-vnet/compare/v4.0.0...v4.0.1) (2024-09-26)


### Bug Fixes

* fix defaults private endpoint network policies ([#84](https://github.com/CloudNationHQ/terraform-azure-vnet/issues/84)) ([f0258d5](https://github.com/CloudNationHQ/terraform-azure-vnet/commit/f0258d57cd58c726b98829c4f5b5ddd61cd94536))

---

## azure-acr
### v3.0.1 (v3.0.1)
**Published at:** 2024-09-26T07:04:30Z

## [3.0.1](https://github.com/CloudNationHQ/terraform-azure-acr/compare/v3.0.0...v3.0.1) (2024-09-26)


### Bug Fixes

* fix defaults retention policy in days ([#65](https://github.com/CloudNationHQ/terraform-azure-acr/issues/65)) ([18a276b](https://github.com/CloudNationHQ/terraform-azure-acr/commit/18a276b09f05070743567b659a1878f44204e9da))

---

## azure-aks
### v3.0.0 (v3.0.0)
**Published at:** 2024-09-26T14:25:57Z

## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-aks/compare/v2.1.0...v3.0.0) (2024-09-26)


### ⚠ BREAKING CHANGES

* data structure has changed due to renaming of properties.

### Features

* aligned several properties in kubernetes pools ([#96](https://github.com/CloudNationHQ/terraform-azure-aks/issues/96)) ([84d097b](https://github.com/CloudNationHQ/terraform-azure-aks/commit/84d097b05edf3071964c3632801f0c011c601329))

### Upgrade from v2.1.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
  - several small enhancements and integrated the functionality from the locals into the resource kubernetes pools resource itself

---

## azure-ca
### v2.0.2 (v2.0.2)
**Published at:** 2024-09-26T09:12:35Z

## [2.0.2](https://github.com/CloudNationHQ/terraform-azure-ca/compare/v2.0.1...v2.0.2) (2024-09-26)


### Bug Fixes

* add dependson on container app jobs regarding acr pull role assignments ([#37](https://github.com/CloudNationHQ/terraform-azure-ca/issues/37)) ([aa38462](https://github.com/CloudNationHQ/terraform-azure-ca/commit/aa3846259b4e40d98c6e58be5331f77cc17f64ec))

---

