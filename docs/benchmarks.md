# Datasets, benchmarks, and environments

[Home](../README.md) · [Paper catalog](papers.md) · [Classification guide](taxonomy.md)

Choose a resource by the behavior you want to measure. The linked papers and project pages describe access, splits, and usage terms.

| Study goal | Suggested starting points |
| --- | --- |
| Train or verify multimodal reasoning with spatial evidence | [U-MRG-14K](#training-and-grounding) |
| Train a coding agent with executable biomedical feedback | [MedAgentGym](#interactive-environments) |
| Measure EHR tool use and recovery | [MedAgentBench and EHRFlowBench](#interactive-environments) |
| Localize errors across a medical research workflow | [AutoMedBench](#interactive-environments) |
| Measure hallucination, grounding, or clinical-note errors | [MedHallu, HEAL-MedVQA, and MEDEC](#reliability-and-safety) |

## Training and grounding

| Resource | Coverage | How to use it |
| --- | --- | --- |
| [ReasonMed](https://aclanthology.org/2025.emnlp-main.1344/) | 370,000 reasoning examples curated from 1.75 million candidate paths | Train or compare medical reasoning models on curated traces. See the [paper entry](papers.md#reasonmed) for how the data was generated. |
| [U-MRG-14K](https://ojs.aaai.org/index.php/AAAI/article/view/38141) | Approximately 14,000 reasoning and grounding samples | Test whether a model can translate a medical question into spatial evidence. See the [MedReasoner entry](papers.md#medreasoner). |

## Reliability and safety

| Resource | Coverage | How to use it |
| --- | --- | --- |
| [MedHallu](https://aclanthology.org/2025.emnlp-main.143/) | 10,000 medical question-answer pairs | Test whether an evaluator detects controlled hallucinations in answers. |
| [EndoAgentBench](https://arxiv.org/abs/2508.07292) | 6,132 question-answer pairs from 11 endoscopic datasets | Evaluate perception and diagnostic reasoning across an endoscopic workflow. |
| [HEAL-MedVQA](https://www.ijcai.org/proceedings/2025/853) | Approximately 67,000 medical visual question-answer pairs | Evaluate answer correctness alongside localization of visual evidence. |
| [MEDEC](https://aclanthology.org/2025.findings-acl.1159/) | 3,848 clinical texts across five error categories | Measure detection and correction of errors in clinical notes. |

## Interactive environments

| Resource | Coverage | How to use it |
| --- | --- | --- |
| [AgentClinic](https://www.nature.com/articles/s41746-026-02674-7) | Simulated interactions across nine specialties and seven languages | Evaluate sequential diagnosis, patient interaction, and multimodal tool use. |
| [AutoMedBench](https://arxiv.org/abs/2606.01961) | Medical research tasks with rubrics for five workflow stages | Measure how errors in planning, setup, validation, inference, and submission affect outcomes. [Code](https://github.com/AutoMedBench/AutoMedBench) |
| [EHRFlowBench](https://www.nature.com/articles/s41746-026-03097-0) | Published evaluation subset of 100 EHR analysis tasks across 10 categories | Study execution, repair, and reuse of prior experience. See the [HealthFlow entry](papers.md#healthflow) for its memory update mechanism. |
| [HealthAgentBench](https://arxiv.org/abs/2606.31179) | 54 executable tasks across seven healthcare environments | Measure task completion with task-specific verifiers. [Code](https://github.com/microsoft/HealthAgentBench) |
| [MedAgentBench](https://doi.org/10.1056/AIdbp2500144) | 300 physician-written tasks across 100 virtual patient profiles | Evaluate actions against a FHIR interface. [Code](https://github.com/stanfordmlgroup/MedAgentBench) |
| [MedAgentGym](https://openreview.net/pdf?id=jHDZEUgS4r) | Executable biomedical data-science tasks with verifiable outputs | Train with program execution feedback and measure transfer to held-out tasks. [Code](https://github.com/wshi83/MedAgentGym) · [Data](https://huggingface.co/MedAgentGym) |

## Record the evaluation setup

When comparing systems, record the resource version, split, and allowed tools. If the agent learns during evaluation, specify the order of episodes, what feedback it receives, and which state persists. Use separate tasks to select updates and measure their benefit, and report both gains and regressions under matched budgets.
