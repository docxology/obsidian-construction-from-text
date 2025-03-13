# Deep physical neural networks trained with backpropagation:

__Paper Type:__ Experimental

## M1: System Overview & Implementation
*   **Vector ID:** M1
*   **Vector Type:** Overview

### **1.1 System Description**

*   **Vector ID:** M1.1
*   **Vector Type:** Description
    *   Content: The system is a hybrid in situ–in silico algorithm called physics-aware training (PAT) used to train deep physical neural networks (PNNs). PNNs are constructed from layers of controllable physical systems, such as mechanics (oscillating metal plate), electronics (nonlinear electronic oscillator), and optics (ultrafast second-harmonic generation (SHG)). The system performs machine learning tasks, specifically audio and image classification, by harnessing the physical transformations of these systems. Input data and trainable parameters are encoded into physical properties (e.g., time-dependent forces, voltage, pulse spectra). The physical systems process the input, and the output is measured. PAT uses backpropagation, where a differentiable digital model estimates gradients to update physical system parameters based on the error between the physical output and the target output.
    *   CT-GIN Mapping: `SystemNode` attributes: `systemType: Hybrid`, `domain: Physics-based Machine Learning`, `mechanism: Physics-aware training (PAT) of Physical Neural Networks (PNNs)`, `components: Mechanical system, Electronic system, Optical system, Digital computer for backpropagation`, `purpose: Energy-efficient and faster machine learning, Automatically designed physical functionalities`
    *   Implicit/Explicit: Mixed
        *  Justification: The system's components, purpose, and general operation are explicitly stated. However, details like "deep physical neural networks" and "physics-aware training" need implicit understanding from the context provided in the article.

### **1.2 Implementation Clarity**

*   **Vector ID:** M1.2
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The implementation is relatively clear for an experimental paper. The paper describes the PAT algorithm and its application to three different physical systems. Figures illustrate the setups for optics, mechanics, and electronics. The methods section provides further details on experimental procedures and model training. Clarity could be improved by providing more specifics on the digital model used for backpropagation for each physical system and the exact parameterization of the physical systems (e.g., equations governing the metal plate oscillation, electronic oscillator, and SHG process).
    *   Implicit/Explicit: Mixed
        * Justification: The high-level implementation is explicit, with diagrams and descriptions. However, the fine details of each physical system's control and modeling are implicitly assumed to be understood by experts in those fields, or referred to supplementary materials.

### **1.3 Key Parameters**

*   **Vector ID:** M1.3
*   **Vector Type:** ParameterTable
    *   Table:
        | Parameter Name | Value | Units | Source (Fig/Table/Section) | Implicit/Explicit | Data Reliability (High/Medium/Low) | Derivation Method (if Implicit) |
        | :------------- | :---: | :---: | :-----------------------: | :-----------------: | :-----------------------------: | :-------------------------------: |
        | Optical pulse center wavelength | ~800 | nm | Fig 2a, Methods | Explicit | High | N/A |
        | Optical pulse duration | ~100 | fs | Methods | Explicit | High | N/A |
        | Metal plate size | 3.2x3.2x1 | cm | Methods | Explicit | High | N/A |
        | BBO crystal length | 0.5 | mm | Methods | Explicit | High | N/A |
        | Electronic circuit sampling rate | 1 | MS/s | Methods | Explicit | High | N/A |

    *   **Note:** List *up to 5* key parameters characterizing the system's *implementation*.  Provide values and units if possible. If a parameter is not explicitly stated but derived/inferred, clearly state the derivation method. *Always* include units if applicable. If a value is not applicable, write "N/A".  Data Reliability: High = Directly measured, Medium = Derived from measurements/simulations, Low = Estimated/Inferred.

## M2: Energy Flow
*   **Vector ID:** M2
*   **Vector Type:** Energy

### **2.1 Energy Input**

*   **Vector ID:** M2.1
*   **Vector Type:** Input
    *   Content: For the optical PNN, the energy source is a mode-locked titanium-sapphire laser. For the mechanical PNN, the energy source is an audio amplifier driving a speaker. For the electronic PNN, the energy source is a USB data acquisition (DAQ) device providing voltage.
    *   Value: N/A
    *   Units: N/A
    *   CT-GIN Mapping: `EnergyInputNode`: attributes - `source: Titanium-sapphire laser, Audio amplifier, USB DAQ`, `type: Optical pulse, Electrical signal, Electrical signal`
    *   Implicit/Explicit: Explicit
        *  Justification: These energy sources are explicitly mentioned in the Methods section when describing each experimental setup (Ultrafast nonlinear optical pulse propagation experiments, Oscillating mechanical plate experiments, Analogue electronic circuit experiments).

### **2.2 Energy Transduction**

*   **Vector ID:** M2.2
*   **Vector Type:** Transduction
    *   Content: In the optical PNN, the laser's optical energy is transduced through pulse shaping (spectral modulation) to encode input data and parameters. This shaped pulse then propagates through a χ(2) crystal, generating a blue pulse via second-harmonic generation (SHG), thus transducing infrared photons to blue photons and performing nonlinear computation. In the mechanical PNN, electrical energy from the audio amplifier drives the speaker, causing mechanical oscillations in the metal plate. Input and parameters are encoded into time-varying forces applied to the plate. The plate's mechanical oscillations are measured by a microphone, transducing mechanical energy to electrical signals. In the electronic PNN, electrical energy from the DAQ device is used as input voltage to a nonlinear electronic circuit (RLC oscillator with a transistor). The circuit's transient response (voltage oscillations) is measured, retaining electrical energy in the electrical domain but transforming it via nonlinear circuit dynamics.
    *   CT-GIN Mapping: `EnergyTransductionEdge`: attributes - `mechanism: Spectral Modulation, Second Harmonic Generation (SHG)`, `from_node: Laser Output`, `to_node: SHG Output Spectrum`; `EnergyTransductionEdge`: attributes - `mechanism: Electromechanical transduction, Mechanical oscillation`, `from_node: Audio Amplifier Output`, `to_node: Metal Plate Oscillation`; `EnergyTransductionEdge`: attributes - `mechanism: Nonlinear Electronic Oscillation`, `from_node: DAQ Output Voltage`, `to_node: Electronic Oscillator Output Voltage`
    *   Implicit/Explicit: Mixed
        *  Justification: The main energy transduction steps are explicitly described in the context of each PNN type within the text and Methods section. The physical mechanisms like SHG and mechanical oscillation are also stated although the details of these mechanisms are implicitly assumed to be known or require external knowledge.

### **2.3 Energy Efficiency**

*   **Vector ID:** M2.3
*   **Vector Type:** Score
    *   Score: [6]
    *   Justification/Metrics: The paper claims PNNs have the "potential to perform machine learning faster and more energy-efficiently than conventional electronic processors". However, no quantitative energy efficiency metrics (e.g., energy per operation, joules per classification) are provided for the experimental PNN implementations.  The score is moderate because while energy efficiency is a primary motivation and potential benefit, the paper lacks concrete efficiency measurements for these specific systems, relying on general arguments and potential.
    *   CT-GIN Mapping: Attribute of relevant `EnergyTransductionEdge`s
    *   Implicit/Explicit: Implicit
      *  Justification: Energy efficiency is discussed conceptually and motivationally, but without explicit quantitative metrics for the demonstrated systems.  The efficiency score is inferred based on the potential advantages and lack of explicit efficiency data.

### **2.4 Energy Dissipation**

*   **Vector ID:** M2.4
*   **Vector Type:** Dissipation
    *   Content: Dissipation mechanisms are implicitly present in all described systems, but not explicitly quantified. In the optical system, dissipation likely occurs due to losses in optical components (pulse shaper, crystal), imperfect SHG conversion, and spectral filtering.  In the mechanical system, dissipation arises from air resistance, internal friction within the metal plate, and speaker coil resistance. In the electronic system, dissipation is due to resistance in circuit components (resistors, inductor, transistor).  Qualitatively, dissipation is expected to be Medium for optics and electronics and potentially Higher for mechanics due to mechanical losses and sound radiation.
    *   CT-GIN Mapping: Creates `EnergyDissipationNode`s: `DissipationType: Optical Losses, Mechanical Friction, Electrical Resistance` and `EnergyDissipationEdge`s from each `EnergyTransductionEdge` to respective `EnergyDissipationNode`s.
    *    Implicit/Explicit: Implicit
        *  Justification: Dissipation mechanisms are not explicitly quantified or detailed in the paper. Their presence is inferred from general physics principles governing optical, mechanical, and electronic systems.  The qualitative assessment is based on typical dissipation sources in such systems.

## M3: Memory
*   **Vector ID:** M3
*   **Vector Type:** Memory

### **3.1 Memory Presence:**

*   **Vector ID:** M3.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: The trainable parameters within the PNNs represent a form of memory. These parameters, encoded as spectral modulations in optics, forces in mechanics, and voltages in electronics, are adjusted during training and persist after the training stimulus (data) is removed. They influence future behavior by determining how the physical system transforms subsequent inputs in the forward pass. The trained parameters dictate the network's classification performance on new data, demonstrating memory influencing future behavior.
    *    Implicit/Explicit: Explicit
        * Justification: The concept of "trainable parameters" and their adjustment via backpropagation to store learned information is explicitly central to the paper's physics-aware training methodology and the function of neural networks in general.

### **3.2 Memory Type:**

*   **Vector ID:** M3.2
*   **Vector Type:** Score
*   Score: [7]
*   Justification: The memory is analogous to synaptic weights in artificial neural networks. The parameters are re-writable through the PAT algorithm and are stable as long as they are stored digitally or in the physical system's configuration. Retention is long-term in the context of the trained model, capacity depends on the number of trainable parameters, and readout accuracy is related to the precision of parameter setting and the system's noise level. The score is 7 because while parameters are re-writable and stable and hold learned information influencing future computation, the paper does not provide detailed characterization in terms of bit stability, refresh rate, or other specific memory metrics, instead focusing on classification accuracy as the performance metric.
*   CT-GIN Mapping: Defines the `MemoryNode` type.
*    Implicit/Explicit: Mixed
    * Justification: The paper describes parameter training and persistence, which implies re-writability and stability implicitly characteristic of memory. The score and justification are based on analogy to neural network weights and general memory characteristics, combined with the paper's description of the training process.

### **3.3 Memory Retention Time:**

*   **Vector ID:** M3.3
*   **Vector Type:** Parameter
*   Value: Long-term
*    Units: Qualitative Descriptor: "Long-term"
*   Justification: The retention time of the trained parameters is effectively long-term, meaning the parameters, once set by the physics-aware training, will persist unless explicitly retrained or altered.  In experimental context, this means the parameters (e.g., spectral shaping settings, force scalings, voltage scalings) programmed into the control hardware (pulse shaper, DAQ) will remain as set until changed. In a digital context where parameters are stored as numerical values in a computer, retention is also long-term, limited by digital data storage persistence which is practically indefinite for the scope of the presented application.
*    Implicit/Explicit: Implicit
        * Justification: The term "long-term" is a qualitative descriptor inferred from the context of machine learning and neural network training where trained weights are expected to be stable for inference tasks after training.  The paper implicitly assumes this persistence for the trained PNN parameters.

### **3.4 Memory Capacity (Optional - if applicable)**

* **Vector ID:** M3.4
* **Vector Type:** Parameter
*  Value: High
*   Units: Qualitative Descriptor: "High" (Number of Trainable Parameters)
*   Justification: Memory capacity is related to the number of trainable parameters in the PNN. While the exact number is not explicitly listed, the paper describes training "deep" PNNs with multiple layers. Neural networks, in general, can have a very large number of parameters, especially deep networks. In the optical SHG-PNN example, spectral modulation vectors are used as parameters, which can be high-dimensional. The mechanical and electronic PNNs also use trainable rescaling parameters at each layer. Qualitatively, the memory capacity can be considered "High" in terms of the number of adjustable weights, typical in neural network models.
*    Implicit/Explicit: Implicit
        *  Justification:  The paper implicitly describes network architectures capable of having a large number of trainable parameters given the context of "deep learning" and multilayer networks. "High" capacity is an inferred qualitative descriptor based on typical neural network sizes, without specific parameter count being provided in the excerpt.

### **3.5 Readout Accuracy (Optional - if applicable)**

* **Vector ID:** M3.5
* **Vector Type:** Parameter
*   Value: High
*   Units: Qualitative Descriptor: "High" (Related to Classification Accuracy)
*   Justification: Readout accuracy is implicitly related to the classification accuracy achieved by the trained PNNs. The paper reports high test accuracies: 93% for vowel classification with SHG, 87% for MNIST with mechanics, 93% for MNIST with electronics, and 97% for MNIST with optics. These high accuracies suggest that the parameters are effectively "read out" by the physical systems to perform the desired transformations with reasonable fidelity to achieve these classification scores.
*    Implicit/Explicit: Implicit
       *  Justification:  Readout accuracy is not directly quantified as a memory metric but is inferred from the high classification accuracies. The "High" qualitative descriptor is justified by the reported performance metrics, indicating effective parameter utilization during the forward pass.

### **3.6 Degradation Rate (Optional - if applicable)**
* **Vector ID:** M3.6
* **Vector Type:** Parameter
    *   Value: Negligible
    *   Units: Qualitative Descriptor: "Negligible" (Over experimental timescales)
    *   Justification: The paper does not discuss memory degradation explicitly. However, in the context of digitally stored parameters and experimentally programmed physical system controls, degradation is likely to be negligible over the typical timescales of machine learning inference tasks (seconds to hours, potentially days if recalibration is performed less frequently).  If parameters are stored digitally, degradation is tied to digital data storage reliability, which is very high. If parameters are set in physical hardware (e.g., pulse shaper DMD settings, amplifier gains), their stability is dependent on the hardware's drift characteristics, which are generally designed for stability over operational periods.  For the time scale of experiments presented in the paper, degradation is reasonably assumed to be negligible.
    *    Implicit/Explicit: Implicit
            * Justification: Degradation is not mentioned. "Negligible" degradation is inferred from the typical stability of digital data and experimental control systems over the timeframes relevant to machine learning experiments, in the absence of contrary information in the paper.

### **3.7 Memory Operations Energy Cost (Optional - if applicable)**
* **Vector ID:** M3.7
* **Vector Type:** Table
*   Table:
    | Memory Operation ID | Energy Consumption per Bit | Power Usage during Operation| Units | Uncertainty | Data Source Reference | Implicit/Explicit | Justification |
    | :------------------ | :--------------------------: | :-----------------------------: | :---: |:-----------------:|:-----------------:|:-----------------:| :------------------ |
    | Parameter Update (Training) | N/A | N/A | Joules/bit, Watts | N/A | N/A | Implicit | No data provided on energy cost of memory operations specifically.  |
    | Parameter Storage (Inference) | N/A | N/A | Joules/bit, Watts | N/A | N/A | Implicit | No data provided on energy cost of memory operations specifically. |
*   Implicit/Explicit: Implicit
    *   Justification: The paper focuses on the potential energy efficiency of PNN *computation*, not the energy cost of memory operations (writing/reading parameters). Memory energy costs are not quantified or discussed in the context of PNN parameters.

### **3.8 Memory Fidelity & Robustness Metrics (Optional - if applicable)**
* **Vector ID:** M3.8
* **Vector Type:** Table
*   Table:
    | Metric ID | Description | Value | Units | CT-GIN Mapping | Data Source | Implicit/Explicit | Justification |
    | :-------- | :---------- | :----: | :---: | :-------------: | :----------: |:-----------------:| :-----------------:|
    | Classification Accuracy | Indirect measure of memory fidelity | 87-97 | % | Attribute of `MemoryNode` (indirect) | Fig 4, Fig 2 | Explicit | High classification accuracies are reported for different PNN systems. |
*   Implicit/Explicit: Explicit
*   Justification: While not direct metrics of memory *fidelity* in a storage sense, classification accuracy serves as an overall indicator of how effectively the trained parameters (memory) enable the system to perform its task. High accuracy suggests a reasonable degree of fidelity in parameter setting and use, even if not a direct bit-error rate type measure.

---

## M4: Self-Organization and Emergent Order
*   **Vector ID:** M4
*   **Vector Type:** Self-Organization

### **4.1 Self-Organization Presence:**

*   **Vector ID:** M4.1
*   **Vector Type:** Binary
    *   Content: [No]
    *   Justification: The paper describes designed physical neural networks trained for specific tasks. The network architectures and the physical systems used are pre-selected and controlled externally using the PAT algorithm. While the *parameters* of the physical systems are automatically tuned through training, the overall *structure* of the system—layers, connections, physical components—is externally designed and imposed. There is no mention of spontaneous self-assembly or emergence of global order from purely local rules without external specification of the network structure. The order is engineered and trained, not emergent in the self-organizing sense.
    *   Implicit/Explicit: Explicit
        *  Justification: The paper explicitly describes a training process (PAT) to *engineer* desired functionalities into pre-designed physical systems.  Self-organization, in the sense of spontaneous order from local rules without external global design, is absent and not claimed in the paper.  The focus is on *training* controlled physical systems, not on self-organizing matter.

**(Conditional: If M4.1 is "No", skip to Module 5. If "Yes", include M4.2-M4.7)**
N/A

## M5: Computation
*   **Vector ID:** M5
*   **Vector Type:** Computation

### **5.1 Embodied Computation Presence:**

*   **Vector ID:** M5.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: Yes, computation is embodied in the physical transformations of the mechanical, electronic, and optical systems. The paper explicitly states that "physical processes, rather than mathematical operations, are trained" and "physical transformations are often faster and consume less energy than their digital emulations." The forward pass of computation is performed by the physical hardware itself as it evolves according to its inherent physics when driven by inputs and parameters.  This physical evolution is the computational process, rather than being implemented by an external digital controller or simulation.
    *    Implicit/Explicit: Explicit
        *  Justification: The core concept of "physical neural networks" and "physics-aware training" explicitly revolves around performing computations via the intrinsic physical dynamics of the hardware. The paper emphasizes breaking "the traditional software–hardware division" to perform computations in situ within physical systems.

### **5.2 Computation Type:**

*   **Vector ID:** M5.2
*   **Vector Type:** Classification
    *   Content: Neuromorphic/Analog
    *   CT-GIN Mapping: `ComputationNode` type: `computationType: Neuromorphic, Analog`
    *    Implicit/Explicit: Mixed
    *    Justification: The paper uses "neural networks" and "neuromorphic computing" terms implicitly suggesting neuromorphic computation. Explicitly, the computation is analog because it relies on the continuous physical dynamics of the systems (oscillations, pulse propagation) rather than discrete digital steps. The physical transformations are described as analogous to, but not isomorphic with, conventional mathematical operations in DNNs, further suggesting analog/neuromorphic type.

### **5.3 Computational Primitive:**

*   **Vector ID:** M5.3
*   **Vector Type:** Function
    *   Content: Nonlinear Transformation
    *   **Sub-Type (if applicable):** Nonlinear Convolution (Optics, approximate), Nonlinear Transient Response (Electronics), Multimode Oscillations (Mechanics, approximate linear convolution)
    *   CT-GIN Mapping: Defines the primary function of the `ComputationNode`. `functionType: Nonlinear Transformation`, `subtype: Nonlinear Convolution (Optics), Nonlinear Transient Response (Electronics), Multimode Oscillations (Mechanics)`
    *   Implicit/Explicit: Mixed
    * Justification: Explicitly, the paper highlights that the physical transformations are "nonlinear". Implicitly,  the optical SHG is described as roughly analogous to a "nonlinear convolution". Electronic circuits exhibit nonlinear transient responses due to transistor characteristics.  Mechanical oscillations of the plate are presented as performing transformations, which, especially for multimode oscillations, can approximate convolution-like operations.  The exact mathematical primitives are complex and system-dependent, but broadly categorized as nonlinear transformations with subtypes related to convolution and transient dynamics.

### **5.4 Embodied Computational Units**
* **Vector ID:** M5.4
* **Vector Type:** Table
*   Table:
| Unit ID | Description | Processing Power | Energy/Operation | Freq/Resp. Time | Bit-Depth | Data Source | Implicit/Explicit | Justification |
| :------ | :---------- | :--------------- | :--------------- | :--------------: | :-------: | :----------: |:-----------------:| :-----------------:|
| Optical SHG Layer | Ultrafast nonlinear pulse propagation in χ(2) media | Potentially high, comparable to optics-based accelerators (unquantified) | Potentially low, due to inherent physics (unquantified) | Femtosecond pulse durations, potentially GHz operation rates | Analog (continuous spectral amplitudes) | Fig 2, Methods | Implicit | Processing power and energy/operation are qualitative inferences based on the general potential of optical computing. Frequency/response time are estimates based on ultrafast pulse durations. Bit-depth is analog, inferred from continuous spectral nature. |
| Mechanical Oscillator Layer | Multimode oscillations of metal plate | Moderate, comparable to linear classifiers (unquantified) | Moderate (speaker and microphone energy, unquantified) |  Oscillation frequencies in kHz range, response time in milliseconds range | Analog (continuous oscillation amplitudes) | Fig 4a-d, Methods | Implicit | Processing power and energy/operation are qualitative inferences based on demonstrated MNIST accuracy (linear classifier performance) and typical mechanical system energy scales. Frequency/response time are estimates based on mechanical oscillation frequencies. Bit-depth is analog, inferred from continuous oscillation nature. |
| Electronic Oscillator Layer | Nonlinear electronic oscillator circuit | Moderate, comparable to digital baselines (unquantified) | Moderate (circuit power, USB DAQ, unquantified) | Transient response times in microsecond to nanosecond range, potentially MHz operation rates | Analog (continuous voltage signals) | Fig 4e-h, Methods | Implicit | Processing power and energy/operation are qualitative inferences based on demonstrated MNIST accuracy (comparable to digital). Frequency/response time are estimates based on electronic circuit response times. Bit-depth is analog, inferred from continuous voltage signals. |

## M6: Temporal Dynamics
*   **Vector ID:** M6
*   **Vector Type:** Temporal

### **6.1 Timescales:**

*   **Vector ID:** M6.1
*   **Vector Type:** ParameterTable
    *   Table:
        | Timescale Description | Value | Units | Source | Implicit/Explicit | Justification |
        | :-------------------- | :---: | :---: | :----: | :----------------: | :------------: |
        | Optical pulse duration | ~100 | fs | Methods | Explicit |  Described in Methods for Ultrafast SHG experiments. |
        | Optical SHG process duration | Picoseconds | ps | Implicit | Typical timescale of SHG in mm-scale crystals. |
        | Electronic circuit response time | Nanoseconds to Microseconds | ns-μs | Implicit | Typical response times of RLC oscillator circuits at MHz frequencies. |
        | Mechanical plate oscillation period | Milliseconds | ms | Implicit | Audible frequencies driving the speaker, kHz range plate oscillations. |
        | Training epoch duration | Minutes to Hours | min-hr | Implicit | Training time is dependent on dataset size, network complexity and hardware. |

### **6.2 Active Inference:**

*   **Vector ID:** M6.2
*   **Vector Type:** Assessment
    *   Content: [No]
    *   Justification: The system does not exhibit active inference. Active inference involves a system predicting future states and acting to minimize prediction error based on an internal model. Here, the PNNs are trained to classify inputs based on backpropagation, which is a supervised learning method. The system is not building an internal model of its environment to predict future inputs or actively select actions to minimize surprise. It reacts to inputs by performing transformations learned during training to classify them, but this is reactive and discriminative, not predictive or actively inferential in the sense of minimizing surprise or prediction error in a dynamic environment.
    *   Implicit/Explicit: Implicit
        *  Justification: Active inference concepts are not mentioned in the paper. Lack of active inference is inferred from the supervised learning nature of backpropagation used in PAT, which focuses on input-output mapping for classification not environment modeling and surprise minimization characteristic of active inference frameworks.
    *   **If Yes/Partial, provide examples of testable CT-GIN metrics that *could* be used to quantify active inference:** N/A

## M7: Adaptation
*   **Vector ID:** M7
*   **Vector Type:** Adaptation

### **7.1 Adaptive Plasticity Presence:**

*   **Vector ID:** M7.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: Yes, the PNNs exhibit adaptive plasticity through the physics-aware training (PAT) process. The trainable parameters of the physical systems (optics, mechanics, electronics) are adjusted based on experience (training data) and feedback (error in classification). This adjustment leads to persistent changes in the system's internal structure (parameter values) and behavior (improved classification accuracy over time).  The system's functionality evolves from random to task-performing through this adaptive process, which is beyond simple stimulus-response and embodies genuine adaptation.
    *    Implicit/Explicit: Explicit
        * Justification: The entire paper is built upon demonstrating adaptive plasticity through the training process. The PAT algorithm and its effect of tuning physical system parameters for improved task performance are explicitly described and validated experimentally.

### **7.2 Adaptation Mechanism:**

*   **Vector ID:** M7.2
*   **Vector Type:** Description
    *   Content: The adaptation mechanism is Physics-Aware Training (PAT) using backpropagation. PAT is a hybrid in situ–in silico algorithm. In the forward pass, the physical system transforms input, producing an output. The error between the physical output and target output is calculated. A differentiable digital model estimates the gradient of the loss function with respect to the trainable physical parameters. Parameters are updated using stochastic gradient descent according to this gradient to minimize error. This iterative process adapts the physical system's parameters to improve task performance (classification accuracy). The adaptation can be likened to a form of gradient-based optimization in parameter space guided by physical system's responses.
    *   CT-GIN Mapping: Defines the `AdaptationNode` type: `adaptationType: Physics-Aware Training (PAT) using Backpropagation` and `Monad` edges representing iterative parameter updates within the training loop. The mechanism is a form of `Parameter Tuning`.
    *    Implicit/Explicit: Explicit
        *  Justification: The PAT algorithm and backpropagation method for adapting parameters are explicitly described in detail in the "Physics-aware training" section and Methods. The iterative, gradient-based nature of parameter updates is clearly articulated as the mechanism of adaptation.

## M8: Emergent Behaviors
*   **Vector ID:** M8
*   **Vector Type:** Behavior

### **8.1 Behavior Description:**

*   **Vector ID:** M8.1
*   **Vector Type:** Description
    *   Content: The main functional behavior is Machine Learning Classification. Specifically, the PNNs are trained and experimentally demonstrated to perform audio vowel classification and handwritten digit (MNIST) image classification. The system takes physical inputs encoding the data (vowel formant frequencies, pixel images) and outputs a classification decision (predicted vowel label, digit label) based on learned physical transformations. Observable behavior is the accurate classification of novel input data after training.
    *   CT-GIN Mapping: Defines the `BehaviorArchetypeNode`. Specify the type of behavior: `behaviorType: Machine Learning Classification`, subtypes: `Vowel Classification, MNIST Digit Classification`.
    *    Implicit/Explicit: Explicit
       *  Justification: Machine learning classification is explicitly stated as the purpose and demonstrated behavior of the PNN systems throughout the paper with experimental validation.

### **8.2 Behavior Robustness:**

*   **Vector ID:** M8.2
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The paper argues that PAT "combines the scalability of backpropagation with the automatic mitigation of imperfections and noise achievable with in situ algorithms."  Experimental results show successful training and classification despite noise and imperfections inherent in physical systems. Figure 3b demonstrates that PAT is robust enough to train SHG-PNN even when in silico training fails. The final accuracies (87-97%) reached in experiments, despite complexities of physical systems, indicate some robustness. However, the paper doesn't quantify robustness explicitly (e.g., noise tolerance levels, operational window sizes). Robustness is shown by comparing PAT to in silico training and by achieving functional classification in real physical systems, but quantitative robustness metrics are not provided.
    *   Implicit/Explicit: Mixed
        *  Justification: Robustness is qualitatively argued and experimentally implied by successful operation in noisy physical systems and comparison to in silico training (Explicit statements and Fig 3b). Quantitative metrics of robustness are absent (Implicit). Score is moderate because experimental success and comparison hint at robustness, but lack of direct robustness quantification limits the score.
    *   CT-GIN Mapping: e.g., This score contributes to the reliability attributes of the `BehaviorArchetypeNode`.

### **8.3 CT-GIN Emergent Behavior Validation**

*    **Vector ID:** M8.3
*    **Vector Type:** Validation
     *  Content: Validation of classification behavior is primarily through test set accuracy (Figs 2c, 3b, 3c, 4d, 4h, 4l).  Operational definitions are based on standard machine learning metrics (accuracy, confusion matrix). Control experiments include comparison to in silico training (Fig 3b, 3c) and digital baselines (Fig 4c, 4g, 4k). Quantitative analysis involves reporting classification accuracies and confusion matrices on test datasets. Reproducibility is indicated by consistent results across different physical systems and repeated experiments (e.g., error bars in Fig 3c). Limitations of validation are primarily in scope (vowel and MNIST classification only) and lack of systematic robustness testing beyond noise mitigation during PAT.
     *   Implicit/Explicit: Explicit
    *   Justification: Validation methods (test accuracy, confusion matrices, control experiments) are explicitly described through figures and text.  Standard machine learning validation practices are used and reported.

## M9: Cognitive Proximity
*   **Vector ID:** M9
*   **Vector Type:** Cognition

### **9.1 Cognitive Mapping:**

*   **Vector ID:** M9.1
*   **Vector Type:** Description
    *   Content: The paper draws an analogy between Deep Neural Networks (DNNs) and Deep Physical Neural Networks (PNNs) metaphorically linking their information processing to cognitive functions.  It is stated that "Just as deep learning realizes computations with deep neural networks made from layers of mathematical functions, our approach allows us to train deep physical neural networks made from layers of controllable physical systems..."  This is a functional analogy where PNN layers performing physical transformations are mapped to DNN layers performing mathematical operations, both enabling complex computation (classification).  Limitations are that this mapping is abstract and functional, not claiming biological cognitive equivalence. The paper primarily focuses on machine learning acceleration and functional device design potential, not direct cognitive emulation.
    *   CT-GIN Mapping: If a mapping exists, this defines a `CognitiveMappingEdge`. Specify source and target (`BehaviorArchetypeNode: Machine Learning Classification` to `CognitiveFunctionNode: Pattern Recognition`).
    *   Implicit/Explicit: Explicit
    * Justification: The analogy between DNNs and PNNs, and the link to deep learning (a field within AI which is metaphorically linked with cognitive functions), are explicitly drawn in the introduction. However it is also explicit that the aim is not to create a cognitive system per se, but a machine learning accelerator based on physical systems.

### **9.2 Cognitive Proximity Score:**

*   **Vector ID:** M9.2
*   **Vector Type:** Score
    *   Score: [2]
    *   Justification: Level 2: Sub-Organismal Responsivity. The PNN system exhibits basic forms of adaptation and plasticity through training to perform classification tasks. It goes beyond simple fixed stimulus-response behavior by learning from data and improving performance over time. However, it lacks complex representation, goal-directedness, contextual understanding, abstract reasoning, social cognition, or self-awareness (higher levels of the Cognizance Scale). The cognitive proximity is limited to pattern recognition achieved through a trained system, analogous to basic sensory discrimination or sub-organismal learning rather than more complex cognitive processes. The system's "intelligence" is in its engineered ability to perform classification via physical transformations, not in displaying more advanced cognitive attributes.
    *   Implicit/Explicit: Mixed
    *  Justification: The score justification is based on comparing the system's capabilities (classification learning) against the CT-GIN Cognizance Scale levels (Explicit scale criteria, Implicit placement of PNN within). The system's functionality is explicitly validated as classification, but its placement at level 2 is an interpretive assessment.

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
    | Sensing/Perception               | 3          | Physical systems act as sensors converting inputs (spectra, forces, voltages) to outputs. | `CognitiveFunctionNode: Sensing/Perception` | Explicit | Physical systems are used for input processing and conversion. |
    | Memory (Short-Term/Working)        | 4          | Parameters held during inference act as short-term working memory for transformation. | `CognitiveFunctionNode: Memory (Short-Term/Working)` | Implicit | Parameters are used in each forward pass, holding state temporarily. |
    | Memory (Long-Term)                 | 7          | Trained parameters represent long-term memory of learned classification rules.       | `CognitiveFunctionNode: Memory (Long-Term)` | Explicit | Trained parameters are persistent and define system function.  |
    | Learning/Adaptation              | 7          | PAT algorithm facilitates adaptation of physical system parameters via backpropagation. | `CognitiveFunctionNode: Learning/Adaptation` | Explicit | PAT explicitly shown to adapt parameters for task improvement. |
    | Decision-Making/Planning          | 2          | Classification is a basic form of decision-making. No planning or complex deliberation.   | `CognitiveFunctionNode: Decision-Making/Planning` | Implicit | Classification selects a category, a basic decision.  |
    | Communication/Social Interaction | 0          | No communication or social interaction capabilities are present or implied.         | N/A                                   | Explicit | Absence of communication features is clear from paper context. |
    | Goal-Directed Behavior            | 2          | Classification is a simple goal, but no complex goal hierarchy or goal switching.      | `CognitiveFunctionNode: Goal-Directed Behavior` | Implicit | Classification serves a predefined goal - limited context.   |
    | Model-Based Reasoning              | 1          | No evidence of internal models beyond trained parameters for direct input-output mapping. | `CognitiveFunctionNode: Model-Based Reasoning` | Implicit | No explicit model representation other than trained parameters. |
    | **Overall score**                 |      [3.375]       |                                                                                       |                                   |                     |                |

    *   **Note:** Assess the system for *each* function, providing a score (0-10) and a short (1-2 sentences) justification.  0 = Absent, 10 = Human-level performance.

## M10: Criticality Assessment
*   **Vector ID:** M10
*   **Vector Type:** Criticality

### **10.1 Criticality:**

*   **Vector ID:** M10.1
*   **Vector Type:** Assessment
    *   Content: [Unclear]
    *   Justification: The paper does not explicitly discuss criticality or whether the PNN systems operate near a critical point. While nonlinearities are crucial to the PNN's operation (e.g., nonlinear optics, nonlinear electronic oscillator), there's no analysis of scale-free behavior, power laws, or long-range correlations that would typically indicate criticality. The system is designed and trained to perform specific classification tasks, which does not inherently imply operation at a critical point although it cannot be excluded,  especially in complex physical systems like nonlinear optics and oscillating plates under driving forces. Without further analysis or data in the paper, criticality cannot be confirmed or refuted.
        *   Critical Parameters (If Yes/Partial): N/A
        *   Evidence: N/A
    *   Implicit/Explicit: Implicit
    *    Justification: Criticality is not mentioned.  Its presence is unclear because while nonlinearity exists, typical evidence of criticality is absent from the paper's analysis and descriptions. Assessment is based on lack of explicit discussion and typical criticality indicators.

## M11: Review Paper Specifics (Conditional)
N/A

## M12: Theoretical Paper Specifics (Conditional)
N/A

## M13: Overall Assessment & Scoring
*   **Vector ID:** M13
*   **Vector Type:** Overall

### **13.1 CT-GIN Readiness Score:**

*   **Vector ID:** M13.1
*   **Vector Type:** Score
*   **Calculated Score:** [5.69]

**CT-GIN Readiness Summary Table:**

| CT-GIN Aspect                   | Strength (Yes/Partial/No) | Key Supporting Metrics (with units) | Limitations (Missing Metrics/Data Gaps)                                           | Improvement Areas (Future Research)                                          |
| :------------------------------ | :-----------------------: | :-----------------------------------| :------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| Energy Flow Efficiency          |         Partial         |               N/A                  | Quantitative energy efficiency metrics (energy per operation, etc.)               |  Provide quantitative energy efficiency benchmarks compared to digital systems. |
| Memory Fidelity                 |           Yes           |          Classification Accuracy (%)   | Direct memory fidelity metrics (bit error rate, retention characterization)     | Characterize memory fidelity beyond classification accuracy.                  |
| Organizational Complexity       |            No           |                N/A                  | Evidence of self-organization or emergent structural order.                     | Explore self-organizing PNN architectures or components.                       |
| Embodied Computation            |           Yes           |          Classification Accuracy (%)   | Processing power, and granular energy per operation of physical units.           | Quantify processing power and energy efficiency of embodied computation.  |
| Temporal Integration            |           Partial         |         Relevant Timescales (fs, ps, ms) | Detailed analysis of temporal dynamics and control mechanisms.             | Analyze temporal dynamics in more detail, explore temporal coding.          |
| Adaptive Plasticity             |           Yes           |          Classification Accuracy (%)   | Detailed mechanism characterization beyond backpropagation description.          | Explore more complex adaptation mechanisms beyond PAT and backpropagation.   |
| Functional Universality         |         Partial         |      Demonstrated Classification Tasks    | Demonstration of wider range of tasks and problem types.                       | Demonstrate PNNs on broader set of computational tasks beyond classification. |
| Cognitive Proximity            |            No           |    Cognitive Proximity Score Level 2    | Evidence for higher-level cognitive functions and stronger cognitive mapping.  | Explore PNN architectures with potential for higher cognitive functions.      |
| Design Scalability & Robustness |         Partial         |          Classification Accuracy (%)   | Quantitative robustness metrics, scalability analysis to larger systems.         | Quantify robustness, explore scalability to larger PNN systems.               |
| **Overall CT-GIN Readiness Score** |           |   |   |      |


### **13.2 Qualitative CT-GIN Assessment Conclusion:**

*   **Vector ID:** M13.2
*   **Vector Type:** Textual Summary
    *   Content: The analyzed paper presents a significant advancement in material intelligence by demonstrating physics-aware training (PAT) to create deep physical neural networks (PNNs) using diverse physical systems (optics, mechanics, electronics). Key strengths include the clear experimental validation of PNNs for machine learning classification, the demonstration of adaptive plasticity through PAT, and the conceptual framework for embodied computation in physical systems. Key limitations arise from the lack of quantitative metrics for energy efficiency, memory fidelity beyond accuracy, and absence of self-organization within the engineered systems.  The cognitive proximity is low (Level 2) as the system primarily performs pattern recognition without exhibiting more advanced cognitive functions.  Overall assessment positions PNNs as a promising step towards energy-efficient and potentially faster machine learning hardware leveraging physical properties, but they are in early stages of CT-GIN readiness, particularly regarding organizational complexity, quantitative characterization of embodied computation, and higher cognitive functions.

### **13.3 CT-GIN Refinement Directions:**

*   **Vector ID:** M13.3
*   **Vector Type:** Recommendations
    *   *   Quantify energy efficiency: Rigorously measure and report energy consumption per operation and compare PNN efficiency to traditional digital hardware benchmarks for similar tasks.
    *   *   Characterize memory in detail: Provide metrics for memory retention, stability, write/read speed and energy cost, beyond classification accuracy.  Investigate the physical mechanisms of parameter storage and potential degradation.
    *   *   Explore self-organization: Investigate PNN architectures or constituent units that exhibit self-organization or emergent order from local interactions, potentially moving beyond purely engineered structures.
    *   *   Quantify embodied computation: Develop metrics to granularly assess the processing power and energy efficiency of unit physical transformations within PNNs.
    *   *   Analyze temporal dynamics: Explore and characterize the temporal dynamics of PNN operations in more detail, potentially exploiting temporal coding or recurrent architectures.
     *   *   Enhance cognitive functions: Investigate PNN architectures and training methods aimed at enabling higher-level cognitive functions beyond basic classification, exploring more complex representations and reasoning.
    *   *   Robustness and Scalability: Systematically quantify robustness to noise, imperfections, and parameter variations. Analyze scalability of PNN architectures to larger, more complex systems and tasks.

## M14: CT-GIN Knowledge Graph

*   **Vector ID:** M14
*   **Vector Type:** Visualization

### **14.1. CT-GIN Knowledge Graph:**
* **Content:**
[__Insert a schematic diagram of the CT-GIN Knowledge Graph. Use distinct shapes/colors for different CT-GIN node types (Energy, Memory, Configuration, Temporal, Behavior, Cognitive, Reliability). Use directed edges to represent relationships, labeled with CT-GIN edge types (Transduction, Transition, Adjunction, Coupling, Feedback, Temporal Evolution, Cognitive Mapping). Annotate nodes and edges with key attributes and parameters (with units!) extracted from the previous sections.__]

```mermaid
%% CT-GIN Knowledge Graph for "Deep physical neural networks trained with backpropagation"

graph LR
    subgraph Energy [Energy]
    EN_Input(EnergyInputNode) -- Transduction --> EN_Transduction
    EN_Transduction(EnergyTransductionEdge) -- Dissipation --> EN_Dissipation
    EN_Dissipation(EnergyDissipationNode)
    style EN_Input fill:#ccf,stroke:#333,stroke-width:2px
    style EN_Transduction fill:#cff,stroke:#333,stroke-width:2px
    style EN_Dissipation fill:#fcc,stroke:#333,stroke-width:2px
    end

    subgraph Memory [Memory]
    M_Memory(MemoryNode)
    style M_Memory fill:#cfc,stroke:#333,stroke-width:2px
    end

    subgraph Computation [Computation]
    COMP_Computation(ComputationNode)
    style COMP_Computation fill:#ffc,stroke:#333,stroke-width:2px
    end

    subgraph Behavior [Behavior]
    BEH_MLClassification(BehaviorArchetypeNode)
    style BEH_MLClassification fill:#fcf,stroke:#333,stroke-width:2px
    end

    subgraph Cognition [Cognition]
    COG_PatternRecognition(CognitiveFunctionNode)
    COG_ProxScore(CognitiveProximityScore)
    style COG_PatternRecognition fill:#eee,stroke:#333,stroke-width:2px
    style COG_ProxScore fill:#eee,stroke:#333,stroke-width:2px
    end


    EN_Input -- "Source: Laser/Amplifier/DAQ" --> EN_Transduction
    EN_Transduction -- "Mechanism: SHG/Oscillation/Circuit" --> COMP_Computation
    EN_Transduction -- "Efficiency: ~Medium" --> EN_Dissipation
    EN_Dissipation -- "Type: Optical/Mechanical/Electrical Losses" --> .->EN_Dissipation

    COMP_Computation -- "Type: Neuromorphic/Analog" --> M_Memory
    M_Memory -- "Type: Trainable Parameters" --> BEH_MLClassification
    BEH_MLClassification -- "Type: Machine Learning Classification" --> COG_PatternRecognition
    COG_PatternRecognition -- "Function: Pattern Recognition" --> COG_ProxScore
    COG_ProxScore -- "Score: 2" --> ..>COG_ProxScore


    classDef nodeFill fill:#f9f,stroke:#333,stroke-width:2px;
    classDef edgeStroke stroke:#777,stroke-width:1px;
    class EN_Input,EN_Transduction,EN_Dissipation,M_Memory,COMP_Computation,BEH_MLClassification,COG_PatternRecognition,COG_ProxScore nodeFill;
    class Transduction,Dissipation,Computation,Memory,Behavior,CognitiveMapping edgeStroke;
```

## M15: Relationship Vectors
*   **Vector ID:** M15
*   **Vector Type:** Relationships
*   Relationships:
        | Source Vector ID | Target Vector ID | Relationship Type |
        | ------------- | ------------- | ----------------- |
        | M2.1 | M2.2 | Transduction |
        | M2.2 | M5.1 | Computation |
        | M5.1 | M3.1 | Memory |
        | M3.1 | M8.1 | Behavior |
        | M8.1 | M9.1 | Cognitive Mapping |

## M16: CT-GIN Template Self-Improvement Insights

*   **Vector ID:** M16.1
*   **Vector Type:** Text
Provide specific, actionable feedback on the *CT-GIN template itself*, based on this analysis:
    *   **Missing Probes:**  Could benefit from probes explicitly asking for *scalability limits* of the system and *fabrication complexity*.  Also a probe for *noise characterization* in more detail, perhaps under M8.2 Behavior Robustness.
    *   **Unclear Definitions:** The distinction between 'Implicit' and 'Inferred' could be clearer. Perhaps 'Inferred' should be reserved for information derived from *outside* the publication altogether.  The "Yoneda Embedding Fulfillment Score" rubric in M4.7 needs to be defined. Rubric for "Memory Type" score (M3.2) could be more structured.
    *   **Unclear Node/Edge Representations:**  Guidance is generally sufficient, but clearer examples of mapping complex dynamic systems to CT-GIN graph would be helpful, especially for temporal dynamics.
    *   **Scoring Difficulties:** Cognitive Proximity Score is subjective and requires careful calibration to the scale.  Robustness score (M8.2) is also somewhat subjective without quantitative data.
    *   **Data Extraction/Output Mapping:**  Template is comprehensive, but for some detailed experimental papers, extracting all relevant parameters into tables can be time-consuming and require careful reading. Potentially consider 'bulk data upload' options for some table fields in future template versions.
    *   **Overall Usability:** Template structure is logical and comprehensive.  Using Markdown format is good for readability and editing. It's quite detailed, which is good for thorough analysis but can be lengthy for simpler systems or papers with less explicit detail on all CT-GIN aspects. Consider optional 'summary' sections for each module.
    * **Specific Suggestions:**
        * Add probes for "Scalability Limits", "Fabrication Complexity", and more detailed "Noise Characterization".
        * Refine 'Implicit' vs 'Inferred' distinction; define 'Inferred' more strictly as external knowledge based.
        * Define rubric for "Yoneda Embedding Fulfillment Score" (M4.7) and improve rubric for "Memory Type" (M3.2).
        * Provide more examples of CT-GIN graph mapping for dynamic and temporal systems.
        * Potentially add 'summary' sections per CT-GIN Module for conciseness.