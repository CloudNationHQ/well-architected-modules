---
title: Release Notes for 2024-12-04
tags: [releases]
keywords: release notes, announcements, what's new, new features
summary: "Releases of the Terraform Well Architected Modules"
sidebar: mydoc_sidebar
permalink: release_notes_20241204.html
folder: release_notes
---

## Module: azure-kv
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-kv/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* keys of the secrets changed, which will cause a replacement.

### Features

* small refactor ([#73](https://github.com/CloudNationHQ/terraform-azure-kv/issues/73)) ([bc168d9](https://github.com/CloudNationHQ/terraform-azure-kv/commit/bc168d93f3971000874791abab59e43d3b1d331f))

### Upgrade from v2.2.1 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`

---

**Published at:** 2024-12-04T12:41:40Z

## Module: azure-vm
## [4.3.1](https://github.com/CloudNationHQ/terraform-azure-vm/releases/tag/v4.3.1)


### Bug Fixes

* replace conditional check to contains key instead of lookup for sensitive values ([#158](https://github.com/CloudNationHQ/terraform-azure-vm/issues/158)) ([e27ce60](https://github.com/CloudNationHQ/terraform-azure-vm/commit/e27ce60ccfbcee952bfff78d965ccc05658499fc))

---

**Published at:** 2024-12-04T11:42:11Z

## Module: azure-ca
## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-ca/releases/tag/v3.0.0)


### ⚠ BREAKING CHANGES

* support multiple authentication blocks in jobs ([#47](https://github.com/CloudNationHQ/terraform-azure-ca/issues/47))

### Features

* support multiple authentication blocks in jobs ([#47](https://github.com/CloudNationHQ/terraform-azure-ca/issues/47)) ([ac57e78](https://github.com/CloudNationHQ/terraform-azure-ca/commit/ac57e78538e9ae63f40e76a4f44123c39509b702))

---

**Published at:** 2024-12-04T10:28:56Z

