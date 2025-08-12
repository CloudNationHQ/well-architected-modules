---
title: Release Notes for 2024-09-26
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20240926.html
folder: release_notes
---

## Module: azure-aks
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-aks/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* data structure has changed due to renaming of properties.

### Features

* aligned several properties in kubernetes pools ([#96](https://github.com/CloudNationHQ/terraform-azure-aks/issues/96)) ([84d097b](https://github.com/CloudNationHQ/terraform-azure-aks/commit/84d097b05edf3071964c3632801f0c011c601329))

### Upgrade from v2.1.0 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`
  - several small enhancements and integrated the functionality from the locals into the resource kubernetes pools resource itself

---

## Module: azure-ca
## [2.0.2](https://github.com/CloudNationHQ/terraform-azure-ca/releases/tag/v2.0.2)


### Bug Fixes

* add dependson on container app jobs regarding acr pull role assignments ([#37](https://github.com/CloudNationHQ/terraform-azure-ca/issues/37)) ([aa38462](https://github.com/CloudNationHQ/terraform-azure-ca/commit/aa3846259b4e40d98c6e58be5331f77cc17f64ec))

---

