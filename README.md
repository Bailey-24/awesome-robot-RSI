# Awesome Robot RSI

Recent papers on robot recursive self-improvement.

[Website](https://Bailey-24.github.io/awesome-robot-RSI/) · [Contributing](CONTRIBUTING.md)

## Papers

### PyRUA-DataFarm: LLM Agent as a Cost-Efficient Teleoperator for Real-Ready Robot Data

**First release:** 2026-11-03

![PyRUA-DataFarm Figure 3: grounding, task and expert code, simulated episodes, video rendering and admission, with rejected outputs routed back to the responsible stage.](assets/papers/pyrua-datafarm.png)

*Kewei Zhang, Juncheng Ma et al., PyRUA-DataFarm, Figure 3. CC BY 4.0. [Figure source](https://arxiv.org/html/2611.05320v1#S4.F3).*

Refines robot expert programs through simulator rollouts against a frozen judge, retaining verified experts to generate demonstrations. Independently reviewed video renders turn those rollouts into action-labelled data for training real-robot policies.

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

### RoboHarn-Evo: Evolving Hierarchical Physical Knowledge for Self-Improving Robotic Manipulation

**First release:** 2026-09-29

![RoboHarn-Evo method: task planning, grounded action, execution checks, and episode reflection evolve hierarchical knowledge.](assets/papers/roboharn-evo.webp)

*Shifeng Bao et al., RoboHarn-Evo: Evolving Hierarchical Physical Knowledge for Self-Improving Robotic Manipulation. Core method figure from the official paper/project. [Figure source](https://ruckbreasoning.github.io/RoboHarn-Evo/).*

Uses execution feedback to revise hierarchical task and action knowledge while keeping the base model and executor fixed.

[Paper](https://arxiv.org/abs/2609.37583) · [Code](https://github.com/RUCKBReasoning/RoboHarn-Evo)

[Project](https://ruckbreasoning.github.io/RoboHarn-Evo/)

### Recursive Harness Distillation across Agents for Robot Manipulation

**First release:** 2026-09-27

![RHD Figure 1: a strong agent distills robot-intervention experience into a playbook refined with a lighter agent’s feedback.](assets/papers/rhd.png)

*Seungyeon Kim et al., Recursive Harness Distillation across Agents for Robot Manipulation. Core method figure from the official paper/project. [Figure source](https://seungyeon.me/RHD/).*

Distills a strong agent’s robot experience into a playbook for a lighter agent, then refines the playbook using the recipient’s feedback.

[Paper](https://arxiv.org/abs/2609.33378)

[Project](https://seungyeon.me/RHD)

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
