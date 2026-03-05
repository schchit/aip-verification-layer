# AIP v1alpha3 Auxiliary Verification Layer

This repository defines a **non-invasive** verification mapping for AIP v1alpha3. HJS acts as a downstream observer (Auxiliary Verifier) that derives structured evidence from native AIP audit logs.

## Core Principles
* **Zero Extension:** No changes required to AIP v1alpha3 schema.
* **AIP-First:** Respects AIP as the foundation for identity and policy.
* **Logic Inference:** Derives Judgment and Termination states from existing audit fields.

## Navigation
* `/mappings`: Detailed field-level logic for v1alpha3.
* `/examples`: Samples of native AIP logs and their derived verification results.

## Logical Binding & Relay Protection
To address the Relay Attack vulnerabilities recently identified in various AI attestation implementations (e.g., as highlighted by Usama Sardar), this verification layer introduces Logical Binding:
Evidence Freshness: By mapping the native AIP aat_jti (unique identifier) and timestamp to the HJS Judgment event, the layer ensures that each authorization is fresh and cannot be reused.
Session Anchoring: The HJS logic binds cryptographic evidence to the specific session_id found in the AIP audit trail, preventing evidence from being replayed in different communication contexts.
Policy Integrity: By including the policy_hash in the derived evidence, HJS ensures that the authorization is only valid for the specific intended logic, providing protection even if transport keys are compromised.
