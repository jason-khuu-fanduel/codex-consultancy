# Specialist routing

Map the complete team from outputs and risk boundaries before spawning, including a separate independent acceptance owner. This is an idea menu, not an organisation chart, installed-agent catalogue, or required staffing list. Match each role to its output, evidence standard, tools, job level, and risk boundary before choosing a title. Launch roles when their inputs are ready. If no pattern fits, define a task-specific persona; if the needed expertise or framing is unclear and materially affects staffing, assign a bounded role-discovery brief before staffing delivery work.

| Need | Role pattern | Owns | Must return |
|---|---|---|---|
| Unknown code or system path | Mapper | entry points, call/state path, side-effect and policy boundaries | exact paths/symbols, confidence, branch points, fastest checks for unknowns |
| Uncertain external fact or API behaviour | Evidence researcher | source-backed claim set | sources, confirmed facts, contradictions, open proof |
| Reproducible defect | Reproducer | minimal reproduction and observed/expected behaviour | steps, environment, evidence, whether reproduced |
| Material proposed idea needs challenge | Hypothesis challenger | fair test of the candidate against evidence and a credible alternative | support/qualify/contradict verdict, evidence, confidence, decision-changing unknowns |
| Missing task framing or expertise | Role scout | the smallest appropriate specialist brief and hiring rationale | candidate role, why it fits, scope, evidence needs, cheaper or simpler alternative |
| Requirement ambiguity | Business analyst | decisions, acceptance criteria, assumptions, and non-goals | clarified scope, decision log, acceptance tests, unresolved choices |
| API or integration change | Contract verifier | caller/provider contract and compatibility risks | inputs/outputs, error cases, versioning risk, proof still needed |
| Data or migration change | Data/migration reviewer | invariants, backfill/rollback safety, and evidence plan | affected data, failure modes, validation and recovery plan |
| Performance concern | Performance investigator | measurement plan and identified bottleneck | baseline, measurement method, evidence, improvement hypothesis |
| Security or privacy boundary | Security/privacy reviewer | threat or data-flow risk assessment | trust boundary, concrete risks, mitigations, residual risk |
| Release or operational change | Deployment reviewer | rollout, observability, and rollback readiness | release checks, monitoring signals, rollback path, blockers |
| User interface risk | Accessibility or UX tester | task-based acceptance and accessibility gaps | flows tested, defects, accessibility evidence, residual risk |
| Bounded implementation | Implementer | one explicit write scope | changes, focused verification, residual risk |
| Cross-cutting change | Boundary specialist | one risky interface: auth, data, async, API, deployment, or privacy | contract/invariants, failure modes, impact on the plan |
| Quality decision | Independent reviewer or SET | acceptance, adversarial or black-box checks | findings with evidence, coverage gaps, verdict, residual risk |
| Incident or confusing failure | Incident investigator | timeline, hypotheses, and proof gaps | evidence timeline, ranked hypotheses, containment or next check |
| Build/tooling disruption | Build or tooling engineer | reproducible diagnosis and minimal repair | reproduction, affected environment, patch or workaround, verification |
| User-facing handoff | Technical writer | operator or user documentation from settled facts | audience fit, procedure, assumptions and missing evidence |

## Routing rules

- Use mapping or evidence research when the change owner or behaviour is uncertain; assign a separate role only when it adds value. Their output is an input to later work, not a proposed patch.
- Use a Boundary specialist only for a material risk boundary; do not split ordinary implementation into artificial specialties.
- Give Implementers disjoint file or subsystem scopes. If the same write scope cannot be separated, sequence the work and name one integration owner, which may be the Manager.
- Give every engagement an Independent reviewer or SET who did not produce the work being accepted. Scale checks to the work; cover a normal path, a failure path, and a relevant integration edge when feasible. This role is at least Mid level.
- Select a Technical writer only when the deliverable needs durable user, operator, API, or decision documentation; do not use one to restate unsettled findings.
- Before inventing a role, check relevant project instructions, existing skills, available tools, and known workflow conventions. Reuse a project-specific capability when it fits; if a delegated role depends on that skill, its brief must require loading it before acting. Do not invent a generic persona that duplicates it.
- Where two candidates seem plausible, prefer the one that can own the smallest decision-changing output with the least handoff cost. Check required access and whether the candidate's prior involvement would compromise independent acceptance. If both roles need the same inputs and would return the same evidence, hire one and refine its brief.
- If the menu lacks a good fit, write a task-specific persona from the template below. If the task itself does not reveal the expertise needed, consider a bounded Role scout assignment only if the Manager cannot resolve the gap efficiently; it recommends a role and brief. Compare a fresh delivery hire with safe reuse using the operating model; retain separate independent acceptance.
- Create a persistent custom agent only after a role pattern has repeated, has stable non-obvious instructions, and cannot be represented as a concise engagement brief. Otherwise use the transient role and the skill's existing reuse pre-check.

## Persona and brief template

Use this for every menu role and every new role. It must describe the work, not merely assert expertise.

```text
Role label: <specific, task-shaped name>
Reports to: <Manager or designated lead>
Runtime: <job level, model, effort, fork, rationale; nested delegation allowed or prohibited>
Persona: You are a <discipline or perspective>. Prioritise <outcome/risk>; be sceptical of <likely failure mode>.
Mission: <one bounded question, artifact, or change>
Why this role: <why this expertise/perspective fits this task now>
Owned output: <decision, evidence package, file scope, or test result>
Inputs: <minimum sources, paths, environment, and upstream results>
Context budget: <first-pass files/sources only; condition for widening the search>
Boundaries: <no-go areas, permissions, read/write scope, and assumptions not allowed>
Quality bar: <observable completion test and evidence required>
Dependencies: <what it waits for and who consumes the result>
Return format: <the applicable result-contract fields, concise>
Stop/escalate: <missing access, conflicting evidence, scope expansion, or repeated failed check that requires handoff>
```

When inventing a persona, use the task's domain, decision, failure modes, and acceptance evidence. Derive job level from the assignment's autonomy, ambiguity, and consequence, not decorative seniority or a generic "expert" label. Select a task-appropriate runtime using the live capabilities and hiring criteria from [model-allocation.md](model-allocation.md).

## Result contract

Every specialist result should be concise and usable by the next role:

```text
Scope covered:
Confirmed evidence:
Inference / assumptions:
Unresolved questions and smallest next check:
Owned artifact or decision:
Verification performed:
Residual risk / handoff:
```

The manager may trim fields that do not apply, but must preserve the separation between evidence, inference, and unknowns.
