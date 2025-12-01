# SaaS Security Controls Profile (SSCP)

## Overview

This repository provides a comprehensive template for defining and managing security configurations for SaaS applications. The core of this project is the `sscp-template.toml` file, which serves as a structured baseline for security controls across various domains.

## Features

The configuration template covers the following key security domains:

*   **Identity and Access Management (IAM):** Federation, SSO, MFA, Least Privilege, Emergency Access, and Provisioning.
*   **Integrations:** Controls for third-party apps, user consent, and automation security.
*   **Sharing and Collaboration:** External sharing policies, link restrictions, and domain allowlists.
*   **Data Security:** Exfiltration controls, data classification, and encryption.
*   **Configuration Management:** Least functionality and baseline enforcement.
*   **Logging and Monitoring:** Audit log retention and SIEM export settings.

## Structure

The `sscp-template.toml` file is organized into sections corresponding to the domains listed above. Each control includes standard metadata fields:

*   `description`: What the control does.
*   `relevant`: Whether the control applies to the specific application.
*   `enabled`: Current implementation status.
*   `value`: The configured setting.
*   `allowed_values`: Acceptable options for the setting.
*   `exception`: Tracks if a policy exception exists.
*   `configuration_details`: Granular settings and parameters.

## Usage

1.  Copy `sscp-template.toml` to your project or configuration repository.
2.  Update the `[meta.application]` section with your specific application details (Name, Owner, Risk Classification).
3.  Review each control section and adjust relavent values to match your organization's security policy and the state of the subject application to reflect the current state. 
4.  Define the target state for your app(s) and update the SSCP overtime to maintain an understanding of security posture and to track and manage improvement. 

## Validation

The template is written in TOML. You can validate the syntax using Python's `tomllib` (available in Python 3.11+).

```python
import tomllib

with open("sscp-template.toml", "rb") as f:
    config = tomllib.load(f)
    print("Configuration loaded successfully.")
```
