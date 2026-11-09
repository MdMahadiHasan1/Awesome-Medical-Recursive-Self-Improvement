# Classifying improvement mechanisms

[Home](../README.md) · [Paper catalog](papers.md) · [Datasets and benchmarks](benchmarks.md)

Read an improvement claim at three levels. First identify the component that changes, then ask how long the change lasts, then check the experiment that measures its effect.

| Label | Include when | Evidence to inspect |
| --- | --- | --- |
| **Inference** | Feedback revises an answer, plan, generated sample, or temporary state for the current case or task. | Compare first-pass and revised results under a comparable inference budget. |
| **Persistent** | A model, memory, tool library, or workflow state changes and carries into future cases or tasks. | Compare frozen and updated systems on later cases. State what was carried over and what was reset. |
| **Meta-update** | The agent changes a rule or component that governs future improvement, such as a rule for generating updates, evaluating proposals, or selecting what to retain. | Compare the old and revised procedures from the same starting state. Check whether the revised procedure produces better updates on fresh episodes with matched feedback and compute. |
| **Resource** | The work provides context, training data, a benchmark, a verifier, or a technique that can support a study of improvement. | Identify which part of the improvement pipeline the resource can train, test, or constrain. |

An agent that stores lessons across cases is **Persistent**. If it also revises how it extracts or validates lessons, that part may qualify as a **Meta-update**. A paper can evaluate a meta-update mechanism without isolating its effect from gains accumulated in the agent. Catalog notes distinguish these where the evidence permits. When the update boundary is unclear, use the narrower label and state what the paper demonstrates.

## Compare systems

1. **Update target.** Record whether the system changes its answer, weights, training data, memory, tools, planner, or evaluator.
2. **Feedback.** Identify the source, such as existing labels, records, simulator outcomes, rubric checks, model judgments, or expert review. Record any annotations or expert effort used.
3. **Persistence.** Identify what carries across cases, tasks, or rounds, and whether the update rule itself can change.
4. **Evaluation.** Separate gains on the current task from gains on later held-out tasks. If the updater uses a benchmark for feedback, use a separate split or task family for the comparison.
5. **Controls.** Compare against a frozen agent and, where applicable, a fixed updater with the same starting state and budgets. Inspect task-level failures and regressions alongside aggregate performance.

Use the [dataset guide](benchmarks.md) to match the evaluation resource to the behavior you want to measure.
