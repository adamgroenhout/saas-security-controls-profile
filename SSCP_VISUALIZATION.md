# SSCP Configuration Report

**Generated:** 2025-12-05

**Application:** Example App
**Description:** Brief description of the application's purpose, key business context, and primary use cases

## IAM
| Control | Enabled | Value | Exception | Description |
| :--- | :---: | :--- | :---: | :--- |
| identity_federation | ✅ | `saml_2.0` | - | Integration with external Identity Providers (IdP) for centralized authentication. |
| sso_assignment | ✅ | `group_restricted` | - | Policy controlling which IdP users are authorized to access the application. |
| sso_enforcement | ✅ | `strict_enforcement` | - | Disables alternative login methods (e. |
| mfa_local | ✅ | `enforced_all` | - | Requirement for MFA on accounts not managed by SSO (e. |
| least_privilege | ✅ | `rbac_strict` | - | Enforcement of minimal necessary permissions for users and service accounts. |
| account_review | ✅ | `quarterly` | - | Frequency and enforcement of user access reviews. |
| nhi_governance | ✅ | `governed_with_expiration` | - | Governance of service accounts and bots, including expiration and identification. |
| emergency_access | ✅ | `break_glass_accounts` | - | Controls and accounts for regaining access during IdP/SSO failures. |
| provisioning | ✅ | `scim` | - | Methodology for managing user lifecycle (creation, updates, deletion). |
| api_key_policy | ✅ | `strict_rotation` | - | Policies for the lifecycle and security of API keys. |
| password_policy_local | ✅ | `strong` | - | Complexity requirements for local (non-SSO) or emergency break-glass accounts. |
| session_idle_timeout | ✅ | `30` | - | Time of inactivity before the application automatically terminates the session. |
| session_absolute_lifetime | ✅ | `14` | - | Maximum duration of a session regardless of activity (forces token refresh). |
| conditional_access_enforcement | ✅ | `idp_enforced` | - | Enforcement of contextual security signals (Device, Location, Risk) during authentication. |
| ip_allowlist | ✅ | `10.0.0.0/8, 192.168.1.0/24` | - | Restrict user access to the admin console and/or API to specific IP ranges. |

## INTEGRATIONS
| Control | Enabled | Value | Exception | Description |
| :--- | :---: | :--- | :---: | :--- |
| user_consent | ✅ | `disabled` | - | Controls whether users can consent to third-party applications accessing their data. |
| automation_security | ✅ | `managed_only` | - | Controls for third-party automation tools and workflow connectors. |
| connected_apps | ✅ | `[See Details]` | - | Security configuration for external application connections, including account scoping, type, and network restrictions. |

## SHARING
| Control | Enabled | Value | Exception | Description |
| :--- | :---: | :--- | :---: | :--- |
| external_collaboration | ✅ | `authenticated_external_users_only` | - | Controls for file sharing and collaboration with external users. |
| public_link_restriction | ✅ | `internal_only` | - | Prevents users from creating public, anonymous links (e. |
| external_domain_restriction | ✅ | `allowlist_only` | - | Restricts external sharing to specific allowed domains or blocks specific denied domains. |

## DATA
| Control | Enabled | Value | Exception | Description |
| :--- | :---: | :--- | :---: | :--- |
| exfiltration_controls | ✅ | `block_takeout_services` | - | Restrictions on mass data export and third-party backup tools. |
| classification | ✅ | `automated_enforcement` | - | Enforcement of data tagging and classification labels. |
| encryption_at_rest | ✅ | `provider_managed` | - | Encryption standards for data stored within the SaaS provider. |

## CONFIGURATION
| Control | Enabled | Value | Exception | Description |
| :--- | :---: | :--- | :---: | :--- |
| least_functionality | ✅ | `strict_baseline` | - | Disabling unused services and features to minimize attack surface. |

## LOGGING
| Control | Enabled | Value | Exception | Description |
| :--- | :---: | :--- | :---: | :--- |
| audit_logs | ✅ | `comprehensive` | - | Capture of security-relevant events. |
