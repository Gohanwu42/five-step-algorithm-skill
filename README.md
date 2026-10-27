# Five-Step Algorithm

A practical skill for turning a task, project, or real-world problem into useful, verified progress.

**Question requirements → Delete unnecessary work → Simplify → Accelerate → Automate where worthwhile.**

The skill helps an assistant apply that sequence and complete authorized work. It supports new tasks as well as existing processes. For physical tasks or work outside its tools, it prepares the next action and explains how the user can verify the result. It is a way to organize action, not a substitute for domain expertise or evidence.

## Use

Install the `five-step-algorithm/` folder using your agent's skill installation mechanism, then invoke it by name. The folder follows the [Agent Skills format](https://agentskills.io/specification); discovery and installation depend on the client. `agents/openai.yaml` supplies optional Codex interface metadata. No API key or additional service is required by the skill.

Example requests:

```text
Use $five-step-algorithm to turn these notes into a one-page meeting brief.
Create the brief, and check it against the decisions we need to make.
```

```text
Use $five-step-algorithm to help me clear my spare room this weekend.
I have two hours and cannot discard anyone else's belongings.
```

```text
Use $five-step-algorithm on our weekly report. It takes six hours.
Inspect the attached workflow, then build the smallest useful improvement.
```

```text
Use $five-step-algorithm to investigate why this import fails.
Reproduce the problem, make a focused fix, and verify the result.
```

Give the outcome, constraints, and whatever evidence you have. A complete process map or numerical baseline is not required. For coaching or analysis only, say so.

For a chat tool without skill support, paste [prompt.txt](five-step-algorithm/prompt.txt), then describe your task. File access and execution depend on the host's tools and permissions; the prompt does not create those capabilities.

## What changed from the supplied version

- Moves from recommendation-only consulting to execution within the user's authority.
- Handles new tasks and uncertain problems without inventing an existing process.
- Keeps five transformation steps, with verification throughout and at completion.
- Replaces blanket aggressive deletion with evidence, reversible trials, and restoration criteria.
- Makes automation optional and scales the output to the task.
- Distinguishes a prepared artifact from a completed real-world action.

The original archive remains untouched. Its promotional image is not included in this revision because it describes the previous workflow.

## Maintain and validate

`five-step-algorithm/SKILL.md` is the source of truth. The standalone prompt is generated from its body to keep both versions consistent:

```sh
python3 scripts/export_prompt.py
python3 scripts/export_prompt.py --check
```

Behavioral evaluation scenarios and acceptance criteria are in [evaluations/cases.md](evaluations/cases.md); the initial checks are recorded in [validation results](evaluations/results-2026-10-26.md). Evaluate outcomes and artifacts, not exact wording. Structural validation and scenario checks do not establish reliability across every domain.

## Origin

Inspired by the five-step sequence described by Elon Musk in [Everyday Astronaut's Starbase tour, Part 1](https://www.youtube.com/watch?v=t705r8ICkRw). This skill adapts that sequence for general task execution; the authorization boundaries, proportional workflow, and verification guidance are additions. It is not affiliated with or endorsed by Elon Musk, SpaceX, Tesla, or xAI.
