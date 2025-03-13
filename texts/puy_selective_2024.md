# Selective social interactions and speed-induced leadership in schooling fish:

__Paper Type:__ Hybrid

## M1: System Overview & Implementation
*   **Vector ID:** M1
*   **Vector Type:** Overview

### **1.1 System Description**

*   **Vector ID:** M1.1
*   **Vector Type:** Description
    *   Content: The system under study is a group of schooling fish, specifically black neon tetras (Hyphessobrycon herbertaxelrodi), observed in a controlled experimental tank. The system is analyzed to understand the social interactions, particularly alignment forces and leadership dynamics, based on the relative speeds of neighboring fish. The components include the fish, experimental tank, tracking system, and agent-based model simulations. The purpose is to investigate the mechanisms of collective motion and coordination in animal groups, focusing on the role of selective attention and speed-induced leadership. The system uses force map techniques, validated with agent-based models, to analyze experimental data and infer interaction rules among individuals within the school.
    *   CT-GIN Mapping: `SystemNode` attributes: `systemType: Biological & Computational`, `domain: Animal Behavior`, `mechanism: Force Map Analysis, Agent-Based Modeling`, `components: Schooling Fish, Experimental Tank, Agent-Based Model`, `purpose: Understand collective motion and social interactions in animal groups, investigate speed-induced leadership`
    *   Implicit/Explicit: Mixed
        *  Justification: The system components, purpose, and high-level description are explicit in the introduction and results sections. The operational details, such as specific force map techniques and agent-based model parameters, are described explicitly in the methods and results. The combination of experimental and computational approaches is also explicit, leading to a 'Mixed' categorization as it combines direct descriptions and implied methodologies used to achieve the stated purpose.

### **1.2 Implementation Clarity**

*   **Vector ID:** M1.2
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The implementation is relatively clear. The paper provides details on the experimental setup (tank dimensions, fish species, tracking methods) and the agent-based model (force equations, interaction types, parameters in methods section and table). Force map analysis is explained with equations and figures. However, some aspects, such as the exact parameters used for the selective interactions model and the precise numerical integration methods, could be more detailed for perfect reproducibility. Figure and video supplements enhance the clarity, but some fine-grained experimental and simulation details are left at a level that assumes some background knowledge in the field.
    *   Implicit/Explicit: Mixed
        * Justification: Clarity about the overall approach and key methodologies is explicit. However, some finer implementation details necessary for full replication require implicit understanding based on common practices in agent-based modeling and data analysis in behavioral biology, leading to a 'Mixed' categorization.

### **1.3 Key Parameters**

*   **Vector ID:** M1.3
*   **Vector Type:** ParameterTable
    *   Table:
        | Parameter Name | Value | Units | Source (Fig/Table/Section) | Implicit/Explicit | Data Reliability (High/Medium/Low) | Derivation Method (if Implicit) |
        | :------------- | :---: | :---: | :-----------------------: | :-----------------: | :-----------------------------: | :-------------------------------: |
        | Number of Fish (N) | 39 | individuals | Methods (Experimental data) | Explicit | High | N/A |
        | Tank Side Length | 100 | cm | Methods (Experimental data) | Explicit | High | N/A |
        | Water Depth | 5 | cm | Methods (Experimental data) | Explicit | High | N/A |
        | Frame Rate | 50 | fps | Methods (Experimental data) | Explicit | High | N/A |
        | Time step (∆t) | 0.02 | s | Methods (Standard model) | Explicit | Medium | Based on frame rate equivalence |

    *   **Note:** List *up to 5* key parameters characterizing the system's *implementation*.  Provide values and units if possible. If a parameter is not explicitly stated but derived/inferred, clearly state the derivation method. *Always* include units if applicable. If a value is not applicable, write "N/A".  Data Reliability: High = Directly measured, Medium = Derived from measurements/simulations, Low = Estimated/Inferred.

## M2: Energy Flow
*   **Vector ID:** M2
*   **Vector Type:** Energy

### **2.1 Energy Input**

*   **Vector ID:** M2.1
*   **Vector Type:** Input
    *   Content: The primary energy source for the experimental system is metabolic energy from food consumed by the fish, which fuels their movement and social interactions within the tank. For the agent-based model, the energy input is computational energy required to run the simulations and calculate forces, accelerations, and positions of agents over time.
    *   Value: N/A
    *   Units: N/A
    *   CT-GIN Mapping: `EnergyInputNode`: attributes - `source: Metabolic (fish), Computational (model)`, `type: Chemical (food), Electrical (computation)`
    *   Implicit/Explicit: Implicit
        *  Justification: Energy input is not explicitly quantified or detailed in terms of Joules or Watts, but it is implicitly understood that fish require metabolic energy and simulations require computational energy to run. The types of energy are inferred from the nature of biological systems and computational processes.

### **2.2 Energy Transduction**

*   **Vector ID:** M2.2
*   **Vector Type:** Transduction
    *   Content: In the experimental system, chemical energy from food is transduced into kinetic energy through the fish's biological processes and muscular contractions, enabling locomotion and social interactions. Light energy is used for observation and tracking, being transduced by camera sensors into electrical signals and digital data. In the agent-based model, computational (electrical) energy is used to perform calculations based on predefined force equations, effectively transducing algorithmic instructions into simulated motion and interactions of agents within the model environment.
    *   CT-GIN Mapping: `EnergyTransductionEdge`: attributes - `mechanism: Metabolic processes, Muscular contraction, Algorithmic calculation`, `from_node: Chemical Energy (food), Computational Energy`, `to_node: Kinetic Energy (fish motion), Simulated motion (agents), Digital Data (tracking)`
    *   Implicit/Explicit: Implicit
        *  Justification: The energy transduction processes are not detailed at a molecular or physiological level, but they are implicitly described by referring to general biological processes (metabolic energy to kinetic energy for fish) and computational processes (electrical energy to simulated motion in the model). The physical mechanisms are generally understood in the context of biology and computational physics, but not explicitly detailed in the publication text.

### **2.3 Energy Efficiency**

*   **Vector ID:** M2.3
*   **Vector Type:** Score
    *   Score: [3]
    *   Justification/Metrics: Energy efficiency is not explicitly quantified for either the experimental or computational systems. Biological systems, such as fish schools, are generally not optimized for energy efficiency in the engineering sense; much of the metabolic energy is dissipated as heat and used for processes other than directed motion and social interaction. Agent-based models, while computationally efficient for simulation purposes, still dissipate electrical energy as heat during computation, and their efficiency is relative to the specific computational setup and algorithm, not addressed in detail in the paper. Qualitatively, both systems can be considered 'Low' efficiency in terms of converting input energy into the specific output of coordinated motion and information processing studied in this paper.
    *   CT-GIN Mapping: Attribute of relevant `EnergyTransductionEdge`s: `efficiency_score: 3`, `efficiency_qualitative: Low`
    *   Implicit/Explicit: Implicit
      *  Justification: Energy efficiency is not directly measured or calculated, it's a qualitative assessment based on general understanding that biological and standard computational systems are not perfectly efficient. The 'Low' score is inferred from typical efficiencies of biological locomotion and computational processes, which are not explicitly stated but commonly known.

### **2.4 Energy Dissipation**

*   **Vector ID:** M2.4
*   **Vector Type:** Dissipation
    *   Content: In the experimental fish system, energy is dissipated primarily as heat due to metabolic processes and friction between the fish and water as they move. There's also energy dissipation in the tracking system through heat generated by electronic components and light emitted from the illumination source (if any, although not specified). In the agent-based model simulation, energy is dissipated as heat in the computer hardware due to electrical resistance during computation. Quantification of dissipation is not provided in the paper. Qualitatively, dissipation is expected to be significant in both systems, typical for biological and computational processes involving motion and calculation.
    *   CT-GIN Mapping: `EnergyDissipationNode`: attributes - `mechanism: Metabolic heat, Friction (fish-water), Electrical resistance (computation)`, `type: Thermal, Mechanical, Electrical`; `EnergyDissipationEdge`: attributes - `from_node: Kinetic Energy (fish, agents), Computational Energy`, `to_node: Heat Energy`
    *    Implicit/Explicit: Implicit
        *  Justification: Dissipation mechanisms are identified based on general physical principles (metabolic heat, friction, electrical resistance) applicable to the described systems but are not explicitly quantified or measured in the publication. Their presence and qualitative nature are inferred from the nature of biological and computational systems.

## M3: Memory
*   **Vector ID:** M3
*   **Vector Type:** Memory

### **3.1 Memory Presence:**

*   **Vector ID:** M3.1
*   **Vector Type:** Binary
    *   Content: [No]
    *   Justification: While schooling behavior in general may involve forms of social or collective memory over longer timescales (e.g., group-level behavioral traditions or spatial knowledge), the paper does not investigate or explicitly demonstrate memory in the sense of persistent changes in individual fish state that influences *future* behavior *beyond* the immediate timescale of social interactions studied. The observed "selective attention" mechanism is presented as a real-time response to current neighbor speeds, not a modification of behavior based on past experiences stored in individual fish or the school as a whole within the context and timescale of these specific experiments. Thus, 'memory' as defined in the template (persistent state change influencing future behavior beyond stimulus) is not evident in the analyzed system within the scope of this paper.
    *    Implicit/Explicit: Implicit
        * Justification: The absence of explicit discussion or experimental evidence for memory functions, combined with the focus on real-time interactions and force map analyses, implicitly suggests a lack of memory component as defined in the template, within the investigated system's description by this paper.

## M4: Self-Organization and Emergent Order
*   **Vector ID:** M4
*   **Vector Type:** Self-Organization

### **4.1 Self-Organization Presence:**

*   **Vector ID:** M4.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: Schooling behavior itself is a classic example of self-organization. The paper describes how coherent collective motion (polarized movement, swarming, milling) emerges from local interactions among individual fish, based on attraction, repulsion, and alignment forces.  The global order of the fish school (its shape, directionality, and collective movements) is not dictated by a central controller or a pre-designed structure but arises spontaneously from the decentralized interaction rules operating at the individual level and between neighboring fish. The force map analysis and agent-based modeling are used to understand and characterize these local interaction rules that lead to emergent schooling patterns at the global scale.
    *   Implicit/Explicit: Explicit
        *  Justification: The paper explicitly discusses "emergent" leadership and collective motion arising from individual interactions, which is a direct indication of self-organization. Terms like "emergent leadership" and descriptions of collective patterns resulting from local rules clearly point to self-organization as a core feature of schooling behavior analyzed.

### **4.2 Local Interaction Rules:**

*   **Vector ID:** M4.2
*   **Vector Type:** Rules
    *   Content: The local interaction rules are primarily based on effective social forces: attraction, repulsion, and alignment, alongside individual forces.
        * Attraction-Repulsion: As described by equation (1), the force between individual i and neighbor j is given by F⃗att-rep = −k(d -d ) (⃗x -⃗x )/d , where d is the distance between fish i and j, d is the equilibrium distance, and k is a constant that varies ij ij 0 i j ij 0
          ij
          depending on whether d is less than or greater than d (k for repulsion if d < d and k for attraction if d > d ). This rule causes fish to be attracted to and repelled from neighbors based on distance maintaining a preferred inter-individual distance.
        * Alignment: As given by equation (2), the alignment force is F⃗alig = µ(⃗v −⃗v ), where µ is the alignment constant, and ⃗v and ⃗v are velocities of individuals i and j respectively. This rule causes fish to align their velocities with their neighbors.
        * Selective Interaction: Individuals interact primarily with neighbors moving at faster speeds, ignoring slower ones. In the selective interactions model, weights in social interactions are calculated as in the standard model but only considering faster neighbors. This imposes a condition to the local interaction based on relative speed.
        * Individual Forces: Friction-propulsion force F⃗fric-prop = (v -v )/τ v̂ , where v is preferred speed, τ is speed relaxation time, and v̂ is the direction of motion. Noise force F⃗noise = σ ξ (t)v̂ +σ ξ (t)φ̂ , where σ , σ are noise constants and ξ (t), ξ (t) are independent Gaussian white noise processes. These rules drive individual motion and introduce stochasticity.
    *   CT-GIN Mapping: `AdjunctionEdge` description (local side): `type: Social Interaction`, `subtype: Attraction-Repulsion, Alignment, Selective Attention`, `rules: Equations (1) & (2), Speed-based selection criteria`, `parameters: k_rep, k_att, d_0, µ, v_0, τ, σ_v, σ_φ`. These define the "LocalInteraction" category of edges.
    * **Implicit/Explicit**: Explicit
        *  Justification: The local interaction rules are explicitly described using equations and clear descriptions in the Methods and Results sections of the paper. Equations (1) and (2) are directly provided for attraction-repulsion and alignment forces. The selective interaction mechanism and individual forces are also described in detail within the main text and Methods.

### **4.2.1 Local Interaction Parameters:**

* **Vector ID:** M4.2.1
* **Vector Type:** Table
*   Table:
    | Rule ID | Description | Parameter Name | Parameter Value Range | Units | Data Source | Implicit/Explicit | Justification |
    | :------ | :---------- | :------------- | :---------- | :---: | :----------: | :----------------: | :------------: |
    | AR-1 | Repulsion constant | k_rep | 12.5 | s^-2 | Table I | Explicit | Value explicitly stated in table |
    | AR-2 | Attraction constant | k_att | 5 | s^-2 | Table I | Explicit | Value explicitly stated in table |
    | AR-3 | Equilibrium distance | d_0 | 5.8 | cm | Table I | Explicit | Value explicitly stated in table |
    | AL-1 | Alignment constant | µ | 1.5 | s^-1 | Table I | Explicit | Value explicitly stated in table |
    | IF-1 | Preferred speed | v_0 | 11 | cm/s | Table I | Explicit | Value explicitly stated in table |
### **4.3 Global Order:**

*   **Vector ID:** M4.3
*   **Vector Type:** Order
    *   Content: The global order that emerges in the schooling fish system includes:
        * Polarized movement: Individuals move globally in the same direction. This represents a high degree of orientational order and coordination in the school.
        * Swarming: Individuals aggregate in a cohesive group but move in random directions. This indicates high spatial cohesion but low orientational order.
        * Milling: Individuals rotate around a common core. This represents a circular global pattern of movement, indicating a specific type of collective motion.
    These patterns are mentioned in the context of models of collective motion and implicitly observed in experiments as schooling is described as polarized and compact. The paper focuses on polarized movement as characteristic in the experiments with black neon tetra.
    *   CT-GIN Mapping: `ConfigurationalNode`: `orderType: Polarized Movement, Swarming, Milling`, `description: Collective motion patterns in schooling fish`, `parameters: Polarization (ϕ), Nearest neighbor distance, Convex hull area`.
    * **Implicit/Explicit**: Mixed
        *  Justification: The descriptions of polarized movement, swarming, and milling are explicitly stated as typical features of collective motion in the introduction. While polarized movement is implicitly the dominant global order observed in the *experiments* with black neon tetra (described as forming polarized, compact schools), the paper uses these terms generally in the context of collective motion models and experimental analysis. Thus it's Mixed because the types are explicitly defined, but their prominence in the *specific experimental system* is more implicitly suggested through descriptions of schooling behavior.

### **4.4 Predictability of Global Order:**

*   **Vector ID:** M4.4
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The emergence of global order in the schooling fish system (polarized motion, swarming, milling) is moderately predictable given the local interaction rules. Agent-based models based on attraction, repulsion, and alignment are shown to reproduce these types of emergent collective behaviors qualitatively, indicating a degree of predictability.  The paper shows force maps derived from experimental data are consistent with these interaction rules. However, the exact type of global order that emerges (e.g., precise polarization level, swarm density, milling radius) and the transitions between these states may be less precisely predictable due to the stochastic nature of individual behavior and environmental influences. Figure 4 shows probability density functions of polarization and other order parameters, indicating variability and thus not perfect predictability, but a statistically describable distribution of order states.
    * **Implicit/Explicit**: Mixed
    *  Justification: The predictability of *types* of global order (polarized movement, swarming, milling) from local rules is implicitly validated by the model's ability to reproduce these patterns. However, the degree of predictability of *specific quantitative metrics* of global order (polarization value, size of group) is more mixed.  The paper uses PDFs to describe order parameters, suggesting statistical predictability but not perfect determinism. The score reflects this mixed nature - predictability is present but not absolute or perfectly quantified in all aspects.
    *   CT-GIN Mapping: Contributes to the `AdjunctionEdge` weight: `predictability_score: 7`, `predictability_justification: Model reproduces qualitative order, statistical predictability of quantitative metrics, stochasticity limits precise prediction.`

### **4.5. Local Interaction Rules (for Self-Organization)**
* **Vector ID:** M4.5
* **Vector Type:** Table
*   Table:
| Rule ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Source |
| :------ | :---------- | :-------- | :---------- | :---------- | :----------------: | :------------: | :-----: |
| SA-1 | Selective Alignment with faster neighbours | Speed Difference Threshold |  v_i < v_NN | cm/s | Explicit | Defined as selective interaction based on speed. | Results, Selective Interactions Model |
| AR-Weights | Attraction-Repulsion Weighting | Inverse Distance | w_ij = 1/d_ij | cm^-1 | Explicit | Weights are based on inverse metric distance. | Methods, Standard Model |

### **4.6. Globally Emergent Order and Order Parameters**
* **Vector ID:** M4.6
* **Vector Type:** Table
*   Table:
| Property ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Protocol | Source |
| :---------- | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :------: | :-----: |
| POL-1 | Polarization | ϕ | [0, 1] | Dimensionless | Explicit | Ranges from disorder to perfect order. | Fig 4a, Results | Figure 4a |
| NND-1 | Nearest Neighbor Distance | <d_NN> | Range in PDF | cm | Explicit | Measure of group cohesiveness. | Fig 4b, Results | Figure 4b |
| CH-Area-1 | Convex Hull Area (normalized) | s | Range in PDF | cm^2 | Explicit | Measure of group extension. | Fig 4c, Results | Figure 4c |
| CDT-1 | Contact Duration Time (Voronoi) | t_V | Range in PDF | s | Explicit | Measure of neighbour shuffling. | Fig 4d, Results | Figure 4d |

### **4.7 Yoneda Embedding and Local-to-Global Mapping Fidelity**

*   **Vector ID:** M4.7
*   **Vector Type:** Table
*   Table:
    | Link Type | Description | Predictability | Yoneda Score | Metrics | Implicit/Explicit | Justification | Source |
    | :-------- | :---------- | :------------- | :----------- | :------ | :----------------: | :------------: | :-----: |
    | Local Rules -> Global Order | Mapping from interaction forces to schooling patterns | Moderate | 6 | Qualitative force map agreement, statistical similarity of order parameter PDFs | Mixed | Force maps qualitatively recover expected forces, model PDFs partially match experimental PDFs; Precise quantitative prediction is limited. | Results, Figure 1,2,3,4 |
    *   **Yoneda Embedding Fulfillment Score [0-10]:** [**Rubric for Yoneda Score:**
        * 0-2: No discernible link between local rules and global order; global order appears random or unrelated to local interactions.
        * 3-4: Weak or inconsistent link; some qualitative resemblance but frequent deviations; low predictability.
        * 5-6: Moderate link; qualitative resemblance generally holds; statistical trends are captured but significant individual variation; medium predictability.
        * 7-8: Strong link; good qualitative and statistical agreement; model accurately captures key features of global order; high predictability for statistical averages.
        * 9-10: Very strong/near perfect link; precise quantitative prediction of global order from local rules; model accurately reproduces almost all aspects of emergent behavior; exceptional predictability.
        **Specific Examples for different score levels:**
        * Score 2: Model predicts completely random motion regardless of interaction rules, experimental data shows schooling – major mismatch.
        * Score 5: Model produces swarming, experiments show polarized motion – qualitative patterns somewhat similar but mismatch in specific type of order; statistical measures partially overlap.
        * Score 8: Model accurately reproduces polarized schooling, velocity distributions, and group size distributions observed in experiment – strong qualitative and quantitative agreement for key metrics.]
    *   **Metrics:**  [**Metrics used for predictability and Yoneda embedding fulfillment:**
        * Qualitative visual comparison of force maps (experimental vs. model).
        * Comparison of Probability Density Functions (PDFs) for order parameters (Polarization ϕ, Nearest Neighbor Distance <d_NN>, Convex Hull Area s, Voronoi Contact Duration t_V) between model and experimental data (Figure 4).
        * Visual assessment of simulated collective motion patterns (polarized, swarming, milling) in videos (Supplementary Videos 2, 3, 4) compared to observed schooling in experimental video (Supplementary Video 1 and 5).]
    *   **Justification:** The Yoneda score of 6 indicates a moderate fulfillment. The force maps derived from the agent-based models qualitatively resemble those from the experimental data (Figure 1 vs. Figure 2, Figure 3 vs. Figure 2), showing that local interaction rules capture the essential features of observed forces.  The PDFs of order parameters for the selective interactions model show better qualitative agreement with experimental data PDFs compared to the standard model (Figure 4), suggesting some level of statistical predictability. However, the models are simplifications and do not achieve precise quantitative prediction of all aspects of schooling dynamics. The "selective interactions" model improves the match, but there are still deviations, and the predictability is primarily statistical (describing distributions) rather than deterministic for individual fish movements or exact school configurations. Thus, a score of 6 reflects moderate, but not perfect, fidelity in the local-to-global mapping.

## M5: Computation
*   **Vector ID:** M5
*   **Vector Type:** Computation

### **5.1 Embodied Computation Presence:**

*   **Vector ID:** M5.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: In the biological system, the brain of each individual fish performs embodied computation.  Fish are not simply reacting passively to stimuli, but actively processing sensory information (visual, lateral line, etc.) from their environment and neighbors, and making 'decisions' about their movement direction and speed based on these inputs according to some internal 'ruleset'. This processing is intrinsic to their neural and physical embodiment—it's not performed by an external controller.  In the agent-based model, the computational process is explicitly embodied within the simulation code itself, which calculates forces, updates positions and velocities according to defined interaction rules, representing a computational instantiation of embodied social behavior in silico.
    *    Implicit/Explicit: Explicit
        *  Justification: The paper explicitly discusses "individual decision-making processes" and "selective attention mechanisms" of fish, indicating an implicit recognition of computation occurring within the fish to drive behavior and social interactions. Agent-based modeling itself is an explicit computational approach to study embodied behavior.

### **5.2 Computation Type:**

*   **Vector ID:** M5.2
*   **Vector Type:** Classification
    *   Content: [Analog]
    *   CT-GIN Mapping: `ComputationNode` type: `computationType: Analog`
    *    Implicit/Explicit: Implicit
    *    Justification: Biological computation in fish brains is understood to be primarily analog and distributed, involving continuous signals and graded responses in neural networks, rather than digital logic.  The agent-based model, though simulated on digital computers, is based on continuous force equations and velocity updates, reflecting analog-style computation at the level of interaction rules. The models are not described in terms of logical gates or discrete digital operations, which suggests an analog operational mode.

### **5.3 Computational Primitive:**

*   **Vector ID:** M5.3
*   **Vector Type:** Function
    *   Content: The most basic computational primitives embodied in the system are:
        * Vector Summation:  Each fish effectively sums the force vectors from its neighbors (attraction, repulsion, alignment) and its individual propulsion/friction and noise forces to determine its acceleration. This is a continuous vector summation.
        * Weighted Averaging (Implicit in Voronoi): Forces from Voronoi neighbors are averaged with weights given by inverse distance, effectively prioritizing closer neighbors. This implies a form of weighted averaging as a computational primitive in integrating social cues. The selective interactions model further modifies this by effectively setting weights to zero for slower neighbors – a form of conditional filtering.
        * Thresholding (Implicit Selective Attention): The "selective attention mechanism" acts as a threshold function – processing information from faster neighbors while ignoring/attenuating input from slower neighbors. This resembles a threshold-based computation where relative speed acts as a gating or selection signal for social information.
    *   **Sub-Type (if applicable):** Vector Summation; Weighted Averaging; Thresholding (Selective Attention)
    *   CT-GIN Mapping: Defines the primary function of the `ComputationNode`: `primitiveFunction: Vector Summation, Weighted Averaging, Thresholding`, `functionSubtype: N/A, Distance-Weighted, Speed-Threshold`.
    *   Implicit/Explicit: Mixed
    * Justification: Vector summation and weighted averaging are implicitly represented in the force equations and Voronoi weighting scheme, reflecting continuous analog operations. Thresholding, via "selective attention," is more explicitly proposed as a mechanism. The computational primitives are inferred from the model equations and the described behavioral mechanism rather than being explicitly listed as computational primitives in the paper.

### **5.4 Embodied Computational Units**
* **Vector ID:** M5.4
* **Vector Type:** Table
*   Table:
| Unit ID | Description | Processing Power | Energy/Operation | Freq/Resp. Time | Bit-Depth | Data Source | Implicit/Explicit | Justification |
| :------ | :---------- | :--------------- | :--------------- | :--------------: | :-------: | :----------: |:-----------------:| :-----------------:|
| Fish-Brain-Unit | Individual fish brain | N/A | N/A | N/A | Analog (continuous values) | Implicit (biological system) | Implicit | Processing power, energy, response time, and bit-depth are not quantified for individual fish brains in the paper. Bit-depth is qualitatively assessed as analog due to the continuous nature of biological signals. |
| Agent-Model-Unit | Computational agent in model | Operations per timestep dependent on hardware | Computational energy per timestep dependent on hardware | ~50 Hz (Simulation timestep) | Floating point (simulation variables) | Implicit (computational model) | Implicit | Processing power and energy per operation are hardware-dependent and not specified. Frequency/response time is set by the simulation timestep (corresponding to experimental frame rate). Bit-depth reflects floating point precision of simulation variables, typical in computational physics models. |

## M6: Temporal Dynamics
*   **Vector ID:** M6
*   **Vector Type:** Temporal

### **6.1 Timescales:**

*   **Vector ID:** M6.1
*   **Vector Type:** ParameterTable
    *   Table:
        | Timescale Description | Value | Units | Source | Implicit/Explicit | Justification |
        | :-------------------- | :---: | :---: | :----: | :----------------: | :------------: |
        | Frame interval (data sampling) | 0.02 | s | Methods (Experimental data & model) | Explicit | Inverse of frame rate (50 fps) |
        | Speed relaxation time (model) | 1.6 | s | Table I (Standard Model) | Explicit | Parameter value in model definition |
        | Reaction time (leader-follower) | ~0.2 | s | Figure 6, Results (Leadership and Alignment)| Implicit | Delay at peak correlation in leader-follower analysis |

    *   **Note:** Identify and quantify the *relevant timescales* of the system's dynamics (e.g., response time, process duration, oscillation period, memory decay, adaptation/learning timescale, self-assembly timescale). Use consistent units (e.g., seconds, milliseconds) for comparability.

### **6.2 Active Inference:**

*   **Vector ID:** M6.2
*   **Vector Type:** Assessment
    *   Content: [Partial] *Active Inference*: The system partially exhibits aspects of active inference.
        * Prediction: Fish implicitly 'predict' the near-future positions and velocities of their neighbors to maintain school cohesion and alignment. This is not an explicit, model-based prediction but inherently embedded in their reactive social behaviors. Force maps are a method to retroactively infer these implicit predictions through observed accelerations.
        * Action Selection: Fish select actions (adjustments to speed and direction) to minimize deviations from desired social proximities and alignments within the school. The selective attention mechanism suggests a form of action selection based on neighbor speed.
        * Internal Models: It's unclear if fish possess explicit internal models of their environment and social dynamics as tested in this paper. The model uses simple force-based rules which are computationally tractable but may not fully represent the complexity of fish cognition or internal models if any exist. The paper doesn't provide direct evidence for or against detailed internal models in fish, focusing more on effective interaction forces.

    *   Justification: The system shows reactive and adaptive behavior consistent with *some* aspects of active inference—minimizing discrepancies in movement relative to neighbors. However, the paper doesn't provide evidence for explicit internal models or sophisticated predictive processing in the active inference sense. The "partial" assessment reflects reactive behavior suggestive of error minimization but lacking demonstrated model-based predictive processing.
    *   Implicit/Explicit: Mixed
        *  Justification: The paper's interpretation of behavior in terms of "selective attention" and force-based interactions implicitly relates to minimizing deviations from a desired social state (cohesion, alignment), characteristic of active inference. However, explicit validation in terms of prediction error minimization, internal model architectures, or surprise metrics, as typically used in active inference frameworks, is absent. The "Partial" classification indicates a mix of suggestive reactive features and the absence of explicit active inference validation.
    *   **If Yes/Partial, provide examples of testable CT-GIN metrics that *could* be used to quantify active inference:** [Testable CT-GIN metrics for active inference quantification:
        * Prediction Error (Velocity Deviation): Measure the deviation between a fish's current velocity and the average velocity of its faster neighbors (or predicted velocity based on a short-term extrapolation). Reduction in this deviation over time could indicate error minimization.
        * Anticipation Timescale (Correlation Analysis): Examine time-delayed correlations between changes in a neighbor’s velocity and the focal fish's subsequent velocity changes. A positive anticipation timescale (focal fish reacting *before* neighbor changes are fully manifested) could suggest predictive behavior.
        * Model Complexity (Force Map Structure): Analyze the complexity of the inferred force maps. Simpler, more structured force maps that still effectively capture observed behavior might suggest more efficient or model-based prediction strategies compared to highly complex or noisy force maps.
        * Experimental Setup: Introduce perturbations in the school (e.g., sudden changes in flow, simulated predator approach) and measure how quickly and effectively fish adapt their behavior to minimize "surprise" or maintain school cohesion under these disturbances, which could be quantified as increased alignment or reduced inter-individual distances post-perturbation compared to pre-perturbation baseline.]

## M7: Adaptation
*   **Vector ID:** M7
*   **Vector Type:** Adaptation

### **7.1 Adaptive Plasticity Presence:**

*   **Vector ID:** M7.1
*   **Vector Type:** Binary
    *   Content: [No]
    *   Justification: The paper does not present evidence for adaptive plasticity as defined—persistent changes in behavior or internal structure in response to *experience* that improves performance *over time*. The described "selective attention" is a fixed behavioral rule or mechanism applied consistently throughout the observation period. While fish behavior is inherently plastic over longer ontogenetic or evolutionary timescales, within the timeframe of these experiments and the model analysis, there's no demonstrated learning or adaptive modification of interaction rules based on experience or feedback. The system reacts instantaneously to neighbor speeds, and while context-dependent, it's not shown to *adapt* its responsiveness over successive interactions or changing environmental conditions in a way that would represent adaptive plasticity.
    *    Implicit/Explicit: Implicit
        * Justification:  The paper focuses on *static* interaction rules (attraction, repulsion, alignment, selective attention) and their real-time effects on schooling dynamics.  The absence of discussion or experiments relating to changes in these rules or fish behavior *over time* due to experience or feedback, implicitly indicates a lack of adaptive plasticity as a studied feature in this work.

## M8: Emergent Behaviors
*   **Vector ID:** M8
*   **Vector Type:** Behavior

### **8.1 Behavior Description:**

*   **Vector ID:** M8.1
*   **Vector Type:** Description
    *   Content: The main functional behaviors of the schooling fish system are:
        * Coherent Collective Motion: Emergence of polarized movement, swarming, and milling patterns from individual fish interactions. This is the foundational behavior observed.
        * Speed-Based Selective Alignment: Individuals preferentially align with faster neighbors and effectively anti-align (ignore) slower neighbors. This is the key emergent behavior discovered and analyzed using force maps.
        * Speed-Induced Leadership: Faster individuals tend to act as leaders, influencing the direction of slower followers. Leadership dynamically emerges based on instantaneous relative speeds.
        * Force Map Signatures: Observation of characteristic force maps—attraction-repulsion based on relative position, and alignment/anti-alignment based on relative velocity and selective interactions. These are the key observable behavioral signatures used to validate the emergent interaction rules.
    *   CT-GIN Mapping: `BehaviorArchetypeNode`. Specify the type of behavior: `behaviorType: Collective Motion, Selective Alignment, Leadership`, `behaviorSubtype: Schooling, Polarized Movement, Swarming, Milling, Speed-Based, Dynamic Leadership, Force Map Signature`.
    *    Implicit/Explicit: Explicit
       *  Justification: These behaviors are explicitly described in the Results and Discussion sections as central findings of the paper.  Terms like "collective motion," "selective alignment," "speed-induced leadership," and "force maps" are used directly to characterize the observed and modeled behaviors.

### **8.2 Behavior Robustness:**

*   **Vector ID:** M8.2
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: Schooling behavior, in general, and as observed in this study, shows moderate robustness. Fish schools persist and maintain coherence under various conditions, including some level of noise and individual variations in behavior (as seen in experimental variability and model stochasticity). The paper tested robustness of alignment/anti-alignment force map patterns across different fish numbers, neighbor distances, distances to tank walls, heading orientations, and focal fish velocities (Supplementary Figures S5-S10), finding qualitative consistency of the core findings. However, robustness is not rigorously quantified (e.g., tolerance to specific noise levels, failure rates under extreme conditions). Qualitative robustness to a range of conditions relevant to experimental setup and natural variations in fish behavior is indicated, but detailed quantitative robustness assessments are absent.
    *   Implicit/Explicit: Mixed
        *  Justification: Qualitative robustness is implicitly demonstrated through the consistent observation of schooling and force map patterns across different experimental fish groups and model parameter variations (as shown in supplementary figures).  However, lack of quantitative metrics for robustness (e.g., operational window size, noise tolerance thresholds) implies that the robustness score is based on qualitative assessment and indirect evidence rather than precise quantitative measurements.
    *   CT-GIN Mapping: e.g., This score contributes to the reliability attributes of the `BehaviorArchetypeNode`: `robustness_score: 7`, `robustness_qualitative: Moderately Robust`, `robustness_perturbations_tested: Number of fish, neighbor distance, wall proximity, heading, velocity`.

### **8.3 CT-GIN Emergent Behavior Validation**

*    **Vector ID:** M8.3
*    **Vector Type:** Validation
     *  Content: Methods used to validate claims of emergent behaviors:
        * Operational Definitions: Behaviors like "alignment" and "anti-alignment" are operationally defined through the direction of average acceleration vectors in the force maps (inward for alignment, outward for anti-alignment). "Leadership" is operationally defined through time-delayed correlations in velocities (positive delay for leaders, negative for followers).
        * Control Experiments/Variations: The study tested force map patterns across variations in number of fish, neighbor distances etc. (Supplementary Figures S5-S10) to check for consistent patterns and rule out confounding factors.  Surrogate data analysis with known leader-follower setups (Figure 5) acts as a form of control, validating force map interpretations for leader/follower dynamics.
        * Quantitative Analysis: Force maps are a quantitative method, averaging accelerations based on relative positions and velocities.  Statistical measures like PDFs of order parameters (Figure 4) and correlation coefficients (Figure 6) are used to quantify behavior and compare model predictions to experimental data.
        * Robustness/Reliability/Reproducibility: Robustness is tested across different conditions (Supplementary Figs S5-S10), suggesting some reliability of the observed patterns. Reproducibility is supported by the agent-based model, which can recreate qualitatively similar force maps and behaviors with the defined rules.
        * Limitations: Validation is primarily qualitative and statistical. Force map analysis is known to have limitations (non-uniqueness of interaction rule inferences, potential mixing of different interactions). Quantitative precision in predicting individual fish trajectories from force rules is not achieved or claimed. The surrogate leader-follower analysis is limited to self-comparison in experimental data and does not involve direct manipulation or control of leadership roles.
         (Cite figures/tables/sections: Results section, Figures 1-6, Supplementary Figures S1-S18, Methods section).
     *   Implicit/Explicit: Explicit
    *   Justification: Validation methods are explicitly described throughout the Results section and illustrated in figures and supplementary materials. Operational definitions, control variations (in supplementary figures), quantitative analysis (force maps, PDFs, correlations), and discussions of limitations are clearly presented in the text.

## M9: Cognitive Proximity
*   **Vector ID:** M9
*   **Vector Type:** Cognition

### **9.1 Cognitive Mapping:**

*   **Vector ID:** M9.1
*   **Vector Type:** Description
    *   Content: The paper implicitly and explicitly maps aspects of fish behavior to cognitive processes, particularly "selective attention."
        * Selective Attention Analogy: The observed behavior (aligning with faster, ignoring slower neighbours) is explicitly interpreted as analogous to a "selective attention mechanism," suggesting fish are cognitively prioritizing faster-moving neighbors as more salient or informative social cues. This is framed as a potential mechanism to reduce cognitive load.
        * Leadership and Information Flow: Leader-follower relationships are discussed in terms of "information flow," analogizing faster fish to "influential individuals" transmitting movement information within the group. This implies a cognitive component in processing social information and responding to 'leaders'.
        * Limitations of Analogy: The paper acknowledges that force maps may not uniquely identify interaction rules and cautions against over-interpreting "anti-alignment" as a deliberate behavior, suggesting it may arise from inattention rather than explicit cognitive anti-alignment. The cognitive mapping is primarily analogical and functional, relating observed behavior to postulated cognitive mechanisms, without direct neurophysiological or detailed cognitive modeling of fish brains.
    *   CT-GIN Mapping: `CognitiveMappingEdge`. Specify source and target: `sourceNode: BehaviorArchetypeNode (Selective Alignment, Leadership)`, `targetNode: CognitiveFunctionNode (Selective Attention, Information Prioritization)`.
    *   Implicit/Explicit: Mixed
    * Justification: The cognitive mapping to "selective attention" and "information flow/leadership" is explicitly stated and discussed in the Results and Discussion sections. However, the nature of this mapping is primarily analogical and interpretative, rather than based on direct cognitive process measurements or detailed cognitive models of fish. Thus, it is 'Mixed' as it combines explicit cognitive labels and implicit inferential mapping from observed behavior to cognitive function.

### **9.2 Cognitive Proximity Score:**

*   **Vector ID:** M9.2
*   **Vector Type:** Score
    *   Score: [2.5]
    *   Justification: Based on the CT-GIN Cognizance Scale and the analysis in M9.1, the cognitive proximity score is approximately 2.5, falling between Level 2 (Sub-Organismal Responsivity) and Level 3 (Reactive/Adaptive Autonomy).
        * Level 2 (Sub-Organismal): The system exhibits behavior that resembles basic attention-like filtering (selective alignment), but the underlying mechanism remains at a relatively low level of cognitive complexity. It's closer to a sensory filtering or reactive bias than complex goal-directed attention. The "anti-alignment" is argued to be effective ignoring, not active purposeful behavior.
        * Level 3 (Reactive/Adaptive Autonomy – Partial): There's a hint of adaptive behavior in the speed-selective interactions—fish dynamically adjust their interactions based on neighbor speed, which can be seen as a form of context-dependent reactivity. However, genuine autonomy or complex goal-directed behavior, as at level 3, is not clearly evident.
        * Shortfall from Higher Levels: The system lacks demonstrated internal models, planning, relational cognition, or any higher-level cognitive functions (levels 4-10). The "intelligence" is primarily in the emergent collective motion and the selectivity of social interactions, not in complex individual cognitive capabilities. The cognitive proximity remains at a basic reactive/filtering stage, with analogies to attention but without deeper cognitive features being demonstrated or claimed.
    *   Implicit/Explicit: Mixed
    *  Justification: The score is a mixed assessment, combining explicit cognitive function analogies ("selective attention") from the paper with an implicit evaluation of the system's actual cognitive complexity based on the CT-GIN scale criteria. The justification explicitly contrasts the observed behavior with levels 2 and 3 of the scale, explaining why it scores between these levels and doesn't reach higher levels of cognizance (4+).

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
    | Sensing/Perception               |      6       | Fish sense relative positions and velocities of neighbors (primarily visually and via lateral line). Moderate fidelity, limited specificity beyond movement cues. | `CognitiveFunctionNode: Sensing/Perception` | Implicit | Inferred from behavioral response to neighbors' movement. |
    | Memory (Short-Term/Working)        |      2       | Possible short-term sensory memory needed to process neighbor speeds, but not explicitly tested or quantified. Limited retention, volatile. | `CognitiveFunctionNode: Memory (Short-Term)` | Implicit | Inferred as potentially necessary for real-time interaction, low score due to lack of direct evidence. |
    | Memory (Long-Term)                 |      1       | No evidence of long-term memory functions within the context of this study. Schooling behavior is innate/learnt over ontogeny, not changed by experiment. | `N/A`                                   | Implicit | Absent from experimental scope and results. |
    | Learning/Adaptation              |      2       | No learning or adaptation *within* experiment. Selective attention is a fixed rule, not modified. Very minimal plasticity demonstrated. |`CognitiveFunctionNode: Learning/Adaptation` | Implicit | Absent from experimental scope and results, low score due to lack of dynamic change. |
    | Decision-Making/Planning          |      4       | Fish make moment-to-moment 'decisions' about direction and speed, reactive to social cues. Simple, reactive decision making. No evidence of planning. |`CognitiveFunctionNode: Decision-Making`  | Implicit | Inferred from movement adjustments in response to neighbours, low planning evidence. |
    | Communication/Social Interaction |      7       | Schooling IS social interaction. Fish communicate implicitly through movement and speed cues, influencing each other's behavior. | `CognitiveFunctionNode: Communication/Social Interaction` | Explicit | Core focus, explicitly studied and demonstrated in schooling behavior. |
    | Goal-Directed Behavior            |      3       | Maintain school cohesion is an implicit 'goal'. But individual actions are more reactive than explicitly goal-directed over longer timescales. | `CognitiveFunctionNode: Goal-Directed Behavior` | Implicit | Inferred from school cohesion maintenance but limited individual long term goals. |
    | Model-Based Reasoning              |      1       | No evidence for model-based reasoning. Behavior appears rule-based and reactive, not based on explicit internal models of environment or social dynamics. | `N/A`                                   | Implicit | Absent from analysis and experimental design, low score due to lack of model reliance. |
    | **Overall score**                 |      [3.25]       | Averaged score from individual cognitive functions.                                                                                       |                                   |                     |                |

    *   **Note:** Assess the system for *each* function, providing a score (0-10) and a short (1-2 sentences) justification.  0 = Absent, 10 = Human-level performance.

## M10: Criticality Assessment
*   **Vector ID:** M10
*   **Vector Type:** Criticality

### **10.1 Criticality:**

*   **Vector ID:** M10.1
*   **Vector Type:** Assessment
    *   Content: [Unclear] Does the system operate near a critical point, displaying scale-free behavior, power laws, or long-range correlations?
    *   Justification: The paper does not explicitly investigate or discuss criticality in the schooling fish system.  While collective animal behavior in general, and flocking/schooling in particular, *can* exhibit criticality (phase transitions in group behavior, scale-free networks of interaction in some species in other studies), this paper does not present data or analysis to assess criticality for black neon tetras or in the context of speed-induced leadership and selective interactions specifically. No power law distributions, long-range correlation analyses, or order parameter fluctuations indicative of criticality are presented or mentioned within this publication. Therefore, it's unclear from *this paper* if the system operates near criticality.
        *   Critical Parameters (If Yes/Partial): [N/A]
        *   Evidence: [No evidence in the paper]
    *   Implicit/Explicit: Implicit
    *    Justification: The absence of any discussion or analysis related to criticality, phase transitions, scale-free behavior, or power laws in the paper implicitly suggests that criticality is not a feature that was investigated or found to be relevant within the scope of this study.

## M11: Review Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Review")**

*   **Vector ID:** M11
*   **Vector Type:** Review
    *   Content: N/A

## M12: Theoretical Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Theoretical")**

*   **Vector ID:** M12
*   **Vector Type:** Theory
    *   Content: N/A

## M13: Overall Assessment & Scoring

*   **Vector ID:** M13
*   **Vector Type:** Overall

### **13.1 CT-GIN Readiness Score:**

*   **Vector ID:** M13.1
*   **Vector Type:** Score
*   **Calculated Score:** [5.3]

**CT-GIN Readiness Summary Table:**

| CT-GIN Aspect                   | Strength (Yes/Partial/No) | Key Supporting Metrics (with units) | Limitations (Missing Metrics/Data Gaps)                                           | Improvement Areas (Future Research)                                          |
| :------------------------------ | :-----------------------: | :-----------------------------------| :------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| Energy Flow Efficiency          |           No            |                 N/A                  | Efficiency not quantified                                                     | Quantify metabolic and computational energy use and efficiency metrics.       |
| Memory Fidelity                 |           No            |                 N/A                  | No explicit memory mechanism demonstrated.                                    | Investigate potential for short-term social memory and its neural basis.      |
| Organizational Complexity       |          Yes          | Polarization ϕ, Convex hull area s | Limited types of emergent order explored.                                       | Explore range of emergent patterns (swarming, milling) and transitions.      |
| Embodied Computation            |          Yes          |      Force maps, Reaction time ~0.2s    | Limited quantification of computational power, energy use per operation.        | Quantify computational load, energy efficiency of information processing.     |
| Temporal Integration            |        Partial          |       Reaction time ~0.2 s        | Limited to reaction timescales, no long-term temporal integration demonstrated. | Investigate longer timescales of social dynamics, temporal coding.           |
| Adaptive Plasticity             |           No            |                 N/A                  | No adaptive change demonstrated in interaction rules.                          | Study plasticity of interaction rules through learning/experience paradigms. |
| Functional Universality         |           No            |                 N/A                  | Functionality limited to schooling, alignment, leadership.                     | Explore broader functional repertoire beyond basic social coordination.       |
| Cognitive Proximity            |        Partial          | Cognitive Proximity Score: 2.5     | Cognitive mapping limited to analogical 'selective attention'.                 | Develop more detailed cognitive models, test for higher-level cognitive functions. |
| Design Scalability & Robustness |        Partial          |  Robustness Score: 7                | Robustness tested qualitatively, not rigorously quantified.                     | Quantify robustness to noise, perturbations, component variability.           |
| **Overall CT-GIN Readiness Score** |        5.3       |   Average Score: 5.3  |   |      |


### **13.2 Qualitative CT-GIN Assessment Conclusion:**

*   **Vector ID:** M13.2
*   **Vector Type:** Textual Summary
    *   Content: The paper presents a compelling study of schooling fish behavior, demonstrating evidence for speed-induced leadership and selective social interactions based on relative speeds. Key Strengths include the use of force map analysis to empirically derive interaction rules from experimental data and the validation of these findings through agent-based modeling. The emergent behavior of selective alignment is robustly demonstrated across various conditions. However, Key Limitations exist in the areas of memory, energy efficiency, and cognitive complexity, which are not deeply explored or quantified. The cognitive proximity remains at a basic sub-organismal/reactive level, primarily drawing analogies to selective attention. Overall Assessment: The work provides significant insights into the self-organizing principles of collective motion and provides a valuable methodological framework for analyzing social interactions in biological systems. Within the CT-GIN framework, it demonstrates moderate readiness, exhibiting self-organization and embodied computation at a basic level, but lacking in more advanced features like memory, adaptation, and higher cognitive functions. Future work could significantly enhance its CT-GIN profile by addressing the limitations outlined in the summary table, particularly by exploring memory mechanisms, quantifying energy aspects, and delving into the potential cognitive underpinnings of selective social behaviors in fish.

### **13.3 CT-GIN Refinement Directions:**

*   **Vector ID:** M13.3
*   **Vector Type:** Recommendations
    *   - Quantify energy expenditure for individual fish and the entire school to assess energy efficiency in relation to collective motion and information processing.
    *   - Investigate potential short-term memory mechanisms that may be involved in speed-based selective attention, perhaps through neural correlates or behavioral experiments designed to test for temporal dependencies beyond immediate reactions.
    *   - Explore a wider range of emergent patterns beyond polarized motion, such as swarming and milling within this system, and analyze the transitions between these states in relation to environmental or internal parameters.
    *   - Develop quantifiable metrics for the computational power and energy cost of information processing in individual fish brains and the agent-based model, possibly using information-theoretic measures or computational complexity analyses.
    *   - Conduct experiments to investigate temporal integration and anticipation in fish schooling behavior over longer timescales, testing for predictive strategies and responses to delayed information.
    *   - Design experiments to probe adaptive plasticity in social interaction rules, examining if and how these rules can be modified through learning or experience in response to changing environmental conditions or social contexts.
    *   - Broaden the functional repertoire of the system beyond basic social coordination to explore more complex behaviors, such as collective decision-making, foraging, or predator avoidance, within the CT-GIN framework.
    *   - Develop more detailed cognitive models that explicitly represent potential internal models or predictive processing within fish brains, going beyond analogical mappings to selective attention.
    *   - Rigorously quantify the robustness of schooling behavior and force map patterns to various perturbations, using operational window sizes, noise tolerance thresholds, and failure rate metrics to assess design scalability and reliability aspects.

## M14: CT-GIN Knowledge Graph

*   **Vector ID:** M14
*   **Vector Type:** Visualization

### **14.1. CT-GIN Knowledge Graph:**
* **Content:**
[__Textual Description of CT-GIN Knowledge Graph (Schematic Diagram in visual format would be ideal):__

**Nodes:**

*   **SystemNode:** (Shape: Circle, Color: Blue)
    *   Attributes: `systemType: Biological & Computational`, `domain: Animal Behavior`, `mechanism: Force Map Analysis, Agent-Based Modeling`, `components: Schooling Fish, Experimental Tank, Agent-Based Model`, `purpose: Understand collective motion and social interactions in animal groups, investigate speed-induced leadership`

*   **EnergyInputNode:** (Shape: Diamond, Color: Green)
    *   Attributes: `source: Metabolic (fish), Computational (model)`, `type: Chemical (food), Electrical (computation)`

*   **ComputationNode:** (Shape: Square, Color: Orange)
    *   Attributes: `computationType: Analog`, `primitiveFunction: Vector Summation, Weighted Averaging, Thresholding`, `functionSubtype: N/A, Distance-Weighted, Speed-Threshold`

*   **ConfigurationalNode:** (Shape: Pentagon, Color: Purple)
    *   Attributes: `orderType: Polarized Movement, Swarming, Milling`, `description: Collective motion patterns in schooling fish`, `parameters: Polarization (ϕ), Nearest neighbor distance, Convex hull area`

*   **BehaviorArchetypeNode:** (Shape: Hexagon, Color: Red)
    *   Attributes: `behaviorType: Collective Motion, Selective Alignment, Leadership`, `behaviorSubtype: Schooling, Polarized Movement, Swarming, Milling, Speed-Based, Dynamic Leadership, Force Map Signature`,  `robustness_score: 7`, `robustness_qualitative: Moderately Robust`

*   **CognitiveFunctionNode:** (Shape: Heptagon, Color: Yellow)
    *   Attributes: `functionType: Selective Attention, Information Prioritization, Sensing/Perception, Memory (Short-Term), Communication/Social Interaction, Decision-Making, Goal-Directed Behavior`

**Edges:**

*   **EnergyTransductionEdge:** (Color: Dark Green, Directed)
    *   Attributes: `mechanism: Metabolic processes, Muscular contraction, Algorithmic calculation`, `from_node: Chemical Energy (food), Computational Energy`, `to_node: Kinetic Energy (fish motion), Simulated motion (agents), Digital Data (tracking)`, `efficiency_score: 3`, `efficiency_qualitative: Low`

*   **AdjunctionEdge (Local Interaction):** (Color: Dark Blue, Directed, bidirection optional)
    *   Attributes: `type: Social Interaction`, `subtype: Attraction-Repulsion, Alignment, Selective Attention`, `rules: Equations (1) & (2), Speed-based selection criteria`, `parameters: k_rep, k_att, d_0, µ, v_0, τ, σ_v, σ_φ`, `predictability_score: 7`

*   **CognitiveMappingEdge:** (Color: Dark Red, Dashed, Directed)
    *   Attributes: `sourceNode: BehaviorArchetypeNode (Selective Alignment, Leadership)`, `targetNode: CognitiveFunctionNode (Selective Attention, Information Prioritization)`


**Example Node and Edge Connections (Partial):**

*   EnergyInputNode ->(EnergyTransductionEdge)-> BehaviorArchetypeNode (Collective Motion)
*   SystemNode --(AdjunctionEdge)-> ConfigurationalNode (Local Rules -> Global Order)
*   BehaviorArchetypeNode (Selective Alignment) --(CognitiveMappingEdge)-> CognitiveFunctionNode (Selective Attention)
*   ComputationNode --(Implicitly related to via System Description)--> BehaviorArchetypeNode.

__]

## M15: Relationship Vectors
*   **Vector ID:** M15
*   **Vector Type:** Relationships
*   Relationships:
        | Source Vector ID | Target Vector ID | Relationship Type |
        | ------------- | ------------- | ----------------- |
        | M2.1 | M2.2 | Energy Flow |
        | M2.2 | M2.4 | Energy Flow |
        | M4.2 | M4.3 | Local-to-Global (Adjunction) |
        | M5.1 | M8.1 | Computation-to-Behavior |
        | M9.1 | M8.1 | Cognitive Mapping relates to Behavior |

## M16: CT-GIN Template Self-Improvement Insights

*   **Vector ID:** M16
*   **Vector Type:** Feedback

### **Template Feedback:**

*    **Vector ID:** M16.1
*   **Vector Type:** Text
Provide specific, actionable feedback on the *CT-GIN template itself*, based on this analysis:
    *   **Missing Probes:** The template is quite comprehensive. Perhaps a probe explicitly asking about "Scalability of System" (beyond robustness, towards larger groups or more complex architectures) could be beneficial. Also "Environmental Dependency" probe, to assess how much system relies on specific controlled environment.
    *   **Unclear Definitions:** The "Cognitive Proximity Score" levels in Module 9 could benefit from slightly more detailed behavioral anchors for each level. While the rubric is helpful, more operational examples tied to observable material system behaviors for each score level might enhance inter-rater reliability.
    *   **Unclear Node/Edge Representations:** The guidance was generally sufficient. For complex systems, more detailed examples of decomposing system functionality into specific node/edge types might be helpful in future iterations of the template. Specifying allowed attribute types (numerical, categorical, text) for nodes and edges could also enhance clarity and data standardization.
    *   **Scoring Difficulties:** Assigning scores for "Cognitive Proximity" and "Yoneda Embedding" was somewhat subjective and required interpretation, even with the rubrics. More finely grained scoring criteria with intermediate anchor points could increase scoring precision and consensus.
    *   **Data Extraction/Output Mapping:** Mapping extracted information to the CT-GIN nodes and edges was generally straightforward. The table formats and structured question probes facilitated data extraction and organization into corresponding CT-GIN elements.
    *   **Overall Usability:** The template was generally well-structured and usable. The modular approach and clear headings make it easy to navigate and systematically analyze papers. The inclusion of example CT-GIN mappings in each section is very helpful.
    * **Specific Suggestions:**
        * Add a "Scalability" probe in Module M8 (Emergent Behaviors) to assess system's potential for scaling up in size or complexity.
        * Add an "Environmental Dependency" probe in Module M1 (System Overview).
        * Expand the "CT-GIN Cognizance Scale" rubric with more operational behavioral examples for each level, especially for levels 2-5, relevant to material systems.
        * Provide more detailed examples or a short guide on decomposing complex systems into specific CT-GIN node and edge types for different system architectures (e.g., hierarchical, network-based, etc.)
        * Consider adding sub-scores within the "Cognitive Function Checklist" (M9.3) for Short-Term and Long-Term Memory to differentiate between these aspects more explicitly.