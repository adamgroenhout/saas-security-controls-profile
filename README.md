# SaaS Security Configuration Baseline

This repository contains a configuration baseline for Software as a Service (SaaS) security. The primary artifact is `saas_security_config.toml`, which captures fundamental security controls, settings, and architectural components necessary for a secure SaaS environment.

## Purpose

The goal of this configuration file is to provide a standardized, machine-readable format for defining and auditing SaaS security posture. It covers critical areas such as:

*   **Identity and Access Management (IAM)**: Federation, MFA, Least Privilege, Account Reviews.
*   **Network Security**: IP Allowlisting, Encryption.
*   **Integrations**: Third-party integration inventory and control.
*   **Configuration Management**: Secure baselines and feature restrictions.
*   **Logging**: Audit logging configuration.

## File Structure

The configuration is written in [TOML](https://toml.io/). Each security control is defined as a table with the following standard fields:

*   **`label`**: A human-readable name for the control.
*   **`description`**: A brief explanation of the control's purpose.
*   **`enabled`** (boolean): Indicates if the control is currently active.
*   **`relevant`** (boolean): Indicates if the control applies to the specific environment.
*   **`value`**: The current configuration setting (string, list, or boolean).
*   **`allowed_values`**: A reference list of standard options or valid formats.
*   **`configuration_details`**: A sub-table containing specific parameters (e.g., URLs, expiry dates, strictness levels).

## Usage

This file can be used as:

1.  **A Policy Reference**: A manual checklist for security administrators to ensure compliance.
2.  **Infrastructure-as-Code Input**: Input for automation tools that configure or audit SaaS platforms via API.
3.  **Audit Artifact**: A snapshot of the intended security configuration for compliance reviews.

## Example

```toml
[iam.mfa_local]
label = "Multi-Factor Authentication (Local Accounts)"
description = "Requirement for MFA on accounts not managed by SSO."
enabled = true
relevant = true
value = "enforced_all"
allowed_values = ["enforced_all", "enforced_admin_only", "optional", "disabled"]
```
