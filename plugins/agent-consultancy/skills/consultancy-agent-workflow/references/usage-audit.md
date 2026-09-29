# Usage and execution audit

The audit checks efficiency without redoing domain work except for necessary sampling. The Manager can perform it; use an independent Auditor when that adds value. Inspect the live tool catalog and available telemetry, not merely documentation. If reads fail or sources are absent, name the gap and continue in proxy mode rather than inventing counters or blocking delivery.

## Live usage and billing evidence

At staffing and final handoff, and at justified intermediate audits, collect a fresh read-only usage snapshot when accessible before making usage-based recommendations. Combine adjacent checks where no meaningful execution intervened; do not poll continuously.

1. Discover any installed Usage & Billing skill/plugin and read its instructions if available. Use its applicable read-only token, usage, and billing tools. Check the active tool catalog (and tool search if supplied); do not equate an absent skill name with absent telemetry.
2. Call whatever read-only account/usage-limits tool the live host exposes, if any (for example a `get_usage_limits`-style call). If only the Manager can access it, have the Manager read it and send the Auditor a timestamped, minimized snapshot. When the host offers both a per-bucket/per-window representation and a flattened legacy one, prefer the per-bucket form and use the legacy form only as fallback; never sum both representations of the same data. For each available bucket/window record the used percentage, remaining percentage clamped to 0–100, window duration, and reset time converted to a common timezone. Missing fields mean unavailable, not zero.
3. Obtain task/agent token counters through the installed usage capability or runtime telemetry when exposed. Use `get_goal` only for an existing relevant goal; do not create a goal to manufacture telemetry. Record source, timestamp, attribution scope, and whether counters include descendants. Preserve input, cached-input, output, and reasoning distinctions where supplied; avoid double-counting cumulative snapshots or overlapping totals.
4. Compare current and previous readings only within the same source, scope, bucket, and reset window. Account limits are shared across tasks: percentage changes are not this team's token consumption. Account percentages cannot be converted into token counts or billing spend. Report actual token/cost data only when supplied by an applicable source; otherwise mark it unavailable. Do not substitute one billing model's figures for another's — for example, an API or usage-based account's billing data is not equivalent to a seat- or subscription-based account's usage, and the two must not be mixed.
5. Base recommendations on evidence: remove duplicated work, reduce oversized context, adjust model or effort when task evidence and verification support it, or sequence noncritical agents when limits tighten. Protect independent acceptance and its criteria. Give the observation, affected agents, proposed change, and expected directional effect; never claim measured savings without measured attribution.

If a named plugin is absent, report that fact and use available native telemetry. Do not install an invented dependency or invoke resets, credit purchases, plan changes, or other billing mutations as part of an audit. Persist only compact aggregate readings needed for checkpoint comparisons, not account identifiers or raw usage payloads.


## Audit decision

Inspect ownership levels, task fit, model/effort decisions and actual spawn settings, context size, duplicate investigation, idle handoffs, repeated failures, discarded work, and verification gaps. Check capacity reporting, cleanup outcomes, and whether any reuse respected runtime fit and independent acceptance. In proxy mode these support qualitative recommendations only, not token figures, utilization percentages, prices, or measured savings. Account telemetry can coexist with proxy-based task-efficiency findings; label each scope accurately.

Return concisely:

```text
Data basis: telemetry | proxies | mixed, with scopes
Source and timestamp: tools actually called; missing or failed sources
Snapshot/delta: comparable counters/windows only; attribution limitations
Findings: observed waste or quality risk with evidence
Actions: affected owners, change, and directional expected effect
Next checkpoint: event if needed
```

The Manager accepts, modifies, or rejects actionable recommendations, recording reasons for material decisions and broadcasting adopted guidance to affected agents. Cost optimization cannot override user intent, correctness, necessary review, or authorization. Never claim measured savings without measured attribution.
