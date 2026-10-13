app_name = "ubongo_temp"
app_title = "Ubongo Governance"
app_publisher = "Aakvatech Limited"
app_description = "DARCI, risk, compliance, contract, and intellectual property governance"
app_email = "info@aakvatech.com"
app_license = "MIT"
required_apps = ["frappe"]
add_to_apps_screen = [{"name": "ubongo_temp", "logo": "/assets/ubongo_temp/images/governance.svg", "title": "Ubongo Governance", "route": "/app/governance-overview"}]

doc_events = {
    "Governance Project": {"validate": "ubongo_temp.governance.validation.validate_darci"},
    "Governance Risk": {"validate": "ubongo_temp.governance.validation.validate_risk"},
    "Governance Contract": {"validate": "ubongo_temp.governance.validation.validate_contract"},
    "IP License": {"validate": "ubongo_temp.governance.validation.validate_license"},
    "Compliance Assessment": {"validate": "ubongo_temp.governance.validation.validate_assessment"},
}
scheduler_events = {"daily": ["ubongo_temp.governance.monitoring.check_governance_alerts"]}
