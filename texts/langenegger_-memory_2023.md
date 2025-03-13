# In-memory factorization of holographic perceptual representations:

__Paper Type:__ Experimental

## M1: System Overview & Implementation
*   **Vector ID:** M1
*   **Vector Type:** Overview

### **1.1 System Description**

*   **Vector ID:** M1.1
*   **Vector Type:** Description
    *   Content: The system is an experimental in-memory compute engine designed to efficiently factorize high-dimensional holographic vector representations. It combines brain-inspired hyperdimensional computing with analog in-memory computing (IMC) using phase-change memristive devices arranged in crossbar arrays. The system iteratively factorizes a product vector, representing combined attributes of a sensory signal, into its constituent attribute vectors by performing matrix-vector multiplications (MVM) in memory. This is achieved by storing codebooks (sets of basis vectors for attributes) in memristive crossbar arrays. The system exploits the intrinsic stochasticity of memristive devices and sparse activation functions to enhance performance and overcome limitations of deterministic resonator networks. The purpose is to efficiently solve large-scale factorization problems relevant to sensory perception and artificial intelligence.
    *   CT-GIN Mapping: `SystemNode` attributes: `systemType: Hybrid`, `domain: Artificial Intelligence, Neuromorphic Computing, Sensory Perception`, `mechanism: In-memory computing, holographic vector factorization, resonator network, stochastic computation`, `components: Phase-change memristive devices, crossbar arrays, analog-to-digital converters, digital control logic`, `purpose: Efficient factorization of high-dimensional holographic vectors, disentanglement of sensory attributes`
    *   Implicit/Explicit: Mixed
        *  Justification: The system's components, purpose, and general operation are explicitly described in the introduction and throughout the paper. The brain-inspired nature and connection to holographic representation are also explicit. However, the categorization as "hybrid" and the detailed breakdown of the domain and mechanism into specific aspects require some interpretation and synthesis of the explicitly stated information.

### **1.2 Implementation Clarity**

*   **Vector ID:** M1.2
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The implementation is relatively clear. The paper details the use of PCM devices in crossbar arrays, explains the in-memory MVM operations for similarity calculation and projection, and describes the role of stochasticity and sparse activations. Figures 1, 2, and 4 provide visual aids to understand the architecture and experimental setup. The Methods section further elaborates on the experimental procedures and parameter optimization. However, some lower-level details of the hardware implementation, such as specific circuit designs within the IMC cores and the permute logic, are not fully elaborated, leading to a slightly less than perfect clarity.
    *   Implicit/Explicit: Mixed
        * Justification: The overall architecture and key principles are explicitly described with supporting figures. The clarity score is based on a mixed assessment, acknowledging both the explicit details provided and the implicit understanding required for certain implementation aspects not fully detailed.

### **1.3 Key Parameters**

*   **Vector ID:** M1.3
*   **Vector Type:** ParameterTable
    *   Table:
        | Parameter Name | Value | Units | Source (Fig/Table/Section) | Implicit/Explicit | Data Reliability (High/Medium/Low) | Derivation Method (if Implicit) |
        | :------------- | :---: | :---: | :-----------------------: | :-----------------: | :-----------------------------: | :-------------------------------: |
        | Vector Dimensionality (D) | 256 | Dimensions | II, Large-Scale Experimental Demonstration | Explicit | High | N/A |
        | Codebook Size (M) | 256 | Vectors per codebook | II, Large-Scale Experimental Demonstration | Explicit | High | N/A |
        | Number of Factors (F) | 3 | Factors | II, Large-Scale Experimental Demonstration | Explicit | High | N/A |
        | Crossbar Array Size | 256x256 | Unit cells | II, Large-Scale Experimental Demonstration | Explicit | High | N/A |
        | Max Iterations (N) | 21,845 | Iterations | II, Large-Scale Experimental Demonstration | Explicit | Medium |  Constrained to ensure lower complexity than brute-force search (Methods) |

    *   **Note:** List *up to 5* key parameters characterizing the system's *implementation*.  Provide values and units if possible. If a parameter is not explicitly stated but derived/inferred, clearly state the derivation method. *Always* include units if applicable. If a value is not applicable, write "N/A".  Data Reliability: High = Directly measured, Medium = Derived from measurements/simulations, Low = Estimated/Inferred.

## M2: Energy Flow
*   **Vector ID:** M2
*   **Vector Type:** Energy

### **2.1 Energy Input**

*   **Vector ID:** M2.1
*   **Vector Type:** Input
    *   Content: The energy input is electrical voltage pulses applied to the wordlines of the memristive crossbar arrays. The input is modulated using Pulse-Width Modulation (PWM).
    *   Value: Constant pulse-width modulated voltage
    *   Units: Volts (V), Pulse width (time units)
    *   CT-GIN Mapping: `EnergyInputNode`: attributes - `source: Electrical voltage pulses`, `type: Electrical`
    *   Implicit/Explicit: Explicit
        *  Justification: Described in the section "Large-Scale Experimental Demonstration" and Methods, specifically mentioning constant pulse-width modulated voltage.

### **2.2 Energy Transduction**

*   **Vector ID:** M2.2
*   **Vector Type:** Transduction
    *   Content: Electrical energy in the form of voltage pulses is applied to the wordlines of the memristive crossbar. This voltage drives current through the PCM devices in the crossbar array due to Ohm's law. The conductance of the PCM devices, programmed to represent the codebook vectors, modulates the current. Kirchhoff’s current summation law at the bitlines sums these currents, effectively performing the matrix-vector multiplication in the analog domain (electrical current). This analog current is then converted to a digital signal by analog-to-digital converters (ADCs). This digital signal is used for subsequent digital processing (unbinding, activation, bipolarization) and to drive the next iteration of MVM in the second core for projection. The energy transduction is primarily electrical to electrical, mediated by the resistive switching behavior of PCM devices.
    *   CT-GIN Mapping: `EnergyTransductionEdge`: attributes - `mechanism: Resistive switching, Ohm's Law, Kirchhoff's Current Law, Analog-to-digital conversion`, `from_node: EnergyInputNode`, `to_node: ComputationNode (Similarity Calculation, Projection)`
    *   Implicit/Explicit: Mixed
        *  Justification: The paper explicitly states Ohm's law and Kirchhoff’s current summation law are exploited for MVM operations. The flow from voltage input to current summation and ADC conversion is also explicit. The description of the role of PCM conductance and its modulation of current is implicit but directly inferable from the description of memristive device operation in crossbar arrays.

### **2.3 Energy Efficiency**

*   **Vector ID:** M2.3
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification/Metrics: The paper estimates an energy saving of 12.2x compared to a reference digital design for factorizing a single query. A custom-designed in-memory factorizer is estimated to consume 33.1 µJ per query on average, compared to 402 µJ for the reference digital design (Supplementary Note 4).  The in-memory MVM operation is stated to have O(1) time complexity, independent of matrix size, reducing computational time complexity. Energy efficiency is achieved through in-place computation and reduced number of iterations. The efficiency is high relative to digital designs for the specific task as demonstrated by experimental estimations, although absolute energy efficiency compared to theoretical limits is not discussed.
    *   CT-GIN Mapping: Attribute of relevant `EnergyTransductionEdge`s: `efficiency_relative_to_digital: 12.2x improvement`, `energy_per_query_in_memory: 33.1 µJ`, `energy_per_query_digital_reference: 402 µJ`
    *   Implicit/Explicit: Mixed
      *  Justification: The energy saving metric and comparison to digital design are explicitly stated in the Discussion and Supplementary Note 4. The justification for high efficiency (in-place computation, O(1) time complexity) are also explicit. The efficiency score is a mixed assessment, taking into account the explicit quantifiable metrics and the implicit context of comparison against digital approaches for a specific operation.

### **2.4 Energy Dissipation**

*   **Vector ID:** M2.4
*   **Vector Type:** Dissipation
    *   Content: Energy dissipation mechanisms include:
        *   **Resistive heating in PCM devices and interconnects within the crossbar array:** Quantified implicitly through overall energy consumption of the crossbar operation.
        *   **Energy consumption in peripheral circuits:** PWM generation, ADC conversion, digital logic for unbinding, activation, and permutation. Quantified as separate energy components in Supplementary Note 4 (e.g., DAC, ADC energy).
        *   **Leakage currents in PCM devices and CMOS circuits:**  Not explicitly quantified but implicitly contributes to power consumption.
        *   **Energy loss during analog-to-digital conversion:** Accounted for in ADC energy consumption.

    *   CT-GIN Mapping: `EnergyDissipationNode` attributes: `mechanism: Resistive heating, peripheral circuit dissipation, leakage currents, ADC conversion loss`, `type: Heat, Electrical Loss` ; `EnergyDissipationEdge` attributes: `mechanism: Resistive heating`, `from_node: EnergyTransductionEdge (Crossbar operation)`, `to_node: EnergyDissipationNode`
    *    Implicit/Explicit: Mixed
        *  Justification:  Resistive heating is implicitly understood as a primary dissipation mechanism in resistive devices. The energy consumption related to peripheral circuits (PWM, ADC) is explicitly broken down in Supplementary Note 4, quantifying a part of dissipation. Leakage currents and ADC conversion loss are implicitly present dissipation mechanisms in such systems and are standard sources of energy loss in electronic circuits, though not explicitly quantified in this specific paper text.

## M3: Memory
*   **Vector ID:** M3
*   **Vector Type:** Memory

### **3.1 Memory Presence:**

*   **Vector ID:** M3.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: The codebooks, representing attribute vectors, are stored non-volatility in the phase-change memory (PCM) devices within the crossbar arrays. This storage of codevectors constitutes memory, as it's a persistent change in the system's physical state (conductance of PCM devices) that is retained over time. This memory directly influences future behavior by defining the matrix used in subsequent MVM operations for factorization. The non-volatile nature ensures that the codebooks persist even without continuous power, influencing factorization performance over extended periods.
    *    Implicit/Explicit: Explicit
        * Justification: The paper explicitly states "non-volatile storage of the codebooks is an added advantage compared to the digital design." and mentions "bipolar codebooks are stored in two out of four devices". This explicitly indicates the presence of memory in the PCM devices for storing codebooks.

### **3.2 Memory Type:**

*   **Vector ID:** M3.2
*   **Vector Type:** Score
*   Score: [7]
*   Justification: The memory is implemented using phase-change memory (PCM) devices, offering non-volatile storage.  The codebook values are stored as conductance states in PCM cells. Retention is long-term due to non-volatility. Capacity per cell is somewhat limited to analog conductance levels, effectively storing bipolar (+1/-1) values discretely but with analog variability. Readout accuracy is affected by the stochasticity and variability inherent in PCM devices, influencing the accuracy of MVM operations. While not perfect digital memory (score 10), it offers robust non-volatile storage suitable for the application. The score reflects the non-volatile nature and practical utility, balanced by the analog variability and limited per-cell discrete state storage.
*   CT-GIN Mapping: Defines the `MemoryNode` type: `memoryType: Phase-Change Memory (PCM)`
*    Implicit/Explicit: Mixed
    * Justification: The type of memory (PCM) and non-volatility are explicitly mentioned. The score and detailed justification concerning retention, capacity, and readout accuracy derive from a mixed understanding. While the paper mentions stochasticity affecting MVM, a detailed quantitative breakdown of memory fidelity and robustness is implicit.

### **3.3 Memory Retention Time:**

*   **Vector ID:** M3.3
*   **Vector Type:** Parameter
*   Value: Long-term
*    Units: Qualitative Descriptor: "Long-term"
*   Justification: Phase-change memory is inherently non-volatile, meaning data retention is expected to be long-term, persisting for years without power. While the paper doesn't give a specific retention time in hours, days, or years, the context of non-volatile storage implies long-term retention relevant for retaining codebooks over operational timescales of AI systems.
*    Implicit/Explicit: Explicit
        * Justification:  The non-volatile nature of PCM is explicitly stated in the Discussion section as "The non-volatile storage of the codebooks is an added advantage compared to the digital design". This directly implies a long retention time compared to volatile memory.
*   CT-GIN Mapping: Key attribute of the `MemoryNode`: `retentionTime: Long-term`

### **3.4 Memory Capacity (Optional - if applicable)**

* **Vector ID:** M3.4
* **Vector Type:** Parameter
*  Value: 1 bit (effective per cell, bipolar)
*   Units: bits/cell
*   Justification: Each unit cell in the crossbar array stores bipolar codebook values (+1 or -1) using PCM devices. Although PCM itself can have multi-level cell (MLC) capability, in this configuration, each cell effectively stores one bit of information representing a bipolar weight in the codebook. The paper mentions storing "bipolar codebooks are stored in two out of four devices", further suggesting a 1-bit effective storage for each bipolar weight value. The total capacity depends on the array size and number of codevectors, but per cell, it is effectively 1-bit for the implemented bipolar representation.
*    Implicit/Explicit: Implicit
        *  Justification: While the paper doesn't explicitly say "1 bit per cell capacity", the description of storing bipolar codebooks (+1/-1 values) in PCM devices implicitly indicates an effective 1-bit storage per cell in this application.

### **3.5 Readout Accuracy (Optional - if applicable)**

* **Vector ID:** M3.5
* **Vector Type:** Parameter
*   Value: Affected by stochasticity
*   Units: Qualitative Descriptor: "Affected by stochasticity"
*   Justification: The paper emphasizes the "intrinsic stochasticity associated with crystal nucleation and growth" in PCM devices and read noise (1/f and random telegraph noise). Figure 4b shows the distribution of measured output, indicating variability. This stochasticity directly affects the readout accuracy of the stored codebook values during MVM operations, as the output current will have a distribution rather than a precise deterministic value. The stochasticity is even exploited as a computational resource. While not numerically quantified as a percentage or error rate, the paper clearly indicates that readout is not perfectly accurate due to inherent device variability.
*    Implicit/Explicit: Explicit
       *  Justification: The paper explicitly discusses and highlights the "intrinsic stochasticity" of PCM devices and its role in the system's operation. Figure 4b visually confirms the distribution of measured output reflecting readout variability.

### **3.6 Degradation Rate (Optional - if applicable)**
* **Vector ID:** M3.6
* **Vector Type:** Parameter
    *   Value: Increases slightly over time
    *   Units: Qualitative Descriptor: "Slight increase over time"
    *   Justification: The paper mentions that "This distribution [of conduction values] will get slightly broader with time as a result of the variability associated with the structural relaxation of the atomic configuration in each device". This structural relaxation (drift) is a known phenomenon in PCM devices that causes conductance values to change slowly over time, leading to a gradual degradation in the stored memory values and potentially influencing readout accuracy if not periodically refreshed or compensated for (though refresh is not mentioned in the paper).
    *    Implicit/Explicit: Explicit
            * Justification:  The statement regarding the broadening of the conductance distribution over time due to structural relaxation is explicitly mentioned in the "Large-Scale Experimental Demonstration" section.
    *   CT-GIN Mapping: Attribute of the `MemoryNode`: `degradationRate: Slight increase over time due to structural relaxation`

### **3.7 Memory Operations Energy Cost (Optional - if applicable)**
* **Vector ID:** M3.7
* **Vector Type:** Table
*   Table:
    | Memory Operation ID | Energy Consumption per Bit | Power Usage during Operation| Units | Uncertainty | Data Source Reference | Implicit/Explicit | Justification |
    | :------------------ | :--------------------------: | :-----------------------------: | :---: |:-----------------:|:-----------------:|:-----------------:| :------------------ |
    | Program (Write) | N/A | N/A | N/A | N/A | N/A | N/A | Programming energy cost not explicitly quantified, only read (MVM) is detailed. |
    | Read (MVM during Similarity Calculation) |  ~ 2.87 nJ / 256 bits | ~ 2.87 nJ per iteration | nJ | Low | Supplementary Note 4 | Explicit |  Energy per iteration for similarity calculation is explicitly provided, assuming ~256 bit read per iteration based on D=256 vector dimension. |
     | Read (MVM during Projection) | ~ 1.94 nJ / 256 bits | ~ 1.94 nJ per iteration | nJ | Low | Supplementary Note 4 | Explicit | Energy per iteration for projection is explicitly provided, assuming ~256 bit read per iteration based on D=256 vector dimension. |
*   Implicit/Explicit: Mixed
    *   Justification: Energy consumption for read operations (MVM) is explicitly given in Supplementary Note 4. Energy cost for programming/writing is not explicitly provided, hence marked as N/A. Calculation of "per bit" energy is implicit, derived by dividing total energy per iteration by the vector dimension (assumed to be related to bits read).

### **3.8 Memory Fidelity & Robustness Metrics (Optional - if applicable)**
* **Vector ID:** M3.8
* **Vector Type:** Table
*   Table:
    | Metric ID | Description | Value | Units | CT-GIN Mapping | Data Source | Implicit/Explicit | Justification |
    | :-------- | :---------- | :----: | :---: | :-------------: | :----------: |:-----------------:| :-----------------:|
    | Factorization Accuracy | Percentage of correctly factorized product vectors | 99.71 | % | Attribute of `BehaviorArchetypeNode (Factorization)` & `ReliabilityNode` | II, Large-Scale Experimental Demonstration | Explicit | Achieved accuracy with in-memory factorizer experimentally. |
    | Accuracy with Digital Design (Reference) | Accuracy of digital design without stochasticity | 95.76 | % |  Attribute of `ReliabilityNode (Digital Reference Implementation)` | III, Discussion | Explicit | Accuracy achieved by deterministic digital design. |
    | Accuracy with Zero Noise Simulation | Accuracy of in-memory factorizer simulation with no noise | 25.4 | % | Attribute of `ReliabilityNode (Simulation, Zero Noise)` | Supplementary Note 3, ExtendedDataFig.1 | Explicit | Accuracy reported in simulation with zero noise. |

*   Implicit/Explicit: Explicit
*   Justification: All metrics in the table are explicitly stated within the paper, either in the main text or supplementary materials, comparing the performance of the in-memory factorizer with baseline designs or simulations under different conditions.

---

## M4: Self-Organization and Emergent Order
*   **Vector ID:** M4
*   **Vector Type:** Self-Organization

### **4.1 Self-Organization Presence:**

*   **Vector ID:** M4.1
*   **Vector Type:** Binary
    *   Content: [No]
    *   Justification: The system does not exhibit self-organization in the sense of spontaneous emergence of global order or patterns from local interactions without external control defining the global structure. The architecture and the codebooks are pre-designed and programmed.  The system operates on a pre-defined task (vector factorization) within a structured framework of crossbar arrays and algorithms. While stochasticity is exploited, it's a property of the devices used (PCM), not a mechanism for self-organization of the system's structure or behavior. The overall factorization process is directed by a pre-programmed algorithm; the stochastic element is incorporated into the algorithm's steps, rather than leading to emergent order.
    *   Implicit/Explicit: Implicit
        *  Justification: The paper structure and descriptions focus on engineered components and algorithmic control. The absence of discussion or evidence for spontaneous structural or behavioral emergence through local interactions strongly implies lack of self-organization in this context.

**(Conditional: If M4.1 is "No", skip to Module 5. If "Yes", include M4.2-M4.7)**

## M5: Computation
*   **Vector ID:** M5
*   **Vector Type:** Computation

### **5.1 Embodied Computation Presence:**

*   **Vector ID:** M5.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: Matrix-vector multiplication (MVM), a core computational operation, is physically embodied within the memristive crossbar arrays. The computation arises from the physical laws governing electrical conduction in the crossbar structure (Ohm's law, Kirchhoff's current law). The resistive elements (PCM devices) and their interconnections inherently perform the MVM operation as voltage pulses propagate through the array and currents sum at the bitlines. This is computation intrinsic to the material structure and operation, not solely by an external controller. The in-memory nature means computation happens where data (codebooks) is stored, further embodying computation within the memory substrate itself.
    *    Implicit/Explicit: Explicit
        *  Justification:  The paper explicitly highlights "in-memory computing (IMC)" and states "The proposed in-memory factorizer stores the codevectors on crossbar arrays of memristive devices performing analog in-memory MVM operations." and "These operations can be executed in-memory in a crossbar array of memristive devices by exploiting the Ohm’s law and Kirchhoff’s current summations law." This directly confirms the presence of embodied computation.

### **5.2 Computation Type:**

*   **Vector ID:** M5.2
*   **Vector Type:** Classification
    *   Content: [Analog]
    *   CT-GIN Mapping: Defines the `ComputationNode` type: `computationType: Analog`
    *    Implicit/Explicit: Explicit
    *    Justification: The paper emphasizes “analog in-memory computing” and “analog MVM operations”. The computation in the crossbar relies on analog conductance values of PCM devices and summation of analog currents.  The output of the MVM is described as "analog in-memory MVM results".  The stochasticity is also an analog property of the PCM devices.

### **5.3 Computational Primitive:**

*   **Vector ID:** M5.3
*   **Vector Type:** Function
    *   Content: Matrix Multiplication (specifically Matrix-Vector Multiplication - MVM). The MVM operation is performed in analog in-memory. For similarity calculation, it is  αf(t)=x˜f(t)·Xf and for projection, it is xˆf(t+1)=sign(αf(t)·(Xf)T).  Mathematically, MVM computes the dot product of the input vector with each row of the matrix (codebook), resulting in an output vector of similarities or projections.
    *   **Sub-Type (if applicable):** Matrix Multiplication: Matrix-Vector Multiplication
    *   CT-GIN Mapping: Defines the primary function of the `ComputationNode`: `computationalPrimitive: Matrix Multiplication`, `subType: Matrix-Vector Multiplication`
    *   Implicit/Explicit: Explicit
    * Justification: The paper repeatedly states that "matrix-vectormultiply(MVM)operations" are the dominant operations and are performed "in-memory".  Equations (S4) and (S5) in Supplementary Note 1 explicitly represent the similarity search and projection as MVM operations.

### **5.4 Embodied Computational Units**
* **Vector ID:** M5.4
* **Vector Type:** Table
*   Table:
| Unit ID | Description | Processing Power | Energy/Operation | Freq/Resp. Time | Bit-Depth | Data Source | Implicit/Explicit | Justification |
| :------ | :---------- | :--------------- | :--------------- | :--------------: | :-------: | :----------: |:-----------------:| :-----------------:|
| IMC Core Unit Cell | Single PCM unit cell in crossbar array | N/A (Analog Computation) | Very low (part of total MVM energy) | ~10 ns (MVM operation time) | Analog (conductance levels) | Fig 4a, Supplementary Note 4 | Explicit | Unit cell is the fundamental computing element. Speed from Supplementary Note Table S3 (Time per iteration for Similarity calculation). Bit-depth refers to analog nature, not digital bits. |
| IMC Core (256x256 array) | 256x256 crossbar array | ~52.4 TOPS (Similarity Calc) ~13.1 TOPS (Projection) | ~2.87 nJ (Similarity Calc) ~1.94 nJ (Projection) | ~10 ns (Similarity Calc) ~40 ns (Projection) | Analog output (digitized by 8 or 1 bit ADC) | Table S3, Supplementary Note 4 | Explicit | Core enables parallel MVM. TOPS and Energy from Supplementary Note Table S3. Response Time from Supplementary Note Table S3 (Time per iteration) |

## M6: Temporal Dynamics
*   **Vector ID:** M6
*   **Vector Type:** Temporal

### **6.1 Timescales:**

*   **Vector ID:** M6.1
*   **Vector Type:** ParameterTable
    *   Table:
        | Timescale Description | Value | Units | Source | Implicit/Explicit | Justification |
        | :-------------------- | :---: | :---: | :----: | :----------------: | :------------: |
        | MVM Operation Time (Similarity Calc) | 10 | ns | Table S3 | Explicit | Time per iteration for Similarity calculation from Supplementary Table S3 |
        | MVM Operation Time (Projection) | 40 | ns | Table S3 | Explicit | Time per iteration for Projection from Supplementary Table S3 |
        | Iteration Time (Total incl. Digital) | 350 | ns | Table S3 | Explicit | Time per iteration (total) from Supplementary Table S3 |
        | Convergence Time (Average) | 3312 iterations * 350 ns/iteration | ~ 1.16 ms |  II, Large-Scale Experimental Demonstration & M6.1 (Iteration Time) | Mixed | Average number of iterations is explicit. Iteration time is explicit. Convergence time is derived by multiplication. |
        | PCM Conductance Drift Time | Long-term | Qualitative | II, Large-Scale Experimental Demonstration | Explicit |  Mention of broadening conductance distribution "with time" due to structural relaxation. |

### **6.2 Active Inference:**

*   **Vector ID:** M6.2
*   **Vector Type:** Assessment
    *   Content: [No]
    *   Justification: The system does not exhibit active inference. It performs iterative factorization based on a fixed algorithm. There’s no evidence of prediction of future states, action selection to minimize discrepancies based on an internal model, or updating internal models by experience. The system reacts to input product vectors but does not actively explore or model its environment in a way that would qualify as active inference. The iterations are a search process within a defined codebook space, not an active attempt to minimize surprise or prediction error based on an internal world model.
    *   Implicit/Explicit: Implicit
        *  Justification: The paper describes a factorization algorithm with iterative refinement. The absence of any descriptions or mechanisms related to prediction, model-based action selection, or model updating strongly implies lack of active inference.
    *   **If Yes/Partial, provide examples of testable CT-GIN metrics that *could* be used to quantify active inference:** [N/A]

## M7: Adaptation
*   **Vector ID:** M7
*   **Vector Type:** Adaptation

### **7.1 Adaptive Plasticity Presence:**

*   **Vector ID:** M7.1
*   **Vector Type:** Binary
    *   Content: [No]
    *   Justification: The system does not exhibit adaptive plasticity. The codebooks (memory) are programmed once and remain fixed during operation. There is no mechanism described for the system to change its internal structure or behavior in response to experience to improve performance over time or alter its functionality. The hyperparameters (activation and convergence thresholds) are optimized using Bayesian optimization *before* deployment, but are fixed during operation and are not adaptively adjusted based on ongoing interactions or performance feedback during runtime.  The stochasticity is a fixed device property, not an adaptive mechanism.
    *    Implicit/Explicit: Implicit
        * Justification: The paper details a fixed factorization algorithm with pre-programmed codebooks. The lack of any description or mechanism for runtime modifications of codebooks, algorithm, or hyperparameters based on experience, implies absence of adaptive plasticity.

**(Conditional: If M7.1 is "No", skip to Module 8. If "Yes", include M7.2)**

## M8: Emergent Behaviors
*   **Vector ID:** M8
*   **Vector Type:** Behavior

### **8.1 Behavior Description:**

*   **Vector ID:** M8.1
*   **Vector Type:** Description
    *   Content: The main functional behavior is **holographic vector factorization** or **attribute disentanglement**. Given a product vector representing combined attributes, the system iteratively searches and outputs estimates of the constituent attribute vectors.  Observable behavior is the system receiving an input product vector and, after a number of iterations, outputting a set of factor vectors which, when recombined (bound), closely approximate the input product vector.  This is demonstrated experimentally with synthetic vectors and visual perceptual representations from the RAVEN dataset. The system reliably and efficiently factorizes vectors spanning a large search space.
    *   CT-GIN Mapping: Defines the `BehaviorArchetypeNode`. Specify the type of behavior: `behaviorType: Holographic Vector Factorization, Attribute Disentanglement`
    *    Implicit/Explicit: Explicit
       *  Justification:  The paper title and main objective are explicitly about "factorization of holographic perceptual representations". The experimental demonstrations and results clearly validate this behavior.

### **8.2 Behavior Robustness:**

*   **Vector ID:** M8.2
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The system demonstrates robustness to device stochasticity, which is actually exploited for improved performance.  It shows reliable factorization even with the inherent variability in PCM devices and noise.  The experimental results show high accuracy (99.71% and 99.42% for synthetic and visual data respectively) and successful factorization in the hardware implementation. Robustness to variations in device characteristics is implicitly suggested by the successful operation across multiple devices in the 256x256 array, and the noise tolerance simulations shown in ExtendedDataFig.1. However, robustness to large-scale component failures or significant parameter variations beyond the characterized noise levels is not explicitly evaluated or quantified, so it is not rated as extremely robust (score 10).
    *   Implicit/Explicit: Mixed
        *  Justification: Robustness to stochasticity is explicitly highlighted as a feature. The experimental accuracy scores imply a degree of robustness in the hardware implementation.  The noise tolerance simulations further support this. However, the overall robustness score is a mixed assessment, acknowledging the explicit evidence of stochasticity tolerance but noting the lack of quantification for robustness against other types of perturbations and failures.
    *   CT-GIN Mapping: e.g., This score contributes to the reliability attributes of the `BehaviorArchetypeNode`: `robustnessScore: 7`

### **8.3 CT-GIN Emergent Behavior Validation**

*    **Vector ID:** M8.3
*    **Vector Type:** Validation
     *  Content: Validation methods include:
         * **Operational definition:** Factorization accuracy (percentage of correctly factorized vectors) is the primary operational definition of successful behavior.
         * **Experimental demonstration:**  Large-scale experiments using two IMC cores with PCM devices validate the factorizer's functionality in hardware (Fig. 4, Section II).
         * **Comparison to Baseline:** Performance is compared against a baseline resonator network and a digital design, demonstrating improved accuracy and operational capacity of the in-memory factorizer.
         * **Accuracy Metrics:**  Quantifiable accuracy metrics (percentage accuracy, average iterations to convergence) are used to evaluate performance.
         * **RAVEN dataset application:** Application to visual attribute disentanglement using the RAVEN dataset (Fig. 4d, Section II) demonstrates efficacy in a perception-related task.
         * **Simulations:** Simulations are used to analyze the impact of stochasticity and compare different activation functions (Section I, Methods, Supplementary Notes).
         * **Bayesian Optimization:** Bayesian optimization is used to optimize hyperparameters, ensuring robust performance.
         * **Reproducibility:** Code and data availability (github & zenodo links) enhance reproducibility.
         Limitations: Detailed robustness testing beyond noise and device variability is limited. Validation primarily focuses on accuracy and efficiency metrics for vector factorization.
     *   Implicit/Explicit: Mixed
    *   Justification: The validation methods are described throughout the paper, particularly in Sections I, II, Methods, and Supplementary Notes.  Accuracy metrics, experimental demonstrations, simulations, and comparisons are explicitly presented.  The limitations and implicit aspects arise from the scope of validation, where certain types of robustness testing are not explicitly detailed.

## M9: Cognitive Proximity
*   **Vector ID:** M9
*   **Vector Type:** Cognition

### **9.1 Cognitive Mapping:**

*   **Vector ID:** M9.1
*   **Vector Type:** Description
    *   Content: The paper explicitly maps the system's functionality to "sensory perception and cognition," specifically addressing "disentanglement of constituent attributes of a sensory signal" as a "critical task for future artificial intelligence systems" and "one of the fundamental problems in sensory perception is unbinding—the separation of causes of a raw sensory signal".  It draws an analogy to visual perception, where pixel intensities result from combined physical attributes (reflectance, shading). The factorization of holographic vectors is presented as a mathematical approach to model this unbinding process in perception and cognition. The use of "brain-inspired hyperdimensional computing" and "resonator networks" further reinforces the cognitive analogy. The application to visual attribute disentanglement using the RAVEN dataset directly connects the system's operation to a visual reasoning task relevant to cognitive science.
    *   CT-GIN Mapping: If a mapping exists, this defines a `CognitiveMappingEdge`. Specify source and target: `CognitiveMappingEdge`: attributes: {`source: BehaviorArchetypeNode (Holographic Vector Factorization)`, `target: CognitiveFunctionNode (Sensory Perception, Attribute Disentanglement)`}, `analogy: Unbinding of sensory attributes in perception`
    *   Implicit/Explicit: Explicit
    * Justification: The cognitive mapping is explicitly stated in the Introduction, linking the factorization task to sensory perception and cognition, and referencing "brain-inspired" approaches.

### **9.2 Cognitive Proximity Score:**

*   **Vector ID:** M9.2
*   **Vector Type:** Score
    *   Score: [3]
    *   Justification:  The system achieves **Level 3: Reactive/Adaptive Autonomy** on the CT-GIN Cognizance Scale. It adapts its iterative search based on the input product vector and feedback within the resonator network, allowing it to solve factorization problems autonomously without external control during operation. It goes beyond simple stimulus-response by performing an iterative search and incorporating stochasticity and sparse activations to improve convergence and accuracy. However, the behavioral repertoire is limited to vector factorization. It lacks goal-directed behavior beyond solving the factorization task, model-based reasoning, contextual understanding, abstract thought, or social cognition (higher levels on the scale). The “adaptation” is algorithmic iteration, not system-level plasticity or learning from experience beyond a single input vector instance. It does not reach levels of goal-directed or model-based cognition (Levels 4+).
    *   Implicit/Explicit: Mixed
    *  Justification: The score and justification are based on a mixed assessment. The system's autonomous operation and iterative nature support a rating beyond simple responsivity (Level 1). The explicit analogy to perception and "brain-inspired" approach might suggest higher cognitive proximity at first glance. However, critical analysis of the actual demonstrated functionality reveals limitations to a specific computational task (vector factorization) without evidence of more complex cognitive functions, thus placing it at Level 3.

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
    | Sensing/Perception               | 2          | Input is pre-processed (e.g., from CNN), system doesn't directly sense environment. Vector input represents perceptual representation. | `CognitiveFunctionNode: Sensing/Perception` | Implicit | System operates on pre-processed input vectors, implying a prior sensing/perception stage, but not embodied within the material itself regarding direct environmental sensing. |
    | Memory (Short-Term/Working)        | 4          | Iteration states are a form of short-term working memory to guide search within an iteration sequence. | `CognitiveFunctionNode: Memory (Short-Term/Working)` | Implicit |  Iterative process necessitates maintaining intermediate states which functions as a transient form of working memory during the factorization process. |
    | Memory (Long-Term)                 | 7          | Non-volatile PCM codebook storage represents long-term memory of attributes.             | `CognitiveFunctionNode: Memory (Long-Term)` | Explicit | Non-volatile PCM memory is explicitly described for storing codebooks. |
    | Learning/Adaptation              | 2          | Hyperparameters are optimized *offline*. No online learning or adaptation *during* operation. | `CognitiveFunctionNode: Learning/Adaptation` | Implicit |  Absence of online learning mechanisms points to low score for learning/adaptation at runtime. |
    | Decision-Making/Planning          | 3          | Iterative search involves making decisions at each step (projection, activation), but within a predefined algorithmic search space, no explicit planning in terms of broader goals. | `CognitiveFunctionNode: Decision-Making/Planning` | Implicit | Iterative nature represents steps that resemble decision making within the predefined factorization process, but not in a broader context of planning or goal-directed actions. |
    | Communication/Social Interaction | 0          | System operates in isolation, no communication or social interaction.                 | N/A                              | Explicit | System description does not include any communication or social interaction aspects. |
    | Goal-Directed Behavior            | 3          | Goal is predefined (factorize input vector), but no higher-level goals or flexibility in goal selection or re-planning. | `CognitiveFunctionNode: Goal-Directed Behavior` | Implicit | Factorization goal is implicit in the system design, but limited in scope compared to broader intelligent goal-directedness. |
    | Model-Based Reasoning              | 1          | Codebooks are a basic form of model representing attributes, very rudimentary, not flexible or complex models. | `CognitiveFunctionNode: Model-Based Reasoning` | Implicit | Codebooks serve as a model for attribute representation, but it is simple and fixed compared to rich model-based reasoning in cognition. |
    | **Overall score**                 |      [3.0]       | Average of individual function scores.                                                  |                                   |                     |                |

    *   **Note:** Assess the system for *each* function, providing a score (0-10) and a short (1-2 sentences) justification.  0 = Absent, 10 = Human-level performance.

## M10: Criticality Assessment
*   **Vector ID:** M10
*   **Vector Type:** Criticality

### **10.1 Criticality:**

*   **Vector ID:** M10.1
*   **Vector Type:** Assessment
    *   Content: [No]
    *   Justification: The paper does not provide evidence or discussion suggesting the system operates near a critical point, displays scale-free behavior, power laws, or long-range correlations. The system's behavior is primarily determined by the engineered algorithm and device properties, rather than emergent phenomena associated with criticality. Stochasticity is exploited but is more of a noise source intentionally used for computational benefit rather than indicative of criticality.  No analysis of system dynamics in terms of phase transitions, order parameters, or criticality is presented.
        *   Critical Parameters (If Yes/Partial): [N/A]
        *   Evidence: [N/A]
    *   Implicit/Explicit: Implicit
    *    Justification: The absence of any mention or analysis related to criticality, scale-free behavior, or power laws in the paper strongly implies that the system is not designed or characterized in the context of criticality.

## M11: Review Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Review")**
N/A

## M12: Theoretical Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Theoretical")**
N/A

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
| Energy Flow Efficiency          | Yes                       | 12.2x energy saving vs. digital, 33.1 µJ per query | Absolute energy efficiency vs. theoretical limits not quantified.                | Further optimize analog circuit design, reduce peripheral circuit energy use.      |
| Memory Fidelity                 | Partial                   | 99.71% factorization accuracy       | Readout accuracy and degradation rate quantitatively less defined.              | Quantify memory fidelity metrics (retention, endurance, disturb) more precisely. |
| Organizational Complexity       | No                        | Pre-designed crossbar array         | No self-organization, fixed architecture.                                         | Explore self-organizing architectures for codebook generation or network structure. |
| Embodied Computation            | Yes                       | MVM in memristive crossbar         | Limited computational primitives beyond MVM in embodied units.                | Embodiment of more diverse computational primitives within material.         |
| Temporal Integration            | Yes                       | Iterative factorization process, ~1.16 ms average convergence time |  Active inference and long-term adaptation timescales not present.             | Incorporate mechanisms for active inference and adaptation over longer timescales. |
| Adaptive Plasticity             | No                        | Hyperparameters fixed post-optimization| No online learning or adaptation within the system.                            | Implement online learning and adaptive plasticity mechanisms.                  |
| Functional Universality         | No                        | Specific task: holographic vector factorization |  Limited to factorization, no demonstration of broader functional universality. | Explore adaptability to different computational tasks.                         |
| Cognitive Proximity            | Partial                   | Level 3: Reactive/Adaptive Autonomy | Falls short of goal-directed, model-based, or higher-level cognition (Level 4+). |  Integrate model-based reasoning and goal-directedness.                          |
| Design Scalability & Robustness | Yes                       | 256x256 crossbar, robust to stochasticity, 99.71% accuracy | Scalability to larger arrays, robustness to component failures less explored.|  Investigate scalability to larger arrays and robustness to various failures.    |
| **Overall CT-GIN Readiness Score** |        |   5.33 |   |      |


### **13.2 Qualitative CT-GIN Assessment Conclusion:**

*   **Vector ID:** M13.2
*   **Vector Type:** Textual Summary
    *   Content: The in-memory factorizer demonstrates key strengths in energy efficiency and embodied computation, achieving significant energy savings compared to digital approaches and successfully implementing matrix-vector multiplication within memristive crossbar arrays. The system shows partial readiness in memory fidelity, achieving high factorization accuracy but with memory characteristics influenced by device stochasticity and degradation. Organizational complexity and adaptive plasticity are not present, as the system has a pre-designed architecture and fixed codebooks without online learning. Temporal integration is limited to the iterative factorization process.  Cognitive proximity is at Level 3 (Reactive/Adaptive Autonomy), showing iterative search but lacking higher-level cognitive functions. Overall, the system is a significant advancement in energy-efficient, neuromorphic computing for specific tasks like vector factorization, but has limitations in organizational complexity, adaptive plasticity, and cognitive breadth within the CT-GIN framework. Future potential lies in enhancing memory fidelity, incorporating online learning, and exploring self-organizing architectures to move closer to more complex facets of material intelligence and potentially higher CT-GIN readiness levels.

### **13.3 CT-GIN Refinement Directions:**

*   **Vector ID:** M13.3
*   **Vector Type:** Recommendations
    *   Content:
        *   Enhance memory fidelity and robustness: Investigate methods to mitigate PCM device variability and drift to improve memory readout accuracy and retention. Explore error correction schemes or device-level optimizations.
        *   Incorporate online learning and adaptive plasticity: Implement mechanisms for the system to adapt its codebooks or algorithm parameters based on task performance or environmental changes. Explore on-chip learning rules compatible with memristive devices.
        *   Explore self-organizing architectures: Investigate approaches to generate or refine codebooks or network structures through self-organization processes rather than fixed pre-programming. Explore local interaction rules for emergent organization.
        *   Expand computational primitives of embodied units: Go beyond MVM to embody a wider range of computational primitives within memristive or other material substrates to broaden the functional capabilities of the material-based compute engine.
        *   Investigate scalability to larger systems and complex tasks:  Scale up the system to larger crossbar arrays and address more complex cognitive tasks beyond vector factorization to assess the scalability and functional versatility of the approach.
        *   Explore mechanisms for active inference and goal-directed behavior:  Incorporate feedback loops and control mechanisms that enable the system to predict future states, select actions based on internal models, and exhibit goal-directed behavior beyond the current reactive factorization task.

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
        | M2.2 | M5.4 | Coupling |
        | M5.4 | M8.1 | Adjunction |
        | M9.1 | M8.1 | Cognitive Mapping |
        | M3.1 | M5.4 | Adjunction |
        | M5.4 | M6.1 | Temporal Evolution |
        | M8.1 | M9.2 | Cognitive Mapping |

## M16: CT-GIN Template Self-Improvement Insights

*   **Vector ID:** M16
*   **Vector Type:** Feedback

### **Template Feedback:**

*    **Vector ID:** M16.1
*   **Vector Type:** Text
Provide specific, actionable feedback on the *CT-GIN template itself*, based on this analysis:
    *   **Missing Probes:** The template is quite comprehensive. Perhaps adding a probe in the "Computation" module to specifically assess the *programmability* or *reconfigurability* of the embodied computational units could be useful.
    *   **Unclear Definitions:** The definition of "Self-Organization" could be slightly clarified to explicitly differentiate between *designed order* in self-assembling systems and *emergent order* from purely local interactions without global design constraints.
    *   **Unclear Node/Edge Representations:** The guidance for mapping to GIN nodes/edges was sufficient for this paper.
    *   **Scoring Difficulties:**  Assigning cognitive proximity scores (M9.2 and M9.3) remains somewhat subjective. Providing more granular descriptions for each level of the Cognizance Scale, perhaps with more concrete examples related to material systems, could reduce subjectivity. For M9.3 Checklist, perhaps a more direct link to the Cognizance Scale level for each function could help.
    *   **Data Extraction/Output Mapping:** Data extraction and mapping to the template was generally straightforward. The structured format of the template is helpful.
    *   **Overall Usability:** The template is generally usable and well-structured. The modular approach is effective for breaking down the analysis.
    * **Specific Suggestions:**
        *   Add a probe M5.5 in "Computation": "Programmability/Reconfigurability of Computational Units" (Score and Justification).
        *   Refine the definition of "Self-Organization" in M4.1 to further clarify the distinction between designed and emergent order in material systems context.
        *   Expand the descriptions for each level of the CT-GIN Cognizance Scale (M9.2) with examples more specific to material intelligence implementations.
        *   In M9.3 Checklist, consider adding a column to explicitly link each cognitive function score back to the overall Cognizance Scale level justification.