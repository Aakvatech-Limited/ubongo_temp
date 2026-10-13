# Governance Risk — five-star assessment

Likelihood and Impact are Frappe Rating controls with five stars each, preserving their original fieldnames.

Frappe stores one filled star as 0.2, three stars as 0.6, and five stars as 1.0. Half stars are supported. Risk Score = (likelihood × 5) × (impact × 5), yielding 1–25, potentially in quarter-point steps. The score is read-only and automatically recalculated on save.

No existing risk data needs conversion, so there are no additional migration fields or backfill patches. Use `bench --site SITE migrate` after updating the app. Demo risk is configured for three-star likelihood and four-star impact (score 12).

No raw SQL is used.
