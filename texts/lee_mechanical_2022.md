# Mechanical neural networks: Architected materials that learn behaviors

__Paper Type:__ Experimental

## M1: System Overview & Implementation
*   **Vector ID:** M1
*   **Vector Type:** Overview

### **1.1 System Description**

*   **Vector ID:** M1.1
*   **Vector Type:** Description
    *   Content: The system is a mechanical neural network (MNN) made of architected materials. It is a lattice of interconnected tunable beams joining at nodes, which are driven by force or displacement inputs and outputs. The stiffness of the beams is tuned like weights in artificial neural networks (ANNs) to enable learning mechanical behaviors. An example lattice was fabricated using voice coils and strain gauges for tunable beams arranged in a triangular configuration with input and output nodes. The MNN learns through an optimization algorithm that adjusts beam stiffness to minimize the mean squared error (MSE) between measured and desired output node displacements under specific loading scenarios. The purpose is to create artificial-intelligent (AI) materials that can learn mechanical behaviors and properties, such as shape morphing and bulk properties.
    *   CT-GIN Mapping: `SystemNode` attributes: `systemType: Mechanical Neural Network`, `domain: Mechanical Metamaterials`, `mechanism: Tunable Beam Stiffness Adjustment`, `components: Tunable Beams, Nodes, Actuators, Sensors, Controller, Optimization Algorithm`, `purpose: Learning Mechanical Behaviors and Properties`
    *   Implicit/Explicit: Mixed
        *  Justification: The system description combines explicit statements from the abstract, introduction and results sections regarding components and learning mechanisms, with implicit understanding of neural network analogy requiring interpretation.

### **1.2 Implementation Clarity**

*   **Vector ID:** M1.2
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The implementation is described with good detail, including the use of tunable beams with voice coils and strain gauges, lattice configuration (triangular), and optimization algorithms (GA, PPS). Figures and supplementary materials further clarify the fabrication and control aspects. However, some details on the exact control algorithm parameters and specific optimization algorithm settings (beyond GA and PPS names) are not fully elaborated within the main text.
    *   Implicit/Explicit: Mixed
        * Justification: The clarity is mixed because while main components and methods are explicit, fine details of control and optimization are less so, requiring reference to supplementary materials for full clarity.

### **1.3 Key Parameters**

*   **Vector ID:** M1.3
*   **Vector Type:** ParameterTable
    *   Table:
        | Parameter Name | Value | Units | Source (Fig/Table/Section) | Implicit/Explicit | Data Reliability (High/Medium/Low) | Derivation Method (if Implicit) |
        | :------------- | :---: | :---: | :-----------------------: | :-----------------: | :-----------------------------: | :-------------------------------: |
        | Max Beam Stiffness | 2.3 | N/mm | Fig 2C | Explicit | High | Measured experimentally |
        | Min Beam Stiffness | -2 | N/mm | Fig 2C | Explicit | High | Measured experimentally |
        | Lattice Layers | 8 (Simulation), 2 (Experiment) | layers | Fig 1B, Fig 3B | Explicit | High | Specified in text/figures |
        | Tunable Beams (Experiment) | 21 | count | Fig 4A | Explicit | High | Counted from figure description |
        | Output Nodes (Experiment) | 2 | count | Fig 4A | Explicit | High | Counted from figure description |

    *   **Note:** List *up to 5* key parameters characterizing the system's *implementation*.  Provide values and units if possible. If a parameter is not explicitly stated but derived/inferred, clearly state the derivation method. *Always* include units if applicable. If a value is not applicable, write "N/A".  Data Reliability: High = Directly measured, Medium = Derived from measurements/simulations, Low = Estimated/Inferred.

## M2: Energy Flow
*   **Vector ID:** M2
*   **Vector Type:** Energy

### **2.1 Energy Input**

*   **Vector ID:** M2.1
*   **Vector Type:** Input
    *   Content: Mechanical force applied to the input nodes. In experiments, voice coil actuators apply forces. In simulations, forces are numerically applied.
    *   Value: ±2 (Simulation), Unspecified (Experiment)
    *   Units: N
    *   CT-GIN Mapping: `EnergyInputNode`: attributes - `source: Voice coil actuators/Simulation Software`, `type: Mechanical Force`
    *   Implicit/Explicit: Mixed
        *  Justification: Type of energy input (mechanical force) is explicit. Source is mixed; Voice coil actuators explicitly mentioned for experiments, numerical application implicit for simulations. Magnitude explicitly given for simulation but not for experiment.

### **2.2 Energy Transduction**

*   **Vector ID:** M2.2
*   **Vector Type:** Transduction
    *   Content: Electrical energy is converted into mechanical energy by voice coil actuators to apply forces on input nodes.  The mechanical force propagates through the lattice, deforming the tunable beams. Strain gauges on beams sense deformation and output electrical signals processed by the closed-loop controller. Controller adjusts voice coils, tuning beam stiffness. Energy flow: Electrical (controller) -> Mechanical (voice coils) -> Mechanical Deformation (beams) -> Electrical (strain gauges) -> Electrical (controller).
    *   CT-GIN Mapping: `EnergyTransductionEdge`: attributes - `mechanism: Electromechanical transduction, Force propagation, Strain sensing, Stiffness modulation`, `from_node: EnergyInputNode (Electrical)`, `to_node: Mechanical Deformation (Beams)` , `from_node: Mechanical Deformation (Beams)`, `to_node: EnergyOutputNode (Electrical Strain Gauge Signals)`
    *   Implicit/Explicit: Mixed
        *  Justification: Energy transduction mechanisms are described explicitly (voice coils, strain gauges, stiffness tuning). The detailed flow path involves implicit understanding of control loop operating principles.

### **2.3 Energy Efficiency**

*   **Vector ID:** M2.3
*   **Vector Type:** Score
    *   Score: [4]
    *   Justification/Metrics: Efficiency is likely Low. Actively controlled tunable beams using voice coils and strain gauges consume energy to maintain stiffness and for actuation.  Energy is dissipated through heat in voice coils, friction in mechanical components, and electrical resistance in circuits. No quantitative efficiency metrics are provided. Qualitative assessment: Low due to active control and multiple transduction steps involving lossy processes.
    *   CT-GIN Mapping: Attribute of relevant `EnergyTransductionEdge`s: `efficiency: Low (Qualitative)`
    *   Implicit/Explicit: Implicit
      *  Justification: Efficiency is not explicitly quantified or discussed, but can be inferred as low based on the nature of active control mechanisms involving electromechanical transduction and known inefficiencies in such systems.

### **2.4 Energy Dissipation**

*   **Vector ID:** M2.4
*   **Vector Type:** Dissipation
    *   Content: Energy dissipation occurs due to:
        1.  **Voice coil actuator inefficiency:** Heat generation due to electrical resistance.
        2.  **Friction:** In moving parts of tunable beams and nodes, although flexures minimize this.
        3.  **Electrical resistance:** In control circuits.
        4.  **Strain gauge power dissipation:**  Though likely small.
    Quantification: Precise quantification is not provided. Qualitative assessment: Dissipation is likely Medium to High due to active control and moving parts, but flexure bearings might reduce friction compared to sliding mechanisms.
    *   CT-GIN Mapping: `EnergyDissipationNode`: `type: Heat, Friction, Electrical Resistance`, `EnergyDissipationEdge`: `mechanism: Ohmic heating, Mechanical Friction, Electrical Losses`, `from_node: EnergyTransductionEdge`, `to_node: EnergyDissipationNode`
    *    Implicit/Explicit: Implicit
        *  Justification: Dissipation mechanisms are inferred from typical losses in electromechanical systems, not explicitly quantified.

## M3: Memory
*   **Vector ID:** M3
*   **Vector Type:** Memory

### **3.1 Memory Presence:**

*   **Vector ID:** M3.1
*   **Vector Type:** Binary
    *   Content: Yes
    *   Justification: Beam stiffness values are tuned and retained to achieve learned behaviors. These stiffness configurations represent memory of learned mechanical responses.  The paper explicitly states MNNs "store a kind of mechanical 'muscle memory' in their architecture".  Changing stiffness values based on experience and retaining them to influence future behavior under similar conditions constitutes memory.
    *    Implicit/Explicit: Explicit
        * Justification: The concept of "mechanical muscle memory" and stiffness tuning are explicitly mentioned as mechanisms for storing learned behaviors.

### **3.2 Memory Type:**

*   **Vector ID:** M3.2
*   **Vector Type:** Score
*   Score: [6]
*   Justification: The memory is analogous to synaptic weights in ANNs.  It's a form of analog memory stored in the continuous stiffness values of beams. Retention is implied to be persistent as the MNN "relearns previously mastered behaviors". Capacity is multi-behavioral, storing stiffness configurations for different behaviors, though not quantified in terms of bits or states. Read-out accuracy is limited by MSE reduction achieved during learning, not perfect recall but optimized response. Score of 6 reflects moderate retention and capacity with imperfect readout, resembling adaptive parameter storage rather than high-fidelity digital memory.
*   CT-GIN Mapping: `MemoryNode` type: `Analog Parameter Memory (Beam Stiffness)`
*    Implicit/Explicit: Mixed
    * Justification: Analogy to ANN weights and stiffness tuning are explicit descriptions of memory type.  Retention, capacity, and accuracy are inferred properties based on system behavior and learning process description.

### **3.3 Memory Retention Time:**

*   **Vector ID:** M3.3
*   **Vector Type:** Parameter
*   Value: Long-term
*    Units: Qualitative Descriptor
*   Justification:  The paper describes MNNs' ability to "relearn previously mastered behaviors and acquire new behaviors". This implies the retention of previously learned stiffness configurations over extended periods, described qualitatively as "prolonged exposure" and "flight experience", suggesting long-term retention of learned behaviors. Explicit retention time is not quantified.
*    Implicit/Explicit: Implicit
        * Justification: Long-term retention is inferred from descriptions of relearning and adaptation over time and varying conditions, not explicitly quantified with specific time units.

### **3.4 Memory Capacity (Optional - if applicable)**

* **Vector ID:** M3.4
* **Vector Type:** Parameter
*  Value: Multiple Behaviors
*   Units: distinct states
*   Justification: The MNN learns "multiple mechanical behaviors simultaneously". Solutions achieving "two shape-morphing behaviors" are demonstrated. Figure 1D and 1E show different stiffness combinations achieving same behaviors, suggesting capacity for multiple solutions and potentially multiple behaviors. Capacity not quantified by bit or state count but demonstrated by learning and storing configurations for at least two distinct behaviors simultaneously.
*    Implicit/Explicit: Explicit
        *  Justification: Explicitly demonstrated ability to learn and store configurations for "multiple mechanical behaviors simultaneously", specifically two shape-morphing behaviors.

### **3.5 Readout Accuracy (Optional - if applicable)**

* **Vector ID:** M3.5
* **Vector Type:** Parameter
*   Value: MSE Achieved
*   Units: mm^2
*   Justification: Readout accuracy is reflected in the Mean Squared Error (MSE) after learning. Experimentally, MSE for GA is 0.006 mm^2 and PPS is 0.063 mm^2. For linear stiffness simulation, MSE is 0.056 mm^2 and nonlinear is 0.093 mm^2. Lower MSE indicates higher accuracy in reproducing target displacements, representing more accurate readout of learned behavior from stored stiffness memory.
*    Implicit/Explicit: Explicit
       *  Justification: MSE values are explicitly provided as metrics of learning performance, directly reflecting readout accuracy in terms of displacement errors.

### **3.6 Degradation Rate (Optional - if applicable)**
* **Vector ID:** M3.6
* **Vector Type:** Parameter
    *   Value: N/A
    *   Units: N/A
    *   Justification: Degradation rate of memory (stiffness configurations) is not discussed or quantified.  The focus is on learning and relearning, implying sufficient stability for demonstrating learning but no specific data on spontaneous degradation or decay over time without external influence.
    *    Implicit/Explicit: Implicit
            * Justification: Absence of discussion or data suggests degradation is either not significant within experimental timescales or not characterized.

### **3.7 Memory Operations Energy Cost (Optional - if applicable)**
* **Vector ID:** M3.7
* **Vector Type:** Table
*   Table:
    | Memory Operation ID | Energy Consumption per Bit | Power Usage during Operation| Units | Uncertainty | Data Source Reference | Implicit/Explicit | Justification |
    | :------------------ | :--------------------------: | :-----------------------------: | :---: |:-----------------:|:-----------------:|:-----------------:| :------------------ |
    | Writing (Stiffness Tuning) | N/A                          | N/A                             |       | N/A            | N/A           | Implicit         | No data provided |
    | Reading (Behavior Expression) | N/A                          | N/A                             |       | N/A            | N/A           | Implicit         | No data provided |
*   Implicit/Explicit: Implicit
    *   Justification: Energy cost of memory operations (writing/tuning stiffness, reading/expressing learned behavior) is not quantified or discussed. Implicitly energy is consumed by actuators and control system for both tuning and operation, but no specific values are given related to memory operations explicitly.

### **3.8 Memory Fidelity & Robustness Metrics (Optional - if applicable)**
* **Vector ID:** M3.8
* **Vector Type:** Table
*   Table:
    | Metric ID | Description | Value | Units | CT-GIN Mapping | Data Source | Implicit/Explicit | Justification |
    | :-------- | :---------- | :----: | :---: | :-------------: | :----------: |:-----------------:| :-----------------:|
    | MSE (GA) | Mean Squared Error after learning with Genetic Algorithm | 0.006 | mm^2 |  Attribute of `MemoryNode` | Fig 4B | Explicit |  Explicitly stated MSE value |
    | MSE (PPS) | Mean Squared Error after learning with Partial Pattern Search | 0.063 | mm^2 |  Attribute of `MemoryNode` | Fig 4C | Explicit |  Explicitly stated MSE value |
*   Implicit/Explicit: Explicit
*   Justification: Memory fidelity is implicitly reflected in the achieved MSE values. Robustness of memory against perturbations (damage, refixturing) is conceptually mentioned ("If an MNN is damaged, cut...or fixtured differently, then it can relearn..."), but no quantitative metrics are provided for robustness directly, only relearning capability is described qualitatively.

---

## M4: Self-Organization and Emergent Order
*   **Vector ID:** M4
*   **Vector Type:** Self-Organization

### **4.1 Self-Organization Presence:**

*   **Vector ID:** M4.1
*   **Vector Type:** Binary
    *   Content: No
    *   Justification: The MNN lattice structure is designed and fabricated externally. Beam stiffness values are tuned by a global optimization algorithm (GA or PPS) to achieve desired global behaviors.  While local beam stiffness adjustments contribute to the global behavior, the overall structure and learning process are externally directed, not spontaneously emerging global order from purely local interactions without external algorithms defining the global configuration or learning rules.  The observed order (shape morphing) is a programmed outcome, not emergent self-organization.
    *   Implicit/Explicit: Explicit
        *  Justification: The paper describes a designed and controlled system. Learning is through optimization algorithms (GA, PPS), which are external control mechanisms. There is no description of spontaneous emergence of global structural order from local interactions without external directives defining the global structure or learning process.

### **4.2 Local Interaction Rules:**

*   **Vector ID:** M4.2
*   **Vector Type:** Rules
    *   Content: N/A
    *   CT-GIN Mapping: N/A
    * **Implicit/Explicit**: N/A
        *  Justification: Self-organization is not present, so local interaction rules leading to emergent global order are not described.

### **4.2.1 Local Interaction Parameters:**

* **Vector ID:** M4.2.1
* **Vector Type:** Table
*   Table:
    | Rule ID | Description | Parameter Name | Parameter Value Range | Units | Data Source | Implicit/Explicit | Justification |
    | :------ | :---------- | :------------- | :---------- | :---: | :----------: | :----------------: | :------------: |
    | N/A     | N/A         | N/A            | N/A         | N/A   | N/A         | N/A              | N/A          |
### **4.3 Global Order:**

*   **Vector ID:** M4.3
*   **Vector Type:** Order
    *   Content: N/A
    *   CT-GIN Mapping: N/A
    * **Implicit/Explicit**: N/A
        *  Justification: Self-organization is not present, so emergent global order is not applicable.

### **4.4 Predictability of Global Order:**

*   **Vector ID:** M4.4
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification: N/A
    * **Implicit/Explicit**: N/A
    *  Justification: N/A
    *   CT-GIN Mapping: N/A

### **4.5. Local Interaction Rules (for Self-Organization)**
* **Vector ID:** M4.5
* **Vector Type:** Table
*   Table:
| Rule ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Source |
| :------ | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :-----: |
| N/A     | N/A         | N/A       | N/A         | N/A   | N/A              | N/A          | N/A    |

### **4.6. Globally Emergent Order and Order Parameters**
* **Vector ID:** M4.6
* **Vector Type:** Table
*   Table:
| Property ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Protocol | Source |
| :---------- | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :------: | :-----: |
| N/A     | N/A         | N/A       | N/A         | N/A   | N/A              | N/A          | N/A    | N/A    |

### **4.7 Yoneda Embedding and Local-to-Global Mapping Fidelity**

*   **Vector ID:** M4.7
*   **Vector Type:** Table
*   Table:
    | Link Type | Description | Predictability | Yoneda Score | Metrics | Implicit/Explicit | Justification | Source |
    | :-------- | :---------- | :------------- | :----------- | :------ | :----------------: | :------------: | :-----: |
     | N/A     | N/A         | N/A            | N/A          | N/A     | N/A              | N/A          | N/A    |
    *   **Yoneda Embedding Fulfillment Score [0-10]:** [N/A]
    *   **Metrics:**  [N/A]
    *   **Justification:** [N/A]

## M5: Computation
*   **Vector ID:** M5
*   **Vector Type:** Computation

### **5.1 Embodied Computation Presence:**

*   **Vector ID:** M5.1
*   **Vector Type:** Binary
    *   Content: Yes
    *   Justification: Computation is embodied as the MNN physically transforms input forces/displacements to output displacements through its mechanical structure and tunable beam stiffnesses. This mapping function, analogous to an ANN, is physically implemented by the material itself via its interconnected beams and nodes, not solely by external digital control in operation although trained by external algorithm. The deformation of the lattice due to applied forces and resultant output displacements represent a form of embodied mechanical computation.
    *    Implicit/Explicit: Mixed
        *  Justification: Embodied computation concept is implied through analogy to ANNs and physical implementation of network mapping but is not explicitly labeled as "embodied computation" in those exact terms by the paper.

### **5.2 Computation Type:**

*   **Vector ID:** M5.2
*   **Vector Type:** Classification
    *   Content: Neuromorphic
    *   CT-GIN Mapping: `ComputationNode` type: `Neuromorphic`
    *    Implicit/Explicit: Explicit
    *    Justification: The paper explicitly draws an analogy between MNNs and ANNs, stating "MNNs are mechanical analogs to ANNs".  ANNs are foundational to neuromorphic computing. Tuning beam stiffness is compared to "how artificial neural networks (ANNs) tune their weights". This direct analogy classifies the computation as neuromorphic given the neural network inspiration and weight-like stiffness parameter tuning.

### **5.3 Computational Primitive:**

*   **Vector ID:** M5.3
*   **Vector Type:** Function
    *   Content: Weighted Summation and Non-linear Activation (Analog). The MNN performs a weighted summation operation through the interconnected beams, where stiffness acts as weights.  The physical deformation and force propagation through the lattice of beams and nodes leading to output displacements constitutes an analog computation. The non-linear force-displacement response option further introduces non-linearity analogous to activation functions in ANNs, though linear stiffness is also explored. Primitive is analogous to a mechanical neuron performing weighted summation and potentially non-linear activation.
    *   **Sub-Type (if applicable):** Weighted Summation (Linear or Non-linear)
    *   CT-GIN Mapping: Defines the primary function of the `ComputationNode`: `Weighted Summation (Analog)`
    *   Implicit/Explicit: Mixed
    * Justification: Weighted summation and non-linear activation are implied through ANN analogy and description of stiffness as "weights" and non-linear stiffness options.  The exact mathematical form of the embodied computation is not fully derived in terms of precise equations in the main text, relying on analogy.

### **5.4 Embodied Computational Units**
* **Vector ID:** M5.4
* **Vector Type:** Table
*   Table:
| Unit ID | Description | Processing Power | Energy/Operation | Freq/Resp. Time | Bit-Depth | Data Source | Implicit/Explicit | Justification |
| :------ | :---------- | :--------------- | :--------------- | :--------------: | :-------: | :----------: |:-----------------:| :-----------------:|
| Beam | Tunable beam as computational unit | N/A | N/A | Static Stiffness | Analog | Fig 2A | Implicit | No processing power metrics provided, static stiffness suggests rate limited by mechanical deformation timescales, analog nature implied by continuous stiffness tuning] |

## M6: Temporal Dynamics
*   **Vector ID:** M6
*   **Vector Type:** Temporal

### **6.1 Timescales:**

*   **Vector ID:** M6.1
*   **Vector Type:** ParameterTable
    *   Table:
        | Timescale Description | Value | Units | Source | Implicit/Explicit | Justification |
        | :-------------------- | :---: | :---: | :----: | :----------------: | :------------: |
        | Beam Stiffness Tuning Time | Unspecified | N/A | Section: Tunable beams | Implicit | Not explicitly quantified, assumed to be related to controller response and Instron testing cycle time |
        | Learning Time (PPS) | 2.68 | hours | Fig 4C | Explicit | Time taken for PPS algorithm to converge |
        | Learning Time (GA) | 111.13 | hours | Fig 4B | Explicit | Time taken for GA algorithm to converge |
        | Beam Response Time | Unspecified | N/A | Fig 2B | Implicit | Related to voice coil and flexure dynamics, faster than learning timescales |
    *   **Note:** Identify and quantify the *relevant timescales* of the system's dynamics (e.g., response time, process duration, oscillation period, memory decay, adaptation/learning timescale, self-assembly timescale). Use consistent units (e.g., seconds, milliseconds) for comparability.

### **6.2 Active Inference:**

*   **Vector ID:** M6.2
*   **Vector Type:** Assessment
    *   Content: No
    *   Justification: The MNN learns to minimize MSE, but this is driven by an external optimization algorithm (GA or PPS), not by the system itself actively predicting or inferring optimal stiffness states based on an internal model of its environment.  The system reacts to measured errors and adjusts parameters based on the algorithm's instructions; it doesn't exhibit independent prediction or model-based action selection to minimize surprise. Active inference implies an internal model and self-driven error minimization, which are not demonstrated in this externally trained MNN.
    *   Implicit/Explicit: Implicit
        *  Justification: Active inference is a higher-level cognitive function not explicitly claimed or demonstrated. The learning mechanism is described as optimization algorithm-driven error reduction, not self-predictive or model-based surprise minimization in the sense of active inference.
    *   **If Yes/Partial, provide examples of testable CT-GIN metrics that *could* be used to quantify active inference:** N/A

## M7: Adaptation
*   **Vector ID:** M7
*   **Vector Type:** Adaptation

### **7.1 Adaptive Plasticity Presence:**

*   **Vector ID:** M7.1
*   **Vector Type:** Binary
    *   Content: Yes
    *   Justification: The MNN exhibits adaptive plasticity by changing its beam stiffness (internal structure/parameter) in response to "prolonged exposure to unanticipated ambient loading scenarios".  This change is persistent in the stiffness values that are retained as memory. Learning "new behaviors" and relearning "previously mastered behaviors" demonstrates improved or altered functionality over time, going beyond simple immediate stimulus-response. This stiffness tuning is a persistent change based on experience (learning trials), indicating adaptive plasticity.
    *    Implicit/Explicit: Explicit
        * Justification:  "Learn behaviors", "relearn", "acquire new behaviors", "tuning stiffness" all explicitly point to adaptive plasticity – a change in system parameters (stiffness) based on experience (learning process) leading to functional change.

### **7.2 Adaptation Mechanism:**

*   **Vector ID:** M7.2
*   **Vector Type:** Description
    *   Content: The adaptation mechanism is stiffness tuning via optimization algorithms (GA and PPS).  For each loading scenario, the MSE between measured output displacements and target displacements is calculated.  Optimization algorithms (GA or PPS) then adjust beam stiffness values iteratively to minimize the MSE. This is a form of parameter tuning driven by feedback (MSE) from environmental interaction (loading scenarios and displacement measurements).  Algorithms are inspired by evolutionary computation (GA) and local search (PPS), acting as external learning rules guiding stiffness adaptation.  Equations or explicit algorithms for GA and PPS are not provided within the main text, referred to supplementary material and standard algorithms.
    *   CT-GIN Mapping: `AdaptationNode` type: `Parameter Tuning (Beam Stiffness)`, `Monad` edges: `type: Optimization Algorithm (GA/PPS)` Mechanism: `Error-driven Stiffness Adjustment`, Type of adaptation mechanism: `Optimization Algorithm (GA/PPS)`
    *    Implicit/Explicit: Mixed
        *  Justification: Stiffness tuning and use of optimization algorithms as adaptation mechanisms are explicitly described.  Details of the algorithm, equations, and precise implementation are not elaborated upon in the main text.

## M8: Emergent Behaviors
*   **Vector ID:** M8
*   **Vector Type:** Behavior

### **8.1 Behavior Description:**

*   **Vector ID:** M8.1
*   **Vector Type:** Description
    *   Content: The main functional behavior is shape morphing. The MNN learns to deform into specific target shapes (sinusoidal contours) in response to different input force scenarios (horizontal or vertical forces).  Observable behaviors are the displacements of output nodes conforming to desired sinusoidal curves when specific forces are applied to input nodes. The system "learns two different shape-morphing behaviors simultaneously."
    *   CT-GIN Mapping: `BehaviorArchetypeNode`. Specify the type of behavior: `Shape Morphing`
    *    Implicit/Explicit: Explicit
       *  Justification: Shape morphing is explicitly described as the desired and demonstrated behavior. Target sinusoidal shapes and response to different force inputs are operational definitions of this behavior.

### **8.2 Behavior Robustness:**

*   **Vector ID:** M8.2
*   **Vector Type:** Score
    *   Score: [5]
    *   Justification: Robustness is partially implied by the statement that MNNs can "relearn previously mastered behaviors and acquire new behaviors as needed with exposure to changing ambient conditions [damaged, cut, refixtured]". This suggests some robustness against structural changes and varying conditions, demonstrating relearning capability. However, quantitative metrics for robustness (e.g., tolerance to noise in inputs, operational window for stiffness values, resilience to damage in terms of performance degradation) are not provided. Qualitative assessment: Medium, indicating some adaptive robustness through relearning but no quantified resilience metrics.
    *   Implicit/Explicit: Mixed
        *  Justification: Relearning capability implies some robustness, but lack of quantitative robustness metrics and qualitative assessment means robustness is only partially supported and understood from the provided text.

### **8.3 CT-GIN Emergent Behavior Validation**

*    **Vector ID:** M8.3
*    **Vector Type:** Validation
     *  Content: Validation is performed experimentally and through simulations. Experimental validation involves fabricating an MNN and demonstrating learning of two shape-morphing behaviors by tracking output node displacements (Fig 4, Movies S2, S3, S4). Simulations using a computational tool informed by beam characteristics verify learning in different lattice sizes, configurations, and behavior numbers (Fig 5, Fig S12). Control experiments and quantitative analysis are used by comparing MSE over time (Fig 4B, 4C, 4D, Fig 5A, 5B, 5C). Robustness is implied by relearning capability (text statement) but not directly validated through specific robustness experiments. Limitations: Quantified validation primarily focuses on MSE reduction during learning, rather than comprehensive robustness or failure mode analysis.
     *   Implicit/Explicit: Mixed
    *   Justification: Validation methods (experiments and simulations) and metrics (MSE plots) are explicitly described. Robustness validation is implied but not explicitly designed or quantified beyond relearning concept mention.

## M9: Cognitive Proximity
*   **Vector ID:** M9
*   **Vector Type:** Cognition

### **9.1 Cognitive Mapping:**

*   **Vector ID:** M9.1
*   **Vector Type:** Description
    *   Content: The paper explicitly draws a cognitive mapping by comparing MNNs to Artificial Neural Networks (ANNs) and biological brains.  "Scientists have been inspired by the interconnected network of neurons...and enable complex learning...mimic natural learning for numerous AI applications." "MNNs mechanically learn behaviors analogously to how ANNs mathematically map numerical inputs to outputs." "MNNs are mechanical analogs to ANNs in that they map force and displacement inputs and outputs using tunable beams, which are analogous to weights, and physical nodes, which are analogous to neurons." The analogy is primarily structural and functional, comparing components (beams/weights, nodes/neurons) and learning mechanisms (stiffness/weight tuning).  Limitations: Analogy is at a high level of abstraction focusing on network architecture and learning principle,  not a detailed mapping of specific cognitive functions or biological neural processes.
    *   CT-GIN Mapping: `CognitiveMappingEdge`. Source: `BehaviorArchetypeNode (Shape Morphing)`, Target: `CognitiveFunctionNode (Learning, Pattern Recognition)`.
    *   Implicit/Explicit: Explicit
    * Justification: The paper explicitly uses the analogy to ANNs and biological brains to frame MNNs in a cognitive context.

### **9.2 Cognitive Proximity Score:**

*   **Vector ID:** M9.2
*   **Vector Type:** Score
    *   Score: [3]
    *   Justification: Level 3: Reactive/Adaptive Autonomy. The MNN adapts its behavior (shape morphing) based on experience (learning process) and feedback (MSE minimization), but within a limited behavioral repertoire (shape morphing). It demonstrates learning and adaptation analogous to ANNs, but lacks goal-directedness beyond achieving target shapes, contextual understanding, or higher-level cognitive functions. It is reactive in the sense that it learns responses to predefined loading scenarios and targets, rather than exhibiting autonomous goal formulation or complex relational reasoning. Falls short of Level 4 (Goal-Directed/Model-Based) as no internal models or planning are evident.
    *   Implicit/Explicit: Mixed
    *  Justification: Score is Mixed, based on explicit analogy to ANNs (suggesting some cognitive proximity), but limited by the observed behavior being primarily reactive and adaptive parameter tuning within a predefined task (shape morphing), placing it at Level 3 of the Cognizance Scale, requiring implicit evaluation based on scale's criteria and system capabilities.

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
    | Sensing/Perception               | 4          | Strain gauges sense deformation (stimuli). Limited to mechanical strain.                   | `CognitiveFunctionNode: Sensing`    | Explicit          | Sensors explicitly used to measure deformation |
    | Memory (Short-Term/Working)        | 5          | Stiffness configuration acts as working memory during learning. Limited retention data.   | `CognitiveFunctionNode: Memory (Short-Term)` | Implicit          | Stiffness changes during learning and behavior expression suggests working memory function |
    | Memory (Long-Term)                 | 6          | Stiffness values retained as memory. Relearning implies long-term retention. No degradation data. | `CognitiveFunctionNode: Memory (Long-Term)`  | Implicit          | Relearning capability and "mechanical muscle memory" imply long-term retention|
    | Learning/Adaptation              | 7          | Stiffness tuning via GA/PPS represents learning. Adapts to loading scenarios.              | `CognitiveFunctionNode: Learning`   | Explicit          | Learning and adaptation to loading scenarios is the core focus of the paper |
    | Decision-Making/Planning          | 2          | Limited decision making. Algorithm decides stiffness updates. MNN reacts to input.        | `CognitiveFunctionNode: Decision-Making` | Implicit          | No evidence of planning or independent decision making beyond reactive stiffness adjustments |
    | Communication/Social Interaction | 0          | No communication or social interaction capabilities described.                          | N/A                                   | Explicit          | Not mentioned |
    | Goal-Directed Behavior            | 3          | Goal is pre-defined target shape morphing. No autonomous goal formulation.              | `CognitiveFunctionNode: Goal-Directed Behavior` | Implicit          | Goal is externally set target shape, not internally derived or flexible |
    | Model-Based Reasoning              | 1          | No evidence of internal models or reasoning beyond parameter tuning based on error.      | `CognitiveFunctionNode: Model-Based Reasoning` | Implicit          | Learning is primarily error-driven optimization, not model-predictive |
    | **Overall score**                 |      [3.5]       | Average of scores above                                                                                       |                                   |                     |                |

    *   **Note:** Assess the system for *each* function, providing a score (0-10) and a short (1-2 sentences) justification.  0 = Absent, 10 = Human-level performance.

## M10: Criticality Assessment
*   **Vector ID:** M10
*   **Vector Type:** Criticality

### **10.1 Criticality:**

*   **Vector ID:** M10.1
*   **Vector Type:** Assessment
    *   Content: Unclear
    *   Justification: The paper does not discuss criticality, scale-free behavior, power laws, or long-range correlations in the MNN system. The system is described as a network, and neural networks can exhibit critical behavior in certain regimes, but this is not analyzed or mentioned in the context of MNNs in this paper.  While complex network behavior is present, evidence for criticality is absent. Assessment: Unclear due to lack of data or discussion related to criticality.
        *   Critical Parameters (If Yes/Partial): N/A
        *   Evidence: N/A
    *   Implicit/Explicit: Implicit
    *    Justification: Absence of discussion or data about criticality leaves its presence unclear. Criticality is not explicitly addressed, nor is there implicit data suggestive of critical phenomena (power laws, long-range correlations) within the provided text.

## M11: Review Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Review")**

*   **Vector ID:** M11
*   **Vector Type:** Review

### **11.1 Literature Synthesis Quality:**

*   **Vector ID:** M11.1
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification: N/A
    *    Implicit/Explicit: N/A
         *  Justification: N/A

### **11.2 Gap Identification:**

*   **Vector ID:** M11.2
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification: N/A
    *   Implicit/Explicit: N/A
        *  Justification: N/A

### **11.3 Future Directions:**

*   **Vector ID:** M11.3
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification: N/A
    *    Implicit/Explicit: N/A
    *   Justification: N/A

### **11.4 Review Paper CT-GIN Alignment Score**

*   **Vector ID:** M11.4
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification: N/A
    *    Implicit/Explicit: N/A
        *  Justification: N/A

## M12: Theoretical Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Theoretical")**

*   **Vector ID:** M12
*   **Vector Type:** Theory

### **12.1 Theoretical Rigor:**

*   **Vector ID:** M12.1
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification: N/A
       * Implicit/Explicit: N/A
       *  Justification: N/A

### **12.2 Realization Potential:**

*   **Vector ID:** M12.2
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification: N/A
    *   Implicit/Explicit: N/A
    *  Justification: N/A

### **12.3 Potential for Future CT-GIN Implementation Score**

* **Vector ID:** M12.3
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification:  N/A
    *    Implicit/Explicit: N/A
    *   Justification: N/A

## M13: Overall Assessment & Scoring

*   **Vector ID:** M13
*   **Vector Type:** Overall

### **13.1 CT-GIN Readiness Score:**

*   **Vector ID:** M13.1
*   **Vector Type:** Score
*   **Calculated Score:** [4.3]  (Average of scores from Modules 1-4, M8.2 and M9.2, scores with N/A convert in 0).  *This score MUST be automatically calculated. Only Number.*

**CT-GIN Readiness Summary Table:**

| CT-GIN Aspect                   | Strength (Yes/Partial/No) | Key Supporting Metrics (with units) | Limitations (Missing Metrics/Data Gaps)                                           | Improvement Areas (Future Research)                                          |
| :------------------------------ | :-----------------------: | :-----------------------------------| :------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| Energy Flow Efficiency          | No                         | Qualitative: Low                     | Quantitative efficiency metrics, dissipation distribution                          | Optimize energy transduction, reduce dissipation, explore passive stiffness tuning|
| Memory Fidelity                 | Partial                    | MSE (GA): 0.006 mm^2, MSE (PPS): 0.063 mm^2 | Retention time, degradation rate, capacity limits                                  | Quantify memory characteristics, enhance fidelity and capacity, explore distributed memory mechanisms |
| Organizational Complexity       | Yes                        | Triangular lattice, 21 beams         | Local interaction rules for self-organization                                   | Explore self-organizing structures, implement local interaction based learning rules|
| Embodied Computation            | Yes                        | Neuromorphic, Analog                 | Processing power, energy per operation, response time, computational primitives | Quantify computational performance, explore complex primitives, optimize energy efficiency |
| Temporal Integration            | Partial                    | Learning Time (hours)                | Beam response time, detailed dynamics timescales                                  | Characterize dynamic timescales, explore temporal coding in memory and computation |
| Adaptive Plasticity             | Yes                        | Relearning capability              | Adaptation mechanism details, plasticity limits                                 | Explore diverse adaptation mechanisms, enhance plasticity and adaptability to novel environments |
| Functional Universality         | No                         | Shape Morphing                       | Demonstration of diverse behaviors (computation, sensing, locomotion)          | Expand behavioral repertoire beyond shape morphing, demonstrate functional versatility |
| Cognitive Proximity            | Partial                    | Cognizance Level 3                   | Higher cognitive function assessment (goal-directedness, planning, reasoning)     | Implement goal-directedness, model-based reasoning, explore higher cognitive functions |
| Design Scalability & Robustness | Partial                    | Relearning after damage (qualitative) | Quantitative robustness metrics (noise tolerance, failure rates), scalability analysis | Quantify robustness and scalability, design for fault tolerance, improve robustness |
| **Overall CT-GIN Readiness Score** |        4.3               |   Average from modules             | See limitations per aspect                                                     | See improvement areas per aspect                                           |


### **13.2 Qualitative CT-GIN Assessment Conclusion:**

*   **Vector ID:** M13.2
*   **Vector Type:** Textual Summary
    *   Content: The Mechanical Neural Network (MNN) demonstrates promising initial steps towards material intelligence, particularly in embodied computation and adaptive plasticity. Key strengths lie in its ability to learn mechanical behaviors through stiffness tuning, analogous to neural networks, and its experimental validation of shape morphing. Limitations include low energy efficiency due to active control, lack of self-organization, limited functional universality (focused on shape morphing), and low cognitive proximity (reactive adaptation, not goal-directed or model-based). The system exhibits reactive/adaptive autonomy (Cognizance Level 3) through parameter tuning, but falls short of higher cognitive functions. Overall assessment: The MNN is a valuable experimental platform for exploring learning in architected materials, demonstrating embodied computation and adaptive plasticity within a limited behavioral scope. Its potential within CT-GIN lies in further developing self-organization, enhancing energy efficiency, expanding functional universality, and progressing towards higher cognitive functions.

### **13.3 CT-GIN Refinement Directions:**

*   **Vector ID:** M13.3
*   **Vector Type:** Recommendations
    *   * Enhance Energy Efficiency: Explore passive mechanisms for stiffness tuning and behavior expression, reducing reliance on active control and electromechanical transduction to minimize energy dissipation and improve efficiency.
    *   * Incorporate Self-Organization: Design MNNs capable of self-assembling or reconfiguring their structure based on local interaction rules, moving beyond externally designed lattices to achieve emergent structural order and potentially more robust and adaptable systems.
    *   * Expand Functional Universality: Investigate MNNs for diverse behaviors beyond shape morphing, such as mechanical computation, sensing, locomotion, and self-healing, to broaden their functional repertoire and demonstrate greater versatility.
    *   * Advance Cognitive Proximity: Explore mechanisms for goal-directed behavior and model-based reasoning in MNNs, moving beyond reactive adaptation to enable planning, anticipation, and more flexible, context-aware responses, potentially by implementing internal models within the material architecture.
    *   * Quantify Robustness and Scalability: Conduct systematic studies to quantify robustness against noise, damage, and parameter variations, and analyze scalability of MNN designs to larger and more complex systems, establishing reliable performance metrics.
    *   * Investigate Temporal Dynamics: Characterize and optimize temporal dynamics, including response times, learning timescales, and memory retention, to enhance the system’s capacity for dynamic and time-sensitive tasks, potentially exploring temporal coding.

## M14: CT-GIN Knowledge Graph

*   **Vector ID:** M14
*   **Vector Type:** Visualization

### **14.1. CT-GIN Knowledge Graph:**
* **Content:**
[__Textual Description of CT-GIN Knowledge Graph (Schematic Diagram Approximation):__

**Node Types (Shapes/Colors):**
*   `SystemNode` (Circle/Blue): "Mechanical Neural Network" - Attributes: `systemType: Mechanical Neural Network`, `domain: Mechanical Metamaterials`, `mechanism: Tunable Beam Stiffness Adjustment`, `components: Tunable Beams, Nodes, Actuators, Sensors, Controller, Optimization Algorithm`, `purpose: Learning Mechanical Behaviors and Properties`
*   `EnergyInputNode` (Square/Red): "Mechanical Force" - Attributes: `source: Voice coil actuators/Simulation Software`, `type: Mechanical Force`, `value: ±2 N (Simulation)`
*   `EnergyDissipationNode` (Diamond/Black): "Energy Losses" - Attributes: `type: Heat, Friction, Electrical Resistance`
*   `MemoryNode` (Triangle/Green): "Beam Stiffness Memory" - Attributes: `type: Analog Parameter Memory (Beam Stiffness)`, `retention: Long-term (Qualitative)`, `capacity: Multiple Behaviors`, `readout_accuracy: MSE Achieved`
*   `ComputationNode` (Hexagon/Orange): "Neuromorphic Computation" - Attributes: `type: Neuromorphic`, `primitive: Weighted Summation (Analog)`
*   `BehaviorArchetypeNode` (Star/Purple): "Shape Morphing" - Attributes: `type: Shape Morphing`, `robustness_score: 5/10`
*   `CognitiveFunctionNode` (Ellipse/Yellow):
    *   "Sensing": Score 4/10
    *   "Memory (Short-Term)": Score 5/10
    *   "Memory (Long-Term)": Score 6/10
    *   "Learning": Score 7/10
    *   "Decision-Making": Score 2/10
    *   "Goal-Directed Behavior": Score 3/10
    *   "Model-Based Reasoning": Score 1/10

**Edge Types (Labels/Arrows):**
*   `EnergyTransductionEdge` (Solid Arrow/Red): "Electromechanical Transduction" - Attributes: `mechanism: Electromechanical transduction, Force propagation, Strain sensing, Stiffness modulation`, `efficiency: Low (Qualitative)` - From: `EnergyInputNode (Electrical)` to `Mechanical Deformation (Beams)`, From: `Mechanical Deformation (Beams)` to `EnergyOutputNode (Electrical Strain Gauge Signals)`
*   `EnergyDissipationEdge` (Dashed Arrow/Black): "Dissipation" - Attributes: `mechanism: Ohmic heating, Mechanical Friction, Electrical Losses` - From: `EnergyTransductionEdge` to `EnergyDissipationNode`
*   `Monad` (Solid Arrow/Green): "Optimization-Driven Adaptation"- Attributes: `type: Optimization Algorithm (GA/PPS)`, `Mechanism: Error-driven Stiffness Adjustment`, `Adaptation Type: Optimization Algorithm (GA/PPS)` - From: `BehaviorArchetypeNode` to `MemoryNode` (Stiffness Tuning)
*   `CognitiveMappingEdge` (Dotted Arrow/Yellow): "ANN Analogy" - From: `BehaviorArchetypeNode (Shape Morphing)` to `CognitiveFunctionNode (Learning, Pattern Recognition)`

**Parameters and Units Annotated on Nodes/Edges (Examples):**
*   `EnergyInputNode`: Value: ±2 N (Simulation)
*   `MemoryNode`: Readout Accuracy: MSE Achieved (units mm^2 from Fig 4B, 4C, 4D, Fig 5A, 5B, 5C)
*   `BehaviorArchetypeNode`: Robustness Score: 5

__End of Knowledge Graph Description__]

## M15: Relationship Vectors
*   **Vector ID:** M15
*   **Vector Type:** Relationships
*   Relationships:
        | Source Vector ID | Target Vector ID | Relationship Type |
        | ------------- | ------------- | ----------------- |
        | M2.1 | M2.2 | Energy Flow |
        | M2.2 | M2.4 | Energy Dissipation |
        | M2.1 | M8.1 | Input to Behavior |
        | M3.1 | M7.1 | Memory enables Adaptation |
        | M5.1 | M8.1 | Computation enables Behavior |
        | M7.2 | M3.1 | Adaptation modifies Memory |
        | M9.1 | M8.1 | Cognitive Mapping related to Behavior |

## M16: CT-GIN Template Self-Improvement Insights

*   **Vector ID:** M16
*   **Vector Type:** Feedback

### **Template Feedback:**

*    **Vector ID:** M16.1
*   **Vector Type:** Text
Provide specific, actionable feedback on the *CT-GIN template itself*, based on this analysis:
    *   **Missing Probes:**  Probes for quantifying robustness in more varied and specific ways (e.g., robustness against temperature variations, mechanical damage type/extent, sensor noise levels) would be beneficial particularly for experimental papers. A probe to explicitly assess design scalability could be added to Module M1.
    *   **Unclear Definitions:** The definition of "Active Inference" in M6.2 could be further clarified with more operational criteria testable in material systems, for example, explicit mention of predictive coding or predictive error minimization metrics applicable to physical systems.
    *   **Unclear Node/Edge Representations:** The guidance for mapping to GIN nodes/edges is generally sufficient. However, for complex systems, it might be useful to have more examples of breaking down nested or hierarchical aspects into distinct nodes and edges to represent the system's architecture multileveled organization.
    *   **Scoring Difficulties:** Scoring "Cognitive Proximity" remains somewhat subjective, despite the scale provided. Providing more granular descriptions for each level with specific, measurable criteria applicable to material systems would enhance objectivity and consistency across different analyses.  The distinction between levels 2 and 3 could be more operationally defined in terms of measurable system properties.
    *   **Data Extraction/Output Mapping:**  The template is generally well-structured for data extraction. Mapping qualitative assessments into CT-GIN framework, such as "Low Energy Efficiency," could be facilitated by suggesting standard qualitative descriptors as attributes for relevant edges.  The 'Note' sections in parameter tables are helpful reminders.
    *   **Overall Usability:** The template is comprehensive and generally usable, although lengthy for detailed papers.  Breaking down some of the larger sections (e.g., M3, M4, M9) into more subsections could improve navigation and focused analysis on specific sub-aspects within each module.
    * **Specific Suggestions:**
        * Add more specific robustness probes in M8.2, detailing types of robustness to assess.
        * Refine "Active Inference" definition in M6.2 with operational criteria for material systems.
        * Provide more examples of hierarchical CT-GIN modeling for complex systems in template guidance for M14.
        * Elaborate cognitive proximity scale in M9.2 with more granular, measurable criteria for each level.
        * Include standard qualitative descriptors as attribute options for edges for parameters that cannot be quantified numerically in the template guidance.
