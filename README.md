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
| 2026 | [AI Agents in Clinical Practice: An Evidence Map](https://www.nature.com/articles/s41746-026-02960-4) | npj Digital Medicine | Clinical-agent autonomy, deployment, and self-learning landscape `RSI-Enabler` |
| 2026 | [The Role of Agentic Artificial Intelligence in Healthcare: A Scoping Review](https://www.nature.com/articles/s41746-026-02517-5) | npj Digital Medicine | Agentic healthcare systems, autonomy, adaptation, and clinical deployment `RSI-Enabler` |
| 2026 | [Multimodal Artificial Intelligence Agents in Healthcare: A Scoping Review](https://www.nature.com/articles/s41746-026-03060-z) | npj Digital Medicine | Multimodal agents, tools, memory, orchestration, and clinical environments `RSI-Enabler` |
| 2026 | [The Path to Self-Evolving Clinical Systems: Scaling Medical Agents from Assistance to Autonomy](https://arxiv.org/abs/2607.11175)                               | arXiv        | `Medical-RSI Survey`  |
| 2025 | [A Survey of LLM-based Agents in Medicine: How Far Are We from Baymax?](https://aclanthology.org/2025.findings-acl.539/)                                         | ACL Findings | `RSI-Enabler`         |
| 2025 | [Can We Trust AI Doctors? A Survey of Medical Hallucination in Large Language and Large Vision-Language Models](https://aclanthology.org/2025.findings-acl.350/) | ACL Findings | `Safety / Evaluation` |

---

<a name="model-self-improvement"></a>

# 🧠 Model Self-Improvement

Methods that improve medical models through reinforcement learning, continual learning, self-correction, adaptation, curriculum learning, or learned reasoning policies.

### Reinforcement Learning & Verifiable Reasoning

| Year | Paper                                                                                                                                                                   | Venue        | Improvement Mechanism                                 |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ----------------------------------------------------- |
| 2026 | [EvoClinician: A Self-Evolving Agent for Multi-Turn Medical Diagnosis via Test-Time Evolutionary Learning](https://arxiv.org/abs/2601.22964) [[Code](https://github.com/yf-he/EvoClinician)] | arXiv | Diagnose → Grade → Evolve loop updates diagnostic strategy and memory at test time `Persistent-SI` |
| 2026 | [Traj-Evolve: A Self-Evolving Multi-Agent System for Patient Trajectory Modeling in Lung Cancer Early Detection](https://arxiv.org/abs/2606.02812) | arXiv | Experience Pool + multi-agent reinforcement learning + reward-ranked fine-tuning `Persistent-SI` |
| 2026 | [EvoMDT: A Self-Evolving Multi-Agent System for Structured Clinical Decision-Making in Multi-Cancer](https://www.nature.com/articles/s41746-025-02304-8) [[Code](https://github.com/KesselZ/EvoMDT)] | npj Digital Medicine | Feedback/outcome-driven evolution of prompts, consensus weights, and retrieval scope `Persistent-SI` |
| 2026 | [MDTeamGPT: Mitigating Context Collapse and Enabling Self-Evolution in Medical Multi-Agent Reasoning](https://aclanthology.org/2026.findings-acl.1427/) [[Code](https://github.com/KaiChenNJ/MDTeamGPT)] | ACL Findings 2026 | Error reflection + structured experience accumulation in CorrectKB and ChainKB `Persistent-SI` |
| 2026 | [MedExAgent: Training LLM Agents to Ask, Examine, and Diagnose in Noisy Clinical Environments](https://arxiv.org/abs/2605.07058) | arXiv | SFT + reinforcement learning for adaptive questioning, examination, and cost-aware diagnosis `Persistent-SI` |
| 2026 | [Shifting Adaptation from Weight Space to Memory Space: A Memory-Augmented Agent for Medical Image Segmentation](https://arxiv.org/abs/2603.05873) | arXiv | Dynamic working-memory adaptation with frozen backbone; continual/test-time adaptation `Persistent-SI` |
| 2026 | [MedReasoner: Reinforcement Learning Drives Reasoning Grounding from Clinical Thought to Pixel-Level Precision](https://ojs.aaai.org/index.php/AAAI/article/view/38141) | AAAI 2026    | RL + grounding rewards `Persistent-SI`                |
| 2025 | [GMAI-VL-R1: Harnessing Reinforcement Learning for Multimodal Medical Reasoning](https://arxiv.org/abs/2504.01886)                                                      | arXiv        | RL + rejection-sampled reasoning data `Persistent-SI` |
| 2025 | [Towards Medical Complex Reasoning with LLMs through Medical Verifiable Problems](https://aclanthology.org/2025.findings-acl.751/)                                      | ACL Findings | Verifier-guided search + RL `Persistent-SI`           |
| 2025 | [Fleming-R1: Toward Expert-Level Medical Reasoning via Reinforcement Learning](https://arxiv.org/abs/2509.15279)                                                        | arXiv        | RLVR + adaptive hard-example mining `Persistent-SI`   |

### Continual & Test-Time Adaptation

| Year | Paper                                                                                                                                                                                                                                                                   | Venue              | Improvement Mechanism                      |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------ | ------------------------------------------ |
| 2026 | [Continual Alignment for SAM: Rethinking Foundation Models for Medical Image Segmentation in Continual Learning](https://openaccess.thecvf.com/content/CVPR2026F/html/Wang_Continual_Alignment_for_SAM__Rethinking_Foundation_Models_for_Medical_CVPRF_2026_paper.html) | CVPR 2026 Findings | Continual adaptation `Persistent-SI`       |
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

### Evolving Clinical Memory

| Year | Paper | Venue | Memory / Knowledge Mechanism |
| ---- | ----- | ----- | ---------------------------- |
| 2026 | [Evo-MedAgent: Beyond One-Shot Diagnosis with Agents That Remember, Reflect, and Improve](https://arxiv.org/abs/2604.14475) | arXiv | Retrospective Clinical Episodes + evolving procedural heuristics + tool-reliability memory `Persistent-SI` |
| 2026 | [TheraAgent: Multi-Agent Framework with Self-Evolving Memory and Evidence-Calibrated Reasoning for PET Theranostics](https://arxiv.org/abs/2603.13676) | arXiv | Self-Evolving Agentic Memory learns prognostic patterns from accumulated cases `Persistent-SI` |
| 2026 | [SkinGPT-X: A Self-Evolving Collaborative Multi-Agent System for Transparent and Trustworthy Dermatological Diagnosis](https://arxiv.org/abs/2603.26122) | arXiv | EvoDerma-Mem continually refines diagnostic guidance from accumulated experience `Persistent-SI` |
| 2026 | [ClinicalAgents: Multi-Agent Orchestration for Clinical Decision Making with Dual-Memory](https://arxiv.org/abs/2603.26182) | arXiv | Mutable working memory + experience memory + feedback-driven retrieval `RSI-Enabler` |
| 2025 | [EndoAgent: A Memory-Guided Reflective Agent for Intelligent Endoscopic Vision-to-Decision Reasoning](https://arxiv.org/abs/2508.07292) [[Code](https://github.com/Tyyds-ai/EndoAgent)] | arXiv | Short-term action memory + long-term experiential memory + reflection `Persistent-SI` |

### Evolving Medical Knowledge

| Year | Paper | Venue | Memory / Knowledge Mechanism |
| ---- | ----- | ----- | ---------------------------- |
| 2026 | [MedKGent: A Large Language Model Agent Framework for Constructing Temporally Evolving Medical Knowledge Graph](https://www.nature.com/articles/s41746-026-03058-7) | npj Digital Medicine | Incremental temporal KG construction, confidence reinforcement, and conflict resolution `RSI-Enabler` |
| 2026 | [An Autonomous AI Agent for Knowledge and Data Cooperation in ED Clinical Decision Support](https://www.nature.com/articles/s41746-026-02869-y) | npj Digital Medicine | Dynamic clinical data + established knowledge graph → adaptive tool selection `RSI-Enabler` |
| 2026 | [MultiMed-RAG: Leveraging Multi-Source Knowledge and Agent Collaboration for Medical Tasks](https://www.nature.com/articles/s41746-026-02962-2) | npj Digital Medicine | Dynamic knowledge-source selection + evidence validation + multi-agent retrieval `RSI-Enabler` |

---

<a name="tool-skill-workflow-self-improvement"></a>

# 🛠️ Tool, Skill & Workflow Self-Improvement

Medical agents that improve tool use, clinical skills, planning strategies, workflow execution, or reusable procedural knowledge.

| Year | Paper                                                                                                                                            | Venue                | Improvement Mechanism                                           |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------- | --------------------------------------------------------------- |
| 2026 | [Evolving Medical Imaging Agents via Experience-Driven Self-Skill Discovery (MACRO)](https://arxiv.org/abs/2603.05860) | arXiv | Verified trajectories → recurring tool sequences → autonomous composite-tool synthesis → skill registration `Meta-RSI` |
| 2026 | [Empowering AI Data Scientists Using a Multi-Agent LLM Framework with Self-Evolving Capabilities for Autonomous, Tool-Aware Biomedical Data Analyses](https://www.nature.com/articles/s41551-026-01634-6) | Nature Biomedical Engineering | BioMedAgent learns tool usage and executable workflows through exploration + memory retrieval `Meta-RSI` |
| 2025 | [STELLA: Self-Evolving LLM Agent for Biomedical Research](https://arxiv.org/abs/2507.02004) [[Code](https://github.com/zaixizhang/STELLA)] | arXiv / bioRxiv | Evolving reasoning-template library + autonomous Tool Ocean expansion `Meta-RSI` |
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
| 2026 | [Route, Retrieve, Reflect, Repair: Self-Improving Agentic Framework for Visual Detection and Linguistic Reasoning in Medical Imaging](https://arxiv.org/abs/2601.08192) [[Code](https://github.com/faiyazabdullah/MultimodalMedAgent)] | arXiv | Router → Retriever → Reflector → Repairer + exemplar-memory accumulation `Inference-SI / Persistent-SI` |
| 2026 | [AutoMedBench: Towards Medical AutoResearch with Agentic AI Models](https://arxiv.org/abs/2606.01961) [[Code](https://github.com/AutoMedBench/AutoMedBench)] | arXiv | Stage-level Plan/Setup/Validate/Inference/Submit rubrics expose where agent workflows fail `RSI-Enabler` |
| 2026 | [Detecting Clinical Discrepancies in Health Coaching Agents: A Dual-Stream Memory and Reconciliation Architecture](https://proceedings.mlr.press/v340/pugh26a.html) | MLHC 2026 | EHR-vs-patient-memory reconciliation + discrepancy severity detection `Safety / RSI-Enabler` |
| 2025 | [Towards Medical Complex Reasoning with LLMs through Medical Verifiable Problems](https://aclanthology.org/2025.findings-acl.751/)                 | ACL Findings | Medical verifier + verifier-guided RL `RSI-Enabler`      |
| 2025 | [Localizing Before Answering: A Benchmark for Grounded Medical Visual Question Answering](https://www.ijcai.org/proceedings/2025/853)              | IJCAI 2025   | Grounding/localization feedback `RSI-Enabler`            |
| 2025 | [MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models](https://aclanthology.org/2025.emnlp-main.143/) | EMNLP 2025   | Hallucination evaluator `RSI-Enabler`                    |

### Generator–Evaluator–Reflector Loops

| Year | Paper                                                                                                                                | Venue        | Mechanism                                                      |
| ---- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------ | -------------------------------------------------------------- |
| 2025 | [FRAME: Feedback-Refined Agent Methodology for Enhancing Medical Research Insights](https://aclanthology.org/2025.findings-acl.400/) | ACL Findings | Generator → evaluator → reflector feedback loop `Inference-SI` |
| 2025 | [MCQG-SRefine](https://aclanthology.org/2025.naacl-long.538/)                                                                        | NAACL 2025   | Self-critique → correction → evaluation `Inference-SI`         |

---

<a name="environment-driven-self-improvement"></a>

# 🌍 Environment-Driven Self-Improvement

Systems that learn through interaction with executable clinical, biomedical, EHR, FHIR, simulation, or research environments.

| Year | Paper / Environment                                                                                                         | Venue                | Role                                                                |
| ---- | --------------------------------------------------------------------------------------------------------------------------- | -------------------- | ------------------------------------------------------------------- |
| 2026 | [HealthAgentBench: A Unified Benchmark Suite of Realistic Agentic Healthcare Environments for Challenging Frontier AI Agents](https://arxiv.org/abs/2606.31179) [[Code](https://github.com/microsoft/HealthAgentBench)] | arXiv / Microsoft Research | 54 executable healthcare tasks across 7 environments with task-specific verifiers `RSI-Enabler` |
| 2026 | [AutoMedBench: Towards Medical AutoResearch with Agentic AI Models](https://arxiv.org/abs/2606.01961) [[Code](https://github.com/AutoMedBench/AutoMedBench)] | arXiv | Long-horizon autonomous medical-AI research environment with stage-level evaluation `RSI-Enabler` |
| 2026 | [AgentClinic: A Multimodal Benchmark for Tool-Using Clinical AI Agents](https://www.nature.com/articles/s41746-026-02674-7) | npj Digital Medicine | Sequential multimodal clinical environment `RSI-Enabler`            |
| 2025 | [MedAgentGym](https://arxiv.org/abs/2506.04405)                                                                             | arXiv                | Executable environment + scalable trajectories + RL `Persistent-SI` |
| 2025 | [MedAgentBench: A Realistic Virtual EHR Environment to Benchmark Medical LLM Agents](https://arxiv.org/abs/2501.14654)      | arXiv                | FHIR-compliant EHR environment `RSI-Enabler`                        |
| 2025 | [MedAgentSim: Self-Evolving Multi-Agent Simulations for Realistic Clinical Interactions](https://papers.miccai.org/miccai-2025/0537-Paper2575.html) | MICCAI 2025 | Doctor–patient–measurement simulation + experience retrieval + iterative diagnostic improvement `Persistent-SI` |

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

| Year | Paper                                                                                                                                                                  | Venue                | Meta-Improvement Role                                                                              |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | -------------------------------------------------------------------------------------------------- |
| 2026 | [HealthFlow: Automating Electronic Health Record Analysis via a Strategically Self-Evolving Multi-Agent Framework](https://www.nature.com/articles/s41746-026-03097-0) | npj Digital Medicine | Distills successes and failures into persistent strategic knowledge for future planning `Meta-RSI` |
| 2025 | [DrAgent](https://aclanthology.org/2025.findings-emnlp.848/)                                                                                                           | EMNLP Findings       | Recursive curriculum optimization for increasingly difficult clinical reasoning `Persistent-SI`    |
| 2025 | [FRAME](https://aclanthology.org/2025.findings-acl.400/)                                                                                                               | ACL Findings         | Generator–evaluator–reflector iterative refinement `Inference-SI`                                  |

### Direct Medical Recursive / Meta Self-Improvement

| Year | Paper | Venue | Meta-Improvement Role |
| ---- | ----- | ----- | --------------------- |
| 2026 | [MedRSI: Recursive Self-Improvement for Medical Agents via Clinically Aligned Self-Evolution](https://arxiv.org/abs/2609.24838) [[Code](https://github.com/ImprintLab/MedRSI)] | arXiv | Diagnostic failure → clinical-cost prioritization → capability invention → validation → conservative registration → persistent capability expansion `Meta-RSI` |
| 2026 | [BaT: Towards Self-Evolving Medical Research Agent with Stage Rubrics](https://arxiv.org/abs/2608.16211) [[Code](https://github.com/AutoMedBench/Benchmark-as-Teacher)] | arXiv | Benchmark failure → stage curriculum selection → rubric-verified GRPO → checkpoint update → re-evaluation `Meta-RSI` |
| 2026 | [Evolving Medical Imaging Agents via Experience-Driven Self-Skill Discovery (MACRO)](https://arxiv.org/abs/2603.05860) | arXiv | Experience → skill discovery → composite-tool synthesis → tool registration → learned reuse `Meta-RSI` |
| 2026 | [Empowering AI Data Scientists Using a Multi-Agent LLM Framework with Self-Evolving Capabilities for Autonomous, Tool-Aware Biomedical Data Analyses](https://www.nature.com/articles/s41551-026-01634-6) | Nature Biomedical Engineering | Interactive exploration → workflow/tool learning → memory accumulation → improved future biomedical analysis `Meta-RSI` |
| 2025 | [STELLA: Self-Evolving LLM Agent for Biomedical Research](https://arxiv.org/abs/2507.02004) [[Code](https://github.com/zaixizhang/STELLA)] | arXiv / bioRxiv | Experience → reasoning-template evolution + autonomous tool creation → expanded future capability `Meta-RSI` |
| 2026 | [Traj-Evolve: A Self-Evolving Multi-Agent System for Patient Trajectory Modeling in Lung Cancer Early Detection](https://arxiv.org/abs/2606.02812) | arXiv | Experience accumulation + retrieval evolution + multi-agent policy optimization `Persistent-SI` |
| 2026 | [EvoMDT: A Self-Evolving Multi-Agent System for Structured Clinical Decision-Making in Multi-Cancer](https://www.nature.com/articles/s41746-025-02304-8) [[Code](https://github.com/KesselZ/EvoMDT)] | npj Digital Medicine | Feedback/outcome signals evolve prompts, consensus weights, and retrieval scope `Persistent-SI` |
| 2026 | [Evo-MedAgent: Beyond One-Shot Diagnosis with Agents That Remember, Reflect, and Improve](https://arxiv.org/abs/2604.14475) | arXiv | Cross-case reflection evolves clinical episodes, procedural heuristics, and tool reliability `Persistent-SI` |
| 2026 | [MDTeamGPT: Mitigating Context Collapse and Enabling Self-Evolution in Medical Multi-Agent Reasoning](https://aclanthology.org/2026.findings-acl.1427/) [[Code](https://github.com/KaiChenNJ/MDTeamGPT)] | ACL Findings 2026 | Structured extraction of successful reasoning and errors into reusable evolving knowledge bases `Persistent-SI` |

---

<a name="safety-reliability-governance"></a>

# 🛡️ Safety, Reliability & Governance

Self-improving medical AI must ensure that improvement does not introduce new clinical risks, amplify hallucinations, propagate erroneous experience, or degrade previously acquired capabilities. Medical-RSI therefore requires **continuous safety evaluation, grounding verification, failure detection, uncertainty-aware behavior, no-regression mechanisms, and governed model updates**.

### Hallucination, Grounding & Clinical Error Detection

| Year | Paper / Resource                                                                                                                                                 | Venue             | Safety / Reliability Role                                                                             |
| ---- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ----------------------------------------------------------------------------------------------------- |
| 2025 | [MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models](https://aclanthology.org/2025.emnlp-main.143/)               | EMNLP 2025        | Controlled medical hallucination detection with 10K QA pairs `RSI-Enabler`                            |
| 2025 | [Localizing Before Answering: A Benchmark for Grounded Medical Visual Question Answering](https://www.ijcai.org/proceedings/2025/853)                            | IJCAI 2025        | HEAL-MedVQA evaluates visual grounding and hallucination robustness using 67K VQA pairs `RSI-Enabler` |
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
| 2026    | [EHRFlowBench](https://www.nature.com/articles/s41746-026-03097-0) | 100 expert-curated EHR analysis tasks across 10 categories                              | Planning, execution, verification, recovery, and governed reuse of prior experience `Meta-RSI / RSI-Enabler` |
| 2026    | [AgentClinic](https://www.nature.com/articles/s41746-026-02674-7)  | Multimodal simulated clinical interactions across 9 specialties and 7 languages         | Sequential clinical reasoning, multimodal evidence collection, and tool-use evaluation `RSI-Enabler`         |
| 2025    | [MedAgentBench](https://doi.org/10.1056/AIdbp2500144)              | 300 physician-written EHR tasks; 100 patient profiles with more than 700K data elements | FHIR-based interactive EHR environment for medical-agent evaluation `RSI-Enabler`                            |
| 2025/26 | [MedAgentGym](https://arxiv.org/abs/2506.04405)                    | 72,413 executable medical and biomedical tasks                                          | Environment feedback + verifiable outcomes + scalable training trajectories `Persistent-SI`                  |

---
