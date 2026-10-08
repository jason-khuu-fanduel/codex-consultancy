# Consultancy Agent Workflow

An installable Codex skill for adaptive, manager-led specialist delivery. The repository, marketplace, and plugin identifier remain `codex-consultancy`.

## How it works

- Maps the smallest complete team before work starts, with explicit delivery, integration, and independent acceptance ownership.
- Uses discovery for unresolved material choices and continues already-authorized work without repeated sign-off.
- Separates ownership levels from runtime selection, choosing available models and effort from task evidence rather than fixed model tiers.
- Checks staffing and final handoff, adding independent or intermediate audits when useful.
- Requires a separate acceptance owner for every engagement, with proportionate checks and explicit uncertainty.
- Preserves verified partial results and changes approach after repeated failure.
- Creates reusable skills only when evidence and a concrete future use justify them.
- Uses real telemetry when available and clearly labeled proxies otherwise.

The Manager coordinates and signs off; specialists deliver the work, with a disclosed Manager delivery fallback when capacity requires it. Suitable idle delivery agents can take related assignments with explicit new briefs. Fresh agents provide promoted runtimes or independent acceptance of work they did not contribute to. Capacity limits and rejected hires are reported promptly; cleanup uses only supported release actions and does not assume interruption frees slots. Persistent Goals require explicit requests. The workflow does not expand authorization for publication, external messages, spending, or destructive actions.

## Install

Your Codex account needs GitHub access to this repository.

```sh
codex plugin marketplace add AdamNi-7080/codex-consultancy
codex plugin add codex-consultancy@codex-consultancy
```

Start a new Codex task and invoke `$consultancy-agent-workflow`, or ask for a managed consultancy engagement.

## Update and compatibility

Version 0.1.2 adds adaptive hiring, evidence-based model and effort promotion, proactive safe reuse, and explicit capacity recovery. The skill name remains `consultancy-agent-workflow`. The previous `$consultancy` invocation is replaced by `$consultancy-agent-workflow`; no duplicate alias skill is shipped. Repository, marketplace, and plugin installation identifiers are unchanged.

Refresh your marketplace and update the plugin through your installed Codex plugin management flow, then start a new task to load the revised instructions. This repository update does not itself reinstall plugins or change global configuration.

The workflow instructions can be checked structurally and reviewed against scenarios; improved delivery quality and reduced overhead still need evidence from real engagements.

## Behavior checks

`tests/scenarios.json` contains simulated engagements and a structured decision contract. Have an independent evaluator read the skill and these scenarios, then save its decisions as JSON without seeing `tests/check_decisions.py`. Run `python3 tests/check_decisions.py <decisions.json>` to check observable hiring, recovery, and capacity choices. These are decision simulations, not proof of live runtime behavior. Repeat after material staffing changes; test actual spawning separately in an authorized engagement.
