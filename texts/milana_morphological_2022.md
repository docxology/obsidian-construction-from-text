# Morphological Control of Cilia-Inspired Asymmetric Movements Using Nonlinear Soft Inflatable Actuators

__Paper Type:__ Experimental

## M1: System Overview & Implementation
*   **Vector ID:** M1
*   **Vector Type:** Overview

### **1.1 System Description**

*   **Vector ID:** M1.1
*   **Vector Type:** Description
    *   Content: The system is a soft robotic cilia array inspired by biological cilia, designed for asymmetric movements using morphological control. It consists of nonlinear soft bending actuators made from a cylindrical latex balloon inside a flexible PVC shell with circumferential slits. These actuators exhibit a nonlinear pressure-volume relationship with snap-through instability. Two types of systems are demonstrated: a single artificial cilium with two stacked actuators for spatial asymmetry and an array of four actuators for metachronal wave motion. Both systems are driven by a single pressure input. The purpose is to simplify control of soft robotic cilia and reduce tethering by using morphological control, harnessing the physical properties of the actuators to generate complex movements without dedicated control loops for each actuator.
    *   CT-GIN Mapping: `SystemNode` attributes: `systemType: Soft Robot`, `domain: Robotics, Microfluidics`, `mechanism: Morphological Control, Nonlinear Actuation`, `components: Nonlinear soft bending actuators, PVC shell, Latex balloon, Flow restrictors`, `purpose: Cilia-inspired asymmetric motion, Fluid propulsion, Simplified control`
    *   Implicit/Explicit: Explicit
        *  Justification: The system description, components, and purpose are explicitly stated in the abstract, introduction, materials and methods, results and discussion, and conclusion sections of the paper.

### **1.2 Implementation Clarity**

*   **Vector ID:** M1.2
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The implementation is relatively clear, with detailed descriptions of the actuator design, materials, and experimental setups for both spatial asymmetry and metachronal wave demonstrations in the Materials and Methods and Results and Discussion sections, including schematic representations (Figure 3B, 4B) and experimental images (Figure 2B, 3E, 4C). The paper provides sufficient details to understand the construction, operating principles, and experimental validation methods. However, some fabrication details, such as the precise gluing method for luer locks and the precise dimensions of the slits, are not exhaustively detailed but are standard soft robotics techniques.
    *   Implicit/Explicit: Mixed
        * Justification: Clarity is high due to explicit descriptions and figures (Explicit). Some minor fabrication details are implicitly assumed to be known standard soft robotics techniques (Implicit).

### **1.3 Key Parameters**

*   **Vector ID:** M1.3
*   **Vector Type:** ParameterTable
    *   Table:
        | Parameter Name | Value | Units | Source (Fig/Table/Section) | Implicit/Explicit | Data Reliability (High/Medium/Low) | Derivation Method (if Implicit) |
        | :------------- | :---: | :---: | :-----------------------: | :-----------------: | :-----------------------------: | :-------------------------------: |
        | PVC Shell Outer Diameter | 11.2 | mm | Materials and Methods | Explicit | High | N/A |
        | PVC Shell Inner Diameter | 8 | mm | Materials and Methods | Explicit | High | N/A |
        | Latex Balloon Wall Thickness | 0.8 | mm | Materials and Methods | Explicit | High | N/A |
        | Slit Spacing | 5 | mm | Materials and Methods | Explicit | High | N/A |
        | Flow Restrictor Inner Diameter | 0.2 | mm | Materials and Methods | Explicit | High | N/A |

    *   **Note:** List *up to 5* key parameters characterizing the system's *implementation*.  Provide values and units if possible. If a parameter is not explicitly stated but derived/inferred, clearly state the derivation method. *Always* include units if applicable. If a value is not applicable, write "N/A".  Data Reliability: High = Directly measured, Medium = Derived from measurements/simulations, Low = Estimated/Inferred.

## M2: Energy Flow
*   **Vector ID:** M2
*   **Vector Type:** Energy

### **2.1 Energy Input**

*   **Vector ID:** M2.1
*   **Vector Type:** Input
    *   Content: The primary energy source is pneumatic pressure supplied by a proportional valve (Festo MPPES-3-1). The air pressure inflates the actuators causing deformation. For the spatial asymmetry setup the input pressure is ramped up and down between 0 and 0.3MPa. For the metachrony setup, a trapezoidal pressure input to 0.3MPa is used.
    *   Value: 0 - 0.3
    *   Units: MPa
    *   CT-GIN Mapping: `EnergyInputNode`: attributes - `source: Pneumatic Pressure`, `type: Pressure`
    *   Implicit/Explicit: Explicit
        *  Justification: The energy source, type, and pressure values are explicitly mentioned in the Materials and Methods and Results sections. Proportional valve and pressure range are stated explicitly.

### **2.2 Energy Transduction**

*   **Vector ID:** M2.2
*   **Vector Type:** Transduction
    *   Content: The energy transduction begins with pneumatic pressure from the external source. This pneumatic pressure energy is transduced into mechanical strain energy within the latex balloon and PVC shell of the actuators. The pressure causes volumetric expansion of the balloon, which is constrained by the PVC shell and slits, leading to bending deformation due to the differential expansion dictated by the slit pattern. The shape of the pressure-volume curve and snap-through instability are crucial for controlling the sequence of bending.  Further transduction into kinetic energy takes place during the dynamic bending motion of the cilia.
    *   CT-GIN Mapping: `EnergyTransductionEdge`: attributes - `mechanism: Pneumatic to Mechanical`, `from_node: EnergyInputNode`, `to_node: ActuatorNode(Mechanical Strain Energy)`
    *   Implicit/Explicit: Mixed
        *  Justification: The basic transduction from pneumatic to mechanical energy is explicit through describing inflation and bending. The details of strain energy and precise mechanisms of snap-through are implicit, inferred from the description of nonlinear actuator behavior and the context of soft robotics, although supported by cited references (Overvelde et al., 2015).

### **2.3 Energy Efficiency**

*   **Vector ID:** M2.3
*   **Vector Type:** Score
    *   Score: [4]
    *   Justification/Metrics: The energy efficiency is likely low to medium. Pneumatic actuation in soft robotics is generally not highly energy efficient due to losses in air compression, valve operation, and material hysteresis. The paper does not provide quantitative efficiency metrics. Qualitatively, energy is dissipated through heat generation in the proportional valve, frictional losses in air flow through tubing and restrictors, and hysteresis and internal friction within the deforming latex and PVC materials. The snap-through mechanism, while crucial for control, may also contribute to energy loss due to rapid, non-conservative deformations.  The system utilizes morphological control to simplify the *control scheme*, not necessarily to maximize energy efficiency of actuation itself.
    *   CT-GIN Mapping: Attribute of relevant `EnergyTransductionEdge`s:  `efficiency_score: 4`, `efficiency_qualitative: Low to Medium`
    *   Implicit/Explicit: Implicit
      *  Justification: The score and justification are based on general knowledge of pneumatic systems and soft robotics, and implicit understanding that morphological control prioritizes simplicity over maximal energy efficiency in this context. No explicit efficiency metrics are provided in the paper.

### **2.4 Energy Dissipation**

*   **Vector ID:** M2.4
*   **Vector Type:** Dissipation
    *   Content: Energy dissipation mechanisms include:
        1.  **Valve losses:** The proportional valve (Festo MPPES-3-1) will dissipate energy as heat due to electrical resistance and internal friction of moving parts.
        2.  **Fluid resistance:** Air flow through the tubing and flow restrictors involves viscous dissipation, converting pneumatic energy into heat.  This is explicitly harnessed for morphological control in the metachronal wave setup, but still represents dissipation.
        3.  **Material hysteresis:** The latex balloon and PVC shell will exhibit viscoelastic behavior, causing energy loss as heat during deformation and relaxation cycles due to internal friction and non-ideal elastic response of the polymers.
        4.  **Friction:**  Friction between the latex balloon and PVC shell, though likely minimal due to lubrication by air pressure, could contribute to dissipation.
    Quantification is not provided in the paper, so qualitative assessment is Medium for valve and fluid resistance, and likely Medium-High for material hysteresis given the large deformations.
    *   CT-GIN Mapping: Creates `EnergyDissipationNode`s: `ValveDissipation`, `FluidResistanceDissipation`, `MaterialHysteresisDissipation`; and `EnergyDissipationEdge`s from `EnergyTransductionEdge` to each dissipation node.
    *    Implicit/Explicit: Mixed
        *  Justification: Dissipation mechanisms are inferred from general physics principles and knowledge of pneumatic and soft robotic systems (Implicit). Valve, fluid resistance, and material hysteresis are standard dissipation sources in such systems (Inferred).  The specific valve model is mentioned (Explicit), allowing inference about valve related dissipation.

## M3: Memory
*   **Vector ID:** M3
*   **Vector Type:** Memory

### **3.1 Memory Presence:**

*   **Vector ID:** M3.1
*   **Vector Type:** Binary
    *   Content: No
    *   Justification: The system, as presented, does not exhibit memory in the sense of a persistent change in system state that influences future behavior beyond the immediate stimulus. The actuators respond to instantaneous pressure changes, and the sequence of movements is determined by the morphological design and pressure input profile, not by past states or experiences. While the actuators exhibit bistability, this contributes to the *sequencing* of actions rather than memory of past inputs or states. The state of the system is directly tied to the current applied pressure.
    *    Implicit/Explicit: Explicit
        * Justification: The absence of memory is inferred from the description of the system's operation, which focuses on immediate, pressure-driven responses and lacks any mechanism for internal state persistence beyond the current pressure and actuator configuration (Implicit). The paper explicitly describes morphological control as harnessing passive mechanical characteristics, which usually does not entail memory (Explicit).

## M4: Self-Organization and Emergent Order
*   **Vector ID:** M4
*   **Vector Type:** Self-Organization

### **4.1 Self-Organization Presence:**

*   **Vector ID:** M4.1
*   **Vector Type:** Binary
    *   Content: Yes
    *   Justification:  The system exhibits a degree of self-organization in the emergence of coordinated, sequential motions within the cilia array from a single, global pressure input. The global order, in the form of asymmetric cilia movements and metachronal waves, emerges from the *local* interactions between actuators, flow restrictors, and their nonlinear pressure-volume characteristics, without external control dictating each actuator's individual motion. The pre-programmed sequence arises from the embodied morphology, specifically, from the tuned nonlinearities and fluidic interactions, demonstrating a spontaneous organization of movement patterns beyond simple independent actuator responses.
    *   Implicit/Explicit: Mixed
        *  Justification: The emergence of global order (asymmetric movements and metachronal waves) from local interactions (actuator dynamics and fluid flow) is implicitly demonstrated and claimed as morphological control (Implicit). The paper explicitly states that morphological control harnesses passive mechanical characteristics to simplify control, suggesting self-organization (Explicit).

### **4.2 Local Interaction Rules:**

*   **Vector ID:** M4.2
*   **Vector Type:** Rules
    *   Content: The local interaction rules are governed by fluidic principles and actuator mechanics:
        1.  **Actuator Pressure-Volume Relationship:** Each actuator follows a nonlinear pressure-volume (PV) curve with a peak and valley. This intrinsic property dictates how the volume and curvature change in response to pressure, incorporating snap-through instabilities. These curves are empirically measured and used in simulations.
        2.  **Fluid Flow Dynamics through Restrictors (Metachronal Setup):** In the metachronal setup, narrow tubes act as flow restrictors between actuators. The pressure drop across a restrictor (Δpᵢ) is modeled using Darcy-Weisbach law (Equation 3) or simplified for laminar flow (Equation 4), relating pressure drop to flow rate (qᵢ), fluid properties (density ρ, dynamic viscosity μ), restrictor dimensions (length Lᵢ, inner diameter dᵢ). This introduces time delays and sequential actuation.
        3.  **Actuator Interconnection (Spatial Asymmetry Setup Configuration 4):** In spatial asymmetry configuration 4, a silicone plug with a needle acts as a flow restrictor between two actuators, dynamically controlling pressure difference between them.
        4.  **Quasi-Static Interaction (No Restrictors):** In configurations 2 and 3 of spatial asymmetry and the initial metachronal setup without restrictors, actuators interact quasi-statically, where pressure is approximately uniform across the system (Equation 5), and actuator volumes are determined by their PV curves at the common pressure.
    *   CT-GIN Mapping: Part of the `AdjunctionEdge` description (local side). These define the "LocalInteraction" category of edges. Attributes include: `interactionType: Fluidic, Mechanical`, `governingEquations: PV Curve, Darcy-Weisbach Law (or laminar flow simplification), Quasi-Static Pressure Equilibrium`.
    * **Implicit/Explicit**: Mixed
        *  Justification:  The PV curves and their importance are explicitly described and measured (Explicit). The fluid dynamics equations (Darcy-Weisbach, laminar flow) and quasi-static approximation are also explicitly presented and used in simulations (Explicit). The interpretation of these equations as *local interaction rules* governing the system's self-organization is implicit but strongly supported by the context of morphological control (Implicit).

### **4.2.1 Local Interaction Parameters:**

* **Vector ID:** M4.2.1
* **Vector Type:** Table
*   Table:
    | Rule ID | Description | Parameter Name | Parameter Value Range | Units | Data Source | Implicit/Explicit | Justification |
    | :------ | :---------- | :------------- | :---------- | :---: | :----------: | :----------------: | :------------: |
    | 1       | Actuator PV Curve | Latex Balloon Outer Diameter | 3.2, 4.8, 6.4 | mm  | Fig 2A          | Explicit       | Different actuator types are defined by this parameter, directly affecting PV curve and thus local interaction. |
    | 2       | Flow Restrictor | Restrictor Inner Diameter | 0.2, 2 (spatial asymmetry) | mm  | Materials and Methods, SI | Explicit       | Defines fluid resistance and pressure drop, hence temporal coupling in metachronal array. |
    | 2       | Flow Restrictor | Restrictor Length | 0.5, 10 (spatial asymmetry) | m, mm | Materials and Methods, SI | Explicit       | Defines fluid resistance and pressure drop. |
    | 2       | Flow Restrictor | Fluid Density (ρ) | 1.78 | kg/m³ | Eq. (3)          | Explicit       | Parameter in Darcy-Weisbach. Constant is assumed. |
    | 2       | Flow Restrictor | Darcy Friction Factor (f<0xE2><0x82><0x93><0x9E>) | 0.04 | unitless| Eq. (3)          | Explicit       | Parameter in Darcy-Weisbach. Constant is assumed. |
### **4.3 Global Order:**

*   **Vector ID:** M4.3
*   **Vector Type:** Order
    *   Content: The global order that emerges is:
        1.  **Spatial Asymmetry:** For the single artificial cilium, a nonreciprocal movement pattern emerges, resulting in a swept area that mimics the asymmetric stroke of biological cilia. This is visually evident in the simulated and experimental trajectories (Figure 3D, 3E, and Supplementary Movies S1-S3). The swept area itself quantifies the global order (Figure 3F).
        2.  **Metachronal Wave:** For the cilia array, a wave-like sequential bending motion propagates across the array. This metachronal wave is observed spatiotemporally in the kymographs (Figure 4E) and visualized in Figure 4C and Supplementary Movie S4, S5. The wave speed and phase shift between cilia quantify the global order (Figure 4E, and associated analysis in Results and Discussion).
    *   CT-GIN Mapping: Defines a `ConfigurationalNode`: Attributes for Spatial Asymmetry - `orderType: Nonreciprocal motion`, `quantifier: Swept Area (mm²)`. Attributes for Metachronal Wave - `orderType: Sequential Bending Wave`, `quantifier: Wave Speed (mm/s), Phase Shift (rad)`.
    * **Implicit/Explicit**: Explicit
        *  Justification: The descriptions of spatial asymmetry and metachronal wave as emergent global orders are explicitly presented in the Results and Discussion section, supported by experimental and simulation visualizations and quantified metrics (swept area, wave speed, phase shift) (Explicit).

### **4.4 Predictability of Global Order:**

*   **Vector ID:** M4.4
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The global order is reasonably predictable, especially given the simulations closely match experimental outcomes (Figure 3F, 4D). The swept area and metachronal wave characteristics (speed, phase shift) are quantitatively predicted by the lumped fluidic system simulations based on empirically measured actuator PV and KV curves. Correlation between simulation and experiment is shown in Figure 3F and 4D. However, predictability is not perfect due to potential variations in actuator fabrication, experimental noise, and simplifications in the fluidic model (e.g., constant fluid properties, lumped parameter approximation). The system behavior is designed to be predictable given the input pressure profile and actuator morphology, but some deviations exist in practice.
    * **Implicit/Explicit**: Mixed
    *  Justification: The predictability is explicitly supported by the simulations' agreement with experiments and quantifiable metrics are used (swept area correlation) (Explicit). Limitations to perfect predictability due to fabrication variations and model simplifications are implicitly acknowledged by the general nature of experimental research (Implicit).

### **4.5. Local Interaction Rules (for Self-Organization)**
* **Vector ID:** M4.5
* **Vector Type:** Table
*   Table:
| Rule ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Source |
| :------ | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :-----: |
| 1       | Nonlinear PV curve | PV curve shape | Monotonic, NM-low, NM-high | Qualitative | Explicit | PV curve determines actuator response. | Fig 2A |
| 2       | Flow restriction | Resistance of tubes | Varied via inner diameter and length | Varied | Explicit | Flow restriction dictates the time delay between actuators. | Materials and Methods |

### **4.6. Globally Emergent Order and Order Parameters**
* **Vector ID:** M4.6
* **Vector Type:** Table
*   Table:
| Property ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Protocol | Source |
| :---------- | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :------: | :-----: |
| 1       | Spatial Asymmetry | Swept Area | 25-282 | mm² | Explicit | Quantifies asymmetry. | Tip tracking | Fig 3F |
| 2       | Metachronal Wave | Wave Speed (inflation) | 23 | mm/s | Explicit | Characterizes wave propagation. | Kymograph analysis | Fig 4E |
| 3       | Metachronal Wave | Wave Speed (deflation) | 53 | mm/s | Explicit | Characterizes wave propagation. | Kymograph analysis | Fig 4E |
| 4       | Metachronal Wave | Phase Shift (inflation) | 0.19π | rad | Explicit | Describes temporal coordination. | Wave speed calculation | Results |
| 5       | Metachronal Wave | Phase Shift (deflation) | 0.08π | rad | Explicit | Describes temporal coordination. | Wave speed calculation | Results |

### **4.7 Yoneda Embedding and Local-to-Global Mapping Fidelity**

*   **Vector ID:** M4.7
*   **Vector Type:** Table
*   Table:
    | Link Type | Description | Predictability | Yoneda Score | Metrics | Implicit/Explicit | Justification | Source |
    | :-------- | :---------- | :------------- | :----------- | :------ | :----------------: | :------------: | :-----: |
     | Local PV to Global Swept Area | PV Curve shape influences swept area | Medium-High | 7 | Swept Area (mm²), Simulation Accuracy (R² if available, qualitatively assessed) | Mixed | Simulations predict swept area based on PV curves, but with some deviations as discussed in 4.4 Predictability. | Fig 3, Results |
    | Local Flow Res. to Metachronal Wave | Flow restrictors influence wave speed and phase shift | Medium-High | 7 | Wave Speed (mm/s), Phase Shift (rad), Kymograph visualization qual. | Mixed | Simulations predict wave characteristics based on flow restrictor properties, again with limitations as per 4.4. | Fig 4, Results |
    *   **Yoneda Embedding Fulfillment Score [0-10]:** [Rubric: 0-2: Local rules almost unrelated to global order, order largely externally imposed. 3-5: Local rules contribute weakly to global order, significant external influence or stochasticity. 6-8: Local rules strongly shape global order, reasonably predictable. 9-10: Near-perfect mapping from local rules to global order, highly robust and predictable.]
    *   **Metrics:**  [Metrics used are Swept Area for spatial asymmetry and Wave Speed and Phase Shift for metachronal wave, and Qualitative assessment of simulation accuracy by visual inspection of plots and kymographs.]
    *   **Justification:** The Yoneda score reflects a moderately strong mapping from local rules (PV curves, flow resistance) to global order (swept area, metachronal wave). While predictable and simulated with reasonable accuracy, the mapping is not perfect due to factors mentioned in section 4.4, resulting in a score of 7. The system relies on designed morphology to generate order, rather than purely emergent order from simple rules.

## M5: Computation
*   **Vector ID:** M5
*   **Vector Type:** Computation

### **5.1 Embodied Computation Presence:**

*   **Vector ID:** M5.1
*   **Vector Type:** Binary
    *   Content: No
    *   Justification: The system does not perform embodied computation in the sense of material-intrinsic information processing beyond simple physical responses. The nonlinear actuator behavior and fluidic interactions generate complex motion sequences, but these are not computational primitives operating on inputs to produce outputs beyond the direct physical actuation. The system behaves according to its physical design and input pressure, without performing logical operations, algorithmic processing, or any form of decision-making beyond reacting to the applied pressure. The "computation" is in the temporal sequencing of actuation provided by physical properties, which simplifies *control*, but isn't computation in the informational sense.
    *    Implicit/Explicit: Implicit
        *  Justification: The paper emphasizes morphological *control* as a simplification of conventional control *schemes*, suggesting that the complexity is shifted into the physical morphology rather than computational units (Implicit). The description focuses on physical mechanisms and lacks any mention of information processing or computational operations performed by the material itself (Implicit).

## M6: Temporal Dynamics
*   **Vector ID:** M6
*   **Vector Type:** Temporal

### **6.1 Timescales:**

*   **Vector ID:** M6.1
*   **Vector Type:** ParameterTable
    *   Table:
        | Timescale Description | Value | Units | Source | Implicit/Explicit | Justification |
        | :-------------------- | :---: | :---: | :----: | :----------------: | :------------: |
        | Pressure Ramp Rate (Quasi-static spatial asymmetry) | 5 | kPa/s | Spatial Asymmetry Setup Section | Explicit | Rate of pressure change for quasi-static experiments |
        | Pressure Ramp Rate (Dynamic spatial asymmetry - Inflation) | 300 | kPa/s | Spatial Asymmetry Setup Section (Inference from 0.3MPa/1s) | Implicit | Inflation rate for dynamic experiment |
        | Pressure Ramp Rate (Dynamic spatial asymmetry - Deflation) | 60 | kPa/s | Spatial Asymmetry Setup Section | Explicit | Deflation rate for dynamic experiment |
        | Metachrony Cycle Period (Approximate) | 18 | s | Figure 4D, Time axis range | Implicit | Estimated from figure axis range per cycle in Figure 4D |
        | Valve Response Time | N/A | N/A | N/A | Implicit | Typical valve response, not specified |

    *   **Note:** Identify and quantify the *relevant timescales* of the system's dynamics (e.g., response time, process duration, oscillation period, memory decay, adaptation/learning timescale, self-assembly timescale). Use consistent units (e.g., seconds, milliseconds) for comparability.

### **6.2 Active Inference:**

*   **Vector ID:** M6.2
*   **Vector Type:** Assessment
    *   Content: No
    *   Justification: The system does not exhibit active inference. There's no evidence of: (1) *prediction* of future states – the system reacts to the current pressure input without anticipating future inputs or environmental changes; (2) *action selection* to minimize discrepancies – the cilia's motion is a direct result of the pressure input and morphological design, not a selection from a repertoire of actions to achieve a specific goal or minimize prediction error; (3) *internal models* updated by experience – no learning or adaptation mechanism is described where the system modifies an internal model based on feedback or experience to improve future performance. The system operates as a pre-programmed physical system responding deterministically to pressure inputs.
    *   Implicit/Explicit: Implicit
        *  Justification: The absence of active inference is inferred from the system's deterministic, feedforward nature and lack of learning or predictive mechanisms. The focus on morphological control suggests pre-programmed behavior rather than active inference (Implicit). No aspect of the paper suggests predictive modeling or error minimization driven behaviour (Implicit).
    *   **If Yes/Partial, provide examples of testable CT-GIN metrics that *could* be used to quantify active inference:** N/A

## M7: Adaptation
*   **Vector ID:** M7
*   **Vector Type:** Adaptation

### **7.1 Adaptive Plasticity Presence:**

*   **Vector ID:** M7.1
*   **Vector Type:** Binary
    *   Content: No
    *   Justification: The system does not exhibit adaptive plasticity.  The behavior and internal structure are fixed by the initial design and fabrication. There is no mechanism described for the system to *change its behavior or internal structure* in response to experience or environmental changes to improve performance or alter functionality *over time*. The system performs pre-programmed motions based on its morphology and pressure input. While the system can respond to different pressure inputs, this is not adaptation; it's a predetermined response curve, not a persistent change driven by experience altering its future response.
    *    Implicit/Explicit: Explicit
        * Justification: The lack of adaptive plasticity is inferred from the emphasis on static morphological control and the absence of any description of learning or adaptation mechanisms in the paper. The system's behavior is presented as fixed by design (Implicit). The paper focuses on demonstrating pre-programmed sequences, not adaptation (Explicit emphasis).

## M8: Emergent Behaviors
*   **Vector ID:** M8
*   **Vector Type:** Behavior

### **8.1 Behavior Description:**

*   **Vector ID:** M8.1
*   **Vector Type:** Description
    *   Content: The main functional behaviors are:
        1.  **Cilia-inspired asymmetric motion:**  The single artificial cilium system exhibits a nonreciprocal bending motion, creating a swept area resembling biological cilia. This is for low Reynolds number fluid propulsion.
        2.  **Metachronal Wave Propagation:** The cilia array demonstrates a sequential, wave-like bending motion across the array. This metachronal wave is also inspired by biological cilia and is intended for directional fluid transport in arrays.
    These behaviors are presented as emergent from the morphological design and controlled by a single pressure input in each setup, simplifying control compared to systems with multiple actuators requiring individual control lines.
    *   CT-GIN Mapping: Defines the `BehaviorArchetypeNode`. Specify the type of behavior: `type: Locomotion, Fluid Propulsion`, `subtype: Cilia-inspired Asymmetric Motion, Metachronal Wave`.
    *    Implicit/Explicit: Explicit
       *  Justification: The behaviors are explicitly described as cilia-inspired asymmetric motion and metachronal wave propagation, and are central to the paper's objectives and results (Explicit). The functional purpose of fluid propulsion is also explicitly stated (Explicit).

### **8.2 Behavior Robustness:**

*   **Vector ID:** M8.2
*   **Vector Type:** Score
    *   Score: [6]
    *   Justification: Behavior robustness is moderate. The system functions based on relatively simple components (balloons, PVC, tubing), suggesting some inherent robustness to imperfections in individual components. The morphological control approach itself aims for robustness by distributing control across physical properties rather than relying on precise electronic or software control that could be more fragile. However, robustness is likely limited:
        1.  **Sensitivity to Material Properties:**  Performance relies on specific pressure-volume curves of the actuators. Variations in latex balloon and PVC shell material properties or dimensions during fabrication could affect the intended nonlinear behavior and sequencing, thus impacting behavior fidelity. Fabricational tolerances are not quantitatively assessed.
        2.  **Fluidic System Robustness:**  The system depends on fluidic connections and valve operation. Blockages in tubing, leaks, or valve malfunctions could disrupt performance. Robustness of these components is typical for pneumatic systems, around medium. No mention of specific robustness tests against perturbations is made.
        3.  **Limited Environmental Perturbation Analysis:** The paper doesn't explicitly test robustness against external mechanical disturbances, temperature variations, or other environmental factors.
    Qualitatively assessed, robustness is medium to moderately high for component variations and operational simplicity, but unquantified and untested against diverse perturbations.
    *   Implicit/Explicit: Mixed
        *  Justification: Qualitative assessment of robustness based on component simplicity and morphological control principle is implicit, inferred from general engineering principles (Implicit). Limitations arising from material and fluidic system sensitivities are also inferred common sense understanding of such systems (Implicit). Explicit robustness tests and quantifiable metrics are absent, limiting more precise evaluation and thus lowering the confidence in achieving higher robustness score.

### **8.3 CT-GIN Emergent Behavior Validation**

*    **Vector ID:** M8.3
*    **Vector Type:** Validation
     *  Content: Validation methods for emergent behaviors include:
        1.  **Experimental Demonstration:** Both spatial asymmetry and metachronal wave behaviors are experimentally demonstrated using fabricated prototypes (Figure 3E, 4C, Supplementary Movies S1-S5). The nonreciprocal motion of cilia and metachronal wave are visually observed and recorded using cameras.
        2.  **Quantitative Analysis:** Swept area is quantitatively measured for spatial asymmetry (Figure 3F), and wave speed and phase shift are calculated for metachronal waves (Figure 4E, Results and Discussion). These metrics provide quantitative validation of the intended behaviors.
        3.  **Simulation Validation:** Lumped fluidic system simulations are developed and compared with experimental results (Figure 3D, 3F, 4D, 4E). The agreement between simulation and experiment, although not perfect, supports the understanding of the underlying mechanisms and the emergence of the observed behaviors from the designed morphology and interaction rules.  Figure 3F shows comparison of swept area and Figure 4D shows curvature responses.
        4.  **Operational Definitions:** The behaviors are operationally defined by swept area (for asymmetric motion) and wave characteristics (for metachrony), allowing for quantifiable assessment.
        Control experiments, direct robustness/reliability assessment, and detailed reproducibility data beyond example demonstrations are not explicitly presented.
     *   Implicit/Explicit: Mixed
    *   Justification: Experimental demonstration, quantitative analysis, and simulation validation are explicitly described methods used to validate emergent behaviors (Explicit). Observational recording through camera is explicit mention. Operational definitions via swept area and wave metrics are also explicit. The limitations regarding control experiments, robustness, and reproducibility are implicit as they are not explicitly addressed although standard for full validation in scientific publications (Implicit).

## M9: Cognitive Proximity
*   **Vector ID:** M9
*   **Vector Type:** Cognition

### **9.1 Cognitive Mapping:**

*   **Vector ID:** M9.1
*   **Vector Type:** Description
    *   Content: The paper uses "morphological control" and "embodied intelligence" terminology from the field of embodied cognition, drawing an analogy between the simplified control in their soft robot and control distribution in biological systems.  Figure 1 explicitly contrasts "external" and "morphological" control schemes, mapping them loosely to "brain" and "body" functions in biological systems. The concept of "sequencing" in actuation is also implicitly related to basic cognitive functions of temporal ordering of actions. However, these are primarily metaphorical mappings to illustrate the control simplification aspect of morphological control, not to claim genuine cognitive functions in the artificial cilia system beyond basic sequential behavior. The "embodied intelligence" is in the *design methodology*, not in emergent cognition *of the system itself* in traditional cognition science context.
    *   CT-GIN Mapping: `CognitiveMappingEdge`: `source: BehaviorArchetypeNode(Cilia-inspired Motion, Metachronal Wave)`, `target: CognitiveFunctionNode(Control Simplification, Embodied Intelligence (metaphorical))`, `mappingType: Metaphorical Analogy`, `limitations: No genuine cognitive functions beyond basic sequencing`.
    *   Implicit/Explicit: Explicit
    * Justification: The use of terms like "morphological control" and "embodied intelligence" and the analogy to biological systems are explicit in the introduction and discussion (Explicit). The limitation to metaphorical mapping and absence of claims of genuine cognitive functions beyond basic sequencing are implicit but are the dominant interpretation given the engineering focus and lack of cognitive function analysis.

### **9.2 Cognitive Proximity Score:**

*   **Vector ID:** M9.2
*   **Vector Type:** Score
    *   Score: [1]
    *   Justification: Using the CT-GIN Cognizance Scale, the system scores at Level 1: Simple Responsivity.
        *   **Level 1 Justification:** The artificial cilia exhibit basic stimulus-response behavior. They respond to pneumatic pressure input with predetermined bending motions. Reactions are fixed by the morphological design and pressure input profile. There is no evidence of internal state beyond the immediate stimulus and current configuration, no adaptation, goal-directed behavior, or any higher-level cognitive functions (Levels 2+). Although inspired by biological cilia, the system operates at a much simpler functional level, primarily demonstrating engineered sequential actuation through morphology rather than genuine cognitive processing. The system achieves *simplified control*, which draws *inspiration* from biological embodied intelligence, but does not *realize* embodied intelligence at a cognitive level.
    *   Implicit/Explicit: Mixed
    *  Justification: The score of Level 1 is inferred from the system's described functionality, emphasizing stimulus-response and absence of higher-level cognitive features (Implicit). The cognitive mapping of "morphological control" and "embodied intelligence" exists metaphorically in the paper, making the classification "mixed" as some language relating to cognition is present, but not in a scientifically rigorous, functional sense. The system's *lack* of cognitive features above Level 1 is evident both implicitly and explicitly.

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
    | Sensing/Perception               |      1       | Senses pressure input only; minimal internal sensing.                                  | `CognitiveFunctionNode: Sensing`   | Explicit          | Pressure sensing via pneumatic input is explicit |
    | Memory (Short-Term/Working)        |      0       | No active short-term memory; state is purely reactive to current pressure.             | N/A                                   | Implicit          | Memory absent based on system description. |
    | Memory (Long-Term)                 |      0       | No long-term memory; no structural or persistent changes from past inputs.            | N/A                                   | Implicit          | Memory absent based on system description. |
    | Learning/Adaptation              |      0       | No learning or adaptation mechanisms; behavior fixed by design and input.            | N/A                                   | Explicit          | Adaptation is not discussed or implemented. |
    | Decision-Making/Planning          |      0       | No decision-making or planning; actions are predetermined by morphology and input. | N/A                                   | Implicit          | Decision making is not part of the system's function. |
    | Communication/Social Interaction |      0       | No communication or social interaction capabilities.                                  | N/A                                   | N/A               | Not applicable. |
    | Goal-Directed Behavior            |      1       | Goal is predefined: cilia-inspired motion and metachronal waves, but not adaptable goals | `CognitiveFunctionNode: Goal-Directed Behavior` | Implicit          | Predefined goals; lacks adaptive goal selection.|
    | Model-Based Reasoning              |      0       | No internal models or reasoning; purely reactive system.                              | N/A                                   | Implicit          | Model-based reasoning is not present.|
    | **Overall score**                 |      0.25      |                                                                                       |                                   |                     |                |

    *   **Note:** Assess the system for *each* function, providing a score (0-10) and a short (1-2 sentences) justification.  0 = Absent, 10 = Human-level performance.

## M10: Criticality Assessment
*   **Vector ID:** M10
*   **Vector Type:** Criticality

### **10.1 Criticality:**

*   **Vector ID:** M10.1
*   **Vector Type:** Assessment
    *   Content: No
    *   Justification: The paper does not suggest that the system operates near a critical point or exhibits scale-free behavior, power laws, or long-range correlations. The system's behavior is described by deterministic physical principles (fluid dynamics, nonlinear elasticity) and is designed to produce predictable, controlled motion sequences.  While snap-through instabilities are mentioned, they are harnessed for *discrete* state transitions and morphological *control* of sequences, not explicitly linked to criticality or emergent collective phenomena in the sense of phase transitions or complex systems operating at the edge of chaos. The focus is on engineered functionality, not on emergent criticality-related properties.
        *   Critical Parameters (If Yes/Partial): N/A
        *   Evidence: N/A
    *   Implicit/Explicit: Implicit
    *    Justification: The absence of criticality is inferred from the paper's focus on deterministic, engineered behavior and lack of any discussion or evidence of criticality-related phenomena. The focus is on *control* and *sequencing*, not on emergent criticality (Implicit). No mention of criticality metrics or analysis is present.

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
*   **Calculated Score:** [5.5]

**CT-GIN Readiness Summary Table:**

| CT-GIN Aspect                   | Strength (Yes/Partial/No) | Key Supporting Metrics (with units) | Limitations (Missing Metrics/Data Gaps)                                           | Improvement Areas (Future Research)                                          |
| :------------------------------ | :-----------------------: | :-----------------------------------| :------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| Energy Flow Efficiency          |           Partial         | Qualitative assessment: Low-Medium | Quantitative efficiency metrics, detailed dissipation breakdown                 | Optimize actuator and valve design, minimize fluid resistance and hysteresis. |
| Memory Fidelity                 |             No            |                 N/A                  | Memory retention time, capacity, readout accuracy, degradation rate, energy cost | Incorporate bistable or multistable elements for state retention and memory. |
| Organizational Complexity       |            Yes            | Swept Area (mm²), Wave Speed (mm/s), Phase Shift (rad) |  Predictability metrics beyond qualitative simulation agreement                |  Explore more complex array configurations, hierarchical designs.             |
| Embodied Computation            |             No            |                 N/A                  | Processing power, energy per operation, response time, bit-depth, computational primitives | Integrate basic logic operations or analog computation into actuator design.|
| Temporal Integration            |           Partial         | Timescales (kPa/s, s)               | Actuator response time, detailed timing control precision                          |  Refine temporal control with more precise flow restrictors or valve actuation.|
| Adaptive Plasticity             |             No            |                 N/A                  | Adaptation rate, learning curves, mechanism of plasticity                       | Implement feedback mechanisms for adaptation to environmental changes.       |
| Functional Universality         |             No            |  Cilia Motion, Metachronal Wave       | Demonstrate broader range of functional behaviors, adaptability to tasks.       | Explore multifunctionality by integrating sensing or other actuator types.  |
| Cognitive Proximity            |             No            |         Cognitive Score: 1          | Metrics for goal-directedness, model-based reasoning, decision-making          |  Add rudimentary goal-directed behavior or simple decision-making based on inputs.|
| Design Scalability & Robustness |           Partial         | Qualitative Assessment: Moderate    |  Quantified robustness against material variations, environmental perturbations      | Conduct robustness studies, improve fabrication tolerances, explore self-healing.  |
| **Overall CT-GIN Readiness Score** |           Partial         |   5.5                              |                                                                                  |                                                                               |


### **13.2 Qualitative CT-GIN Assessment Conclusion:**

*   **Vector ID:** M13.2
*   **Vector Type:** Textual Summary
    *   Content: This paper presents an experimentally validated soft robotic system for cilia-inspired asymmetric motion and metachronal waves based on morphological control. Key Strengths: clear implementation of nonlinear soft actuators, demonstration of self-organized motion sequences from a single input, and validation through simulations and experiments. Organizational complexity and temporal dynamics are partially characterized, and the design shows moderate robustness due to its simplicity. Key Limitations: Lack of memory, embodied computation, and adaptive plasticity. Energy efficiency is likely low. Cognitive proximity is minimal, with the system exhibiting only basic responsivity. Overall Assessment: The system demonstrates interesting emergent behaviors in terms of motion sequencing driven by morphology. It represents a Level 1 cognizant system with simple responsivity. Potential within CT-GIN: The work provides a good example of morphological control principles for generating complex behaviors from simple components. Future iterations could significantly enhance CT-GIN readiness by incorporating memory, adaptation, and exploring potential for basic embodied computation and improved energy efficiency. Further research is needed to quantify robustness and scalability.

### **13.3 CT-GIN Refinement Directions:**

*   **Vector ID:** M13.3
*   **Vector Type:** Recommendations
    *   *   Incorporate bistable or multistable mechanisms within the actuators to introduce memory capabilities, enabling state retention and influencing future actuation sequences based on past states.
    *   Explore integrating rudimentary sensing capabilities into the actuator design to enable feedback-driven adaptation to environmental conditions, moving beyond purely pre-programmed behavior.
    *   Investigate designs for improving energy efficiency, potentially through optimized actuator geometries, alternative actuation methods, or energy recovery strategies.
    *   Quantify robustness to material variations, fabrication tolerances, and environmental perturbations through systematic experimental testing and statistical analysis.
    *   Explore hierarchical architectures for cilia arrays, potentially combining different actuator types or multi-layered designs to increase functional complexity and control.
    *   Develop and integrate basic embodied computational primitives within the material itself, going beyond sequencing to enable simple logical operations or signal processing within the soft robotic system.
    *   Extend the functional repertoire beyond cilia motion to demonstrate broader applicability and adaptability to diverse tasks or environmental contexts.

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
        | M2.1     |     M2.2    | Energy Transduction |
        | M2.2     |     M8.1    | Embodiment of Behavior |
        | M4.2     |     M4.3    | Adjunction (Local to Global Order) |
        | M1.1     |     M2.1    | System Input |
        | M1.1     |     M8.1    | System Behavior |
        | M9.1     |     M8.1    | Cognitive Mapping Source |

## M16: CT-GIN Template Self-Improvement Insights

*   **Vector ID:** M16
*   **Vector Type:** Feedback

### **Template Feedback:**

*    **Vector ID:** M16.1
*   **Vector Type:** Text
Provide specific, actionable feedback on the *CT-GIN template itself*, based on this analysis:
    *   **Missing Probes:** The template is comprehensive. Perhaps a probe for "Scalability" within Module M1 or M13 could be added to explicitly assess the potential for scaling up the design (e.g., to larger arrays, smaller scales).
    *   **Unclear Definitions:** Definitions are generally clear. "Active Inference" might benefit from slightly more operational examples within the template itself.
    *   **Unclear Node/Edge Representations:** Guidance for mapping to GIN nodes/edges is sufficient. Providing example CT-GIN graphs for different paper types in the template could be helpful for users.
    *   **Scoring Difficulties:** Scoring rubrics are generally helpful. The Yoneda Embedding rubric in M4.7 could be made slightly more granular, perhaps with intermediate examples for scores of 4-6. Cognitive Proximity scale is clear.
    *   **Data Extraction/Output Mapping:** Data extraction was straightforward. Template output mapping was clear and direct. No major challenges.
    *   **Overall Usability:** The template is well-structured and reasonably easy to use, although quite extensive and detailed, which is necessary for thorough analysis. The modular structure helps in systematically analyzing different aspects.
    * **Specific Suggestions:**
        *   Add a "Scalability" probe in Module M1 or M13.
        *   Provide more operational examples for "Active Inference" definition.
        *   Include example CT-GIN knowledge graphs in the template for illustration.
        *   Refine Yoneda Embedding rubric in M4.7 for better granularity (scores 4-6 examples).
