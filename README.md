# AIP v1alpha3 Auxiliary Verification Layer

This repository defines a **non-invasive** verification mapping for AIP v1alpha3. HJS acts as a downstream observer (Auxiliary Verifier) that derives structured evidence from native AIP audit logs.

## Core Principles
* **Zero Extension:** No changes required to AIP v1alpha3 schema.
* **AIP-First:** Respects AIP as the foundation for identity and policy.
* **Logic Inference:** Derives Judgment and Termination states from existing audit fields.

## Navigation
* `/mappings`: Field-level logic for v1alpha3 alignment.
* `/examples`: Samples of native AIP logs and derived results.
* `/tools`: Minimal Python connector for logic demonstration.
