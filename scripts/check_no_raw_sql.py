"""Reject direct SQL execution without an explicitly reviewed exception."""
import ast
from pathlib import Path

ROOT = Path("ubongo_temp")
BLOCKED = {
    "frappe.db.sql",
    "frappe.db.multisql",
    "frappe.db.sql_ddl",
    "frappe.db.execute_query",
}
bad = []
for path in sorted(ROOT.rglob("*.py")):
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except SyntaxError as exc:
        bad.append(f"{path}:{exc.lineno}: invalid Python: {exc.msg}")
        continue
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        target = node.func
        parts = []
        while isinstance(target, ast.Attribute):
            parts.append(target.attr)
            target = target.value
        if isinstance(target, ast.Name):
            parts.append(target.id)
        name = ".".join(reversed(parts))
        if name in BLOCKED or name.endswith(".cursor.execute") or name.endswith("._cursor.execute"):
            bad.append(f"{path}:{node.lineno}: forbidden SQL execution: {name}")
if bad:
    print("\n".join(bad))
    raise SystemExit(1)
print("No forbidden direct SQL execution detected.")
