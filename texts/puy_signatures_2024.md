

# Signatures of criticality in turning avalanches of schooling fish:

__Paper Type:__ Experimental

## M1: System Overview & Implementation
*   **Vector ID:** M1
*   **Vector Type:** Overview

### **1.1 System Description**

*   **Vector ID:** M1.1
*   **Vector Type:** Description
    *   Content: The system is an experimental setup to study turning avalanches in schooling fish (*Hyphessobrycon herbertaxelrodi*) in a square tank. The system consists of a school of fish (N=8, 16, 32, or 50 individuals) swimming freely in a 2D experimental tank. Fish trajectories are recorded and digitized to analyze turning behavior. The purpose is to investigate statistical properties of turning avalanches, defined by large changes in the heading direction of individuals and to identify signatures of criticality in collective motion of living systems.
    *   CT-GIN Mapping: `SystemNode` attributes: `systemType: Experimental`, `domain: Biological`, `mechanism: Collective Motion, Critical Phenomena`, `components: Fish School, Experimental Tank, Recording System, Data Analysis Software`, `purpose: Study criticality in collective animal behavior`
    *   Implicit/Explicit: Explicit
        *  Justification: The system, components and purpose are directly described in the introduction and methods sections of the excerpt.

### **1.2 Implementation Clarity**

*   **Vector ID:** M1.2
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The experimental setup, fish species, and data acquisition methods are clearly described. The definition of turning avalanches and metrics used for analysis are also provided.  Clarity is slightly reduced by the reference to Appendix A and B and Supplemental Material for full experimental details and derivations, which are not provided in the excerpt.
    *   Implicit/Explicit: Mixed
        * Justification:  The general implementation is explicit from the main text. Detailed procedures refers to external material (Appendix, Supplemental Material), hence mixed.

### **1.3 Key Parameters**

*   **Vector ID:** M1.3
*   **Vector Type:** ParameterTable
    *   Table:
        | Parameter Name | Value | Units | Source (Fig/Table/Section) | Implicit/Explicit | Data Reliability (High/Medium/Low) | Derivation Method (if Implicit) |
        | :------------- | :---: | :---: | :-----------------------: | :-----------------: | :-----------------------------: | :-------------------------------: |
        | Number of fish (N) | 8, 16, 32, 50 | individuals | Sect. II | Explicit | High | N/A |
        | Tank side (L) | 100 | cm | Sect. Appendix A | Explicit | High | N/A |
        | Water column depth | 5 | cm | Sect. Appendix A | Explicit | High | N/A |
        | Recording frame rate | 50 | frames/s | Sect. Appendix A | Explicit | High | N/A |
        | Turning threshold (ω_th) | 0.1 (e.g.) | rad/frame | Fig.2 caption, Sect III | Explicit | High | N/A |

    *   **Note:** List *up to 5* key parameters characterizing the system's *implementation*.  Provide values and units if possible. If a parameter is not explicitly stated but derived/inferred, clearly state the derivation method. *Always* include units if applicable. If a value is not applicable, write "N/A".  Data Reliability: High = Directly measured, Medium = Derived from measurements/simulations, Low = Estimated/Inferred.

## M2: Energy Flow
*   **Vector ID:** M2
*   **Vector Type:** Energy

### **2.1 Energy Input**

*   **Vector ID:** M2.1
*   **Vector Type:** Input
    *   Content: The primary energy source is the metabolic energy of the fish, derived from food consumed and processed by the fish.
    *   Value: N/A
    *   Units: N/A
    *   CT-GIN Mapping: `EnergyInputNode`: attributes - `source: Metabolic Energy (Fish Food)`, `type: Chemical`
    *   Implicit/Explicit: Implicit
        *  Justification: The energy source is not explicitly stated but it's implicitly understood that the fish are living organisms requiring metabolic energy to move.

### **2.2 Energy Transduction**

*   **Vector ID:** M2.2
*   **Vector Type:** Transduction
    *   Content: Chemical energy from metabolism is transduced into kinetic energy of the fish movement through muscular contraction. This kinetic energy facilitates swimming and turning maneuvers, which are then observed and quantified as turning avalanches. There isn't a detailed description of biomechanical energy transfer, but energy flow goes from metabolic energy to kinetic energy to behavioral patterns.
    *   CT-GIN Mapping: `EnergyTransductionEdge`: attributes - `mechanism: Biomechanical (Muscle Contraction)`, `from_node: EnergyInputNode`, `to_node: SystemNode`, `to_node_attribute: Kinetic Energy`
    *   Implicit/Explicit: Implicit
        *  Justification: Energy transduction mechanisms are not detailed, but inferred from the context of animal movement and biology. The excerpt mentions "burst-and-coast mechanism of the individuals" which points towards muscular activity and kinetic energy, thus inferred.

### **2.3 Energy Efficiency**

*   **Vector ID:** M2.3
*   **Vector Type:** Score
    *   Score: [3]
    *   Justification/Metrics: Energy efficiency of the system is likely low, typical for biological systems. No metrics are provided to quantify energy efficiency.  The system involves biological organisms and processes, which are known to be thermodynamically inefficient compared to engineered systems but robust and adaptive. Qualitative assessment is Low, due to biological nature and lack of energy optimization considerations in the study.
    *   CT-GIN Mapping: Attribute of relevant `EnergyTransductionEdge`s: `efficiency_score: 3/10`, `efficiency_assessment: Low`
    *   Implicit/Explicit: Implicit
      *  Justification: Efficiency is not discussed in the paper but qualitatively assessed as low based on general biological system characteristics and lack of efficiency metrics provided in the text.

### **2.4 Energy Dissipation**

*   **Vector ID:** M2.4
*   **Vector Type:** Dissipation
    *   Content: Energy dissipation mechanisms include hydrodynamic drag from fish moving through water, heat loss due to metabolic processes, and potentially sound generation (although not mentioned). Quantification is not provided, but dissipation is inherent to fish locomotion in a fluid environment. Qualitatively, dissipation is likely significant, especially for larger schools.
    *   CT-GIN Mapping: `EnergyDissipationNode`: attributes - `mechanism: Hydrodynamic Drag, Metabolic Heat Loss`, `dissipation_type: Heat, Kinetic`, `DissipationEdge`: attributes - `from_node: SystemNode`, `to_node: EnergyDissipationNode`
    *    Implicit/Explicit: Implicit
        *  Justification: Dissipation is not explicitly quantified or discussed in detail but its presence is implied by the nature of physical systems (fish moving in water) and fundamental thermodynamics.

## M3: Memory
*   **Vector ID:** M3
*   **Vector Type:** Memory

### **3.1 Memory Presence:**

*   **Vector ID:** M3.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: The study mentions "collective memory" in the introduction, citing reference [13]. This refers to the idea that animal groups can retain and use past information to influence current behavior, suggesting a form of memory at the collective level that influences movement patterns. The paper also discusses clustering of avalanche events over time and correlations, hinting at temporal dependencies in the system's dynamics, which could be interpreted as a form of short-term memory influencing avalanche occurrence.
    *    Implicit/Explicit: Mixed
        * Justification: The concept of "collective memory" is explicitly mentioned with citation, but the direct demonstration of memory mechanisms within the turning avalanches is implicit in the observed temporal correlations and clustering analyzed in Section VII.

### **3.2 Memory Type:**

*   **Vector ID:** M3.2
*   **Vector Type:** Score
*   Score: [4]
*   Justification: The memory type can be considered short-term and dynamic, related to the recent history of avalanche events and the internal state of the fish school influencing the likelihood of subsequent avalanches. It's not a high-fidelity, re-writable memory like in digital systems, or long-term stable memory, but a more ephemeral form of temporal dependence. The "memory" influences the *probability* of future events (aftershocks clustering) and the system’s state ("state of the school"), but its precise capacity, retention, and readout accuracy aren't quantified. Score of 4 reflects basic, short-term, dynamic influence, not sophisticated memory function.
*   CT-GIN Mapping: Defines the `MemoryNode` type: `memoryType: Short-Term Dynamic`, `memoryFidelityScore: 4/10`.
*    Implicit/Explicit: Mixed
    * Justification: Memory *presence* is hinted at explicitly through citation, but *type* and *score* are inferred from the analysis of temporal correlations ("aftershocks") and system dynamics, not explicitly quantified as memory metrics.

### **3.3 Memory Retention Time:**

*   **Vector ID:** M3.3
*   **Vector Type:** Parameter
*   Value: Short-term
*    Units: Qualitative Descriptor
*   Justification:  The paper discusses temporal correlations in avalanches over a timescale of approximately 250 frames (Fig. S6), corresponding to the "average time the school needs to perform a half-turn around the tank". This suggests a short-term memory timescale related to the immediate past history of the school's movement and avalanche events, roughly on the order of a few seconds (250 frames / 50 frames/s = 5 seconds). However, precise retention time not explicitly measured or defined.
*    Implicit/Explicit: Mixed
        * Justification: The timescale of correlation (250 frames) is explicitly mentioned in relation to aftershocks, but interpreting it as memory *retention time* and describing it qualitatively as 'short-term' is inferential.

### **3.4 Memory Capacity (Optional - if applicable)**

* **Vector ID:** M3.4
* **Vector Type:** Parameter
*  Value: N/A
*   Units: N/A
*   Justification: Memory capacity is not quantified or discussed in the paper. It is unclear how many distinct states or how much information is stored in this short-term dynamic memory.
*    Implicit/Explicit: Implicit
        *  Justification: Absent from the text thus implicit N/A.

### **3.5 Readout Accuracy (Optional - if applicable)**

* **Vector ID:** M3.5
* **Vector Type:** Parameter
*   Value: N/A
*   Units: N/A
*   Justification: Readout accuracy of memory is not assessed. It is unclear how faithfully past events are recalled or used to influence current or future avalanches.
*    Implicit/Explicit: Implicit
       *  Justification: Absent from the text thus implicit N/A.

### **3.6 Degradation Rate (Optional - if applicable)**
* **Vector ID:** M3.6
* **Vector Type:** Parameter
    *   Value: N/A
    *   Units: N/A
    *   Justification: Memory degradation rate is not quantified. The analysis suggests temporal correlations diminish over time, but rate isn't explicitly measured or defined.
    *    Implicit/Explicit: Implicit
            * Justification: Absent from the text thus implicit N/A.

### **3.7 Memory Operations Energy Cost (Optional - if applicable)**
* **Vector ID:** M3.7
* **Vector Type:** Table
*   Table:
    | Memory Operation ID | Energy Consumption per Bit | Power Usage during Operation| Units | Uncertainty | Data Source Reference | Implicit/Explicit | Justification |
    | :------------------ | :--------------------------: | :-----------------------------: | :---: |:-----------------:|:-----------------:|:-----------------:| :------------------ |
    | N/A                  | N/A                            | N/A                               | N/A   | N/A             | N/A              | Implicit        | Not discussed in the paper. |
*   Implicit/Explicit: Implicit
    *   Justification: Memory energy cost is not analyzed or mentioned. Thus implicit N/A.

### **3.8 Memory Fidelity & Robustness Metrics (Optional - if applicable)**
* **Vector ID:** M3.8
* **Vector Type:** Table
*   Table:
    | Metric ID | Description | Value | Units | CT-GIN Mapping | Data Source | Implicit/Explicit | Justification |
    | :-------- | :---------- | :----: | :---: | :-------------: | :----------: |:-----------------:| :-----------------:|
    | N/A       | N/A         | N/A   | N/A   | N/A            | N/A        | Implicit        | Not discussed in the paper. |
*   Implicit/Explicit: Implicit
*   Justification: Memory fidelity and robustness are not discussed. Thus implicit N/A.
---

## M4: Self-Organization and Emergent Order
*   **Vector ID:** M4
*   **Vector Type:** Self-Organization

### **4.1 Self-Organization Presence:**

*   **Vector ID:** M4.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: The paper investigates "spontaneous behavioral cascades" and "self-organized critical phenomena". The emergence of turning avalanches from local interactions between fish, without centralized control, fits the definition of self-organization. The power-law distributions and scale-free behavior suggest that the global pattern of avalanches arises from local dynamics and interactions within the school, rather than being pre-programmed or externally imposed order.
    *   Implicit/Explicit: Mixed
        *  Justification: "Spontaneous" and "self-organized criticality" are explicit key terms. The link between "local interactions" and "global order" in the context of avalanche emergence is implicit, but strongly suggested by the framework of criticality and collective motion.

**(Conditional: If M4.1 is "No", skip to Module 5. If "Yes", include M4.2-M4.7)**

### **4.2 Local Interaction Rules:**

*   **Vector ID:** M4.2
*   **Vector Type:** Rules
    *   Content: The local interaction rules are not explicitly defined mathematically or algorithmically in this excerpt. However, the paper implicitly describes them as based on fish responding to changes in heading direction of their neighbors ("individuals follow the behavior of others"). Specifically, an "active fish" is defined by its "turning rate ω > ω_th". Avalanches are sequences of consecutive frames where "at least one active fish" is present, implying local interactions trigger subsequent turns in other fish. The exact nature of "following" (e.g., alignment, attraction, repulsion) and the threshold for triggering a ‘large turn’ in a neighbor are not detailed in this excerpt, referencing instead model-based investigations in [27-30].
    *   CT-GIN Mapping: Part of the `AdjunctionEdge` description (local side). `AdjunctionEdge` attributes: `interactionType: Imitation/Social Influence`, `localRuleDescription: Fish react to turning rates of neighbors, active fish defined by ω > ω_th (threshold-based)`, `underlyingMechanism: Social contagion of turning behavior`
    * **Implicit/Explicit**: Mixed
        *  Justification: The general principle of "following the behavior of others" is mentioned explicitly. The operational definition of "active fish" and avalanches provides concrete rule-based elements, making it mixed. However, detailed mathematical or algorithmic formulations of these local rules are not in this excerpt, thus remain implicit, referencing external literature.

### **4.2.1 Local Interaction Parameters:**

* **Vector ID:** M4.2.1
* **Vector Type:** Table
*   Table:
    | Rule ID | Description | Parameter Name | Parameter Value Range | Units | Data Source | Implicit/Explicit | Justification |
    | :------ | :---------- | :------------- | :---------- | :---: | :----------: | :----------------: | :------------: |
    | R1      | Turning Threshold for Active Fish | Turning threshold | ω_th ∈ [0.01, 0.3] | rad/frame  | Sect. II, III | Explicit       | Range estimated for realistic avalanche definition. |
### **4.3 Global Order:**

*   **Vector ID:** M4.3
*   **Vector Type:** Order
    *   Content: The global order that emerges is scale-free avalanche dynamics, characterized by power-law distributions of avalanche duration, size, and interevent time. This scale-free behavior is interpreted as a "signature of criticality". The "turning avalanche", a large directional shift propagating across the group, represents a collective reorientation of the school’s trajectory, which is an emergent global order.
    *   CT-GIN Mapping: Defines a `ConfigurationalNode`: `configurationalType: Scale-Free Avalanche Dynamics`, `emergentOrder: Power-law distributions of avalanche metrics, collective directional shifts`, `orderParameter: Avalanche duration exponent (α), size exponent (τ), interevent time exponent (γ)`
    * **Implicit/Explicit**: Mixed
        *  Justification: The power-law distributions and scale-free behavior as "signatures of criticality" are explicitly stated as results. The interpretation of these statistical patterns as "emergent global order" and "collective reorientation", while strongly implied and discussed, and related to "collective decision-making processes", is more of an interpretation than a direct measurement of a visually observable global order parameter, thus mixed.

### **4.4 Predictability of Global Order:**

*   **Vector ID:** M4.4
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification:  The emergence of scale-free avalanche statistics is relatively predictable given the local interaction rules and system parameters (fish density, responsiveness to neighbors, etc.). Power-law exponents (α, τ, γ) are consistently observed across different school sizes (Fig. 2), indicating a degree of predictability in the statistical properties of the emergent order. Data collapses (Fig. 3) further support the predictability of distributions under certain conditions (fixed activity rate). However, individual avalanche events remain stochastic and their exact timing and size unpredictable outside of a statistical sense, hence score of 7 reflecting statistical predictability of global order, not deterministic prediction of individual events.
    * **Implicit/Explicit**: Mixed
    *  Justification: The repeatability of power-law exponents and data collapses across different N values supports predictability, making it explicit to a certain extent in terms of statistical properties. However, predictability of *individual* avalanche events is not addressed or quantified, and remains within stochastic dynamics, thus mixed.
    *   CT-GIN Mapping: Contributes to the `AdjunctionEdge` weight: `globalOrderPredictabilityScore: 7/10`, `predictabilityMetrics: Power-law exponents (α, τ, γ) consistency across N, data collapse (Fig. 3)`

### **4.5. Local Interaction Rules (for Self-Organization)**
* **Vector ID:** M4.5
* **Vector Type:** Table
*   Table:
| Rule ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Source |
| :------ | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :-----: |
| N/A         | N/A        | N/A      | N/A         | N/A   | Implicit         | Not explicitly quantified in detail, only qualitatively described. | N/A    |

### **4.6. Globally Emergent Order and Order Parameters**
* **Vector ID:** M4.6
* **Vector Type:** Table
*   Table:
| Property ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Protocol | Source |
| :---------- | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :------: | :-----: |
| P1          | Duration distribution exponent | α | 2.4 ± 0.2 | N/A  | Explicit       |  Fig 2(a), Sect III | Linear regression | Fig 2(a) |
| P2          | Size distribution exponent | τ | 1.97 ± 0.14 | N/A  | Explicit       | Fig 2(b), Sect III | Linear regression | Fig 2(b) |
| P3          | Time interval distribution exponent | γ | 1.62 ± 0.08 | N/A  | Explicit       | Fig 2(d), Sect III | Linear regression | Fig 2(d) |
| P4          | Duration-size scaling exponent | m | 1.41 ± 0.06 | N/A  | Explicit       | Fig 2(c), Sect III | Linear regression | Fig 2(c) |

### **4.7 Yoneda Embedding and Local-to-Global Mapping Fidelity**

*   **Vector ID:** M4.7
*   **Vector Type:** Table
*   Table:
    | Link Type | Description | Predictability | Yoneda Score | Metrics | Implicit/Explicit | Justification | Source |
    | :-------- | :---------- | :------------- | :----------- | :------ | :----------------: | :------------: | :-----: |
     | Local Rules -> Global Order | Mapping from local fish interaction rules to scale-free avalanche dynamics.  | Medium | 6 | Power law exponents, data collapse | Mixed | Statistical properties (power laws) are somewhat predictable but individual avalanche events are not. Yoneda score reflects moderate fidelity due to statistical link, not deterministic. | Sect. III, IV |
    *   **Yoneda Embedding Fulfillment Score [0-10]:** [**Rubric for assessing score and specific examples for different score levels.** Higher scores indicate more deterministic and direct mapping fidelity. **0-2**: No discernible link. Random global order. **3-5**: Weak statistical correlation, limited predictability. **6-8**: Statistically robust mapping, moderate predictability.  **9-10**:  Near-deterministic mapping, high predictability of global order from local rules.  Score 6 here represents statistically significant linkage, but not complete predictability of global order from local rules.]
    *   **Metrics:**  [**Metrics used to assess predictability and Yoneda embedding fulfillment:** Consistency of power-law exponents (α, τ, γ) across different school sizes, data collapse observed in distributions (duration, interevent time), scaling relation between duration and size (m exponent).]
    *   **Justification:** The link between local fish interactions (following neighbors, turning rate thresholds) and the global scale-free avalanche statistics is statistically robust, and quantifiable by consistent power-law exponents and observed data collapses. However, the exact timing and size of individual avalanche events remain stochastic and not deterministically predictable from local rules alone, thus a moderate Yoneda score of 6. The mapping fidelity is statistical, not a precise, one-to-one mapping for each individual event, reflecting complexity in the system.

## M5: Computation
*   **Vector ID:** M5
*   **Vector Type:** Computation

### **5.1 Embodied Computation Presence:**

*   **Vector ID:** M5.1
*   **Vector Type:** Binary
    *   Content: [Partial]
    *   Justification: The fish school system exhibits aspects of embodied computation in the sense that collective decision-making for directional changes ("collective decision-making processes in selecting a new movement direction") emerges from the physical interactions of individual fish. The propagation of turning avalanches can be seen as a distributed process of information transfer and potentially rudimentary "computation" performed by the school as a whole to achieve group-level behavioral changes (reorientation). However, it's not computation in a programmable or explicitly defined algorithmic sense. "Computation" here is an emergent property of the collective movement and social interactions, implicitly performing a form of distributed decision-making regarding group direction but no well-defined computational algorithm in the material itself. Score 'Partial' reflects this implicit, emergent, and rudimentary form of computation, not programmable or general-purpose.
    *    Implicit/Explicit: Mixed
        *  Justification: "Collective decision-making" and "information transfer" are explicitly mentioned in relation to turning avalanches suggesting a form of computation. However, 'embodied computation' as a specific, programmable function is not explicitly stated.  Interpretation as rudimentary computation in biological sense is implicit. Score 'Partial' and Justification is Mixed.

**(Conditional: If M5.1 is "No", skip to Module 6. If "Yes", include M5.2-5.4)**

### **5.2 Computation Type:**

*   **Vector ID:** M5.2
*   **Vector Type:** Classification
    *   Content: [Analog/Neuromorphic/Reservoir Computing/Other: Distributed Social Information Processing] Other: Distributed Social Information Processing. The computation is not digital, analog in direct signal processing sense or neuromorphic in sense of predefined neural network architecture, or reservoir computing. It is more akin to a distributed social information processing system, where 'computation' emerges from interactions and information flow within a social group, leading to collective behavioral outputs (directional changes). The "computation" is in the form of distributed, parallel processing of social cues (turning of neighbors), leading to emergent group decisions.
    *   CT-GIN Mapping: Defines the `ComputationNode` type: `computationType: Distributed Social Information Processing`
    *    Implicit/Explicit: Mixed
    *    Justification: 'Distributed' nature and connection to 'information processing' and 'decision-making' are implied and partly explicit through terminology. The classification as "Distributed Social Information Processing", and deviation from typical computation types (analog, digital, neuromorphic), requires interpretation and is therefore mixed.

### **5.3 Computational Primitive:**

*   **Vector ID:** M5.3
*   **Vector Type:** Function
    *   Content: Thresholding/Propagation/Aggregation. The basic computational primitive is somewhat like a thresholding and propagation mechanism. Individuals react if turning rate of neighbours exceeds a threshold (ω_th), and this "activation" propagates through the school as an avalanche. Aggregation is also present, as individual turns contribute to a collective directional shift. It is not a single, well-defined mathematical function but a combination of threshold-based activation of individual responses, propagation of activity through social interactions, and aggregation of individual behaviors into a collective output (directional change). Sub-Type: Thresholding (turning rate ω > ω_th), Propagation (avalanche cascade), Aggregation (collective direction shift).
    *   CT-GIN Mapping: Defines the primary function of the `ComputationNode`: `primitiveFunction: Thresholding & Propagation & Aggregation`, `functionSubtype: Thresholding (turning rate), Propagation (social cascade), Aggregation (collective direction)`
    *   Implicit/Explicit: Mixed
    * Justification: 'Threshold' for "active fish" is explicit. "Propagation" of avalanches is explicit term. "Aggregation" implied by collective reorientation. Combining as primitives "Thresholding/Propagation/Aggregation" requires interpretation and synthesis, thus Mixed.

### **5.4 Embodied Computational Units**
* **Vector ID:** M5.4
* **Vector Type:** Table
*   Table:
| Unit ID | Description | Processing Power | Energy/Operation | Freq/Resp. Time | Bit-Depth | Data Source | Implicit/Explicit | Justification |
| :------ | :---------- | :--------------- | :--------------- | :--------------: | :-------: | :----------: |:-----------------:| :-----------------:|
| U1      | Individual Fish | N/A            | Low (Metabolic) | ~50 frames/s (recording) | Analog (heading direction) | Sect II           | Implicit/Mixed    | Processing power, energy, bit-depth are not quantified but inferred qualitatively. Frame rate is from recording parameters. |

## M6: Temporal Dynamics
*   **Vector ID:** M6
*   **Vector Type:** Temporal

### **6.1 Timescales:**

*   **Vector ID:** M6.1
*   **Vector Type:** ParameterTable
    *   Table:
        | Timescale Description | Value | Units | Source | Implicit/Explicit | Justification |
        | :-------------------- | :---: | :---: | :----: | :----------------: | :------------: |
        | Recording frame interval | 0.02 | s | Appendix A | Explicit |  1/50 frames/s |
        | Avalanche duration (T) | ~1-100 | frames | Fig. 2(a) | Explicit | Range from PDF of avalanche duration. |
        | Avalanche interevent time (t_i) | ~1-100 | frames | Fig. 2(d) | Explicit | Range from PDF of interevent time.  |
        | Correlation timescale (aftershocks) | ~250 | frames | Sect. VII | Explicit | First maximum of MSD of center of mass from Fig. S6 |
    *   **Note:** Identify and quantify the *relevant timescales* of the system's dynamics (e.g., response time, process duration, oscillation period, memory decay, adaptation/learning timescale, self-assembly timescale). Use consistent units (e.g., seconds, milliseconds) for comparability.

### **6.2 Active Inference:**

*   **Vector ID:** M6.2
*   **Vector Type:** Assessment
    *   Content: [Unclear] *Active Inference*: It is unclear if the fish system exhibits active inference in a strict sense. While fish respond to environmental cues (tank walls), and there's collective decision-making, the paper doesn't explicitly demonstrate prediction of future states, action selection to minimize prediction error, or internal models. The "burst-and-coast" mechanism and relation of avalanches to minima of center-of-mass speed (Fig 5(c)) suggest some anticipatory behavior (decision making at onset of active phase), but it's not formalized as active inference or explicitly validated as minimizing surprise or prediction error. "Unclear" reflects lack of direct evidence or analysis related to active inference framework in this excerpt.
    *   Justification: Active inference framework not explicitly discussed or tested in the paper. No direct evidence for prediction error minimization or internal models provided. Behavior is described as response to current stimuli and exhibiting criticality, not framed in active inference terms.
    *   Implicit/Explicit: Implicit
        *  Justification: Active Inference is not mentioned or analyzed in the text. Thus, implicit.
    *   **If Yes/Partial, provide examples of testable CT-GIN metrics that *could* be used to quantify active inference:** [N/A]

## M7: Adaptation
*   **Vector ID:** M7
*   **Vector Type:** Adaptation

### **7.1 Adaptive Plasticity Presence:**

*   **Vector ID:** M7.1
*   **Vector Type:** Binary
    *   Content: [No] *Adaptive Plasticity*:  The paper primarily focuses on static statistical properties (power laws) of turning avalanches and their dependence on school size and turning threshold, analyzing recordings under constant experimental conditions. There's no evidence presented for *changes in behavior or internal structure* over time in response to experience or learning within the time frame of the experiments described. The system is analyzed in a stationary state, assessing criticality signatures. 'No' reflects lack of demonstrated adaptive plasticity – persistent change in behavior or structure due to experience – in the context of this study.
    *   Justification: The study investigates stationary statistical properties, not changes in behavior or structure over time due to experience. Adaptive plasticity mechanisms are not discussed or tested. Focus is on criticality signatures irrespective of adaptation or learning.
    *    Implicit/Explicit: Explicit
        * Justification:  Adaptation mechanisms are absent from the described experimental analysis and focus of the study.  Thus explicit negative.

**(Conditional: If M7.1 is "No", skip to Module 8. If "Yes", include M7.2)**

### **7.2 Adaptation Mechanism:**

*   **Vector ID:** M7.2
*   **Vector Type:** Description
    *   Content: N/A
    *   CT-GIN Mapping: N/A
    *    Implicit/Explicit: Implicit
        *  Justification:  Adaptation absent, therefore N/A.

## M8: Emergent Behaviors
*   **Vector ID:** M8
*   **Vector Type:** Behavior

### **8.1 Behavior Description:**

*   **Vector ID:** M8.1
*   **Vector Type:** Description
    *   Content: The main functional behavior is the emergence of scale-free turning avalanches in schooling fish, characterized by power-law distributions in avalanche duration, size, and interevent time. This emergent behavior reflects collective directional changes and reorientations of the school, arising spontaneously from local social interactions, and indicative of operation near a critical point. "Turning avalanche activity" and its statistical properties (power laws, data collapses, scaling exponents) are the key observable behaviors the system displays.
    *   CT-GIN Mapping: Defines the `BehaviorArchetypeNode`. `behaviorType: Emergent Scale-Free Turning Avalanches`, `observableBehavior: Power-law distributions of avalanche duration, size, interevent time, data collapses, scaling exponents`
    *    Implicit/Explicit: Explicit
       *  Justification: "Turning avalanches", "scale-free behavior", "power laws" and associated metrics are explicitly described as the focus of the study and observed behaviors.

### **8.2 Behavior Robustness:**

*   **Vector ID:** M8.2
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The scale-free avalanche behavior appears relatively robust to variations in school size (N=8 to 50) and turning threshold (ω_th), as power-law exponents are similar and data collapses observed across these parameter ranges (Figs. 2, 3, S1). This suggests some degree of robustness in the emergent behavior to changes in system parameters. However, fragility is introduced by tank walls, which distort avalanche statistics ("dragon kings", shoulders in tails), indicating limits to robustness against boundary perturbations. Score reflects moderate robustness to parameter variation but sensitivity to boundary conditions.
    *   Implicit/Explicit: Mixed
        *  Justification: Robustness shown by similar power laws and data collapse across different N and ω_th values, explicitly demonstrated in figures, strengthening 'robustness'. 'Fragility' due to tank walls and dragon kings is also explicitly observed and discussed. Score reflecting moderate is mixed inference.
    *   CT-GIN Mapping: This score contributes to the reliability attributes of the `BehaviorArchetypeNode`: `behaviorRobustnessScore: 7/10`, `robustnessAgainst: Parameter Variation (N,  ω_th)`, `fragilityAgainst: Boundary Perturbations (tank walls)`

### **8.3 CT-GIN Emergent Behavior Validation**

*    **Vector ID:** M8.3
*    **Vector Type:** Validation
     *  Content: Validation methods include statistical analysis of avalanche metrics (duration, size, interevent time distributions), data collapses, scaling relationships, and comparison with theoretical predictions from criticality. Control "randomized avalanches" used as contour plot in Fig. 7(b) for correlation analysis. Robustness shown by consistency of power-law exponents across school sizes and thresholds. Limitations: finite size effects, tank wall influences distorting statistics, experimental setup limits to small group sizes (N<=50). Figures 1-7, Sections III, IV, VII.
     *   Implicit/Explicit: Explicit
    *   Justification: Validation methods are explicitly described and demonstrated in Results sections and figures. Control comparison with randomized data is explicit visual control.  Limitations are also discussed, especially in Sect. V.

## M9: Cognitive Proximity
*   **Vector ID:** M9
*   **Vector Type:** Cognition

### **9.1 Cognitive Mapping:**

*   **Vector ID:** M9.1
*   **Vector Type:** Description
    *   Content: The paper draws analogies between turning avalanches in fish schools and "behavioral cascades" and "information transfer" seen in other animal groups (honeybees, birds, monkeys, humans). It links turning avalanches to "collective decision-making processes" suggesting a cognitive function in coordinating group movement and direction. The concept of "criticality" itself, borrowed from statistical physics, is mapped metaphorically to advantages in "signal detection, storing, and processing" in biological systems (Introduction, ref. [4-6]). Analogies to "aftershocks" from seismology for temporal correlations are also used, but primarily for analytical framework, not cognitive mapping. Overall, mapping is metaphorical, suggesting parallels in information processing & collective decisions, not claiming direct cognitive equivalence.
    *   CT-GIN Mapping: `CognitiveMappingEdge`: `sourceNode: BehaviorArchetypeNode`, `targetNode: CognitiveFunctionNode`, `mappingType: Metaphorical Analogy`, `analogyDescription: Turning Avalanches <-> Collective Decision-Making, Criticality <-> Information Processing Advantages, Aftershocks <-> Temporal Correlations`, `mappingLimitations: Metaphorical, not direct cognitive equivalence`
    *   Implicit/Explicit: Mixed
    * Justification: Analogies to "collective decision-making" and "information transfer" are explicitly stated, as is link to "criticality" and "information processing advantages". The mapping is explicitly framed as analogies, not direct cognitive equivalence. Thus, Mixed.

### **9.2 Cognitive Proximity Score:**

*   **Vector ID:** M9.2
*   **Vector Type:** Score
    *   Score: [3]
    *   Justification: The system exhibits responsiveness (Level 1) in its collective directional changes triggered by local interactions. It shows some form of sub-organismal responsivity (Level 2) in terms of avalanche dynamics that are statistically patterned and robust to parameter changes. There are hints towards Reactive/Adaptive Autonomy (Level 3) in the sense that the school adapts its direction collectively through avalanches, possibly in response to environmental context (tank walls), and showing burst-and-coast decision minima but it’s rudimentary, not well-defined goal directedness or internal models (Level 4+). Score of 3 reflects proximity to Reactive/Adaptive Autonomy but far from goal-directed or model-based cognition.
    *   Implicit/Explicit: Mixed
    *  Justification: Responsivity in collective direction change (Level 1, 2) is explicit observation. Hints towards Adaptive Autonomy (Level 3) are implied in relation to burst-and-coast, tank walls, and "decision-making", but remain inferential, not explicitly demonstrated or at Level 4+ of model-based cognition. Thus, Mixed.

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
    | Sensing/Perception               |      4       | Perceive neighbors' turning via visual or hydrodynamic cues. Basic social sensing.      | `CognitiveFunctionNode: Sensing/Perception`                     | Implicit        | Inferred from social behavior context. |
    | Memory (Short-Term/Working)        |      3       | Short-term temporal correlations in avalanche events, limited retention.               | `CognitiveFunctionNode: Memory (Short-Term)`                      | Mixed           |  Implied by temporal correlations, limited evidence. |
    | Memory (Long-Term)                 |      0       | No evidence of long-term memory or persistent changes due to experience in excerpt.   | N/A                                   | Explicit        | Absent from study. |
    | Learning/Adaptation              |      1       | No clear indication of learning or adaptive plasticity mechanisms, fixed behaviors studied. | N/A                                   | Explicit        | No evidence for learning or adaptation mechanisms. |
    | Decision-Making/Planning          |      3       | Collective directional changes hint at group-level "decision", rudimentary planning. | `CognitiveFunctionNode: Decision-Making`                         | Mixed           | Inferred from collective behavior, limited explicit evidence. |
    | Communication/Social Interaction |      6       | Social interactions drive avalanche propagation, information transfer within group. | `CognitiveFunctionNode: Communication/Social Interaction`         | Explicit        | Explicitly discussed in relation to avalanche propagation. |
    | Goal-Directed Behavior            |      2       | Collective directional shifts, but no specific, measurable goals defined or demonstrated. | `CognitiveFunctionNode: Goal-Directed Behavior`                 | Implicit        | Inferred from directional movement, lack of specific goals. |
    | Model-Based Reasoning              |      0       | No evidence of internal models or model-based reasoning in avalanche behavior.        | N/A                                   | Explicit        | Absent from study. |
    | **Overall score**                 |      [2.4]       |                                                                                       |                                   |                     |                |

    *   **Note:** Assess the system for *each* function, providing a score (0-10) and a short (1-2 sentences) justification.  0 = Absent, 10 = Human-level performance.

## M10: Criticality Assessment
*   **Vector ID:** M10
*   **Vector Type:** Criticality

### **10.1 Criticality:**

*   **Vector ID:** M10.1
*   **Vector Type:** Assessment
    *   Content: [Yes] Does the system operate near a critical point, displaying scale-free behavior, power laws, or long-range correlations? Yes. The paper explicitly investigates "signatures of criticality" in turning avalanches, and finds "power-law distributions and robust scale-free behavior". Data collapses and scaling relationships are also confirmed. Temporal correlations ("aftershocks") are explored. Authors conclude results "strongly suggest the presence of a scale-free avalanche dynamics, which could be compatible with the school operating in the vicinity of a critical point."
    *   Justification: The entire study is designed to test for criticality, and the core findings explicitly support scale-free behavior and potential criticality.
        *   Critical Parameters (If Yes/Partial): Turning rate threshold (ω_th), Activity rate (r).
        *   Evidence: Power-law distributions for avalanche duration, size, and interevent time (Fig. 2). Data collapses (Fig. 3). Scaling relationship between avalanche size and duration (Fig. 2(c)). Omori law for aftershocks (Fig. 7(c)). "Our results identify power-law distributions and robust scale-free behavior through data collapses and scaling relationships, confirming a necessary condition for criticality in fish schools." (Abstract).
    *   Implicit/Explicit: Explicit
    *    Justification: Criticality and scale-free behaviour are central and explicit claims, supported by explicit evidence from figures and the abstract.

## M11: Review Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Review")**

*   **Vector ID:** M11
*   **Vector Type:** Review

### **11.1 Literature Synthesis Quality:**

*   **Vector ID:** M11.1
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification: N/A
    *    Implicit/Explicit: Implicit
         *  Justification: Paper is not a review.

### **11.2 Gap Identification:**

*   **Vector ID:** M11.2
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification: N/A
    *   Implicit/Explicit: Implicit
        *  Justification: Paper is not a review.

### **11.3 Future Directions:**

*   **Vector ID:** M11.3
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification: N/A
    *    Implicit/Explicit: Implicit
    *   Justification: Paper is not a review.

### **11.4 Review Paper CT-GIN Alignment Score**

*   **Vector ID:** M11.4
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification: N/A
    *    Implicit/Explicit: Implicit
        *  Justification: Paper is not a review.

## M12: Theoretical Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Theoretical")**

*   **Vector ID:** M12
*   **Vector Type:** Theory

### **12.1 Theoretical Rigor:**

*   **Vector ID:** M12.1
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification: N/A
       * Implicit/Explicit: Implicit
       *  Justification: Paper is not theoretical.

### **12.2 Realization Potential:**

*   **Vector ID:** M12.2
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification: N/A
    *   Implicit/Explicit: Implicit
    *  Justification: Paper is experimental.

### **12.3 Potential for Future CT-GIN Implementation Score**

* **Vector ID:** M12.3
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification:  N/A
    *    Implicit/Explicit: Implicit
    *   Justification: Paper is experimental.

## M13: Overall Assessment & Scoring

*   **Vector ID:** M13
*   **Vector Type:** Overall

### **13.1 CT-GIN Readiness Score:**

*   **Vector ID:** M13.1
*   **Vector Type:** Score
*   **Calculated Score:** [5.2]  (Average of scores from Modules 1-4, M8.2 and M9.2, scores with N/A convert in 0).  *This score MUST be automatically calculated. Only Number.*

**CT-GIN Readiness Summary Table:**

| CT-GIN Aspect                   | Strength (Yes/Partial/No) | Key Supporting Metrics (with units) | Limitations (Missing Metrics/Data Gaps)                                           | Improvement Areas (Future Research)                                          |
| :------------------------------ | :-----------------------: | :-----------------------------------| :------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| Energy Flow Efficiency          | No                        | N/A                                 | No specific energy efficiency metrics or quantification.                         | Investigate energy budget and efficiency of collective motion.                 |
| Memory Fidelity                 | Partial                   | Short-term temporal correlations       | No quantification of memory capacity, readout accuracy, degradation rate.       | Quantify memory properties (retention, capacity, fidelity).                 |
| Organizational Complexity       | Yes                       | Scale-free avalanche distributions, data collapse | Influence of tank walls, finite size effects limit ideal scale-free behavior.    | Larger system sizes, minimize boundary effects.                               |
| Embodied Computation            | Partial                   | Emergent collective direction shift  | Rudimentary computation, not programmable algorithms.                              | Define and test specific embodied computations.                               |
| Temporal Integration            | Yes                       | Timescales of avalanches, aftershocks (frames, seconds) | Precise timescale metrics for memory and adaptation lacking.                | Quantify temporal integration more precisely.                                 |
| Adaptive Plasticity             | No                        | N/A                               | No evidence of adaptation or learning within experimental timeframe.         | Study adaptive responses of schooling behavior to changing environments.       |
| Functional Universality         | No                        | N/A                                 | Behavior limited to collective motion and turning avalanches.                    | Explore functional versatility beyond turning avalanches.                      |
| Cognitive Proximity            | Partial                  | Analogies to collective decision-making | Mapping is metaphorical, not direct cognitive equivalence.                      | Investigate deeper cognitive mappings and validate them experimentally.       |
| Design Scalability & Robustness | Partial                  | Robustness to parameter variation (N, ω_th) | Fragility to boundary conditions (tank walls), limited system size.            | Improve robustness, scalability to larger systems.                            |
| **Overall CT-GIN Readiness Score** |        Partial         |   Power-law exponents, data collapse, timescales  | Missing metrics for energy, memory, limited proof of complex cognition and adaptation.      |      Quantification of missing metrics, deeper cognitive validation, adaptation studies.                               |


### **13.2 Qualitative CT-GIN Assessment Conclusion:**

*   **Vector ID:** M13.2
*   **Vector Type:** Textual Summary
    *   Content: This experimental paper provides evidence for emergent scale-free behavior in schooling fish, manifesting as turning avalanches. Key strengths include robust demonstration of criticality signatures through power-law distributions, data collapses, and scaling relationships. The system showcases self-organization in collective motion and rudimentary embodied computation in directional changes. Key limitations are the lack of focus on energy efficiency, limited characterization of memory, and absence of demonstrable adaptive plasticity. Cognitive proximity remains low, with metaphorical mappings to decision-making but no deep cognitive function validation. Overall, the system demonstrates potential for CT-GIN framework by exhibiting emergent order from local interactions and scale-free dynamics, but further research is needed to enhance memory, efficiency, adaptive capabilities, and cognitive functions to progress towards more complex cognizant matter.

### **13.3 CT-GIN Refinement Directions:**

*   **Vector ID:** M13.3
*   **Vector Type:** Recommendations
    *   *   **Quantify Energy Flow:** Investigate and quantify energy input, transduction, and dissipation in fish schooling and avalanche dynamics to assess energy efficiency and constraints.
    *   **Characterize Memory:** Design experiments to directly measure memory retention time, capacity, readout accuracy, and degradation rate in the fish school system related to turning decisions.
    *   **Explore Adaptive Plasticity:** Study how fish schools adapt their turning avalanche behavior in response to changing environmental conditions, learning, or external stimuli over time, demonstrating genuine adaptive plasticity.
    *   **Validate Cognitive Functions:** Move beyond metaphorical mappings to cognitive functions and design experiments to test specific cognitive capacities (e.g., goal-directed behavior, planning, learning rules, social communication).

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
        | M4.2 | M4.3 | Adjunction |
        | M4.2 | M4.4 | Adjunction |
        | M4.3 | M8.1 | Transition |
        | M9.1 | M9.2 | Cognitive Mapping |
        | M8.1 | M9.1 | Cognitive Mapping |

## M16: CT-GIN Template Self-Improvement Insights

*   **Vector ID:** M16
*   **Vector Type:** Feedback

### **Template Feedback:**

*    **Vector ID:** M16.1
*   **Vector Type:** Text
Provide specific, actionable feedback on the *CT-GIN template itself*, based on this analysis:
    *   **Missing Probes:** None significantly missing for this paper type, but more detailed probes for computational primitives and embodied computation types could be beneficial for systems with clearer computational architectures. For adaptive systems, more granular probes for adaptation mechanisms (e.g. types of learning, reward signals) would be useful.
    *   **Unclear Definitions:** The definition of "Embodied Computation" could be slightly clarified to distinguish between implicit, emergent forms and more explicit, programmable types. The distinction used in the response (Distributed Social Information Processing) highlights the need for broader category in computation types beyond standard analog/digital/neuromorphic.
    *   **Unclear Node/Edge Representations:** The guidance for CT-GIN mapping was sufficient.  Perhaps more examples of mapping complex behaviors or abstract concepts to Nodes/Edges would be helpful in a general template guide.
    *   **Scoring Difficulties:**  Cognitive Proximity Score is subjective and requires careful consideration of the Cognizance Scale. Providing more concrete examples for each level in the scale related to material intelligence could improve consistency and reduce subjectivity.
    *   **Data Extraction/Output Mapping:** Data extraction and mapping to the template was relatively straightforward for this experimental paper due to the well-structured and quantitative nature of the results. For more descriptive or qualitative papers, extraction and quantification might be more challenging, requiring template to consider qualitative data and more flexible response formats in some sections (Text responses are already quite flexible).
    *   **Overall Usability:** The template was generally usable and well-structured, facilitating a detailed analysis of the paper within the CT-GIN framework. The modular design and clear probe questions were helpful.
    * **Specific Suggestions:**
        * For M5 (Computation): Add subtypes/examples for "Other" computation types beyond analog/digital/neuromorphic to accommodate more diverse forms of embodied computation (like 'Distributed Social Information Processing').
        * For M7 (Adaptation): Add probes to identify specific types of learning mechanisms (e.g., Reinforcement Learning, Hebbian Learning etc.) when adaptation is present, potentially linking to CT-GIN's Monad framework more directly.
        * For M9.2 (Cognitive Proximity Score): Create a more detailed rubric for scoring cognitive proximity, possibly with examples of material intelligence systems at each level to reduce subjectivity and increase inter-rater reliability.
        * Consider adding a "Reliability" Module to explicitly assess system reliability, robustness, and failure modes, integrating with and expanding on M8.2 (Behavior Robustness).
