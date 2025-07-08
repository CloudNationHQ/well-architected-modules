---
title: Module Types
sidebar: mydoc_sidebar
permalink: terraform_module_types.html
folder: mydoc
---

## Module Types
WAM defines two module types (classifications), Resource Modules and Pattern Modules, that can be created, published, and consumed.

### Resource Modules

**Definition:**  
Resource Modules are self-contained Terraform modules designed to provision and manage specific Azure resources and their extensions in a consistent, repeatable manner.

**Purpose:**  
- Standardize the deployment of Azure resources.
- Promote reuse and reduce duplication by encapsulating best practices for resource configuration.
- Simplify lifecycle management by grouping related resources.

**Key Characteristics:**  
- **Lifecycle Cohesion:** All resources within a Resource Module share the same lifecycle (created, updated, or destroyed together).
- **Parent-Child Relationships:** Modules often combine parent resources with their dependent child resources (e.g., an Azure Key Vault with its secrets, or a Storage Account with its containers and blobs).
- **Logical Grouping:** Resources that are interdependent or commonly deployed together are logically grouped.
- **Parameterization:** Expose input variables for customization while enforcing sensible defaults and validation.
- **Outputs:** Provide outputs for integration with other modules or higher-level patterns.
- **Documentation:** Include clear usage instructions, examples, and descriptions of inputs/outputs.

**Availability:**  
- **Open Source:** Resource Modules are published publicly, encouraging community collaboration, peer review, and reuse.
- **Versioned:** Modules are versioned to ensure stability and traceability.

**Example Use Cases:**  
- Deploying a secure Azure Storage Account with default encryption and network rules.
- Provisioning an Azure Key Vault with pre-configured access policies and secrets.

---

### Pattern Modules

**Definition:**  
Pattern Modules are higher-level Terraform modules that orchestrate multiple Resource Modules and additional components to deliver complete architectural patterns or solutions.

**Purpose:**  
- Enable rapid deployment of complex solutions by composing Resource Modules and other resources.
- Capture and enforce organizational standards, business logic, and architectural best practices.
- Abstract complexity and provide opinionated, ready-to-use patterns.

**Key Characteristics:**  
- **Composition:** Primarily built by combining multiple Resource Modules, but may also include scripts (e.g., PowerShell), configuration files (e.g., Dockerfiles), or other resources.
- **Business Logic:** Often encapsulate proprietary logic, workflows, or compliance requirements.
- **Customization:** Expose parameters for solution-level customization while hiding underlying complexity.
- **Integration:** May integrate with external systems, CI/CD pipelines, or organizational processes.
- **Documentation:** Provide detailed guidance on usage, customization, and integration points.

**Availability:**  
- **Private:** Pattern Modules are usually maintained privately within an organization, as they may contain sensitive or proprietary logic.
- **Controlled Access:** Access is restricted to authorized teams or users.

**Example Use Cases:**  
- Deploying a secure web application pattern that includes networking, storage, compute, monitoring, and security controls.
- Implementing a standardized landing zone for new projects, enforcing organizational policies and guardrails.

---

### Summary Table

| Aspect                | Resource Modules                                  | Pattern Modules                                   |
|-----------------------|---------------------------------------------------|---------------------------------------------------|
| **Scope**             | Single resource or tightly coupled resources      | Multiple modules and resources (solution-level)   |
| **Purpose**           | Standardize resource deployment                   | Deliver architectural patterns and solutions      |
| **Availability**      | Public, open source                              | Private, organization-specific                    |
| **Business Logic**    | Minimal, focused on resource configuration        | May include significant business logic            |
| **Reusability**       | High, across projects and teams                   | High within organization, less across orgs        |
| **Examples**          | Key Vault module, Storage Account module          | Secure web app pattern, landing zone pattern      |

---

### When to Use Each Module Type

- **Resource Modules:**  
    Use when you need to deploy, manage, or reuse a specific Azure resource or a tightly coupled set of resources. Ideal for building blocks in your infrastructure-as-code strategy.

- **Pattern Modules:**  
    Use when you want to deploy a complete solution or architectural pattern that combines multiple resources, enforces standards, or implements business logic. Ideal for accelerating project setup and ensuring compliance.

---

**Note:**  
In WAM documentation, the term "module" or "Well-Architected-Module" typically refers to **Resource Modules** unless otherwise specified.

{% include links.html %}
