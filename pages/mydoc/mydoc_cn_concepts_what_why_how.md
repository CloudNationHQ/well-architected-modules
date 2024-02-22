---
title: What Why How
sidebar: mydoc_sidebar
permalink: mydoc_cn_concepts_what_why_how.html
folder: mydoc
---

## What is Well Architected Modules?
Well Architect Modules (WAM), as "One CloudNation", we want to provide and define the single definition of what a good IaC module is;

How they should be constructed and built
Enforcing consistency and testing where possible
How they are to be consumed
What they deliver for consumers in terms of resources deployed and configured
And where appropriate aligned across public Cloud platforms (e.g. Azure, AWS, etc.).

Our mission is to deliver a comprehensive Well Architected Modules library in multiple IaC repositories, following the principles of the well-architected framework, serving as the trusted Microsoft source of truth. Supported by Microsoft, WAM will accelerate deployment time for Azure resources and architectural patterns, empowering every person and organization on the planet on their IaC journey.

## Definition of "Well Architected" Summary

The modules are supported by CloudNation, across it's many internal organizations, as described in Module Support
Modules are aligned to clear specifications that enforces consistency between all WAM modules. See the 'Specifications & Definitions' section in the menu
Modules will continue to stay up-to-date with product/service roadmaps owned by the module owners and contributors
Modules will align to WAF recommendations. See 'What does WAM mean by "WAF Aligned"?'
Modules will provide clear documentation alongside examples to promote self-service consumption
Modules will be tested to ensure they comply with the specifications for WAM and their examples deploy as intended

## Why Well Architected Modules?

This effort to create Well Architected Modules, with a strategy and definition, is required based on the sheer number of existing attempts from all areas across CloudNation to try and address this same area for our customers and partners. Across CloudNation there are many initiatives, projects and repositories that host and provide IaC modules in several languages. Each of these come with differing code styling and standards, consumption methods and approaches, testing frameworks, target personas, contribution guidelines, module definitions and most importantly support statements from their owners and maintainers.

However, none of these existing attempts have ever made it all the way through to becoming a brand and the go to place for IaC modules from CloudNation that consumers can trust (mainly around longevity and support), build upon and contribute back to.

Performing this effort now to create a shared single aligned strategy and definition for IaC modules from CloudNation, will allow us to accelerate existing and future projects, such as Application Landing Zone Accelerators (LZAs), as well as providing the building blocks via a library of modules, in the language of the consumers choice, that is consistent, trusted and supported by CloudNation. This all leads to consumers being able to accelerate faster, no matter what stage of their IaC journey they are on.

We have seen over the past FY that this topic alone is important and is one that has led to confusion and frustration to customers who are consuming modules developed by individuals. CloudNation build on an community to create more Well Architected Modules

## How will we create, support and enforce Well Architected Modules?
Well Architected Modules will achieve this, and its mission statement, by implementing and enforcing the following; driven by the WAM Core Team:

Publishing WAM modules to their respective public registries for consumption
For Terraform this will the HashiCorp Terraform Registry
Creating, publishing and maintaining the Well Architected Modules specifications (this site)
Including IaC language specific specifications (today Terraform)
Creating easy to follow WAM module contribution and publishing guidance for each IaC language (today Terraform)
Enforcing tests for each WAM module is compliant with the WAM specifications, where possible, via Unit and Integration tests
Enforcing End-to-End Deployment tests of each WAM module
Providing, and backing, a long-term support statement, regardless of the WAM module's ownership status
Backed by the WAM Core Team of CloudNation

{% include links.html %}
