# Governance user guide

## 1. DARCI
Create a Governance Project, allocate **exactly one Driver** (coordinates), **exactly one Approver** (final decision) and one or more **Responsible** people (execute). Consulted and Informed are optional. Draft projects may have incomplete allocations; moving out of Draft validates them. A person can have multiple roles, but duplicate person/role pairs are rejected.

## 2. Risks
Register each risk, select domain and functional area, assign an owner, score likelihood and impact from 1 to 5. The Risk Score is likelihood × impact (1–25). Add a treatment, mitigation plan and next review date. Daily due-date alerts cover the next 30 days.

## 3. Compliance
Register policies, standards and recurring review dates in Compliance Requirement. Record each assessment and evidence in Compliance Assessment. Non-compliant and partially compliant results require a gap, corrective plan, action owner and target date. Use Governance Control Register for cross-functional review.

## 4. Contracts
Use lifecycle stages Requested → Drafting → Internal Review → Negotiation → Approval Pending → Approved → Signature Pending → Executed → Active. Attach the current draft and a signed copy. Maintain obligation rows with owners, deadlines, status and evidence. Record provider references if signing occurs externally. A contract cannot move to Executed/Active without signed-document attachment; this is **not** signature verification.

## 5. Intellectual property
Create an IP Asset for trademarks, copyrights, publications, methodologies and research. Record registration, evidence, territory, rights and infringement notes. Create separate IP License records for each permitted party and permitted use; active licenses require an agreement attachment. Alerts flag approaching expiry, but do not conduct infringement surveillance.

## 6. Demo
Only run `bench --site SITE execute ubongo_temp.ubongo_governance.demo.install_demo` on a test site. Every synthetic business record uses the `[DEMO]` prefix. Delete demo records before production onboarding.
