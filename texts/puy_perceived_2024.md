# Perceived risk determines spatial position in fish shoals through altered rules of interaction:

__Paper Type:__ Experimental

## M1: System Overview & Implementation
*   **Vector ID:** M1
*   **Vector Type:** Overview

### **1.1 System Description**

*   **Vector ID:** M1.1
*   **Vector Type:** Description
    *   Content: The system is composed of two subgroups of black neon tetra fish: habituated (Hab) and non-habituated (Non-hab) to an experimental environment. The system analyzes the collective movement of these merged subgroups within an experimental tank, focusing on how perceived risk (manipulated by habituation) influences spatial positioning and interaction rules within the shoal. The purpose is to understand how individual differences in risk perception drive spatial assortment and collective behavior in animal groups. Components include the fish subgroups, the experimental tank, and video recording equipment for trajectory analysis.
    *   CT-GIN Mapping: `SystemNode` attributes: `systemType`: "Biological", `domain`: "Animal Behavior", `mechanism`: "Risk Perception-Driven Interaction", `components`: "Habituated Fish, Non-habituated Fish, Experimental Tank, Video Recording System", `purpose`: "Investigate impact of risk perception heterogeneity on spatial assortment and collective behavior".
    *   Implicit/Explicit: Explicit
        *  Justification: The system description, components, and purpose are explicitly stated in the introduction and methods sections of the paper.

### **1.2 Implementation Clarity**

*   **Vector ID:** M1.2
*   **Vector Type:** Score
    *   Score: [9]
    *   Justification: The experimental setup, procedure for habituation and testing, and data analysis methods (trajectory recording, force map, machine learning) are described in detail within the Methods and Results sections. The paper clearly explains how the subgroups were created, how their behavior was recorded, and the analytical tools used to interpret the data. Minor details such as dimensions of fish containers during the merge and the specific models of cameras or software are absent, but overall the implementation is very clear and reproducible based on the provided information.
    *   Implicit/Explicit: Mixed
        * Justification:  The overall implementation is clearly described (Explicit), but some minor specific equipment details are implicit or assumed to be standard laboratory equipment.

### **1.3 Key Parameters**

*   **Vector ID:** M1.3
*   **Vector Type:** ParameterTable
    *   Table:
        | Parameter Name | Value | Units | Source (Fig/Table/Section) | Implicit/Explicit | Data Reliability (High/Medium/Low) | Derivation Method (if Implicit) |
        | :------------- | :---: | :---: | :-----------------------: | :-----------------: | :-----------------------------: | :-------------------------------: |
        | Number of fish per subgroup | 8 | individuals | Methods | Explicit | High | N/A |
        | Experiment duration | 2 | hours | Methods | Explicit | High | N/A |
        | Video frame rate | 50 | fps | Methods | Explicit | High | N/A |
        | Tank water column height | 7 | cm | Methods | Explicit | High | N/A |
        | Habituation days | 5 | days | Methods | Explicit | High | N/A |

    *   **Note:** List *up to 5* key parameters characterizing the system's *implementation*.  Provide values and units if possible. If a parameter is not explicitly stated but derived/inferred, clearly state the derivation method. *Always* include units if applicable. If a value is not applicable, write "N/A".  Data Reliability: High = Directly measured, Medium = Derived from measurements/simulations, Low = Estimated/Inferred.

## M2: Energy Flow
*   **Vector ID:** M2
*   **Vector Type:** Energy

### **2.1 Energy Input**

*   **Vector ID:** M2.1
*   **Vector Type:** Input
    *   Content: The primary energy source is the metabolic energy derived from food consumed by the fish (Ocean Nutrition Community Formula Flakes). Light energy from six lamps above the experimental tank is also provided, but primarily for visualization rather than directly powering the fish behavior in terms of motion, though it influences the photic environment and potentially fish behavior indirectly.
    *   Value: N/A
    *   Units: N/A
    *   CT-GIN Mapping: `EnergyInputNode`: attributes - `source`: "Metabolic (Food), Light", `type`: "Chemical, Electromagnetic".
    *   Implicit/Explicit: Mixed
        *  Justification: The food source is explicitly mentioned. Light is mentioned as homogenous light intensity, implicitly serving as a consistent ambient condition allowing for observation, rather than as direct energy input for movement. The metabolic origin of fish movement energy is inferred and common biological knowledge.

### **2.2 Energy Transduction**

*   **Vector ID:** M2.2
*   **Vector Type:** Transduction
    *   Content: Chemical energy from food is transduced into kinetic energy through the fish's biological processes (cellular respiration, muscle contraction). Light energy is transduced via photoreceptors in the fish's eyes into neuronal signals, influencing their perception of the environment and consequently their behavior, which translates into kinetic energy.
    *   CT-GIN Mapping: `EnergyTransductionEdge`: attributes - `mechanism`: "Biochemical, Photochemical-Neural-Muscular", `from_node`: "EnergyInputNode (Metabolic, Light)", `to_node`: "SystemNode (Fish Movement)".
    *   Implicit/Explicit: Implicit
        *  Justification: The paper does not explicitly detail energy transduction pathways, but it is implicitly understood that fish utilize metabolic energy from food for motion and light for vision which guides behavior. This relies on general biological knowledge.

### **2.3 Energy Efficiency**

*   **Vector ID:** M2.3
*   **Vector Type:** Score
    *   Score: [3]
    *   Justification/Metrics: The paper does not provide any quantitative metrics for energy efficiency. Fish biological systems are generally not highly efficient in converting metabolic energy to motion, with significant energy lost as heat and in metabolic processes.  The score is low due to the absence of efficiency considerations or optimizations in the study and the inherently low efficiency of biological systems for locomotion. Qualitative Assessment: Low.
    *   CT-GIN Mapping: Attribute of `EnergyTransductionEdge`s, `attribute_name`: "efficiency_score", `attribute_value`: 3.
    *   Implicit/Explicit: Implicit
      *  Justification: Energy efficiency is not discussed in the paper, and the score is inferred based on general knowledge about biological systems and the lack of optimization for energy use in the experimental design.

### **2.4 Energy Dissipation**

*   **Vector ID:** M2.4
*   **Vector Type:** Dissipation
    *   Content: Energy dissipation mechanisms include heat production during metabolism and muscle activity, hydrodynamic drag as fish move through water, and internal friction within biological tissues. Quantification of these mechanisms within the context of this study is not provided and would be complex. Qualitative assessment: High. Energy is continually dissipated through heat and drag as the fish move and maintain biological functions.
    *   CT-GIN Mapping: Creates `EnergyDissipationNode`s: `type`: "Heat, Hydrodynamic Drag, Internal Friction", and `EnergyDissipationEdge`s: `mechanism`: "Metabolic Heat Loss, Friction", `from_node`: "SystemNode (Fish Movement, Metabolic Processes)", `to_node`: "EnergyDissipationNode".
    *    Implicit/Explicit: Implicit
        *  Justification: Dissipation mechanisms are not explicitly quantified or thoroughly discussed but are implicitly present in the biological system and its movement in a fluid environment.  The assessment is based on fundamental physics and biology principles.

## M3: Memory
*   **Vector ID:** M3
*   **Vector Type:** Memory

### **3.1 Memory Presence:**

*   **Vector ID:** M3.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: Habituation inherently implies memory. The "habituated" subgroup exhibits a persistent change in state (lower perceived risk, altered behavior) due to prior experience (exposure to the experimental tank). This past experience influences their future behavior when merged with the non-habituated fish, demonstrated in their spatial positioning and interaction rules.
    *    Implicit/Explicit: Implicit
        * Justification: Memory is not explicitly discussed as a "memory component" but is implicitly required for habituation to occur. The experimental design relies on the premise that habituation induces a memory of a low-risk environment in one subgroup, affecting their subsequent behavior.

### **3.2 Memory Type:**

*   **Vector ID:** M3.2
*   **Vector Type:** Score
*   Score: [5]
*   Justification: The memory in this system resembles procedural or implicit memory, manifested in altered behavioral responses due to habituation. Retention is at least for the duration of the experiment (2 hours) and potentially longer from the 5-day habituation period. Capacity is limited to a binary state (habituated/non-habituated), not allowing for multiple re-writable states described in the score description. Read-out accuracy is inferred from observed behavioral differences, but not directly quantified for memory retrieval fidelity itself. Scale: 0 - no memory resemblance; 5 - basic behavioral change memory, not multi-state or high-fidelity; 10 - high fidelity, multi-state rewritable memory.
*   CT-GIN Mapping: Defines the `MemoryNode` type. `MemoryNode` attributes:  `memoryType`: "Implicit/Procedural", `retention`: "Medium-term (hours to days)", `capacity`: "Limited (binary state)", `readOutAccuracy`: "Qualitative (Behavioral)".
*    Implicit/Explicit: Mixed
    * Justification: The existence of memory (due to habituation) is implicit, while the score is a qualitative assessment based on the observed behavioral changes and general understanding of habituation as a basic form of implicit memory. The specific score and type are inferred.

### **3.3 Memory Retention Time:**

*   **Vector ID:** M3.3
*   **Vector Type:** Parameter
*   Value: [Long-term]
*    Units: [Qualitative Descriptor]
*   Justification: The habituation process occurred over 5 days, and the behavioral differences were observed throughout the 2-hour experiment on day 6. This suggests memory retention of at least 24 hours (from the last habituation session to the experiment) and persistent behavioral influence during the experimental period itself.  Qualitative Descriptor: Long-term relative to the timescale of the experiment.
*    Implicit/Explicit: Mixed
        * Justification: Memory retention is not directly measured in terms of decay rates but inferred to be "long-term" based on the experimental timescale and persistent behavioral differences observed. The term "Long-term" is a qualitative description relative to the experimental duration.
*   CT-GIN Mapping: Key attribute of the `MemoryNode`, `attribute_name`: "retentionTime", `attribute_value`: "Long-term (hours to days)", `units`: "Qualitative Descriptor".

### **3.4 Memory Capacity (Optional - if applicable)**

* **Vector ID:** M3.4
* **Vector Type:** Parameter
*  Value: [Binary States]
*   Units: [distinct states]
*   Justification: Memory capacity is limited in this context to distinguishing between two states: habituated (low perceived risk) and non-habituated (high perceived risk). There's no evidence of multiple, differentiable memory states or graded levels of habituation described.
*    Implicit/Explicit: Implicit
        *  Justification:  While habituation is binary (habituated/not), the paper implicitly treats it as a memory state that differs between the subgroups, thus defining a binary capacity relevant to the experimental design.
*   CT-GIN Mapping: Key attribute of the `MemoryNode`, `attribute_name`: "capacity", `attribute_value`: "Binary States", `units`: "distinct states".

### **3.5 Readout Accuracy (Optional - if applicable)**

* **Vector ID:** M3.5
* **Vector Type:** Parameter
*   Value: [Qualitative]
*   Units: [N/A]
*   Justification: Readout accuracy isn't quantified. It's qualitatively assessed by observing consistent behavioral differences (spatial positioning, interaction rules) between the subgroups, suggesting a relatively reliable recall or expression of the habituation memory in behavior. However, error rates or probabilistic measures of memory retrieval aren’t provided. Qualitative assessment: relatively accurate based on behavioral consistency.
*    Implicit/Explicit: Implicit
       *  Justification: Readout accuracy is evaluated implicitly through the consistent behavioral patterns.  The 'Qualitative' descriptor reflects the lack of numerical quantification for memory recall fidelity.
*   CT-GIN Mapping: Attribute of `MemoryNode` or related `ReadoutEdge`, `attribute_name`: "readoutAccuracy", `attribute_value`: "Qualitative (Behavioral)", `units`: "N/A".

### **3.6 Degradation Rate (Optional - if applicable)**
* **Vector ID:** M3.6
* **Vector Type:** Parameter
    *   Value: [N/A]
    *   Units: [N/A]
    *   Justification: The paper does not assess memory degradation rate. The experiment is designed to observe behavior within a 2-hour timeframe *after* habituation. Memory stability is assumed within this window, but degradation over longer periods is not investigated.
    *    Implicit/Explicit: Explicit
            * Justification: Degradation rate is not mentioned or measured in the paper, so explicitly N/A.
    *   CT-GIN Mapping: Attribute of the `MemoryNode`, `attribute_name`: "degradationRate", `attribute_value`: "N/A", `units`: "N/A".

### **3.7 Memory Operations Energy Cost (Optional - if applicable)**
* **Vector ID:** M3.7
* **Vector Type:** Table
*   Table:
    | Memory Operation ID | Energy Consumption per Bit | Power Usage during Operation| Units | Uncertainty | Data Source Reference | Implicit/Explicit | Justification |
    | :------------------ | :--------------------------: | :-----------------------------: | :---: |:-----------------:|:-----------------:|:-----------------:| :------------------ |
    | Habituation encoding | N/A                         | N/A                             |  N/A  | N/A            | N/A    | Explicit | No data available in paper for energy cost of memory operations. Memory operations are implicit and biological. |
    | Memory recall (behavioral) | N/A                         | N/A                             |  N/A  | N/A            | N/A    | Explicit | No data available in paper for energy cost of memory operations. Memory operations are implicit and biological. |
*   Implicit/Explicit: Explicit
    *   Justification: Energy cost of memory operations is not analyzed or discussed in the paper, hence explicitly N/A.

### **3.8 Memory Fidelity & Robustness Metrics (Optional - if applicable)**
* **Vector ID:** M3.8
* **Vector Type:** Table
*   Table:
    | Metric ID | Description | Value | Units | CT-GIN Mapping | Data Source | Implicit/Explicit | Justification |
    | :-------- | :---------- | :----: | :---: | :-------------: | :----------: |:-----------------:| :-----------------:|
    | Classification Accuracy  | Machine Learning Classification | ~79 | % | Attribute of `MemoryNode` | Table Ib | Explicit | Machine Learning tool successfully classifies subgroups with ~79% accuracy based on behavior. |
*   Implicit/Explicit: Explicit
*   Justification: The machine learning classification accuracy of approximately 79% serves as a measure of behavioral fidelity correlated with subgroup identity (habituated vs non-habituated), which is linked to the memory of habituation. This is explicitly reported in the Results section and Table Ib.

---

## M4: Self-Organization and Emergent Order
*   **Vector ID:** M4
*   **Vector Type:** Self-Organization

### **4.1 Self-Organization Presence:**

*   **Vector ID:** M4.1
*   **Vector Type:** Binary
    *   Content: [Yes] *Self-organization*: spontaneous emergence of global order/patterns from *local* interactions, *without* external control defining the global structure.
    *   Justification: Fish shoaling itself is a self-organized behavior, resulting from local interaction rules (attraction, repulsion, alignment) among individuals, without a central leader dictating the shoal's global structure. The spatial assortment observed (risk-sensitive fish in the center) also emerges from altered local interaction rules based on individual risk perception, rather than external organization. The global pattern (spatial assortment in the shoal) emerges spontaneously from these local interactions.
    *   Implicit/Explicit: Mixed
        *  Justification: The paper implicitly assumes shoaling is self-organized (common knowledge in animal behavior) and explicitly investigates how *altered* local interactions contribute to *emergent spatial patterns* related to risk.  The 'emergent order' of spatial assortment is directly investigated.

### **4.2 Local Interaction Rules:**

*   **Vector ID:** M4.2
*   **Vector Type:** Rules
    *   Content: Local interaction rules are modeled implicitly through "effective forces" inferred from fish movement. These include:
        1.  **Attraction-Repulsion forces:**  Governed by distance to nearest neighbors. Repulsion at short distances, attraction at longer distances, with an equilibrium distance in between. Figure 2f quantifies the radial acceleration (ar) as a function of nearest neighbor distance, showing stronger repulsion for habituated vs non-habituated individuals.
        2.  **Alignment forces:** Based on relative velocities with nearest neighbors. Selective alignment with faster neighbors. Alignment forces are inferred from alignment force maps (Supplementary Fig. S13) and velocity density distributions (Fig. 4). Non-habituated fish with habituated neighbors exhibit stronger alignment interactions (inferred from alignment force map plots and density distributions).
        3.  **Self-Propulsion forces:** Characterized by burst-and-coast dynamics. Non-habituated fish exhibit constrained burst-and-coast motion (Fig. 6b-d).
    These rules are not presented as explicit equations but are inferred from behavioral data and visualized using force maps and probability density functions.
    *   CT-GIN Mapping: Part of the `AdjunctionEdge` description (local side). These define the "LocalInteraction" category of edges. `AdjunctionEdge` attributes: `interactionType`: "Attraction-Repulsion, Alignment, Self-Propulsion", `description`: "Effective forces inferred from acceleration patterns as function of relative position and velocity with neighbours. Quantified by force maps and PDFs.",  `parameters`: "Equilibrium distance in attraction-repulsion, strength of repulsion/attraction/alignment forces, burst-and-coast dynamics parameters."
    * **Implicit/Explicit**: Mixed
        *  Justification: The *existence* of local interaction rules (attraction, repulsion, alignment) as drivers of shoaling is implicitly assumed (standard in collective behavior). The specific *form* and *parameters* of these rules are inferred *implicitly* through analysis of acceleration patterns, force maps, and statistical distributions depicted in figures, not explicitly stated as mathematical rules, but visualized and qualitatively described based on the figures.

### **4.2.1 Local Interaction Parameters:**

* **Vector ID:** M4.2.1
* **Vector Type:** Table
*   Table:
    | Rule ID | Description | Parameter Name | Parameter Value Range | Units | Data Source | Implicit/Explicit | Justification |
    | :------ | :---------- | :------------- | :---------- | :---: | :----------: | :----------------: | :------------: |
    | 1 | Repulsion Strength (Attraction-Repulsion) | Peak radial acceleration at short NN distance |  ~20 Habituated, ~10 Non-habituated  | cm/s² | Fig 2f | Implicit | Estimated from peak height in Fig 2f showing average radial acceleration vs NN distance. |
    | 2 | Equilibrium NN Distance (Attraction-Repulsion) | Distance at ar = 0 |  ~ 2-3 | cm | Fig 2f | Implicit | Estimated from zero-crossing in Fig 2f showing average radial acceleration vs NN distance. |
    | 3 | Preferred NN distance (Distance PDF peak) | Peak of NN distance PDF | ~ 2 | cm | Fig 2c | Explicit | PDF peak distance explicitly identified as preferred NN distance in text. |
    | 4 | Burst-and-coast minimum speed | Speed at lower PDF peak | ~ 3 | cm/s | Fig 6b | Implicit | Estimated from lower peak location in speed PDF Figure 6b. |
    | 5 | Burst-and-coast maximum speed | Speed at upper PDF peak/shoulder | ~ 35 Habituated, ~ 25 Non-habituated  | cm/s | Fig 6b | Implicit | Estimated from approximate shoulder/peak location in speed PDF Figure 6b. |
### **4.3 Global Order:**

*   **Vector ID:** M4.3
*   **Vector Type:** Order
    *   Content: The global order that emerges is spatial assortment within the shoal, specifically the tendency for non-habituated (higher risk perception) fish to occupy more central positions and habituated (lower risk perception) fish to occupy more peripheral positions. This is visualized in spatial density distributions (Fig. 1a, 1b, 1c) and confirmed by analysis of time spent on the shoal border (Fig. 1d). The shoal maintains cohesion and polarization as a group but exhibits internal spatial differentiation based on risk perception.
    *   CT-GIN Mapping: Defines a `ConfigurationalNode`. `ConfigurationalNode` attributes: `orderType`: "Spatial Assortment", `description`: "Risk-based spatial segregation within fish shoal.", `manifestation`: "Central positioning of high-risk fish, peripheral positioning of low-risk fish.",  `quantification`: "Spatial density distributions (Fig. 1a-c), border duration PDF (Fig. 1d).".
    * **Implicit/Explicit**: Explicit
        *  Justification: The emergent global order (spatial assortment) is directly observed and quantified through spatial density distributions and border duration analysis presented in the Results and figures. The description of this global order is explicit in the text and figures’ captions.

### **4.4 Predictability of Global Order:**

*   **Vector ID:** M4.4
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The spatial assortment is statistically predictable, as demonstrated by consistent differences in spatial density distributions and border occupancy between habituated and non-habituated fish across series and time. However, it's not perfectly deterministic; individual fish positions fluctuate dynamically. Predictability is supported by statistical significance of differences shown in figures and supplementary figures, reflecting a consistent bias but not absolute certainty in individual positioning. Qualitative assessment: Moderately predictable on a group level statistical basis.
    * **Implicit/Explicit**: Mixed
    *  Justification: The predictability is implicitly shown by the statistical consistency across replicates and time (consistent trends in figures), but not explicitly quantified with metrics like correlation coefficients for predictive models. The Score is an assessment based on the visual and qualitative description of statistical patterns.
    *   CT-GIN Mapping: Contributes to the `AdjunctionEdge` weight. `AdjunctionEdge` attributes: `predictabilityScore`: 7, `predictabilityJustification`: "Statistically significant spatial assortment observed across replicates and time, but not perfectly deterministic at individual level.  Consistent trends in density distributions and border occupancy.".

### **4.5. Local Interaction Rules (for Self-Organization)**
* **Vector ID:** M4.5
* **Vector Type:** Table
*   Table:
| Rule ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Source |
| :------ | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :-----: |
| 1 | Attraction | Radial acceleration becomes negative at distance from center-of-mass | Beyond ~10-15 | cm | Implicit | Negative values in radial acceleration plots in Fig 1g indicate attraction to center at larger distances | Fig 1g |
| 2 | Repulsion | Radial acceleration becomes positive at distance from nearest neighbor | Below ~2-3 | cm | Implicit | Positive values in radial acceleration plots in Fig 2f indicate repulsion between neighbors at short distances | Fig 2f |
| 3 | Alignment | Acceleration towards neighbours | Positive relative speed difference | cm/s | Implicit | Alignment force map shows arrows pointing inwards for positive velocity difference with neighbour, Supplementary Fig S13 | Supplementary Fig S13 |

### **4.6. Globally Emergent Order and Order Parameters**
* **Vector ID:** M4.6
* **Vector Type:** Table
*   Table:
| Property ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Protocol | Source |
| :---------- | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :------: | :-----: |
| 1 | Spatial Segregation Index | Density Ratio (Non-habituated central/Peripheral) | > 1 | unitless | Implicit | Density plots Fig 1a-c show higher non-habituated density centrally and lower peripherally, thus ratio > 1 implies segregation | Density Calculation from Fig 1a-c | Fig 1a-c |
| 2 | Border Occupancy Ratio (Habituated/Non-habituated) | Ratio of border duration PDF peak heights (Hab/Non-hab) | > 1 for short durations, < 1 for long durations | unitless | Explicit | Border Duration PDF in Fig 1d shows crossing, meaning ratio of Hab/Non-hab changes around 5s duration | PDF peak height measurement from Fig 1d  | Fig 1d |
| 3 | Polarization (Subgroup) | Polarization ϕ  | 0-1 (higher for non-habituated) | unitless | Explicit | Polarization measure used to quantify subgroup alignment, Fig 3b shows higher ϕ for non-habituated | Polarization Calculation | Fig 3b |

### **4.7 Yoneda Embedding and Local-to-Global Mapping Fidelity**

*   **Vector ID:** M4.7
*   **Vector Type:** Table
*   Table:
    | Link Type | Description | Predictability | Yoneda Score | Metrics | Implicit/Explicit | Justification | Source |
    | :-------- | :---------- | :------------- | :----------- | :------ | :----------------: | :------------: | :-----: |
    | Local Rules -> Spatial Assortment  | Local interaction parameters (repulsion, attraction, alignment) lead to spatial segregation by risk perception | Moderately Predictable (Score 7 from 4.4) | 6 |  Consistency of trends in density distributions, border occupancy, force maps across series and time.  Qualitative and statistical consistency. | Mixed | Spatial assortment is consistently observed but not perfectly deterministic. Local rules are inferred but not explicitly mathematically defined. Score of 6 reflects moderate, not perfect, predictability and implicit rule description. | Fig 1, 2, S1, S2, S5, S6 |
    *   **Yoneda Embedding Fulfillment Score [0-10]:** [Rubric: 0-2: No clear link, random global order.  3-4: Weak, inconsistent link; occasional global order. 5-7: Moderate link; statistically predictable global order from local rules.  8-9: Strong link; quantitatively precise prediction. 10: Perfect bijective mapping. Score 6 here reflects moderate link based on consistently observed spatial patterns and inferred local rules, but not a quantitatively precise, bijective mapping.  Examples: 0 - Random positions. 3 - Occasional weak clustering but no risk pattern. 7 - Statistically significant center-periphery risk pattern. 10 -  Precisely calculable position based on individual risk and local rules.]
    *   **Metrics:**  [Consistency of spatial density distributions, border occupancy, force maps across experimental series and time. Visual and statistical trend analysis.  Qualitative assessment of rule description precision.]
    *   **Justification:** The Yoneda Embedding score of 6 reflects a moderate level of fidelity in the mapping from local interaction rules (inferred effective forces and behavioral tendencies based on risk perception) to the observed global order (spatial assortment). While the spatial assortment is consistently observed and statistically predictable based on risk perception, the local interaction rules are themselves inferred and not explicitly mathematically formulated or perfectly quantified. The link is statistically significant and qualitatively clear, but not precisely, quantitatively bijective.

## M5: Computation
*   **Vector ID:** M5
*   **Vector Type:** Computation

### **5.1 Embodied Computation Presence:**

*   **Vector ID:** M5.1
*   **Vector Type:** Binary
    *   Content: [Yes] *Embodied computation*: computation intrinsic to the material's physical properties, *not* by an external controller.
    *   Justification: Fish brains perform embodied computation. Decisions regarding movement, spatial positioning, and interactions with neighbors are made by individual fish based on sensory input and internal state (risk perception). This computation is embodied in the fish's neural and physiological systems, translating sensory information into motor actions and social behaviors without external digital controllers. The machine learning tool is for *analysis* of fish behavior not for *control* of fish system.
    *    Implicit/Explicit: Implicit
        *  Justification: The concept of embodied computation in fish brains is implicit, relying on general biological understanding that animal behavior is computationally driven by neural systems.  The paper focuses on *observing and analyzing* this embodied computation rather than explicitly describing its mechanisms at a neuronal level, but it's inherently assumed.

### **5.2 Computation Type:**

*   **Vector ID:** M5.2
*   **Vector Type:** Classification
    *   Content: [Analog/Neuromorphic]  Fish brains perform analog, neuromorphic computation. Neural processing is continuous, graded, and parallel, resembling analog computation more than discrete digital steps. Neuromorphic aspect highlighted because brain-like processing involves distributed processing and adaptation inherent to neural networks.
    *   CT-GIN Mapping: Defines the `ComputationNode` type. `ComputationNode` attributes: `computationType`: "Analog/Neuromorphic".
    *    Implicit/Explicit: Inferred
    *    Justification:  The computational type is inferred based on understanding of biological neural networks which operate using analog and neuromorphic principles. The paper doesn't explicitly state "analog computation" but the described system is biological and brain-based.

### **5.3 Computational Primitive:**

*   **Vector ID:** M5.3
*   **Vector Type:** Function
    *   Content: Thresholding (activation function), Filtering (sensory input filtering), Signal Modulation (interaction rules modulation based on risk perception), Decision Making (spatial positioning, leader-follower roles). At a basic level, neuron activation itself is a thresholding function. Sensory processing involves filtering of environmental information. Risk perception modulates how fish react to social signals and make decisions about positioning and following behaviors.
    *   **Sub-Type (if applicable):** (Thresholding: Neural activation threshold; Filtering: Sensory filtering of visual/social cues.)
    *   CT-GIN Mapping: Defines the primary function of the `ComputationNode`. `ComputationNode` attributes:  `primitiveFunction`: "Thresholding, Filtering, Signal Modulation, Decision Making", `functionSubType`: "Thresholding: Neural activation threshold; Filtering: Sensory filtering of visual/social cues".
    *   Implicit/Explicit: Inferred
    * Justification: The described computations are primitives inferred from general understanding of neural information processing and animal behavior decision-making. These primitives are not explicitly stated in the paper in these terms, but are inferred as underlying mechanisms driving the observed behaviors.

### **5.4 Embodied Computational Units**
* **Vector ID:** M5.4
* **Vector Type:** Table
*   Table:
| Unit ID | Description | Processing Power | Energy/Operation | Freq/Resp. Time | Bit-Depth | Data Source | Implicit/Explicit | Justification |
| :------ | :---------- | :--------------- | :--------------- | :--------------: | :-------: | :----------: |:-----------------:| :-----------------:|
| Neuron | Biological neuron in fish brain | ~100-1000 operations/second (estimated) | ~10 fJ/synaptic operation (estimated) | ~millisecond  | Analog (graded) |  Inferred from general neuroscience knowledge | Inferred | Processing power, energy per operation, response time, and bit-depth are only estimates based on general neuroscience knowledge, not specific to this paper or fish type. Quantification within the context of this paper is impossible.  |

## M6: Temporal Dynamics
*   **Vector ID:** M6
*   **Vector Type:** Temporal

### **6.1 Timescales:**

*   **Vector ID:** M6.1
*   **Vector Type:** ParameterTable
    *   Table:
        | Timescale Description | Value | Units | Source | Implicit/Explicit | Justification |
        | :-------------------- | :---: | :---: | :----: | :----------------: | :------------: |
        | Neural Response Time (fish) | ~ milliseconds | ms | Inferred | Inferred | Inferred based on general biological neural response times. Not measured in paper directly. |
        | Reaction Time (fish leader-follower) | ~ ~0.1-0.2 | seconds | Fig 5 | Explicit |  Observed delay in leader-follower correlations in Fig 5. |
        | Burst-and-Coast Cycle Period | ~ ~1-2 | seconds | Fig 6a | Explicit |  Visual estimation from temporal speed evolution in Fig 6a for burst-and-coast dynamics. |
        | Border Duration (typical) | ~ 0.15 | seconds | Fig 1d | Explicit |  PDF peak for border duration in Fig 1d. |
        | Experiment Duration | 2 | hours | Methods | Explicit |  Experimental protocol, Methods section. |

    *   **Note:** Identify and quantify the *relevant timescales* of the system's dynamics (e.g., response time, process duration, oscillation period, memory decay, adaptation/learning timescale, self-assembly timescale). Use consistent units (e.g., seconds, milliseconds) for comparability.

### **6.2 Active Inference:**

*   **Vector ID:** M6.2
*   **Vector Type:** Assessment
    *   Content: [Partial] *Active Inference*: The system actively adjusts its behavior or internal state to minimize surprise or prediction error, based on an internal model of its environment.
    *   Justification: Fish behavior *partially* aligns with active inference. (1) *Prediction* and *surprise minimization* are suggested by selfish herd behavior; fish predict higher predation risk at periphery and move toward center (minimize 'surprise' of predation). (2) *Action selection* occurs in spatial positioning and interaction adjustments to achieve safer central locations. (3) *Internal models* – risk perception based on habituation can be considered a simple internal model of environmental risk, updated by experience (habituation). "Partial" as more complex aspects of active inference (detailed world models, hierarchical prediction errors) are not demonstrably present or investigated in this study.
    *   Implicit/Explicit: Mixed
        *  Justification: Active inference framework is not explicitly mentioned, but some observed behaviors (selfish herding interpreted as risk minimization, adaptive positioning) *implicitly* suggest aspects aligning with basic active inference principles. However, full validation and detailed modeling within active inference framework are absent - hence "Partial".
    *   **If Yes/Partial, provide examples of testable CT-GIN metrics that *could* be used to quantify active inference:** [Prediction error reduction rate: Measure the decrease in "prediction error" (e.g., proxied by distance to periphery, or 'risk exposure') over time as fish adjust spatial positions. Timescale of anticipation: Measure how quickly fish react to perceived increases in risk (e.g., simulated predator cues - not in this paper, but suggested for future). Complexity of internal models: Indirectly assess complexity by examining the range of behavioral responses to varied risk levels or environmental changes - though this paper uses binary (habituation) risk manipulation.]

## M7: Adaptation
*   **Vector ID:** M7
*   **Vector Type:** Adaptation

### **7.1 Adaptive Plasticity Presence:**

*   **Vector ID:** M7.1
*   **Vector Type:** Binary
    *   Content: [Yes] *Adaptive Plasticity*: System *changes its behavior or internal structure* in response to experience, leading to improved performance or altered functionality *over time*. This is *beyond* simple stimulus-response; it involves a persistent change.
    *   Justification: Habituated fish exhibit *adaptive plasticity*. Their prior experience (habituation to environment) leads to a *persistent change* in their behavioral tendencies (e.g., reduced repulsion, altered coordination) when compared to non-habituated fish. This change in behavior is not a transient stimulus-response but a longer-lasting modification of their interaction rules due to experience. It is adaptive in the sense that it changes their behavior in a way potentially relevant to survival and risk management (selfish herd hypothesis).
    *    Implicit/Explicit: Explicit
        * Justification: The paper explicitly demonstrates behavioral differences between habituated and non-habituated fish due to the habituation experience. This change is persistent throughout the 2-hour experiment and reflects a modification of behavior beyond immediate stimulus-response. Habituation is described as 'manipulating informational state' implying adaptive change.

### **7.2 Adaptation Mechanism:**

*   **Vector ID:** M7.2
*   **Vector Type:** Description
    *   Content: The adaptation mechanism is habituation. Repeated exposure to the experimental tank environment reduces the perceived risk for the habituated subgroup. This presumably involves neural plasticity within the fish brain, leading to a modification of neural circuits that process risk-related sensory information.  The specific neural mechanisms are not detailed, but the behavioral outcome is altered local interaction rules: reduced repulsion to neighbors, increased coordination, follower tendency. The adaptation is driven by environmental signals (absence of threat during habituation) causing a change in internal state (risk perception) that then modifies interaction rules and collective behavior. Mechanism implicitly aligns with basic associative learning (associating experimental environment with safety).
    *   CT-GIN Mapping: Defines the `AdaptationNode` type and `Monad` edges. `AdaptationNode` type: `adaptationType`: "Habituation/Associative Learning", `mechanismDescription`: "Neural plasticity in risk perception pathways due to repeated exposure to low-risk environment.", `drivingForce`: "Environmental signals (absence of threat), Internal state change (reduced risk perception).", `resultingChange`: "Modified local interaction rules (reduced repulsion, increased coordination, follower tendency)". `Monad` edges: represent the self-modification of the system state through habituation experience.
    *    Implicit/Explicit: Mixed
        *  Justification: The *behavioral outcome* of adaptation (altered interaction rules) is *explicitly* demonstrated and described. The *mechanism* of adaptation (neural plasticity, associative learning) is *implicitly* inferred based on understanding of habituation, but neural processes not directly measured or detailed.

## M8: Emergent Behaviors
*   **Vector ID:** M8
*   **Vector Type:** Behavior

### **8.1 Behavior Description:**

*   **Vector ID:** M8.1
*   **Vector Type:** Description
    *   Content: The main emergent behavior is risk-based spatial assortment in fish shoals. This manifests as non-habituated (higher risk perception) fish congregating toward the center of the group, while habituated (lower risk perception) fish are more frequently found at the periphery or front of the group. Furthermore, altered interaction rules emerge: non-habituated fish exhibit greater coordination and follower roles. The group as a whole shows cohesive movement and polarization, but with internal spatial structuring and differentiated roles based on risk perception heterogeneity.
    *   CT-GIN Mapping: Defines the `BehaviorArchetypeNode`. `BehaviorArchetypeNode` attributes: `behaviorType`: "Spatial Assortment, Differentiated Social Roles, Cohesive Group Movement", `description`: "Risk-based spatial segregation within shoal, with high-risk fish central and low-risk peripheral, accompanied by differentiated social roles (leaders/followers) and overall cohesive shoal motion.", `observableManifestation`: "Spatial density distributions, leader-follower correlations, velocity alignment measures".
    *    Implicit/Explicit: Explicit
       *  Justification: The described behaviors (spatial assortment, differentiated social roles, cohesive movement) are explicitly observed, quantified, and described in the Results section and associated figures. These are presented as the main findings of the study.

### **8.2 Behavior Robustness:**

*   **Vector ID:** M8.2
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The spatial assortment behavior and altered interaction rules are shown to be robust across three independent experimental series (replicates) presented in supplementary figures (S1, S5, S7, S11, S14, S16). Consistency across series indicates robustness to variations in individual fish sets. Furthermore, the behavior persists throughout the 2-hour experiment duration, shown in supplementary figures (S2, S6, S8, S12, S15, S17), demonstrating temporal robustness. Robustness is demonstrated by replication and temporal persistence, suggesting it's not a fragile transient effect. Qualitative assessment: Robust across replicates and time.
    *   Implicit/Explicit: Explicit
        *  Justification: Robustness is empirically demonstrated by consistent results across multiple experimental series and throughout the duration of the trials, explicitly shown through supplementary figures referencing series and time-course analyses.
    *   CT-GIN Mapping: This score contributes to the reliability attributes of the `BehaviorArchetypeNode`. `BehaviorArchetypeNode` attributes:  `robustnessScore`: 8, `robustnessJustification`: "Behavioral patterns (spatial assortment, interaction rules changes) consistent across 3 experimental replicates and throughout 2-hour trial duration. Robust to individual fish variability and temporal variations within experiment. Demonstrated via replicate comparisons in supplementary figures.".

### **8.3 CT-GIN Emergent Behavior Validation**

*    **Vector ID:** M8.3
*    **Vector Type:** Validation
     *  Content: Claims of emergent behaviors (spatial assortment, interaction rules changes) are validated by:
         1. **Operational Definitions:** Spatial position defined using normalized relative positions and center of mass (section "Group-level spatial interactions"). Border definition using convex hull (section "Group-level spatial interactions"). Interaction rules inferred from "force maps" and "alignment force maps" based on average acceleration (sections "Group-level spatial interactions", "Local-level spatial interactions", "Local-level coordination", and "Methods"). Leader-follower roles defined using time-delayed correlations (section "Leader-follower relationships"). Burst-and-coast dynamics defined by speed minima and maxima (section "Burst-and-coast dynamics").
         2. **Quantitative Analysis:** Statistical measures include PDFs (probability density functions) for spatial position, border duration, velocity differences, burst-and-coast parameters. Force maps and alignment force maps visualize average accelerations. Leader-follower roles quantified with correlation coefficients and delay analyses.
         3. **Replicates and Temporal Consistency:** Results are shown to be consistent across three experimental series and across different time intervals within experiments (Supplementary Figs. S1, S2, S5, S6, S7, S8, S11, S12, S14, S15, S16, S17).
         4. **Machine Learning Validation:** Machine learning tool successfully classifies subgroup identity based on observed behaviors, further validating behavioral differences (section "Machine learning identification tool", Table Ib). Limitations: Control experiments directly manipulating perceived risk independently of habituation are not performed. Cites Figures and sections throughout Results and Methods.
     *   Implicit/Explicit: Explicit
    *   Justification: Validation methods are clearly described in the Methods and Results sections, and results supporting the claims are explicitly presented in figures and supplementary figures throughout the paper.

## M9: Cognitive Proximity
*   **Vector ID:** M9
*   **Vector Type:** Cognition

### **9.1 Cognitive Mapping:**

*   **Vector ID:** M9.1
*   **Vector Type:** Description
    *   Content: The paper maps observed behaviors to cognitive concepts, primarily "risk perception" and "selfish herd hypothesis". "Risk perception" is used as a cognitive state that is manipulated via habituation and is hypothesized to drive behavioral differences. "Selfish herd hypothesis" is a cognitive/behavioral ecology concept explaining grouping behavior as individual risk minimization, interpreted as relevant to explain spatial assortment in fish. These are analogies at behavioral ecology level, not direct mappings to specific neural cognitive processes within fish brains, more metaphorical than mechanistic cognitive mapping.
    *   CT-GIN Mapping: If a mapping exists, this defines a `CognitiveMappingEdge`. Specify source and target (e.g., `BehaviorArchetypeNode` to `CognitiveFunctionNode`). `CognitiveMappingEdge`: `sourceNode`: "BehaviorArchetypeNode (Spatial Assortment)", `targetNode`: "CognitiveFunctionNode (Risk Perception, Self-Preservation)", `mappingType`: "Behavioral Ecology Analogy", `analogyDescription`: "Spatial assortment in fish shoal interpreted through lens of 'selfish herd' hypothesis, driven by individual 'risk perception' differences due to habituation.".
    *   Implicit/Explicit: Mixed
    * Justification:  The cognitive mapping to "risk perception" and "selfish herd" is explicitly used in the paper's framing and discussion, but the depth is at a behavioral ecology level, representing broader cognitive concepts as drivers of behavior rather than detailed cognitive mechanism mapping.  Analogy is explicitly used, but cognitive mechanisms are implicit.

### **9.2 Cognitive Proximity Score:**

*   **Vector ID:** M9.2
*   **Vector Type:** Score
    *   Score: [3]
    *   Justification: Score of 3 on CT-GIN Cognizance Scale aligns with "Reactive/Adaptive Autonomy" (Level 3). Fish adapt behavior (spatial positioning, interaction rules) based on experience (habituation, inferred risk), showing adaptation *beyond* simple stimulus-response. However, this adaptation is within a *limited behavioral repertoire* (shoaling, spatial adjustment, basic interaction adjustments). Evidence for *goal-directed/model-based cognition* (Level 4+) is absent; no demonstration of planning, flexible action selection, or complex world models, only basic risk-modulated shoaling. Fish exhibit basic adaptation driven by perceived risk, but not higher-level cognitive functions described in higher Cognizance Scale levels.
    *   Implicit/Explicit: Mixed
    *  Justification: Cognitive Proximity score assessed based on observed level of behavioral complexity and adaptation compared to CT-GIN Cognizance Scale. Justification involves both *explicit* behavioral observations in paper and *implicit* comparison to the tiered cognitive scale characteristics to arrive at Level 3 assessment. Score is not directly stated but inferred, mixed explicit evidence and implicit comparison.

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
    | Sensing/Perception               |       7      | Visual perception of environment and conspecifics drives behavior and social interaction. | `CognitiveFunctionNode`: `functionName`: "Sensing/Perception" | Implicit | Implicit: Assumed visual perception drives behavior, inferred from general fish biology. |
    | Memory (Short-Term/Working)        |       4      | Short-term memory likely involved in maintaining neighbor identity and shoal structure | `CognitiveFunctionNode`: `functionName`: "Memory (Short-Term/Working)" | Implicit | Implicit: Working memory presumed for maintaining social context, but not directly demonstrated. |
    | Memory (Long-Term)                 |       5      | Long-term (days) habituation memory modifies risk perception & behavior              | `CognitiveFunctionNode`: `functionName`: "Memory (Long-Term)" | Implicit | Implicit: Long-term memory inferred from persistent effects of habituation. |
    | Learning/Adaptation              |       6      | Habituation is a basic form of learning, adaptive adjustment to perceived risk.      | `CognitiveFunctionNode`: `functionName`: "Learning/Adaptation" | Explicit | Explicit: Habituation is explicitly tested and described in methods section. |
    | Decision-Making/Planning          |       3      | Basic decision-making in spatial positioning (central vs periphery) and following.  | `CognitiveFunctionNode`: `functionName`: "Decision-Making/Planning" | Implicit | Implicit: Decision-making inferred from behavioral choices, but no planning explicitly shown. |
    | Communication/Social Interaction |       7      | Shoaling behaviour is inherently social, based on local interactions and coordination.| `CognitiveFunctionNode`: `functionName`: "Communication/Social Interaction" | Explicit | Explicit: Study focuses on social interaction rules and coordination in shoals. |
    | Goal-Directed Behavior            |       4      | Selfish herd interpreted as goal to reduce predation risk via central positioning.   | `CognitiveFunctionNode`: `functionName`: "Goal-Directed Behavior" | Mixed | Mixed: Goal-directedness ('selfish herd') interpretation used, but directly demonstrated goals not investigated. |
    | Model-Based Reasoning              |       2      | Rudimentary 'risk model' via habituation, very simple environmental representation. | `CognitiveFunctionNode`: `functionName`: "Model-Based Reasoning" | Implicit | Implicit: 'Risk model' inferred from habituation effect, but very basic level of representation. |
    | **Overall score**                 |      [4.75]       |                                                                                       |                                   |                     |                |

    *   **Note:** Assess the system for *each* function, providing a score (0-10) and a short (1-2 sentences) justification.  0 = Absent, 10 = Human-level performance.

## M10: Criticality Assessment
*   **Vector ID:** M10
*   **Vector Type:** Criticality

### **10.1 Criticality:**

*   **Vector ID:** M10.1
*   **Vector Type:** Assessment
    *   Content: [Unclear] Does the system operate near a critical point, displaying scale-free behavior, power laws, or long-range correlations?
    *   Justification: The paper does not explicitly investigate criticality, phase transitions, scale-free behavior, power laws, or long-range correlations in fish shoal behavior. While collective animal behavior *can* exhibit criticality in some contexts (flocking phase transitions), this specific study does not provide evidence or analysis related to these concepts. Assessment: Unclear if system operates near criticality based on presented data.
        *   Critical Parameters (If Yes/Partial): [N/A]
        *   Evidence: [No evidence presented in paper.]
    *   Implicit/Explicit: Explicit
    *    Justification: Criticality is not mentioned or analyzed in the paper, hence explicitly "Unclear" based on paper's content. No data or equations related to criticality are present.

## M11: Review Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Review")**

*   **Vector ID:** M11
*   **Vector Type:** Review

### **11.1 Literature Synthesis Quality:**

*   **Vector ID:** M11.1
*   **Vector Type:** Score
    *   Score: [N/A]
    *   Justification: N/A
    *    Implicit/Explicit: [N/A]
         *  Justification: N/A

### **11.2 Gap Identification:**

*   **Vector ID:** M11.2
*   **Vector Type:** Score
    *   Score: [N/A]
    *   Justification: N/A
    *   Implicit/Explicit: [N/A]
        *  Justification: N/A

### **11.3 Future Directions:**

*   **Vector ID:** M11.3
*   **Vector Type:** Score
    *   Score: [N/A]
    *   Justification: N/A
    *    Implicit/Explicit: [N/A]
    *   Justification: N/A

### **11.4 Review Paper CT-GIN Alignment Score**

*   **Vector ID:** M11.4
*   **Vector Type:** Score
    *   Score: [N/A]
    *   Justification: N/A
    *    Implicit/Explicit: [N/A]
        *  Justification: N/A

## M12: Theoretical Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Theoretical")**

*   **Vector ID:** M12
*   **Vector Type:** Theory

### **12.1 Theoretical Rigor:**

*   **Vector ID:** M12.1
*   **Vector Type:** Score
    *   Score: [N/A]
    *   Justification: N/A
       * Implicit/Explicit: [N/A]
       *  Justification: N/A

### **12.2 Realization Potential:**

*   **Vector ID:** M12.2
*   **Vector Type:** Score
    *   Score: [N/A]
    *   Justification: N/A
    *   Implicit/Explicit: [N/A]
    *  Justification: N/A

### **12.3 Potential for Future CT-GIN Implementation Score**

* **Vector ID:** M12.3
*   **Vector Type:** Score
    *   Score: [N/A]
    *   Justification:  N/A
    *    Implicit/Explicit: [N/A]
    *   Justification: N/A

## M13: Overall Assessment & Scoring

*   **Vector ID:** M13
*   **Vector Type:** Overall

### **13.1 CT-GIN Readiness Score:**

*   **Vector ID:** M13.1
*   **Vector Type:** Score
*   **Calculated Score:** [5.33]

**CT-GIN Readiness Summary Table:**

| CT-GIN Aspect                   | Strength (Yes/Partial/No) | Key Supporting Metrics (with units) | Limitations (Missing Metrics/Data Gaps)                                           | Improvement Areas (Future Research)                                          |
| :------------------------------ | :-----------------------: | :-----------------------------------| :------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| Energy Flow Efficiency          |        No               |              N/A                     | Efficiency metrics not quantified.                                                  | Energy efficiency analysis, metabolic energy quantification during behavior.    |
| Memory Fidelity                 |         Yes               | Machine Learning Accuracy: ~79%      | Quantitative read-out accuracy and degradation rate of memory not assessed.       | Memory fidelity quantification, degradation rate, multi-state memory capacity. |
| Organizational Complexity       |         Yes               | Spatial Assortment, Polarization     | More detailed mapping of local rules to global order parameters.                  | Deeper analysis of local rule parameters and their relation to emergent order. |
| Embodied Computation            |         Yes               | Neuronal computation (inferred)      | No direct measurement of computational power or metrics.                          | Computational capacity quantification, more detailed neural modelling.        |
| Temporal Integration            |         Partial           | Reaction Time: ~0.1-0.2 s            | No explicit active inference model testing.                                      | Testable active inference metrics, prediction error reduction rate.          |
| Adaptive Plasticity             |         Yes               | Habituation-induced behavior change | Neural mechanisms of plasticity not directly investigated.                        | Neural mechanism study, plasticity characterization in more detail.           |
| Functional Universality         |        No               |              N/A                     | Functional universality is not explored. Focus on specific shoaling behavior.    | Exploration of diverse behaviors and potential functional universality.        |
| Cognitive Proximity            |         Partial           | Cognitive Proximity Score: 3         | Limited cognitive functions explored (basic adaptation, risk perception).       | Investigate higher-level cognitive functions, planning, relational cognition.   |
| Design Scalability & Robustness |         Yes               | Robustness Score: 8                 | Scalability not directly addressed.                                               | Scalability considerations for artificial material implementations.         |
| **Overall CT-GIN Readiness Score** |         |   5.33    |   |      |


### **13.2 Qualitative CT-GIN Assessment Conclusion:**

*   **Vector ID:** M13.2
*   **Vector Type:** Textual Summary
    *   Content: The analyzed paper on fish shoal behavior demonstrates emergent spatial order and adaptive plasticity driven by perceived risk, providing a biological example relevant to material intelligence. Key strengths include empirical validation of behavioral changes due to habituation, robust demonstration of emergent spatial assortment and altered interaction rules, and identification of key timescales in fish social behavior. Key limitations are the lack of quantification for energy efficiency and memory characteristics beyond behavioral observation, unclear assessment of criticality, and limited cognitive depth beyond basic adaptation and risk perception. Overall assessment: The biological system exhibits moderate CT-GIN readiness (Score 5.33), showing self-organization, adaptation, and embodied computation at a basic level, although it is far from achieving advanced cognitive functions or optimized energy utilization typical of artificial intelligent materials. Potential within CT-GIN lies in using biological examples like this to inspire design principles for distributed, self-organizing, and adaptive material systems, specifically focusing on risk-modulated interactions as a control parameter.

### **13.3 CT-GIN Refinement Directions:**

*   **Vector ID:** M13.3
*   **Vector Type:** Recommendations
    *   Content:
        *  Investigate energy efficiency of behavioral responses and metabolic costs associated with different interaction rules and spatial positions.
        *  Quantify memory fidelity and degradation rates of habituation memory in fish, beyond behavioral observation.
        *  Develop more detailed models mapping local interaction rules to global order parameters to enhance predictability and Yoneda embedding fidelity.
        *  Explore potential criticality in fish shoal dynamics and identify critical parameters.
        *  Expand the study to investigate higher-level cognitive functions in fish related to social behavior, such as social learning, communication complexity, and planning within groups.
        *  Translate the identified principles of risk-modulated interaction and self-organization into design blueprints for synthetic material systems exhibiting adaptive behavior, robust collective dynamics, and rudimentary embodied computation.
        *  Analyze scalability aspects if these biological principles were to be translated into artificial systems.

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
        | M2.1 | M2.2 | Transduction |
        | M2.2 | M2.4 | Dissipation |
        | M4.2 | M4.3 | Adjunction |
        | M7.1 | M7.2 | Monad |
        | M8.1 | M9.1 | Cognitive Mapping |

## M16: CT-GIN Template Self-Improvement Insights

*   **Vector ID:** M16
*   **Vector Type:** Feedback

### **Template Feedback:**

*    **Vector ID:** M16.1
*   **Vector Type:** Text
Provide specific, actionable feedback on the *CT-GIN template itself*, based on this analysis:
    *   **Missing Probes:** No major missing probes identified for this experimental biology paper. Perhaps adding probe related to "Sensory Modality" in M1 or M5 could be useful if analyzing systems focused on specific sensing modalities.
    *   **Unclear Definitions:** Definitions were generally clear. "Active Inference" definition in M6 requires careful nuanced interpretation for biological examples, further clarifying the *level* of "internal model" expected might be helpful (basic vs. complex predictive models).
    *   **Unclear Node/Edge Representations:** Node/edge mapping was generally good. Maybe differentiate within 'AdjunctionEdge' types (rule-to-order vs rule-to-rule). 'Monad' edge is slightly abstract, clearer biological examples for self-modification in template would be helpful.
    *   **Scoring Difficulties:** Cognitive Proximity scoring (M9.2 & M9.3) remains somewhat subjective. Providing more graded examples within Cognizance Scale rubric would be beneficial. Perhaps adding "typical examples" for each level in the scale.
    *   **Data Extraction/Output Mapping:** Data extraction was mostly straightforward. Mapping to tables and structured output worked well.
    *   **Overall Usability:** Template was generally usable and comprehensive. The structured format is beneficial.
    * **Specific Suggestions:** Add graded examples to CT-GIN Cognizance Scale rubric to reduce scoring subjectivity. Consider differentiating 'AdjunctionEdge' subtypes. Provide clearer examples for 'Monad' edges and biological self-modification. Clarify expected "internal model" complexity in 'Active Inference' definition. Consider optional probe for "Sensory Modality" in System Overview module.