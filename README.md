# Consultancy Agent Workflow

An installable, host-agnostic skill for adaptive, manager-led specialist delivery. The plugin and marketplace identifier is `agent-consultancy`. The underlying GitHub repository is still named `codex-consultancy` — renaming the repository itself is a separate step and hasn't been done here.

## How it works

- Maps the smallest complete team before work starts, with explicit delivery, integration, and independent acceptance ownership.
- Uses discovery for unresolved material choices and continues already-authorized work without repeated sign-off.
- Separates job levels — ownership, autonomy, and consequence — from runtime selection, choosing available models and effort from task evidence and whatever the live host actually exposes, rather than a fixed model-tier table.
- Checks staffing and final handoff, adding independent or intermediate audits when useful.
- Requires a separate acceptance owner for every engagement, with proportionate checks and explicit uncertainty.
- Preserves verified partial results and changes approach after repeated failure.
- Creates reusable skills only when evidence and a concrete future use justify them.
- Uses real telemetry when available and clearly labeled proxies otherwise.

The Manager coordinates and signs off; specialists deliver the work, with a disclosed Manager delivery fallback when capacity requires it. Suitable idle delivery agents can take related assignments with explicit new briefs. Fresh agents provide promoted runtimes or independent acceptance of work they did not contribute to. Capacity limits and rejected hires are reported promptly; cleanup uses only supported release actions and does not assume interruption frees slots. Persistent Goals require explicit requests. The workflow does not expand authorization for publication, external messages, spending, or destructive actions.

## Install

### Codex

Your Codex account needs GitHub access to this repository.

```sh
codex plugin marketplace add AdamNi-7080/codex-consultancy
codex plugin add agent-consultancy@agent-consultancy
```

Start a new Codex task and invoke `$consultancy-agent-workflow`, or ask for a managed consultancy engagement.

### Claude Code

```sh
claude plugin marketplace add AdamNi-7080/codex-consultancy
claude plugin install agent-consultancy@agent-consultancy
```

Before this repository is pushed, use a local path instead: `claude plugin marketplace add /path/to/codex-consultancy`. Then invoke it the same way — ask for a managed consultancy engagement, or its skill form `consultancy-agent-workflow`. Both manifests pass `claude plugin validate`.

## Portability

The workflow logic itself — staffing, job levels, evidence and acceptance discipline, audits — does not assume any specific model provider or effort vocabulary. [references/model-allocation.md](plugins/agent-consultancy/skills/consultancy-agent-workflow/references/model-allocation.md) resolves concrete models and effort settings from whatever the live host's spawn tool exposes, rather than naming a fixed model family. References to host-specific concepts (a "Plan mode," a "Goal" tool, a particular usage-telemetry call) are phrased so the skill checks what the current host actually provides instead of assuming any one host's own tool names.

The same plugin directory (`plugins/agent-consultancy/`) is packaged for two hosts side by side, and both read the identical `skills/consultancy-agent-workflow/` content:

- **Codex**: `.codex-plugin/plugin.json` + `.agents/plugins/marketplace.json`.
- **Claude Code**: `plugins/agent-consultancy/.claude-plugin/plugin.json` + `.claude-plugin/marketplace.json` at the repo root.

Adding a third host means writing that host's own manifest format next to these two, pointing at the same plugin directory; the skill content underneath needs no further changes.

## Update and compatibility

Version 0.1.2 adds adaptive hiring, evidence-based model and effort promotion, proactive safe reuse, and explicit capacity recovery, and generalizes the workflow to run on any host rather than assuming Codex's own tool names and model family. The skill name remains `consultancy-agent-workflow`. The previous `$consultancy` invocation is replaced by `$consultancy-agent-workflow`; no duplicate alias skill is shipped.

The plugin/marketplace identifier changed from `codex-consultancy` to `agent-consultancy`. If you installed the plugin under the old identifier, uninstall it (`codex plugin remove codex-consultancy@codex-consultancy` or `claude plugin uninstall codex-consultancy@codex-consultancy`) and reinstall under the new one above; a marketplace refresh alone does not rename an already-installed plugin.

Refresh your marketplace and update the plugin through your installed plugin management flow, then start a new task to load the revised instructions. This repository update does not itself reinstall plugins or change global configuration.

The workflow instructions can be checked structurally and reviewed against scenarios; improved delivery quality and reduced overhead still need evidence from real engagements.

## Behavior checks

`tests/scenarios.json` contains simulated engagements and a structured decision contract. Have an independent evaluator read the skill and these scenarios, then save its decisions as JSON without seeing `tests/check_decisions.py`. Run `python3 tests/check_decisions.py <decisions.json>` to check observable hiring, recovery, and capacity choices. These are decision simulations, not proof of live runtime behavior. Repeat after material staffing changes; test actual spawning separately in an authorized engagement.
