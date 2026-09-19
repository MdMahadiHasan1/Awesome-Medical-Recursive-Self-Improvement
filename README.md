<div align="center">

# 🧬 Awesome Medical Recursive Self-Improvement

### Papers, Datasets, Models, Environments, Evaluators, and Resources for Self-Improving Medical AI

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Medical AI](https://img.shields.io/badge/Medical-AI-red)
![Recursive Self-Improvement](https://img.shields.io/badge/Recursive-Self--Improvement-blue)
![Last Updated](https://img.shields.io/badge/Updated-2026-green)

</div>

---

**Medical Recursive Self-Improvement (Medical-RSI)** studies medical AI systems that use
their own interactions, predictions, feedback, failures, clinical environments, generated
data, or accumulated experience to improve future behavior.

# 📚 Overview

- [Surveys](#surveys)
- [Model Self-Improvement](#model-self-improvement)
- [Data Self-Improvement](#data-self-improvement)
- [Memory & Knowledge Self-Improvement](#memory-knowledge-self-improvement)
- [Tool, Skill & Workflow Self-Improvement](#tool-skill-workflow-self-improvement)
- [Evaluator, Verifier & Feedback Improvement](#evaluator-verifier-feedback-improvement)
- [Environment-Driven Self-Improvement](#environment-driven-self-improvement)
- [Recursive Meta-Improvement](#recursive-meta-improvement)
- [Safety, Reliability & Governance](#safety-reliability-governance)
- [Datasets](#datasets)
---
<a name="surveys"></a>
# 📖 Surveys

Research defining the foundations of medical agents, self-evolving clinical systems,
medical reasoning, feedback, and reliability.

| Year | Paper | Venue | RSI Relevance |
|---|---|---|---|
| 2026 | [The Path to Self-Evolving Clinical Systems: Scaling Medical Agents from Assistance to Autonomy](https://arxiv.org/abs/2607.11175) | arXiv | `Medical-RSI Survey` |
| 2025 | [A Survey of LLM-based Agents in Medicine: How Far Are We from Baymax?](https://aclanthology.org/2025.findings-acl.539/) | ACL Findings | `RSI-Enabler` |
| 2025 | [Can We Trust AI Doctors? A Survey of Medical Hallucination in Large Language and Large Vision-Language Models](https://aclanthology.org/2025.findings-acl.350/) | ACL Findings | `Safety / Evaluation` |

---
<a name="model-self-improvement"></a>
# 🧠 Model Self-Improvement

Methods that improve medical models through reinforcement learning, continual learning,
self-correction, adaptation, curriculum learning, or learned reasoning policies.

### Reinforcement Learning & Verifiable Reasoning

| Year | Paper | Venue | Improvement Mechanism |
|---|---|---|---|
| 2026 | [MedReasoner: Reinforcement Learning Drives Reasoning Grounding from Clinical Thought to Pixel-Level Precision](https://ojs.aaai.org/index.php/AAAI/article/view/38141) | AAAI 2026 | RL + grounding rewards `Persistent-SI` |
| 2025 | [GMAI-VL-R1: Harnessing Reinforcement Learning for Multimodal Medical Reasoning](https://arxiv.org/abs/2504.01886) | arXiv | RL + rejection-sampled reasoning data `Persistent-SI` |
| 2025 | [Towards Medical Complex Reasoning with LLMs through Medical Verifiable Problems](https://aclanthology.org/2025.findings-acl.751/) | ACL Findings | Verifier-guided search + RL `Persistent-SI` |
| 2025 | [Fleming-R1: Toward Expert-Level Medical Reasoning via Reinforcement Learning](https://arxiv.org/abs/2509.15279) | arXiv | RLVR + adaptive hard-example mining `Persistent-SI` |

### Continual & Test-Time Adaptation

| Year | Paper | Venue | Improvement Mechanism |
|---|---|---|---|
| 2026 | [Continual Alignment for SAM: Rethinking Foundation Models for Medical Image Segmentation in Continual Learning](https://openaccess.thecvf.com/content/CVPR2026F/html/Wang_Continual_Alignment_for_SAM__Rethinking_Foundation_Models_for_Medical_CVPRF_2026_paper.html) | CVPR 2026 Findings | Continual adaptation `Persistent-SI` |
| 2025 | [Test-time Adaptation for Foundation Medical Segmentation Model Without Parametric Updates](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Test-time_Adaptation_for_Foundation_Medical_Segmentation_Model_Without_Parametric_Updates_ICCV_2025_paper.html) | ICCV 2025 | Test-time latent adaptation `Inference-SI` |
| 2025 | [Progressive Test Time Energy Adaptation for Medical Image Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Progressive_Test_Time_Energy_Adaptation_for_Medical_Image_Segmentation_ICCV_2025_paper.html) | ICCV 2025 | Progressive adaptation `Persistent-SI` |

---
<a name="data-self-improvement"></a>
# 🗃️ Data Self-Improvement

Systems that automatically generate, critique, filter, repair, diversify, or prioritize
medical training examples.

### Self-Generated & Synthetic Medical Data

| Year | Paper | Venue | Data Improvement |
|---|---|---|---|
| 2025 | [ReasonMed: A 370K Multi-Agent Generated Dataset for Advancing Medical Reasoning](https://aclanthology.org/2025.emnlp-main.1344/) | EMNLP 2025 | Generation → verification → error refinement `Persistent-SI` |
| 2025 | [GMAI-VL-R1](https://arxiv.org/abs/2504.01886) | arXiv | Rejection-sampled reasoning synthesis `Persistent-SI` |
| 2025 | [A Modular Approach for Clinical SLMs Driven by Synthetic Data...](https://aclanthology.org/2025.acl-long.950/) | ACL 2025 | MediFlow synthetic clinical instructions `RSI-Enabler` |
| 2025 | [MCQG-SRefine: Multiple Choice Question Generation and Evaluation with Iterative Self-Critique, Correction, and Comparison Feedback](https://aclanthology.org/2025.naacl-long.538/) | NAACL 2025 | Iterative data critique/correction `Inference-SI` |

### Automated Annotation, Filtering & Hard Cases

| Year | Paper | Venue | Data Improvement |
|---|---|---|---|
| 2025 | [UKBOB: One Billion MRI Labeled Masks for Generalizable 3D Medical Image Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Bourigault_UKBOB_One_Billion_MRI_Labeled_Masks_for_Generalizable_3D_Medical_ICCV_2025_paper.html) | ICCV 2025 | Automated labeling + quality filtering `RSI-Enabler` |
| 2025 | [Fleming-R1](https://arxiv.org/abs/2509.15279) | arXiv | Adaptive hard-example mining `Persistent-SI` |

---
<a name="memory-knowledge-self-improvement"></a>
# 🧾 Memory & Knowledge Self-Improvement

Systems that accumulate reusable clinical experiences, successful strategies,
failure histories, or medical knowledge across tasks.

| Year | Paper | Venue | Memory Mechanism |
|---|---|---|---|
| 2026 | [HealthFlow: Automating Electronic Health Record Analysis via a Strategically Self-Evolving Multi-Agent Framework](https://www.nature.com/articles/s41746-026-03097-0) | npj Digital Medicine | Persistent strategic knowledge from successes/failures `Meta-RSI` |
| 2025 | [ReflecTool: Towards Reflection-Aware Tool-Augmented Clinical Agents](https://aclanthology.org/2025.acl-long.663/) | ACL 2025 | Long-term successful-process + tool-experience memory `Persistent-SI` |

---
<a name="tool-skill-workflow-self-improvement"></a>
# 🛠️ Tool, Skill & Workflow Self-Improvement

Medical agents that improve tool use, clinical skills, planning strategies,
workflow execution, or reusable procedural knowledge.

| Year | Paper | Venue | Improvement Mechanism |
|---|---|---|---|
| 2026 | [HealthFlow](https://www.nature.com/articles/s41746-026-03097-0) | npj Digital Medicine | Self-evolving strategic planning `Meta-RSI` |
| 2025 | [ReflecTool](https://aclanthology.org/2025.acl-long.663/) | ACL 2025 | Experience-guided tool selection + verification `Persistent-SI` |
| 2025 | [DrAgent: Empowering Large Language Models as Medical Agents for Multi-hop Medical Reasoning](https://aclanthology.org/2025.findings-emnlp.848/) | EMNLP Findings | Clinical tools + recursive curriculum learning `Persistent-SI` |
| 2025 | [MedAgentGym: Training LLM Agents for Code-Based Medical Reasoning at Scale](https://arxiv.org/abs/2506.04405) | arXiv | Tool/environment-based SFT + RL `Persistent-SI` |

---
<a name="evaluator-verifier-feedback-improvement"></a>
# ✅ Evaluator, Verifier & Feedback Improvement

Evaluators and feedback systems are critical because recursive improvement is only
useful when the system can reliably distinguish **better from worse**.

### Medical Verifiers

| Year | Paper | Venue | Mechanism |
|---|---|---|---|
| 2025 | [Towards Medical Complex Reasoning with LLMs through Medical Verifiable Problems](https://aclanthology.org/2025.findings-acl.751/) | ACL Findings | Medical verifier + verifier-guided RL `RSI-Enabler` |
| 2025 | [ReflecTool](https://aclanthology.org/2025.acl-long.663/) | ACL 2025 | Tool-use verifier + iterative refinement `Persistent-SI` |
| 2025 | [Localizing Before Answering: A Benchmark for Grounded Medical Visual Question Answering](https://www.ijcai.org/proceedings/2025/853) | IJCAI 2025 | Grounding/localization feedback `RSI-Enabler` |
| 2025 | [MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models](https://aclanthology.org/2025.emnlp-main.143/) | EMNLP 2025 | Hallucination evaluator `RSI-Enabler` |

### Generator–Evaluator–Reflector Loops

| Year | Paper | Venue | Mechanism |
|---|---|---|---|
| 2025 | [FRAME: Feedback-Refined Agent Methodology for Enhancing Medical Research Insights](https://aclanthology.org/2025.findings-acl.400/) | ACL Findings | Generator → evaluator → reflector feedback loop `Inference-SI` |
| 2025 | [MCQG-SRefine](https://aclanthology.org/2025.naacl-long.538/) | NAACL 2025 | Self-critique → correction → evaluation `Inference-SI` |

---
<a name="environment-driven-self-improvement"></a>
# 🌍 Environment-Driven Self-Improvement

Systems that learn through interaction with executable clinical, biomedical,
EHR, FHIR, simulation, or research environments.

| Year | Paper / Environment | Venue | Role |
|---|---|---|---|
| 2026 | [HealthFlow + EHRFlowBench](https://www.nature.com/articles/s41746-026-03097-0) | npj Digital Medicine | Environment feedback → strategic evolution `Meta-RSI` |
| 2026 | [AgentClinic: A Multimodal Benchmark for Tool-Using Clinical AI Agents](https://www.nature.com/articles/s41746-026-02674-7) | npj Digital Medicine | Sequential multimodal clinical environment `RSI-Enabler` |
| 2025 | [MedAgentGym](https://arxiv.org/abs/2506.04405) | arXiv | Executable environment + scalable trajectories + RL `Persistent-SI` |
| 2025 | [MedAgentBench: A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents](https://arxiv.org/abs/2501.14654) | arXiv | FHIR-compliant EHR environment `RSI-Enabler` |

---
<a name="recursive-meta-improvement"></a>
# 🔁 Recursive Meta-Improvement

The highest level of Medical-RSI.

Instead of only improving answers or model weights, the system improves
**how it learns, plans, evaluates, selects tools, constructs curricula,
or modifies its own improvement strategy**.

```text
Experience_t
     ↓
Failure / Success Analysis
     ↓
Evaluator / Verifier
     ↓
Improvement Strategy
     ↓
┌────────────────────────────────┐
│ Model / Data / Memory / Tools  │
│ Workflow / Planner / Evaluator │
└────────────────────────────────┘
     ↓
Improved System_(t+1)
     ↓
Meta-Evaluation
     ↓
Improved Improvement Strategy_(t+1)
     ↺

---
