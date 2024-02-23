---
title: Contributing
sidebar: mydoc_sidebar
permalink: mydoc_cn_contributing_module_contributing.html
folder: mydoc
---

## contributing

This page provides an overview of the contribution process for WAM modules.

## New Module Proposal & Creation

Each WAM module MUST have a Module Proposal issue created and approved by the WAM core team before it can be created or changed!

## WAM Framework

All module MUST be published as a pre-release version (e.g., 0.1.0, 0.1.1, 0.2.0, etc.)
Consumers should also read the release notes for each version, if considering updating to a more recent version of a module to see if there are any considerations or breaking changes etc.

## Module Owner Has Issue/Is Blocked/Has A Request

In the event that a module owner has an issue or is blocked due to specific WAM missing guidance, test environments, permission requirements, etc. they should follow the below steps:

Common issues/blockers/asks/request are:

Subscription level features
Resource Provider Registration
Preview Services Enablement
Entra ID (formerly Azure Active Directory) configuration (SPN creation, etc.)

Create a GitHub Issue
Discuss the issue/blocker with the WAM core team
Agree upon action/resolution/closure
Implement agreed upon action/resolution/closure

Please note for module specific issues, these should be logged in the module’s source repository

## Terraform Contribution Guide

Before submitting a new module proposal for Terraform, please review the FAQ section on “CARML/TFWAM to WAM Evolution Details”

While this page describes and summarizes important aspects of contributing to WAM, it only references some of the shared and language specific requirements.

Therefore, this contribution guide MUST be used in conjunction with the Shared Specification and the Terraform specific specifications. ALL WAM modules (Resource and Pattern modules) MUST meet the respective requirements described in these specifications!

This section lists WAM’s Terraform-specific contribution guidance.

Prerequisites
Composition
Terraform contribution flow

{% include links.html %}
