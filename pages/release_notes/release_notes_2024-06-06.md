---
title: Releases for 2024-06-06
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 08, 2025
summary: "Releases of the Terraform Well Architected Modules 2024-06-06"
sidebar: mydoc_sidebar
permalink: release_notes_20240606.html
folder: release_notes
---

# Release Notes for 2024-06-06

## azure-vm
### v2.0.0 (v2.0.0)
**Published at:** 2024-06-06T17:24:26Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-vm/compare/v1.13.0...v2.0.0) (2024-06-06)


### ⚠ BREAKING CHANGES

* Introduction of optional multiple IP configurations alters the data structure, making the change not backwards compatible

### Features

* **deps:** bump github.com/Azure/azure-sdk-for-go/sdk/azidentity ([#102](https://github.com/CloudNationHQ/terraform-azure-vm/issues/102)) ([637208c](https://github.com/CloudNationHQ/terraform-azure-vm/commit/637208cdd016de940b5f9c202d00711351e7b784))
* **deps:** bump github.com/hashicorp/go-getter in /tests ([#104](https://github.com/CloudNationHQ/terraform-azure-vm/issues/104)) ([d77904f](https://github.com/CloudNationHQ/terraform-azure-vm/commit/d77904fc33fbb062d4eb36702b8ba47a05500b11))
* **deps:** bump golang.org/x/net from 0.19.0 to 0.23.0 in /tests ([#103](https://github.com/CloudNationHQ/terraform-azure-vm/issues/103)) ([a2cc6e9](https://github.com/CloudNationHQ/terraform-azure-vm/commit/a2cc6e952e8ce87f5593a13e22bd2c7a780c9b9e))
* support multiple IP configurations per interface ([#111](https://github.com/CloudNationHQ/terraform-azure-vm/issues/111)) ([41373cd](https://github.com/CloudNationHQ/terraform-azure-vm/commit/41373cd8b64e1bfb79b333fc6f2ae34b8ee7aee8))

---

