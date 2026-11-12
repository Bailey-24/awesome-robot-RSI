# Awesome Robot RSI

Recent papers on robot recursive self-improvement.

[Website](https://Bailey-24.github.io/awesome-robot-RSI/) · [Contributing](CONTRIBUTING.md)

## Papers

### PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data

**First release:** 2026-11-03

![PyRUA-DataFarm Figure 3: grounding, task and expert code, simulated episodes, video rendering and admission, with rejected outputs routed back to the responsible stage.](assets/papers/pyrua-datafarm.png)

*Kewei Zhang, Juncheng Ma et al., PyRUA-DataFarm, Figure 3. CC BY 4.0. [Figure source](https://arxiv.org/html/2611.05320v1#S4.F3).*

Refines and retains robot expert programs from simulator feedback to generate training demonstrations. The November 11 code release adds user-feedback repairs with re-frozen task contracts and fresh hidden-seed admission checks.

[Paper](https://arxiv.org/abs/2611.05320) · [Code](https://github.com/DAGroup-PKU/PyRUA-Lean/tree/DataFarm)

[Project](https://dagroup-pku.github.io/PyRUA-Lean/DataFarm/)

### TAMPAgent: Agentic Belief-Space Planning for Mobile Manipulation

**First release:** 2026-11-02

![TAMPAgent Figure 4: agent hypotheses, planner constraints, tool certification, execution and replanning.](assets/papers/tampagent.png)

*Utkarsh A. Mishra et al., TAMPAgent, Figure 4. CC BY 4.0. [Figure source](https://arxiv.org/html/2611.03584v1#S3.F4).*

Combines an agent with belief-space task-and-motion planning. A single-task self-improvement study retains memory between attempts, allowing earlier failures to guide later solutions.

[Paper](https://arxiv.org/abs/2611.03584)

[Project](https://umishra.me/TAMPAgent/)

### RoboArchitect: Automating the Design of Robotic Agents with Persistent Memory

**First release:** 2026-10-30

![RoboArchitect Figure 2: a coding model diagnoses rollouts and evolves a frozen policy’s harness and persistent memory.](assets/papers/roboarchitect.png)

*Shengguang Wu et al., RoboArchitect, Figure 2. [Figure source](https://arxiv.org/html/2610.42141v1#S2.F2).*

A coding model studies robot rollouts and repeatedly improves the tools, control routines and persistent memory around a frozen VLA policy. The resulting harness is evaluated on unseen scenes and tasks.

[Paper](https://arxiv.org/abs/2610.42141) · [Code](https://github.com/roboarchitect-ai/RoboArchitect)

[Project](https://roboarchitect-ai.github.io/)

### REA: A Routed Embodied Agent Runtime for Asynchronous Brain-Cerebellum Control

**First release:** 2026-10-30

![REA Figure 3: asynchronous policy dispatch from route memory and a boundary-triggered judge gate, compared with blocking control loops.](assets/papers/rea.png)

*Pengfei Zhou et al., REA, Figure 3. CC BY-NC-SA 4.0. [Figure source](https://arxiv.org/html/2610.42053v1#S1.F3).*

Retains development success statistics to route among reusable robot policies, including ASPIRE’s refined and evolved code. It evaluates this memory and a failure-judging gate on held-out episodes.

[Paper](https://arxiv.org/abs/2610.42053) · [Code](https://github.com/InfRec-Cardinal/REA)

[Project](https://mikeeeeeeeeeeeeee.github.io/REA/)

### BioAgent: Self-Directed Skill Acquisition and Capability Growth for Long-Horizon Laboratory Protocols

**First release:** 2026-10-30

![BioAgent Figure 2: requirement analysis, capability matching, targeted teaching, execution verification and offline learning return validated skills to future planning.](assets/papers/bioagent.png)

*Gaojing Zhang et al., BioAgent, Figure 2. [Figure source](https://arxiv.org/html/2610.41383v1#S2.F2).*

Uses execution records to identify missing laboratory skills, request human teaching when needed, and validate new or revised skills. Accepted experience supports offline policy updates and reusable task packages.

[Paper](https://arxiv.org/abs/2610.41383)

[Project](https://suiuko.github.io/bioagentweb/)

### TinyAstral: Transferring Self-Evolving Harnesses to Tiny Generalist Manipulation Agents

**First release:** 2026-10-30

![TinyAstral Figure 2: statistically gated harness evolution, teacher-trajectory distillation and deployment of small students in the same harness.](assets/papers/tinyastral.png)

*Kehong Gong et al., TinyAstral, Figure 2. [Figure source](https://arxiv.org/html/2610.41216v1#S3.F2).*

Coding agents improve a frozen teacher’s tools, memory and recovery, keeping edits that pass paired statistical tests. Teacher trajectories then train small robot agents that reuse the evolved harness.

[Paper](https://arxiv.org/abs/2610.41216) · [Code](https://github.com/Garfield-kh/TinyAstral)

[Data](https://huggingface.co/datasets/kehong/TinyAstral-SFT) · [Models](https://huggingface.co/kehong/TinyAstral-weights) · [Project](https://garfield-kh.github.io/TinyAstral/)

### Gym-Anything for Robotics: Scaling physical simulations with digital agents

**First release:** 2026-10-29

![Gym-Anything Figure 2: simulation selection, creation and audit, task generation, and learning from repeated attempts and privileged experience.](assets/papers/gym-anything-robotics.png)

*Pranjal Aggarwal and Sean Welleck, Gym-Anything for Robotics, Figure 2. CC BY 4.0. [Figure source](https://arxiv.org/html/2610.40565v1#S1.F2).*

Builds audited robot simulations and studies agents that retain notes and code across repeated attempts. RoboWorld also evaluates privileged coaching and VLA training from code-generated demonstrations.

[Paper](https://arxiv.org/abs/2610.40565) · [Code](https://github.com/gym-anything/robotics)

[Project](https://gym-anything.github.io/robotics/)

### Ask to Evolve: A Unified Harness for Lifelong Embodied Navigation with Hybrid Action Space and Persistent Memory

**First release:** 2026-10-29

![EvoLife Figure 2: hybrid navigation actions, active interaction and persistent spatial memory retain experience for future tasks.](assets/papers/evolife.png)

*Kai Sheng et al., EvoLife, Figure 2. [Figure source](https://arxiv.org/html/2610.39446v1#S3.F2).*

Combines navigation with active requests for guidance and persistent spatial memory. It retains place descriptions, observations and interaction history to improve later visits and tasks.

[Paper](https://arxiv.org/abs/2610.39446)

[Project](https://kai-sheng-caesar.github.io/EvoLife-Web/)

### RobotAgentBench: Towards Open-world Robot Autonomy

**First release:** 2026-10-26

![RobotAgentBench Figure 1: household environments, composable tasks and task-level and open-ended scenario evaluation.](assets/papers/robotagentbench.png)

*Lingjun Mao et al., RobotAgentBench, Figure 1. CC BY 4.0. [Figure source](https://arxiv.org/html/2610.34649v1#S1.F1).*

Benchmarks household robot agents that revise and retain reusable control tools from execution feedback. Compares recursive self-improvement across task-level capabilities and open-ended home scenarios.

[Paper](https://arxiv.org/abs/2610.34649) · [Code](https://github.com/AetherLabsAI/RobotAgentBench)

[Data](https://huggingface.co/datasets/AetherLabs-AI/RobotAgentBench-TrainingData) · [Models](https://huggingface.co/AetherLabs-AI/InternVLA-A1.5-RAB) · [Project](https://aetherlabsai.github.io/RobotAgentBench/)

### R²SI: Recursive Robot Self-Improvement via a Bi-Level Agentic System with Agent–Model Co-Evolution

**Report released:** 2026-10-24

Technical report date; the project was announced on 2026-10-17.

![Figure 1: a Recursion Agent tests and releases harness and reactive-model updates for an inner Robot Agent.](assets/papers/worldscape-r2si.png)

*Manifold AI Team, R²SI technical report, Figure 1. [Figure source](https://r2si.worldscape.io/report.pdf#page=2).*

Uses a Robot Agent to execute tasks and a Recursion Agent to improve reusable skills and train the reactive model from rollout feedback. [RoboDojo-Sim Agent #5 · Score 46.58 · Success 39.35% (2026-10-31).](https://robodojo-benchmark.com/leaderboard?bench=sim#agent)

[Paper](https://r2si.worldscape.io/report.pdf)

[Models](https://huggingface.co/manifoldai-research/WorldScape-R2SI) · [Project](https://r2si.worldscape.io/)

### From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation

**First release:** 2026-10-21

![SERA method: a task-history harness around a frozen VLA is revised and selected using rollout feedback.](assets/papers/sera.png)

*Tingwen Du et al., From VLM Planners to Robotic Agents: Self-Evolving Harnesses for History-Dependent Manipulation. Core method figure from the official paper/project. [Figure source](https://stevenkkxs.github.io/sera-webpage/).*

Improves a planning harness from robot rollouts while keeping the low-level VLA fixed, helping the agent track task history and recover from failures.

[Paper](https://arxiv.org/abs/2610.29560) · [Code](https://github.com/StevenKKXS/SERA)

[Project](https://stevenkkxs.github.io/sera-webpage/)

### Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy

**First release:** 2026-10-19

![PhysRSI-Eval workflow: initial evaluation is followed by budgeted attempts with persistent skills, tools, policies, and memory.](assets/papers/physrsi-eval.jpg)

*Zekai Li et al., Where is Physical RSI capability from? An Observational Scaling Law of LLM-as-policy. Core method figure from the official paper/project. [Figure source](https://physrsi-eval.github.io/).*

Evaluates how robot agents improve across repeated attempts, measuring learning speed, interaction cost, and generalization.

[Paper](https://arxiv.org/abs/2610.26848) · [Code](https://github.com/PhysRSI-Eval/PhysRSI-Eval-code)

[Project](https://physrsi-eval.github.io/)

### HexaShell: A Universal Harness for Robot Coding Agents in Simulation and the Real World

**First release:** 2026-10-16

![HexaShell v3 Figure 2: shared robot API, sandboxed Python execution, grounded perception and adapters, with optional retained task skills.](assets/papers/hexashell-v3.png)

*Hongcheng Gao, Jianshu Zeng et al., HexaShell v3, Figure 2. CC BY 4.0. [Figure source](https://arxiv.org/html/2610.23479v3#S2.F2).*

Shares a 14-tool harness across simulators and real robots. An analysis agent drafts reusable task skills from earlier execution records, with human review before evaluation. [RoboDojo-Sim Agent (HexaShell-Preview) #4 · Score 53.18 · Success 46.85% (2026-10-31).](https://robodojo-benchmark.com/leaderboard?bench=sim#agent)

[Paper](https://arxiv.org/abs/2610.23479) · [Code](https://github.com/HexaFuture/HexaShell)

[Project](https://hexafuture.ai/blog/hexashell/)

### InstAgent: A Recursively Self-Improving Agent Operating System for Heterogeneous Robot Collaboration

**First release:** 2026-10-16

![InstAgent Figure 2: BT-based RSI from Skill BTs to collaboration programs. (a) Skill BTs provide reusable capability procedures for task composition. (b) HeteroComposer binds retrieved subtrees to task-specific roles and arguments and composes them with inter-](assets/papers/instagent.png)

*Haoyang Luo et al., InstAgent, Figure 2. [Figure source](https://arxiv.org/html/2610.23098v1#S3.F2).*

Turns execution-time corrections into validated collaboration behavior trees that can be reused by robot teams. Shared multimodal memory preserves context for later tasks and handoffs.

[Paper](https://arxiv.org/abs/2610.23098)

[Project](https://instagent01.github.io/)

### CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots

**First release:** 2026-10-16

![CoEvolve Figure 2: Framework of CoEvolve . The Task Orchestrator commits a team subtask, which the Policy Coder grounds into executable robot policies. Physical verification accepts or rejects the resulting transition; rejected executions trigger structured c](assets/papers/coevolve.png)

*Zicheng Liu et al., CoEvolve, Figure 2. CC BY 4.0. [Figure source](https://arxiv.org/html/2610.23288v1#S1.F2).*

Revises multi-humanoid coordination code from verified physical transitions while keeping motor skills fixed. Accepted coordination examples and experience guide later runs.

[Paper](https://arxiv.org/abs/2610.23288)

### CarryOn: A Dual-Loop Harness for Personalized and Reliable Robot Assistance

**First release:** 2026-10-15

![CarryOn Figure 2: Two loops, one task context. The planning loop grounds a request in persistent context and dispatches supported subtasks. The execution loop retains the VLA for manipulation, with proactive shielding before hazardous contact and recovery af](assets/papers/carryon.png)

*Zixuan Wang et al., CarryOn, Figure 2. CC BY 4.0. [Figure source](https://arxiv.org/html/2610.21453v1#S3.F2).*

Keeps revisable user and scene memory for personalized robot assistance. Reflection on failed rollouts refines reusable recovery skills around a frozen VLA policy.

[Paper](https://arxiv.org/abs/2610.21453) · [Code](https://github.com/JIA-Lab-research/CarryOn)

[Project](https://vincent2311.github.io/Projects/CarryOn/)

### EmbodiedEvo: Self-Evolving Coding Agent For Physical Intelligence

**First release:** 2026-10-13

![EmbodiedEvo method: Playground feedback evolves Skills and Lessons before a frozen harness transfers to fresh Test agents.](assets/papers/embodiedevo.webp)

*Wenyi Li et al., EmbodiedEvo: Self-Evolving Coding Agent For Physical Intelligence. Core method figure from the official paper/project. [Figure source](https://lab.einsia.ai/embodiedevo/).*

Learns reusable code Skills and diagnostic Lessons in a practice scene, then transfers them to new scenes without weight updates. Learned artifacts for 42 RoboDojo tasks are now public. [RoboDojo-Sim Agent #6 · Score 45.08 · Success 38.95% (2026-10-31).](https://robodojo-benchmark.com/leaderboard?bench=sim#agent)

[Paper](https://arxiv.org/abs/2610.18867) · [Code](https://github.com/Einsia/EmbodiedEvo)

[Project](https://lab.einsia.ai/embodiedevo/)

### SEAR: Self-Evolving Agentic Robotics

**First release:** 2026-10-13

![SEAR Figure 2: code policies, live agents, and auto-research update a persistent library from simulation or hardware feedback.](assets/papers/sear.png)

*Xinyi Wang et al., SEAR: Self-Evolving Agentic Robotics. Core method figure from the official paper/project. [Figure source](https://arxiv.org/html/2610.18792v1#S1.F2).*

Studies whether robot agents retain useful skills and memories, and whether those improvements transfer across tasks, simulators, and real robots.

[Paper](https://arxiv.org/abs/2610.18792)

[Project](https://sear.bot/)

### RSI-Nav: Data-Centric Recursive Self-Improvement for Navigation via Policy-Synchronized Language-Action Dual Bootstrapping

**First release:** 2026-10-11

![RSI-Nav Figure 3: the current policy generates instructions, filters them through execution, and updates after each trajectory shard.](assets/papers/rsi-nav.png)

*Songze Li et al., RSI-Nav: Data-Centric Recursive Self-Improvement for Navigation via Policy-Synchronized Language-Action Dual Bootstrapping. Core method figure from the official paper/project. [Figure source](https://arxiv.org/html/2610.15782v1#S3.F3).*

Bootstraps navigation by generating instructions, filtering them through execution, and repeatedly updating the policy with the resulting data.

[Paper](https://arxiv.org/abs/2610.15782) · [Code](https://github.com/OpenGVLab/RSI-Nav)

### Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement

**First release:** 2026-10-08

![COAP Figure 3: coding agents improve a shared stateful library offline; the final program controls the robot without model inference.](assets/papers/coap.png)

*Kairui Hu et al., Embodied Turing Machines: Stateful Code for Robot Recursive Self-Improvement. Core method figure from the official paper/project. [Figure source](https://arxiv.org/html/2610.12369v1#S3.F3).*

Builds a shared stateful code library through execution feedback, then runs robot tasks directly from code without model inference at test time.

[Paper](https://arxiv.org/abs/2610.12369)

### EmbodiedRSI: Active Continual Robot Learning Through Hypothesis-Guided Co-Evolution

**First release:** 2026-10-07

![EmbodiedRSI architecture: the Fast System tests code/skill hypotheses through a Hypothesis Graph while the Slow System consolidates hierarchical memory.](assets/papers/embodiedrsi.png)

*Python Song et al. (2026), EMBODIEDRSI method overview. [Figure source](https://geeksongs.github.io/agentic_robotics/).*

Selects informative robot experiments to test hypotheses and improve executable code, reusable skills, and memory.

[Paper](https://arxiv.org/abs/2610.10498)

[Project](https://geeksongs.github.io/agentic_robotics/)

### EmbodiedSmith: Scaling Embodied Data through Recursive Self-Improvement Flywheel in Simulation

**First release:** 2026-10-06

![EmbodiedSmith Figure 3: Closed-loop robot task generation and validation. (a) Instructions are grounded in the scene, robot configuration, and available skills. (b) The Agent proposes a skill sequence and success conditions, which are used to build and compile a c](assets/papers/embodiedsmith.webp)

*Yikai Qin et al., EmbodiedSmith, Figure 3. [Figure source](https://arxiv.org/html/2610.07969v1#S3.F4).*

Uses simulation checks to revise task code, robot plans and scenes in a coupled generation loop. Accepted executions become demonstrations for training robot policies.

[Paper](https://arxiv.org/abs/2610.07969)

### Co-Evolving Robot Orchestrators and Policies through Deployment

**First release:** 2026-10-06

![Robo-COP Figure 2: The Robo-COP deployment-to-learning loop. A: The orchestrator mixes scripted motion and VLA calls, logs one action stream, and updates memory. B: Judges segment the stream into labeled skills; a controller decides when to train. C: Candidat](assets/papers/robo-cop.webp)

*Xilun Zhang et al., Robo-COP, Figure 2. [Figure source](https://arxiv.org/html/2610.09228v1#S2.F2).*

Curates demonstrations from deployment, selectively fine-tunes robot skills and adopts policies only after verification. The orchestrator updates its memories as the policy changes.

[Paper](https://arxiv.org/abs/2610.09228)

### RobotUse: Allocating Computation, Context, and Decisions

**First release:** 2026-10-04

![RobotUse Figure 1: RobotUse. The main agent decides in language: from the current state, the playbook, and returned reports, it issues an instruction. The subagent decides on the image, selecting points and poses that the robot backend plans and executes, and](assets/papers/robotuse.png)

*Junhoo Lee et al., RobotUse, Figure 1. CC BY 4.0. [Figure source](https://arxiv.org/html/2610.04929v1#S1.F1).*

A between-episode refiner turns robot execution reports into a persistent playbook. Later attempts reuse and revise guidance on spatial choices, recovery and task delegation.

[Paper](https://arxiv.org/abs/2610.04929) · [Code](https://github.com/robotuse-team/RobotUse)

[Project](https://robotuse-team.github.io/)

### Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents

**First release:** 2026-10-01

![RPG pipeline: runtime and privileged agents, video diagnosis, an implementor, and a merger improve a shared skill library.](assets/papers/rpg.webp)

*Yen-Jen Wang et al., Reconstruct, Practice, Go Real: Guided Self-Improvement for Embodied Agents. Core method figure from the official paper/project. [Figure source](https://rpg-robot.github.io/).*

Reconstructs tasks in simulation, improves a shared skill library through practice and failure diagnosis, and transfers it to physical robots.

[Paper](https://arxiv.org/abs/2610.02204)

[Project](https://rpg-robot.github.io/)

### Fewer Tokens, Better Action: GPT-6 Astra Robot Agents with 14% Higher Success Rate but 65% Fewer Tokens

**First release:** 2026-10-01

![Figure 2: composing primitives in Python cells with selective observation feedback.](assets/papers/pyrua-lean.svg)

*Ruiyang Si, Jianxin Bi et al., PyRUA-Lean, Figure 2. [Figure source](https://arxiv.org/html/2610.01939v1/method_red.svg).*

Reduces repeated model calls by letting robot agents compose actions and local checks in Python. The repository also releases PyRUA-RSI’s offline-refined task programs, which run without language-model calls during evaluation. [RoboDojo-Sim Agent #3 · Score 55.26 · Success 50.35% (2026-10-31).](https://robodojo-benchmark.com/leaderboard?bench=sim#agent)

[Paper](https://arxiv.org/abs/2610.01939) · [Code](https://github.com/DAGroup-PKU/PyRUA-Lean)

[Models](https://huggingface.co/DAGroup-PKU/PyRUA-Lean-Coder-v0.1-4B) · [Project](https://dagroup-pku.github.io/PyRUA-Lean/)

### DynaHarness: A Dynamic Physical Harness for Self-Evolving Robot Agents

**First release:** 2026-09-30

![DynaHarness Figure 2: Overview of DynaHarness . The slow brain plans; the fast brain governs execution; the offline loop evaluates updates from recorded evidence.](assets/papers/dynaharness.png)

*Haoyuan Deng et al., DynaHarness, Figure 2. [Figure source](https://arxiv.org/html/2609.40306v1#S3.F2).*

Attributes execution failures to reusable robot capabilities and proposes targeted repairs. Paired regression checks decide which revisions enter the shared physical harness.

[Paper](https://arxiv.org/abs/2609.40306)

[Project](https://denghaoyuan123.github.io/Dynaharness_page/)

### ASENA: Self-evolving Agents for Embodied Navigation

**First release:** 2026-09-30

![ASENA Figure 2: ASENA connects coding agents to physical robots. The system integrates robot sensing, a persistent workspace, supervised execution, and an optional learned navigation policy. Each run is stored as an MCAP record [ 10 ] that aligns sensor an](assets/papers/asena.png)

*An-Chieh Cheng et al., ASENA, Figure 2. CC BY 4.0. [Figure source](https://arxiv.org/html/2609.39207v1#S3.F2).*

Coding agents retain notes and executable skills after inspecting simulation feedback. A shared robot harness supports navigation, interaction and supervised physical execution without changing agent weights.

[Paper](https://arxiv.org/abs/2609.39207)

[Project](https://research.nvidia.com/labs/gear/asena/)

### Make Code as Policy Great Again: Frontier Agents Write, Call, and Evolve Robot Tools

**First release:** 2026-09-30

![URAI Figure 2: Tool development and execution in URAI. (a) Between episodes, the programming agent revises the tool collection, code, and execution strategy using development feedback. Validated versions are frozen before evaluation; model weights remain ](assets/papers/urai.png)

*Shijia Ge et al., URAI, Figure 2. CC BY 4.0. [Figure source](https://arxiv.org/html/2609.39018v1#S3.F2).*

A programming agent uses execution feedback and human guidance to refine reusable robot tools. A separate execution agent selects tools, with validated revisions kept across episodes.

[Paper](https://arxiv.org/abs/2609.39018)

### RoboHarn-Evo: Evolving Hierarchical Physical Knowledge for Self-Improving Robotic Manipulation

**First release:** 2026-09-29

![RoboHarn-Evo method: task planning, grounded action, execution checks, and episode reflection evolve hierarchical knowledge.](assets/papers/roboharn-evo.webp)

*Shifeng Bao et al., RoboHarn-Evo: Evolving Hierarchical Physical Knowledge for Self-Improving Robotic Manipulation. Core method figure from the official paper/project. [Figure source](https://ruckbreasoning.github.io/RoboHarn-Evo/).*

Uses execution feedback to revise hierarchical task and action knowledge while keeping the base model and executor fixed.

[Paper](https://arxiv.org/abs/2609.37583) · [Code](https://github.com/RUCKBReasoning/RoboHarn-Evo)

[Project](https://ruckbreasoning.github.io/RoboHarn-Evo/)

### DexAgent: An Agentic Human2Sim2Robot Framework for Dexterous Manipulation with Self-Evolving Tool Library

**First release:** 2026-09-28

![DexAgent Figure 2: DexAgent converts a single egocentric human video and a task prompt into robot training data through four stages. Stage 1 decomposes the task into subgoals and identifies the manipulated objects and their key properties. Stage 2 reconstruct](assets/papers/dexagent.png)

*Youhui Wang et al., DexAgent, Figure 2. CC BY 4.0. [Figure source](https://arxiv.org/html/2609.35318v1#S3.F2).*

Converts human videos into simulated robot demonstrations using property-specific checks to repair skills and verifiers. Newly developed tools remain in a library for later videos.

[Paper](https://arxiv.org/abs/2609.35318)

[Project](https://dexagent123.github.io/)

### Recursive Harness Distillation across Agents for Robot Manipulation

**First release:** 2026-09-27

![RHD Figure 1: a strong agent distills robot-intervention experience into a playbook refined with a lighter agent’s feedback.](assets/papers/rhd.png)

*Seungyeon Kim et al., Recursive Harness Distillation across Agents for Robot Manipulation. Core method figure from the official paper/project. [Figure source](https://seungyeon.me/RHD/).*

Distills a strong agent’s robot experience into a playbook for a lighter agent, then refines the playbook using the recipient’s feedback.

[Paper](https://arxiv.org/abs/2609.33378)

[Project](https://seungyeon.me/RHD)

### RoboFoundry: System-as-Policy Evolution for Self-Learning Embodied Agents

**First release:** 2026-09-26

![RoboFoundry Figure 2: Overview of RoboFoundry. (a) The inner loop runs task-specific System-as-Policy through context/skill surfaces and semantic/execution bindings, producing embodiment-specific rollouts and traces. (b) The general system supplies reusable cont](assets/papers/robofoundry.webp)

*Jingsong Liang et al., RoboFoundry, Figure 2. [Figure source](https://arxiv.org/html/2609.32862v1#S2.F2).*

Turns execution traces into tested changes to context, memory and hierarchical skills. Recurring repairs are promoted into a shared system for later tasks and robot embodiments.

[Paper](https://arxiv.org/abs/2609.32862)

[Project](https://jingsongliang.com/robofoundry/)

### HarnessPAI: An Evolving Harness for Physical AI

**First release:** 2026-09-24

![HarnessPAI Figure 1: Overview of HarnessPAI , a general physical harness framework.](assets/papers/harnesspai.webp)

*Xin Wang et al., HarnessPAI, Figure 1. [Figure source](https://arxiv.org/html/2609.29166v1#S0.F1).*

Executes fixed robot programs within each rollout, then uses failure feedback to revise code between rollouts. Validated programs and repair skills are kept for reuse and demonstration generation.

[Paper](https://arxiv.org/abs/2609.29166) · [Code](https://github.com/Darwin-Agent/HarnessPAI)

[Project](https://darwin-agent.github.io/HarnessPAI/)

### RACaP: Agentic Reasoning, Acting, and Coding as Policies for Evolvable Robot Learning

**First release:** 2026-09-24

![RACaP Figure 1: RACaP separates code evolution from runtime execution. During evolution, a capability curriculum produces paired rollouts, a visual critic and coding agent revise reusable mechanisms, and native success selects the next version. During depl](assets/papers/racap.png)

*Zexi Li et al., RACaP, Figure 1. [Figure source](https://arxiv.org/html/2609.29394v1#S1.F1).*

Evolves typed robot APIs, a ReAct harness and experience memory through a capability curriculum and paired candidate tests. Deployment reuses frozen APIs while visual reasoning adapts their arguments.

[Paper](https://arxiv.org/abs/2609.29394) · [Code](https://github.com/Robo-Harness/racap)

### Zetta ζ: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence

**First release:** 2026-08-17

![Zetta Z-Harness framework: execution feedback evolves runtime critics and recovery skills around a frozen policy.](assets/papers/zetta.png)

*Xin Ding et al., Zetta ζ: An Efficient Closed-Loop Embodied Harness for Self-Evolving Physical Intelligence. Core method figure from the official paper/project. [Figure source](https://air-embodied-brain.github.io/zetta/).*

Improves runtime critics and recovery skills from execution feedback around a frozen robot policy.

[Paper](https://arxiv.org/abs/2608.16590) · [Code](https://github.com/air-embodied-brain/Zetta-Embodiment)

[Project](https://air-embodied-brain.github.io/zetta/)

### SHAPER: Self-Evolving Embodied Agents via Skill-Harness Evolution

**First release:** 2026-08-11

![SHAPER Figure 2: rollout diagnosis produces textual gradients for sequential skill and harness evolution with sandbox validation and selection.](assets/papers/shaper.png)

*Peidong Wang et al., SHAPER: Self-Evolving Embodied Agents via Skill-Harness Evolution. Core method figure from the official paper/project. [Figure source](https://arxiv.org/html/2608.11350v1#S3.F2).*

Uses rollout diagnosis to evolve reusable skills and the agent’s context-code harness without updating model weights.

[Paper](https://arxiv.org/abs/2608.11350)

### PhyAgentOS: A Self-Evolving Operating System for Embodied Agents with Decoupled Cognitive Planning and Physical Execution

**First release:** 2026-07-18

![PhyAgentOS Figure 3: Overall architecture of PhyAgentOS. The agent layer determines task intent and compiles executable sessions, whereas the runtime layer supervises and performs target interaction. The shared protocol boundary makes the handoff explicit, audi](assets/papers/phyagentos.png)

*Yang Liu et al., PhyAgentOS, Figure 3. [Figure source](https://arxiv.org/html/2607.16636v1#S3.F3).*

Turns verified robot sessions into reusable skills and corrective lessons. File-based state and memory connect planning, supervised execution and later task attempts.

[Paper](https://arxiv.org/abs/2607.16636) · [Code](https://github.com/PhyAgentOS/PhyAgentOS-core)

[Project](https://phy-agent-os.net)

### ASPIRE: Agentic /Skills Discovery for Robotics

**First release:** 2026-06-30

![ASPIRE system overview: execution traces, agentic program search and a reusable skill library (Figure 1).](assets/papers/aspire.png)

*Runyu Lu et al., ASPIRE, arXiv:2607.00272v2, Figure 1. CC BY 4.0. [Figure source](https://arxiv.org/html/2607.00272v2#S1.F1).*

Discovers reusable robot /skills by writing programs, diagnosing execution traces, repairing failures, and retaining successful strategies.

[Paper](https://arxiv.org/abs/2607.00272) · [Code](https://github.com/NVlabs/ASPIRE)

[Project](https://research.nvidia.com/labs/gear/aspire/)

### ENPIRE: Agentic Robot Policy Self-Improvement in the Real World

**First release:** 2026-06-18

![ENPIRE physical autoresearch framework and real-world task overview (Figure 2).](assets/papers/enpire.png)

*Wenli Xiao et al., ENPIRE, arXiv:2606.19980v2, Figure 2. CC BY 4.0. [Figure source](https://arxiv.org/html/2606.19980v2#S0.F2).*

Automates real-world policy improvement through repeated robot resets, execution, outcome verification, and revisions to policy or training code.

[Paper](https://arxiv.org/abs/2606.19980) · [Code](https://github.com/NVlabs/ENPIRE)

[Project](https://research.nvidia.com/labs/gear/enpire/)


## Development

See [build and deployment instructions](docs/使用与部署.md). Edit `data/catalogue.json`, then run `python3 website/build.py` to update the README and website.

## Attribution

Based on [Awesome Robot Use Agent](https://github.com/kairunwen/Awesome-Robot-Use-Agent) by Kairun Wen. [MIT license](LICENSE). Figures retain their original licenses; see [credits](assets/ATTRIBUTION.md).

<!-- Generated by website/build.py from data/catalogue.json. -->
