<div align="center">

# 🧬 Awesome Medical Recursive Self-Improvement

### Papers, Datasets, Models, Environments, Evaluators, and Resources for Self-Improving Medical AI

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Medical AI](https://img.shields.io/badge/Medical-AI-red)
![Recursive Self-Improvement](https://img.shields.io/badge/Recursive-Self--Improvement-blue)
![Last Updated](https://img.shields.io/badge/Updated-2026-green)

</div>

---

**Medical Recursive Self-Improvement (Medical-RSI)** studies medical AI systems that use their own interactions, predictions, feedback, failures, clinical environments, generated data, or accumulated experience to improve future behavior.

> **Scope labels used in this list**
>
> - `Meta-RSI`: the system persistently improves the **procedure that produces later improvements** (for example its curriculum, tool/skill creation process, training strategy, or update policy).
> - `Persistent-SI`: a persistent component such as model weights, memory, skills, tools, prompts, or policies improves across episodes, but the improvement mechanism itself is not necessarily improved.
> - `Inference-SI`: iterative refinement happens within one episode/query and is not clearly retained for future episodes.
> - `RSI-Enabler`: a benchmark, evaluator, verifier, dataset, or environment that enables or measures self-improvement but is not itself a self-improving system.
>
> This distinction is intentionally conservative: papers using the terms *self-evolving* or *self-improving* are not automatically labeled recursive self-improvement.

# 📚 Overview

* [Surveys](#surveys)
* [Model Self-Improvement](#model-self-improvement)
* [Data Self-Improvement](#data-self-improvement)
* [Memory & Knowledge Self-Improvement](#memory-knowledge-self-improvement)
* [Tool, Skill & Workflow Self-Improvement](#tool-skill-workflow-self-improvement)
* [Evaluator, Verifier & Feedback Improvement](#evaluator-verifier-feedback-improvement)
* [Environment-Driven Self-Improvement](#environment-driven-self-improvement)
* [Recursive Meta-Improvement](#recursive-meta-improvement)
* [Safety, Reliability & Governance](#safety-reliability-governance)
* [Datasets](#datasets)

---

<a name="surveys"></a>

# 📖 Surveys

Research defining the foundations of medical agents, self-evolving clinical systems, medical reasoning, feedback, and reliability.

| Year | Paper                                                                                                                                                            | Venue        | RSI Relevance         |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | --------------------- |
| 2026 | [The Path to Self-Evolving Clinical Systems: Scaling Medical Agents from Assistance to Autonomy](https://arxiv.org/abs/2607.11175)                               | arXiv        | `Medical-RSI Survey`  |
| 2026 | [Recursive Self-Improvement in AI: From Bounded Self-Refinement to Autonomous Research Loops](https://arxiv.org/abs/2607.07663)                                    | arXiv        | `RSI Foundation / Survey` |
| 2025 | [A Survey of LLM-based Agents in Medicine: How Far Are We from Baymax?](https://aclanthology.org/2025.findings-acl.539/)                                         | ACL Findings | `RSI-Enabler`         |
| 2025 | [Can We Trust AI Doctors? A Survey of Medical Hallucination in Large Language and Large Vision-Language Models](https://aclanthology.org/2025.findings-acl.350/) | ACL Findings | `Safety / Evaluation` |

---

<a name="model-self-improvement"></a>

# 🧠 Model Self-Improvement

Methods that improve medical models through reinforcement learning, continual learning, self-correction, adaptation, curriculum learning, or learned reasoning policies.

### Recursive / Iterative Post-Training

| Year | Paper | Venue | Improvement Mechanism |
| ---- | ----- | ----- | --------------------- |
| 2026 | [Cura 1T: Specialized Model for Agentic Healthcare](https://arxiv.org/abs/2607.15314) [[Code](https://github.com/actava-ai/Cura)] | arXiv | Human-gated recursive training loop: target capability → train → evaluate trajectories → repair data mixture → retain/revert checkpoint `Meta-RSI` |
| 2026 | [BaT: Towards Self-Evolving Medical Research Agent with Stage Rubrics](https://arxiv.org/abs/2608.16211) [[Code](https://github.com/AutoMedBench/Benchmark-as-Teacher)] | arXiv | Stage-rubric diagnosis + bilevel curriculum RL + checkpoint re-evaluation `Meta-RSI` |
| 2025 | [MedReflect: Teaching Medical LLMs to Self-Improve via Reflective Correction](https://arxiv.org/abs/2510.03687) | arXiv | Reflection-generated supervision followed by parameter update `Persistent-SI` |

### Reinforcement Learning & Verifiable Reasoning

| Year | Paper                                                                                                                                                                   | Venue        | Improvement Mechanism                                 |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ----------------------------------------------------- |
| 2026 | [MedReasoner: Reinforcement Learning Drives Reasoning Grounding from Clinical Thought to Pixel-Level Precision](https://ojs.aaai.org/index.php/AAAI/article/view/38141) | AAAI 2026    | RL + grounding rewards `Persistent-SI`                |
| 2025 | [GMAI-VL-R1: Harnessing Reinforcement Learning for Multimodal Medical Reasoning](https://arxiv.org/abs/2504.01886)                                                      | arXiv        | RL + rejection-sampled reasoning data `Persistent-SI` |
| 2025 | [Towards Medical Complex Reasoning with LLMs through Medical Verifiable Problems](https://aclanthology.org/2025.findings-acl.751/)                                      | ACL Findings | Verifier-guided search + RL `Persistent-SI`           |
| 2025 | [Fleming-R1: Toward Expert-Level Medical Reasoning via Reinforcement Learning](https://arxiv.org/abs/2509.15279)                                                        | arXiv        | RLVR + adaptive hard-example mining `Persistent-SI`   |

### Continual & Test-Time Adaptation

| Year | Paper                                                                                                                                                                                                                                                                   | Venue              | Improvement Mechanism                      |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------ |
| 2026 | [Continual Alignment for SAM: Rethinking Foundation Models for Medical Image Segmentation in Continual Learning](https://openaccess.thecvf.com/content/CVPR2026F/html/Wang_Continual_Alignment_for_SAM__Rethinking_Foundation_Models_for_Medical_CVPRF_2026_paper.html) | CVPR 2026 Findings | Continual adaptation `Persistent-SI`       |
| 2026 | [Shifting Adaptation from Weight Space to Memory Space: A Memory-Augmented Agent for Medical Image Segmentation](https://arxiv.org/abs/2603.05873) | arXiv | Static/few-shot/test-time memory adaptation around a fixed backbone `Persistent-SI` |
| 2025 | [Test-time Adaptation for Foundation Medical Segmentation Model Without Parametric Updates](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Test-time_Adaptation_for_Foundation_Medical_Segmentation_Model_Without_Parametric_Updates_ICCV_2025_paper.html)    | ICCV 2025          | Test-time latent adaptation `Inference-SI` |
| 2025 | [Progressive Test Time Energy Adaptation for Medical Image Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Progressive_Test_Time_Energy_Adaptation_for_Medical_Image_Segmentation_ICCV_2025_paper.html)                                         | ICCV 2025          | Progressive adaptation `Persistent-SI`     |

---

<a name="data-self-improvement"></a>

# 🗃️ Data Self-Improvement

Systems that automatically generate, critique, filter, repair, diversify, or prioritize medical training examples.

### Self-Generated & Synthetic Medical Data

| Year | Paper                                                                                                                                                                               | Venue      | Data Improvement                                             |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- | ------------------------------------------------------------ |
| 2025 | [ReasonMed: A 370K Multi-Agent Generated Dataset for Advancing Medical Reasoning](https://aclanthology.org/2025.emnlp-main.1344/)                                                   | EMNLP 2025 | Generation → verification → error refinement `Persistent-SI` |
| 2025 | [GMAI-VL-R1](https://arxiv.org/abs/2504.01886)                                                                                                                                      | arXiv      | Rejection-sampled reasoning synthesis `Persistent-SI`        |
| 2025 | [A Modular Approach for Clinical SLMs Driven by Synthetic Data](https://aclanthology.org/2025.acl-long.950/)                                                                        | ACL 2025   | MediFlow synthetic clinical instructions `RSI-Enabler`       |
| 2025 | [MCQG-SRefine: Multiple Choice Question Generation and Evaluation with Iterative Self-Critique, Correction, and Comparison Feedback](https://aclanthology.org/2025.naacl-long.538/) | NAACL 2025 | Iterative data critique/correction `Inference-SI`            |

### Automated Annotation, Filtering & Hard Cases

| Year | Paper                                                                                                                                                                                                                                        | Venue     | Data Improvement                                     |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ---------------------------------------------------- |
| 2025 | [UKBOB: One Billion MRI Labeled Masks for Generalizable 3D Medical Image Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Bourigault_UKBOB_One_Billion_MRI_Labeled_Masks_for_Generalizable_3D_Medical_ICCV_2025_paper.html) | ICCV 2025 | Automated labeling + quality filtering `RSI-Enabler` |
| 2025 | [Fleming-R1](https://arxiv.org/abs/2509.15279)                                                                                                                                                                                               | arXiv     | Adaptive hard-example mining `Persistent-SI`         |

---

<a name="memory-knowledge-self-improvement"></a>

# 🧾 Memory & Knowledge Self-Improvement

Systems that accumulate reusable clinical experiences, successful strategies, failure histories, or medical knowledge across tasks.

| Year | Paper                                                                                                                                                                  | Venue                | Memory Mechanism                                                      |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | --------------------------------------------------------------------- |
| 2026 | [EMR: Self-Evolving Medical Multi-Agent System via Experience Mining and Reuse](https://arxiv.org/abs/2609.15161) | arXiv | Hierarchical library of clinical principles, diagnostic patterns, and representative cases mined from successes/failures `Persistent-SI` |
| 2026 | [Adaptive Memory and Reflection Multi-Agent System for Medical Question Answering](https://arxiv.org/abs/2608.19029) [[Code](https://github.com/mm-air/AMR-Agent)] | arXiv | Agent-specific persistent memory + reflection feedback + retrieval `Persistent-SI` |
| 2026 | [A Self-Evolving Agent for Longitudinal Personal Health Management](https://arxiv.org/abs/2607.13940) [[Code](https://github.com/HC-Guo/HealthClaw)] | arXiv | Governed longitudinal profile, procedure, and episodic memory updated after each episode `Persistent-SI` |
| 2026 | [Experience Makes Skillful: Enabling Generalizable Medical Agent Reasoning via Self-Evolving Skill Memory](https://arxiv.org/abs/2606.09365) | arXiv | Utility-aware skill memory with Read–Write–Assess–Govern evolution `Persistent-SI` |
| 2026 | [Evo-MedAgent: Beyond One-Shot Diagnosis with Agents That Remember, Reflect, and Improve](https://arxiv.org/abs/2604.14475) | arXiv | Retrospective episodes + evolving procedural heuristics + tool-reliability memory `Persistent-SI` |
| 2026 | [MDTeamGPT: Mitigating Context Collapse and Enabling Self-Evolution in Medical Multi-Agent Reasoning](https://aclanthology.org/2026.findings-acl.1427/) | ACL Findings 2026 | Structured trajectory distillation and error reflection for reusable multi-agent experience `Persistent-SI` |
| 2026 | [SAGEAgent: A Self-evolving Agent for Cost-Aware Modality Acquisition in Multimodal Survival Prediction](https://papers.miccai.org/miccai-2026/0915-Paper0802.html) [[Code](https://github.com/Chongyu1117/SAGEAgent)] | MICCAI 2026 | Episodic + semantic memory that accumulates reusable acquisition strategies `Persistent-SI` |
| 2026 | [HealthFlow: Automating Electronic Health Record Analysis via a Strategically Self-Evolving Multi-Agent Framework](https://www.nature.com/articles/s41746-026-03097-0) | npj Digital Medicine | Persistent strategic knowledge from successes/failures `Meta-RSI`     |
| 2025 | [ReflecTool: Towards Reflection-Aware Tool-Augmented Clinical Agents](https://aclanthology.org/2025.acl-long.663/)                                                     | ACL 2025             | Long-term successful-process + tool-experience memory `Persistent-SI` |

---

<a name="tool-skill-workflow-self-improvement"></a>

# 🛠️ Tool, Skill & Workflow Self-Improvement

Medical agents that improve tool use, clinical skills, planning strategies, workflow execution, or reusable procedural knowledge.

| Year | Paper                                                                                                                                            | Venue                | Improvement Mechanism                                           |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------- | --------------------------------------------------------------- |
| 2026 | [Evolving Medical Imaging Agents via Experience-driven Self-skill Discovery](https://arxiv.org/abs/2603.05860) | arXiv | Discovers successful multi-step tool chains, compiles them into reusable composite skills, and reinforces invocation `Meta-RSI / Persistent-SI` |
| 2026 | [Experience Makes Skillful (SkeMex)](https://arxiv.org/abs/2606.09365) | arXiv | Distills trajectories into governed reusable procedural skills `Persistent-SI` |
| 2026 | [Evo-RAD: Navigating Rare Retinal Disease Diagnosis via Self-Evolving Agentic Retrieval](https://papers.miccai.org/miccai-2026/0360-Paper1081.html) [[Code](https://github.com/SDH-Lab/Evo-RAD)] | MICCAI 2026 | Iteratively evolves retrieval/reference-set decisions for rare retinal diagnosis `Inference-SI / Policy Adaptation` |
| 2026 | [HealthFlow](https://www.nature.com/articles/s41746-026-03097-0)                                                                                 | npj Digital Medicine | Self-evolving strategic planning `Meta-RSI`                     |
| 2025 | [STELLA: Self-Evolving LLM Agent for Biomedical Research](https://arxiv.org/abs/2507.02004) [[Code](https://github.com/zaixizhang/STELLA)] | arXiv / bioRxiv | Evolving reasoning-template library + autonomous discovery/integration of new bioinformatics tools `Meta-RSI` |
| 2025 | [ReflecTool](https://aclanthology.org/2025.acl-long.663/)                                                                                        | ACL 2025             | Experience-guided tool selection + verification `Persistent-SI` |
| 2025 | [DrAgent: Empowering Large Language Models as Medical Agents for Multi-hop Medical Reasoning](https://aclanthology.org/2025.findings-emnlp.848/) | EMNLP Findings       | Clinical tools + recursive curriculum learning `Persistent-SI`  |
| 2025 | [MedAgentGym: Training LLM Agents for Code-Based Medical Reasoning at Scale](https://arxiv.org/abs/2506.04405)                                   | arXiv                | Tool/environment-based SFT + RL `Persistent-SI`                 |

---

<a name="evaluator-verifier-feedback-improvement"></a>

# ✅ Evaluator, Verifier & Feedback Improvement

Evaluators and feedback systems are critical because recursive improvement is only useful when the system can reliably distinguish **better from worse**.

### Medical Verifiers

| Year | Paper                                                                                                                                              | Venue        | Mechanism                                                |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | -------------------------------------------------------- |
| 2025 | [Towards Medical Complex Reasoning with LLMs through Medical Verifiable Problems](https://aclanthology.org/2025.findings-acl.751/)                 | ACL Findings | Medical verifier + verifier-guided RL `RSI-Enabler`      |
| 2025 | [ReflecTool](https://aclanthology.org/2025.acl-long.663/)                                                                                          | ACL 2025     | Tool-use verifier + iterative refinement `Persistent-SI` |
| 2025 | [Localizing Before Answering: A Benchmark for Grounded Medical Visual Question Answering](https://www.ijcai.org/proceedings/2025/853)              | IJCAI 2025   | Grounding/localization feedback `RSI-Enabler`            |
| 2026 | [AutoMedBench: Towards Medical AutoResearch with Agentic AI Models](https://arxiv.org/abs/2606.01961) [[Code](https://github.com/AutoMedBench/AutoMedBench)] | arXiv | Stage-level workflow evaluation (Plan → Setup → Validate → Inference → Submit) for autonomous medical-AI research `RSI-Enabler` |
| 2026 | [TheraAgent: Self-Improving Therapeutic Agent for Precise and Comprehensive Treatment Planning](https://aclanthology.org/2026.findings-acl.1490/) | ACL Findings 2026 | Treatment-specific judge integrated into iterative generate → judge → refine `Inference-SI / Verifier` |
| 2026 | [Trust but Verify: Mitigating Medical Hallucinations via Post-Hoc Adversarial Auditing and Multi-Agent Feedback Loops](https://arxiv.org/abs/2606.14149) | arXiv | Adversarial auditing + multi-agent feedback for medical hallucination mitigation `Inference-SI / Safety` |
| 2025 | [MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models](https://aclanthology.org/2025.emnlp-main.143/) | EMNLP 2025   | Hallucination evaluator `RSI-Enabler`                    |

### Generator–Evaluator–Reflector Loops

| Year | Paper                                                                                                                                | Venue        | Mechanism                                                      |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------ | -------------------------------------------------------------- |
| 2026 | [Route, Retrieve, Reflect, Repair: Self-Improving Agentic Framework for Visual Detection and Linguistic Reasoning in Medical Imaging](https://arxiv.org/abs/2601.08192) [[Code](https://github.com/faiyazabdullah/MultimodalMedAgent)] | arXiv | Router → retriever → reflector → repairer loop with exemplar curation for later cases `Persistent-SI` |
| 2026 | [TheraAgent](https://aclanthology.org/2026.findings-acl.1490/) | ACL Findings 2026 | Generate → judge → refine treatment-planning loop `Inference-SI` |
| 2026 | [SEMA-RAG: A Self-Evolving Multi-Agent Retrieval-Augmented Generation Framework for Medical Reasoning](https://aclanthology.org/2026.findings-acl.917/) | ACL Findings 2026 | Interpreter → explorer → arbiter with sufficiency-driven multi-round evidence acquisition `Inference-SI` |
| 2025 | [FRAME: Feedback-Refined Agent Methodology for Enhancing Medical Research Insights](https://aclanthology.org/2025.findings-acl.400/) | ACL Findings | Generator → evaluator → reflector feedback loop `Inference-SI` |
| 2025 | [MCQG-SRefine](https://aclanthology.org/2025.naacl-long.538/)                                                                        | NAACL 2025   | Self-critique → correction → evaluation `Inference-SI`         |

---

<a name="environment-driven-self-improvement"></a>

# 🌍 Environment-Driven Self-Improvement

Systems that learn through interaction with executable clinical, biomedical, EHR, FHIR, simulation, or research environments.

| Year | Paper / Environment                                                                                                         | Venue                | Role                                                                |
| ---- | --------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------- |
| 2026 | [ClinicalReTrial: A Self-Evolving AI Agent for Clinical Trial Protocol Optimization](https://arxiv.org/abs/2601.00290) | arXiv | Outcome-prediction simulator supplies dense reward for closed-loop redesign + hierarchical reusable memory `Persistent-SI` |
| 2026 | [EvoClinician: A Self-Evolving Agent for Multi-Turn Medical Diagnosis via Test-Time Evolutionary Learning](https://arxiv.org/abs/2601.22964) [[Code](https://github.com/yf-he/EvoClinician)] | arXiv | Med-Inquire environment + Diagnose → Grade → Evolve loop that updates strategy prompt/memory `Persistent-SI` |
| 2026 | [AutoMedBench](https://arxiv.org/abs/2606.01961) [[Code](https://github.com/AutoMedBench/AutoMedBench)] | arXiv | Long-horizon sandboxed medical-AI research environment with stage-wise feedback `RSI-Enabler` |
| 2026 | [HealthFlow + EHRFlowBench](https://www.nature.com/articles/s41746-026-03097-0)                                             | npj Digital Medicine | Environment feedback → strategic evolution `Meta-RSI`               |
| 2025 | [MedAgentSim: Self-Evolving Multi-Agent Simulations for Realistic Clinical Interactions](https://papers.miccai.org/miccai-2025/0537-Paper2575.html) | MICCAI 2025 | Doctor/patient/measurement simulation with iterative diagnostic-strategy improvement `Persistent-SI / RSI-Enabler` |
| 2026 | [AgentClinic: A Multimodal Benchmark for Tool-Using Clinical AI Agents](https://www.nature.com/articles/s41746-026-02674-7) | npj Digital Medicine | Sequential multimodal clinical environment `RSI-Enabler`            |
| 2025 | [MedAgentGym](https://arxiv.org/abs/2506.04405)                                                                             | arXiv                | Executable environment + scalable trajectories + RL `Persistent-SI` |
| 2025 | [MedAgentBench: A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents](https://arxiv.org/abs/2501.14654)      | arXiv                | FHIR-compliant EHR environment `RSI-Enabler`                        |

---

<a name="recursive-meta-improvement"></a>

# 🔁 Recursive Meta-Improvement

The highest level of Medical-RSI. Instead of only improving answers or model weights, the system improves **how it learns, plans, evaluates, selects tools, constructs curricula, or modifies its own improvement strategy**.

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
```

### Closest Current Medical Work

> The strongest entries here are those where the **update loop itself is repeatedly reused** to produce later model/agent improvements. Other self-evolving systems are listed as `Partial Meta-RSI` when they modify reusable skills, tools, code, or strategies but do not yet demonstrate open-ended improvement of the improvement algorithm itself.

| Year | Paper                                                                                                                                                                  | Venue                | Meta-Improvement Role                                                                              |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | -------------------------------------------------------------------------------------------------- |
| 2026 | [Cura 1T: Specialized Model for Agentic Healthcare](https://arxiv.org/abs/2607.15314) [[Code](https://github.com/actava-ai/Cura)] | arXiv | Human-gated RSI harness repeatedly plans a capability target, trains, evaluates trajectories, repairs the data mixture, and keeps/reverts checkpoints `Meta-RSI` |
| 2026 | [Toward Vibe Medicine: A Self-Evolving Multi-Agent Framework for Clinical Decision Support](https://doi.org/10.1016/j.metrad.2026.100223) | Meta-Radiology | Clinical evolution manager supports memory-, model-, and code-level updates from longitudinal interaction history `Partial Meta-RSI` |
| 2026 | [Evolving Medical Imaging Agents via Experience-driven Self-skill Discovery (MACRO)](https://arxiv.org/abs/2603.05860) | arXiv | Converts verified successful tool trajectories into new composite tools and reinforces their reuse `Partial Meta-RSI` |
| 2026 | [ClinicalReTrial](https://arxiv.org/abs/2601.00290) | arXiv | Reward-driven redesign loop learns reusable trial-modification patterns from simulated outcomes `Persistent-SI / Partial Meta-RSI` |
| 2026 | [HealthFlow: Automating Electronic Health Record Analysis via a Strategically Self-Evolving Multi-Agent Framework](https://www.nature.com/articles/s41746-026-03097-0) | npj Digital Medicine | Distills successes and failures into persistent strategic knowledge for future planning `Meta-RSI` |
| 2025 | [STELLA: Self-Evolving LLM Agent for Biomedical Research](https://arxiv.org/abs/2507.02004) [[Code](https://github.com/zaixizhang/STELLA)] | arXiv / bioRxiv | Evolves reasoning templates and autonomously expands its tool repertoire through a tool-creation agent `Partial Meta-RSI` |
| 2025 | [ReflecTool](https://aclanthology.org/2025.acl-long.663/)                                                                                                              | ACL 2025             | Reuses accumulated experience to improve later tool selection and verification `Persistent-SI`     |
| 2025 | [DrAgent](https://aclanthology.org/2025.findings-emnlp.848/)                                                                                                           | EMNLP Findings       | Recursive curriculum optimization for increasingly difficult clinical reasoning `Persistent-SI`    |
| 2025 | [FRAME](https://aclanthology.org/2025.findings-acl.400/)                                                                                                               | ACL Findings         | Generator–evaluator–reflector iterative refinement `Inference-SI`                                  |
| 2026 | [BaT: Towards Self-Evolving Medical Research Agent with Stage Rubrics](https://arxiv.org/abs/2608.16211) [[Code](https://github.com/AutoMedBench/Benchmark-as-Teacher)] | arXiv | **Benchmark-as-Teacher (BaT)** closes the evaluation → curriculum → training → re-evaluation loop: stage-level rubrics identify weaknesses, **BiCuRL** selects the next training curriculum from a Stage Bank, rubric-verified rollouts update the policy with GRPO, and the improved checkpoint is recursively returned to evaluation `Meta-RSI` |

---

<a name="safety-reliability-governance"></a>

# 🛡️ Safety, Reliability & Governance

Self-improving medical AI must ensure that improvement does not introduce new clinical risks, amplify hallucinations, propagate erroneous experience, or degrade previously acquired capabilities. Medical-RSI therefore requires **continuous safety evaluation, grounding verification, failure detection, uncertainty-aware behavior, no-regression mechanisms, and governed model updates**.

### Hallucination, Grounding & Clinical Error Detection

| Year | Paper / Resource                                                                                                                                                 | Venue             | Safety / Reliability Role                                                                             |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------- |
| 2025 | [MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models](https://aclanthology.org/2025.emnlp-main.143/)               | EMNLP 2025        | Controlled medical hallucination detection with 10K QA pairs `RSI-Enabler`                            |
| 2025 | [Localizing Before Answering: A Benchmark for Grounded Medical Visual Question Answering](https://www.ijcai.org/proceedings/2025/853)                            | IJCAI 2025        | HEAL-MedVQA evaluates visual grounding and hallucination robustness using 67K VQA pairs `RSI-Enabler` |
| 2026 | [Route, Retrieve, Reflect, Repair (R⁴)](https://arxiv.org/abs/2601.08192) | arXiv | Reflection targets negation, laterality, unsupported claims, contradictions, missing findings, and localization errors before repair `Persistent-SI / Safety` |
| 2026 | [TheraAgent](https://aclanthology.org/2026.findings-acl.1490/) | ACL Findings 2026 | Treatment-specific judge drives iterative refinement toward more complete and safer treatment plans `Inference-SI / Safety` |
| 2026 | [Trust but Verify](https://arxiv.org/abs/2606.14149) | arXiv | Post-hoc adversarial auditing and multi-agent feedback for obsolete/unsafe medical recommendations `Inference-SI / Safety` |
| 2025 | [MEDEC: A Benchmark for Medical Error Detection and Correction in Clinical Notes](https://aclanthology.org/2025.findings-acl.1159/)                              | ACL Findings 2025 | Medical error detection and correction across major clinical error categories `RSI-Enabler`           |
| 2025 | [Can We Trust AI Doctors? A Survey of Medical Hallucination in Large Language and Large Vision-Language Models](https://aclanthology.org/2025.findings-acl.350/) | ACL Findings 2025 | Medical hallucination taxonomy, evaluation, detection, and mitigation `Safety Survey`                 |

### Robustness, Forgetting & Safe Updating

| Year | Paper                                                                                                                                                                                                                                                                   | Venue                | Safety / Reliability Role                                                                    |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | -------------------------------------------------------------------------------------------- |
| 2026 | [Continual Alignment for SAM: Rethinking Foundation Models for Medical Image Segmentation in Continual Learning](https://openaccess.thecvf.com/content/CVPR2026F/html/Wang_Continual_Alignment_for_SAM__Rethinking_Foundation_Models_for_Medical_CVPRF_2026_paper.html) | CVPR 2026 Findings   | Continual adaptation with protection against catastrophic forgetting `Persistent-SI`         |
| 2026 | [Benchmarking Large Language Model-Based Agent Systems for Clinical Decision Tasks](https://www.nature.com/articles/s41746-026-02443-6)                                                                                                                                 | npj Digital Medicine | Evaluates clinical-agent reliability, tool use, hallucinations, and safeguards `RSI-Enabler` |

### Governance & Lifecycle Control

| Year | Guideline / Paper                                                                                                                                                    | Venue   | Governance Role                                                                                                          |
| ---- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------ |
| 2025 | [FUTURE-AI: International Consensus Guideline for Trustworthy and Deployable Artificial Intelligence in Healthcare](https://www.bmj.com/content/388/bmj-2024-081554) | The BMJ | Lifecycle governance across fairness, universality, traceability, usability, robustness, and explainability `Governance` |

---

<a name="datasets"></a>

# 🗂️ Datasets

Medical-RSI requires more than static medical QA datasets. Particularly relevant resources provide **reasoning trajectories, generated-and-refined examples, verifiable feedback, failure annotations, executable environments, persistent interactions, or longitudinal evaluation**.

### Training & Self-Improvement Datasets

| Year    | Dataset                                                             | Scale                                                                          | Medical-RSI Role                                                                                           | Associated Work                                                       |
| ------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| 2025    | [ReasonMed](https://aclanthology.org/2025.emnlp-main.1344/)         | 370K curated reasoning examples distilled from 1.75M generated reasoning paths | Multi-agent generation → verification → error refinement `Persistent-SI`                                   | [ReasonMed](https://aclanthology.org/2025.emnlp-main.1344/)           |
| 2025/26 | [MedAgentGym](https://arxiv.org/abs/2506.04405)                     | 72,413 executable tasks across 129 categories                                  | Interactive feedback, trajectory generation, SFT, and continued RL `Persistent-SI`                         | [MedAgentGym](https://arxiv.org/abs/2506.04405)                       |
| 2026    | [U-MRG-14K](https://ojs.aaai.org/index.php/AAAI/article/view/38141) | 14K multimodal reasoning-grounding samples                                     | Clinical reasoning traces + pixel-level masks + verifiable grounding rewards `Persistent-SI / RSI-Enabler` | [MedReasoner](https://ojs.aaai.org/index.php/AAAI/article/view/38141) |

### Safety, Hallucination & Verification Datasets

| Year | Dataset                                                   | Scale                   | Medical-RSI Role                                                                             | Associated Work                                                           |
| ---- | --------------------------------------------------------- | ----------------------- | -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| 2025 | [MedHallu](https://aclanthology.org/2025.emnlp-main.143/) | 10,000 medical QA pairs | Controlled hallucination detection and evaluator development `RSI-Enabler`                   | [MedHallu](https://aclanthology.org/2025.emnlp-main.143/)                 |
| 2025 | [HEAL-MedVQA](https://www.ijcai.org/proceedings/2025/853) | 67K VQA pairs           | Physician-annotated pathological-region grounding and hallucination evaluation `RSI-Enabler` | [Localizing Before Answering](https://www.ijcai.org/proceedings/2025/853) |
| 2025 | [MEDEC](https://aclanthology.org/2025.findings-acl.1159/) | 3,848 clinical texts    | Medical error detection and correction across five clinical error categories `RSI-Enabler`   | [MEDEC](https://aclanthology.org/2025.findings-acl.1159/)                 |

### Interactive Environments & Agent Benchmarks

| Year    | Dataset / Environment                                              | Scale / Coverage                                                                        | Medical-RSI Role                                                                                             |
| ------- | ------------------------------------------------------------------ | --------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| 2026    | [AutoMedBench](https://arxiv.org/abs/2606.01961) [[Code](https://github.com/AutoMedBench/AutoMedBench)] | Long-horizon autonomous medical-AI research tasks across multiple imaging/reasoning tracks | Stage-wise Plan/Setup/Validate/Inference/Submit scoring; directly supports benchmark-driven self-improvement `RSI-Enabler` |
| 2026    | [Med-Inquire / EvoClinician](https://arxiv.org/abs/2601.22964) | Multi-turn diagnostic cases with hidden patient information exposed through patient/examination agents | Interactive diagnosis environment with process grading for test-time strategy evolution `Persistent-SI / RSI-Enabler` |
| 2026    | [EHRFlowBench](https://www.nature.com/articles/s41746-026-03097-0) | 100 expert-curated EHR analysis tasks across 10 categories                              | Planning, execution, verification, recovery, and governed reuse of prior experience `Meta-RSI / RSI-Enabler` |
| 2026    | [AgentClinic](https://www.nature.com/articles/s41746-026-02674-7)  | Multimodal simulated clinical interactions across 9 specialties and 7 languages         | Sequential clinical reasoning, multimodal evidence collection, and tool-use evaluation `RSI-Enabler`         |
| 2025    | [MedAgentBench](https://doi.org/10.1056/AIdbp2500144)              | 300 physician-written EHR tasks; 100 patient profiles with more than 700K data elements | FHIR-based interactive EHR environment for medical-agent evaluation `RSI-Enabler`                            |
| 2025/26 | [MedAgentGym](https://arxiv.org/abs/2506.04405)                    | 72,413 executable medical and biomedical tasks                                          | Environment feedback + verifiable outcomes + scalable training trajectories `Persistent-SI`                  |
| 2025    | [MedAgentSim](https://papers.miccai.org/miccai-2025/0537-Paper2575.html) | Interactive doctor–patient–measurement simulation | Dynamic clinical interactions plus experience-based iterative strategy refinement `Persistent-SI / RSI-Enabler` |

---
