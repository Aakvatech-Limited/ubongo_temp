# Finance and integrations

Five provider registry examples: ApprovalMax, Everhour, Gusto, Google Drive, Payroll Software. Configurations default to disabled, secret values use Password fields, and no real API synchronization, webhook, OAuth or approval integration exists yet. Each vendor requires adapter implementation, authorization, response handling, audit trail and independent testing.

Bank Feed Connection accepts BRA, CRDB and Stanbic as requested names. Bank Feed Entry stages transactions using external transaction ID deduplication. No real feed, bank authorization, statement importer, or ERPNext Bank Transaction posting is implemented. Verify the exact BRA bank identity with the customer before implementing its connector.

Budget Variance Review accepts manual review-period budgets and actuals. Variance = actual minus budget; favourability is category-aware. Budget Variance Summary reports saved reviews. Periodic automatic extraction from ERPNext accounting/budget records is pending.

Financial Forecast supports Base, Optimistic, Pessimistic or Custom scenarios. Each monthly category line has a baseline, percentage change and manual adjustment; forecast = baseline × (1 + percent/100) + adjustment. Financial Scenario Comparison compares saved scenarios. Net = revenue minus costs in the same currency and should not be interpreted as a complete three-statement forecast or precise cash flow.

Run on a **development site only**:

```sh
bench --site SITE execute ubongo_temp.governance.finance_demo.install_finance_demo
```

Seeds disabled provider configurations, three synthetic bank feed connections and entries, three one-month TZS forecasts, and a BVA. Entries are labeled [DEMO]; no bank credentials and no accounting transactions are generated.

Before production: validate migrations, secure permissions, build vetted provider-specific API adapters, accounting import and reconciliation, periodic scheduler, full dashboards and export native v16.50 Sidebar/Dock through Developer Mode.
