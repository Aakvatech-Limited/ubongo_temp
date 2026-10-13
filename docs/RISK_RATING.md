# Governance Risk — five-star assessment

Likelihood and Impact are interactive five-star Rating controls. Frappe stores Rating as a fraction: one star = 0.2 and five stars = 1.0. Half stars are supported. Risk Score = (Likelihood Rating × 5) × (Impact Rating × 5), with a possible range of 1 to 25. Score uses a Float field to preserve half-star precision.

The previous `likelihood` and `impact` integer fields are retained but hidden for backward compatibility and set to nearest whole star on save. Existing records are initialized from the previous integer values by the post-model-sync patch `ubongo_temp.patches.v16_0.backfill_governance_risk_stars`. No raw SQL is used.

Run `bench --site SITE migrate`, then check existing 1-star, 3-star and 5-star risks and edit a half-star value. The star values should be authoritative for new records.
