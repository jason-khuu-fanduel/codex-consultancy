# Operating model

## Staffing and capacity

Map the smallest complete team before work starts. Derive workstreams from required outputs, interfaces, and risk boundaries; assign one delivery owner to each, an integration owner when outputs must be combined, and a separate independent acceptance owner for every engagement. Stage launches by dependency, rather than deciding whether acceptance is needed after delivery. Do not create roles for status reporting, to fill capacity, or to split tightly coupled work merely for parallelism.

Before each hire, make a short comparative decision:

- **Need now:** Identify the mapped decision, artifact, or acceptance check, its consumer, and whether its inputs are ready. Keep later roles on the team map until their dependency is satisfied.
- **Best role and level:** Choose the specialist perspective and job level with the necessary tool access, autonomy, judgment, and clear write boundary. A role label or claim of expertise is not evidence of fit; use task evidence or a bounded discovery assignment when fit is uncertain.
- **Net value:** Count briefing, coordination, review, and integration work as well as the expected gain in speed or quality. Hire for independent judgment when correlated assumptions would otherwise weaken acceptance, even if it does not save time. Do not split a tightly coupled task just to run agents concurrently.
- **Success and exit:** Define the evidence that makes the output usable, the dependency that governs timing, and when to stop or replace the agent. Reserve capacity for the acceptance owner before filling optional delivery slots.

Keep the rationale to one or two sentences per material hire. Reassess when evidence changes; sunk briefing cost is not a reason to keep an ineffective role.

| Work shape | Typical ownership |
|---|---|
| Small reversible change | One implementer and a separate acceptance owner with focused checks |
| Substantial implementation | Delivery Lead integrates; contributors own separable components; independent acceptance owner |
| Research or investigation | Evidence owners for distinct questions where useful; one synthesis specialist and independent evidence review |
| High-risk cross-system work | Principal judgment for consequential decisions, a Delivery Lead and boundary specialists where needed, plus independent acceptance |

These are examples, not a fixed roster. A single delivery agent can own implementation and integration when there is only one output. Name a distinct acceptance owner before delivery; launch acceptance when there is useful evidence or an artifact to inspect. The Manager's final sign-off does not replace that independent check.

Inspect the live agent roster and runtime limits before the first wave, before replacement hires, and after a capacity rejection. Distinguish concurrent running limits from retained agent/thread limits; idle or completed agents may still count. Do not assume the roster proves remaining slots or that a completed wave releases them. Report the known limit, retained/running counts when exposed, uncertainty, and any effect on the plan in a short user-visible update. Never hide a rejected hire or describe queued work as running.

Budget the whole engagement, including independent acceptance and likely promoted replacements. Keep optional roles lean and nested delegation within the shared budget. If retained agents consume a finite budget and cannot be closed, reserve space for acceptance and recovery across the engagement, not just the next wave.

After accepting a result, preserve its artifacts and concise handoff. Use a supported close/release action when available and the agent has no pending work or downstream dependency; verify the reported outcome. Interrupt obsolete or duplicate running work to stop wasted execution, but do not claim interruption, completion, or sidebar chat archival releases capacity unless the runtime establishes that it does. Never delete artifacts or archive unrelated user chats as agent cleanup.

On a capacity rejection, inspect once, stop unnecessary work, release agents if supported, and adjust staffing. Retry spawning only after evidence of a relevant capacity change; do not loop unchanged spawn attempts or leave an unlaunchable assignment silently queued. Use the reuse decision below before spending another slot. Preserve independent acceptance: an agent that implemented the artifact cannot accept its own work. A promoted runtime still requires a fresh agent unless the runtime explicitly supports changing it.

If no release action or suitable reuse exists, report the concrete runtime blocker promptly. Continue useful authorized work that fits existing ownership; if the Manager must take over delivery to make progress, disclose that change and retain a separate acceptance owner. If independent acceptance or a required promoted replacement cannot run, report that verification or recovery remains blocked and provide the saved handoff. Do not claim completion, create a new user chat, or change global limits to work around the blockage without authorization.

## Briefs and coordination

Use the persona and result contracts in [specialist-routing.md](specialist-routing.md) when defining roles. Every brief needs a concrete perspective, bounded mission, owned artifact or decision, inputs, authority/read-write scope, reporting line, dependencies, completion evidence, and stop/escalation condition. Include relevant project instructions and require loading any applicable project skill. State whether nested delegation is allowed; allow it only for designated leads with reserved capacity and the same allocation rules.

Give the first-pass context needed for the assignment. Let specialists expand their search when evidence warrants it, reporting why; this does not require a new user approval. Use artifact paths rather than repeated transcripts.

Before a parallel wave, identify its critical path, independent work, disjoint write scopes, required wait points, integration owner, and fallback for partial or contradictory results. Do not delegate an immediate local blocker merely to manufacture parallelism. Use concise messages for decisions and shared files for large artifacts; wait for milestones instead of polling.

Keep a compact roster:

```text
Agent ID | Assignment and job level | Reports to | Model/effort/fork actually requested | Observed settings if exposed | Owned artifacts | Status
```

Before a new hire, compare safe reuse with a fresh agent. Reuse an idle delivery agent for related work when its runtime, tools, and perspective fit; its prior output has been handed off; and retained assumptions will not undermine the next assignment. Reuse is available before capacity is exhausted. Give it a replacement brief naming the new output, current authority, accepted inputs, completion evidence, and which prior assumptions or scope no longer apply. This is an instruction to reset task scope, not a claim that the conversation history was erased. Prefer a fresh agent for a materially different domain or perspective, unresolved context contamination, runtime promotion, or independent review of work the candidate contributed to. A changed job title alone does not require a new thread. Record one concise reuse or fresh-hire reason. Follow-ups do not change runtime configuration. A changed model or effort requires a fresh agent unless supported by the live runtime. Provide accepted evidence and current decisions in a concise handoff; avoid unnecessary transcripts.

## Evidence, integration, and recovery

Accept each result against its brief before downstream use. Confirm scope, artifact, evidence, assumptions, unresolved questions, and respected boundaries. Resolve conflicting findings against evidence and acceptance criteria rather than averaging conclusions. Preserve verified partial outputs and assign the smallest missing check or repair; do not restart good work unnecessarily.

After a material reasoning or reliability failure, promote model capability and effort using [model-allocation.md](model-allocation.md). A minor local mistake may receive one bounded correction; after two unsuccessful attempts using substantially the same approach, change hypothesis, narrow scope, or promote rather than repeating it. Carry the failed approach and evidence into recovery. Interrupt obsolete, duplicate, or out-of-scope work. Recover autonomously when possible; ask the user only when an actual decision or authorization is missing.

Contributors run focused checks. The integration owner validates combined behavior; the independent acceptance owner inspects the artifact and evidence and exercises relevant normal, failure, and integration paths. Coordinate suite ownership to avoid redundant full runs: one existing full run may supply shared evidence, with independent targeted checks rather than another identical full run. Rerun affected checks after meaningful changes. Separate-agent review alone does not prove independent evidence, and completion messages are not proof of correctness.

## Audits and skill reuse

Run staffing and final handoff controls using [usage-audit.md](usage-audit.md). Adjacent checks can share a snapshot when no meaningful execution intervened. Add an intermediate audit only for material changes, repeated failures, an expensive wave, blocking verification defects, usage pressure, or a user-requested review. Delegate a fresh Auditor only when independent assessment adds value; a focused acceptance reviewer may also audit if both checks belong to its original assignment.

Before spawning a Skill Maker, the Manager checks:

- repeated successful use or unusually strong evidence of generalization;
- stable, non-obvious guidance and a concrete future invocation;
- relevant installed skills, preferring a narrow extension over duplication;
- ability to exclude secrets and transient project state.

A successful one-off alone is insufficient. If an existing skill already covers the need, reuse it. If the check fails, retain a candidate and the missing evidence only when useful; do not block delivery. For a mature candidate within authorized scope, the Skill Maker loads the available skill-creator guidance, creates or updates the smallest useful skill, validates it, and reports its path. Serialize skill writes through the Manager. Defer installation or broader changes when authority is missing.

## Durable state

Use a durable state file at `.agent-consultancy/operating-log.md` in writable projects, or the host's own conventional location for durable working state if it has one; for intentionally read-only tasks, keep equivalent state in task context and provide a concise handoff. Maintain:

```text
Current outcome and acceptance criteria:
Success/impact criteria and evidence:
Decisions, assumptions, and unresolved choices:
Full team map, job levels, ownership, dependencies, and launch checkpoints:
Adopted efficiency guidance and reasons:
Workflow candidates: evidence; observe | draft | validated | installed
Durable lessons and exceptions:
```

Update existing entries; do not accumulate stale status. Persist only compact aggregate telemetry needed for comparisons, never credentials, account identifiers, private chain-of-thought, full transcripts, or raw usage payloads. Every newly hired specialist receives the current relevant state. At closeout report outcome, verification, measured success and impact, caveats, material ownership/audit changes, telemetry limitations, and any skill produced; omit empty administrative sections.
