# In-Situ Sensing and Dynamics Predictions for Electrothermally-Actuated Soft Robot Limbs

__Paper Type:__ Experimental

## M1: System Overview & Implementation
*   **Vector ID:** M1
*   **Vector Type:** Overview

### **1.1 System Description**

*   **Vector ID:** M1.1
*   **Vector Type:** Description
    *   Content: The system is a planar soft robot limb actuated by a pair of Shape Memory Alloy (SMA) coils. It incorporates in-situ temperature sensors attached to each SMA coil and a dielectric elastomer bend sensor to measure angular deflection. The purpose is to enable dynamics prediction of the soft robot limb's motion using data from these embedded sensors. An LSTM neural network is trained to model the relationship between Pulse-Width Modulation (PWM) control inputs, temperature sensor readings, and limb deflection. The system aims to achieve accurate, long-term (10 minutes) open-loop prediction of the limb's motion, contributing to the development of compact, untethered electrothermally-actuated soft robots with embedded sensing. The components include SMA coil actuators, type K thermocouples for temperature sensing, a capacitive bend sensor, a silicone rubber body, and an LSTM neural network model for dynamics prediction.
    *   CT-GIN Mapping: `SystemNode` attributes: `systemType`="Soft Robot Limb", `domain`="Robotics", `mechanism`="Electrothermal Actuation, Machine Learning-based Dynamics Modeling", `components`="SMA Coils, Thermocouple Sensors, Bend Sensor, LSTM Neural Network, Silicone Body", `purpose`="In-situ Sensing and Dynamics Prediction for Soft Robot Motion", `actuationType`="Electrothermal", `sensingType`="Temperature, Deflection"
    *   Implicit/Explicit: Mixed
        *  Justification: The system description combines explicit statements from the abstract and introduction regarding components and purpose with implicit understanding of electrothermal actuation mechanisms and machine learning roles within the system.

### **1.2 Implementation Clarity**

*   **Vector ID:** M1.2
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The hardware implementation is described with reasonable clarity, including sensor fabrication and integration details as shown in Figure 3. The neural network architecture (LSTM) is mentioned, and data collection and training procedures are outlined in Section 2. However, specific hyperparameters of the LSTM and detailed circuit diagrams are not provided, which slightly reduces clarity. The overall experimental setup is well described, but some finer details are left implicit.
    *   Implicit/Explicit: Mixed
        * Justification: The clarity is derived from both explicit descriptions of hardware and methods and implicit assumptions about standard neural network implementations and engineering practices.

### **1.3 Key Parameters**

*   **Vector ID:** M1.3
*   **Vector Type:** ParameterTable
    *   Table:
        | Parameter Name | Value | Units | Source (Fig/Table/Section) | Implicit/Explicit | Data Reliability (High/Medium/Low) | Derivation Method (if Implicit) |
        | :------------- | :---: | :---: | :-----------------------: | :-----------------: | :-----------------------------: | :-------------------------------: |
        | SMA Wire Diameter | 0.020 | inches | Section 2.1.1 | Explicit | High | Manufacturer specification |
        | PWM Voltage | 7 | V | Section 2.1.2 | Explicit | High | Set voltage from benchtop supply |
        | LSTM Layer Nodes | 300 | - | Section 2.3.1 | Explicit | High | Defined network architecture parameter |
        | Fully-Connected Layer Nodes | 300 | - | Section 2.3.1 | Explicit | High | Defined network architecture parameter |
        | Adam Optimizer Learning Rate | 1e-3 | - | Section 2.4 | Explicit | High | Set training hyperparameter |

    *   **Note:** N/A

## M2: Energy Flow
*   **Vector ID:** M2
*   **Vector Type:** Energy

### **2.1 Energy Input**

*   **Vector ID:** M2.1
*   **Vector Type:** Input
    *   Content: The primary energy source is electrical power supplied by a benchtop power supply.
    *   Value: 7
    *   Units: V (nominal voltage)
    *   CT-GIN Mapping: `EnergyInputNode`: attributes - `source`="Benchtop Power Supply", `type`="Electrical"
    *   Implicit/Explicit: Explicit
        *  Justification: The energy source and voltage are explicitly mentioned in Section 2.1.2.

### **2.2 Energy Transduction**

*   **Vector ID:** M2.2
*   **Vector Type:** Transduction
    *   Content: Electrical energy from the power supply is converted into thermal energy via Joule heating in the SMA coils when electrical current is applied. This thermal energy causes a phase transformation in the SMA, leading to mechanical strain and contraction of the coils. The mechanical energy of the SMA contraction is then transduced into kinetic energy, resulting in the angular deflection of the soft robot limb. The flow is Electrical Energy -> Joule Heating (Thermal Energy) -> SMA Actuation (Mechanical Energy) -> Limb Deflection (Kinetic Energy).
    *   CT-GIN Mapping: `EnergyTransductionEdge`: attributes - `mechanism`="Joule Heating", `from_node`="Electrical Energy", `to_node`="Thermal Energy (SMA Coils)"; `EnergyTransductionEdge`: attributes - `mechanism`="SMA Phase Transformation & Contraction", `from_node`="Thermal Energy (SMA Coils)", `to_node`="Mechanical Energy (SMA Actuation)"; `EnergyTransductionEdge`: attributes - `mechanism`="Mechanical Deformation of Soft Limb", `from_node`="Mechanical Energy (SMA Actuation)", `to_node`="Kinetic Energy (Limb Deflection)"
    *   Implicit/Explicit: Mixed
        *  Justification: The primary transduction mechanisms are inferred from the description of electrothermal actuation and SMA properties alongside explicit mention of Joule heating. The paper does not explicitly detail each step as energy transduction but it’s implied by the system's operation.

### **2.3 Energy Efficiency**

*   **Vector ID:** M2.3
*   **Vector Type:** Score
    *   Score: [3]
    *   Justification/Metrics: Electrothermal actuation using SMAs is inherently inefficient. A significant portion of the electrical energy is lost as heat to the environment due to thermal dissipation and the complex hysteresis behavior of SMA materials. The paper does not provide any quantitative metrics for energy efficiency, suggesting efficiency is not a primary focus and is likely low in this electrothermal system. Qualitative Assessment: Low.
    *   CT-GIN Mapping: Attribute `efficiencyScore` = 3 on `EnergyTransductionEdge` with `mechanism`="Joule Heating" and `EnergyTransductionEdge` with `mechanism`="SMA Phase Transformation & Contraction"
    *   Implicit/Explicit: Implicit
      *  Justification: The low efficiency score is an inference based on general knowledge about SMA actuators and electrothermal actuation principles, not explicitly stated in the paper.

### **2.4 Energy Dissipation**

*   **Vector ID:** M2.4
*   **Vector Type:** Dissipation
    *   Content: Energy dissipation mechanisms include heat loss to the surrounding environment from the SMA coils and silicone body, electrical resistance in the SMA wires leading to further heat generation without contributing directly to mechanical work, and hysteresis losses within the SMA material during thermal cycling. The paper does not provide quantitative values for energy dissipation.  Qualitative Assessment: Heat loss is likely a significant dissipation mechanism due to the nature of electrothermal actuation and the embodiment in silicone.
    *   CT-GIN Mapping: `EnergyDissipationNode`: attributes - `type`="Heat Loss to Environment", `source`="SMA Coils, Silicone Body"; `EnergyDissipationNode`: attributes - `type`="Electrical Resistance Loss", `source`="SMA Wires"; `EnergyDissipationNode`: attributes - `type`="Hysteresis Loss", `source`="SMA Material"; `EnergyDissipationEdge`: attributes - `mechanism`="Thermal Conduction, Convection, Radiation", `from_node`="Thermal Energy (SMA Coils)", `to_node`="EnergyDissipationNode: Heat Loss to Environment"; `EnergyDissipationEdge`: attributes - `mechanism`="Electrical Resistivity", `from_node`="Electrical Energy", `to_node`="EnergyDissipationNode: Electrical Resistance Loss"; `EnergyDissipationEdge`: attributes - `mechanism`="Material Hysteresis", `from_node`="Mechanical Energy (SMA Actuation)", `to_node`="EnergyDissipationNode: Hysteresis Loss"
    *    Implicit/Explicit: Implicit
        *  Justification: Identification of dissipation mechanisms is inferred from the physics of electrothermal systems and SMA operation. The paper does not explicitly quantify these losses, making the assessment qualitative and implicit.

## M3: Memory
*   **Vector ID:** M3
*   **Vector Type:** Memory

### **3.1 Memory Presence:**

*   **Vector ID:** M3.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: The Long Short-Term Memory (LSTM) neural network architecture is explicitly used to model the dynamics and predict the bending angle of the soft robot limb. The LSTM network retains information about past inputs and states through its internal cell state and learned weights, which persist beyond the immediate stimulus and influence future predictions of limb deflection. This constitutes memory as it directly affects the system’s future behavior.
    *    Implicit/Explicit: Explicit
        * Justification: The presence of memory is explicit because the paper directly states the use of LSTM, a memory-capable neural network, to model and predict system dynamics.

### **3.2 Memory Type:**

*   **Vector ID:** M3.2
*   **Vector Type:** Score
*   Score: [7]
*   Justification: The memory can be classified as a temporal or sequence memory, implemented through the LSTM network. It is analog in nature, storing continuous-valued information in its weights and cell states. The retention is demonstrated over a 10-minute prediction horizon. The capacity is related to the network size (300 nodes per layer) and the amount of training data. Read-out accuracy is reflected in the RMSE of the deflection predictions. While not perfect memory (score 10), it exhibits significant capability for retaining and utilizing temporal information for prediction within the system's operational context.
*   CT-GIN Mapping: `MemoryNode` type = "LSTM Neural Network", `memoryType` = "Temporal", `representation` = "Analog", `retentionMechanism` = "Network Weights & Cell States"
*    Implicit/Explicit: Mixed
    * Justification: The memory type (LSTM) is explicitly stated. The score and detailed justification are based on an interpretation of LSTM capabilities and performance within the described application, inferred from the paper's results and general understanding of LSTM networks.

### **3.3 Memory Retention Time:**

*   **Vector ID:** M3.3
*   **Vector Type:** Parameter
*   Value: 10
*    Units: minutes
*   Justification: The paper demonstrates successful open-loop rollout predictions over timescales of "10 minutes or more" with "no significant drift," indicating that the LSTM network effectively retains and uses relevant information for prediction over at least this duration.
*    Implicit/Explicit: Explicit
        * Justification: The 10-minute retention time is explicitly stated in the abstract and results sections regarding long-term prediction capabilities.
*   CT-GIN Mapping: Key attribute of the `MemoryNode`: `retentionTime` = 10 minutes

### **3.4 Memory Capacity (Optional - if applicable)**

* **Vector ID:** M3.4
* **Vector Type:** Parameter
*  Value: N/A
*   Units: N/A
*   Justification: The paper does not explicitly quantify memory capacity in terms of discrete states or information content (e.g., bits). Memory capacity is implicitly determined by the number of LSTM units and the complexity of learned dynamics, but this is not numerically assessed in the paper.
*    Implicit/Explicit: Implicit
        *  Justification: Memory capacity is not directly addressed. Its relevance and quantification are inferred from general knowledge about LSTM networks, but lacking explicit data in the paper.
*   CT-GIN Mapping: Key attribute of the `MemoryNode`: `capacity` = "N/A (Qualitatively related to network size and training data)"

### **3.5 Readout Accuracy (Optional - if applicable)**

* **Vector ID:** M3.5
* **Vector Type:** Parameter
*   Value: 5.350
*   Units: degrees (RMSE for Test 4 open-loop rollout)
*   Justification: The readout accuracy, representing the model's ability to recall and utilize the learned dynamics memory for prediction, is quantified by the Root Mean Squared Error (RMSE) of the open-loop rollout simulations. For Test 4 (bidirectional bending with temperature feedback), the RMSE is reported as 5.350 degrees, representing the typical error in the predicted deflection angle using the LSTM memory.
*    Implicit/Explicit: Explicit
       *  Justification: The RMSE value for readout accuracy is explicitly stated in the Results section (Fig. 7, Table 1) as a metric for model performance.
*   CT-GIN Mapping: Key attribute of `MemoryNode` or related `ReadoutEdge`: `readoutAccuracy` = 5.350 degrees (RMSE)

### **3.6 Degradation Rate (Optional - if applicable)**
* **Vector ID:** M3.6
* **Vector Type:** Parameter
    *   Value: N/A
    *   Units: Qualitative Descriptor: "Low Degradation"
    *   Justification: The paper states "no significant drift over very long horizons (10 minutes or more)," implying a low degradation rate of the memory or prediction accuracy over the tested timescale. However, the degradation rate is not quantified with a specific percentage loss per hour or similar metric.
    *    Implicit/Explicit: Mixed
            * Justification: The qualitative assessment of low degradation is explicitly stated, but a quantitative rate is not provided, leading to a mixed explicit/implicit categorization.
    *   CT-GIN Mapping: Attribute of the `MemoryNode`: `degradationRate` = "Low Degradation over 10 minutes (Qualitative)"

### **3.7 Memory Operations Energy Cost (Optional - if applicable)**
* **Vector ID:** M3.7
* **Vector Type:** Table
*   Table:
    | Memory Operation ID | Energy Consumption per Bit | Power Usage during Operation| Units | Uncertainty | Data Source Reference | Implicit/Explicit | Justification |
    | :------------------ | :--------------------------: | :-----------------------------: | :---: |:-----------------:|:-----------------:|:-----------------:| :------------------ |
    | LSTM Prediction | N/A                            | N/A                                 | N/A   | N/A             | N/A               | Implicit         | Energy cost of LSTM operations is not reported; assumed external computation |
*   Implicit/Explicit: Implicit
    *   Justification: The paper does not discuss or quantify the energy cost of memory operations within the LSTM network. It is implicitly assumed that the neural network computation is performed externally (e.g., on a computer), and the energy consumption of these operations is beyond the scope of the paper focusing on the soft robot limb and sensing.

### **3.8 Memory Fidelity & Robustness Metrics (Optional - if applicable)**
* **Vector ID:** M3.8
* **Vector Type:** Table
*   Table:
    | Metric ID | Description | Value | Units | CT-GIN Mapping | Data Source | Implicit/Explicit | Justification |
    | :-------- | :---------- | :----: | :---: | :-------------: | :----------: |:-----------------:| :-----------------:|
    | RMSE_Rollout_Test4 | Root Mean Squared Error of open-loop rollout prediction for Test 4 (Bidirectional, with Temperature) | 5.350 | degrees | Attribute of `MemoryNode` (LSTM) Performance | Table 1, Figure 7 | Explicit | Quantifies prediction error in a long-term simulation |
    | RMSE_OneStep_Test1 | Root Mean Squared Error of one-step-ahead prediction for Test 1 (Unidirectional, PWM only) | 0.2091 | degrees | Attribute of `MemoryNode` (LSTM) Performance | Figure 6 | Explicit |  Quantifies immediate prediction error |
*   Implicit/Explicit: Explicit
*   Justification: The metrics used to assess memory fidelity and robustness (specifically prediction accuracy as RMSE) are explicitly reported in the Results section and figures.

---

## M4: Self-Organization and Emergent Order
*   **Vector ID:** M4
*   **Vector Type:** Self-Organization

### **4.1 Self-Organization Presence:**

*   **Vector ID:** M4.1
*   **Vector Type:** Binary
    *   Content: [No]
    *   Justification: The paper describes a system that is explicitly designed and fabricated with predefined components (SMA coils, sensors, silicone body) and a trained neural network. There is no indication of spontaneous self-assembly or emergence of global order from local interactions within the described system. The structure and functionality are entirely determined by the design and training process, not by self-organization.
    *   Implicit/Explicit: Explicit
        *  Justification: The absence of self-organization is explicit as the paper details a designed and engineered system, contrasting with systems exhibiting spontaneous order formation.

**(Conditional: If M4.1 is "No", skip to Module 5. If "Yes", include M4.2-M4.7)**

### **4.2 Local Interaction Rules:**

*   **Vector ID:** M4.2
*   **Vector Type:** Rules
    *   Content: N/A
    *   CT-GIN Mapping: N/A
    * **Implicit/Explicit**: N/A
        *  Justification: Since self-organization is not present, this section is not applicable.

### **4.2.1 Local Interaction Parameters:**

* **Vector ID:** M4.2.1
* **Vector Type:** Table
*   Table:
    | Rule ID | Description | Parameter Name | Parameter Value Range | Units | Data Source | Implicit/Explicit | Justification |
    | :------ | :---------- | :------------- | :---------- | :---: | :----------: | :----------------: | :------------: |
    | N/A  | N/A         | N/A            | N/A           | N/A   | N/A         | N/A              | N/A          |
### **4.3 Global Order:**

*   **Vector ID:** M4.3
*   **Vector Type:** Order
    *   Content: N/A
    *   CT-GIN Mapping: N/A
    * **Implicit/Explicit**: N/A
        *  Justification: Since self-organization is not present, this section is not applicable.

### **4.4 Predictability of Global Order:**

*   **Vector ID:** M4.4
*   **Vector Type:** Score
    *   Score: [0]
    *   Justification: Since there is no self-organization, the predictability of a global order in the context of self-organization is not applicable and scored as 0. The order in the system is designed, not emergent, so predictability in that sense is high (design predictability), but irrelevant to self-organization.
    * **Implicit/Explicit**: N/A
    *  Justification: Not applicable in the context of no self-organization.
    *   CT-GIN Mapping: N/A

### **4.5. Local Interaction Rules (for Self-Organization)**
* **Vector ID:** M4.5
* **Vector Type:** Table
*   Table:
| Rule ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Source |
| :------ | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :-----: |
| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |

### **4.6. Globally Emergent Order and Order Parameters**
* **Vector ID:** M4.6
* **Vector Type:** Table
*   Table:
| Property ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Protocol | Source |
| :---------- | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :------: | :-----: |
| N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |

### **4.7 Yoneda Embedding and Local-to-Global Mapping Fidelity**

*   **Vector ID:** M4.7
*   **Vector Type:** Table
*   Table:
    | Link Type | Description | Predictability | Yoneda Score | Metrics | Implicit/Explicit | Justification | Source |
    | :-------- | :---------- | :------------- | :----------- | :------ | :----------------: | :------------: | :-----: |
     | N/A  | N/A         | N/A            | N/A           | N/A     | N/A               | N/A          | N/A   |
    *   **Yoneda Embedding Fulfillment Score [0-10]:** [N/A]
    *   **Metrics:**  [N/A]
    *   **Justification:** [N/A]

## M5: Computation
*   **Vector ID:** M5
*   **Vector Type:** Computation

### **5.1 Embodied Computation Presence:**

*   **Vector ID:** M5.1
*   **Vector Type:** Binary
    *   Content: [No]
    *   Justification: The computational aspect of the system, namely the dynamics prediction, is performed by the LSTM neural network. This network is implemented as software running on a computer (Google Colab), which is external to the soft robot limb itself. The robot limb and its sensors provide input data to the neural network, but the limb material and structure do not intrinsically perform the computation. The computation is not embodied within the material, but rather performed by an external processing unit.
    *    Implicit/Explicit: Explicit
        *  Justification: The paper clearly describes the neural network as a separate entity trained and run on a computer, not as an intrinsic computational property of the soft robot material.

**(Conditional: If M5.1 is "No", skip to Module 6. If "Yes", include M5.2-5.4)**

### **5.2 Computation Type:**

*   **Vector ID:** M5.2
*   **Vector Type:** Classification
    *   Content: [Neuromorphic]
    *   CT-GIN Mapping: `ComputationNode` type = "Neural Network"
    *    Implicit/Explicit: Explicit
    *    Justification: The computation is performed by an LSTM *neural network*, which is explicitly stated and is a neuromorphic type of computation.

### **5.3 Computational Primitive:**

*   **Vector ID:** M5.3
*   **Vector Type:** Function
    *   Content: The computational primitive is time-series prediction of the robot limb's bending angle. At a lower level, the LSTM network performs complex non-linear transformations of input sequences through matrix multiplications, activation functions (tanh, sigmoid, ReLU), and memory cell updates.  Each LSTM cell implements functions for forget gate (sigmoid), input gate (sigmoid), output gate (sigmoid), cell state update (tanh, component-wise multiplication, addition), and hidden state output (tanh, component-wise multiplication). The overall network function is to map input sequences of PWM and temperature data (and past deflection) to future deflection angles.
    *   **Sub-Type (if applicable):** Time-Series Prediction, Recurrent Neural Network (LSTM)
    *   CT-GIN Mapping: Defines the primary function of the `ComputationNode`: `computationalPrimitive` = "Time-Series Prediction", `subType` = "LSTM Recurrent Neural Network"
    *   Implicit/Explicit: Mixed
    * Justification: The overall function (time-series prediction) is explicit. The detailed breakdown of LSTM cell operations and activation functions is based on general knowledge of LSTM architecture and is therefore implicitly derived in the context of this paper's usage of LSTM.

### **5.4 Embodied Computational Units**
* **Vector ID:** M5.4
* **Vector Type:** Table
*   Table:
| Unit ID | Description | Processing Power | Energy/Operation | Freq/Resp. Time | Bit-Depth | Data Source | Implicit/Explicit | Justification |
| :------ | :---------- | :--------------- | :--------------- | :--------------: | :-------: | :----------: |:-----------------:| :-----------------:|
| LSTM Cell  | Basic unit of LSTM network | N/A              | N/A              | N/A             | Analog-like  | N/A         | Implicit        | Computational unit is the LSTM cell in external software model.   |

## M6: Temporal Dynamics
*   **Vector ID:** M6
*   **Vector Type:** Temporal

### **6.1 Timescales:**

*   **Vector ID:** M6.1
*   **Vector Type:** ParameterTable
    *   Table:
        | Timescale Description | Value | Units | Source | Implicit/Explicit | Justification |
        | :-------------------- | :---: | :---: | :----: | :----------------: | :------------: |
        | Open-loop Prediction Horizon | 10 or more | minutes | Abstract, Results, Fig. 7 | Explicit |  Duration over which accurate predictions are demonstrated |
        | Data Collection Duration | 6 | hours | Section 2.2 | Explicit | Total time of experimental data collection |
        | Training Data Duration | 30 | minutes | Section 2.2 | Explicit |  Subset of collected data used for training the LSTM model |
        | LSTM Training Epochs | 20 | epochs | Section 2.4 | Explicit | Number of training iterations |
        | PWM Control Cycle Period | N/A | seconds | Section 2.1.2 | Implicit | PWM control is used, cycle period assumed to be in typical microcontroller range, not explicitly specified |

    *   **Note:** N/A

### **6.2 Active Inference:**

*   **Vector ID:** M6.2
*   **Vector Type:** Assessment
    *   Content: [Partial]
    *   Justification: The system demonstrates elements partially related to active inference. The LSTM network learns to predict future states (limb deflection) based on sensory inputs (temperature, deflection) and control commands (PWM). This predictive capability can be seen as an internal model. The system uses this model to anticipate the limb's behavior. However, the current implementation lacks active selection of actions *by the robot* to minimize prediction error or "surprise" in a closed-loop, embodied fashion. The control is still largely feedforward based on PWM inputs; the LSTM enhances prediction but doesn't close the loop for active error minimization through embodied action selection in a way characteristic of active inference.  It's more passive prediction with sensor feedback for model training and input, not active closed-loop control specifically designed to minimize surprise.
    *   Implicit/Explicit: Mixed
        *  Justification:  The predictive nature of the LSTM and use of sensor data for prediction aligns partially with active inference principles (internal model, prediction). However, the absence of active, embodied action selection for surprise minimization makes it only a partial implementation. This assessment is based on both explicit descriptions of the LSTM and control strategy, and implicit interpretation within the framework of active inference.
    *   **If Yes/Partial, provide examples of testable CT-GIN metrics that *could* be used to quantify active inference:** Testable CT-GIN metrics to quantify active inference *if* the system were extended could include: 1. Prediction Error Reduction Rate under different control strategies: Measure how different control policies (beyond simple PWM) influence the rate at which prediction error (difference between predicted and actual deflection) is reduced over time. Policies designed to actively minimize predicted error should show faster reduction. 2. Timescale of Anticipation: Quantify how far into the future the system's predictions are effectively influencing current control action in a closed-loop setup. Active inference systems tend to exhibit anticipatory control, where current actions are shaped by predictions of events further in the future, not just immediate responses. 3. Complexity & Adaptability of Internal Models: Assess how the complexity of the LSTM model (e.g., number of parameters, effective dimensionality of latent space) changes when the system is tasked with actively minimizing surprise in dynamically changing environments. Active inference agents typically require more complex and adaptable models to handle environmental uncertainty and achieve effective surprise minimization. Experimental setups to test this could involve introducing perturbations or changes in the environment (e.g., external forces on the limb) and measuring how the system adapts its control and prediction models.

## M7: Adaptation
*   **Vector ID:** M7
*   **Vector Type:** Adaptation

### **7.1 Adaptive Plasticity Presence:**

*   **Vector ID:** M7.1
*   **Vector Type:** Binary
    *   Content: [No]
    *   Justification: The system, as described, does not exhibit adaptive plasticity *during operation*. The LSTM neural network is trained offline using a pre-collected dataset. Once trained, the network weights are fixed, and the model is used for open-loop prediction. There is no mechanism for the system to further adapt its behavior or internal model in response to new experiences or changes in the environment after the training phase is complete. The behavior remains fixed based on the initially learned dynamics.
    *    Implicit/Explicit: Explicit
        * Justification: The description clearly outlines a training phase followed by a fixed prediction phase. No online adaptation or plasticity is mentioned or implied within the operational system.

**(Conditional: If M7.1 is "No", skip to Module 8. If "Yes", include M7.2)**

### **7.2 Adaptation Mechanism:**

*   **Vector ID:** M7.2
*   **Vector Type:** Description
    *   Content: N/A
    *   CT-GIN Mapping: N/A
    *    Implicit/Explicit: N/A
        *  Justification: Since adaptive plasticity is not present, this section is not applicable.

## M8: Emergent Behaviors
*   **Vector ID:** M8
*   **Vector Type:** Behavior

### **8.1 Behavior Description:**

*   **Vector ID:** M8.1
*   **Vector Type:** Description
    *   Content: The primary functional behavior is the prediction of the soft robot limb's angular deflection over time. This prediction is achieved by processing PWM control signals and in-situ temperature sensor data through a trained LSTM neural network. The system outputs a predicted trajectory of the limb's bending angle.  Observable behavior is the time-series prediction of deflection angle, validated against measured deflection.
    *   CT-GIN Mapping: `BehaviorArchetypeNode`. Specify the type of behavior: "Dynamics Prediction of Soft Robot Limb Motion". `behaviorType` = "Prediction", `domain` = "Robotics", `observableOutput` = "Time-series of Predicted Deflection Angle", `inputSignals` = "PWM, Temperature Sensor Data"
    *    Implicit/Explicit: Explicit
       *  Justification: The behavior description is directly derived from the paper's stated objective and demonstrated results – the system predicts limb motion.

### **8.2 Behavior Robustness:**

*   **Vector ID:** M8.2
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The model demonstrates reasonable robustness in its prediction capability over extended timescales (10 minutes), exhibiting low drift and prediction errors comparable to the sensor accuracy. This indicates robustness to internal dynamic variations and time. However, robustness to external perturbations (e.g., external forces, temperature changes outside training data), sensor noise, or potential component failures (e.g., sensor drift, SMA degradation) is not explicitly tested or quantified.  The robustness demonstrated is primarily in terms of temporal stability of prediction under the controlled experimental setup. Qualitative assessment: Moderately Robust (temporal stability demonstrated, but limited stress testing).
    *   Implicit/Explicit: Mixed
        *  Justification: The temporal robustness (low drift over 10 mins) is explicitly shown in the results. However, the limitations in robustness testing (lack of external perturbation tests, sensor noise analysis, etc.) are implicitly inferred from the scope of the experiments presented.
    *   CT-GIN Mapping: e.g., This score contributes to the reliability attributes of the `BehaviorArchetypeNode`: `robustnessScore` = 7, `robustnessAspects` = "Temporal Stability of Prediction", `robustnessLimitations` = "Untested against external perturbations, sensor noise, component failures"

### **8.3 CT-GIN Emergent Behavior Validation**

*    **Vector ID:** M8.3
*    **Vector Type:** Validation
     *  Content: Validation of the prediction behavior is quantitatively performed using Root Mean Squared Error (RMSE) metrics for both one-step-ahead and open-loop rollout predictions. These metrics are compared across different input configurations (PWM only, PWM+Temperature) and motion types (unidirectional, bidirectional) as shown in Figure 6, Figure 7, and Table 1. Control experiments involve comparison to a least-squares fit model (Table 1, Figure 8) to demonstrate the LSTM's superior ability to capture hysteresis. Reproducibility is supported by the open-sourced code and datasets. Limitations of validation are that it primarily focuses on the accuracy of deflection prediction and does not explore broader functional behaviors or robustness to diverse external conditions beyond the training data distribution.
     *   Implicit/Explicit: Explicit
    *   Justification: The validation methods (RMSE, comparisons, open-source data), results (figures, tables), and limitations are explicitly detailed within the Results and Methods sections of the paper.

## M9: Cognitive Proximity
*   **Vector ID:** M9
*   **Vector Type:** Cognition

### **9.1 Cognitive Mapping:**

*   **Vector ID:** M9.1
*   **Vector Type:** Description
    *   Content: None. The paper does not attempt to explicitly map the system's functionality to cognitive processes, even metaphorically, beyond referring to "dynamics modeling" and "prediction" which are general information processing terms but not framed as cognitive analogies in the paper.
    *   CT-GIN Mapping: N/A
    *   Implicit/Explicit: Explicit
    * Justification: The absence of cognitive mapping is clear from the lack of any discussion in the paper relating the system's operation to cognitive functions or analogies.

### **9.2 Cognitive Proximity Score:**

*   **Vector ID:** M9.2
*   **Vector Type:** Score
    *   Score: [1]
    *   Justification: The system is best placed at Level 1: Simple Responsivity on the CT-GIN Cognizance Scale. While it employs a learned model (LSTM) for prediction, the fundamental behavior remains a stimulus-response. Electrical input (PWM) and sensor readings lead to a predicted deflection angle. The system's "response" is more sophisticated than a direct stimulus-response due to the predictive model, but it lacks goal-directedness, planning, contextual understanding, or higher-level cognitive functions. It reacts to inputs with a learned prediction, but actions are not autonomously chosen to achieve goals or adapt flexibly in complex scenarios. It is beyond Level 0 (purely reactive) due to the predictive model, but confined to basic responsivity within a learned framework.
    *   Implicit/Explicit: Mixed
    *  Justification: The score of 1 is an interpretation based on mapping the system's demonstrated behavior (prediction of limb deflection) onto the CT-GIN Cognizance Scale. This involves assessing the system's capabilities against the scale's levels, which is an inferential process, although based on explicit descriptions of the system's functionality in the paper.

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
    | Sensing/Perception               | 6          | Temperature and deflection are sensed with reasonable accuracy using embedded sensors. | `CognitiveFunctionNode`: `functionType`="Sensing/Perception", `sensorTypes`="Temperature, Deflection" | Explicit            | Explicit          |
    | Memory (Short-Term/Working)        | 5          | LSTM network inherently possesses short-term memory capabilities for time-series tasks.   | `CognitiveFunctionNode`: `functionType`="Memory (Short-Term/Working)", `mechanism`="LSTM Network" | Explicit            | Explicit          |
    | Memory (Long-Term)                 | 6          | LSTM weights and trained parameters encode long-term memory of learned dynamics.     | `CognitiveFunctionNode`: `functionType`="Memory (Long-Term)", `mechanism`="LSTM Network Weights" | Explicit            | Explicit          |
    | Learning/Adaptation              | 4          | LSTM learns dynamics during offline training but lacks online adaptation in operation.  | `CognitiveFunctionNode`: `functionType`="Learning/Adaptation", `learningType`="Offline LSTM Training" | Explicit            | Explicit          |
    | Decision-Making/Planning          | 1          | No explicit decision-making or planning capabilities described. System predicts motion. | `CognitiveFunctionNode`: `functionType`="Decision-Making/Planning", `level`="Absent" | Explicit            | Explicit          |
    | Communication/Social Interaction | 0          | No communication or social interaction functions present.                            | `CognitiveFunctionNode`: `functionType`="Communication/Social Interaction", `level`="Absent" | Explicit            | Explicit          |
    | Goal-Directed Behavior            | 1          | System's primary behavior is dynamics prediction, not goal-directed action.             | `CognitiveFunctionNode`: `functionType`="Goal-Directed Behavior", `level`="Low" | Explicit            | Explicit          |
    | Model-Based Reasoning              | 3          | LSTM serves as a model for prediction, but not complex reasoning in a cognitive sense. | `CognitiveFunctionNode`: `functionType`="Model-Based Reasoning", `modelType`="LSTM Network", `reasoningLevel`="Basic Prediction" | Explicit            | Explicit          |
    | **Overall score**                 |      3.3       | Average of the individual cognitive function scores.                                | N/A                              | N/A                 | N/A               |

    *   **Note:** N/A

## M10: Criticality Assessment
*   **Vector ID:** M10
*   **Vector Type:** Criticality

### **10.1 Criticality:**

*   **Vector ID:** M10.1
*   **Vector Type:** Assessment
    *   Content: [No]
    *   Justification: The paper does not discuss or imply that the system operates near a critical point or exhibits criticality phenomena. The dynamics are modeled using a neural network, focusing on data-driven prediction rather than exploring phase transitions, scale-free behavior, or long-range correlations associated with criticality. The system's behavior is presented within a deterministic modeling framework, not in the context of critical phenomena.
        *   Critical Parameters (If Yes/Partial): [N/A]
        *   Evidence: [No evidence of criticality is present in equations, figures, or data.]
    *   Implicit/Explicit: Explicit
    *    Justification: The absence of criticality is explicitly determined from the lack of any mention or evidence within the paper, focusing instead on deterministic neural network modeling.

## M11: Review Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Review")**

*   **Vector ID:** M11
*   **Vector Type:** Review
### **11.1 Literature Synthesis Quality:**

*   **Vector ID:** M11.1
*   **Vector Type:** Score
    *   Score: N/A
    *   Justification: N/A
       * Implicit/Explicit: N/A
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
    *   Justification: N/A
    *    Implicit/Explicit: N/A
    *   Justification: N/A

## M13: Overall Assessment & Scoring

*   **Vector ID:** M13
*   **Vector Type:** Overall

### **13.1 CT-GIN Readiness Score:**

*   **Vector ID:** M13.1
*   **Vector Type:** Score
*   **Calculated Score:** [4.3]

**CT-GIN Readiness Summary Table:**

| CT-GIN Aspect                   | Strength  | Key Supporting Metrics (with units) | Limitations (Missing Metrics/Data Gaps)                                           | Improvement Areas (Future Research)                                          |
| :------------------------------ | :-------: | :-----------------------------------| :------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| Energy Flow Efficiency          |    Low    | N/A                                 | Lacks efficiency quantification                                                 | Explore energy-efficient actuation methods; quantify efficiency                 |
| Memory Fidelity                 |  Medium   | RMSE Rollout: 5.350 degrees         | Capacity, degradation not fully explored                                        | Quantify memory capacity, degradation over longer times                        |
| Organizational Complexity       |    No     | N/A                                 | No self-organization                                                            | Explore self-organizing structural elements in the soft robot                  |
| Embodied Computation            |    No     | N/A                                 | Computation offloaded to external computer                                      | Implement computation within the material or robot body                      |
| Temporal Integration            |  Partial  | Prediction horizon: 10 minutes     | Active inference aspects not deeply explored                                    | Investigate active inference mechanisms for control and adaptation           |
| Adaptive Plasticity             |    No     | N/A                                 | No online adaptation                                                            | Implement online learning or adaptation in robot's control model            |
| Functional Universality         |  Limited  | Dynamics Prediction               | Behavior focused on limb motion prediction                                        | Explore broader range of functional behaviors                               |
| Cognitive Proximity            |    Low    | Cognitive Level 1                   | Lacks goal-directedness, higher-level cognitive functions                       | Integrate goal-directed behavior, planning, or more complex cognition       |
| Design Scalability & Robustness |  Partial  | Robust to time, low drift         | Robustness not comprehensively tested (external perturbations, failure modes) | Test robustness to wider range of perturbations; consider scalability aspects |
| **Overall CT-GIN Readiness Score** |   4.3   | RMSE Rollout: 5.350 degrees         | Limited embodied intelligence, no self-organization or criticality               | Embodied computation, self-organization, adaptive plasticity, criticality     |


### **13.2 Qualitative CT-GIN Assessment Conclusion:**

*   **Vector ID:** M13.2
*   **Vector Type:** Textual Summary
    *   Content: The analyzed paper presents a soft robot limb with in-situ sensing and LSTM-based dynamics prediction. Key strengths include the demonstration of long-term motion prediction and sensor integration. However, the system exhibits limitations in CT-GIN aspects such as energy efficiency, embodied computation, and lack of self-organization and adaptive plasticity. Overall assessment indicates a system at a low level of CT-GIN readiness (Level 1 Cognitive Proximity), primarily focused on stimulus-response and predictive modeling rather than emergent, self-organizing, or truly adaptive behaviors. Future development towards higher CT-GIN levels would require incorporating embodied computation, self-organization principles, and mechanisms for online adaptation and active inference.

### **13.3 CT-GIN Refinement Directions:**

*   **Vector ID:** M13.3
*   **Vector Type:** Recommendations
    *   Content: * Explore energy-efficient actuation mechanisms beyond electrothermal SMAs.
* Implement embodied computation by integrating computational elements within the soft robot body, potentially using analog or neuromorphic approaches.
* Investigate self-organization principles for robot limb structure or actuation patterns to reduce design complexity and enhance adaptability.
* Incorporate online learning and adaptive plasticity mechanisms to enable the robot to refine its model and behavior during operation.
* Explore active inference-based control strategies to allow the robot to actively interact with its environment and minimize prediction errors in a closed-loop manner.
* Broaden the functional behaviors beyond motion prediction to include goal-directed tasks, environmental interaction, or basic forms of problem-solving.
* Systematically evaluate robustness to external perturbations, sensor noise, and component failures, and design for increased resilience.

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

## M16: CT-GIN Template Self-Improvement Insights

*   **Vector ID:** M16
*   **Vector Type:** Feedback

### **Template Feedback:**

*    **Vector ID:** M16.1
*   **Vector Type:** Text
Provide specific, actionable feedback on the *CT-GIN template itself*, based on this analysis:
    *   **Missing Probes:** No immediately obvious missing probes. The template seems comprehensive for initial assessment. Maybe probes related to material composition and fabrication complexity could be added for deeper material intelligence analysis.
    *   **Unclear Definitions:** Definitions are generally clear. "Active Inference" might benefit from a slightly more operational definition within the context of material systems, perhaps with more concrete examples.
    *   **Unclear Node/Edge Representations:** Guidance for GIN mapping is sufficient.
    *   **Scoring Difficulties:** Cognitive Proximity Score and Checklist scores are somewhat subjective and require careful justification based on the Cognizance Scale. Providing more granular descriptions for each Cognitive Function level in M9.3 checklist could improve consistency and reduce subjectivity.
    *   **Data Extraction/Output Mapping:** Generally straightforward data extraction. Mapping quantitative parameters with units to table format works well.
    *   **Overall Usability:** Template is well structured and usable. Lengthy for detailed papers but allows for comprehensive analysis.
    * **Specific Suggestions:**
        * Add probes for material composition details (Material types, complexity).
        * Add probes for fabrication complexity and scalability (Number of steps, precision requirements, materials cost).
        * Refine 'Active Inference' definition for material systems (operational terms with examples).
        * Add more granular level descriptions to Cognitive Function Checklist scores in M9.3 to better differentiate between levels for each function.