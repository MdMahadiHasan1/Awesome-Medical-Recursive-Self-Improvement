# Paper catalog

[Home](../README.md) · [Datasets and benchmarks](benchmarks.md) · [Classification guide](taxonomy.md)

Each paper has one primary entry. Venue labels distinguish proceedings and journals from preprints. The [classification guide](taxonomy.md) explains the four evidence labels.

## Contents

- [Surveys](#surveys)
- [Model self-improvement](#model-self-improvement)
- [Data self-improvement](#data-self-improvement)
- [Memory and knowledge](#memory-knowledge-self-improvement)
- [Tools, skills, and workflows](#tool-skill-workflow-self-improvement)
- [Evaluators, verifiers, and feedback](#evaluator-verifier-feedback-improvement)
- [Environment-driven improvement](#environment-driven-self-improvement)
- [Recursive meta-improvement](#recursive-meta-improvement)
- [Safety, reliability, and governance](#safety-reliability-governance)

## Surveys

Field overviews for clinical agents, medical reasoning, and reliability.

- [AI Agents in Clinical Practice: An Evidence Map](https://www.nature.com/articles/s41746-026-02960-4) · npj Digital Medicine, 2026 · **Resource**. Clinical-agent autonomy, deployment, and self-learning landscape.
- [The Role of Agentic Artificial Intelligence in Healthcare: A Scoping Review](https://www.nature.com/articles/s41746-026-02517-5) · npj Digital Medicine, 2026 · **Resource**. Agentic healthcare systems, autonomy, adaptation, and clinical deployment.
- [Multimodal Artificial Intelligence Agents in Healthcare: A Scoping Review](https://www.nature.com/articles/s41746-026-03060-z) · npj Digital Medicine, 2026 · **Resource**. Multimodal agents, tools, memory, orchestration, and clinical environments.
- <a name="the-path-to-self-evolving-clinical-systems"></a>[The Path to Self-Evolving Clinical Systems: Scaling Medical Agents from Assistance to Autonomy](https://arxiv.org/abs/2607.11175) · arXiv preprint, 2026 · **Resource**. Surveys the transition from clinical assistance to more autonomous and adaptive agents.
- [A Survey of LLM-based Agents in Medicine: How Far Are We from Baymax?](https://aclanthology.org/2025.findings-acl.539/) · ACL Findings, 2025 · **Resource**. Reviews architectures and evaluation settings for medical language-model agents.
- [Can We Trust AI Doctors? A Survey of Medical Hallucination in Large Language and Large Vision-Language Models](https://aclanthology.org/2025.findings-acl.350/) · ACL Findings, 2025 · **Resource**. Reviews hallucination in medical language and vision-language models and how it is evaluated.

## Model self-improvement

Weight updates, training recipes, and test-time adaptation for medical models.

### Reinforcement Learning & Verifiable Reasoning

- [Traj-Evolve: A Self-Evolving Multi-Agent System for Patient Trajectory Modeling in Lung Cancer Early Detection](https://arxiv.org/abs/2606.02812) · arXiv preprint, 2026 · **Persistent**. Uses experience and reward-ranked trajectories to update agents for lung cancer risk modeling.
- [MedExAgent: Training LLM Agents to Ask, Examine, and Diagnose in Noisy Clinical Environments](https://arxiv.org/abs/2605.07058) · arXiv preprint, 2026 · **Resource**. Trains a cost-aware questioning and examination policy with supervised fine-tuning and reinforcement learning in a simulated environment.
- <a name="medreasoner"></a>[MedReasoner: Reinforcement Learning Drives Reasoning Grounding from Clinical Thought to Pixel-Level Precision](https://ojs.aaai.org/index.php/AAAI/article/view/38141) · AAAI, 2026 · **Resource**. Uses spatial format and accuracy rewards to train a medical image reasoner that prompts a frozen segmentation model.
- [GMAI-VL-R1: Harnessing Reinforcement Learning for Multimodal Medical Reasoning](https://arxiv.org/abs/2504.01886) · arXiv preprint, 2025 · **Resource**. Combines reinforcement learning and rejection-sampled reasoning data for multimodal medical reasoning.
- <a name="fleming-r1"></a>[Fleming-R1: Toward Expert-Level Medical Reasoning via Reinforcement Learning](https://arxiv.org/abs/2509.15279) · arXiv preprint, 2025 · **Persistent**. Uses verifiable rewards and adaptive hard-example selection to update medical reasoning models.

### Continual & Test-Time Adaptation

- [Shifting Adaptation from Weight Space to Memory Space: A Memory-Augmented Agent for Medical Image Segmentation](https://arxiv.org/abs/2603.05873) · arXiv preprint, 2026 · **Persistent**. Adapts medical segmentation through working memory while keeping the backbone frozen.
- [Continual Alignment for SAM: Rethinking Foundation Models for Medical Image Segmentation in Continual Learning](https://openaccess.thecvf.com/content/CVPR2026F/html/Wang_Continual_Alignment_for_SAM__Rethinking_Foundation_Models_for_Medical_CVPRF_2026_paper.html) · CVPR Findings, 2026 · **Persistent**. Adapts SAM across successive medical segmentation tasks and evaluates retention of earlier capabilities.
- [Test-time Adaptation for Foundation Medical Segmentation Model Without Parametric Updates](https://openaccess.thecvf.com/content/ICCV2025/html/Chen_Test-time_Adaptation_for_Foundation_Medical_Segmentation_Model_Without_Parametric_Updates_ICCV_2025_paper.html) · ICCV, 2025 · **Inference**. Adapts latent representations for medical segmentation without changing model parameters.
- [Progressive Test Time Energy Adaptation for Medical Image Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Zhang_Progressive_Test_Time_Energy_Adaptation_for_Medical_Image_Segmentation_ICCV_2025_paper.html) · ICCV, 2025 · **Persistent**. Adapts a segmentation model progressively to test-domain data using an energy objective.

## Data self-improvement

Methods for generating, filtering, and refining medical supervision.

See also [Fleming-R1](#fleming-r1) for adaptive hard-example selection.

### Self-Generated & Synthetic Medical Data

- <a name="reasonmed"></a>[ReasonMed: A 370K Multi-Agent Generated Dataset for Advancing Medical Reasoning](https://aclanthology.org/2025.emnlp-main.1344/) · EMNLP, 2025 · **Resource**. Generates candidate reasoning paths, verifies them, and repairs steps flagged by the verifier to build a training dataset.
- [A Modular Approach for Clinical SLMs Driven by Synthetic Data with Pre-Instruction Tuning, Model Merging, and Clinical-Tasks Alignment](https://aclanthology.org/2025.acl-long.950/) · ACL, 2025 · **Resource**. Builds synthetic clinical instructions for training modular small language models.
- <a name="mcqg-srefine"></a>[MCQG-SRefine: Multiple Choice Question Generation and Evaluation with Iterative Self-Critique, Correction, and Comparison Feedback](https://aclanthology.org/2025.naacl-long.538/) · NAACL, 2025 · **Inference**. Iteratively critiques, revises, and compares generated multiple-choice questions.

### Automated Annotation, Filtering & Hard Cases

- [UKBOB: One Billion MRI Labeled Masks for Generalizable 3D Medical Image Segmentation](https://openaccess.thecvf.com/content/ICCV2025/html/Bourigault_UKBOB_One_Billion_MRI_Labeled_Masks_for_Generalizable_3D_Medical_ICCV_2025_paper.html) · ICCV, 2025 · **Resource**. Uses automated labeling and filtering to construct a large-scale MRI segmentation training set.

<a name="memory-knowledge-self-improvement"></a>
## Memory and knowledge

Clinical experiences and knowledge that inform later decisions.

### Evolving Clinical Memory

- [EvoClinician: A Self-Evolving Agent for Multi-Turn Medical Diagnosis via Test-Time Evolutionary Learning](https://arxiv.org/abs/2601.22964) · arXiv preprint, 2026 · **Persistent**. Uses graded diagnostic interactions to revise strategy prompts and memory for later cases. [Code](https://github.com/yf-he/EvoClinician)
- [MDTeamGPT: Mitigating Context Collapse and Enabling Self-Evolution in Medical Multi-Agent Reasoning](https://aclanthology.org/2026.findings-acl.1427/) · ACL Findings, 2026 · **Persistent**. Builds reusable knowledge from reflection on medical multi-agent reasoning errors. [Code](https://github.com/KaiChenNJ/MDTeamGPT)
- [Evo-MedAgent: Beyond One-Shot Diagnosis with Agents That Remember, Reflect, and Improve](https://arxiv.org/abs/2604.14475) · arXiv preprint, 2026 · **Persistent**. Retains clinical episodes, procedural heuristics, and information about tool reliability across cases.
- [TheraAgent: Multi-Agent Framework with Self-Evolving Memory and Evidence-Calibrated Reasoning for PET Theranostics](https://arxiv.org/abs/2603.13676) · arXiv preprint, 2026 · **Persistent**. Uses a growing memory of PET theranostics cases to support reasoning about prognosis.
- [SkinGPT-X: A Self-Evolving Collaborative Multi-Agent System for Transparent and Trustworthy Dermatological Diagnosis](https://arxiv.org/abs/2603.26122) · arXiv preprint, 2026 · **Persistent**. Refines a dermatology memory with experience from prior diagnostic cases.
- [ClinicalAgents: Multi-Agent Orchestration for Clinical Decision Making with Dual-Memory](https://doi.org/10.1145/3770855.3818931) · KDD, 2026 · **Inference**. Uses mutable working memory for the current case and retrieves guidelines and cases from static experience memory.

### Evolving Medical Knowledge

- [MedKGent: A Large Language Model Agent Framework for Constructing Temporally Evolving Medical Knowledge Graph](https://www.nature.com/articles/s41746-026-03058-7) · npj Digital Medicine, 2026 · **Resource**. Builds a temporal medical knowledge graph and resolves conflicts as new evidence arrives.
- [An Autonomous AI Agent for Knowledge and Data Cooperation in ED Clinical Decision Support](https://www.nature.com/articles/s41746-026-02869-y) · npj Digital Medicine, 2026 · **Resource**. Selects tools using incoming clinical data and an established knowledge graph.
- [MultiMed-RAG: Leveraging Multi-Source Knowledge and Agent Collaboration for Medical Tasks](https://www.nature.com/articles/s41746-026-02962-2) · npj Digital Medicine, 2026 · **Resource**. Selects among knowledge sources and uses collaborating agents to retrieve and validate evidence.

<a name="tool-skill-workflow-self-improvement"></a>
## Tools, skills, and workflows

Changes to how agents select, compose, and reuse tools.

See also [MACRO](#macro) for composite-tool discovery and [STELLA](#stella) for biomedical research tools.

- [EvoMDT: A Self-Evolving Multi-Agent System for Structured Clinical Decision-Making in Multi-Cancer](https://www.nature.com/articles/s41746-025-02304-8) · npj Digital Medicine, 2026 · **Persistent**. Uses feedback to adjust prompts, consensus weights, and retrieval scope for multi-cancer decision support.
- [ReflecTool: Towards Reflection-Aware Tool-Augmented Clinical Agents](https://aclanthology.org/2025.acl-long.663/) · ACL, 2025 · **Persistent**. Uses experience to inform tool selection and verification in later tasks.
- [DrAgent: Empowering Large Language Models as Medical Agents for Multi-hop Medical Reasoning](https://aclanthology.org/2025.findings-emnlp.848/) · EMNLP Findings, 2025 · **Persistent**. Trains tool-using agents for multi-hop medical reasoning with a curriculum.

<a name="evaluator-verifier-feedback-improvement"></a>
## Evaluators, verifiers, and feedback

Methods that produce feedback or use it to revise outputs.

See also [MCQG-SRefine](#mcqg-srefine) for generator–evaluator feedback in question authoring.

### Medical Verifiers

- [Route, Retrieve, Reflect, Repair: Self-Improving Agentic Framework for Visual Detection and Linguistic Reasoning in Medical Imaging](https://arxiv.org/abs/2601.08192) · arXiv preprint, 2026 · **Persistent**. Reflects on and repairs current imaging outputs, and accumulates exemplars for future cases.
- [AutoMedBench: Towards Medical AutoResearch with Agentic AI Models](https://arxiv.org/abs/2606.01961) · arXiv preprint, 2026 · **Resource**. Stage-level Plan/Setup/Validate/Inference/Submit rubrics expose where agent workflows fail. [Code](https://github.com/AutoMedBench/AutoMedBench)
- [Detecting Clinical Discrepancies in Health Coaching Agents: A Dual-Stream Memory and Reconciliation Architecture](https://proceedings.mlr.press/v340/pugh26a.html) · MLHC, 2026 · **Resource**. Reconciles EHR records with memory derived from patient conversations and scores discrepancy severity.
- [Towards Medical Complex Reasoning with LLMs through Medical Verifiable Problems](https://aclanthology.org/2025.findings-acl.751/) · ACL Findings, 2025 · **Resource**. Constructs verifiable medical reasoning problems and uses the verifier as a training signal.

### Generator–Evaluator–Reflector Loops

- [EndoCogniAgent: Closed-Loop Agentic Reasoning with Self-Consistency Validation for Endoscopic Diagnosis](https://arxiv.org/abs/2508.07292) · arXiv preprint, 2025 · **Inference**. Acquires evidence iteratively, checks it against the image and prior findings, and updates the diagnostic state within a case. [Code](https://github.com/Tyyds-ai/EndoCogniAgent)
- [FRAME: Feedback-Refined Agent Methodology for Enhancing Medical Research Insights](https://aclanthology.org/2025.findings-acl.400/) · ACL Findings, 2025 · **Inference**. Uses evaluator feedback and reflection to revise research responses within a task.

<a name="environment-driven-self-improvement"></a>
## Environment-driven improvement

Training and adaptation through interactions with executable environments. See the [benchmark guide](benchmarks.md#interactive-environments) for evaluation resources.

- [HealthAgentBench: A Unified Benchmark Suite of Realistic Agentic Healthcare Environments for Challenging Frontier AI Agents](https://arxiv.org/abs/2606.31179) · arXiv preprint, 2026 · **Resource**. 54 executable healthcare tasks across 7 environments with task-specific verifiers. [Code](https://github.com/microsoft/HealthAgentBench)
- [AgentClinic: A Multimodal Benchmark for Tool-Using Clinical AI Agents](https://www.nature.com/articles/s41746-026-02674-7) · npj Digital Medicine, 2026 · **Resource**. Simulates clinical interactions that require multimodal evidence collection and tool use.
- <a name="medagentgym"></a>[MedAgentGym: A Scalable Agentic Training Environment for Code-Centric Reasoning in Biomedical Data Science](https://openreview.net/pdf?id=jHDZEUgS4r) · ICLR, 2026 · **Persistent**. Trains agents with offline and online reinforcement learning using executable biomedical tasks and verifiable outputs. [Code](https://github.com/wshi83/MedAgentGym)
- [MedAgentBench: A Virtual EHR Environment to Benchmark Medical LLM Agents](https://doi.org/10.1056/AIdbp2500144) · NEJM AI, 2025 · **Resource**. Provides a virtual FHIR environment for evaluating clinical agent actions.
- [MedAgentSim: Self-Evolving Multi-Agent Simulations for Realistic Clinical Interactions](https://papers.miccai.org/miccai-2025/0537-Paper2575.html) · MICCAI, 2025 · **Persistent**. Uses simulated clinical interactions and retrieves past diagnostic experience.

## Recursive meta-improvement

These systems are starting points for studying recursive improvement. They create tools, adapt curricula, or accumulate reusable experience. The entries identify the state shown to change. See the [classification guide](taxonomy.md) for how to test whether the update procedure itself improved.

- <a name="medrsi"></a>[MedRSI: Recursive Self-Improvement for Medical Agents via Clinically Aligned Self-Evolution](https://arxiv.org/abs/2609.24838) · arXiv preprint, 2026 · **Persistent**. Uses clinical cost to prioritize failures, proposes new diagnostic capabilities, and tests them on later cohorts before registering them. [Code](https://github.com/ImprintLab/MedRSI)
- <a name="bat"></a>[BaT: Towards Self-Evolving Medical Research Agent with Stage Rubrics](https://arxiv.org/abs/2608.16211) · arXiv preprint, 2026 · **Persistent**. Uses stage-level benchmark feedback to select curricula and update a research agent with rubric-verified reinforcement learning. The outer loop reuses a fixed evaluation and curriculum-selection procedure as the checkpoint changes. [Code](https://github.com/AutoMedBench/Benchmark-as-Teacher)
- <a name="healthflow"></a>[HealthFlow: Automating Electronic Health Record Analysis via a Strategically Self-Evolving Multi-Agent Framework](https://www.nature.com/articles/s41746-026-03097-0) · npj Digital Medicine, 2026 · **Persistent**. Writes, revises, and retires reusable planning experience across EHR analysis tasks under a governed memory policy.
- <a name="macro"></a>[Evolving Medical Imaging Agents via Experience-Driven Self-Skill Discovery (MACRO)](https://arxiv.org/abs/2603.05860) · arXiv preprint, 2026 · **Persistent**. Uses recurring tool sequences from execution traces to synthesize and register composite tools for later runs.
- [Empowering AI Data Scientists Using a Multi-Agent LLM Framework with Self-Evolving Capabilities for Autonomous, Tool-Aware Biomedical Data Analyses](https://www.nature.com/articles/s41551-026-01634-6) · Nature Biomedical Engineering, 2026 · **Persistent**. Reuses learned biomedical analysis workflows and tools through an experience memory.
- <a name="stella"></a>[STELLA: Self-Evolving LLM Agent for Biomedical Research](https://arxiv.org/abs/2507.02004) · arXiv preprint, 2025 · **Persistent**. Retains biomedical research experience as reasoning templates and extends the available tool library. [Code](https://github.com/zaixizhang/STELLA)

<a name="safety-reliability-governance"></a>
## Safety, reliability, and governance

Resources for measuring and managing clinical failure modes.

### Hallucination, Grounding & Clinical Error Detection

- [MedHallu: A Comprehensive Benchmark for Detecting Medical Hallucinations in Large Language Models](https://aclanthology.org/2025.emnlp-main.143/) · EMNLP, 2025 · **Resource**. Evaluates medical hallucination detection with controlled answer pairs.
- [Localizing Before Answering: A Benchmark for Grounded Medical Visual Question Answering](https://www.ijcai.org/proceedings/2025/853) · IJCAI, 2025 · **Resource**. Measures whether medical visual answers are grounded in the relevant image regions.
- [MEDEC: A Benchmark for Medical Error Detection and Correction in Clinical Notes](https://aclanthology.org/2025.findings-acl.1159/) · ACL Findings, 2025 · **Resource**. Measures the detection and correction of errors in clinical notes.

### Robustness, Forgetting & Safe Updating

- [Benchmarking Large Language Model-Based Agent Systems for Clinical Decision Tasks](https://www.nature.com/articles/s41746-026-02443-6) · npj Digital Medicine, 2026 · **Resource**. Evaluates clinical-agent reliability, tool use, hallucinations, and safeguards.

### Governance & Lifecycle Control

- [FUTURE-AI: International Consensus Guideline for Trustworthy and Deployable Artificial Intelligence in Healthcare](https://www.bmj.com/content/388/bmj-2024-081554) · The BMJ, 2025 · **Resource**. Defines lifecycle principles covering fairness, universality, traceability, usability, robustness, and explainability.
