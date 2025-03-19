---
title: Module Specifications
sidebar: mydoc_sidebar
permalink: specs_module_specifications.html
folder: mydoc
---

## Terraform Specific Specification
This page contains the Terraform specific requirements for WAM modules (Resource and Pattern modules) that ALL Terraform WAM modules MUST meet. These requirements are in addition to the Shared Specification requirements that ALL WAM modules MUST meet.

## Shared Requirements (Resource & Pattern Modules)

Listed below are both functional and non-functional requirements for Terraform WAM modules (Resource and Pattern).


## ID: TFFR1 - Category: Composition - Cross-Referencing Modules

Module owners MAY cross-references other modules to build either Resource or Pattern modules. However, they MUST be referenced only by a HashiCorp Terraform registry reference to a pinned version e.g.,

{% include links.html %}
