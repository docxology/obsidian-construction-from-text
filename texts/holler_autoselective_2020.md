# Autoselective transport of mammalian cells with a chemotactic droplet

__Paper Type:__ Experimental

## M1: System Overview & Implementation
*   **Vector ID:** M1
*   **Vector Type:** Overview

### **1.1 System Description**

*   **Vector ID:** M1.1
*   **Vector Type:** Description
    *   Content: The system is a droplet-based chemotactic transport system for mammalian cells. It uses a 1-decanol droplet as a transporter and alginate capsules to encapsulate mammalian cells (H460, H1299, A549, HEK293T, HS68). The droplet moves directionally in a chemical gradient (NaCl), driven by Marangoni flow due to surface tension imbalance. Selectivity arises from biosurfactants produced by living lung cancer cell lines (H460, H1299, A549) when encapsulated in hydrogel capsules. These surfactants modify the hydrogel surface, enabling droplet adhesion and supporting chemotaxis. The purpose is to selectively transport living cells and potentially distinguish cell types based on biosurfactant production. Components include: 1-decanol droplet, alginate hydrogel capsules, mammalian cells, DMEM growth media, NaCl salt gradient, surfactants (biosurfactants from cells and potentially decanoate in controls).
    *   CT-GIN Mapping: `SystemNode` attributes: `systemType: Droplet-based Chemotactic Transport`, `domain: Biological Cell Transport`, `mechanism: Marangoni Chemotaxis, Biosurfactant Mediated Adhesion`, `components: Decanol droplet, Alginate capsules, Mammalian cells, NaCl, Biosurfactants`, `purpose: Selective cell transport, Cell type differentiation`
    *   Implicit/Explicit: Mixed
        *  Justification: The system components, purpose, and function are explicitly described in the abstract, introduction, results, and methods sections. The underlying mechanism is implicitly described drawing from known Marangoni effect and chemotaxis principles, and explicitly referencing surfactant role. The CT-GIN mapping is inferred based on the system description.

### **1.2 Implementation Clarity**

*   **Vector ID:** M1.2
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The implementation is well-described, with detailed methods for cell encapsulation, droplet preparation, chemotaxis setup, and viability assays. Figures and supplementary movies further clarify the setup and the transport process. The roles of each component and the experimental procedure are detailed. Clarity could be increased with more precise quantification of surfactant concentration and surface tension dynamics during transport.
    *   Implicit/Explicit: Mixed
        * Justification: The overall implementation is clearly described explicitly in the methods and result section and supported by figures and supplementary materials.  Some details, such as real-time surfactant concentration at the droplet interface, are implicit, but the crucial steps are explicitly stated.

### **1.3 Key Parameters**

*   **Vector ID:** M1.3
*   **Vector Type:** ParameterTable
    *   Table:
        | Parameter Name | Value | Units | Source (Fig/Table/Section) | Implicit/Explicit | Data Reliability (High/Medium/Low) | Derivation Method (if Implicit) |
        | :------------- | :---: | :---: | :-----------------------: | :-----------------: | :-----------------------------: | :-------------------------------: |
        | Capsule Diameter | 2.5 - 3 | mm | Results | Explicit | High | N/A |
        | Capsule Weight | 15.7 ± 0.6 | mg | Results | Explicit | High | N/A |
        | Capsule Volume | ~15 | µl | Results | Explicit | Medium | Approximated from weight and density, and volume replicates (10 capsules). |
        | Decanol Droplet Volume | 20, 250 | µl | Methods, Transport and cell viability assessment; Chemotaxis feasibility and autoselectivity. | Explicit | High | N/A |
        | NaCl Concentration Gradient | 3 | M | Results, Methods | Explicit | High | N/A |

    *   **Note:** List *up to 5* key parameters characterizing the system's *implementation*.  Provide values and units if possible. If a parameter is not explicitly stated but derived/inferred, clearly state the derivation method. *Always* include units if applicable. If a value is not applicable, write "N/A".  Data Reliability: High = Directly measured, Medium = Derived from measurements/simulations, Low = Estimated/Inferred.

## M2: Energy Flow
*   **Vector ID:** M2
*   **Vector Type:** Energy

### **2.1 Energy Input**

*   **Vector ID:** M2.1
*   **Vector Type:** Input
    *   Content: The primary energy input is chemical potential energy stored in the NaCl salt gradient.
    *   Value: N/A
    *   Units: N/A
    *   CT-GIN Mapping: `EnergyInputNode`: attributes - `source: NaCl salt gradient`, `type: Chemical Potential`
    *   Implicit/Explicit: Implicit
        *  Justification:  While the paper mentions adding NaCl to create a chemical gradient, the explicit characterization of the "energy input" as chemical potential is implicit, inferred from the principles of chemotaxis and diffusion driven processes.

### **2.2 Energy Transduction**

*   **Vector ID:** M2.2
*   **Vector Type:** Transduction
    *   Content: The chemical potential energy of the NaCl gradient is transduced into kinetic energy of the decanol droplet movement. The salt gradient creates a surface tension gradient across the droplet due to the surfactant at the interface (biosurfactants or decanoate). This surface tension imbalance leads to Marangoni flow within and around the droplet, resulting in directional droplet motion towards the higher salt concentration. The biosurfactants produced by the cells play a crucial role in establishing and maintaining the interface needed for this transduction.
    *   CT-GIN Mapping: `EnergyTransductionEdge`: attributes - `mechanism: Marangoni effect`, `from_node: Chemical Potential Energy (NaCl gradient)`, `to_node: Kinetic Energy (Droplet Motion)`
    *   Implicit/Explicit: Mixed
        *  Justification: The Marangoni effect is described as the mechanism of droplet motion, which is explicitly mentioned in the introduction and discussion. The role of surfactant and surface tension gradients is also explicitly described. The energy transduction process is described implicitly, based on physics principles of Marangoni effect in the context of chemotaxis.

### **2.3 Energy Efficiency**

*   **Vector ID:** M2.3
*   **Vector Type:** Score
    *   Score: [3]
    *   Justification/Metrics: Energy efficiency is likely low but not explicitly quantified. Marangoni effect based systems are generally not highly energy efficient. Most of the chemical potential energy is dissipated through diffusion and mixing of NaCl in the aqueous phase, and viscous drag from the droplet motion. Only a small fraction of the initial chemical potential is converted into the directed motion of the droplet and the transport of capsules. No quantitative data is provided to assess efficiency. Qualitative Assessment: Low.
    *   CT-GIN Mapping: Attribute of `EnergyTransductionEdge`s: `efficiency: Low`
    *   Implicit/Explicit: Implicit
      *  Justification: Efficiency is not quantified or discussed in the paper. Score is inferred based on general understanding of Marangoni driven systems and lack of energy recovery mechanisms.

### **2.4 Energy Dissipation**

*   **Vector ID:** M2.4
*   **Vector Type:** Dissipation
    *   Content: Energy dissipation mechanisms include:
        1.  **Diffusion of NaCl:** The salt gradient dissipates as NaCl diffuses into the aqueous phase, reducing the chemical potential gradient. Quantification is not provided but is a major dissipation factor.
        2.  **Viscous Drag:** The motion of the decanol droplet through the aqueous phase generates viscous drag, dissipating kinetic energy as heat. Quantification is not provided.
        3.  **Interfacial Dissipation:** Energy may be dissipated at the droplet-aqueous phase interface due to surfactant dynamics and mixing. Quantification is not provided.
        4. **Heat loss**: General thermal dissipation to the environment is implicit but not quantified.
    Qualitative Assessment: Energy dissipation is likely high due to diffusion and viscous drag.
    *   CT-GIN Mapping: Creates `EnergyDissipationNode`s: `Diffusion (NaCl)`, `Viscous Drag`, `Interfacial Dissipation`; and `EnergyDissipationEdge`s: connecting `Kinetic Energy (Droplet Motion)` to `EnergyDissipationNode`s.
    *    Implicit/Explicit: Implicit
        *  Justification: Dissipation mechanisms are not explicitly quantified, but are inferred from the description of the system and general physical principles.  Diffusion and viscous drag are standard dissipation mechanisms in fluid dynamics and chemical gradient systems.

## M3: Memory
*   **Vector ID:** M3
*   **Vector Type:** Memory

### **3.1 Memory Presence:**

*   **Vector ID:** M3.1
*   **Vector Type:** Binary
    *   Content: [No]
    *   Justification: The system, as described, does not exhibit memory in the sense of a persistent change in system state that influences *future* behavior *beyond* responding to the immediate salt gradient and surfactant availability. The droplet chemotaxis is a direct stimulus-response reaction to the instantaneous chemical gradient and surfactant concentration. There is no mention of the system adapting its transport behavior based on past experiences or carrying forward information about previous transport events to influence subsequent ones. The viability of the cells *after* transport is measured, but this is an *outcome*, not a mechanism for influencing future transport behaviour of subsequent droplets.
    *    Implicit/Explicit: Implicit
        * Justification: The absence of memory is inferred from the description of the system's operation which is purely reactive to instantaneous gradients. The paper focuses on immediate transport capabilities and viability, not on learning or adaptive behaviours based on history.

**(Conditional: If M3.1 is "No", skip to Module 4. If "Yes", include M3.2 and M3.3.)**
Skip to Module 4.

## M4: Self-Organization and Emergent Order
*   **Vector ID:** M4
*   **Vector Type:** Self-Organization

### **4.1 Self-Organization Presence:**

*   **Vector ID:** M4.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: Yes, there is evidence of self-organization at the level of the droplet motion and the capsule-droplet interaction. The chemotactic movement is not externally programmed, but arises spontaneously from the local interactions between the droplet, the surfactant, and the salt gradient. The system self-organizes its movement directionally towards a higher salt concentration due to the Marangoni instability, which is a form of spontaneous pattern formation driven by local interfacial tension gradients. The selective adhesion of the capsule to the droplet is also a form of self-organization, driven by the biosurfactants produced by the cells altering the interfacial properties, leading to emergent selective transport.
    *   Implicit/Explicit: Mixed
        *  Justification:  The paper explicitly highlights the chemotactic movement and selective transport as system behaviors. The interpretation of these behaviors as "self-organization" is implicit, but strongly supported by the description of the underlying physics - Marangoni effect and surfactant-mediated interactions - which are known to lead to spontaneous order from local interactions. The paper itself uses the term "self-motile systems".

**(Conditional: If M4.1 is "No", skip to Module 5. If "Yes", include M4.2-M4.7)**

### **4.2 Local Interaction Rules:**

*   **Vector ID:** M4.2
*   **Vector Type:** Rules
    *   Content:
        1.  **Surface Tension Gradient Generation:**  Local NaCl concentration differences create interfacial surface tension gradients. Higher NaCl concentration reduces surface tension of the 1-decanol droplet. This is mediated by surfactants at the interface (biosurfactants or decanoate).
        2.  **Marangoni Flow Induction:**  Surface tension gradients induce Marangoni flow from regions of lower surface tension (higher NaCl concentration) to regions of higher surface tension (lower NaCl concentration). This flow drives droplet motion towards higher NaCl concentration.
        3.  **Surfactant Production & Hydrogel Modification:** Living lung cancer cells encapsulated in alginate produce biosurfactants. These surfactants diffuse out of the capsule and modify the alginate hydrogel surface, making it more hydrophobic and thus promoting adhesion to the 1-decanol droplet.
        4.  **Adhesion/Detachment:** Hydrogel capsule adheres to the decanol droplet surface if the interfacial energy is sufficiently reduced by surfactant modification. Lack of surfactant (dead cells or empty capsules) results in poor adhesion and detachment.
    These rules operate locally at the droplet interface and capsule surface. The collective effect is the directed movement and selective transport.
    *   CT-GIN Mapping: Part of the `AdjunctionEdge` description (local side). `LocalInteractionRuleNode` attributes: `ruleType: Surface Tension Gradient Generation, Marangoni Flow Induction, Surfactant Production, Adhesion/Detachment`, `mechanism: Interfacial tension, Marangoni effect, Biosurfactant chemistry`. These define the "LocalInteraction" category of edges between `DropletNode`, `SurfactantNode`, `SaltGradientNode`, and `CapsuleNode`.
    * **Implicit/Explicit**: Mixed
        *  Justification: Rules 1, 2, and 4 are implicitly described, relying on established physicochemical principles of Marangoni flows and interfacial phenomena. Rule 3 concerning biosurfactant production by cancer cells and its effect on hydrogel modification is experimentally validated and explicitly described in the results and discussion, and inferred from the experiments.

### **4.2.1 Local Interaction Parameters:**

* **Vector ID:** M4.2.1
* **Vector Type:** Table
*   Table:
    | Rule ID | Description | Parameter Name | Parameter Value Range | Units | Data Source | Implicit/Explicit | Justification |
    | :------ | :---------- | :------------- | :---------- | :---: | :----------: | :----------------: | :------------: |
    | 1       | Surface Tension Gradient | NaCl Concentration | 0 - 1.5 (in 1:1 mix with 3M NaCl) | M | Fig 5, Methods | Explicit | NaCl at 3M is added and mixed 1:1 in surface tension measurements |
    | 1       | Surface Tension Gradient | Surface Tension of decanol in DMEM with surfactants from living cells  | ~24 - ~27  | mN/m | Fig 4 | Explicit | Measured values in Fig 4 |
    | 2       | Marangoni Flow Induction | Surface Tension Difference (Δγ) | ~2.8 (live cells supernatant), ~3.7 (decanoate pH 11.5), ~2.5 (decanoate pH 7), ~1.1 (dead cells supernatant) | mN/m | Fig 5 | Explicit | Values derived from Fig 5. |
    | 3       | Surfactant Production | Biosurfactant Concentration | N/A (Qualitative) | N/A | Fig 2, Results | Implicit | Surfactant concentration is not quantified, only qualitatively assessed via dilution and association time |
    | 4       | Adhesion/Detachment | Capsule-Droplet Association Time (Living Cells) | ~90 | minutes | Fig 2 | Explicit | Measured in Fig 2. Mean for lung cancer cell lines. |
    | 4       | Adhesion/Detachment | Capsule-Droplet Association Time (Dead Cells/Empty) | ~0 | minutes | Fig 2 | Explicit | Capsules release immediately. |

### **4.3 Global Order:**

*   **Vector ID:** M4.3
*   **Vector Type:** Order
    *   Content: The global order is the directed transport of alginate capsules containing living cells towards the source of higher NaCl concentration. This is a spatiotemporal order, where the droplet and capsule system moves in a coordinated manner over macroscopic distances. The selectivity for living cells is also a form of emergent order in terms of cargo transported. At a higher level of abstraction, the system exhibits a rudimentary form of "autoselective" behavior.
    *   CT-GIN Mapping: Defines a `ConfigurationalNode`: `configurationType: Directed Transport, Selective Cargo Transport`, `spatialOrder: Directed motion towards salt gradient`, `temporalOrder: Sustained transport over time`, `cargoSelectivity: Living cells vs Dead cells/Empty capsules`.
    * **Implicit/Explicit**: Mixed
        *  Justification: The directed transport and selective transport are explicitly demonstrated and described in the results.  The characterization as "global order" and "autoselective behavior" is an interpretation and thus implicit, framing the observed behavior in terms of self-organization and emergence.

### **4.4 Predictability of Global Order:**

*   **Vector ID:** M4.4
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The directed transport of capsules with living cells is highly predictable when biosurfactants are present. The paper reports "10 successful transports out of 10 transport trials" for capsules polymerized using lung cancer cell-DMEM supernatant. The lack of transport for empty capsules or capsules with dead cells is also highly predictable ("10 releases out of 10 trials").  Predictability is high under controlled experimental conditions. However, factors like subtle variations in surfactant concentration, droplet size, or external disturbances could introduce some variability. Qualitative assessment: High predictability under defined conditions.
    * **Implicit/Explicit**: Mixed
    *  Justification: The high success rate of transport and release under different conditions are explicitly stated experimental results. The "predictability score" is a qualitative assessment based on these results and general understanding that experimental systems have some degree of inherent variability.
    *   CT-GIN Mapping: Contributes to the `AdjunctionEdge` weight: `predictabilityScore: 8`.

### **4.5. Local Interaction Rules (for Self-Organization)**
* **Vector ID:** M4.5
* **Vector Type:** Table
*   Table:
| Rule ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Source |
| :------ | :---------- | :-------- | :---------- | :---------- | :----------------: | :------------: | :-----: |
| 1 | Surface Tension Dependence on NaCl  | NaCl Concentration | 0 - 1.5 | M | Explicit | Surface tension measured with varying NaCl concentration (via 1:1 mixing with 3M NaCl) | Fig 5 |
| 2 | Surfactant Effect on Interfacial Tension | Surfactant Type (Biosurfactant vs Decanoate) | Qualitative (Presence/Absence, Different types) | N/A | Explicit | Surface tension difference observed with and without biosurfactants and decanoate in Fig 4, 5 | Fig 4, 5 |
| 3 | Adhesion Strength vs Surfactant | Surfactant Concentration (Diluted Supernatant) | Dilutions: 1:1, 1:5, 1:10, 1:20, Pure DMEM, Pure Water, BT Cells Supernatant | N/A | Explicit | Association time measured for different dilutions of supernatant containing surfactants, different controls in Fig 2 | Fig 2 |

### **4.6. Globally Emergent Order and Order Parameters**
* **Vector ID:** M4.6
* **Vector Type:** Table
*   Table:
| Property ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Protocol | Source |
| :---------- | :---------- | :-------- | :---------- | :---------- | :----------------: | :------------: | :------: | :-----: |
| 1 | Chemotactic Velocity | Droplet Velocity in DMEM only | 0.0131 ± 0.002 | cm/sec | Explicit | Velocity reported for DMEM only control | Results | Text |
| 2 | Chemotactic Distance  | Path Length in DMEM only | 56 ± 3 | % of total distance | Explicit | Path length for DMEM only control, percentage of total distance between droplet and salt starting point | Results | Text |
| 3 | Transport Success Rate (Live Cells) | Successful transports/total trials | 10/10 | N/A | Explicit | Transport of capsules with living cells is efficient in every trial | Results | Text |
| 4 | Transport Success Rate (Dead/Empty) | Successful transports/total trials | 0/10 | N/A | Explicit | Empty capsules and capsules with BT cells are released immediately | Results | Text |
| 5 | Capsule-Droplet Association Time (Live Cells) | Association Time | ~90 | minutes | Explicit | Association time for capsules produced from supernatant of living cells | Results, Fig 2 | Fig 2, Text |
### **4.7 Yoneda Embedding and Local-to-Global Mapping Fidelity**

*   **Vector ID:** M4.7
*   **Vector Type:** Table
*   Table:
    | Link Type | Description | Predictability | Yoneda Score | Metrics | Implicit/Explicit | Justification | Source |
    | :-------- | :---------- | :------------- | :----------- | :------ | :----------------: | :------------: | :-----: |
     | Local Rules -> Transport | Local Surface Tension Gradients -> Directed transport of cells | High | 7 | Transport Success Rate, Capsule-Droplet Association Time | Mixed | High predictability of transport outcome given local surfactant and salt conditions observed experimentally | Results, Fig 2, Text |
    *   **Yoneda Embedding Fulfillment Score [0-10]:** [Rubric: 0-2: No discernible link between local rules and global order. 3-5: Weak or inconsistent link. Global order partially predictable from local rules, but with significant noise or exceptions. 6-8: Moderate to strong link. Global order is largely predictable from local rules under defined conditions, with some variability. 9-10: Very strong and robust link. Global order is almost entirely determined by local rules, highly predictable and consistent. Examples: 3 - Flock direction weakly influenced by individual bird's local interactions. 7 - Crystal structure largely determined by local atomic interactions. 9 - Cellular automata rules consistently generate predictable global patterns.] Score: 7. The global behavior (directed transport) is strongly linked to the local rules (surface tension gradients and surfactant-mediated adhesion). The predictability is high under controlled conditions, but there's potential for variability and external factors to influence the system, hence a score of 7 rather than higher.
    *   **Metrics:**  [Transport Success Rate; Capsule-Droplet Association Time]
    *   **Justification:** The Yoneda score of 7 reflects a strong but not perfect mapping from local interaction rules to the emergent global behavior of directed and selective transport. The metrics used (transport success rate and association time) directly quantify the emergent order and its dependence on experimental conditions representing local rules (surfactant presence, salt gradient).

## M5: Computation
*   **Vector ID:** M5
*   **Vector Type:** Computation

### **5.1 Embodied Computation Presence:**

*   **Vector ID:** M5.1
*   **Vector Type:** Binary
    *   Content: [No]
    *   Justification: The system does not perform explicit computation. The droplet motion and selective transport are based on physicochemical responses to the external chemical gradient and surfactant presence. While there are interactions and responses within the system, they do not constitute computational primitives or logical operations in a meaningful sense. The system reacts to stimuli, but doesn't process information to perform calculations or solve problems beyond this basic responsivity. The system selects living cells based on surfactant production, but this selection is a physical outcome of interfacial interactions, not a computational decision.
    *    Implicit/Explicit: Implicit
        *  Justification:  The paper describes a physical system that reacts to its environment.  The absence of embodied computation is inferred from the lack of any description of information processing, logical operations, or units performing calculations. The system's behavior is explained by physics and chemistry, not computational algorithms.

**(Conditional: If M5.1 is "No", skip to Module 6. If "Yes", include M5.2-5.4)**
Skip to Module 6.

## M6: Temporal Dynamics
*   **Vector ID:** M6
*   **Vector Type:** Temporal

### **6.1 Timescales:**

*   **Vector ID:** M6.1
*   **Vector Type:** ParameterTable
    *   Table:
        | Timescale Description | Value | Units | Source | Implicit/Explicit | Justification |
        | :-------------------- | :---: | :---: | :----: | :----------------: | :------------: |
        | Capsule Incubation Time in DMEM | 2 | days | Methods, Alginate hydrogel and capsule formation. | Explicit | Duration of cell incubation in capsules. |
        | Capsule-Droplet Association Time (Living Cells) | ~90 | minutes | Results, Fig 2 | Explicit | Time capsule remains associated with droplet. |
        | Transport Time (Qualitative) | Minutes to hours | Implicit | Observation of chemotaxis, Movie S1 | Implicit | Based on description of transport experiments and supplementary movies. |
        | Cell Viability Assay Incubation (MTT) | 3 | hours | Methods, Transport and cell viability assessment | Explicit | Incubation for MTT assay. |
        | Cell Proliferation Assessment Time to Confluence (After Transport) | 3 | weeks | Results, Cell survival after transport | Explicit | Time to reach confluence after being plated after transport. Compared to 2 weeks for cells before transport. |

### **6.2 Active Inference:**

*   **Vector ID:** M6.2
*   **Vector Type:** Assessment
    *   Content: [No]
    *   Justification: There is no evidence of active inference in this system. The droplet does not have an internal model of its environment, nor does it predict future states or select actions to minimize prediction error. The chemotactic movement is a purely reactive response to the instantaneous salt gradient. The system does not "learn" about its environment or adapt its behavior beyond the immediate stimulus-response cycle. There's no indication of prediction, anticipation, or internal model updating.
    *   Implicit/Explicit: Implicit
        *  Justification: The paper describes a reactive system, responding directly to external stimuli. Active inference requires internal models and predictive behavior, which are absent in the system description and experimental results. The system lacks any mechanism for prediction or model updating.
    *   **If Yes/Partial, provide examples of testable CT-GIN metrics that *could* be used to quantify active inference:** N/A

## M7: Adaptation
*   **Vector ID:** M7
*   **Vector Type:** Adaptation

### **7.1 Adaptive Plasticity Presence:**

*   **Vector ID:** M7.1
*   **Vector Type:** Binary
    *   Content: [No]
    *   Justification:  The system does not exhibit adaptive plasticity. The droplet chemotaxis and selective transport are fixed behaviors determined by the physicochemical properties of the components and their interactions. There is no mechanism for the system to change its behavior or internal structure in response to experience over time to improve performance or alter functionality. The system responds to the presence of biosurfactants and salt gradient in a predetermined way. The viability of cells might change over time or different conditions but the transport system itself doesn't adapt.
    *    Implicit/Explicit: Implicit
        * Justification: The system's behavior is consistently described as a stimulus-response system without any indication of persistent changes based on experience or feedback loops that would lead to adaptive behavior.

**(Conditional: If M7.1 is "No", skip to Module 8. If "Yes", include M7.2)**
Skip to Module 8.

## M8: Emergent Behaviors
*   **Vector ID:** M8
*   **Vector Type:** Behavior

### **8.1 Behavior Description:**

*   **Vector ID:** M8.1
*   **Vector Type:** Description
    *   Content: The main emergent behaviors are:
        1.  **Chemotactic Transport:** Directed motion of the decanol droplet towards higher NaCl concentration.
        2.  **Autoselective капсула Transport:** Selective transport of alginate capsules containing living lung cancer cells, but not empty capsules or capsules with dead cells. This selectivity arises spontaneously from the interaction of the artificial droplet system and the biological cells' biosurfactant production.
    These behaviors are emergent because they arise from the interplay of multiple components (droplet, surfactant, salt gradient, cells, capsules) and are not properties of any single component in isolation. The "autoselectivity" is particularly emergent as it's a system-level property arising from the interaction of artificial and biological subsystems.
    *   CT-GIN Mapping: Defines the `BehaviorArchetypeNode`. `behaviorType: Chemotactic Transport, Autoselective Capsule Transport`, `description: Directed droplet motion towards salt gradient, Selective transport of living surfacant-producing cells`.
    *    Implicit/Explicit: Mixed
       *  Justification: The chemotactic transport and selective transport are explicitly observed and described results of the experiments. The characterization of these behaviors as "emergent" is an interpretation, but strongly supported by the system description: the behaviors arise from interactions between components and are not pre-programmed or externally controlled in a direct way, thus implied emergence.

### **8.2 Behavior Robustness:**

*   **Vector ID:** M8.2
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The chemotactic transport and autoselectivity are shown to be reasonably robust under the tested conditions. The 10/10 success rate suggests reliability. Robustness is demonstrated across different lung cancer cell lines. The system is shown to function with variations in surfactant source (biosurfactants, decanoate). However, robustness to significant changes in environmental conditions (temperature, flow variations, complex chemical environments), droplet size variations, or capsule properties is not explicitly tested or quantified.  Qualitative Assessment: Moderately Robust under tested conditions.
    *   Implicit/Explicit: Mixed
        *  Justification: High success rates suggest robustness under tested experimental conditions, this is explicit in the quantitative results.  Limitations in robustness assessment (lack of testing under drastically different conditions) are implicit, inferred from considering the scope of experimental variation explored in the paper.
    *   CT-GIN Mapping: This score contributes to the reliability attributes of the `BehaviorArchetypeNode`: `robustnessScore: 7`.

### **8.3 CT-GIN Emergent Behavior Validation**

*    **Vector ID:** M8.3
*    **Vector Type:** Validation
     *  Content: Validation methods include:
        1.  **Controlled Experiments:** Comparing transport of capsules with living cells vs. dead cells vs. empty capsules to demonstrate autoselectivity (Results, Autoselective transport).
        2.  **Quantitative Assays:** Measuring capsule-droplet association time (Fig 2) and surface tension changes (Figs 4, 5) to quantify the role of biosurfactants and surface tension gradients in transport.
        3.  **Viability Assays:** Assessing cell viability before and after transport (Fig 3, Table 1) to evaluate the impact of the transport process on cell survival.
        4.  **Control Conditions:** Testing transport in pure DMEM, DMEM with dead cells supernatant, DMEM with empty capsules supernatant to establish the necessity of living cell-produced surfactants for efficient chemotaxis (Results, chemotaxis feasibility; Fig 4, 5).
        5.  **Reproducibility:** Reporting replicates (typically 10) for association tests and chemotaxis trials, and triplicates for viability assays demonstrating reproducibility under given conditions (Methods section throughout).
    Limitations: Robustness to a wider range of environmental perturbations and long-term operational reliability are not systematically assessed.
     *   Implicit/Explicit: Explicit
    *   Justification: Validation methods are explicitly described in the "Results" and "Methods" sections, referencing figures and tables as indicated. The description of controls, quantitative measurements, and replicates is direct from the text. Limitations are implicitly noted by the scope of experiments performed and lack of broader stress-testing.

## M9: Cognitive Proximity
*   **Vector ID:** M9
*   **Vector Type:** Cognition

### **9.1 Cognitive Mapping:**

*   **Vector ID:** M9.1
*   **Vector Type:** Description
    *   Content: The paper draws an analogy between the droplet system and basic aspects of living systems' behavior, particularly chemotaxis and selective cargo transport. It suggests the system demonstrates a "primitive example of how self-motile systems may be produced that can also be selective for the types of cargo transported" and hints at future extension to "demarcation between different types of mammalian cells…due to stage of differentiation, production of key markers, and perhaps potency." The "autoselectivity" for living cells is metaphorically connected to "distinguishing between living versus dead cells with selectivity emerging through the interface of artificial life systems with natural living systems." Limitations: These are metaphorical mappings; the system lacks higher-level cognitive functions.
    *   CT-GIN Mapping: `CognitiveMappingEdge` from `BehaviorArchetypeNode: Autoselective Capsule Transport` to `CognitiveFunctionNode: Basic Chemotaxis, Primitive Discrimination`.
    *   Implicit/Explicit: Mixed
    * Justification: The paper explicitly uses terms like "autoselective" and draws comparisons to "life-like behaviors" and "primitive example of how self-motile systems may be produced that can also be selective". These are explicit attempts at cognitive framing. However, the understanding of these as analogies and limitations to basic biological behaviours is implicit in the overall scientific and technical tone, and the lack of claims for higher cognitive functionalities.

### **9.2 Cognitive Proximity Score:**

*   **Vector ID:** M9.2
*   **Vector Type:** Score
    *   Score: [2]
    *   Justification: Level 2: Sub-Organismal Responsivity. The system exhibits a basic form of selective response (transporting living cells), which could be loosely analogized to rudimentary discrimination. However, it lacks complex representation, goal-directedness beyond reacting to a chemical gradient, memory, learning, or any higher-level cognitive functions. The system's "selectivity" is based on a simple physicochemical interaction (surfactant-mediated adhesion), not a complex decision-making process. It is beyond simple stimulus-response (Level 1) due to the emergent selective transport behavior, but it’s far from reactive/adaptive autonomy (Level 3) or goal-directed cognition (Level 4).
    *   Implicit/Explicit: Mixed
    *  Justification: Score is based on applying the *CT-GIN Cognizance Scale*. Justification uses explicit descriptions of the system's behavior from the paper (selective transport) and contrasts it implicitly with higher levels of cognitive complexity which are clearly absent. The scoring is thus mixed, based on explicit behaviour and implicit lack of higher functions in the context of the provided scale.

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
    | Sensing/Perception               |      4       | Senses chemical gradient (NaCl), indirectly "senses" surfactant presence through interfacial properties. Basic sensing mediated by physical interactions. Limited range of sensory inputs.                     | `CognitiveFunctionNode: Sensing/Perception` | Mixed | Sensing of NaCl concentration via physical response is implicit. Indirect 'sensing' of surfactant is inferred from selective behavior. Range and complexity are implicitly limited. |
    | Memory (Short-Term/Working)        |      0       | Absent. No short-term retention or manipulation of information. Reacts to immediate stimuli only.                                                                                       | N/A | Implicit | Absence of memory is inferred from system description and lack of any mention of memory mechanisms. |
    | Memory (Long-Term)                 |      0       | Absent. No long-term storage or retrieval of information. System state not persistently modified by past experiences affecting future actions.                                                                                       | N/A | Implicit | Absence of memory is inferred as above. |
    | Learning/Adaptation              |      0       | Absent. No adaptive behavior, performance improvement based on experience, or change in internal structure over time in response to interaction history.                                                                                       | N/A | Implicit | Absence of learning and adaptation is inferred from the static stimulus-response nature of the system. |
    | Decision-Making/Planning          |      1       | Rudimentary "decision" to move towards higher salt. Not based on complex evaluation or planning, but a direct physical response to gradient. Selection between living/dead cargo is a passive outcome of interaction. | `CognitiveFunctionNode: Decision-Making/Planning` | Mixed | Basic directionality of motion implies rudimentary "decision," though mechanistic not cognitive. Lack of planning or complex choice is implicit. |
    | Communication/Social Interaction |      0       | Absent. The droplet acts in isolation, no communication or interaction with other agents or systems performing similar or cooperative tasks.                                                                                       | N/A | Implicit | Social interaction/communication is clearly absent from the system description. |
    | Goal-Directed Behavior            |      2       | Weakly goal-directed (towards higher salt concentration). Can be seen as a rudimentary goal, but driven by physics, not internally represented goals or purposes.                                                                                       | `CognitiveFunctionNode: Goal-Directed Behavior` | Mixed | Directional movement can be interpreted as weakly goal-directed, however, the nature is physical not intentional, inferred limit. |
    | Model-Based Reasoning              |      0       | Absent. No internal model of the environment, no reasoning or inference based on a model. Behavior is purely reactive, not model-based predictive.                                                                                       | N/A | Implicit | Model-based reasoning is entirely absent from the system mechanisms and descriptions. |
    | **Overall score**                 |      [1]       |                                                                                       |                                   |                     |                |

    *   **Note:** Assess the system for *each* function, providing a score (0-10) and a short (1-2 sentences) justification.  0 = Absent, 10 = Human-level performance.

## M10: Criticality Assessment
*   **Vector ID:** M10
*   **Vector Type:** Criticality

### **10.1 Criticality:**

*   **Vector ID:** M10.1
*   **Vector Type:** Assessment
    *   Content: [Unclear]
    *   Justification: The paper does not explicitly address criticality or the system's operation near a critical point.  Marangoni instabilities themselves can sometimes exhibit complex dynamics and pattern formation that could potentially be related to criticality, but this is not discussed in the context of this specific system. There is no evidence presented for scale-free behavior, power laws, or long-range correlations. The system seems to operate in a relatively stable regime, driven by a controlled external gradient and surfactant effect.  More detailed analysis of droplet dynamics and interfacial fluctuations would be needed to assess criticality.
        *   Critical Parameters (If Yes/Partial): N/A
        *   Evidence: N/A
    *   Implicit/Explicit: Implicit
    *    Justification: Criticality is not mentioned, assessed or implied in the text. Its relevance to Marangoni systems is background knowledge, but not applied to the described experiments, hence assessment "Unclear" relying on absence of evidence in paper.

## M11: Review Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Review")**
Skip Module 11.

## M12: Theoretical Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Theoretical")**
Skip Module 12.

## M13: Overall Assessment & Scoring

*   **Vector ID:** M13
*   **Vector Type:** Overall

### **13.1 CT-GIN Readiness Score:**

*   **Vector ID:** M13.1
*   **Vector Type:** Score
*   **Calculated Score:** [5.3]  (Average of scores from Modules 1-4, M8.2 and M9.2, scores with N/A convert in 0).  *This score MUST be automatically calculated. Only Number.*

**CT-GIN Readiness Summary Table:**

| CT-GIN Aspect                   | Strength (Yes/Partial/No) | Key Supporting Metrics (with units) | Limitations (Missing Metrics/Data Gaps)                                           | Improvement Areas (Future Research)                                          |
| :------------------------------ | :-----------------------: | :-----------------------------------| :------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| Energy Flow Efficiency          | No                         | N/A                                 | Efficiency not quantified                                                       | Quantify efficiency, explore energy recycling or more efficient transduction mechanisms. |
| Memory Fidelity                 | No                         | N/A                                 | No memory demonstrated                                                          | Implement memory mechanism, investigate structural or chemical memory elements. |
| Organizational Complexity       | Partial                    | Capsule-Droplet Association Time ~90 minutes, Transport Success Rate 10/10          | Level of organization is basic, primarily driven by external gradient.             | Explore more complex self-organizing structures, internal feedback loops for order. |
| Embodied Computation            | No                         | N/A                                 | No computational primitives demonstrated                                          | Integrate computational elements, explore analog computation in droplet system |
| Temporal Integration            | No                         | Timescales defined for experiment duration. | No integration of past events into future behavior (memory absent)              | Implement temporal memory, investigate temporal coding and processing.      |
| Adaptive Plasticity             | No                         | N/A                                 | No adaptive plasticity demonstrated                                             | Introduce mechanisms for adaptation, explore feedback-driven parameter changes. |
| Functional Universality         | No                         | Autoselective transport demonstrated.   | Functionality limited to transport, selectivity based on surfactant production. | Expand functionality, explore multi-functional materials and behaviors.     |
| Cognitive Proximity            | No                         | Cognitive Proximity Score: 2          | Very low cognitive proximity, lacks higher cognitive functions                       | Develop higher cognitive functions (memory, learning, planning).             |
| Design Scalability & Robustness | Partial                    | Robustness score 7, 10/10 success rate. | Robustness not tested against wide range of perturbations. Scalability not discussed. | Systematically test robustness, evaluate scalability for larger-scale systems.   |
| **Overall CT-GIN Readiness Score** |        |   |   |      |


### **13.2 Qualitative CT-GIN Assessment Conclusion:**

*   **Vector ID:** M13.2
*   **Vector Type:** Textual Summary
    *   Content: The droplet-based chemotactic transport system demonstrates a basic form of emergent behavior: autoselective transport of living cells. Key strengths are the clear implementation of chemotaxis, the demonstration of selectivity based on biosurfactants, and reasonable robustness under tested conditions. Key limitations are the lack of memory, computation, adaptation, and low cognitive proximity. Energy efficiency is likely low, though not quantified. Organizational complexity is limited, primarily driven by external gradients. Overall assessment: The system represents a Level 2 on the CT-GIN Cognizance Scale, showing sub-organismal responsivity. It's a well-executed experimental demonstration of emergent behavior in a hybrid artificial-biological system, but falls short of exhibiting features of truly cognizant matter due to the absence of memory, computation, and adaptive plasticity. Potential within CT-GIN is moderate, providing a platform for exploring more complex functionalities by integrating memory or adaptive elements in future research.

### **13.3 CT-GIN Refinement Directions:**

*   **Vector ID:** M13.3
*   **Vector Type:** Recommendations
    *   * Integrate a Memory Mechanism: Introduce components that can retain information about past transport events or environmental conditions to influence future droplet behavior. Explore phase-change materials or chemical gradients that persist over time as potential memory elements within the droplet or capsule system.
    *   * Implement Embodied Computation: Incorporate elements that can perform basic analog computation within the material system, potentially using droplet dynamics or interfacial properties to realize computational primitives. Investigate reaction-diffusion systems or non-linear chemical reaction networks within the droplet or capsule for computation.
    *   * Introduce Adaptive Plasticity: Design mechanisms that allow the system to adapt its transport behavior based on feedback or experience. Explore feedback loops that modify surfactant production, droplet properties, or transport parameters in response to system performance or environmental changes.
    *   * Enhance Energy Efficiency: Investigate methods to improve energy transduction efficiency, potentially by optimizing droplet composition, surfactant properties, or gradient generation methods. Explore energy harvesting from the environment to sustain droplet motion and reduce dissipation.
    *   * Increase Organizational Complexity: Move beyond purely reactive behavior to explore more complex self-organizing architectures. Introduce internal feedback loops and hierarchical organization to achieve richer dynamics and emergent functionalities.

## M14: CT-GIN Knowledge Graph

*   **Vector ID:** M14
*   **Vector Type:** Visualization

### **14.1. CT-GIN Knowledge Graph:**
* **Content:**
[__Description of CT-GIN Knowledge Graph Diagram (Textual - Cannot insert image):__

**Nodes:**

*   `SystemNode` (Droplet-based Chemotactic Transport): Attributes: systemType, domain, mechanism, components, purpose. (Shape: Circle, Color: Blue)
*   `EnergyInputNode` (Chemical Potential Energy - NaCl gradient): Attributes: source, type. (Shape: Diamond, Color: Green)
*   `EnergyDissipationNode` (Diffusion (NaCl), Viscous Drag, Interfacial Dissipation): Attributes: type, mechanism. (Shape: Square, Color: Red)
*   `MemoryNode` (Absent): type: none. (Shape: Triangle, Color: Gray)
*   `ComputationNode` (Absent): type: none. (Shape: Pentagon, Color: Gray)
*   `ConfigurationalNode` (Directed Transport, Selective Cargo Transport): Attributes: configurationType, spatialOrder, temporalOrder, cargoSelectivity. (Shape: Hexagon, Color: Orange)
*   `BehaviorArchetypeNode` (Chemotactic Transport, Autoselective Capsule Transport): Attributes: behaviorType, description, robustnessScore. (Shape: Star, Color: Purple)
*   `CognitiveFunctionNode` (Sensing/Perception, Decision-Making/Planning, Goal-Directed Behavior, Basic Chemotaxis, Primitive Discrimination): Attributes: functionType, score. (Shape: Inverted Triangle, Color: Yellow)

**Edges:**

*   `EnergyTransductionEdge` (Marangoni effect): Attributes: mechanism, efficiency, from_node (Chemical Potential Energy), to_node (Kinetic Energy). (Color: Green, Directed arrow from EnergyInputNode to representing droplet kinetic energy - not explicitly node).
*   `EnergyDissipationEdge`: Attributes: mechanism, from_node (Kinetic Energy), to_node (EnergyDissipationNodes). (Color: Red, Directed arrow from representing droplet kinetic energy - not explicitly node to EnergyDissipationNodes).
*   `AdjunctionEdge` (Local Interactions): Attributes: predictabilityScore, LocalInteractionRules (surface tension gradient generation, Marangoni flow induction, surfactant production, adhesion/detachment), from_node (SaltGradientNode- not explicitly node, SurfactantNode- not explicitly node, CapsuleNode- not explicitly node, DropletNode), to_node (ConfigurationalNode). (Color: Black, Directed arrows from nodes related to Salt gradient, surfactant, capsule, droplet to ConfigurationalNode).
*   `CognitiveMappingEdge`: Attributes: mappingDescription, from_node (BehaviorArchetypeNode), to_node (CognitiveFunctionNode). (Color: Yellow, Dashed arrow from BehaviorArchetypeNode to CognitiveFunctionNodes).

**Annotations:** Nodes are labeled with their names and key attributes. Edges are labeled with their types and mechanisms. Parameters with units (e.g., capsule diameter, association time, surface tension) are annotated on relevant nodes and edges. The graph visually represents the CT-GIN framework applied to the droplet transport system, highlighting energy flow, self-organization, emergent behaviors, and cognitive mappings.]

## M15: Relationship Vectors
*   **Vector ID:** M15
*   **Vector Type:** Relationships
*   Relationships:
        | Source Vector ID | Target Vector ID | Relationship Type |
        | ------------- | ------------- | ----------------- |
        | M2.1| M2.2 | Energy Flow |
        | M2.2| M2.4 | Energy Dissipation |
        | M4.2| M4.3 | Self-Organization |
        | M4.2| M4.4 | Yoneda Embedding |
        | M8.1| M8.2 | Behavior Robustness |
        | M8.1| M8.3 | Behavior Validation |
        | M8.1| M9.1 | Cognitive Mapping |
        | M9.1| M9.2 | Cognitive Proximity Score |
        | M9.1| M9.3 | Cognitive Function Checklist |
        | M9.2| M13.1 | CT-GIN Readiness Score Contribution |
        | M4.4| M13.1 | CT-GIN Readiness Score Contribution |
        | M8.2| M13.1 | CT-GIN Readiness Score Contribution |
        | M1.2| M13.1 | CT-GIN Readiness Score Contribution |
        | M2.3| M13.1 | CT-GIN Readiness Score Contribution |
        | M4.7| M13.1 | CT-GIN Readiness Score Contribution |

## M16: CT-GIN Template Self-Improvement Insights

*   **Vector ID:** M16
*   **Vector Type:** Feedback

### **Template Feedback:**

*    **Vector ID:** M16.1
*   **Vector Type:** Text
Provide specific, actionable feedback on the *CT-GIN template itself*, based on this analysis:
    *   **Missing Probes:** The template is comprehensive. Perhaps adding a probe about "Scalability" in module M1 (System Overview), to assess potential for scaling up production or system size, would be beneficial at the overview level. Also, in M8, probing for specific *types* of robustness (e.g., robustness to noise, parameter variations, component failures) could be useful for a more nuanced analysis.
    *   **Unclear Definitions:** The definitions are generally clear. "Active Inference" definition in M6 might be dense and could be simplified for broader applicability assessment. "Self-Organization" vs "Emergent Order" distinction could be slightly sharper, though the current probes are largely effective in separating these.
    *   **Unclear Node/Edge Representations:** GIN node/edge guidance is sufficient for initial mapping. For more complex systems, providing examples of hierarchical or composite node representations might be valuable.  Specifically, in M14, maybe give example how to represent "SaltGradientNode", "SurfactantNode" and "CapsuleNode" which were implicit nodes described in edge connections to ConfiguralNode.
    *   **Scoring Difficulties:** Cognitive Proximity scoring (M9.2) is subjective and requires care to avoid overstatement. Providing more detailed examples for each level of the Cognizance Scale could improve inter-rater reliability.  The Score for M4.4 (Predictability of Global Order) is also somewhat subjective, clarifying the scale with more defined metrics (beyond qualitative) could improve consistency.
    *   **Data Extraction/Output Mapping:** Data extraction was generally straightforward. Mapping qualitative descriptions to scores requires careful judgment, detailed scoring rubrics provided are helpful.
    *   **Overall Usability:** The template is well-structured and relatively easy to use. The modular design is effective. The strict formatting requirements, while crucial for parsing, require meticulous attention.
    * **Specific Suggestions:**
        * Add "Scalability" probe to M1.
        * Add subtype of "Robustness" probe in M8.2 to specify robustness types.
        * Simplify "Active Inference" definition in M6 for broader clarity.
        * Refine Cognitive Proximity (M9.2) and Predictability (M4.4) scoring rubrics with more detailed examples.
        * In M14, add examples of representing implicit nodes in the Knowledge Graph.
        * Double check the automatic scoring calculation for M13.1 to ensure robustness and error-free computation.```markdown
# Autoselective transport of mammalian cells with a chemotactic droplet

__Paper Type:__ Experimental

## M1: System Overview & Implementation
*   **Vector ID:** M1
*   **Vector Type:** Overview

### **1.1 System Description**

*   **Vector ID:** M1.1
*   **Vector Type:** Description
    *   Content: The system is a droplet-based chemotactic transport system for mammalian cells. It uses a 1-decanol droplet as a transporter and alginate capsules to encapsulate mammalian cells (H460, H1299, A549, HEK293T, HS68). The droplet moves directionally in a chemical gradient (NaCl), driven by Marangoni flow due to surface tension imbalance. Selectivity arises from biosurfactants produced by living lung cancer cell lines (H460, H1299, A549) when encapsulated in hydrogel capsules. These surfactants modify the hydrogel surface, enabling droplet adhesion and supporting chemotaxis. The purpose is to selectively transport living cells and potentially distinguish cell types based on biosurfactant production. Components include: 1-decanol droplet, alginate hydrogel capsules, mammalian cells, DMEM growth media, NaCl salt gradient, surfactants (biosurfactants from cells and potentially decanoate in controls).
    *   CT-GIN Mapping: `SystemNode` attributes: `systemType: Droplet-based Chemotactic Transport`, `domain: Biological Cell Transport`, `mechanism: Marangoni Chemotaxis, Biosurfactant Mediated Adhesion`, `components: Decanol droplet, Alginate capsules, Mammalian cells, NaCl, Biosurfactants`, `purpose: Selective cell transport, Cell type differentiation`
    *   Implicit/Explicit: Mixed
        *  Justification: The system components, purpose, and function are explicitly described in the abstract, introduction, results, and methods sections. The underlying mechanism is implicitly described drawing from known Marangoni effect and chemotaxis principles, and explicitly referencing surfactant role. The CT-GIN mapping is inferred based on the system description.

### **1.2 Implementation Clarity**

*   **Vector ID:** M1.2
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The implementation is well-described, with detailed methods for cell encapsulation, droplet preparation, chemotaxis setup, and viability assays. Figures and supplementary movies further clarify the setup and the transport process. The roles of each component and the experimental procedure are detailed. Clarity could be increased with more precise quantification of surfactant concentration and surface tension dynamics during transport.
    *   Implicit/Explicit: Mixed
        * Justification: The overall implementation is clearly described explicitly in the methods and result section and supported by figures and supplementary materials.  Some details, such as real-time surfactant concentration at the droplet interface, are implicit, but the crucial steps are explicitly stated.

### **1.3 Key Parameters**

*   **Vector ID:** M1.3
*   **Vector Type:** ParameterTable
    *   Table:
        | Parameter Name | Value | Units | Source (Fig/Table/Section) | Implicit/Explicit | Data Reliability (High/Medium/Low) | Derivation Method (if Implicit) |
        | :------------- | :---: | :---: | :-----------------------: | :-----------------: | :-----------------------------: | :-------------------------------: |
        | Capsule Diameter | 2.5 - 3 | mm | Results | Explicit | High | N/A |
        | Capsule Weight | 15.7 ± 0.6 | mg | Results | Explicit | High | N/A |
        | Capsule Volume | ~15 | µl | Results | Explicit | Medium | Approximated from weight and density, and volume replicates (10 capsules). |
        | Decanol Droplet Volume | 20, 250 | µl | Methods, Transport and cell viability assessment; Chemotaxis feasibility and autoselectivity. | Explicit | High | N/A |
        | NaCl Concentration Gradient | 3 | M | Results, Methods | Explicit | High | N/A |

    *   **Note:** List *up to 5* key parameters characterizing the system's *implementation*.  Provide values and units if possible. If a parameter is not explicitly stated but derived/inferred, clearly state the derivation method. *Always* include units if applicable. If a value is not applicable, write "N/A".  Data Reliability: High = Directly measured, Medium = Derived from measurements/simulations, Low = Estimated/Inferred.

## M2: Energy Flow
*   **Vector ID:** M2
*   **Vector Type:** Energy

### **2.1 Energy Input**

*   **Vector ID:** M2.1
*   **Vector Type:** Input
    *   Content: The primary energy input is chemical potential energy stored in the NaCl salt gradient.
    *   Value: N/A
    *   Units: N/A
    *   CT-GIN Mapping: `EnergyInputNode`: attributes - `source: NaCl salt gradient`, `type: Chemical Potential`
    *   Implicit/Explicit: Implicit
        *  Justification:  While the paper mentions adding NaCl to create a chemical gradient, the explicit characterization of the "energy input" as chemical potential is implicit, inferred from the principles of chemotaxis and diffusion driven processes.

### **2.2 Energy Transduction**

*   **Vector ID:** M2.2
*   **Vector Type:** Transduction
    *   Content: The chemical potential energy of the NaCl gradient is transduced into kinetic energy of the decanol droplet movement. The salt gradient creates a surface tension gradient across the droplet due to the surfactant at the interface (biosurfactants or decanoate). This surface tension imbalance leads to Marangoni flow within and around the droplet, resulting in directional droplet motion towards the higher salt concentration. The biosurfactants produced by the cells play a crucial role in establishing and maintaining the interface needed for this transduction.
    *   CT-GIN Mapping: `EnergyTransductionEdge`: attributes - `mechanism: Marangoni effect`, `from_node: Chemical Potential Energy (NaCl gradient)`, `to_node: Kinetic Energy (Droplet Motion)`
    *   Implicit/Explicit: Mixed
        *  Justification: The Marangoni effect is described as the mechanism of droplet motion, which is explicitly mentioned in the introduction and discussion. The role of surfactant and surface tension gradients is also explicitly described. The energy transduction process is described implicitly, based on physics principles of Marangoni effect in the context of chemotaxis.

### **2.3 Energy Efficiency**

*   **Vector ID:** M2.3
*   **Vector Type:** Score
    *   Score: [3]
    *   Justification/Metrics: Energy efficiency is likely low but not explicitly quantified. Marangoni effect based systems are generally not highly energy efficient. Most of the chemical potential energy is dissipated through diffusion and mixing of NaCl in the aqueous phase, and viscous drag from the droplet motion. Only a small fraction of the initial chemical potential is converted into the directed motion of the droplet and the transport of capsules. No quantitative data is provided to assess efficiency. Qualitative Assessment: Low.
    *   CT-GIN Mapping: Attribute of `EnergyTransductionEdge`s: `efficiency: Low`
    *   Implicit/Explicit: Implicit
      *  Justification: Efficiency is not quantified or discussed in the paper. Score is inferred based on general understanding of Marangoni driven systems and lack of energy recovery mechanisms.

### **2.4 Energy Dissipation**

*   **Vector ID:** M2.4
*   **Vector Type:** Dissipation
    *   Content: Energy dissipation mechanisms include:
        1.  **Diffusion of NaCl:** The salt gradient dissipates as NaCl diffuses into the aqueous phase, reducing the chemical potential gradient. Quantification is not provided but is a major dissipation factor.
        2.  **Viscous Drag:** The motion of the decanol droplet through the aqueous phase generates viscous drag, dissipating kinetic energy as heat. Quantification is not provided.
        3.  **Interfacial Dissipation:** Energy may be dissipated at the droplet-aqueous phase interface due to surfactant dynamics and mixing. Quantification is not provided.
        4. **Heat loss**: General thermal dissipation to the environment is implicit but not quantified.
    Qualitative Assessment: Energy dissipation is likely high due to diffusion and viscous drag.
    *   CT-GIN Mapping: Creates `EnergyDissipationNode`s: `Diffusion (NaCl)`, `Viscous Drag`, `Interfacial Dissipation`; and `EnergyDissipationEdge`s: connecting `Kinetic Energy (Droplet Motion)` to `EnergyDissipationNode`s.
    *    Implicit/Explicit: Implicit
        *  Justification: Dissipation mechanisms are not explicitly quantified, but are inferred from the description of the system and general physical principles.  Diffusion and viscous drag are standard dissipation mechanisms in fluid dynamics and chemical gradient systems.

## M3: Memory
*   **Vector ID:** M3
*   **Vector Type:** Memory

### **3.1 Memory Presence:**

*   **Vector ID:** M3.1
*   **Vector Type:** Binary
    *   Content: [No]
    *   Justification: The system, as described, does not exhibit memory in the sense of a persistent change in system state that influences *future* behavior *beyond* responding to the immediate salt gradient and surfactant availability. The droplet chemotaxis is a direct stimulus-response reaction to the instantaneous chemical gradient and surfactant concentration. There is no mention of the system adapting its transport behavior based on past experiences or carrying forward information about previous transport events to influence subsequent ones. The viability of the cells *after* transport is measured, but this is an *outcome*, not a mechanism for influencing future transport behaviour of subsequent droplets.
    *    Implicit/Explicit: Implicit
        * Justification: The absence of memory is inferred from the description of the system's operation which is purely reactive to instantaneous gradients. The paper focuses on immediate transport capabilities and viability, not on learning or adaptive behaviours based on history.

## M4: Self-Organization and Emergent Order
*   **Vector ID:** M4
*   **Vector Type:** Self-Organization

### **4.1 Self-Organization Presence:**

*   **Vector ID:** M4.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: Yes, there is evidence of self-organization at the level of the droplet motion and the capsule-droplet interaction. The chemotactic movement is not externally programmed, but arises spontaneously from the local interactions between the droplet, the surfactant, and the salt gradient. The system self-organizes its movement directionally towards a higher salt concentration due to the Marangoni instability, which is a form of spontaneous pattern formation driven by local interfacial tension gradients. The selective adhesion of the capsule to the droplet is also a form of self-organization, driven by the biosurfactants produced by the cells altering the interfacial properties, leading to emergent selective transport.
    *   Implicit/Explicit: Mixed
        *  Justification:  The paper explicitly highlights the chemotactic movement and selective transport as system behaviors. The interpretation of these behaviors as "self-organization" is implicit, but strongly supported by the description of the underlying physics - Marangoni effect and surfactant-mediated interactions - which are known to lead to spontaneous order from local interactions. The paper itself uses the term "self-motile systems".

### **4.2 Local Interaction Rules:**

*   **Vector ID:** M4.2
*   **Vector Type:** Rules
    *   Content:
        1.  **Surface Tension Gradient Generation:**  Local NaCl concentration differences create interfacial surface tension gradients. Higher NaCl concentration reduces surface tension of the 1-decanol droplet. This is mediated by surfactants at the interface (biosurfactants or decanoate).
        2.  **Marangoni Flow Induction:**  Surface tension gradients induce Marangoni flow from regions of lower surface tension (higher NaCl concentration) to regions of higher surface tension (lower NaCl concentration). This flow drives droplet motion towards higher NaCl concentration.
        3.  **Surfactant Production & Hydrogel Modification:** Living lung cancer cells encapsulated in alginate produce biosurfactants. These surfactants diffuse out of the capsule and modify the alginate hydrogel surface, making it more hydrophobic and thus promoting adhesion to the 1-decanol droplet.
        4.  **Adhesion/Detachment:** Hydrogel capsule adheres to the decanol droplet surface if the interfacial energy is sufficiently reduced by surfactant modification. Lack of surfactant (dead cells or empty capsules) results in poor adhesion and detachment.
    These rules operate locally at the droplet interface and capsule surface. The collective effect is the directed movement and selective transport.
    *   CT-GIN Mapping: Part of the `AdjunctionEdge` description (local side). `LocalInteractionRuleNode` attributes: `ruleType: Surface Tension Gradient Generation, Marangoni Flow Induction, Surfactant Production, Adhesion/Detachment`, `mechanism: Interfacial tension, Marangoni effect, Biosurfactant chemistry`. These define the "LocalInteraction" category of edges between `DropletNode`, `SurfactantNode`, `SaltGradientNode`, and `CapsuleNode`.
    * **Implicit/Explicit**: Mixed
        *  Justification: Rules 1, 2, and 4 are implicitly described, relying on established physicochemical principles of Marangoni flows and interfacial phenomena. Rule 3 concerning biosurfactant production by cancer cells and its effect on hydrogel modification is experimentally validated and explicitly described in the results and discussion, and inferred from the experiments.

### **4.2.1 Local Interaction Parameters:**

* **Vector ID:** M4.2.1
* **Vector Type:** Table
*   Table:
    | Rule ID | Description | Parameter Name | Parameter Value Range | Units | Data Source | Implicit/Explicit | Justification |
    | :------ | :---------- | :------------- | :---------- | :---: | :----------: | :----------------: | :------------: |
    | 1       | Surface Tension Gradient | NaCl Concentration | 0 - 1.5 (in 1:1 mix with 3M NaCl) | M | Fig 5, Methods | Explicit | NaCl at 3M is added and mixed 1:1 in surface tension measurements |
    | 1       | Surface Tension Gradient | Surface Tension of decanol in DMEM with surfactants from living cells  | ~24 - ~27  | mN/m | Fig 4 | Explicit | Measured values in Fig 4 |
    | 2       | Marangoni Flow Induction | Surface Tension Difference (Δγ) | ~2.8 (live cells supernatant), ~3.7 (decanoate pH 11.5), ~2.5 (decanoate pH 7), ~1.1 (dead cells supernatant) | mN/m | Fig 5 | Explicit | Values derived from Fig 5. |
    | 3       | Surfactant Production | Biosurfactant Concentration | N/A (Qualitative) | N/A | Fig 2, Results | Implicit | Surfactant concentration is not quantified, only qualitatively assessed via dilution and association time |
    | 4       | Adhesion/Detachment | Capsule-Droplet Association Time (Living Cells) | ~90 | minutes | Fig 2 | Explicit | Measured in Fig 2. Mean for lung cancer cell lines. |
    | 4       | Adhesion/Detachment | Capsule-Droplet Association Time (Dead Cells/Empty) | ~0 | minutes | Fig 2 | Explicit | Capsules release immediately. |

### **4.3 Global Order:**

*   **Vector ID:** M4.3
*   **Vector Type:** Order
    *   Content: The global order is the directed transport of alginate capsules containing living cells towards the source of higher NaCl concentration. This is a spatiotemporal order, where the droplet and capsule system moves in a coordinated manner over macroscopic distances. The selectivity for living cells is also a form of emergent order in terms of cargo transported. At a higher level of abstraction, the system exhibits a rudimentary form of "autoselective" behavior.
    *   CT-GIN Mapping: Defines a `ConfigurationalNode`: `configurationType: Directed Transport, Selective Cargo Transport`, `spatialOrder: Directed motion towards salt gradient`, `temporalOrder: Sustained transport over time`, `cargoSelectivity: Living cells vs Dead cells/Empty capsules`.
    * **Implicit/Explicit**: Mixed
        *  Justification: The directed transport and selective transport are explicitly demonstrated and described in the results.  The characterization as "global order" and "autoselective behavior" is an interpretation and thus implicit, framing the observed behavior in terms of self-organization and emergence.

### **4.4 Predictability of Global Order:**

*   **Vector ID:** M4.4
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The directed transport of capsules with living cells is highly predictable when biosurfactants are present. The paper reports "10 successful transports out of 10 transport trials" for capsules polymerized using lung cancer cell-DMEM supernatant. The lack of transport for empty capsules or capsules with dead cells is also highly predictable ("10 releases out of 10 trials").  Predictability is high under controlled experimental conditions. However, factors like subtle variations in surfactant concentration, droplet size, or external disturbances could introduce some variability. Qualitative assessment: High predictability under defined conditions.
    * **Implicit/Explicit**: Mixed
    *  Justification: The high success rate of transport and release under different conditions are explicitly stated experimental results. The "predictability score" is a qualitative assessment based on these results and general understanding that experimental systems have some degree of inherent variability.
    *   CT-GIN Mapping: Contributes to the `AdjunctionEdge` weight: `predictabilityScore: 8`.

### **4.5. Local Interaction Rules (for Self-Organization)**
* **Vector ID:** M4.5
* **Vector Type:** Table
*   Table:
| Rule ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Source |
| :------ | :---------- | :-------- | :---------- | :---------- | :----------------: | :------------: | :-----: |
| 1 | Surface Tension Dependence on NaCl  | NaCl Concentration | 0 - 1.5 | M | Explicit | Surface tension measured with varying NaCl concentration (via 1:1 mixing with 3M NaCl) | Fig 5 |
| 2 | Surfactant Effect on Interfacial Tension | Surfactant Type (Biosurfactant vs Decanoate) | Qualitative (Presence/Absence, Different types) | N/A | Explicit | Surface tension difference observed with and without biosurfactants and decanoate in Fig 4, 5 | Fig 4, 5 |
| 3 | Adhesion Strength vs Surfactant | Surfactant Concentration (Diluted Supernatant) | Dilutions: 1:1, 1:5, 1:10, 1:20, Pure DMEM, Pure Water, BT Cells Supernatant | N/A | Explicit | Association time measured for different dilutions of supernatant containing surfactants, different controls in Fig 2 | Fig 2 |

### **4.6. Globally Emergent Order and Order Parameters**
* **Vector ID:** M4.6
* **Vector Type:** Table
*   Table:
| Property ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Protocol | Source |
| :---------- | :---------- | :-------- | :---------- | :---------- | :----------------: | :------------: | :------: | :-----: |
| 1 | Chemotactic Velocity | Droplet Velocity in DMEM only | 0.0131 ± 0.002 | cm/sec | Explicit | Velocity reported for DMEM only control | Results | Text |
| 2 | Chemotactic Distance  | Path Length in DMEM only | 56 ± 3 | % of total distance | Explicit | Path length for DMEM only control, percentage of total distance between droplet and salt starting point | Results | Text |
| 3 | Transport Success Rate (Live Cells) | Successful transports/total trials | 10/10 | N/A | Explicit | Transport of capsules with living cells is efficient in every trial | Results | Text |
| 4 | Transport Success Rate (Dead/Empty) | Successful transports/total trials | 0/10 | N/A | Explicit | Empty capsules and capsules with BT cells are released immediately | Results | Text |
| 5 | Capsule-Droplet Association Time (Live Cells) | Association Time | ~90 | minutes | Explicit | Association time for capsules produced from supernatant of living cells | Results, Fig 2 | Fig 2, Text |

### **4.7 Yoneda Embedding and Local-to-Global Mapping Fidelity**

*   **Vector ID:** M4.7
*   **Vector Type:** Table
*   Table:
    | Link Type | Description | Predictability | Yoneda Score | Metrics | Implicit/Explicit | Justification | Source |
    | :-------- | :---------- | :------------- | :----------- | :------ | :----------------: | :------------: | :-----: |
     | Local Rules -> Transport | Local Surface Tension Gradients -> Directed transport of cells | High | 7 | Transport Success Rate, Capsule-Droplet Association Time | Mixed | High predictability of transport outcome given local surfactant and salt conditions observed experimentally | Results, Fig 2, Text |
    *   **Yoneda Embedding Fulfillment Score [0-10]:** [7]
    *   **Metrics:**  [Transport Success Rate; Capsule-Droplet Association Time]
    *   **Justification:** The Yoneda score of 7 reflects a strong but not perfect mapping from local interaction rules to the emergent global behavior of directed and selective transport. The metrics used (transport success rate and association time) directly quantify the emergent order and its dependence on experimental conditions representing local rules (surfactant presence, salt gradient).

## M5: Computation
*   **Vector ID:** M5
*   **Vector Type:** Computation

### **5.1 Embodied Computation Presence:**

*   **Vector ID:** M5.1
*   **Vector Type:** Binary
    *   Content: [No]
    *   Justification: The system does not perform explicit computation. The droplet motion and selective transport are based on physicochemical responses to the external chemical gradient and surfactant presence. While there are interactions and responses within the system, they do not constitute computational primitives or logical operations in a meaningful sense. The system reacts to stimuli, but doesn't process information to perform calculations or solve problems beyond this basic responsivity. The system selects living cells based on surfactant production, but this selection is a physical outcome of interfacial interactions, not a computational decision.
    *    Implicit/Explicit: Implicit
        *  Justification:  The paper describes a physical system that reacts to its environment.  The absence of embodied computation is inferred from the lack of any description of information processing, logical operations, or units performing calculations. The system's behavior is explained by physics and chemistry, not computational algorithms.

## M6: Temporal Dynamics
*   **Vector ID:** M6
*   **Vector Type:** Temporal

### **6.1 Timescales:**

*   **Vector ID:** M6.1
*   **Vector Type:** ParameterTable
    *   Table:
        | Timescale Description | Value | Units | Source | Implicit/Explicit | Justification |
        | :-------------------- | :---: | :---: | :----: | :----------------: | :------------: |
        | Capsule Incubation Time in DMEM | 2 | days | Methods, Alginate hydrogel and capsule formation. | Explicit | Duration of cell incubation in capsules. |
        | Capsule-Droplet Association Time (Living Cells) | ~90 | minutes | Results, Fig 2 | Explicit | Time capsule remains associated with droplet. |
        | Transport Time (Qualitative) | Minutes to hours | Implicit | Observation of chemotaxis, Movie S1 | Implicit | Based on description of transport experiments and supplementary movies. |
        | Cell Viability Assay Incubation (MTT) | 3 | hours | Methods, Transport and cell viability assessment | Explicit | Incubation for MTT assay. |
        | Cell Proliferation Assessment Time to Confluence (After Transport) | 3 | weeks | Results, Cell survival after transport | Explicit | Time to reach confluence after being plated after transport. Compared to 2 weeks for cells before transport. |

### **6.2 Active Inference:**

*   **Vector ID:** M6.2
*   **Vector Type:** Assessment
    *   Content: [No]
    *   Justification: There is no evidence of active inference in this system. The droplet does not have an internal model of its environment, nor does it predict future states or select actions to minimize prediction error. The chemotactic movement is a purely reactive response to the instantaneous salt gradient. The system does not "learn" about its environment or adapt its behavior beyond the immediate stimulus-response cycle. There's no indication of prediction, anticipation, or internal model updating.
    *   Implicit/Explicit: Implicit
        *  Justification: The paper describes a reactive system, responding directly to external stimuli. Active inference requires internal models and predictive behavior, which are absent in the system description and experimental results. The system lacks any mechanism for prediction or model updating.

## M7: Adaptation
*   **Vector ID:** M7
*   **Vector Type:** Adaptation

### **7.1 Adaptive Plasticity Presence:**

*   **Vector ID:** M7.1
*   **Vector Type:** Binary
    *   Content: [No]
    *   Justification:  The system does not exhibit adaptive plasticity. The droplet chemotaxis and selective transport are fixed behaviors determined by the physicochemical properties of the components and their interactions. There is no mechanism for the system to change its behavior or internal structure in response to experience over time to improve performance or alter functionality. The system responds to the presence of biosurfactants and salt gradient in a predetermined way. The viability of cells might change over time or different conditions but the transport system itself doesn't adapt.
    *    Implicit/Explicit: Implicit
        * Justification: The system's behavior is consistently described as a stimulus-response system without any indication of persistent changes based on experience or feedback loops that would lead to adaptive behavior.

## M8: Emergent Behaviors
*   **Vector ID:** M8
*   **Vector Type:** Behavior

### **8.1 Behavior Description:**

*   **Vector ID:** M8.1
*   **Vector Type:** Description
    *   Content: The main emergent behaviors are:
        1.  **Chemotactic Transport:** Directed motion of the decanol droplet towards higher NaCl concentration.
        2.  **Autoselective Capsule Transport:** Selective transport of alginate capsules containing living lung cancer cells, but not empty capsules or capsules with dead cells. This selectivity arises spontaneously from the interaction of the artificial droplet system and the biological cells' biosurfactant production.
    These behaviors are emergent because they arise from the interplay of multiple components (droplet, surfactant, salt gradient, cells, capsules) and are not properties of any single component in isolation. The "autoselectivity" is particularly emergent as it's a system-level property arising from the interaction of artificial and biological subsystems.
    *   CT-GIN Mapping: Defines the `BehaviorArchetypeNode`. `behaviorType: Chemotactic Transport, Autoselective Capsule Transport`, `description: Directed droplet motion towards salt gradient, Selective transport of living surfacant-producing cells`.
    *    Implicit/Explicit: Mixed
       *  Justification: The chemotactic transport and selective transport are explicitly observed and described results of the experiments. The characterization of these behaviors as "emergent" is an interpretation, but strongly supported by the system description: the behaviors arise from interactions between components and are not pre-programmed or externally controlled in a direct way, thus implied emergence.

### **8.2 Behavior Robustness:**

*   **Vector ID:** M8.2
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The chemotactic transport and autoselectivity are shown to be reasonably robust under the tested conditions. The 10/10 success rate suggests reliability. Robustness is demonstrated across different lung cancer cell lines. The system is shown to function with variations in surfactant source (biosurfactants, decanoate). However, robustness to significant changes in environmental conditions (temperature, flow variations, complex chemical environments), droplet size variations, or capsule properties is not explicitly tested or quantified.  Qualitative Assessment: Moderately Robust under tested conditions.
    *   Implicit/Explicit: Mixed
        *  Justification: High success rates suggest robustness under tested experimental conditions, this is explicit in the quantitative results.  Limitations in robustness assessment (lack of testing under drastically different conditions) are implicit, inferred from considering the scope of experimental variation explored in the paper.
    *   CT-GIN Mapping: This score contributes to the reliability attributes of the `BehaviorArchetypeNode`: `robustnessScore: 7`.

### **8.3 CT-GIN Emergent Behavior Validation**

*    **Vector ID:** M8.3
*    **Vector Type:** Validation
     *  Content: Validation methods include:
        1.  **Controlled Experiments:** Comparing transport of capsules with living cells vs. dead cells vs. empty capsules to demonstrate autoselectivity (Results, Autoselective transport).
        2.  **Quantitative Assays:** Measuring capsule-droplet association time (Fig 2) and surface tension changes (Figs 4, 5) to quantify the role of biosurfactants and surface tension gradients in transport.
        3.  **Viability Assays:** Assessing cell viability before and after transport (Fig 3, Table 1) to evaluate the impact of the transport process on cell survival.
        4.  **Control Conditions:** Testing transport in pure DMEM, DMEM with dead cells supernatant, DMEM with empty capsules supernatant to establish the necessity of living cell-produced surfactants for efficient chemotaxis (Results, chemotaxis feasibility; Fig 4, 5).
        5.  **Reproducibility:** Reporting replicates (typically 10) for association tests and chemotaxis trials, and triplicates for viability assays demonstrating reproducibility under given conditions (Methods section throughout).
    Limitations: Robustness to a wider range of environmental perturbations and long-term operational reliability are not systematically assessed.
     *   Implicit/Explicit: Explicit
    *   Justification: Validation methods are explicitly described in the "Results" and "Methods" sections, referencing figures and tables as indicated. The description of controls, quantitative measurements, and replicates is direct from the text. Limitations are implicitly noted by the scope of experiments performed and lack of broader stress-testing.

## M9: Cognitive Proximity
*   **Vector ID:** M9
*   **Vector Type:** Cognition

### **9.1 Cognitive Mapping:**

*   **Vector ID:** M9.1
*   **Vector Type:** Description
    *   Content: The paper draws an analogy between the droplet system and basic aspects of living systems' behavior, particularly chemotaxis and selective cargo transport. It suggests the system demonstrates a "primitive example of how self-motile systems may be produced that can also be selective for the types of cargo transported" and hints at future extension to "demarcation between different types of mammalian cells…due to stage of differentiation, production of key markers, and perhaps potency." The "autoselectivity" for living cells is metaphorically connected to "distinguishing between living versus dead cells with selectivity emerging through the interface of artificial life systems with natural living systems." Limitations: These are metaphorical mappings; the system lacks higher-level cognitive functions.
    *   CT-GIN Mapping: `CognitiveMappingEdge` from `BehaviorArchetypeNode: Autoselective Capsule Transport` to `CognitiveFunctionNode: Basic Chemotaxis, Primitive Discrimination`.
    *   Implicit/Explicit: Mixed
    * Justification: The paper explicitly uses terms like "autoselective" and draws comparisons to "life-like behaviors" and "primitive example of how self-motile systems may be produced that can also be selective". These are explicit attempts at cognitive framing. However, the understanding of these as analogies and limitations to basic biological behaviours is implicit in the overall scientific and technical tone, and the lack of claims for higher cognitive functionalities.

### **9.2 Cognitive Proximity Score:**

*   **Vector ID:** M9.2
*   **Vector Type:** Score
    *   Score: [2]
    *   Justification: Level 2: Sub-Organismal Responsivity. The system exhibits a basic form of selective response (transporting living cells), which could be loosely analogized to rudimentary discrimination. However, it lacks complex representation, goal-directedness beyond reacting to a chemical gradient, memory, learning, or any higher-level cognitive functions. The system's "selectivity" is based on a simple physicochemical interaction (surfactant-mediated adhesion), not a complex decision-making process. It is beyond simple stimulus-response (Level 1) due to the emergent selective transport behavior, but it’s far from reactive/adaptive autonomy (Level 3) or goal-directed cognition (Level 4).
    *   Implicit/Explicit: Mixed
    *  Justification: Score is based on applying the *CT-GIN Cognizance Scale*. Justification uses explicit descriptions of the system's behavior from the paper (selective transport) and contrasts it implicitly with higher levels of cognitive complexity which are clearly absent. The scoring is thus mixed, based on explicit behaviour and implicit lack of higher functions in the context of the provided scale.

### **9.3 Cognitive Function Checklist**

* **Vector ID:** M9.3
* **Vector Type:** Checklist
    *   | Cognitive Function               | Score (0-10) | Justification/Notes                                                                       | CT-GIN Mapping (if applicable) | Implicit/Explicit | Justification for Implicit/Explicit/Mixed |
    | :-------------------------------- | :----------: | :------------------------------------------------------------------------------------ | :--------------------------------: | :-----------------:|:-----------------:|
    | Sensing/Perception               |      4       | Senses chemical gradient (NaCl), indirectly "senses" surfactant presence through interfacial properties. Basic sensing mediated by physical interactions. Limited range of sensory inputs.                     | `CognitiveFunctionNode: Sensing/Perception` | Mixed | Sensing of NaCl concentration via physical response is implicit. Indirect 'sensing' of surfactant is inferred from selective behavior. Range and complexity are implicitly limited. |
    | Memory (Short-Term/Working)        |      0       | Absent. No short-term retention or manipulation of information. Reacts to immediate stimuli only.                                                                                       | N/A | Implicit | Absence of memory is inferred from system description and lack of any mention of memory mechanisms. |
    | Memory (Long-Term)                 |      0       | Absent. No long-term storage or retrieval of information. System state not persistently modified by past experiences affecting future actions.                                                                                       | N/A | Implicit | Absence of memory is inferred as above. |
    | Learning/Adaptation              |      0       | Absent. No adaptive behavior, performance improvement based on experience, or change in internal structure over time in response to interaction history.                                                                                       | N/A | Implicit | Absence of learning and adaptation is inferred from the static stimulus-response nature of the system. |
    | Decision-Making/Planning          |      1       | Rudimentary "decision" to move towards higher salt. Not based on complex evaluation or planning, but a direct physical response to gradient. Selection between living/dead cargo is a passive outcome of interaction. | `CognitiveFunctionNode: Decision-Making/Planning` | Mixed | Basic directionality of motion implies rudimentary "decision," though mechanistic not cognitive. Lack of planning or complex choice is implicit. |
    | Communication/Social Interaction |      0       | Absent. The droplet acts in isolation, no communication or interaction with other agents or systems performing similar or cooperative tasks.                                                                                       | N/A | Implicit | Social interaction/communication is clearly absent from the system description. |
    | Goal-Directed Behavior            |      2       | Weakly goal-directed (towards higher salt concentration). Can be seen as a rudimentary goal, but driven by physics, not internally represented goals or purposes.                                                                                       | `CognitiveFunctionNode: Goal-Directed Behavior` | Mixed | Directional movement can be interpreted as weakly goal-directed, however, the nature is physical not intentional, inferred limit. |
    | Model-Based Reasoning              |      0       | Absent. No internal model of the environment, no reasoning or inference based on a model. Behavior is purely reactive, not model-based predictive.                                                                                       | N/A | Implicit | Model-based reasoning is entirely absent from the system mechanisms and descriptions. |
    | **Overall score**                 |      [1]       |                                                                                       |                                   |                     |                |

## M10: Criticality Assessment
*   **Vector ID:** M10
*   **Vector Type:** Criticality

### **10.1 Criticality:**

*   **Vector ID:** M10.1
*   **Vector Type:** Assessment
    *   Content: [Unclear]
    *   Justification: The paper does not explicitly address criticality or the system's operation near a critical point.  Marangoni instabilities themselves can sometimes exhibit complex dynamics and pattern formation that could potentially be related to criticality, but this is not discussed in the context of this specific system. There is no evidence presented for scale-free behavior, power laws, or long-range correlations. The system seems to operate in a relatively stable regime, driven by a controlled external gradient and surfactant effect.  More detailed analysis of droplet dynamics and interfacial fluctuations would be needed to assess criticality.
        *   Critical Parameters (If Yes/Partial): N/A
        *   Evidence: N/A
    *   Implicit/Explicit: Implicit
    *    Justification: Criticality is not mentioned, assessed or implied in the text. Its relevance to Marangoni systems is background knowledge, but not applied to the described experiments, hence assessment "Unclear" relying on absence of evidence in paper.

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
| Energy Flow Efficiency          | No                         | N/A                                 | Efficiency not quantified                                                       | Quantify efficiency, explore energy recycling or more efficient transduction mechanisms. |
| Memory Fidelity                 | No                         | N/A                                 | No memory demonstrated                                                          | Implement memory mechanism, investigate structural or chemical memory elements. |
| Organizational Complexity       | Partial                    | Capsule-Droplet Association Time ~90 minutes, Transport Success Rate 10/10          | Level of organization is basic, primarily driven by external gradient.             | Explore more complex self-organizing structures, internal feedback loops for order. |
| Embodied Computation            | No                         | N/A                                 | No computational primitives demonstrated                                          | Integrate computational elements, explore analog computation in droplet system |
| Temporal Integration            | No                         | Timescales defined for experiment duration. | No integration of past events into future behavior (memory absent)              | Implement temporal memory, investigate temporal coding and processing.      |
| Adaptive Plasticity             | No                         | N/A                                 | No adaptive plasticity demonstrated                                             | Introduce mechanisms for adaptation, explore feedback-driven parameter changes. |
| Functional Universality         | No                         | Autoselective transport demonstrated.   | Functionality limited to transport, selectivity based on surfactant production. | Expand functionality, explore multi-functional materials and behaviors.     |
| Cognitive Proximity            | No                         | Cognitive Proximity Score: 2          | Very low cognitive proximity, lacks higher cognitive functions                       | Develop higher cognitive functions (memory, learning, planning).             |
| Design Scalability & Robustness | Partial                    | Robustness score 7, 10/10 success rate. | Robustness not tested against wide range of perturbations. Scalability not discussed. | Systematically test robustness, evaluate scalability for larger-scale systems.   |
| **Overall CT-GIN Readiness Score** |        |   |   |      |


### **13.2 Qualitative CT-GIN Assessment Conclusion:**

*   **Vector ID:** M13.2
*   **Vector Type:** Textual Summary
    *   Content: The droplet-based chemotactic transport system demonstrates a basic form of emergent behavior: autoselective transport of living cells. Key strengths are the clear implementation of chemotaxis, the demonstration of selectivity based on biosurfactants, and reasonable robustness under tested conditions. Key limitations are the lack of memory, computation, adaptation, and low cognitive proximity. Energy efficiency is likely low, though not quantified. Organizational complexity is limited, primarily driven by external gradients. Overall assessment: The system represents a Level 2 on the CT-GIN Cognizance Scale, showing sub-organismal responsivity. It's a well-executed experimental demonstration of emergent behavior in a hybrid artificial-biological system, but falls short of exhibiting features of truly cognizant matter due to the absence of memory, computation, and adaptive plasticity. Potential within CT-GIN is moderate, providing a platform for exploring more complex functionalities by integrating memory or adaptive elements in future research.

### **13.3 CT-GIN Refinement Directions:**

*   **Vector ID:** M13.3
*   **Vector Type:** Recommendations
    *   * Integrate a Memory Mechanism: Introduce components that can retain information about past transport events or environmental conditions to influence future droplet behavior. Explore phase-change materials or chemical gradients that persist over time as potential memory elements within the droplet or capsule system.
    *   * Implement Embodied Computation: Incorporate elements that can perform basic analog computation within the material system, potentially using droplet dynamics or interfacial properties to realize computational primitives. Investigate reaction-diffusion systems or non-linear chemical reaction networks within the droplet or capsule for computation.
    *   * Introduce Adaptive Plasticity: Design mechanisms that allow
