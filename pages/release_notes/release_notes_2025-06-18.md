---
title: Releases for 2025-06-18
tags: [releases]
keywords: release notes, announcements, what's new, new features
last_updated: Jul 04, 2025
summary: "Releases of the Terraform Well Architected Modules 2025-06-18"
sidebar: mydoc_sidebar
permalink: release_notes_20250618.html
folder: release_notes
---

# Release Notes for 2025-06-18

## azure-pe
### v2.0.0 (v2.0.0)
**Published at:** 2025-06-18T09:13:29Z

## [2.0.0](https://github.com/CloudNationHQ/terraform-azure-pe/compare/v1.4.4...v2.0.0) (2025-06-18)


### ⚠ BREAKING CHANGES

* The data structure changed, causing a recreate on existing resources.

### Features

* **deps:** bump github.com/gruntwork-io/terratest in /tests ([#47](https://github.com/CloudNationHQ/terraform-azure-pe/issues/47)) ([a57a34a](https://github.com/CloudNationHQ/terraform-azure-pe/commit/a57a34a6097d601f4faa1edafb415c217b39509a))
* **deps:** bump golang.org/x/net from 0.33.0 to 0.36.0 in /tests ([#43](https://github.com/CloudNationHQ/terraform-azure-pe/issues/43)) ([346ab83](https://github.com/CloudNationHQ/terraform-azure-pe/commit/346ab83839f5cc649bbd49666fe6216fd2fb56c3))
* **deps:** bump golang.org/x/net from 0.36.0 to 0.38.0 in /tests ([#45](https://github.com/CloudNationHQ/terraform-azure-pe/issues/45)) ([8517b16](https://github.com/CloudNationHQ/terraform-azure-pe/commit/8517b1649a2d0351b3bc8d1effa1e2bd812aaa35))
* small refactor ([#48](https://github.com/CloudNationHQ/terraform-azure-pe/issues/48)) ([a4b49a3](https://github.com/CloudNationHQ/terraform-azure-pe/commit/a4b49a38ed2d6d9b895f3132eccf85f34321ed0a))

### Upgrade from v1.4.4 to v2.0.0:

- Update module reference to: `version = "~> 2.0"`
- The property and variable resource_group is renamed to resource_group_name
- The structure changed for private_service_connection
- The structure changed for private_dns_zone_group

See the usage examples for details

---

