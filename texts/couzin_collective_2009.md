
# Collective cognition in animal groups

__Paper Type:__ Review

## M1: System Overview & Implementation
*   **Vector ID:** M1
*   **Vector Type:** Overview

### **1.1 System Description**

*   **Vector ID:** M1.1
*   **Vector Type:** Description
    *   Content: The system under review is collective cognition in animal groups, exemplified by swarming ants, schooling fish, and flocking birds. It explores how social interactions, individual states, environmental modifications, and information amplification/decay processes contribute to adaptive group responses. The system aims to understand the principles of collective decision-making and motion in these groups, drawing parallels with neuronal processes and examining distributed coordination, feedback mechanisms, and the influence of group size and leadership on collective behavior. The purpose is to decipher the relationship between individual and group-level properties in animal collectives and consider collective animal behavior within the framework of cognitive science.
    *   CT-GIN Mapping: `SystemNode` attributes: `systemType: Biological`, `domain: Animal Behavior/Cognitive Science`, `mechanism: Collective Cognition`, `components: Individuals within animal groups, social interactions, environment`, `purpose: Understand principles of collective behavior and decision-making in animal groups`
    *   Implicit/Explicit: Mixed
        *  Justification: The system is explicitly described as collective cognition in animal groups. The components and purpose are inferred from the introduction and overall scope of the review, focusing on social interactions and understanding group behavior.

### **1.2 Implementation Clarity**

*   **Vector ID:** M1.2
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The paper is a review and does not describe a specific implemented system in the material intelligence sense. However, it clearly outlines the concepts and mechanisms involved in collective cognition in animal groups, referencing mathematical models and experimental studies. The clarity is in describing the biological systems and theoretical understanding of collective behavior, rather than the implementation of a material system. The description of models and experiments provides a good level of detail within the scope of a review.
    *   Implicit/Explicit: Explicit
        * Justification: The clarity score is based on the explicit writing style and detailed discussions in the review, which are directly observable in the text.

### **1.3 Key Parameters**

*   **Vector ID:** M1.3
*   **Vector Type:** ParameterTable
    *   Table:
        | Parameter Name | Value | Units | Source (Fig/Table/Section) | Implicit/Explicit | Data Reliability (High/Medium/Low) | Derivation Method (if Implicit) |
        | :------------- | :---: | :---: | :-----------------------: | :-----------------: | :-----------------------------: | :-------------------------------: |
        | Alignment Tendency Range | Varies | Spatial distance/Topology | Box 1, Figure I | Explicit | Medium | Model parameter exploration |
        | Quorum Threshold | Varies | Number of neighbors/Density | Section: Amplification and damping of collective response, Ward et al. [25], Pratt et al. [53] | Explicit | Medium | Experimental observation & model fitting |
        | Pheromone Volatility | High/Low | Qualitative | Section: Collective cognition through environmental modification: foraging ants | Explicit | High | Chemical property |
        | Group Size | Varies | Number of individuals | Section: Group size and collective decision-making | Explicit | High | Empirical observation |
        | Opinion Difference (Conflict) | Angle | Degrees | Section: Leadership and coming to a consensus decision, Couzin et al. [31] | Explicit | Medium | Model parameter in simulations, experimental studies with pigeons [33] |

    *   **Note:** List *up to 5* key parameters characterizing the system's *implementation*.  Provide values and units if possible. If a parameter is not explicitly stated but derived/inferred, clearly state the derivation method. *Always* include units if applicable. If a value is not applicable, write "N/A".  Data Reliability: High = Directly measured, Medium = Derived from measurements/simulations, Low = Estimated/Inferred.

## M2: Energy Flow
*   **Vector ID:** M2
*   **Vector Type:** Energy

### **2.1 Energy Input**

*   **Vector ID:** M2.1
*   **Vector Type:** Input
    *   Content: The primary energy source for animal groups is food and metabolic energy conversion. Individuals expend energy for movement, sensing, and interaction. Environmental energy like sunlight or wind might indirectly influence group dynamics but is not the primary input for collective cognition itself within the context of this review.
    *   Value: N/A
    *   Units: N/A
    *   CT-GIN Mapping: `EnergyInputNode`: attributes - `source: Metabolic Energy`, `type: Chemical`
    *   Implicit/Explicit: Implicit
        *  Justification: While not explicitly stated as 'metabolic energy input', it is implicitly understood that all biological systems, including animal groups, are powered by metabolic energy derived from food.  The review focuses on behavioral and informational aspects, assuming the fundamental energy source.

### **2.2 Energy Transduction**

*   **Vector ID:** M2.2
*   **Vector Type:** Transduction
    *   Content: Energy transduction primarily involves the conversion of metabolic energy into kinetic energy for movement and behavioral actions. Sensory organs transduce environmental stimuli (visual, chemical, mechanical) into neural signals, which are then processed to guide individual behaviors and social interactions. Social interactions further transduce behavioral outputs into informational cues influencing group-level patterns and decisions. For example, muscle contraction transduces chemical energy into motion; photoreceptors transduce light into electrical signals.
    *   CT-GIN Mapping: `EnergyTransductionEdge`: attributes - `mechanism: Metabolic conversion to kinetic energy, sensory transduction (visual, chemical, mechanical)`, `from_node: EnergyInputNode`, `to_node: BehaviorArchetypeNode, ComputationNode`
    *   Implicit/Explicit: Implicit
        *  Justification: The paper implicitly discusses energy transduction by detailing sensory perception and behavioral actions, which inherently involve energy conversion processes in biological systems. Although not explicitly detailed as energy transduction steps, these are fundamental biological processes underlying the described collective behaviors.

### **2.3 Energy Efficiency**

*   **Vector ID:** M2.3
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification/Metrics: The efficiency is likely medium to high in terms of behavioral outcomes. Animal groups often achieve complex tasks (predator avoidance, foraging, migration) collectively, potentially with greater success than individuals alone. However, metabolic efficiency of individual movements and interactions within the group is not quantified and may vary. Qualitatively, collective actions can amplify individual efforts, leading to efficient outcomes at the group level (e.g., rapid predator evasion). Quantitatively, no specific energy efficiency metrics are provided in the review for collective behavior itself, but biological systems are generally optimized for energy use given evolutionary pressures.
    *   CT-GIN Mapping: Attribute of relevant `EnergyTransductionEdge`s. e.g., `EnergyTransductionEdge`: `efficiency: Medium-High (Qualitative)`
    *   Implicit/Explicit: Mixed
      *  Justification: The efficiency is assessed qualitatively as medium-high based on the implicit understanding that collective behaviors enhance survival and foraging success, suggesting functional efficiency. However, lack of explicit quantitative metrics makes it mixed.

### **2.4 Energy Dissipation**

*   **Vector ID:** M2.4
*   **Vector Type:** Dissipation
    *   Content: Energy dissipation occurs through metabolic heat production, friction during movement (both within the environment and between individuals in dense groups), and the energetic costs of neural signaling and information processing. Quantitatively, these dissipation mechanisms are not detailed or measured in the reviewed context. Qualitatively, dissipation is expected to be inherent in all biological processes; for example, movement generates heat due to muscle inefficiency and friction, neural activity consumes energy and generates heat, and social interactions may involve energetic displays or signals.
    *   CT-GIN Mapping: Creates `EnergyDissipationNode`s: `type: Metabolic Heat, Friction, Neural Signaling`, and `EnergyDissipationEdge`s: `process: Movement, Neural computation, Social Interaction`
    *    Implicit/Explicit: Implicit
        *  Justification: Energy dissipation mechanisms are implicitly understood to be present in all biological systems due to thermodynamic principles. The specific forms of dissipation (heat, friction, neural costs) are inferred from general biological knowledge about animal movement, neural activity, and metabolic processes, even though not explicitly quantified or detailed in the review within the context of collective behavior.

## M3: Memory
*   **Vector ID:** M3
*   **Vector Type:** Memory

### **3.1 Memory Presence:**

*   **Vector ID:** M3.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: The review explicitly mentions "collective memory" in the context of animal groups exhibiting hysteresis, where "multiple stable collective states can exist for exactly the same individual behavior, and be dependent on the previous history of group structure." This indicates that past group states influence current and future behavior, which is a form of memory at the collective level. Additionally, individual learning and experience contribute to the informational state of the group; for instance, informed individuals guide naive group members based on their knowledge.
    *    Implicit/Explicit: Explicit
        * Justification: The term "collective memory" and the description of hysteresis are explicit references to memory-like phenomena in animal groups.

### **3.2 Memory Type:**

*   **Vector ID:** M3.2
*   **Vector Type:** Score
*   Score: [5]
*   Justification: The memory type is closer to short-term and collective rather than long-term individual memory storage in materials. The "collective memory" described relates to group structural states and potentially pheromone trails in ants, which decay over time if not reinforced (e.g., evaporative decay of pheromone trails acting as a form of forgetting if not re-laid). Stability varies; collective states can be multistable, indicating some retention, but also susceptible to environmental changes and perturbations. Read-out accuracy is not in terms of bit-perfect recall but rather in influencing group behavior towards previously established patterns or directions. It’s not like rewritable digital memory but more like dynamic pattern retention in a network. The score is moderate due to this dynamic and less-stable nature compared to engineered memory systems.
*   CT-GIN Mapping: Defines the `MemoryNode` type as `MemoryNodeType: Collective, Dynamic State`
*    Implicit/Explicit: Mixed
    * Justification: The concept of "collective memory" and its association with group structure (hysteresis) and pheromone trails are explicit. The assessment of memory type as dynamic and somewhat short-term is inferred from the descriptions of decaying signals (pheromones) and the dynamic nature of animal group behavior, not explicitly quantified as memory retention time in engineering terms.

### **3.3 Memory Retention Time:**

*   **Vector ID:** M3.3
*   **Vector Type:** Parameter
*   Value: [Varies]
*    Units: [Qualitative Descriptor: Short-term to Medium-term]
*   Justification: For "collective memory" related to group structure (hysteresis), retention can last as long as the conditions that maintain the structure persist; this is potentially medium-term (order of hours to days if environmental conditions are stable). For pheromone trails in ants, retention depends on pheromone volatility and reinforcement, ranging from short-term (volatile pheromones, minutes to hours) to medium-term under constant reinforcement (potentially days or weeks for less volatile pheromones and maintained trails). These timescales are inferred from the descriptions of dynamic processes like pheromone decay and behavioral changes, not explicitly quantified with precise retention times in engineered memory units.
*    Implicit/Explicit: Mixed
        * Justification: The review mentions pheromone decay and dynamic states implicitly suggesting limited retention times. The qualitative descriptors (short-term to medium-term) are inferred based on typical timescales of biological and chemical processes described (pheromone evaporation, animal behavioral dynamics), not explicit values from the paper.
*   CT-GIN Mapping: Key attribute of the `MemoryNode`: `retentionTime: Short-term to Medium-term (Qualitative)`

### **3.4 Memory Capacity (Optional - if applicable)**

* **Vector ID:** M3.4
* **Vector Type:** Parameter
*  Value: N/A
*   Units: N/A
*   Justification: The concept of memory capacity in terms of bits or distinct states isn't directly applicable to "collective memory" in the way it is discussed. "Capacity" might be interpreted as the number of stable collective states a group can exhibit (multistability), but this isn't quantified. For pheromone trails, it could relate to the complexity of trail networks or the number of distinct pheromone types used, but again, these are not quantified as "capacity" in bit units or similar measures.  The information stored is more in the form of dynamic patterns and environmental modifications rather than discrete data units.
*    Implicit/Explicit: Implicit
        *  Justification: The inapplicability of direct capacity measurement stems from the implicit, analog nature of "collective memory" as described, which is not presented in terms of digital information units, making direct capacity quantification in bits inappropriate based on the review's context.
*   CT-GIN Mapping: N/A

### **3.5 Readout Accuracy (Optional - if applicable)**

* **Vector ID:** M3.5
* **Vector Type:** Parameter
*   Value: N/A
*   Units: N/A
*   Justification: "Readout accuracy" is not directly applicable as "collective memory" isn't about retrieving specific stored data with fidelity. The "readout" is manifested in the group's behavioral response influenced by past states or environmental modifications (e.g., following pheromone trails). Accuracy would relate to how reliably past experiences guide adaptive future behavior at the group level. This is more about functional relevance than bit-perfect readout accuracy.
*    Implicit/Explicit: Implicit
       *  Justification: The concept of readout accuracy is inferred as less relevant because collective memory in this context is about influencing future behavior adaptively rather than retrieving precise stored information, which is not presented as a key performance metric in the review.
*   CT-GIN Mapping: N/A

### **3.6 Degradation Rate (Optional - if applicable)**
* **Vector ID:** M3.6
* **Vector Type:** Parameter
    *   Value: [Varies]
    *   Units: [Qualitative Descriptor: Slow to Medium]
    *   Justification: Degradation rate varies. For pheromone trails, degradation is due to evaporative decay, which can be a medium-term process (hours to days depending on pheromone type and environmental conditions). For "collective memory" embodied in group structure (hysteresis), degradation might occur more slowly, related to changes in environmental conditions or disruptions to group social structure. There's no precise quantitative degradation rate provided, but qualitatively, it's not instantaneous but occurs over time.
    *    Implicit/Explicit: Mixed
            * Justification: The concept of pheromone decay explicitly implies degradation over time. The qualitative descriptors (slow to medium) and understanding that degradation isn't instantaneous are inferred from the descriptions of dynamic processes and the need for reinforcement to maintain pheromone trails and collective states, lacking specific degradation rates.
    *   CT-GIN Mapping: Attribute of the `MemoryNode`: `degradationRate: Slow to Medium (Qualitative)`

### **3.7 Memory Operations Energy Cost (Optional - if applicable)**
* **Vector ID:** M3.7
* **Vector Type:** Table
*   Table:
    | Memory Operation ID | Energy Consumption per Bit | Power Usage during Operation| Units | Uncertainty | Data Source Reference | Implicit/Explicit | Justification |
    | :------------------ | :--------------------------: | :-----------------------------: | :---: |:-----------------:|:-----------------:|:-----------------:| :------------------ |
    | Pheromone Laying & Response | N/A | N/A | - | N/A | Section: Collective cognition through environmental modification: foraging ants | Implicit | N/A |
    | Maintaining Collective State (Hysteresis) | N/A | N/A | - | N/A | Box 1, Figure I | Implicit | N/A |
*   Implicit/Explicit: Implicit
    *   Justification: Energy costs of memory operations are not quantified or discussed in terms of "per bit" or power usage. Implicitly, pheromone laying and responding, and maintaining collective group states all require metabolic energy expenditure by individual animals, but these costs are not analyzed quantitatively in the review.

### **3.8 Memory Fidelity & Robustness Metrics (Optional - if applicable)**
* **Vector ID:** M3.8
* **Vector Type:** Table
*   Table:
    | Metric ID | Description | Value | Units | CT-GIN Mapping | Data Source | Implicit/Explicit | Justification |
    | :-------- | :---------- | :----: | :---: | :-------------: | :----------: |:-----------------:| :-----------------:|
    | Robustness to Perturbation (Collective State) | Ability to maintain collective state against individual variation/noise | High | Qualitative | Attribute of `MemoryNode` | Box 1, Section: Collective motion | Explicit | Distributed control in groups makes them robust to individual perturbation |
    | Fidelity of Trail Following (Ants) | Accuracy of following pheromone trails | Medium-High | Qualitative | Attribute of `MemoryNode` | Section: Collective cognition through environmental modification: foraging ants | Implicit | Trails guide behavior, not perfect fidelity, depends on trail strength & noise |
*   Implicit/Explicit: Mixed
*   Justification: Robustness of collective states is explicitly mentioned as inherent to distributed control. Fidelity of pheromone trail following is inferred to be medium-high as trails guide behavior, but it's understood that biological systems aren't perfectly error-free; fidelity is functional, not absolute, and influenced by noise and trail strength, though not numerically quantified in the review.

---

## M4: Self-Organization and Emergent Order
*   **Vector ID:** M4
*   **Vector Type:** Self-Organization

### **4.1 Self-Organization Presence:**

*   **Vector ID:** M4.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: Self-organization is a central theme. The paper states, "it was realized that collective behavior can arise from repeated and local interactions and need not be explicitly coded as a global blueprint or template." Examples such as flocking, schooling, and swarming emerge from local interactions among individuals, not from central control. Pheromone trail networks in ants and rhythmic activity in ant nests also arise spontaneously from local deposition and interaction rules, demonstrating emergent order.
    *   Implicit/Explicit: Explicit
        *  Justification: The text explicitly states that collective behavior arises from local interactions, and gives examples like flocking and swarming, which are classic examples of self-organization. The description of ant pheromone trails and rhythmic activity reinforces the presence of emergent order from local rules.

### **4.2 Local Interaction Rules:**

*   **Vector ID:** M4.2
*   **Vector Type:** Rules
    *   Content: Local interaction rules include:
        1.  **Alignment:** Individuals tend to align their direction of travel with near neighbors. (Box 1, Figure Ia, 'zoo' zone of orientation).
        2.  **Attraction:** Individuals are attracted to near neighbors, maintaining group cohesion. (Box 1, Figure Id, 'zoa' zone of attraction).
        3.  **Repulsion:** Individuals exhibit near-range repulsion to avoid collision and maintain personal space. (Box 1, Figure Id, 'zor' zone of repulsion).
        4.  **Quorum Sensing:** Individuals increase their probability of copying a behavior (e.g., direction of travel) as more neighbors commit to that behavior (Ward et al. [25]).
        5.  **Pheromone Deposition and Following (Ants):** Ants deposit pheromones while foraging and are more likely to follow stronger pheromone trails (Deneubourg et al. [1990], Beckers et al. [1993]).
        6.  **Recruitment based on Encounter Rate (Ants Nest Emigration):** Ants recruit to a new nest site based on the rate of encountering other recruiters; quorum sensing by encounter rate (Pratt et al. [2002], Pratt [2005]).
    These rules are typically spatial and based on local information – position, motion of neighbors, or local pheromone concentration.
    *   CT-GIN Mapping: Part of the `AdjunctionEdge` description (local side). These define the "LocalInteraction" category of edges. e.g., `AdjunctionEdge`: `interactionType: Alignment, Attraction, Repulsion, Quorum Sensing, Pheromone Interaction`, `scope: Local, Neighbor-based`, `informationBasis: Position, Motion, Pheromone Concentration`
    * **Implicit/Explicit**: Explicit
        *  Justification:  These local interaction rules are explicitly described throughout the review, particularly in Box 1 for collective motion and in sections discussing quorum sensing in fish and ants, pheromone communication in ants. The descriptions are operational, defining specific behavioral tendencies based on local cues.

### **4.2.1 Local Interaction Parameters:**

* **Vector ID:** M4.2.1
* **Vector Type:** Table
*   Table:
    | Rule ID | Description | Parameter Name | Parameter Value Range | Units | Data Source | Implicit/Explicit | Justification |
    | :------ | :---------- | :------------- | :---------- | :---: | :----------: | :----------------: | :------------: |
    | 1 | Alignment | Range of Alignment | Varies, increasing leads to polarized group | Spatial distance/Topology | Box 1, Figure I, Couzin et al. [2002] | Explicit | Model parameter; range influences group structure |
    | 2, 3 | Attraction, Repulsion | Zone Radius (zor, zoa) | Varies | Spatial distance | Box 1, Figure Id, Couzin et al. [2002] | Explicit | Model parameters define spatial zones of interaction |
    | 4 | Quorum Sensing | Quorum Threshold | Varies | Number of neighbors | Ward et al. [25], Pratt et al. [2002] | Explicit | Parameter influencing decision to copy behavior |
    | 5 | Pheromone Interaction | Pheromone Concentration Threshold | Varies | Concentration units | Deneubourg et al. [1990], Beckers et al. [1993] | Implicit | Implied by description of trail following behavior, although not explicitly a threshold value |
    | 6 | Encounter Rate Threshold | Density Quorum (for transport) | Varies | Ant density in nest | Pratt et al. [2002], Pratt [2005] | Explicit | Threshold density to switch recruitment modes |
### **4.3 Global Order:**

*   **Vector ID:** M4.3
*   **Vector Type:** Order
    *   Content: The global order that emerges includes:
        1.  **Collective Motion Patterns:** Swarms, tori, polarized groups (flocks, schools) (Box 1, Figure I).
        2.  **Pheromone Trail Networks:** Self-organized foraging trails in ants, connecting food sources (Section: Collective cognition through environmental modification: foraging ants).
        3.  **Rhythmic Activity in Ant Nests:** Spontaneous generation and spread of rhythmic activity waves within ant nests (Box 2, Figure I).
        4.  **Consensus Decisions:** Groups reaching consensus on direction of travel or nest site selection (Section: Leadership and coming to a consensus decision, Section: Finding a new home).
    These are macroscopic patterns and behaviors at the group level that are not pre-programmed into individuals but emerge from their local interactions.
    *   CT-GIN Mapping: Defines a `ConfigurationalNode`. e.g., `ConfigurationalNode`: `configurationType: Collective Motion Pattern (Swarm, Flock, School, Torus), Pheromone Trail Network, Rhythmic Activity, Consensus Decision`, `emergentProperty: Cohesion, Polarization, Path Efficiency, Synchrony, Coordinated Decision`
    * **Implicit/Explicit**: Explicit
        *  Justification: The review explicitly describes these global orders as outcomes of collective behavior: collective motion patterns in Box 1 and corresponding figures, pheromone trails and rhythmic activity in ant sections, and consensus decisions discussed throughout. These orders are presented as emergent properties arising from the system, not as externally imposed structures.

### **4.4 Predictability of Global Order:**

*   **Vector ID:** M4.4
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: Predictability is medium-high. Computational models show that given local interaction rules and parameters (like alignment range), different global patterns (swarms, flocks, tori) reliably emerge (Box 1, Figure I). Consensus decision outcomes are statistically predictable based on the distribution of informed opinions (Couzin et al. [31], Figure 1a). However, stochasticity in individual behavior and environmental noise introduce some unpredictability in the precise details of the emergent order (e.g., exact path of a flock, precise shape of a pheromone trail network). Predictability is in terms of statistical tendencies and macroscopic patterns rather than precise micro-state prediction for every individual.
    * **Implicit/Explicit**: Mixed
    *  Justification: The score is based on mixed evidence. The models explicitly demonstrate predictable transitions between global states (swarms, flocks) based on parameter changes. But the acknowledgment of individual stochasticity and environmental noise introduces implicit limitations to perfect predictability, suggesting a probabilistic rather than deterministic emergence of order in real biological systems.
    *   CT-GIN Mapping: Contributes to the `AdjunctionEdge` weight. e.g., `AdjunctionEdge`: `predictabilityScore: 7`

### **4.5. Local Interaction Rules (for Self-Organization)**
* **Vector ID:** M4.5
* **Vector Type:** Table
*   Table:
| Rule ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Source |
| :------ | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :-----: |
| 1 | Alignment Rule: Tendency to align with neighbors | Range of neighbors considered for alignment | Varies, e.g., nearest neighbors to a wider radius | Number of neighbors or spatial units | Explicit | Box 1 Model parameter defining interaction scope | Box 1 |
| 2 | Attraction Rule: Tendency to move towards neighbors | Strength of attraction force | Varies, relative to repulsion and alignment forces | Unitless, relative strength | Explicit | Box 1 Model parameter defining interaction strength | Box 1 |
| 3 | Repulsion Rule: Tendency to avoid collisions with neighbors | Strength of repulsion force | Varies, relative to attraction and alignment forces | Unitless, relative strength | Explicit | Box 1 Model parameter defining interaction strength | Box 1 |
| 4 | Quorum Rule: Increased likelihood to follow a direction if a quorum of neighbors are moving that way | Quorum size | Varies, e.g., from 1 to several neighbors | Number of neighbors | Explicit | Ward et al. [25] Experimental observation | Ward et al. [25] |

### **4.6. Globally Emergent Order and Order Parameters**
* **Vector ID:** M4.6
* **Vector Type:** Table
*   Table:
| Property ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Protocol | Source |
| :---------- | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :------: | :-----: |
| 1 | Group Polarization | Order parameter for alignment | Varies, from 0 (disordered) to 1 (perfectly aligned) | Unitless order parameter | Explicit | Box 1  Emergence from alignment rule | Simulation | Box 1 |
| 2 | Group Cohesion | Measures group compactness | Varies depending on attraction strength | Arbitrary units in simulations | Explicit | Box 1 Emergence from attraction rule | Simulation | Box 1 |
| 3 | Trail Efficiency (Ants) | Path length relative to optimal path | Varies, but trails tend towards shortest paths | Ratio, unitless | Implicit | Section on ant foraging trails Emergence from pheromone deposition & following | Observation, Experiment | Deneubourg et al. [1990], Vittori et al. [2006] |
| 4 | Consensus accuracy | Proportion of group choosing majority direction in conflict situations | Varies, increases with group size, depends on opinion difference | Percentage or proportion, unitless | Explicit | Couzin et al. [31], Biro et al. [33] Emergence from information integration in groups | Simulation, Experiment | Couzin et al. [31], Biro et al. [33] |

### **4.7 Yoneda Embedding and Local-to-Global Mapping Fidelity**

*   **Vector ID:** M4.7
*   **Vector Type:** Table
*   Table:
    | Link Type | Description | Predictability | Yoneda Score | Metrics | Implicit/Explicit | Justification | Source |
    | :-------- | :---------- | :------------- | :----------- | :------ | :----------------: | :------------: | :-----: |
     | Local Alignment Rule -> Polarized Flocking | Alignment at individual level leads to global flocking order | High | 7 | Qualitative assessment from model output (Figure I, Box 1) | Explicit | Strong correlation in models, but stochasticity in real systems | Box 1, Figure I |
    | Local Pheromone Deposition & Following -> Efficient Foraging Trails | Ants using pheromones locally create globally efficient foraging pathways | Medium-High | 6 | Path efficiency measurements (Vittori et al. [2006]), qualitative observation of trail networks | Mixed | Trails statistically efficient, but not always perfectly optimal paths | Vittori et al. [2006], Deneubourg et al. [1990] |
    | Local Quorum Sensing -> Consensus Decisions | Local quorum rules in individuals result in group consensus in direction | Medium-High | 7 | Accuracy of consensus in simulations (Couzin et al. [31]), experimental data (Biro et al. [33]) | Mixed | Statistical predictability of consensus, but individual variation exists | Couzin et al. [31], Biro et al. [33] |
    *   **Yoneda Embedding Fulfillment Score [0-10]:** [Rubric: 0-2: No discernible mapping between local rules and global order. Random global patterns. 3-5: Weak mapping. Global order partially influenced by local rules but highly noisy or unpredictable. 6-8: Moderate mapping. Local rules significantly shape global order with reasonable predictability, but some deviations and stochasticity. 9-10: Strong mapping. Local rules almost fully determine global order with high precision and predictability. Minimal deviation/noise.

Examples: Score 3: Random walk model, individuals move randomly, no global pattern emerges. Score 7: Vicsek model, local alignment robustly leads to flocking, but precise flock shape varies. Score 9: Crystalline self-assembly model with precise local bonding rules leading to highly ordered crystal structures.]
    *   **Metrics:**  Qualitative assessment based on observed predictability in models and experiments. Path efficiency in ant trails. Consensus accuracy in group decisions. Visual inspection of emergent patterns (flocking, trails, rhythmic activity).
    *   **Justification:** Yoneda Embedding score is moderate (6-7) reflecting a reasonably strong, but not perfect, mapping from local interaction rules to global emergent orders. Models demonstrate clear links, especially for collective motion. However, biological systems have inherent stochasticity and environmental influences that prevent perfect predictability. Pheromone trails provide functional efficiency but are not always the absolutely shortest possible paths. Consensus is statistically predictable but individual choices can still deviate. The mapping is robust and significant, but with inherent biological variability.

## M5: Computation
*   **Vector ID:** M5
*   **Vector Type:** Computation

### **5.1 Embodied Computation Presence:**

*   **Vector ID:** M5.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: Computation is embodied in the collective behavior. The review argues that animal groups perform "collective decision-making mechanisms" that "share similar functional characteristics" with neuronal decision-making. Processes like quorum sensing in fish and ants involve integrating information from multiple individuals, which constitutes a form of distributed computation. Pheromone trail networks in ants embody a computational process for finding efficient foraging routes through environmental modification and feedback. The synchronization and coordination in groups, and the way information propagates (e.g., waves of turning in flocks) are all forms of computation distributed across the group, not centrally controlled.
    *    Implicit/Explicit: Explicit
        *  Justification: The paper uses terms like "collective decision-making mechanisms" and draws parallels to neuronal information processing. It explicitly discusses how groups "integrate disparate information" and "reach a more accurate consensus decision." These phrases indicate the presence of computation performed by the collective, not just individual reactivity.

### **5.2 Computation Type:**

*   **Vector ID:** M5.2
*   **Vector Type:** Classification
    *   Content: [Analog/Hybrid] The computation is primarily analog. Quorum sensing is a threshold-based analog function integrating continuous signals (number of neighbors, pheromone concentration). Pheromone trail networks act as analog computational substrates, where trail strength (pheromone concentration) represents accumulated information, and trail selection is based on relative strengths, resembling analog competition and weighting mechanisms. The system is hybrid as it involves discrete behavioral choices (e.g., turn or not, recruit or not) based on integrating analog inputs.
    *   CT-GIN Mapping: Defines the `ComputationNode` type. `ComputationNodeType: Analog/Hybrid`, `computationParadigm: Distributed, Bio-inspired`
    *    Implicit/Explicit: Mixed
    *    Justification: The paper doesn't explicitly label the computation as "analog" or "hybrid," but the descriptions of quorum sensing, pheromone trails, and neuronal analogies implicitly point to analog characteristics. Processes are based on integrating continuous signals (number of neighbors, pheromone levels), and decisions are often threshold-based rather than strictly digital logic. The "hybrid" nature is inferred from the combination of continuous signal processing and discrete behavioral outputs.

### **5.3 Computational Primitive:**

*   **Vector ID:** M5.3
*   **Vector Type:** Function
    *   Content: The most basic computational primitives include:
        1.  **Thresholding (Activation Function):** Quorum sensing acts as a thresholding function, where a sufficient number of neighbors or pheromone concentration triggers a behavioral change (e.g., copying direction, switching recruitment mode). (Ward et al. [25], Pratt et al. [2002]). Sub-Type: Thresholding: Step Function, Sigmoid-like (non-linear response to neighbors - Ward et al. [25]).
        2.  **Integration/Summation:** Individuals integrate information from multiple neighbors or cumulative pheromone deposits before making decisions. E.g., integrating neighbor movements in quorum sensing (Ward et al. [25]), temporal integration of inputs in ants (Box 2). Sub-Type: Integration: Weighted Summation (implicitly, based on number of neighbors, pheromone concentration).
        3.  **Competition (Lateral Inhibition):**  Pheromone trail competition in ants, where stronger trails are preferentially reinforced, inhibiting weaker trails. (Section: Collective cognition through environmental modification: foraging ants). Sub-Type: Competition: Winner-Takes-All (simplification; trails are probabilistically chosen based on strength, not strictly winner-takes-all).
        4.  **Feedback (Positive and Negative):** Positive feedback in informational cascades, and negative feedback for damping collective response and preventing oversensitivity. (Section: Amplification and damping of collective response). Sub-Type: Feedback: Positive and Negative Feedback loops (tuning collective response).
    *   **Sub-Type (if applicable):** Thresholding: Step Function, Sigmoid-like; Integration: Weighted Summation; Competition: Winner-Takes-All; Feedback: Positive and Negative
    *   CT-GIN Mapping: Defines the primary function of the `ComputationNode`. e.g., `ComputationNode`: `primitiveFunction: Thresholding, Integration, Competition, Feedback`, `functionType: Non-linear Analog`
    *   Implicit/Explicit: Mixed
    * Justification: The description of quorum sensing and pheromone trail competition explicitly points to thresholding and competition as computational operations. The "integration" and "feedback" aspects are more implicitly described, but are fundamental in understanding how collective decisions are made and how responses are tuned. These are identified as computational primitives by interpreting the described biological processes in computational terms, blending explicit descriptions of behavior and implicit computational interpretations.

### **5.4 Embodied Computational Units**
* **Vector ID:** M5.4
* **Vector Type:** Table
*   Table:
| Unit ID | Description | Processing Power | Energy/Operation | Freq/Resp. Time | Bit-Depth | Data Source | Implicit/Explicit | Justification |
| :------ | :---------- | :--------------- | :--------------- | :--------------: | :-------: | :----------: |:-----------------:| :-----------------:|
| 1 | Individual Animal | Low, individual cognition limitations mentioned | Low metabolic cost per interaction (relative to complex digital computation) | Fast, reaction times on the order of milliseconds to seconds | Analog, continuous signal processing | Throughout review, e.g., Introduction | Implicit | Qualitative assessment based on biological context and comparison |
| 2 | Local Interactions (e.g., Neighbor interaction, Pheromone Interaction) | Low, simple rules | Very low, direct physical coupling, minimal signal processing overhead | Very fast, interaction time scales are immediate/continuous | Analog, continuous physical parameters (position, pheromone concentration) | Box 1, Section on ants | Implicit | Qualitative assessment based on described mechanisms and biological efficiency |

## M6: Temporal Dynamics
*   **Vector ID:** M6
*   **Vector Type:** Temporal

### **6.1 Timescales:**

*   **Vector ID:** M6.1
*   **Vector Type:** ParameterTable
    *   Table:
        | Timescale Description | Value | Units | Source | Implicit/Explicit | Justification |
        | :-------------------- | :---: | :---: | :----: | :----------------: | :------------: |
        | Individual Reaction Time (Fish) | Rapid | Seconds | Introduction, Ward et al. [25] | Implicit | Inferred from description of rapid decisions and experimentally studied reaction times |
        | Collective Decision Time (Fish Quorum) | Fast | Seconds to Minutes | Ward et al. [25] | Implicit | Inferred from description of rapid wave of turning and experimental context |
        | Pheromone Trail Decay Time | Short to Medium | Minutes to Days | Section: Ants as mobile neural networks, Section: Foraging Ants | Explicit | Based on pheromone volatility and maintenance |
        | Ant Nest Rhythmic Activity Period | ~20 | Minutes | Box 2, Figure I | Explicit | From Figure I in Box 2 showing activity periodicity |
        | Colony Emigration Decision Time (Ants) | Graded, slow initial phase followed by fast phase | Hours to Days | Section: Finding a new home | Explicit | Described as graded recruitment and speed-accuracy trade-off |

### **6.2 Active Inference:**

*   **Vector ID:** M6.2
*   **Vector Type:** Assessment
    *   Content: [Partial] Partially. Evidence suggests elements of active inference but not fully articulated as such.
        1.  *Prediction*: Animals implicitly "predict" future danger (predator detection) and resource availability (foraging) based on current sensory cues and social information. For example, predator detection and escape responses anticipate future threat.
        2.  *Action Selection*: Groups "choose" directions, nest sites, foraging paths to minimize threats and maximize resources. Consensus decision-making in direction selection and resource allocation in ants are forms of action selection aiming to optimize outcomes.
        3.  *Internal Models*: Less clear if explicit internal models are formed. Implicitly, behavioral rules (alignment, attraction, repulsion, quorum) and responses to pheromones could act as rudimentary "models" of social and environmental dynamics, guiding adaptive behavior.

    Missing is explicit demonstration of hierarchical predictive models, explicit minimization of prediction error, or iterative model refinement common in active inference frameworks. Behaviors are more characterized by reactive and adaptive responses based on sensory information and local rules, rather than explicitly model-based predictive control in the active inference sense.
    *   Justification: While not explicitly framed as active inference, elements of prediction and action selection are evident in collective behaviors. The "internal model" aspect is weaker and more implicit.  The system shows adaptive responses but lacks clear evidence for complex, hierarchical predictive models typical of full active inference.
    *   Implicit/Explicit: Mixed
        *  Justification: Aspects of prediction and action selection are implicitly present by analyzing the functional outcomes of collective behaviors (predator avoidance, foraging success, consensus decisions). The "internal model" aspect is even more inferred, representing a potential interpretation of behavioral rules as implicit models but not explicitly analyzed as such in the review.
    *   **If Yes/Partial, provide examples of testable CT-GIN metrics that *could* be used to quantify active inference:**
        *   Prediction Error Reduction Rate: Measure how quickly groups reduce behavioral variance or uncertainty after encountering a stimulus (e.g., predator appearance). Higher rate suggests better prediction and error minimization.
        *   Timescale of Anticipation:  Assess latency between stimulus onset and collective response initiation. Shorter latency for adaptive responses could indicate anticipatory mechanisms.
        *   Complexity of Implicit Models:  (Difficult to quantify directly in animal groups). In agent-based models of collective behavior, analyze the complexity of rule sets required for agents to exhibit adaptive collective behaviors. More complex rule sets *might* correlate with more elaborate implicit models.
        *   Adaptation Rate of Behavioral Parameters: If behavioral rules (e.g., alignment strength, quorum threshold) adapt over time based on environmental feedback, measure the timescale of this adaptation. Faster adaptation suggests learning and model refinement.
        *   Information Gain in Collective Decisions: Quantify the information gain (reduction in entropy/uncertainty) from individual to collective decisions. Higher information gain suggests effective information processing and model utilization in collective decision-making.

## M7: Adaptation
*   **Vector ID:** M7
*   **Vector Type:** Adaptation

### **7.1 Adaptive Plasticity Presence:**

*   **Vector ID:** M7.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: Yes, adaptive plasticity is present. The review describes tuning collective response through regulation of positive and negative feedback, enabling "adaptive tuning of collective behavior in response to external stimuli and/or internal state."  Ant colony foraging strategies adapt to resource availability, using pheromone volatility to differentiate between short-term and long-term resource information, demonstrating plasticity in response to changing environmental conditions. Ants also adjust recruitment speed and quorum thresholds depending on the urgency of a situation (e.g., nest destruction), showing adaptive modulation of behavioral parameters.
    *    Implicit/Explicit: Explicit
        * Justification: The text explicitly uses the term "adaptive tuning" and provides examples of ants adjusting their behavior based on environmental changes and urgency. The description of pheromone-based memory as "working memory" and "selective attention" implies adaptive functionality that goes beyond fixed stimulus-response reactions.

### **7.2 Adaptation Mechanism:**

*   **Vector ID:** M7.2
*   **Vector Type:** Description
    *   Content: Adaptation mechanisms include:
        1.  **Feedback Regulation:** Tuning collective response through balancing positive (amplification, recruitment) and negative (damping, decay) feedback loops. This allows for speed-accuracy trade-offs in decision-making and flexible response modulation.
        2.  **Pheromone-Based Memory:** Using pheromones with different volatilities for short-term (volatile) and long-term (less volatile) information storage, enabling adaptive foraging strategies to exploit both new and established resources. This is a form of environmental modulation acting as a memory and adaptive control signal. "Working memory" encoded using slowly decaying chemicals (pheromones).
        3.  **Quorum Threshold Tuning:**  Adjusting quorum thresholds for recruitment speed (ants). Lowering quorum thresholds increases recruitment speed in urgent situations, trading accuracy for speed in a context-dependent manner. A tunable algorithm for collective decision-making (Pratt & Sumpter [2006]).
        4.  **Non-linear Response to Neighbors (Fish):** Sticklebacks exhibit a non-linear response to neighbor movements, largely ignoring single neighbors but strongly responding to a quorum. This improves accuracy by integrating information while minimizing time costs (Ward et al. [25]).
        These mechanisms are environmentally driven (resource availability, urgency, neighbor behavior) and involve internal dynamic adjustments (feedback loop tuning, pheromone use, threshold modulation) leading to altered functionality over time in response to experience and conditions.
    *   CT-GIN Mapping: Defines the `AdaptationNode` type and `Monad` edges. Specify the type of adaptation mechanism: `AdaptationNode`: `adaptationType: Feedback Regulation, Pheromone-based Memory, Quorum Threshold Tuning, Non-linear Response`, `mechanismDetails: Positive/Negative Feedback Control, Chemical Memory Encoding, Threshold Modulation, Non-linear Signal Processing`. `MonadEdge`: Indicates self-modification of behavior or internal parameters.
    *    Implicit/Explicit: Mixed
        *  Justification: Feedback regulation and pheromone-based memory are explicitly mentioned as adaptive processes in the review. Quorum threshold tuning and non-linear neighbor response are described as mechanisms that improve decision accuracy and speed, implicitly representing forms of adaptation in response strategies. The interpretation of these mechanisms as forms of adaptation requires some inference, but is strongly supported by the functional context and terminology used (e.g., "adaptive tuning").

## M8: Emergent Behaviors
*   **Vector ID:** M8
*   **Vector Type:** Behavior

### **8.1 Behavior Description:**

*   **Vector ID:** M8.1
*   **Vector Type:** Description
    *   Content: Main functional behaviors of the system include:
        1.  **Collective Motion:** Coordinated movement as flocks, schools, swarms, with emergent properties like cohesion, polarization, rapid information transfer, and predator evasion. (Section: Collective motion).
        2.  **Collective Decision-Making:** Groups reach consensus decisions on direction, resource location, nest sites, overcoming individual limitations and integrating distributed information. (Section: Leadership and coming to a consensus decision, Section: Finding a new home).
        3.  **Efficient Foraging:** Ants self-organize efficient foraging routes and adaptively allocate foragers to food sources using pheromone trails. (Section: Collective cognition through environmental modification: foraging ants).
        4.  **Rhythmic Activity Coordination:**  Spontaneous, rhythmic activity patterns emerge within ant nests, potentially optimizing task allocation and response to external stimuli. (Box 2).
        5.  **Speed-Accuracy Trade-off Optimization:** Groups balance speed and accuracy in decision-making, exemplified by quorum sensing in fish and graded recruitment in ants, adjusting response speed adaptively based on context and urgency. (Section: Feedback and the speed–accuracy trade-off, Section: Finding a new home).
    These are observable, functional behaviors at the group level, resulting from collective dynamics, not predetermined individual actions.
    *   CT-GIN Mapping: Defines the `BehaviorArchetypeNode`. Specify the type of behavior: `BehaviorArchetypeNode`: `behaviorType: Collective Motion, Collective Decision-Making, Efficient Foraging, Rhythmic Coordination, Speed-Accuracy Trade-off Optimization`, `functionalOutcome: Cohesion, Polarization, Consensus, Path Efficiency, Synchrony, Rapid Response, Adaptability`
    *    Implicit/Explicit: Explicit
       *  Justification: The review explicitly describes these behaviors as emergent properties of animal groups - collective motion, decision-making, efficient foraging, rhythmic activity, and optimization of speed-accuracy trade-offs. These are presented as functional outputs of the collective system, observable and measurable characteristics of group behavior.

### **8.2 Behavior Robustness:**

*   **Vector ID:** M8.2
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: Robustness is relatively high. Distributed control and lack of central leadership make collective behaviors robust to individual perturbation or failure. The paper states, "Because distributed coordination does not depend on a specific subset of individuals, groups are inherently robust to perturbation." Redundancy in information and distributed decision-making increase resilience. For example, if some individuals in a flock make errors, the overall flock direction is maintained due to averaging and social influence. Pheromone trail networks can tolerate individual ant path deviations, and trails are reinforced by multiple ants, enhancing reliability. Robustness is not absolute; extreme perturbations or environmental changes can still disrupt collective behavior, but the decentralized nature enhances resilience to typical variations and noise.
    *   Implicit/Explicit: Explicit
        *  Justification: The review explicitly mentions robustness as a consequence of distributed coordination. Examples provided, such as flocking and pheromone trails, implicitly demonstrate tolerance to individual variations and errors, supporting the assessment of high robustness. The score reflects this explicit statement and implicit evidence of resilient behavior.
    *   CT-GIN Mapping: This score contributes to the reliability attributes of the `BehaviorArchetypeNode`. e.g., `BehaviorArchetypeNode`: `robustnessScore: 8`

### **8.3 CT-GIN Emergent Behavior Validation**

*    **Vector ID:** M8.3
*    **Vector Type:** Validation
     *  Content: Validation methods used in the reviewed literature include:
        1.  **Computational Modeling:** Mathematical models (particle physics inspired, agent-based models) are extensively used to simulate collective behavior. Models demonstrate emergence of collective motion (swarms, flocks) from local interaction rules (Box 1, Figure I). Models also predict and explain consensus decision-making (Couzin et al. [31], Figure 1a). Operational definitions for collective motion patterns and consensus are implicit in model outputs.
        2.  **Experimental Studies on Animal Groups:** Empirical studies on fish (Ward et al. [25], Sumpter et al. [2008]), birds (Biro et al. [33]), ants (Pratt et al. [2002], Deneubourg et al. [1990]) validate model predictions and observe real collective behaviors. Quantitative analysis includes measuring fish turning responses (Ward et al. [25]), pigeon flight paths (Biro et al. [33]), ant trail efficiency (Vittori et al. [2006]), and ant activity rhythms (Boi et al. [1999]). Control experiments are implicitly used by comparing model predictions to observations under different conditions. Robustness and reproducibility are implicitly demonstrated by consistent model outcomes and replicable experimental findings across various studies cited. Limitations include simplification in models compared to biological complexity and challenges in precisely quantifying all aspects of animal behavior. Figures and sections throughout the review, especially Box 1, Box 2, and cited experimental papers, provide evidence.
     *   Implicit/Explicit: Mixed
    *   Justification: Validation methods are mixed explicit and implicit. The use of computational modeling and experimental studies is explicitly mentioned as approaches to understand collective behavior. Specific examples of experimental work and modeling results are cited throughout the review, providing explicit evidence for validation efforts. However, the operational definitions of emergent behaviors, the use of control experiments, and the assessment of robustness and reproducibility are more implicitly inferred from the general scientific methodology of the reviewed studies rather than explicitly detailed for each case in the review itself.

## M9: Cognitive Proximity
*   **Vector ID:** M9
*   **Vector Type:** Cognition

### **9.1 Cognitive Mapping:**

*   **Vector ID:** M9.1
*   **Vector Type:** Description
    *   Content: Yes, there is a significant attempt to map system functionality to cognitive processes. The central theme is to consider "collective animal behavior in the framework of cognitive science." Analogies are explicitly drawn between collective decision-making in animal groups and neuronal decision-making in brains.
        *   **Analogies:**
            1.  **Distributed Coordination:** Parallels between distributed coordination in animal groups and neuronal assemblies.
            2.  **Feedback Mechanisms:** Commonality in feedback processes (positive and negative) tuning collective response in both animal groups and neural systems.
            3.  **Multistability:** Analogy between multistability in collective states of animal groups and multistability (attractors) in neural systems, suggesting potential functional benefits for memory or pattern recognition.
            4.  **Speed-Accuracy Trade-off:** Similar challenges and optimization of speed-accuracy trade-offs in both animal group and brain decision-making.
            5.  **Quorum Sensing & Thresholding:** Functional parallels between quorum sensing in groups and threshold processes in neuronal decision circuits.
            6.  **Ant Colonies as Neural Networks:** Explicit analogy of ant colonies as "mobile neural networks," with ants behaving in a neuron-like fashion and colony activity resembling neuronal network dynamics (Box 2).
            7.  **Competition and Lateral Inhibition:** Similarities between competition among pheromone trails in ants and competition among neuronal groups in brain decision processes.
            8.  **Hebbian Reinforcement:** Analogy between reinforcement of pheromone trails in ants and Hebbian reinforcement of neuronal pathways (long-term potentiation).
        *   **Limitations:**  Analogies are functional and at a "certain level of description."  Biological details differ significantly between animal groups and neurons.  Cognitive mapping is metaphorical and aimed at revealing shared principles of distributed information processing, not claiming animal groups are literally "brains." Animal cognition and collective behavior are distinct levels of biological organization.

    *   CT-GIN Mapping: If a mapping exists, this defines a `CognitiveMappingEdge`. Specify source and target (e.g., `BehaviorArchetypeNode` to `CognitiveFunctionNode`).  e.g., `CognitiveMappingEdge`: `sourceNode: BehaviorArchetypeNode (Collective Decision-Making, Efficient Foraging)`, `targetNode: CognitiveFunctionNode (Decision-Making, Memory, Attention)`, `mappingType: Functional Analogy`, `analogyBasis: Distributed Processing, Feedback Control, Speed-Accuracy Trade-off`
    *   Implicit/Explicit: Explicit
    * Justification: The review explicitly aims to bridge the gap between collective animal behavior and cognitive science. The paper directly states the proposal of "commonalities" with neuronal processes and suggests considering animal behavior "in the framework of cognitive science." Numerous analogies between specific collective behaviors and neuronal functions are explicitly detailed throughout the text. The limitations and metaphorical nature of these mappings are also implicitly acknowledged by emphasizing "commonalities" at a "certain level of description," avoiding strong claims of direct equivalence.

### **9.2 Cognitive Proximity Score:**

*   **Vector ID:** M9.2
*   **Vector Type:** Score
    *   Score: [4]
    *   Justification: Cognitive Proximity Score: Level 4: Goal-Directed/Model-Based Cognition. Justification: The system exhibits aspects aligning with Level 4.
        *   **Goal-Directed Behavior:** Animal groups exhibit goal-directed behaviors like foraging (resource seeking), predator avoidance (threat minimization), and nest site selection (habitat optimization). Consensus decisions suggest group "goals."
        *   **Model-Based Cognition (Implicit):** While not explicit "models" in the human sense, behavioral rules (alignment, pheromone response, quorum sensing), and environmental modifications (pheromone trails) collectively act as implicit "models" of their social and environmental world. These guide behavior and adapt to changing conditions.  For example, pheromone trails represent learned/reinforced paths to resources. Quorum sensing models social information usefulness.
        *   **Reactive/Adaptive Autonomy (Level 3):**  System clearly demonstrates reactive and adaptive autonomy (Level 3) by adjusting behavior to stimuli and learning from experience (e.g., pheromone trail learning).
        *   **Beyond Level 4 Limitations:**  Lacks evidence for higher-level cognitive functions (Levels 5-10). No discussion of contextual/relational cognition, abstract/symbolic thought, social cognition (beyond basic group interaction), metacognition, or consciousness. "Models" are implicit and behavioral, not demonstrably complex, abstract internal representations. Goal-directedness is functional and ecological, not requiring conscious intent in individuals. Cognitive proximity at level 4 is based on functional analogies and distributed information processing, not implying human-like cognition in animal groups. The score is moderate, acknowledging functional complexity and parallels to cognitive processes, but also significant limitations compared to higher cognitive levels.
    *   Implicit/Explicit: Mixed
    *  Justification: The score reflects a mixed assessment. The goal-directed behavior is reasonably explicit in functional descriptions of foraging, predator avoidance, and consensus decisions. "Model-based cognition" is more implicit – inferred by interpreting behavioral rules and environmental modifications as forms of implicit models guiding behavior. The limitations and lack of higher-level cognitive functions are also implicitly understood by the scope and focus of the review, avoiding claims of advanced cognition in animal groups while highlighting functional parallels to basic cognitive processes.

**CT-GIN Cognizance Scale:**

*   **Level 0: Non-Cognitive:** Purely reactive system.  No internal state beyond immediate stimulus-response.
*   **Level 1: Simple Responsivity:** Basic stimulus-response behavior.  Reactions are fixed and predetermined.
*   **Level 2: Sub-Organismal Responsivity:**  Behavior exhibits basic forms of adaptation or plasticity, but lacks complex representation or goal-directedness.
*   **Level 3: Reactive/Adaptive Autonomy:** System adapts its behavior based on experience and feedback, but within a limited behavioral repertoire.
*   **Level 4: Goal-Directed/Model-Based Cognition:** System exhibits goal-directed behavior based on internal models of the world, allowing for planning and flexible action selection.
*   **Level 5: Contextual/Relational Cognition:** System understands and responds to relationships between objects, events, and concepts.
*   **Level 6: Abstract/Symbolic Cognition:** System can manipulate abstract concepts and symbols, enabling logical reasoning and problem-solving.
*   **Level 7: Social Cognition:** System exhibits social intelligence, understanding and interacting with other agents.
*   **Level 8: Metacognition/Self-Awareness:** System possesses awareness of its own internal states and cognitive processes.
*   **Level 9: Phenomenal Consciousness:**  System exhibits subjective experience (qualia). (Currently theoretical for material systems)
*   **Level 10: Sapience/Self-Reflective Consciousness:** System possesses self-awareness, understanding of its own existence, and ability for complex abstract thought. (Currently theoretical for material systems)

### **9.3 Cognitive Function Checklist**

* **Vector ID:** M9.3
* **Vector Type:** Checklist
    *   | Cognitive Function               | Score (0-10) | Justification/Notes                                                                       | CT-GIN Mapping (if applicable) | Implicit/Explicit | Justification for Implicit/Explicit/Mixed |
    | :-------------------------------- | :----------: | :------------------------------------------------------------------------------------ | :--------------------------------: | :-----------------:|:-----------------:|
    | Sensing/Perception               |      7       | Effective sensing of environment and social cues; limitations in individual range but collective amplification. | `CognitiveFunctionNode: Sensing/Perception`   | Explicit          |  Sensing discussed in relation to collective response. |
    | Memory (Short-Term/Working)        |      5       | "Collective Memory" described; short to medium term, dynamic state, pheromone trails. Forgetting/decay present. | `CognitiveFunctionNode: Memory (Short-Term/Working)`  | Explicit          | "Collective memory" term used explicitly.          |
    | Memory (Long-Term)                 |      3       | Limited. Pheromone trails can be long-lasting but require reinforcement. Hysteresis as very basic "long-term" state retention. | `CognitiveFunctionNode: Memory (Long-Term)`   | Implicit          | Long-term aspect is weaker, inferred from limitations of described memory mechanisms. |
    | Learning/Adaptation              |      7       | Adaptive tuning via feedback, pheromone learning, quorum threshold adjustment. Plasticity in response.                          | `CognitiveFunctionNode: Learning/Adaptation` | Explicit          | "Adaptive tuning" and mechanisms are explicitly described. |
    | Decision-Making/Planning          |      7       | Collective decision-making on direction, nest sites, resource allocation. Consensus processes. Goal-directed behavior.         | `CognitiveFunctionNode: Decision-Making/Planning` | Explicit          | Decision-making and consensus are central themes.       |
    | Communication/Social Interaction |      8       | High level of communication and social interaction via local cues, alignment, quorum sensing, pheromones. Distributed coordination. | `CognitiveFunctionNode: Communication/Social Interaction` | Explicit          | Social interactions and communication are core mechanisms described. |
    | Goal-Directed Behavior            |      7       | Foraging, predator avoidance, nest finding – clear functional goals at group level.                                         | `CognitiveFunctionNode: Goal-Directed Behavior` | Explicit          | Functional outcomes explicitly framed as goal-directed behaviors. |
    | Model-Based Reasoning              |      4       | Implicit "models" in behavioral rules, pheromone trails. Very rudimentary level. No abstract reasoning.                       | `CognitiveFunctionNode: Model-Based Reasoning` | Implicit          | "Model-based" aspect is inferred and weaker, implicit in interpreting mechanisms. |
    | **Overall score**                 |      [6]       |                                                                                       |                                   |                     |                |

    *   **Note:** Assess the system for *each* function, providing a score (0-10) and a short (1-2 sentences) justification.  0 = Absent, 10 = Human-level performance.

## M10: Criticality Assessment
*   **Vector ID:** M10
*   **Vector Type:** Criticality

### **10.1 Criticality:**

*   **Vector ID:** M10.1
*   **Vector Type:** Assessment
    *   Content: [Partial] Partial. Hints of criticality but not explicitly demonstrated.
        *   **Evidence for Criticality:**
            1.  **Sudden Transitions:** Abrupt transitions in group state (swarm -> torus -> polarized flock) with gradual parameter changes (alignment range) (Box 1, Figure I) suggest potential for critical transitions and regime shifts, characteristic of systems near criticality.
            2.  **Informational Cascades:** "Informational cascades" where small fluctuations can be amplified into large-scale changes (Section: Amplification and damping of collective response) resemble avalanche-like behavior that is often associated with criticality.
            3.  **Multistability:** Coexistence of multiple stable states (swarms, tori, flocks) for the same parameters (Box 1, Figure I) can be linked to systems operating near bifurcation points in parameter space, a feature of criticality.
            4.  **Self-Organized Rhythmic Activity in Ant Nests:** Spontaneous generation of rhythmic activity waves in ant nests (Box 2, Figure I) is reminiscent of self-organized criticality in excitable media.
        *   **Lack of Explicit Criticality Analysis:**  The review does not explicitly use the term "criticality," nor does it present quantitative evidence of scale-free behavior (power laws) or long-range correlations in animal group systems. Hypotheses are drawn through analogies with neural systems exhibiting self-organized criticality, but criticality is not directly measured or rigorously demonstrated for collective animal behavior within this review.
        *   Critical Parameters (If Yes/Partial): Alignment range, quorum threshold, feedback strengths (positive/negative), pheromone volatility (implicitly influencing dynamics).
        *   Evidence: Qualitative description of sudden transitions (Box 1, Figure I), informational cascades, multistability, self-organized rhythms in ant nests (Box 2, Figure I), analogies to neuronal criticality. Lack of power-law distributions or quantitative criticality metrics reported in this review.
    *   Implicit/Explicit: Mixed
    *    Justification: The assessment of partial criticality is based on mixed evidence. The sudden transitions, informational cascades, multistability, and self-organized rhythms implicitly suggest proximity to critical regimes. These are qualitative indicators, not direct quantitative measures of criticality. The review draws analogies to neuronal systems with criticality (Levina et al. [2007], Plenz & Thiagarajan [2007]), further supporting this interpretation. However, the absence of explicit criticality analysis (power laws, long-range correlations) and direct quantitative evidence makes it partial and inferred rather than definitively demonstrated.

## M11: Review Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Review")**

*   **Vector ID:** M11
*   **Vector Type:** Review

### **11.1 Literature Synthesis Quality:**

*   **Vector ID:** M11.1
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: Synthesis quality is high. The review effectively synthesizes a broad range of literature on collective animal behavior, highlighting common principles and mechanisms. It connects studies across different animal types (fish, birds, insects), demonstrating unifying themes in collective cognition. Key trends are identified, such as the importance of local interactions, feedback processes, distributed control, and speed-accuracy trade-offs. Contradictions are less emphasized, but the review does implicitly address variations by noting that "systems often have very different operational demands and selection pressures" (Box 3, Question 6), suggesting nuanced implementations of common principles. The synthesis is structured around key mechanisms and questions in collective behavior, drawing analogies to cognitive science and neural systems.
    *    Implicit/Explicit: Mixed
         *  Justification: The synthesis is explicitly demonstrated by the review's structure, its coverage of diverse examples, and its identification of common principles. The quality assessment, scoring it at 8, is based on an implicit evaluation of the breadth, depth, and coherence of the synthesis, judging it to be strong but not perfect (e.g., perhaps could have more explicitly addressed contradictions or limitations within the synthesized literature).

### **11.2 Gap Identification:**

*   **Vector ID:** M11.2
*   **Vector Type:** Score
    *   Score: [9]
    *   Justification: Gap identification is excellent. Box 3 ("Questions for future research") explicitly articulates key gaps in research relevant to understanding collective animal behavior and its cognitive aspects. These gaps are clearly articulated, specific, and highly relevant. Examples include:
        *   Understanding the role of selfishness vs. cooperation in collective behavior.
        *   Need for more kinematic data on real organism movements and interactions in groups.
        *   Prevalence and functional role of multistability in animal groups.
        *   Relationship between individual and collective cognition complexity.
        *   Mechanisms by which individuals "know what rules to adopt, and when."
        *   Differentiating function vs. mechanism across different animal group types.
        *   Trade-offs between speed, accuracy, and robustness.
        *   Spatial position and informational status in groups.
        *   Distinguishing explicit vs. emergent implementation of feedback processes.
        These questions are highly pertinent for future research and directly address limitations in current understanding of collective behavior in a cognitive science framework.
    *   Implicit/Explicit: Explicit
        *  Justification: Gap identification is explicitly presented in Box 3 as a series of research questions. The clarity, specificity, and relevance of these questions to the field are directly assessable from the explicit content of Box 3, justifying the high score.

### **11.3 Future Directions:**

*   **Vector ID:** M11.3
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: Future directions are well-proposed and actionable. Box 3 directly suggests concrete future research directions by outlining specific questions that need to be addressed. These directions are aligned with the review's framework (understanding mechanisms of collective cognition) and address the gaps identified in Box 3. For example, the call for more kinematic data directly addresses the gap in empirical data on animal movement and interaction. Investigating multistability, individual vs. collective cognition, rule adoption, and function vs. mechanism differences all propose specific avenues for future research.  Directions are generally well-aligned with the review's focus and provide a clear research agenda.
    *    Implicit/Explicit: Explicit
    *   Justification: Future research directions are explicitly presented as a set of questions in Box 3. Their actionability, relevance, and alignment with the review's framework are directly assessable, justifying the high score for future directions.

### **11.4 Review Paper CT-GIN Alignment Score**

*   **Vector ID:** M11.4
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: Overall alignment is strong but not perfect. The review significantly contributes to the CT-GIN framework by providing rich biological examples of collective systems that exhibit complex behaviors and functional parallels to cognitive processes. It covers breadth in CT-GIN aspects by discussing self-organization, emergent behaviors, feedback mechanisms, temporal dynamics, and drawing cognitive analogies. Depth of analysis is good, synthesizing diverse findings and providing mechanistic insights. Novelty from a CT-GIN perspective is moderate; the review is strong in biological synthesis but implicitly aligns with CT-GIN by highlighting distributed processing, feedback, and emergent order - key concepts within a CT-GIN framework, though not explicitly using CT-GIN terminology. Strength is the biological grounding and comprehensive review of animal collective cognition, weakness could be more explicit articulation within a formal CT-GIN framework and deeper analysis of the system from a purely CT-GIN lens (which is not the review's primary goal).
    *    Implicit/Explicit: Mixed
        *  Justification: The strong alignment is implicitly demonstrated by how well the review's content maps onto CT-GIN categories (self-organization, emergent behavior, cognition analogies, feedback). The score of 8 reflects a strong overall contribution but acknowledges that the review is not explicitly framed in CT-GIN terms, making the alignment somewhat implicit in interpretation rather than overtly stated by the paper itself.

## M12: Theoretical Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Theoretical")**

*   **Vector ID:** M12
*   **Vector Type:** Theory

### **12.1 Theoretical Rigor:**

*   **Vector ID:** M12.1
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification: Paper is a review, not a theoretical paper.
       * Implicit/Explicit: N/A
       *  Justification: N/A

### **12.2 Realization Potential:**

*   **Vector ID:** M12.2
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification: Paper is a review, not a theoretical paper.
    *   Implicit/Explicit: N/A
    *  Justification: N/A

### **12.3 Potential for Future CT-GIN Implementation Score**

* **Vector ID:** M12.3
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification: Paper is a review, not a theoretical paper.
    *    Implicit/Explicit: N/A
    *   Justification: N/A

## M13: Overall Assessment & Scoring

*   **Vector ID:** M13
*   **Vector Type:** Overall

### **13.1 CT-GIN Readiness Score:**

*   **Vector ID:** M13.1
*   **Vector Type:** Score
*   **Calculated Score:** [6.2]
*   **CT-GIN Readiness Summary Table:**

| CT-GIN Aspect                   | Strength (Yes/Partial/No) | Key Supporting Metrics (with units) | Limitations (Missing Metrics/Data Gaps)                                           | Improvement Areas (Future Research)                                          |
| :------------------------------ | :-----------------------: | :-----------------------------------| :------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| Energy Flow Efficiency          |        Medium          |  Qualitative assessment: Medium-High |  No quantitative energy efficiency metrics                                       |  Quantitative energy analysis of collective behaviors                            |
| Memory Fidelity                 |        Partial         |  Qualitative assessment: Medium, Dynamic |  Capacity, Readout Accuracy quantitatively unassessed                                 |  Quantify memory capacity, fidelity, and decay rates                             |
| Organizational Complexity       |          Yes          |  Emergent orders: Flocking, Trails, Rhythms |  Detailed quantification of complexity metrics (e.g., entropy, fractal dimension) |  Quantify organizational complexity with information-theoretic measures       |
| Embodied Computation            |          Yes          |  Primitives: Threshold, Integration, Competition |  Processing Power, Energy/Operation, Freq/Resp. Time, Bit-Depth not quantified |  Quantify computational performance metrics and energy costs                     |
| Temporal Integration            |          Yes          |  Timescales identified qualitatively & quantitatively |  Detailed analysis of temporal hierarchies and multi-timescale dynamics          |  Deepen analysis of temporal dynamics and their role in collective cognition  |
| Adaptive Plasticity             |          Yes          |  Mechanisms: Feedback, Pheromones, Quorum Tuning |  Quantitative measures of adaptation rate and plasticity range                   |  Quantify adaptation rates, plasticity, and learning curves                    |
| Functional Universality         |           No          |  Focused on animal group behaviors       |  Lacks discussion of broader applicability to diverse systems                  |  Explore universality of principles across biological and engineered systems |
| Cognitive Proximity            |        Partial         |  Cognitive Proximity Score: 4/10        |  Limited to functional analogies, lacks higher-level cognitive functions         |  Investigate higher-level cognitive functions in collective systems           |
| Design Scalability & Robustness |          Yes          |  Robustness Score: 8/10                 |  Scalability not explicitly addressed                                            |  Analyze scalability and robustness quantitatively                              |
| **Overall CT-GIN Readiness Score** |         **6.2**       |   |   |      |


### **13.2 Qualitative CT-GIN Assessment Conclusion:**

*   **Vector ID:** M13.2
*   **Vector Type:** Textual Summary
    *   Content: This review paper provides strong support for CT-GIN by richly illustrating collective cognition in biological systems, specifically animal groups. Key Strengths include detailed descriptions of self-organization and emergent behaviors in flocks, ant colonies, and fish schools, emphasizing the role of local interactions, feedback, and distributed computation. The review highlights functional parallels to cognitive processes, particularly in decision-making and information processing, achieving a moderate Cognitive Proximity score, indicating a move towards goal-directed and model-based cognition at the collective level. Robustness due to distributed control is another key strength. Key Limitations are the qualitative nature of much of the analysis, with limited quantifiable metrics for memory, energy efficiency, computational power, and long-term memory. While temporal dynamics are discussed, deep quantification is missing. Functional Universality is not addressed. Overall Assessment: The review provides a strong foundation for understanding biological collective intelligence through a CT-GIN lens, particularly in demonstrating self-organization, embodied computation, and cognitive analogies but would benefit from future research quantitatively assessing key CT-GIN metrics, and exploring scalability and broader universality to move closer to a comprehensive CT-GIN framework for material intelligence.

### **13.3 CT-GIN Refinement Directions:**

*   **Vector ID:** M13.3
*   **Vector Type:** Recommendations
    *   * Quantify key CT-GIN metrics:*  Future research should focus on developing and applying quantitative metrics to assess energy efficiency, memory capacity/fidelity, computational power, organizational complexity, and adaptation rates in collective biological systems.
    *   * Deepen temporal dynamics analysis:*  Investigate multi-timescale dynamics and temporal hierarchies in collective behaviors, employing time-series analysis and information dynamic measures.
    *   * Explore scalability and robustness quantitatively:*  Develop methods to quantitatively assess scalability of collective behaviors and robustness to various perturbations (noise, component failure) in both models and experiments.
    *   * Investigate higher-level cognitive functions:*  Future studies should explore if collective systems can exhibit higher-level cognitive functions (beyond Level 4), such as contextual/relational cognition, or even rudiments of social cognition, perhaps through more complex interaction rules or environmental contexts and how these would map to CT-GIN framework.
    *   * Develop explicit CT-GIN models of collective behavior:*  Future work should aim to develop theoretical CT-GIN models explicitly capturing self-organization, emergent computation, and cognitive mapping in collective systems, going beyond functional analogies to formal CT-GIN representations.
    *   * Broaden scope to non-biological systems:* Investigate the universality of the identified CT-GIN principles by applying them to engineered and synthetic systems, as well as other complex systems beyond animal groups, to test the framework's generalizability.

## M14: CT-GIN Knowledge Graph

*   **Vector ID:** M14
*   **Vector Type:** Visualization

### **14.1. CT-GIN Knowledge Graph:**
* **Content:**
[__Insert a schematic diagram of the CT-GIN Knowledge Graph. Use distinct shapes/colors for different CT-GIN node types (Energy, Memory, Configuration, Temporal, Behavior, Cognitive, Reliability). Use directed edges to represent relationships, labeled with CT-GIN edge types (Transduction, Transition, Adjunction, Coupling, Feedback, Temporal Evolution, Cognitive Mapping). Annotate nodes and edges with key attributes and parameters (with units!) extracted from the previous sections.__]

## M15: Relationship Vectors
*   **Vector ID:** M15
*   **Vector Type:** Relationships
*   Relationships:
        | Source Vector ID | Target Vector ID | Relationship Type |
        | ------------- | ------------- | ----------------- |
        | N/A     | N/A     | N/A     |

## M16: CT-GIN Template Self-Improvement Insights

*   **Vector ID:** M16
*   **Vector Type:** Feedback

### **Template Feedback:**

*    **Vector ID:** M16.1
*   **Vector Type:** Text
Provide specific, actionable feedback on the *CT-GIN template itself*, based on this analysis:
    *   **Missing Probes:** No significant missing probes identified for this review paper. The template is comprehensive for capturing different aspects of material intelligence even in a biological review context.
    *   **Unclear Definitions:** Definitions were generally clear. "Active Inference" definition could benefit from brief, more operational sub-points within the description in the template itself for clarity. "Self-Organization" distinction between designed and emergent order is helpful.
    *   **Unclear Node/Edge Representations:** Node/edge representations guidance is sufficient for a review. For experimental papers, clearer examples of mapping specific experimental components to nodes/edges would be beneficial.
    *   **Scoring Difficulties:**  Cognitive Proximity scoring and mapping to the Cognizance Scale remain somewhat subjective. More granular descriptors for each level of the scale, with specific behavioral/functional examples, could improve inter-rater reliability.
    *   **Data Extraction/Output Mapping:** Data extraction was relatively straightforward for a review paper. For papers with complex tables and figures, perhaps a section prompting to link specific tables/figures to the extracted parameters could be beneficial.
    *   **Overall Usability:** Template is reasonably usable and structured. The modular design is effective. The conditional sections (M11, M12) are well-implemented to maintain template conciseness for different paper types.
    * **Specific Suggestions:**
        * Add operational sub-points within "Active Inference" definition in the template for enhanced clarity.
        * Enhance Cognitive Proximity Scale descriptions with more granular descriptors and behavioral/functional examples for each level.
        * For experimental paper analysis, include examples demonstrating how to map specific experimental components to CT-GIN nodes/edges within the template instructions.
        * Consider adding a section prompting link specific tables/figures from the analyzed paper to extracted parameters, especially for papers with complex data presentations.
```
