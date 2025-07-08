---
title: Releases for 2024-12-04
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 08, 2025
summary: "Releases of the Terraform Well Architected Modules 2024-12-04"
sidebar: mydoc_sidebar
permalink: release_notes_20241204.html
folder: release_notes
---

# Release Notes for 2024-12-04

## azure-kv
### v3.0.0 (v3.0.0)
**Published at:** 2024-12-04T12:41:40Z

## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-kv/compare/v2.2.1...v3.0.0) (2024-12-04)


### ⚠ BREAKING CHANGES

* keys of the secrets changed, which will cause a replacement.

### Features

* small refactor ([#73](https://github.com/CloudNationHQ/terraform-azure-kv/issues/73)) ([bc168d9](https://github.com/CloudNationHQ/terraform-azure-kv/commit/bc168d93f3971000874791abab59e43d3b1d331f))

### Upgrade from v2.2.1 to v3.0.0:

- Update module reference to: `version = "~> 3.0"`

---

## azure-vm
### v4.3.1 (v4.3.1)
**Published at:** 2024-12-04T11:42:11Z

## [4.3.1](https://github.com/CloudNationHQ/terraform-azure-vm/compare/v4.3.0...v4.3.1) (2024-12-04)


### Bug Fixes

* replace conditional check to contains key instead of lookup for sensitive values ([#158](https://github.com/CloudNationHQ/terraform-azure-vm/issues/158)) ([e27ce60](https://github.com/CloudNationHQ/terraform-azure-vm/commit/e27ce60ccfbcee952bfff78d965ccc05658499fc))

---

## azure-ca
### v3.0.0 (v3.0.0)
**Published at:** 2024-12-04T10:28:56Z

## [3.0.0](https://github.com/CloudNationHQ/terraform-azure-ca/compare/v2.1.1...v3.0.0) (2024-12-04)


### ⚠ BREAKING CHANGES

* support multiple authentication blocks in jobs ([#47](https://github.com/CloudNationHQ/terraform-azure-ca/issues/47))

### Features

* support multiple authentication blocks in jobs ([#47](https://github.com/CloudNationHQ/terraform-azure-ca/issues/47)) ([ac57e78](https://github.com/CloudNationHQ/terraform-azure-ca/commit/ac57e78538e9ae63f40e76a4f44123c39509b702))

---

