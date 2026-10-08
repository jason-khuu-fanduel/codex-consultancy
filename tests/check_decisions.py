"""Check observable decisions from independent, simulated skill evaluations."""
import json
import sys
from pathlib import Path


def check(payload):
    expected = {
        "inherit": "inherit", "promote": "promote",
        "tool_failure": "repair_inputs", "reuse": "reuse",
        "independence": "fresh_acceptance", "exhausted": "report_blocker",
        "release": "release_then_spawn", "contamination": "fresh",
    }
    decisions = payload["decisions"]
    by_id = {d["id"]: d for d in decisions}
    failures = []

    def require(condition, message):
        if not condition:
            failures.append(message)

    require(len(by_id) == len(decisions), "Duplicate scenario decisions")
    require(set(by_id) == set(expected), "Missing or unexpected scenarios")
    for name, action in expected.items():
        if name not in by_id:
            continue
        d = by_id[name]
        require(d.get("action") == action, f"{name}: incorrect recovery/hiring action")
        require(bool(d.get("reason")), f"{name}: missing decision rationale")
        require(d.get("retry_without_change") is False, f"{name}: unchanged retry")
        require(d.get("independent_acceptance") is True, f"{name}: lost acceptance boundary")
        if name != "release":
            require(d.get("claim_slot_freed") is False, f"{name}: unsupported slot-release claim")
    if "inherit" in by_id:
        d = by_id["inherit"]
        require(d.get("model") == "inherited" and d.get("effort") == "inherited",
                "inherit: unnecessary model/effort override")
        require(d.get("fork") == "all", "inherit: necessary full context lost")
    if "promote" in by_id:
        d = by_id["promote"]
        require(d.get("model") in {"workhorse", "frontier"}, "promote: capability not raised")
        require(d.get("effort") in {"medium", "high"}, "promote: effort not raised")
        require(d.get("fork") in {"none", "partial"}, "promote: incompatible override fork")
        require(d.get("preserve_work") is True, "promote: valid evidence discarded")
    if "exhausted" in by_id:
        require(bool(by_id["exhausted"].get("user_update")), "exhausted: capacity blocker hidden")
        require(by_id["exhausted"].get("preserve_work") is True, "exhausted: handoff lost")
    if "release" in by_id:
        require(by_id["release"].get("claim_slot_freed") is True,
                "release: confirmed slot release not recognized")
    return failures


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: python3 tests/check_decisions.py <decisions.json>")
    failures = check(json.loads(Path(sys.argv[1]).read_text()))
    if failures:
        sys.exit("\n".join(failures))
    print("PASS: all 8 simulated staffing/recovery decisions")
