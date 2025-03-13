# Hydrodynamic pursuit by cognitive self-steering microswimmers

__Paper Type:__ Theoretical/Computational

## M1: System Overview & Implementation
*   **Vector ID:** M1
*   **Vector Type:** Overview

### **1.1 System Description**

*   **Vector ID:** M1.1
*   **Vector Type:** Description
    *   Content: The system is a theoretical/computational model of a pursuer-target pair of microswimmers in a fluid. Both pursuer and target are modeled as spherical squirmers, but the pursuer is equipped with a cognitive self-steering mechanism. This mechanism allows the pursuer to adapt its propulsion direction and speed based on the target's position or propulsion direction. The system investigates two hydrodynamic steering strategies: reorientation toward the target's position and alignment with the target's propulsion direction combined with speed adaptation. The purpose is to analyze the emergent cooperative motion and pursuit strategies of these microswimmers in a low-Reynolds-number fluid environment, considering hydrodynamic interactions and thermal noise.
    *   CT-GIN Mapping: `SystemNode` attributes: `systemType: Microswimmer Pursuit Model`, `domain: Physics/Fluid Dynamics`, `mechanism: Hydrodynamic Steering, Cognitive Response`, `components: Pursuer Squirmer, Target Squirmer, Fluid Environment`, `purpose: Investigate Pursuit Strategies and Cooperative Motion`
    *   Implicit/Explicit: Explicit
        *  Justification: The system description is explicitly stated in the abstract and introduction sections of the paper, outlining the model components, steering mechanisms, and research objectives.

### **1.2 Implementation Clarity**

*   **Vector ID:** M1.2
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The implementation is relatively clear for a theoretical/computational paper. The squirmermodel and steering strategies are described mathematically, and the simulation method (Multiparticle Collision Dynamics) is mentioned with references. However, specific details of the numerical implementation, such as the exact parameters used in MPC simulations and boundary conditions, are not exhaustively detailed in the main excerpt, requiring reference to the methods section and supplementary materials for full clarity. The cognitive aspect is simplified to adaptation rules, making the "cognitive" label somewhat metaphorical, which is adequately clarified in the text by contrasting it with more complex cognitive systems.
    *   Implicit/Explicit: Mixed
        * Justification: The overall approach and key equations are explicit. The finer details of numerical implementation are implicit within the methods section and references, requiring some inference to fully understand the complete implementation.

### **1.3 Key Parameters**

*   **Vector ID:** M1.3
*   **Vector Type:** ParameterTable
    *   Table:
        | Parameter Name | Value | Units | Source (Fig/Table/Section) | Implicit/Explicit | Data Reliability (High/Medium/Low) | Derivation Method (if Implicit) |
        | :------------- | :---: | :---: | :-----------------------: | :-----------------: | :-----------------------------: | :-------------------------------: |
        | Péclet number (Pe) | 8, 32, 128 | N/A | Eq. (2), Figs. 2, 3, 4, 5 | Explicit | High | N/A |
        | Maneuverability (Ω) | Variable (32-128) | N/A | Eq. (2), Figs. 2, 3, 4, 5 | Explicit | High | N/A |
        | Speed ratio (α) | Variable (0-1.8) | N/A | Figs. 2, 3, 4 | Explicit | High | N/A |
        | Squirmer Diameter (σ) | N/A | m (inferred) | Eq. (2), Figs. 1, 2, 3, 4, 5 | Implicit | Medium | Typical microswimmer scale |
        | Active stress parameter (β) | ±3 | N/A | Figs. 2, 3 | Explicit | High | N/A |

    *   **Note:** Key parameters are explicitly mentioned and varied in the study to explore their influence on pursuit behavior. Squirmer diameter is inferred to be in the micrometer range, typical for microswimmers, although not explicitly stated with a numerical value.

## M2: Energy Flow
*   **Vector ID:** M2
*   **Vector Type:** Energy

### **2.1 Energy Input**

*   **Vector ID:** M2.1
*   **Vector Type:** Input
    *   Content: The energy input is the active driving of the microswimmers provided by the imposed surface flow field (slip velocity). This represents the energy source for self-propulsion. In the context of simulations, this is modeled by setting the squirmer parameters related to propulsion (C<sub>0</sub> and C<sub>1</sub>).
    *   Value: N/A (Model parameter, not a physical input in simulation)
    *   Units: N/A
    *   CT-GIN Mapping: `EnergyInputNode`: attributes - `source: Active Surface Flow Field`, `type: Mechanical`
    *   Implicit/Explicit: Implicit
        *  Justification: While not explicitly labelled "energy input," the text describes the squirmers as "self-propelled by an imposed surface flow field" and details the parameters that define the propulsion (C<sub>0</sub>, C<sub>1</sub>, β). This surface flow is the source of motion and requires energy to be sustained in a real system.

### **2.2 Energy Transduction**

*   **Vector ID:** M2.2
*   **Vector Type:** Transduction
    *   Content: The energy transduction is from the imposed surface flow field to the kinetic energy of the fluid and the microswimmers. The surface slip velocity, defined by Legendre polynomials, generates fluid flow around the squirmers, leading to their propulsion and motion. The adaptation of motion (steering) further transduces the active driving force into directed motion towards or alignment with the target.
    *   CT-GIN Mapping: `EnergyTransductionEdge`: attributes - `mechanism: Hydrodynamic Propulsion, Steering Adaptation`, `from_node: EnergyInputNode`, `to_node: Kinetic Energy (Fluid & Microswimmers)`
    *   Implicit/Explicit: Implicit
        *  Justification: The energy transduction is implied by the description of squirmer propulsion and steering. The paper focuses on hydrodynamic interactions and motion resulting from the surface flow field, which implicitly represents energy conversion into kinetic energy.

### **2.3 Energy Efficiency**

*   **Vector ID:** M2.3
*   **Vector Type:** Score
    *   Score: [5]
    *   Justification/Metrics:  The paper does not explicitly quantify energy efficiency. However, the simulations are performed in a low-Reynolds number regime, where viscous dissipation is dominant. Thus, the energy transduction is expected to be moderately efficient in terms of converting surface flow energy into directed motion, given the constraints of low Reynolds number physics and thermal fluctuations.  A score of 5 reflects a moderate qualitative assessment, acknowledging energy losses due to viscosity and thermal noise but also the directed propulsion achieved.
    *   CT-GIN Mapping: Attribute of `EnergyTransductionEdge`s: `efficiency_score: 5`
    *   Implicit/Explicit: Implicit
      *  Justification:  Efficiency is not directly calculated, but is qualitatively assessable as moderate due to the nature of low Reynolds number hydrodynamics and the focus on directed motion.

### **2.4 Energy Dissipation**

*   **Vector ID:** M2.4
*   **Vector Type:** Dissipation
    *   Content: The primary energy dissipation mechanism is viscous friction in the fluid.  Low Reynolds number regime implies that energy input is largely dissipated into heat due to viscosity. Thermal fluctuations are also present, representing further dissipation and randomization of motion at the microscale. The hard-core repulsion between squirmers, though not directly dissipative, contributes to altering flow fields and thus indirectly affecting energy dissipation patterns.  Quantification of energy dissipation is not provided.
    *   CT-GIN Mapping: Creates `EnergyDissipationNode`: attributes - `mechanism: Viscous Friction, Thermal Fluctuations`; `EnergyDissipationEdge`: attributes - `from_node: Kinetic Energy`, `to_node: Heat, Random Motion`
    *    Implicit/Explicit: Implicit
        *  Justification: Viscous dissipation is inherent in low-Reynolds number hydrodynamics and is mentioned as a characteristic of the system context. Thermal fluctuations are also explicitly included in the model. However, no explicit quantification of dissipated energy is given.

## M3: Memory
*   **Vector ID:** M3
*   **Vector Type:** Memory

### **3.1 Memory Presence:**

*   **Vector ID:** M3.1
*   **Vector Type:** Binary
    *   Content: No
    *   Justification: The system lacks explicit memory in the sense of persistent change in internal state influencing future behavior beyond the immediate adaptation rules. The pursuer's steering is reactive and based on the instantaneous relative position or orientation of the target. While the pursuer adapts its motion, this adaptation is not a form of memory retention but ongoing response to real-time input. There is no storage of past experiences or states that would alter future interactions beyond the defined adaptation rules. The model is Markovian in its approach to steering, reacting to the current sensor input without a historical dependency beyond the current state variables (positions and orientations).
    *    Implicit/Explicit: Explicit
        * Justification: The system is described as reacting and adapting in real-time, based on the current environment. No mechanism for storing past states or experiences to influence future actions is described. The focus is on immediate response, not on learning or historical influence.

## M4: Self-Organization and Emergent Order
*   **Vector ID:** M4
*   **Vector Type:** Self-Organization

### **4.1 Self-Organization Presence:**

*   **Vector ID:** M4.1
*   **Vector Type:** Binary
    *   Content: Yes
    *   Justification:  Stable cooperative states between pursuer and target emerge from local hydrodynamic interactions and the pursuer's steering rules. These states, such as head-to-tail configurations for pullers and leader-follower arrangements for pushers, are not pre-programmed but arise spontaneously from the interactions between individual components (squirmers) and their adaptation behaviors. The global order (cooperative motion, stable pair configurations) emerges from the local rules of hydrodynamic interaction and steering, without external control dictating the final configuration of the pair. The specific configuration achieved is dependent on parameters like speed ratio and maneuverability, highlighting the emergent nature.
    *   Implicit/Explicit: Explicit
        *  Justification:  The paper explicitly discusses "emergent cooperative states" and emphasizes that these states arise from the interplay of hydrodynamic interactions and self-steering mechanisms. The results section details different emergent configurations (head-to-tail, side-by-side, leader-follower) that are outcomes of these local interactions rather than pre-designed global structures.

**(Conditional: If M4.1 is "Yes", include M4.2-M4.7)**

### **4.2 Local Interaction Rules:**

*   **Vector ID:** M4.2
*   **Vector Type:** Rules
    *   Content:
        1.  **Hydrodynamic Interaction:** Squirmers interact through fluid. The fluid dynamics is modeled by multiparticle collision dynamics, capturing fluctuating hydrodynamics. Squirmers generate flow fields described by Legendre polynomials, with strength determined by parameter β (puller/pusher type).
        2.  **Pursuer Steering (Reorientation toward target position):** Angular velocity ω<sub>0</sub> to redirect pursuer's propulsion direction e<sub>p</sub> toward desired direction e<sub>aim</sub> (target position e<sub>c</sub>) is given by: ω<sub>0</sub> = C<sub>0</sub> (e<sub>p</sub> × e<sub>aim</sub>), where C<sub>0</sub> controls actuation strength. e<sub>aim</sub> = e<sub>c</sub> = r<sub>c</sub> / |r<sub>c</sub>|, where r<sub>c</sub> is the vector from pursuer to target.
        3.  **Pursuer Steering (Alignment with target propulsion + Speed adaptation):**  Desired direction e<sub>aim</sub> is target's propulsion direction e<sub>t</sub>, i.e., e<sub>aim</sub> = e<sub>t</sub>. Speed adaptation mechanism (described in Methods section and Eq. (19), (22), but not detailed in the excerpt) adjusts pursuer speed v<sub>p</sub> based on e<sub>p</sub> ⋅ e<sub>c</sub>: accelerates if behind target (e<sub>p</sub> ⋅ e<sub>c</sub> < 0), decelerates if in front (e<sub>p</sub> ⋅ e<sub>c</sub> > 0), limited by max speed v<sub>max</sub>.
        4.  **Steric Repulsion:**  Hard-core repulsion between squirmers, modeled by separation-shifted Lennard-Jones potential to prevent overlap.

    *   CT-GIN Mapping: Part of the `AdjunctionEdge` description (local side). These define the "LocalInteraction" category of edges. `InteractionRuleNode` attributes: `ruleType: Hydrodynamic Interaction`, `ruleType: Reorientation Steering Rule`, `ruleType: Alignment Steering Rule`, `ruleType: Steric Repulsion`. Edges are defined between `SquirmerNode` and `FluidNode`, and control nodes for steering.
    * **Implicit/Explicit**: Explicit
        *  Justification:  The local interaction rules are explicitly described through mathematical equations (steering rules, implicitly hydrodynamic equations through reference to MPC and squirmer model) and qualitative descriptions (steric repulsion). The steering rules are operationally defined by Eqs. (1) and (13), (14) and the adaptation mechanism is described in the Methods section, although details of speed adaptation are less explicit in the excerpt itself.

### **4.2.1 Local Interaction Parameters:**

* **Vector ID:** M4.2.1
* **Vector Type:** Table
*   Table:
    | Rule ID | Description | Parameter Name | Parameter Value Range | Units | Data Source | Implicit/Explicit | Justification |
    | :------ | :---------- | :------------- | :---------- | :---: | :----------: | :----------------: | :------------: |
    | 1 | Hydrodynamic Interaction (Squirmer Model) | β (stresslet parameter) | -3, 3 | N/A | Figs. 2, 3 | Explicit | Directly varied in simulations |
    | 1 | Hydrodynamic Interaction (Fluid Viscosity) | η | 111.3 mk<sub>B</sub>T/a<sup>2</sup> | MPC units | Methods Section | Implicit | Parameter of MPC fluid model, value from Methods Section |
    | 2, 3 | Steering Actuation Strength | C<sub>0</sub> | N/A | N/A | Eq.(1) | Explicit | Parameter in steering rule equations |
    | 3 | Speed Adaptation Strength | κ | N/A | N/A | Eq. (19) | Explicit | Parameter in speed adaptation equation |
    | 3 | Max Pursuer Speed (for speed adaptation) | v<sub>max</sub> | Variable (v<sub>t</sub> to 2.3v<sub>t</sub>) | m/s (inferred) | Fig. 4 | Explicit | Varied in Fig 4, relative to target speed |
### **4.3 Global Order:**

*   **Vector ID:** M4.3
*   **Vector Type:** Order
    *   Content:  The emergent global orders are stable cooperative motion states. These include:
        1.  **Stable pursuer-target pairs (straight trajectory):** For pullers, head-to-tail configurations and touching pairs emerge. For pushers, leader-follower arrangements with finite average distance are seen. Stability depends on speed ratio (α) and maneuverability (Ω).
        2.  **Stable pursuer-target pairs (helical trajectory):** Pursuer follows the target on a helix with a modified radius and pitch. For pullers and ABPs, touching configurations are observed. For pushers, stable cooperative swimming despite hydrodynamic repulsion.
        3.  **Cooperative circular motion (alignment + speed adaptation):** Pushers exhibit stable cooperative circular motion with speed adaptation, where the pursuer circles the target. Radius of circular motion depends on max pursuer speed v<sub>max</sub>.

    *   CT-GIN Mapping: Defines a `ConfigurationalNode`. `ConfigurationNode` attributes: `orderType: Stable Pair Configuration (Straight Trajectory), orderType: Stable Pair Configuration (Helical Trajectory), orderType: Cooperative Circular Motion`, `configurationDetails: Head-to-tail pullers, leader-follower pushers, helical pursuer-target, circular pusher-target`.
    * **Implicit/Explicit**: Explicit
        *  Justification:  The emergent global orders are explicitly described in the Results section, with figures and supplementary movies illustrating these stable configurations and cooperative motions for different scenarios (straight/helical target, puller/pusher, different steering strategies).

### **4.4 Predictability of Global Order:**

*   **Vector ID:** M4.4
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The emergence of stable cooperative states is reasonably predictable given the system parameters (Pe, Ω, α, β) and chosen steering strategy. Phase diagrams (Fig. 2e) and parameter-dependent plots (Figs. 2b, 3c, 4c, 5e) demonstrate how the type and stability of emergent order depend on these parameters, indicating a level of predictability. However, thermal noise and complex hydrodynamic interactions introduce stochasticity, reducing perfect predictability. The system exhibits statistical predictability in terms of average distances, alignment, and stability regions, rather than deterministic outcomes for each individual trajectory. The far-field approximations (Eqs. 3, 4, 5) provide semi-quantitative agreement with simulation results, indicating some theoretical predictability.
    * **Implicit/Explicit**: Mixed
    *  Justification:  The paper demonstrates predictability through parameter-dependent simulations and semi-quantitative agreement with theoretical approximations, showing trends and statistical averages are predictable. However, the inherent stochasticity from thermal noise and complexity of hydrodynamic interactions limits perfect predictability of individual system behaviors, making it a mixed explicit and implicit justification.

### **4.5. Local Interaction Rules (for Self-Organization)**
* **Vector ID:** M4.5
* **Vector Type:** Table
*   Table:
| Rule ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Source |
| :------ | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :-----: |
| 1 | Reorientation Steering Rule | C<sub>0</sub> | N/A | N/A | Explicit | Actuation Strength | Eq. (1) |
| 2 | Alignment Steering Rule | C<sub>0</sub> | N/A | N/A | Explicit | Actuation Strength | Eq. (1) |
| 3 | Speed Adaptation (Pusher) | κ | N/A | N/A | Explicit | Friction coefficient | Eq. (19) |
| 3 | Speed Adaptation (Pusher) | v<sub>max</sub> | Variable (v<sub>t</sub> to 2.3v<sub>t</sub>) | m/s (inferred) | Explicit | Max speed limit  | Fig. 4 |

### **4.6. Globally Emergent Order and Order Parameters**
* **Vector ID:** M4.6
* **Vector Type:** Table
*   Table:
| Property ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Protocol | Source |
| :---------- | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :------: | :-----: |
| 1 | Average Pursuer-Target Distance (straight traj. pushers) | 〈r<sub>c</sub>〉 | Variable | σ | Explicit |  Quantitative metric of configuration | Averaged over simulations | Fig. 2b |
| 2 | Center-of-Mass Speed | U<sub>cm</sub> | Variable | v<sub>p</sub> | Explicit | Quantitative metric of cooperative motion | Averaged over simulations | Fig. 2c |
| 3 | Alignment Parameter | 〈e<sub>p</sub>⋅e<sub>t</sub>〉 | Variable [-1, 1] | N/A | Explicit | Metric of propulsion direction alignment  | Averaged over simulations | Fig. 2d |
| 4 | Order Parameter (helical traj.)  | 〈e<sub>p</sub>⋅e<sub>t</sub>〉 | Variable [-1, 1] | N/A | Explicit | Metric of propulsion direction in helical pursuit | Averaged over simulations | Fig. 3b |
| 5 | Mean Pursuer-Target Distance (helical traj.) | 〈r<sub>c</sub>〉 | Variable | σ | Explicit | Quantitative metric in helical pursuit | Averaged over simulations | Fig. 3c |

### **4.7 Yoneda Embedding and Local-to-Global Mapping Fidelity**

*   **Vector ID:** M4.7
*   **Vector Type:** Table
*   Table:
    | Link Type | Description | Predictability | Yoneda Score | Metrics | Implicit/Explicit | Justification | Source |
    | :-------- | :---------- | :------------- | :----------- | :------ | :----------------: | :------------: | :-----: |
     | Local Steering Rules -> Global Cooperative Motion | How well steering rules predict emergent configurations | Moderate | 6 | Qualitative agreement with far-field approximations; Parameter-dependent phase diagrams and plots show trends, but noise exists | Mixed | Predictability is statistical, not deterministic, due to noise and complexity. Far-field theory provides some predictive power. | Figs. 2, 3, 4, 5, Supplementary Note 1 |
    *   **Yoneda Embedding Fulfillment Score [0-10]:** [Score: 6.  Rubric: 0 = No relation between local rules and global order; 5 = Qualitative relationship visible; 10 = Precise, quantitative, and fully predictable mapping. Score of 6 reflects that a discernible, statistically predictable relationship exists, supported by some theoretical approximations, but with limitations due to stochasticity.]
    *   **Metrics:**  [Phase diagrams showing stability regions, Plots of order parameters (distance, alignment) vs. system parameters, Semi-quantitative agreement with far-field hydrodynamic approximations.]
    *   **Justification:** [The Yoneda score of 6 reflects a moderate degree of mapping fidelity. Local steering rules and hydrodynamic interactions significantly influence the emergent global order, as evidenced by parameter-dependent phase diagrams and order parameters.  Far-field approximations offer some theoretical linking, but the stochastic nature introduced by thermal noise and the complexity of near-field hydrodynamic effects reduce the mapping to a statistical predictability rather than a perfectly deterministic one. Therefore, while a relationship is clear and demonstrable, it’s not a fully precise and deterministic embedding.]

## M5: Computation
*   **Vector ID:** M5
*   **Vector Type:** Computation

### **5.1 Embodied Computation Presence:**

*   **Vector ID:** M5.1
*   **Vector Type:** Binary
    *   Content: Yes
    *   Justification:  Embodied computation is present in a minimal form. The steering mechanism acts as a simple form of computation. The pursuer "computes" a desired angular velocity (ω<sub>0</sub>) based on the relative position (reorientation strategy) or relative orientation (alignment strategy) of the target. This computation is embodied in the physics of the squirmer's response to the steering rule.  The adaptation logic to adjust speed based on relative position in the alignment + speed adaptation scheme also constitutes a minimal embodied computation. These "computations" are not performed by a separate processor but are intrinsically linked to the physical actuation and response of the microswimmer model.
    *    Implicit/Explicit: Mixed
        *  Justification: The paper uses the term "cognitive" and describes "steering strategies" implying a form of information processing and decision making, albeit very simplified.  The steering rules (Eq. 1) and speed adaptation (Eq. 19, 22) represent computational steps physically embodied in the model's dynamics. The "cognition" is minimal and metaphorical, but the steering adaptation is functionally a form of embodied computation.

**(Conditional: If M5.1 is "Yes", include M5.2-5.4)**

### **5.2 Computation Type:**

*   **Vector ID:** M5.2
*   **Vector Type:** Classification
    *   Content: Analog
    *   CT-GIN Mapping: Defines the `ComputationNode` type. `ComputationNode` attributes: `computationType: Analog`
    *    Implicit/Explicit: Implicit
    *    Justification: The steering and speed adaptation are analog operations. The angular velocity adjustment is proportional to the cross product of direction vectors (reorientation) or based on the scalar product of direction vectors (alignment + speed adaptation). Speed adaptation is a continuous time process governed by differential equations. These are not discrete or digital operations but continuous adaptations based on input signals.

### **5.3 Computational Primitive:**

*   **Vector ID:** M5.3
*   **Vector Type:** Function
    *   Content:
        1.  **Vector Cross Product (for reorientation steering):**  e<sub>p</sub> × e<sub>aim</sub>. This operation "computes" the direction of rotation needed to align e<sub>p</sub> with e<sub>aim</sub>. The magnitude is proportional to the sine of the angle between the vectors.
        2.  **Vector Scalar Product (for speed adaptation in alignment strategy):** e<sub>p</sub> ⋅ e<sub>c</sub>. This computes the relative position component along the pursuer's direction, used to adjust speed (accelerate or decelerate).
        3.  **Proportional Control (for steering and speed adaptation):**  The angular velocity ω<sub>0</sub> and speed change v_<sub>p</sub> are proportional to the computed vector products, implementing a proportional control mechanism for steering and speed adaptation.

    *   **Sub-Type (if applicable):** (Vector Cross Product, Vector Scalar Product, Proportional Control)
    *   CT-GIN Mapping: Defines the primary function of the `ComputationNode`. `ComputationNode` attributes: `primitiveFunction: Vector Cross Product, primitiveFunction: Vector Scalar Product, primitiveFunction: Proportional Control`
    *   Implicit/Explicit: Explicit
    * Justification: The computational primitives are directly derived from the equations defining the steering strategies and speed adaptation mechanism (Eq. (1), (13), (14), (19), (22)). Vector products and proportional control are the fundamental operations embodied in these rules.

### **5.4 Embodied Computational Units**
* **Vector ID:** M5.4
* **Vector Type:** Table
*   Table:
| Unit ID | Description | Processing Power | Energy/Operation | Freq/Resp. Time | Bit-Depth | Data Source | Implicit/Explicit | Justification |
| :------ | :---------- | :--------------- | :--------------- | :--------------: | :-------: | :----------: |:-----------------:| :-----------------:|
| 1 | Steering Actuation | N/A (Analog) | N/A (Analog) | Rotational Diffusion Time Scale (D<sub>R</sub><sup>-1</sup>) | N/A (Analog) | Eq. (2) | Implicit |  Processing power and energy are not quantified in bit operations as it's analog. Response time is related to maneuverability and rotational diffusion. Bit-depth N/A for analog. |
| 2 | Speed Adaptation | N/A (Analog) | N/A (Analog) |  Speed Relaxation Time (R<sub>sq</sub>/κv<sub>max</sub>) | N/A (Analog) | Eq. (20) | Implicit | Processing power and energy are not quantified in bit operations as it's analog. Response time estimated from speed adaptation equations. Bit-depth N/A for analog. |

## M6: Temporal Dynamics
*   **Vector ID:** M6
*   **Vector Type:** Temporal

### **6.1 Timescales:**

*   **Vector ID:** M6.1
*   **Vector Type:** ParameterTable
    *   Table:
        | Timescale Description | Value | Units | Source | Implicit/Explicit | Justification |
        | :-------------------- | :---: | :---: | :----: | :----------------: | :------------: |
        | Rotational Diffusion Time | D<sub>R</sub><sup>-1</sup> | s (inferred) | Eq. (2) | Implicit |  Characteristic timescale for random rotational motion. D<sub>R</sub> defined in Eq. (2). Units inferred from typical microswimmer context |
        | Maneuverability Timescale | Ω<sup>-1</sup>D<sub>R</sub> | s (inferred) | Eq. (2) | Implicit | Timescale of active reorientation. Defined by maneuverability Ω and rotational diffusion. Units inferred. |
        | Péclet Number Timescale (Advection) | σ/v<sub>p</sub> | s (inferred) | Eq. (2) | Implicit | Timescale for advection over squirmer diameter. Pe = v<sub>p</sub>σ/D<sub>R</sub>. Units inferred. |
        | Speed Adaptation Relaxation Time | R<sub>sq</sub>/(κv<sub>max</sub>) | s (inferred) | Eq. (20) | Implicit | Timescale for pursuer speed to adapt to target position in alignment strategy. Units inferred. |
    *   **Note:** Timescales are derived from the parameters defined in the paper and typical physical interpretations for microswimmer dynamics. Explicit numerical values with SI units are not provided in the excerpt, necessitating qualitative assessment and inferred units based on typical microscale systems.

### **6.2 Active Inference:**

*   **Vector ID:** M6.2
*   **Vector Type:** Assessment
    *   Content: No
    *   Justification: The system does not exhibit active inference.  There is no evidence of: (1) prediction of future states, (2) action selection to minimize discrepancies between predictions and actual states, or (3) internal models updated by experience. The pursuer reacts instantaneously to the perceived current state of the target based on simple, predefined steering rules. There is no internal model of the target's behavior or environment, and the pursuer's actions are not based on minimizing prediction error.  The steering is purely reactive and not anticipatory or model-based, lacking the core components of active inference.
    *   Implicit/Explicit: Explicit
        *  Justification: The description of the steering and speed adaptation mechanisms highlights a reactive nature, based on current sensory input.  The model lacks any predictive component or internal model of the environment; actions are not chosen to minimize future surprise.  The focus is on immediate pursuit, not prediction-based behavior.
    *   **If Yes/Partial, provide examples of testable CT-GIN metrics that *could* be used to quantify active inference:** [N/A]

## M7: Adaptation
*   **Vector ID:** M7
*   **Vector Type:** Adaptation

### **7.1 Adaptive Plasticity Presence:**

*   **Vector ID:** M7.1
*   **Vector Type:** Binary
    *   Content: Yes
    *   Justification: The system exhibits adaptive plasticity in its propulsion direction and, for one strategy, in its speed. The pursuer *changes its behavior* (direction, speed) in response to the target's presence and trajectory.  This is *beyond* simple stimulus-response because the pursuer's motion is *continuously adjusted* based on real-time feedback from the target. While not learning in a richer sense, the continuous adaptation of motion parameters based on the target's state constitutes a form of adaptive plasticity in the system's behavior.  The steering and speed adaptation rules are fixed, but the *resulting behavior* of pursuit is dynamically adapted to the target's trajectory.
    *    Implicit/Explicit: Mixed
        * Justification: The paper highlights "adaptation of the pursuer’s rotational motion" and "speed adaptation," explicitly using adaptation terms. The steering rules themselves are pre-defined, but their *application* leads to dynamically changing behavior that is plastic in response to the target's movement. This is a form of behavioral plasticity, although not structural or learning-based plasticity.

**(Conditional: If M7.1 is "Yes", include M7.2)**

### **7.2 Adaptation Mechanism:**

*   **Vector ID:** M7.2
*   **Vector Type:** Description
    *   Content: The adaptation mechanism is based on feedback-controlled adjustment of the pursuer's propulsion direction and speed:
        1.  **Reorientation Steering:** Feedback from the target's relative position (vector r<sub>c</sub>) drives adaptation of pursuer's orientation. The angular velocity ω<sub>0</sub> is adjusted proportionally to the cross product (e<sub>p</sub> × e<sub>aim</sub>), which provides feedback to continuously reorient e<sub>p</sub> toward e<sub>aim</sub> (target position). This is a form of proportional feedback control.
        2.  **Alignment Steering with Speed Adaptation:**  Feedback from the target's relative position (e<sub>p</sub> ⋅ e<sub>c</sub>) drives speed adaptation. If behind target (e<sub>p</sub> ⋅ e<sub>c</sub> < 0), speed increases; if ahead (e<sub>p</sub> ⋅ e<sub>c</sub> > 0), speed decreases, capped by v<sub>max</sub>. This is also a feedback mechanism, adjusting speed based on relative positioning regarding the target, combined with alignment of propulsion directions.

        The change is driven by environmental signals (target position/orientation) and implemented through pre-defined feedback rules (Eqs. 1, 13, 14, 19, 22). It's closer to parameter tuning or reactive control than sophisticated learning mechanisms like Hebbian or reinforcement learning.
    *   CT-GIN Mapping: Defines the `AdaptationNode` type and `Monad` edges. `AdaptationNode` attributes: `adaptationMechanism: Proportional Feedback Control (Orientation), adaptationMechanism: Proportional Feedback Control (Speed)`. `Monad` edges connect `AdjunctionEdge` (Local Interactions) to `BehaviorArchetypeNode` (e.g., Locomotion), indicating how local rules adapt behavior. Type of adaptation mechanism: "Proportional Feedback Control".
    *    Implicit/Explicit: Explicit
        *  Justification: The adaptation mechanisms are explicitly detailed by the descriptions of the steering strategies and the speed adaptation rule, including the feedback variables (relative position, relative orientation) and the proportional control nature of the adaptation. The equations (1, 13, 14, 19, 22) operationally define these feedback mechanisms.

## M8: Emergent Behaviors
*   **Vector ID:** M8
*   **Vector Type:** Behavior

### **8.1 Behavior Description:**

*   **Vector ID:** M8.1
*   **Vector Type:** Description
    *   Content: The main functional behaviors are hydrodynamic pursuit and stable cooperative motion between pursuer and target microswimmers. Specific observable behaviors include:
        1.  **Target Capture (Pullers, Reorientation Strategy):** Pursuer approaches and maintains close proximity (touching) to the target for puller type squirmers with reorientation steering.
        2.  **Stable Leader-Follower Motion (Pushers, Reorientation Strategy):** Pursuer follows target at a finite average distance for pusher squirmers with reorientation steering.
        3.  **Stable Cooperative Helical Motion (Helical Target Trajectory):** Pursuer and target move together on helical trajectories.
        4.  **Stable Cooperative Circular Motion (Pushers, Alignment & Speed Adaptation):** Pursuer and target move together in a circular trajectory, especially for pushers with alignment steering and speed adaptation.

    *   CT-GIN Mapping: Defines the `BehaviorArchetypeNode`. `BehaviorArchetypeNode` attributes: `behaviorType: Pursuit, behaviorType: Cooperative Motion, behaviorType: Target Capture, behaviorType: Leader-Follower Motion, behaviorType: Helical Motion, behaviorType: Circular Motion`. Specificity indicated through attributes.
    *    Implicit/Explicit: Explicit
       *  Justification: The behaviors are explicitly described in the Results section with clear labels such as "stable cooperative states," "pursuit," "target capture," "leader-follower," and descriptions of motion patterns (helical, circular). These are directly observable outcomes of the simulations and are presented as the main findings.

### **8.2 Behavior Robustness:**

*   **Vector ID:** M8.2
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The emergent behaviors exhibit moderate robustness.  The stability of pursuit and cooperative motion is shown to be dependent on parameters (Pe, Ω, α), indicating operational windows but also sensitivity to parameters. The system is simulated with thermal noise included through the MPC fluid model, suggesting robustness against thermal fluctuations to a degree, particularly at higher maneuverability (Ω). Figure 2e shows phase diagrams demarcating stable and unstable pursuit regions, implying certain robustness within stable regions but defined boundaries of robustness. Robustness against parameter variations and external noise beyond thermal fluctuations (e.g., perturbations to flow field, changes in squirmer properties) is not explicitly tested or quantified.
    *   Implicit/Explicit: Mixed
        *  Justification: Robustness against thermal noise is implicitly tested through the inclusion of fluctuating hydrodynamics in simulations. Parameter-dependent stability diagrams (Fig. 2e) explicitly show regions of stable behavior, implying robustness within these regions but also limitations.  Robustness against wider perturbations is not explicitly investigated, so assessment is mixed explicit (thermal noise) and implicit/qualitative (parameter sensitivity).
    *   CT-GIN Mapping: This score contributes to the reliability attributes of the `BehaviorArchetypeNode`: `robustnessScore: 7`.

### **8.3 CT-GIN Emergent Behavior Validation**

*    **Vector ID:** M8.3
*    **Vector Type:** Validation
     *  Content: Validation methods include:
         1.  **Computational Simulations:** Primary validation is through numerical simulations using MPC. Trajectories, average distances, alignment parameters, and phase diagrams are generated from simulations to demonstrate and characterize emergent behaviors.
         2.  **Statistical Averaging:** Results are averaged over multiple simulation runs (at least 10 realizations) to account for thermal noise and stochasticity, providing statistical validation of emergent patterns.
         3.  **Comparison with Far-Field Approximations:** Theoretical far-field hydrodynamic approximations (Supplementary Note 1, Sec. S-IIA3, S-IIC) are used to provide semi-quantitative comparison and theoretical support for some simulation findings (e.g., stability conditions, stationary distance, center-of-mass speed).
         4.  **Operational Definitions:** Stability of pursuit is operationally defined by pursuer-target distance r<sub>c</sub> < 4σ. Pursuit is classified as unstable/unsuccessful when r<sub>c</sub> > 4σ.

         Limitations: Validation is primarily computational. Experimental validation is not presented.  Robustness and reliability are mainly assessed within the simulation framework, with limited exploration of wider perturbations. Reproducibility is implied by standard simulation protocols, but explicit reproducibility studies (independent code, labs) are absent.

     *   Implicit/Explicit: Mixed
    *   Justification: Validation methods are explicitly described (simulations, statistical averaging, theory comparison, operational definitions). Limitations of validation, such as lack of experimental confirmation and limited exploration of robustness beyond simulation parameters, are implicit in the scope and methodology of a theoretical/computational paper.

## M9: Cognitive Proximity
*   **Vector ID:** M9
*   **Vector Type:** Cognition

### **9.1 Cognitive Mapping:**

*   **Vector ID:** M9.1
*   **Vector Type:** Description
    *   Content: The paper metaphorically maps the self-steering microswimmers to cognitive systems, drawing analogies to "cognitive flocking model," "intelligent active Brownian particle," "cognitive microswimmers," "sensing," "cognitive," "self-steering," and "adaptive." The "cognition" is explicitly stated to be "minimal," and the modeling approach is contrasted with "more powerful cognitive units, such as macroscopic robots and many animals." The paper mentions that the concept of cognition has been extended to "aneural systems, including bacteria, plants, even to all living organisms," justifying the use of "cognitive" in a broad sense. The mapping is metaphorical, intended to draw parallels to adaptive behavior and information processing in biological and artificial cognitive systems, but acknowledges the simplicity and limitations of the microswimmer model compared to complex cognition.
    *   CT-GIN Mapping: `CognitiveMappingEdge` from `BehaviorArchetypeNode: Pursuit` to `CognitiveFunctionNode: Minimal Cognition/Adaptive Behavior`. Analogy to cognitive processes, but explicitly stated as minimal/metaphorical.
    *   Implicit/Explicit: Explicit
    * Justification:  The paper explicitly uses cognitive terms and draws analogies to cognitive systems but simultaneously clarifies that the "cognition" in the model is minimal and conceptual, not equivalent to higher-level cognition observed in animals or complex AI.  The mapping is explicitly stated as metaphorical and limited.

### **9.2 Cognitive Proximity Score:**

*   **Vector ID:** M9.2
*   **Vector Type:** Score
    *   Score: [2]
    *   Justification: Score of 2, at Level 2: Sub-Organismal Responsivity. The system exhibits basic adaptive behavior (steering, speed adaptation in response to target), which is beyond simple stimulus-response (Level 1) but lacks complex representation or goal-directedness (Level 3 and above). The system adapts its motion but does not exhibit 'memory' in the sense of retaining past states to alter future responses beyond immediate adaptation rules (fails to reach Level 3 reactive/adaptive autonomy). The "cognitive" aspect is limited to these basic adaptive responses and is primarily metaphorical. The system operates within a predefined behavioral repertoire (pursuit under defined steering rules) without exhibiting planning, model-based reasoning, or more complex cognitive functions (thus far below Level 4 goal-directed/model-based cognition). It is above Level 1 as the response is not purely fixed; it is continuously modulated based on sensory input, but lacks hallmarks of higher cognitive levels.
    *   Implicit/Explicit: Mixed
    *  Justification: Score is justified by contrasting the observed behavior with the CT-GIN Cognizance Scale. It is explicitly stated that the cognition is minimal and metaphorical (Level 2 scope). The limitations preventing higher scores (lack of memory, prediction, complex representation) are inferred from the system description, which focuses on reactive and adaptive, but simple, steering mechanisms, fitting Level 2 profile most closely.

**CT-GIN Cognizance Scale:**

*   **Level 0: Non-Cognitive:** Purely reactive system.  No internal state beyond immediate stimulus-response.
*   **Level 1: Simple Responsivity:** Basic stimulus-response behavior.  Reactions are fixed and predetermined.
*   **Level 2: Sub-Organismal Responsivity:**  Behavior exhibits basic forms of adaptation or plasticity, but lacks complex representation or goal-directedness.  **[System score fits here]**
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
    | Sensing/Perception               |       4      | Senses relative position/orientation of target via hydrodynamic interaction (implicit "sensing"), though minimal and indirect. | `CognitiveFunctionNode: Sensing/Perception` linked from `AdjunctionEdge: Hydrodynamic Interaction` | Implicit          | Sensing is not explicitly by dedicated sensor but effective through hydrodynamic coupling. Score reflects minimal, indirect "sensing". |
    | Memory (Short-Term/Working)        |       1      | Minimal. No working memory. System reacts to instantaneous input.                             | None                             | No                | No mechanism for short term or working memory identified.                           |
    | Memory (Long-Term)                 |       0      | Absent. No long-term memory or persistent state change influencing future behavior.    | None                             | No                | No long-term memory mechanism in the model.                                  |
    | Learning/Adaptation              |       3      | Basic adaptation of behavior (steering, speed) to target. Fixed adaptation rules, no learning beyond that. | `CognitiveFunctionNode: Learning/Adaptation` linked from `AdaptationNode: Feedback Control` | Explicit          |  Adaptation mechanism explicitly defined, though basic form of plasticity. Score reflects limited adaptation capacity. |
    | Decision-Making/Planning          |       1      | Minimal decision making, limited to choosing steering direction based on simple rule. No planning. | None                             | No                | Decision-making very basic and rule-bound, no evidence of planning.                 |
    | Communication/Social Interaction |       0      | Absent in pair interaction context.                                                       | None                             | No                | System studied as isolated pair, no consideration of communication/social interaction. |
    | Goal-Directed Behavior            |       2      | Weakly goal-directed towards pursuing the target. Goal is implicit in steering rule, not explicitly represented. | `CognitiveFunctionNode: Goal-Directed Behavior` linked from `BehaviorArchetypeNode: Pursuit` | Implicit          |  Pursuit behavior implies weak form of goal directedness, though goal not explicitly represented in model. Low score for weak, implicit goal direction. |
    | Model-Based Reasoning              |       0      | Absent. No internal models or reasoning.                                               | None                             | No                | Model explicitly reactive, no internal model-based reasoning.                      |
    | **Overall score**                 |      [1.6]       |                                                                                       |                                   |                     |                |

    *   **Note:** Overall score is the average of the individual function scores.

## M10: Criticality Assessment
*   **Vector ID:** M10
*   **Vector Type:** Criticality

### **10.1 Criticality:**

*   **Vector ID:** M10.1
*   **Vector Type:** Assessment
    *   Content: Unclear
    *   Justification: The paper does not explicitly discuss criticality or examine if the system operates near a critical point. There is no analysis of scale-free behavior, power laws, or long-range correlations that would typically indicate criticality. While emergent behaviors (cooperative states) are observed, their emergence is described in terms of parameter dependencies (Pe, Ω, α) leading to stable or unstable pursuit, rather than in the context of phase transitions or critical phenomena typically associated with criticality. The system operates in a fluctuating environment (thermal noise), which is sometimes associated with criticality, but direct evidence or analysis related to criticality is absent in the excerpt.
        *   Critical Parameters (If Yes/Partial): [N/A]
        *   Evidence: [No explicit evidence in the provided text.]
    *   Implicit/Explicit: Implicit
    *    Justification:  The study does not present or analyze data suggesting operation near a critical point. The focus is on emergent cooperative motion and pursuit strategies under varying parameters, but not on criticality in the system's dynamics. The absence of relevant analysis suggests non-presence, but lack of explicit statement makes it unclear.

## M11: Review Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Review")**

N/A

## M12: Theoretical Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Theoretical")**

*   **Vector ID:** M12
*   **Vector Type:** Theory

### **12.1 Theoretical Rigor:**

*   **Vector ID:** M12.1
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The theoretical framework appears reasonably rigorous. It is based on well-established models (squirmer model, MPC fluid dynamics). The steering and adaptation mechanisms are mathematically formulated (Eqs. 1, 13, 14, 19, 22). Assumptions are generally implicit but standard for microswimmer simulations (low Reynolds number, spherical squirmers, etc.). Derivations are not explicitly shown in detail in the excerpt but are referenced (Supplementary Material and cited work). Internal consistency is generally maintained within the described model, with no immediately apparent logical contradictions. The use of far-field approximations to validate simulation trends adds to the theoretical soundness. For a computational model based paper, theoretical rigor is adequate.
       * Implicit/Explicit: Mixed
       *  Justification:  Rigor is judged based on standard practices in theoretical/computational physics. Use of established models and mathematical formulations is explicit.  Detailed derivations and full assumption lists are implicit but can be inferred to align with standard practices in the field. Overall, the theoretical base seems well-founded, supporting a score of 8.

### **12.2 Realization Potential:**

*   **Vector ID:** M12.2
*   **Vector Type:** Score
    *   Score: [6]
    *   Justification: The potential for physical realization is medium. Squirmer models are generic and represent simplified microswimmers, but can be mapped to real systems like Janus particles or active colloids.  Implementing self-steering and speed adaptation in synthetic microswimmers poses significant, but not insurmountable, challenges (mentioned as "major challenges" in paper). Realizing the specific steering mechanisms (reorientation, alignment + speed adaptation) in practice would require engineered actuators and sensors, potentially through chemical, optical, or magnetic means.  Fabrication pathways for active colloids with responsiveness are being developed. Fundamental limitations include complexity of precisely controlling surface flow fields and achieving robust, noise-resistant steering and adaptation at the microscale, particularly with limited maneuverability. Realization, while challenging, is plausible within current and near-future micro-robotic and active material technologies.
    *   Implicit/Explicit: Mixed
    *  Justification:  Realization potential is assessed based on current trends in micro robotics and active materials.  Paper explicitly mentions "challenges" for synthetic microswimmers, implicitly acknowledging realization hurdles. Plausibility is inferred from analogy to existing active colloid and micro-robotics research, but specific pathways and limitations need further inference beyond the excerpt, leading to a medium score of 6.

### **12.3 Potential for Future CT-GIN Implementation Score**

* **Vector ID:** M12.3
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The theoretical framework has good potential to guide future research in CT-GIN implementation. It identifies key principles for pursuit and cooperative motion in active matter systems, highlighting the role of hydrodynamic interactions, steering mechanisms, and adaptation. The model provides a clear, albeit simplified, example of embodied computation (steering rules) and emergent behavior (cooperative states).  The study explores different steering strategies which are relevant to designing artificial cognitive microswimmers.  Novelty lies in systematic comparison of steering strategies and their impact on emergent dynamics. Potential impact is in informing design of micro-robotic systems for tasks like targeted delivery or environmental sensing. Alignment with CT-GIN principles is moderate; while minimal cognition and emergent order are present, aspects like memory, complex computation, and higher cognitive functions are absent.  Framework offers a good starting point for exploring more complex CT-GIN implementations in active matter.
    *    Implicit/Explicit: Mixed
    *   Justification: Potential is evaluated based on novelty, impact, and alignment with CT-GIN. Framework's contribution to understanding emergent behavior and embodied computation in active matter is explicit.  Relevance for future CT-GIN implementation and potential for more complex systems are inferred, based on the framework’s strengths in demonstrating minimal cognitive and self-organizing principles, leading to a score of 7 indicating good, but not outstanding, potential yet.

## M13: Overall Assessment & Scoring
*   **Vector ID:** M13
*   **Vector Type:** Overall

### **13.1 CT-GIN Readiness Score:**

*   **Vector ID:** M13.1
*   **Vector Type:** Score
*   **Calculated Score:** [6.0]

**CT-GIN Readiness Summary Table:**

| CT-GIN Aspect                   | Strength (Yes/Partial/No) | Key Supporting Metrics (with units) | Limitations (Missing Metrics/Data Gaps)                                           | Improvement Areas (Future Research)                                          |
| :------------------------------ | :-----------------------: | :-----------------------------------| :------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| Energy Flow Efficiency          | Partial                   | Qualitative Assessment: Moderate    | Quantified energy input/dissipation, efficiency metrics                          | Quantify energy efficiency, explore energy-optimized steering strategies      |
| Memory Fidelity                 | No                        | N/A                                 | Memory Retention Time, Capacity, Readout Accuracy, Degradation Rate, Operations Energy Cost, Robustness Metrics | Incorporate memory mechanisms, explore memory-augmented steering rules          |
| Organizational Complexity       | Yes                       | Emergent Cooperative States         | Yoneda Embedding Score: 6 (Moderate)                                            | Enhance predictability of global order, refine local-to-global mapping        |
| Embodied Computation            | Yes                       | Analog Computation Primitives: Vector Cross Product, Vector Scalar Product, Proportional Control | Processing Power, Energy/Operation, Freq/Resp. Time, Bit-Depth for computational units | Explore more complex computational primitives, quantify computational performance |
| Temporal Integration            | No                        | Relevant Timescales Identified (Qualitative) | Precise timescale values with units, Active Inference assessment                 | Investigate active inference mechanisms, quantify prediction error reduction    |
| Adaptive Plasticity             | Yes                       | Feedback-controlled Steering, Speed Adaptation | Adaptation Mechanism detailed descriptively                             | Formalize adaptation mechanism mathematically, explore more sophisticated learning rules |
| Functional Universality         | No                        | Limited to Pursuit Behavior           | Demonstration of diverse behaviors                                             | Explore broader range of behaviors beyond pursuit (e.g., navigation, pattern formation) |
| Cognitive Proximity            | Partial                   | Cognitive Proximity Score: 2/10 (Sub-Organismal Responsivity) | Cognitive Function Checklist scores, Justification for limited cognitive functions | Enhance cognitive functions (memory, decision-making, planning, model-based reasoning), move to higher Cognizance Scale levels |
| Design Scalability & Robustness | Partial                   | Behavior Robustness Score: 7/10 (Moderate) | Robustness against parameter variations and broader perturbations, scalability metrics | Enhance robustness against noise and perturbations, explore scalable implementations |
| **Overall CT-GIN Readiness Score** |        |   |   |      |


### **13.2 Qualitative CT-GIN Assessment Conclusion:**

*   **Vector ID:** M13.2
*   **Vector Type:** Textual Summary
    *   Content: This theoretical paper presents a computational model of cognitive self-steering microswimmers, demonstrating emergent cooperative pursuit behaviors driven by hydrodynamic interactions and adaptive steering rules. Key strengths include the clear formulation of steering strategies, emergence of stable cooperative states, and moderate robustness of these behaviors against thermal noise within the simulation framework. The embodied computation is minimal but present in the analog feedback control mechanisms governing steering and speed adaptation. Key limitations include the absence of explicit memory, a very basic form of embodied computation, lack of active inference, and limited cognitive proximity (Level 2: Sub-Organismal Responsivity).  The predictability of global order from local rules is moderate. Overall assessment: The work provides a valuable theoretical foundation and a computational platform for studying minimal cognitive behaviors in active matter systems. It demonstrates basic CT-GIN principles like self-organization and embodied computation in a simplified hydrodynamic context. However, it falls significantly short of realizing higher-level cognitive functions or achieving strong CT-GIN readiness due to the simplicity of the "cognitive" mechanisms and lack of memory or complex information processing. Future potential lies in expanding the model to incorporate more sophisticated memory, computation, and adaptation mechanisms to move towards higher levels of cognizant matter.

### **13.3 CT-GIN Refinement Directions:**

*   **Vector ID:** M13.3
*   **Vector Type:** Recommendations
    *   * Incorporate memory mechanisms into the microswimmer model, enabling the pursuer to learn from past interactions and adapt steering strategies based on experience history (e.g., Reinforcement Learning).
    *   Develop more complex embodied computational primitives beyond vector products and proportional control, exploring analog or neuromorphic computation within the hydrodynamic system itself.
    *   Investigate active inference by equipping the pursuer with an internal model of the target's behavior or environment and designing steering actions to minimize prediction errors.
    *   Quantify energy efficiency of pursuit and cooperative motion, aiming to optimize steering strategies for minimal energy consumption.
    *   Enhance robustness of emergent behaviors against broader range of perturbations (parameter variations, external flow disturbances, stochastic squirmer properties) beyond thermal noise.
    *   Explore design scalability by considering multi-agent systems with multiple pursuers and targets, investigating collective pursuit and swarm behaviors.
    *   Validate computational findings through experimental realization of self-steering microswimmers capable of hydrodynamic pursuit, comparing simulation predictions with experimental observations.
    *   Extend the model to incorporate more diverse functional behaviors beyond pursuit, such as navigation in complex environments, pattern formation in multi-agent systems, or rudimentary forms of problem-solving.

## M14: CT-GIN Knowledge Graph

*   **Vector ID:** M14
*   **Vector Type:** Visualization

### **14.1. CT-GIN Knowledge Graph:**
* **Content:**
[__N/A - Text-based output does not include image.__]

## M15: Relationship Vectors
*   **Vector ID:** M15
*   **Vector Type:** Relationships
*   Relationships:
        | Source Vector ID | Target Vector ID | Relationship Type |
        | ------------- | ------------- | ----------------- |
        | M2.1 | M2.2 | EnergyTransduction |
        | M2.2 | M2.4 | EnergyDissipation |
        | M4.2 | M4.3 | Adjunction |
        | M7.2 | M8.1 | Monad |
        | M8.1 | M9.1 | CognitiveMapping |

## M16: CT-GIN Template Self-Improvement Insights

*   **Vector ID:** M16
*   **Vector Type:** Feedback

### **Template Feedback:**

*    **Vector ID:** M16.1
*   **Vector Type:** Text
Provide specific, actionable feedback on the *CT-GIN template itself*, based on this analysis:
    *   **Missing Probes:** The template is comprehensive. Perhaps adding probes specifically for *scalability* and *manufacturability* in M1 could be useful, as these are crucial for practical material intelligence.
    *   **Unclear Definitions:**  The definition of "Memory" in M3 could be slightly refined to better distinguish between *adaptive response* and true *memory retention*.  Perhaps explicitly adding "persistent modification of internal state beyond stimulus offset" to the definition.
    *   **Unclear Node/Edge Representations:** The guidance was generally sufficient. For M14 (Knowledge Graph image not generated in text output), it might be helpful to include a textual description example of node/edge attribute annotation.
    *   **Scoring Difficulties:** Subjectivity in scoring is inherent, especially for "Cognitive Proximity" and "Robustness."  Providing more granular rubrics for levels within the Cognizance Scale (M9.2) and Robustness Score (M8.2), with specific examples for each score level, could increase consistency.
    *   **Data Extraction/Output Mapping:** Data extraction was straightforward. Output mapping to the template structure was clear and well-defined.
    *   **Overall Usability:** The template is well-structured and relatively easy to use, though quite detailed and requires careful attention to all sections to ensure completeness and adherence to formatting.  Breaking down very long sections (like M4.2) into subsections might improve readability during analysis.
    * **Specific Suggestions:**
        * Add probes for "Scalability" and "Manufacturability" in Module 1.
        * Refine "Memory" definition in M3 to emphasize 'persistent change beyond stimulus'.
        * Provide more granular rubrics with examples for scoring "Cognitive Proximity" (M9.2) and "Robustness" (M8.2).
        * Consider adding subsections for very long descriptive sections (e.g., M4.2, M8.3) to improve readability.```markdown
# Hydrodynamic pursuit by cognitive self-steering microswimmers

__Paper Type:__ Theoretical/Computational

## M1: System Overview & Implementation
*   **Vector ID:** M1
*   **Vector Type:** Overview

### **1.1 System Description**

*   **Vector ID:** M1.1
*   **Vector Type:** Description
    *   Content: This paper presents a theoretical model of a pursuer-target system composed of two spherical squirmers interacting hydrodynamically in a fluid. The target squirmer moves with a prescribed propulsion, while the pursuer is equipped with a "cognitive self-steering" mechanism that adjusts its motion based on the target's position or propulsion direction. Two steering strategies are investigated: (1) reorientation of the pursuer towards the target position and (2) alignment of the pursuer's propulsion with the target's direction, combined with speed adaptation. The model aims to explore stable cooperative motion and pursuit behaviors arising from hydrodynamic interactions and the implemented steering mechanisms.
    *   CT-GIN Mapping: `SystemNode` attributes: `systemType: Microswimmer Pursuit Model`, `domain: Fluid Dynamics/Active Matter`, `mechanism: Hydrodynamic Interaction, Cognitive Steering`, `components: Pursuer Squirmer, Target Squirmer, Fluid`, `purpose: Study Pursuit Strategies, Analyze Cooperative Motion`
    *   Implicit/Explicit: Explicit
        *  Justification: The system description is explicitly stated in the paper's abstract and introduction, detailing the components, mechanisms, and objectives of the study.

### **1.2 Implementation Clarity**

*   **Vector ID:** M1.2
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The implementation is clearly described within the context of a theoretical/computational study. The paper defines the squirmer model, the fluid simulation method (Multiparticle Collision Dynamics), and the mathematical formulations of the two cognitive steering strategies. The parameters used (Péclet number, maneuverability, speed ratio) are clearly defined and their roles explained. While certain simulation details are deferred to the Methods section, the core implementation of the model and the steering algorithms is presented with sufficient clarity to understand and potentially reproduce the computational experiments. The "cognitive" aspect, though simplified, is explicitly acknowledged as a minimal model for adaptive behavior.
    *   Implicit/Explicit: Mixed
        * Justification: The high-level model and steering strategies are explicitly defined mathematically. Implementation details of the MPC simulation and full parameter sets require referencing the Methods section (as stated), making the complete implementation Mixed (partly explicit, partly requiring reference to further sections).

### **1.3 Key Parameters**

*   **Vector ID:** M1.3
*   **Vector Type:** ParameterTable
    *   Table:
        | Parameter Name | Value | Units | Source (Fig/Table/Section) | Implicit/Explicit | Data Reliability (High/Medium/Low) | Derivation Method (if Implicit) |
        | :------------- | :---: | :---: | :-----------------------: | :-----------------: | :-----------------------------: | :-------------------------------: |
        | Péclet number (Pe) | 8, 32, 128 | N/A | Eq. (2), Figs. 2, 3, 4, 5 | Explicit | High | N/A |
        | Maneuverability (Ω) | 32, 64, 128 (and Ω/Pe ratios) | N/A | Eq. (2), Figs. 2, 3, 4, 5 | Explicit | High | N/A |
        | Speed ratio (α = v<sub>t</sub>/v<sub>p</sub>) | 0 to 1.8 | N/A | Figs. 2, 3, 4 | Explicit | High | N/A |
        | Squirmer type (β) | -3 (pusher), 3 (puller) | N/A | Figs. 2, 3, 4 | Explicit | High | N/A |
        | Squirmer Diameter (σ) | N/A (set to unit length in simulations) | m (inferred, typical microswimmer scale) | Eq. (2) | Implicit | Medium | Typical microswimmer dimensions assumed in low-Reynolds number simulations|

    *   **Note:** The table lists the key dimensionless parameters varied in the study and the squirmer type. Squirmer diameter, while not explicitly given a numerical value, is implicitly set as a unit length in simulations and inferred to be at the microscale given context.

## M2: Energy Flow
*   **Vector ID:** M2
*   **Vector Type:** Energy

### **2.1 Energy Input**

*   **Vector ID:** M2.1
*   **Vector Type:** Input
    *   Content: The energy input to the system is provided by the active driving of both the target and pursuer microswimmers. This active driving is modeled as an imposed surface flow field (slip velocity) on the squirmers.  For the target, this is a prescribed flow field maintaining constant velocity. For the pursuer, the flow field is dynamically adapted based on the steering strategies. The energy source, in a physical realization, would be the mechanism maintaining this non-equilibrium surface flow, such as chemical reactions, external fields, or biological motors. In the simulation, it is an inherent property of the squirmer model.
    *   Value: N/A (Model parameter, not an externally applied energy value in the simulation)
    *   Units: N/A
    *   CT-GIN Mapping: `EnergyInputNode`: attributes - `source: Active Surface Flow Field`, `type: Active Mechanical`, `form: Modelled Imposed Slip Velocity`
    *   Implicit/Explicit: Implicit
        *  Justification: While not explicitly termed "energy input," the active surface flow field is the fundamental source of motion and work in the system, acting as the energy injection mechanism for self-propulsion. This energy input is intrinsic to the squirmer model and represents the active nature of the swimmers.

### **2.2 Energy Transduction**

*   **Vector ID:** M2.2
*   **Vector Type:** Transduction
    *   Content: The primary energy transduction is from the energy source driving the surface flow field to the kinetic energy of the fluid and the microswimmers. The imposed slip velocity on the squirmer surfaces generates fluid flow, converting the input energy into fluid motion and propelling the squirmers. The hydrodynamic interactions then mediate energy transfer between the pursuer and target. The steering mechanisms further transduce the active driving into controlled directional motion of the pursuer, guiding it towards or aligning with the target, thus directing the energy flow to achieve pursuit.
    *   CT-GIN Mapping: `EnergyTransductionEdge`: attributes - `mechanism: Hydrodynamic Propulsion and Steering`, `from_node: EnergyInputNode`, `to_node: Kinetic Energy (Fluid & Microswimmers)`, `process: Surface Flow Field to Fluid and Particle Motion`
    *   Implicit/Explicit: Implicit
        *  Justification: The description of squirmer propulsion and hydrodynamic interactions implicitly describes energy transduction processes. The conversion from active driving (surface flow) to motion (kinetic energy) and the role of hydrodynamics and steering in directing this energy flow are implied by the mechanisms outlined, even if not explicitly quantified as energy transduction.

### **2.3 Energy Efficiency**

*   **Vector ID:** M2.3
*   **Vector Type:** Score
    *   Score: [5]
    *   Justification/Metrics: Energy efficiency is not explicitly quantified in the paper. However, given the low Reynolds number regime, viscous dissipation is expected to be significant, indicating moderate energy efficiency. The active driving sustains motion against viscous drag, meaning a continuous energy input is required for sustained pursuit and cooperative motion. The efficiency would be related to how effectively the surface flow energy is converted into directed motion of the pursuers relative to the energy dissipated through viscous friction in the fluid. Without explicit calculations, a score of 5 represents a qualitative assessment of moderate efficiency, acknowledging viscous losses in low Reynolds number regime, but effective directed motion from active driving.
    *   CT-GIN Mapping: Attribute of `EnergyTransductionEdge`s: `efficiency_score: 5 (Moderate, Qualitative Assessment)`
    *   Implicit/Explicit: Implicit
      *  Justification: Efficiency is qualitatively judged as moderate due to the inherent viscous losses at low Reynolds numbers and the nature of active, continuous driving required for motion. No quantitative efficiency metrics are provided, necessitating an implicit assessment based on fundamental physics of low-Re systems.

### **2.4 Energy Dissipation**

*   **Vector ID:** M2.4
*   **Vector Type:** Dissipation
    *   Content: The primary mechanism of energy dissipation in this system is viscous friction within the fluid. At low Reynolds numbers, momentum transport is dominated by viscosity, leading to significant energy dissipation into heat as the fluid and squirmers move. Thermal fluctuations, inherent in the fluid model (MPC), also represent a form of energy dissipation into random molecular motion. Hard-core repulsion, while primarily interaction force, also indirectly contributes to dissipation by altering flow fields and leading to viscous losses. The paper does not quantitatively measure energy dissipation; however, it's implicitly acknowledged as a dominant factor in low-Reynolds number hydrodynamics.
    *   CT-GIN Mapping: Creates `EnergyDissipationNode`: attributes - `mechanism: Viscous Friction, Thermal Fluctuations`; `EnergyDissipationEdge`: attributes - `from_node: Kinetic Energy (Fluid & Microswimmers)`, `to_node: Heat (Viscous Dissipation), Random Motion (Thermal Fluctuations)`
    *    Implicit/Explicit: Implicit
        *  Justification: Viscous friction is a fundamental aspect of low-Reynolds number fluid dynamics, and thermal fluctuations are explicitly part of the MPC model. Dissipation is thus implicitly understood to be dominated by these mechanisms even though not directly quantified or measured in the presented analysis.

## M3: Memory
*   **Vector ID:** M3
*   **Vector Type:** Memory

### **3.1 Memory Presence:**

*   **Vector ID:** M3.1
*   **Vector Type:** Binary
    *   Content: No
    *   Justification: The system, as described in the excerpt, does not exhibit memory in the sense of a persistent change in internal state that influences future behavior beyond immediate reactive adjustments. The pursuer's steering and speed adaptations are based on instantaneous sensory inputs—the relative position or orientation of the target at the current time step. There is no mechanism for the system to retain information about past interactions, trajectories, or environmental conditions to modify its future responses. The squirmers react to the present stimulus without any dependence on historical states or learned patterns beyond the current state variables. While parameters like speed and orientation change dynamically, they are continually updated based on current input, not historical records, thus lacking memory.
    *    Implicit/Explicit: Explicit
        * Justification: The system description focuses on real-time adaptation and reaction to the current environment. No mention or mechanism for storing, retaining, or utilizing past information or experiences to influence future behavior is present, indicating an explicit absence of memory in the described model.

## M4: Self-Organization and Emergent Order
*   **Vector ID:** M4
*   **Vector Type:** Self-Organization

### **4.1 Self-Organization Presence:**

*   **Vector ID:** M4.1
*   **Vector Type:** Binary
    *   Content: Yes
    *   Justification:  The system demonstrates self-organization through the emergence of stable cooperative motion patterns between the pursuer and target. These patterns, such as head-to-tail configurations for pullers, leader-follower arrangements for pushers, and stable helical and circular motions, arise spontaneously from local interactions among components—the hydrodynamic interactions between the squirmers and the implemented steering rules. The global order (the stable cooperative states) is not externally imposed or pre-programmed but emerges from the local rules governing individual squirmer behavior and their mutual influence through the fluid. The type of emergent order depends on parameters like squirmer type (puller/pusher), steering strategy, and speed ratio, demonstrating how global patterns arise from parameter-dependent local interactions.
    *   Implicit/Explicit: Explicit
        *  Justification: The paper clearly emphasizes the "emergent dynamics" and "emergent cooperative states" as key outcomes of the simulations. The results section details different types of stable configurations and motions that arise from the described local interaction rules, explicitly highlighting self-organization as a central feature of the system.

**(Conditional: If M4.1 is "Yes", include M4.2-M4.7)**

### **4.2 Local Interaction Rules:**

*   **Vector ID:** M4.2
*   **Vector Type:** Rules
    *   Content:
        1.  **Hydrodynamic Interactions:** Squirmers interact through the fluid medium, governed by low-Reynolds number hydrodynamics. The fluid is modeled using Multiparticle Collision Dynamics (MPC), capturing fluctuating hydrodynamic effects.  Squirmers generate flow fields described by Legendre polynomials, modulated by the stresslet parameter β (determining puller/pusher type).
        2.  **Reorientation Steering Rule:** The pursuer adjusts its angular velocity (ω<sub>0</sub>) to reorient its propulsion direction (e<sub>p</sub>) towards the target's position (e<sub>c</sub>). This is mathematically expressed as: ω<sub>0</sub> = C<sub>0</sub> (e<sub>p</sub> × e<sub>c</sub>), where C<sub>0</sub> is a maneuverability constant and e<sub>c</sub> is the unit vector pointing from the pursuer to the target.
        3.  **Alignment Steering with Speed Adaptation Rule:** The pursuer adjusts its angular velocity to align its propulsion direction (e<sub>p</sub>) with the target's propulsion direction (e<sub>t</sub>): e<sub>aim</sub> = e<sub>t</sub>. Additionally, the pursuer adapts its speed based on the relative position component along the connection vector (e<sub>p</sub> ⋅ e<sub>c</sub>), accelerating when behind the target and decelerating when ahead, with a maximum speed limit v<sub>max</sub>. The speed adaptation is governed by a velocity relaxation process described in the Methods section and Eqs. (19), (22) (not fully detailed in the excerpt).
        4.  **Steric Repulsion:** Short-range repulsive forces between squirmers, modeled via a separation-shifted Lennard-Jones potential, prevent physical overlap and ensure volume exclusion.

    *   CT-GIN Mapping: Part of the `AdjunctionEdge` description (local side, governing interactions). These define the "LocalInteraction" category of edges in the CT-GIN. `InteractionRuleNode` attributes: `ruleType: Hydrodynamic Interaction`, `ruleType: Reorientation Steering`, `ruleType: Alignment & Speed Adaptation Steering`, `ruleType: Steric Repulsion`. Edges are defined between `SquirmerNode` instances and the `FluidNode`, and steering rules act as control mechanisms modifying `SquirmerNode` behavior.
    * **Implicit/Explicit**: Mixed
        *  Justification: The local interaction rules are explicitly described through mathematical equations (steering rules, steric repulsion potential) and references to the fluid model (MPC) and squirmer hydrodynamics. While detailed MPC and squirmer formulations are implicit, the core local rules driving self-organization (steering, hydrodynamic and steric interactions) are presented explicitly enough to understand the simulation setup.

### **4.2.1 Local Interaction Parameters:**

* **Vector ID:** M4.2.1
* **Vector Type:** Table
*   Table:
    | Rule ID | Description | Parameter Name | Parameter Value Range | Units | Data Source | Implicit/Explicit | Justification |
    | :------ | :---------- | :------------- | :---------- | :---: | :----------: | :----------------: | :------------: |
    | 1 | Squirmer Hydrodynamics | β (stresslet parameter) | -3 (pusher), 3 (puller) | N/A | Figs. 2, 3 | Explicit | Directly sets squirmer type |
    | 1 | Fluid Dynamics | Fluid Viscosity (η) | 111.3 mk<sub>B</sub>T/a<sup>2</sup> | MPC Units | Methods Section | Implicit | Parameter of MPC fluid model, fixed value from Methods section. |
    | 2, 3 | Steering Actuation |  C<sub>0</sub> (steering strength) | N/A | N/A | Eq. (1) | Explicit | Controls strength of angular velocity adjustment in steering rules. |
    | 3 | Speed Adaptation | κ (friction coefficient) | N/A | N/A | Eq. (19) | Explicit | Controls relaxation rate in speed adaptation. |
    | 4 | Steric Repulsion | LJ Potential Parameters (σ<sub>0</sub>, ϵ<sub>0</sub>, d<sub>v</sub>) | σ<sub>0</sub>=0.5a, ϵ<sub>0</sub>=5k<sub>B</sub>T, d<sub>v</sub>=0.25a | MPC Units | Methods Section | Implicit | Fixed parameters for Lennard-Jones potential, from Methods section. |
### **4.3 Global Order:**

*   **Vector ID:** M4.3
*   **Vector Type:** Order
    *   Content: The emergent global orders observed in the system are stable cooperative motion states of the pursuer-target pair. These include:
        1.  **Stable Head-to-Tail Configuration for Pullers (Reorientation Strategy):** For puller squirmers using reorientation steering, a stable configuration emerges where the pursuer follows directly behind the target, often in a touching configuration.
        2.  **Stable Leader-Follower Configuration for Pushers (Reorientation Strategy):** For pusher squirmers with reorientation steering, a stable state emerges where the pursuer follows the target at a finite average distance in a leader-follower arrangement.
        3.  **Cooperative Helical Motion (Helical Target Trajectory):** When the target moves on a helical trajectory, the pursuer stably follows on a modified helical path, exhibiting cooperative helical motion.
        4.  **Cooperative Circular Motion (Pushers, Alignment & Speed Adaptation):** With alignment and speed adaptation steering for pusher squirmers, a cooperative circular motion emerges, where the pair orbits in a stable circular trajectory.

    *   CT-GIN Mapping: Defines a `ConfigurationalNode` in the CT-GIN, representing emergent global order types. `ConfigurationNode` attributes: `orderType: Stable Cooperative Motion`, `motionType: Head-to-Tail (Pullers, Reorientation)`, `motionType: Leader-Follower (Pushers, Reorientation)`, `motionType: Cooperative Helical`, `motionType: Cooperative Circular (Pushers, Alignment & Speed Adaptation)`.
    * **Implicit/Explicit**: Explicit
        *  Justification: The descriptions of global order are explicitly presented in the Results section, detailing the different stable configurations and motion patterns observed in simulations. Figures and supplementary movies directly illustrate these emergent orders for various parameter settings and steering strategies.

### **4.4 Predictability of Global Order:**

*   **Vector ID:** M4.4
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The emergence of global order exhibits moderate predictability. The simulations show that the type of stable cooperative state (e.g., head-to-tail vs. leader-follower) and its stability are dependent on system parameters such as squirmer type (β), speed ratio (α), and maneuverability (Ω). Phase diagrams (Fig. 2e) quantitatively map out regions of stable vs. unstable pursuit as a function of Pe and Ω, indicating a level of parameter-dependent predictability. Theoretical far-field approximations (Eqs. 3-5) provide semi-quantitative agreement with simulation results, further supporting predictability within certain parameter ranges. However, thermal noise inherent in the system introduces stochasticity, limiting perfect deterministic prediction of individual trajectories and configurations. Predictability is statistical, reflected in average distances, alignment parameters, and stability regions, rather than precise outcomes for each run.
    * **Implicit/Explicit**: Mixed
    *  Justification: The predictability is supported by explicit simulation results showing parameter-dependent phases (Figs. 2e) and semi-quantitative agreement with theoretical predictions. However, the inherent stochasticity and statistical nature of the observed order, as well as the deviations from far-field theory especially at close distances, limits perfect predictability, making the assessment Mixed (partly explicit evidence for, and implicit limitations to, predictability).

### **4.5. Local Interaction Rules (for Self-Organization)**
* **Vector ID:** M4.5
* **Vector Type:** Table
*   Table:
| Rule ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Source |
| :------ | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :-----: |
| 1 | Reorientation Steering | C<sub>0</sub> (Steering Strength) | N/A | N/A | Explicit | Controls actuation strength for reorientation towards target | Eq. (1) |
| 2 | Alignment Steering | C<sub>0</sub> (Steering Strength) | N/A | N/A | Explicit | Controls actuation strength for alignment with target direction | Eq. (1) |
| 3 | Speed Adaptation | κ (Speed Adapt. Strength) | N/A | N/A | Explicit |  Controls strength of speed adjustment based on target proximity | Eq. (19) |
| 3 | Speed Adaptation | v<sub>max</sub> (Max Speed) | Variable (relative to v<sub>t</sub>) | m/s (inferred) | Explicit | Limits maximum pursuer speed in adaptation scheme | Fig. 4 |

### **4.6. Globally Emergent Order and Order Parameters**
* **Vector ID:** M4.6
* **Vector Type:** Table
*   Table:
| Property ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Protocol | Source |
| :---------- | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :------: | :-----: |
| 1 | Avg. Pursuer-Target Distance (straight pushers) | 〈r<sub>c</sub>〉 | Variable | σ | Explicit | Quantifies average separation in leader-follower state | Averaged from simulations | Fig. 2b |
| 2 | Center-of-Mass Speed (U<sub>cm</sub>) | U<sub>cm</sub> | Variable | v<sub>p</sub> | Explicit | Measures cooperative motion speed of the pair | Averaged from simulations | Fig. 2c |
| 3 | Alignment Parameter (straight) | 〈e<sub>p</sub>⋅e<sub>t</sub>〉 | -1 to 1 | N/A | Explicit |  Quantifies alignment of pursuer and target propulsion | Averaged from simulations | Fig. 2d |
| 4 | Alignment Parameter (helical) | 〈e<sub>p</sub>⋅e<sub>t</sub>〉 | -1 to 1 | N/A | Explicit |  Quantifies alignment in helical pursuit | Averaged from simulations | Fig. 3b |
| 5 | Avg. Pursuer-Target Distance (helical) | 〈r<sub>c</sub>〉 | Variable | σ | Explicit |  Quantifies separation in helical pursuit | Averaged from simulations | Fig. 3c |
| 6 | Induced Target Angular Frequency (Ω<sub>ind</sub>) | Ω<sub>ind</sub> | Variable | D<sub>R</sub> | Explicit | Quantifies target rotation induced by pursuer | Calculated from simulations (Eq. 6) | Fig. 5d |
| 7 | Persistence Length (l<sub>p</sub>) | l<sub>p</sub> | Variable | σ | Explicit |  Quantifies directional persistence of motion in circular pursuit | Fitted from velocity autocorrelation (Fig. 5c) | Fig. 5c |
| 8 | Radius of Circular Motion (R<sub>ind</sub>) | R<sub>ind</sub> | Variable | σ | Explicit | Quantifies size of circular trajectory in cooperative motion | Calculated from Ω<sub>ind</sub> and v<sub>t</sub> (Fig. 5e) | Fig. 5e |

### **4.7 Yoneda Embedding and Local-to-Global Mapping Fidelity**

*   **Vector ID:** M4.7
*   **Vector Type:** Table
*   Table:
    | Link Type | Description | Predictability | Yoneda Score | Metrics | Implicit/Explicit | Justification | Source |
    | :-------- | :---------- | :------------- | :----------- | :------ | :----------------: | :------------: | :-----: |
     | Local Steering Rules & Hydrodynamics -> Global Cooperative Motion Patterns | How well local rules and hydrodynamic interactions determine emergent configurations | Moderate | 6 | Phase diagrams (Fig. 2e), Parameter-dependent plots of order parameters (Figs. 2, 3, 4, 5), Semi-quantitative agreement with far-field theory (Eqs. 3-5) | Mixed |  Predictability is statistical and parameter-dependent, not fully deterministic. Far-field theory provides partial mapping. Stochasticity limits perfect embedding. | Figs. 2, 3, 4, 5, Supplementary Note 1 |
    *   **Yoneda Embedding Fulfillment Score [0-10]:** [Score: 6. Rubric: 0=No discernible link, 5=Qualitative link, 10=Precise, deterministic link. A score of 6 indicates Moderate fidelity. Local rules significantly influence global order, but the mapping is not perfectly deterministic or quantitatively precise across all conditions due to complexity and noise.]
    *   **Metrics:**  [Statistical measures of predictability: Phase Diagrams indicating stability zones, parameter-dependent plots showing trends in order parameters, and the degree of agreement between simulation results and simplified theoretical approximations.]
    *   **Justification:** [The Yoneda score of 6 reflects a moderate level of mapping fidelity. The local steering rules and hydrodynamic interactions clearly shape the emergent global order, as demonstrated through the phase diagrams and trends in order parameters. However, the mapping is not fully deterministic due to thermal noise and the complexity of hydrodynamic interactions, particularly near-field effects. While the far-field approximations offer some theoretical linkage, they are simplified and deviate from simulation results under certain conditions. The predictability is statistical and parameter-dependent rather than a precise, one-to-one mapping, justifying a score in the mid-range of moderate fidelity.]

## M5: Computation
*   **Vector ID:** M5
*   **Vector Type:** Computation

### **5.1 Embodied Computation Presence:**

*   **Vector ID:** M5.1
*   **Vector Type:** Binary
    *   Content: Yes
    *   Justification: Embodied computation, in a minimal form, is present in the pursuer's steering mechanism. The steering rules act as computational algorithms that are directly implemented within the physical dynamics of the squirmer model. The pursuer "computes" the required angular velocity adjustment based on sensory input (relative position or orientation of the target). This computation is not performed by a separate, discrete processing unit but is intrinsic to the way the pursuer's motion is continuously modified by hydrodynamic and cognitive steering rules. The adaptation of speed in the second strategy also represents a form of embodied computation, reacting to the relative position and adjusting propulsion speed accordingly within the physical model itself. While basic, these mechanisms represent computation directly embodied in the system's physical response.
    *    Implicit/Explicit: Mixed
        *  Justification: The paper uses "cognitive steering" and "adaptation" terms, implying a form of information processing and decision making, albeit simplified. The steering rules given by equations and described adaptation process represent algorithmic steps. These computational steps are embodied directly in the model's physics via the manipulation of the squirmer's surface flow field, thus constituting embodied computation, even if minimal. The "cognitive" label is metaphorical, but the steering and adaptation are functional forms of embodied computation.

**(Conditional: If M5.1 is "Yes", include M5.2-5.4)**

### **5.2 Computation Type:**

*   **Vector ID:** M5.2
*   **Vector Type:** Classification
    *   Content: Analog
    *   CT-GIN Mapping: Defines the `ComputationNode` type in CT-GIN. `ComputationNode` attributes: `computationType: Analog`
    *    Implicit/Explicit: Explicit
    *    Justification: The steering and speed adaptation mechanisms are implemented as continuous, analog processes. The angular velocity adjustments and speed changes are proportional to continuous variables (vector products, relative position components). The system operates in continuous time and space, with adaptations defined by differential equations (in the methods section, for speed adaptation). These are not digitized or discrete computational steps but continuous analog operations reflective of physical processes adjusting motion parameters.

### **5.3 Computational Primitive:**

*   **Vector ID:** M5.3
*   **Vector Type:** Function
    *   Content: The computational primitives embodied in the system are:
        1.  **Vector Cross Product:** Used in the reorientation steering rule (ω<sub>0</sub> = C<sub>0</sub> (e<sub>p</sub> × e<sub>c</sub>)). This vector operation computes the required rotational direction for alignment, encoding directional information.
        2.  **Vector Scalar Product:** Used in the speed adaptation of the alignment strategy (via e<sub>p</sub> ⋅ e<sub>c</sub>). This scalar operation computes the component of the relative position vector along the pursuer's direction, providing a scalar value to modulate speed.
        3.  **Proportional Control:** Both steering and speed adaptation are based on proportional control. The magnitude of angular velocity adjustment and speed change are proportional to the vector products, implementing a feedback control loop to continuously adapt motion based on sensory input.

    *   **Sub-Type (if applicable):** Vector Cross Product, Vector Scalar Product, Proportional Control
    *   CT-GIN Mapping: Defines the primary function of the `ComputationNode` in CT-GIN. `ComputationNode` attributes: `primitiveFunction: Vector Cross Product`, `primitiveFunction: Vector Scalar Product`, `primitiveFunction: Proportional Control`
    *   Implicit/Explicit: Explicit
    * Justification: These primitives are directly derived from the equations defining the steering and speed adaptation algorithms (Eqs. 1, 13, 14, 19, 22). Vector algebra operations and proportional feedback are the fundamental computational steps explicitly performed by the embodied mechanisms in the model.

### **5.4 Embodied Computational Units**
* **Vector ID:** M5.4
* **Vector Type:** Table
*   Table:
| Unit ID | Description | Processing Power | Energy/Operation | Freq/Resp. Time | Bit-Depth | Data Source | Implicit/Explicit | Justification |
| :------ | :---------- | :--------------- | :--------------- | :--------------: | :-------: | :----------: |:-----------------:| :-----------------:|
| 1 | Steering Mechanism (Reorientation & Alignment) | N/A (Analog Processing) | N/A (Analog, embedded in hydrodynamics) | ~ Rotational Diffusion Time (D<sub>R</sub><sup>-1</sup>) | N/A (Analog) | Eq. (2) | Implicit |  Processing power and energy not quantified in digital terms. Response time is related to the intrinsic timescale of rotational diffusion, which is influenced by maneuverability. Bit-depth is not applicable for analog computation. |
| 2 | Speed Adaptation Mechanism | N/A (Analog Processing) | N/A (Analog, embedded in hydrodynamics) | ~ Speed Relaxation Time (R<sub>sq</sub>/κv<sub>max</sub>) | N/A (Analog) | Eq. (20) | Implicit | Processing power and energy not quantified in digital terms. Response time related to speed relaxation process defined by system parameters. Bit-depth not applicable for analog computation. |

## M6: Temporal Dynamics
*   **Vector ID:** M6
*   **Vector Type:** Temporal

### **6.1 Timescales:**

*   **Vector ID:** M6.1
*   **Vector Type:** ParameterTable
    *   Table:
        | Timescale Description | Value | Units | Source | Implicit/Explicit | Justification |
        | :-------------------- | :---: | :---: | :----: | :----------------: | :------------: |
        | Rotational Diffusion Time (τ<sub>R</sub>) | D<sub>R</sub><sup>-1</sup> | s (inferred) | Eq. (2) | Implicit | Characteristic timescale for random rotational motion due to thermal fluctuations. Set by rotational diffusion coefficient D<sub>R</sub>. Units inferred from microswimmer context. |
        | Maneuverability Timescale (τ<sub>Ω</sub>) | Ω<sup>-1</sup>D<sub>R</sub><sup>-1</sup> | s (inferred) | Eq. (2) | Implicit | Timescale for active reorientation driven by steering mechanism. Relates maneuverability Ω and rotational diffusion timescale. Units inferred. |
        | Advection Timescale (τ<sub>adv</sub>) | σ/v<sub>p</sub> | s (inferred) | Eq. (2) | Implicit | Timescale for advection of a squirmer over its diameter σ due to propulsion speed v<sub>p</sub>. Related to Péclet number Pe= v<sub>p</sub>σ/D<sub>R</sub>. Units inferred. |
        | Speed Adaptation Relaxation Time (τ<sub>adapt</sub>) | R<sub>sq</sub>/(κv<sub>max</sub>) | s (inferred) | Eq. (20) | Implicit | Timescale over which pursuer speed adapts to target position in the alignment and speed adaptation strategy. Set by speed adaptation parameters. Units inferred. |
    *   **Note:** Timescales are derived from key parameters and physical interpretations of microswimmer dynamics. Numerical values with SI units are not provided, necessitating qualitative assessment and inferred units based on typical microscale contexts.

### **6.2 Active Inference:**

*   **Vector ID:** M6.2
*   **Vector Type:** Assessment
    *   Content: No
    *   Justification: The system does not demonstrate active inference. There's no indication of: (1) prediction of future target states or environmental changes, (2) selection of actions to minimize prediction error or surprise, or (3) internal models of the target or the environment that are updated based on interactions. The pursuer's behavior is reactive and adaptive, but based on immediate sensory input—the current position or orientation of the target. The steering rules and speed adaptation mechanisms are purely reactive, directly adjusting motion parameters in response to the currently perceived state of the target without anticipation, prediction, or internal model-based reasoning. The system is designed for immediate pursuit and lacks the predictive, model-based components characteristic of active inference.
    *   Implicit/Explicit: Explicit
        *  Justification: The system is described as reactive and adaptive, directly responding to current sensory information. Absence of any predictive component, internal models, or error minimization based on future expectations is evident from the model description. The focus is on present-moment reaction, not predictive or inferential behavior, thus excluding active inference.
    *   **If Yes/Partial, provide examples of testable CT-GIN metrics that *could* be used to quantify active inference:** [N/A]

## M7: Adaptation
*   **Vector ID:** M7
*   **Vector Type:** Adaptation

### **7.1 Adaptive Plasticity Presence:**

*   **Vector ID:** M7.1
*   **Vector Type:** Binary
    *   Content: Yes
    *   Justification: The system exhibits adaptive plasticity in its motile behavior. The pursuer dynamically *changes its behavior* (propulsion direction, and in one strategy, speed) in response to ongoing sensory input from the target. This is beyond simple stimulus-response as the pursuer's motion is *continuously modulated* in real-time based on the evolving relative configuration with the target. The steering mechanisms cause persistent changes in the pursuer's trajectory as it adapts to the target's movement, demonstrating a form of behavioral plasticity—dynamic adjustment of behavior in response to environmental interaction. While steering rules themselves are fixed, their application results in continuously adapting motion patterns, reflecting adaptive plasticity of the system's behavioral output.
    *    Implicit/Explicit: Mixed
        * Justification: The paper explicitly uses "adaptation" in describing steering and speed mechanisms, highlighting their dynamic response to the target. The continuous modulation of pursuer motion based on sensory input signifies adaptive changes to behavioral patterns (trajectories, cooperative states), indicating behavioral plasticity, even if the underlying rules are fixed. This assessment involves both explicit statements of "adaptation" and implicit inference about the dynamic and changing nature of behavior in response to interaction.

**(Conditional: If M7.1 is "Yes", include M7.2)**

### **7.2 Adaptation Mechanism:**

*   **Vector ID:** M7.2
*   **Vector Type:** Description
    *   Content: The adaptation mechanisms are based on feedback-controlled adjustment of the pursuer's propulsion direction and, in one strategy, speed, utilizing sensory input from the target:
        1.  **Reorientation Steering:** Feedback from the target's relative position (vector e<sub>c</sub>) drives direction adaptation. The pursuer's angular velocity ω<sub>0</sub> is continuously adjusted proportionally to the vector cross product (e<sub>p</sub> × e<sub>c</sub>), creating a feedback loop that aligns e<sub>p</sub> towards e<sub>c</sub>. This is a proportional feedback control acting on orientation.
        2.  **Alignment Steering with Speed Adaptation:** Dual feedback mechanism. a) Direction Alignment: Feedback to align e<sub>p</sub> with target direction e<sub>t</sub> (e<sub>aim</sub> = e<sub>t</sub>). b) Speed Adaptation: Feedback from relative position component (e<sub>p</sub> ⋅ e<sub>c</sub>) modulates pursuer speed v<sub>p</sub>. If e<sub>p</sub> ⋅ e<sub>c</sub> < 0 (behind target), v<sub>p</sub> increases; if e<sub>p</sub> ⋅ e<sub>c</sub> > 0 (ahead), v<sub>p</sub> decreases, with a maximum speed limit. This is a combined feedback mechanism adjusting both direction and speed based on target state.

        These adaptation mechanisms are driven by environmental signals (target's position and orientation) and implemented through predefined feedback rules (Eqs. 1, 13, 14, 19, 22). These are forms of reactive, proportional feedback adaptation rather than more complex learning mechanisms such as reinforcement or Hebbian learning.
    *   CT-GIN Mapping: Defines the `AdaptationNode` type in CT-GIN and `Monad` edges representing adaptation mechanisms. `AdaptationNode` attributes: `adaptationMechanism: Proportional Feedback Control (Orientation)`, `adaptationMechanism: Proportional Feedback Control (Speed & Orientation)`.  `Monad` edges connect `AdjunctionEdge: Hydrodynamic Interaction` to `BehaviorArchetypeNode: Locomotion`, indicating how local interactions and rules adapt behavior. Adaptation mechanism type: "Proportional Feedback Control".
    *    Implicit/Explicit: Explicit
        *  Justification: The adaptation mechanisms are clearly detailed through the descriptions of steering strategies and the speed adaptation rule. Feedback variables (relative position vector, relative orientation vector), proportional control nature, and the underlying equations (Eqs. 1, 13, 14, 19, 22) providing operational definitions for these mechanisms are explicitly provided in the paper.

## M8: Emergent Behaviors
*   **Vector ID:** M8
*   **Vector Type:** Behavior

### **8.1 Behavior Description:**

*   **Vector ID:** M8.1
*   **Vector Type:** Description
    *   Content: The primary emergent functional behaviors are hydrodynamic pursuit of a target and the formation of stable cooperative motion states between pursuer and target microswimmers. Specific, observable behaviors include:
        1.  **Target Capture for Pullers (Reorientation Steering):** Puller pursuers, using reorientation steering, effectively approach and maintain very close proximity, often achieving "touching" configurations with the target. Operationally observed as sustained close pursuer-target distance.
        2.  **Stable Leader-Follower Pursuit for Pushers (Reorientation Steering):** Pusher pursuers, with reorientation steering, establish a stable pursuit mode where the pursuer follows the target, maintaining a finite, average separation distance in a leader-follower configuration. Operationally seen as stable average pursuer-target distance greater than squirmer diameter.
        3.  **Cooperative Helical Motion in Helical Target Trajectory:** When the target follows a helical path, the pursuer dynamically adapts and follows on a correlated helical trajectory, exhibiting cooperative helical motion of the pair. Operationally seen as correlated helical trajectories.
        4.  **Cooperative Circular Motion via Alignment & Speed Adaptation (Pushers):** For pusher pursuers using alignment and speed adaptation steering, a stable cooperative state of circular motion emerges, with the pair orbiting in a stable circular trajectory. Operationally seen as sustained circular trajectories.

    *   CT-GIN Mapping: Defines the `BehaviorArchetypeNode` in CT-GIN. `BehaviorArchetypeNode` attributes: `behaviorType: Hydrodynamic Pursuit`, `behaviorType: Cooperative Motion`, `behaviorType: Target Capture (Pullers)`, `behaviorType: Leader-Follower Pursuit (Pushers)`, `behaviorType: Cooperative Helical Motion`, `behaviorType: Cooperative Circular Motion`. Specificity is encoded through attributes defining behavior subtypes and conditions.
    *    Implicit/Explicit: Explicit
       *  Justification: The functional behaviors are explicitly described in the Results section using clear, operational terms such as "target capture," "leader-follower motion," "cooperative helical motion," and "circular motion." Figures and supplementary movies directly visualize and illustrate these emergent behaviors, and quantitative metrics are used to characterize them (average distances, alignment parameters).

### **8.2 Behavior Robustness:**

*   **Vector ID:** M8.2
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The emergent behaviors demonstrate moderate robustness. The phase diagrams (Fig. 2e) and parameter-dependent plots (Figs. 2b, 3c, 4c, 5e) indicate that the stability and type of cooperative motion are dependent on parameters like Péclet number, maneuverability, and speed ratio. This suggests the existence of operational windows for stable pursuit but also sensitivity to parameter changes. The simulations include thermal noise through the MPC fluid model, implying a degree of robustness against thermal fluctuations, especially at higher maneuverability. However, robustness against other types of perturbations (e.g., variability in squirmer properties, external flow disturbances, stronger noise sources) is not explicitly tested or quantified. The score of 7 reflects moderate robustness within simulation parameters and against thermal noise, but with recognized parameter dependencies and unexplored robustness to wider perturbations.
    *   Implicit/Explicit: Mixed
        *  Justification: Robustness against thermal fluctuations is implicitly tested via the inclusion of thermal noise in simulations. Parameter-dependent phase diagrams (Fig. 2e) explicitly define regions of stable pursuit, implying robustness within these regions but boundaries to that robustness. Robustness to other perturbation types is not explicitly investigated, making the robustness assessment mixed—partly explicit (thermal noise robustness in simulations), partly implicit/qualitative (parameter sensitivity and unassessed perturbations).
    *   CT-GIN Mapping: This score contributes to the reliability attributes of the `BehaviorArchetypeNode` in the CT-GIN. Attribute: `robustnessScore: 7 (Moderate)`.

### **8.3 CT-GIN Emergent Behavior Validation**

*    **Vector ID:** M8.3
*    **Vector Type:** Validation
     *  Content: Validation methods used to support claims of emergent behaviors include:
         1.  **Computational Simulations:** Primary validation is through detailed numerical simulations using Multiparticle Collision Dynamics (MPC).  Large number of simulation runs generate trajectory data, from which emergent patterns are identified and characterized.
         2.  **Statistical Averaging:** Results are statistically validated by averaging over multiple independent simulation runs (at least 10 realizations) to account for thermal noise and stochasticity. Average distances, alignment parameters, and phase diagrams are generated from ensemble averages.
         3.  **Theoretical Comparison:** Simplified theoretical far-field hydrodynamic approximations (Supplementary Note 1) are derived and compared with simulation results. Semi-quantitative agreement between theory and simulations provides theoretical support for observed trends and stability conditions.
         4.  **Operational Definitions:** Emergence of stable pursuit is operationally defined using a threshold distance (r<sub>c</sub> < 4σ).  Quantifiable metrics (average distances, alignment parameters, phase diagrams) are used to characterize and validate emergent behaviors.

         Limitations: Validation is primarily computational and theoretical. No direct experimental validation in physical microswimmer systems is presented. Robustness validation is limited to thermal noise and parameter variations within the simulation framework. Reproducibility within the computational framework is implied by standard simulation protocols but not explicitly demonstrated through independent code or laboratory replication.

     *   Implicit/Explicit: Mixed
    *   Justification: Validation methods are explicitly described: computational simulations, statistical averaging, theoretical comparison, and operational definitions. Limitations inherent in computational validation (lack of experimental confirmation, limited robustness assessment) are implicitly understood through the described methodology and scope of a theoretical paper, making the validation assessment Mixed—explicit in methods used, implicit in scope and limitations of computational validation.

## M9: Cognitive Proximity
*   **Vector ID:** M9
*   **Vector Type:** Cognition

### **9.1 Cognitive Mapping:**

*   **Vector ID:** M9.1
*   **Vector Type:** Description
    *   Content: The paper draws a metaphorical mapping between the self-steering microswimmer system and basic cognitive processes, using terms like "cognitive self-steering," "intelligent squirmers," and "cognitive flocking model." The "cognition" is explicitly acknowledged as "minimal" and a "conceptual strategy" different from more complex forms of cognition in animals or robots. The steering and adaptation mechanisms are presented as simplified analogs of cognitive functions like sensing and responding to environmental cues. The mapping is intended to highlight the adaptive and goal-directed nature of the microswimmer pursuit behavior, drawing loose parallels to cognitive processes in biological systems, even while acknowledging the significant differences in complexity and capability. The paper explicitly mentions extending the concept of cognition to "aneural systems" to justify using "cognition" in this context of minimal adaptive behavior.
    *   CT-GIN Mapping: `CognitiveMappingEdge` in CT-GIN, linking `BehaviorArchetypeNode: Pursuit` to `CognitiveFunctionNode: Minimal Cognition (Adaptive Steering)`. Mapping described as metaphorical and limited, highlighting analogies to basic cognitive processes.
    *   Implicit/Explicit: Explicit
    * Justification: The cognitive mapping is explicit in the paper's language (use of cognitive terms) and explicit qualification of this "cognition" as minimal, conceptual, and metaphorical. The analogies to cognitive functions and the acknowledged limitations of the model's cognitive abilities are explicitly stated within the discussion and introduction.

### **9.2 Cognitive Proximity Score:**

*   **Vector ID:** M9.2
*   **Vector Type:** Score
    *   Score: [2]
    *   Justification: Based on the CT-GIN Cognizance Scale, the system scores a 2, aligning with Level 2: Sub-Organismal Responsivity. The system exhibits adaptive behavior (steering, speed adaptation—behavioral plasticity), going beyond simple stimulus-response (Level 1), but lacks representation, goal-directedness in a robust sense, or internal models (fails to reach Level 3). The "cognition" is limited to basic reactive adaptation, not complex cognitive functions. There is no evidence of memory, planning, decision-making beyond immediate steering, or model-based reasoning—features of higher cognitive levels (Level 3 and above). The system's behavior is adaptive within a limited repertoire (pursuit) but lacks flexibility, learning, or higher-order cognitive capacities, fitting the profile of sub-organismal responsivity. The score of 2 reflects the minimal, metaphorical use of "cognitive" in the paper and the system's limited cognitive capabilities within the CT-GIN scale.
    *   Implicit/Explicit: Mixed
    *  Justification: The score is justified by comparing the system’s demonstrated capabilities against the CT-GIN Cognizance Scale levels. The limited nature of the cognition is explicitly acknowledged in the paper. System characteristics that fit Level 2 (basic adaptation but lack of higher functions outlined for Level 3+) are inferred from the system description, leading to a Mixed justification—explicit score level mapping, but implicit assessment of capability limitations against scale criteria.

**CT-GIN Cognizance Scale:**

*   **Level 0: Non-Cognitive:** Purely reactive system.  No internal state beyond immediate stimulus-response.
*   **Level 1: Simple Responsivity:** Basic stimulus-response behavior.  Reactions are fixed and predetermined.
*   **Level 2: Sub-Organismal Responsivity:**  Behavior exhibits basic forms of adaptation or plasticity, but lacks complex representation or goal-directedness.  **[System best fits here]**
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
    | Sensing/Perception               |       4      | Minimal, indirect "sensing" via hydrodynamic interactions. Detects relative position/orientation. | `CognitiveFunctionNode: Sensing/Perception` linked from `AdjunctionEdge: Hydrodynamic Interaction` | Implicit          | Sensing mechanism is indirect, through fluid interaction, not dedicated sensors in the model. Score reflects minimal, fluid-mediated sensing ability. |
    | Memory (Short-Term/Working)        |       1      | Very limited.  Reacts to current sensory input; no working memory for recent past states. | None                             | No                | No discernible mechanism for short-term or working memory. Reacts instantaneously.                           |
    | Memory (Long-Term)                 |       0      | Absent. No mechanism for long-term memory or persistent state modifications.           | None                             | No                | Model lacks any form of long-term memory or historical state-dependent behavior.                                  |
    | Learning/Adaptation              |       3      | Basic adaptation via steering and speed adjustments based on immediate feedback. Fixed adaptation rules, no higher-level learning. | `CognitiveFunctionNode: Learning/Adaptation` linked from `AdaptationNode: Feedback Control` | Explicit          | Adaptation mechanism explicitly defined, proportional feedback. Score reflects limited form of reactive adaptation, not complex learning. |
    | Decision-Making/Planning          |       1      | Minimal. Rudimentary "decisions" are limited to steering direction adjustments as set by rules. No planning, anticipation, or complex choice selection. | None                             | No                | Decision-making limited to basic steering adjustments; no evidence of planning or deliberate choice among alternatives.                 |
    | Communication/Social Interaction |       0      | Absent. Model considered pursuer-target pairs in isolation. No interaction with other agents or communication mechanisms considered. | None                             | No                | System studied as isolated dyad.  Communication and social interaction not within scope. |
    | Goal-Directed Behavior            |       2      | Weakly goal-directed: pursuit of target. Goal is implicit in steering rules, not explicitly represented or optimized. | `CognitiveFunctionNode: Goal-Directed Behavior` linked from `BehaviorArchetypeNode: Pursuit` | Implicit          | Pursuit behavior indicates a weak, implicit goal direction. Score is low due to simplicity and lack of explicit goal representation in model. |
    | Model-Based Reasoning              |       0      | Absent.  No internal models of the target, environment, or self. Behavior is purely reactive, not model-based.          | None                             | No                | Model explicitly a reactive system without any internal model-based reasoning capabilities.                      |
    | **Overall score**                 |      [1.6]       |                                                                                       |                                   |                     |                |

    *   **Note:** Overall score is calculated as the numerical average of individual function scores.

## M10: Criticality Assessment
*   **Vector ID:** M10
*   **Vector Type:** Criticality

### **10.1 Criticality:**

*   **Vector ID:** M10.1
*   **Vector Type:** Assessment
    *   Content: Unclear
    *   Justification: The paper provides no analysis or discussion regarding criticality or operation near a critical point. No mention is made of scale-free behavior, power laws, long-range correlations, or phase transitions in the context of criticality. While the system exhibits emergent cooperative states, the emergence is described as a function of parameters like Péclet number and maneuverability leading to stable or unstable pursuit regimes, rather than in terms of critical phenomena.  The inherent thermal fluctuations in the fluid model might be tangentially related to criticality in some active matter systems, but no explicit analysis or investigation of criticality is presented or suggested in the excerpt. Therefore, based on the provided text, it is unclear if the system's dynamics are linked to criticality.
        *   Critical Parameters (If Yes/Partial): [N/A]
        *   Evidence: [No evidence of criticality analysis or data presented in the excerpt.]
    *   Implicit/Explicit: Explicit
    *    Justification: The absence of any discussion or analysis of criticality in the paper is explicit. The focus is on emergent cooperative states and pursuit strategies in parameter space but not investigated through the lens of criticality, phase transitions, or related signatures. Lack of explicit statements or data related to criticality justifies labelling this aspect as "Unclear" with explicit justification of absence of relevant information in the text.

## M11: Review Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Review")**

N/A

## M12: Theoretical Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Theoretical")**

*   **Vector ID:** M12
*   **Vector Type:** Theory

### **12.1 Theoretical Rigor:**

*   **Vector ID:** M12.1
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The theoretical framework exhibits good rigor for a computational study in active matter physics. It employs established models like the squirmer model for microswimmers and Multiparticle Collision Dynamics (MPC) for fluid simulation, both validated methods in this field. The steering mechanisms and speed adaptation are mathematically well-defined through equations, providing a clear and operational model. Implicit assumptions are generally standard in microswimmer modeling (e.g., low Reynolds number regime, spherical squirmers, idealized surface flow). While derivations are not extensively laid out in the excerpt, the methodology references established literature and supplementary material (as indicated), implying soundness of underlying theoretical derivations. The model is internally consistent within its specified domain. Semi-quantitative agreement with far-field approximations offers additional support for the theoretical framework's validity. Overall, the theoretical rigor is judged to be strong for the type of computational modeling presented.
       * Implicit/Explicit: Mixed
       *  Justification: The use of well-established models and mathematical formulations is explicit, contributing to rigor. Detailed derivations and full lists of assumptions are implicit, but reasonably assumed to be aligned with established practices in the field of microswimmer modeling and computational fluid dynamics. The overall assessment of "good" rigor is Mixed, based on both explicit model components and implicit reliance on standard practices.

### **12.2 Realization Potential:**

*   **Vector ID:** M12.2
*   **Vector Type:** Score
    *   Score: [6]
    *   Justification: The potential for physical realization is assessed as moderate (score of 6). While the squirmer model is a generic representation, it captures essential hydrodynamic features of microswimmers and active colloids. The concept of self-steering through surface flow modulation is conceptually aligned with current efforts in synthetic active matter. Realizing the specific steering strategies (reorientation, alignment & speed adaptation) in synthetic microswimmers represents a significant engineering challenge, as noted in the paper ("major challenges"). It would require sophisticated mechanisms to sense target position/orientation and dynamically control the surface flow field of artificial microswimmers, potentially using chemical gradients, light stimulation, or magnetic fields coupled with engineered actuators and sensors—approaches under active research, but not yet fully mature. The system is conceived for low Reynolds number fluids, which is experimentally achievable at microscale. Fundamental limitations reside in the complexity of precise surface flow control and achieving robust, noise-resistant steering and adaptation functionalities in practical micro-robotic systems. Realization is considered plausible within the scope of ongoing advances in micro-robotics and active materials, though not immediately straightforward.
    *   Implicit/Explicit: Mixed
    *  Justification: Realization potential is evaluated based on the current state of micro-robotics and active matter research, requiring a Mixed assessment. Plausibility is inferred from the generic nature of the squirmer model and conceptual alignment with active colloids and micro-robotics. The paper's acknowledgement of "major challenges" for synthetic microswimmers explicitly highlights the hurdles to physical realization, leading to a moderate score of 6, acknowledging plausibility but also significant engineering challenges.

### **12.3 Potential for Future CT-GIN Implementation Score**

* **Vector ID:** M12.3
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The theoretical framework demonstrates good potential (score of 7) for guiding future research and development pertinent to CT-GIN implementation, particularly in active matter and micro-robotic systems. The model offers a clear, albeit simplified, example of embodied computation (steering rules) and emergent self-organization leading to cooperative behaviors (pursuit, stable configurations). It systematically explores different steering strategies and their impact on emergent dynamics, providing insights relevant for designing artificially cognitive micro-agents. Novelty resides in the comparison of steering strategies and their hydrodynamic consequences. Potential impact lies in informing the design of micro-robots for tasks like targeted transport or environmental sensing guided by minimal cognitive rules. Alignment with CT-GIN principles is present in demonstrating minimal cognition and emergent order, though higher-level cognitive functions and complex CT-GIN aspects are absent in this simplified model. The framework provides a sound starting point for exploring more complex CT-GIN implementations in active matter, indicating good future potential within CT-GIN development, although further expansion to incorporate memory, more sophisticated computation, and learning is needed to fully realize this potential.
    *    Implicit/Explicit: Mixed
    *   Justification: The potential is assessed based on novelty, impact, and alignment with CT-GIN principles. The framework's clear demonstration of minimal cognition, embodied computation, and emergent behavior is explicitly evident. Relevance for future CT-GIN applications and potential for expansion to more complex systems are inferred based on these demonstrated strengths, but the need for significant further development to advance beyond minimal cognition (memory, learning, etc.) leads to a score of 7, indicating good but not outstanding future potential in its current simplified form.

## M13: Overall Assessment & Scoring
*   **Vector ID:** M13
*   **Vector Type:** Overall

### **13.1 CT-GIN Readiness Score:**

*   **Vector ID:** M13.1
*   **Vector Type:** Score
*   **Calculated Score:** [6.0]

**CT-GIN Readiness Summary Table:**

| CT-GIN Aspect                   | Strength (Yes/Partial/No) | Key Supporting Metrics (with units) | Limitations (Missing Metrics/Data Gaps)                                           | Improvement Areas (Future Research)                                          |
| :------------------------------ | :-----------------------: | :-----------------------------------| :------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| Energy Flow Efficiency          | Partial                   | Qualitative Assessment: Moderate    | Quantitative efficiency metrics, Energy dissipation measurements                | Quantify energy efficiency, Optimize steering for energy-efficient pursuit      |
| Memory Fidelity                 | No                        | N/A                                 | Memory Retention Time, Capacity, Readout Accuracy, Operations Energy Cost, Robustness Metrics | Incorporate memory mechanisms, Explore memory-enhanced adaptation strategies  |
| Organizational Complexity       | Yes                       | Emergent Cooperative States         | Yoneda Embedding Score: 6 (Moderate mapping fidelity)                        | Enhance predictability of global order, Refine local-to-global rule mapping    |
| Embodied Computation            | Yes                       | Analog Primitives: Vector Products, Proportional Control | Quantified Processing Power, Energy per Operation, Freq/Resp. Time, Bit-Depth | Explore more complex computational primitives, Quantify computational performance |
| Temporal Integration            | No                        | Relevant Timescales Identified (Qualitative) | Precise timescale values with units, Active Inference assessment                 | Investigate active inference, Explore predictive steering mechanisms         |
| Adaptive Plasticity             | Yes                       | Feedback-Controlled Steering & Speed Adaptation | Detailed descriptive characterization, Limited formalization of adaptation | Formalize adaptation mechanisms mathematically, Explore advanced learning rules |
| Functional Universality         | No                        | Primarily limited to Pursuit Behavior            | Demonstration of functional diversity beyond pursuit                         | Explore broader range of behaviors (e.g., navigation, pattern formation)        |
| Cognitive Proximity            | Partial                   | Cognitive Proximity Score: 2/10 (Level 2) | Cognitive Function Checklist Scores (limited functions scored above 2)          | Enhance cognitive function scores, Move towards higher Cognizance Scale levels   |
| Design Scalability & Robustness | Partial                   | Behavior Robustness Score: 7/10 (moderate robustness against thermal noise) | Scalability analysis, Robustness against wider perturbations                   | Enhance robustness against wider disturbances, Explore scalable implementations |
| **Overall CT-GIN Readiness Score** |        |   |   |      |


### **13.2 Qualitative CT-GIN Assessment Conclusion:**

*   **Vector ID:** M13.2
*   **Vector Type:** Textual Summary
    *   Content: This paper presents a theoretically rigorous computational model of cognitive self-steering microswimmers, demonstrating emergent cooperative pursuit behaviors and several forms of stable motion from minimal local interaction rules and embodied computation (steering mechanisms). Key strengths include the clear formulation of steering strategies, evidence for self-organization, and demonstration of basic adaptive plasticity. However, the system exhibits significant limitations in terms of cognitive proximity, scoring at Level 2 (Sub-Organismal Responsivity) on the CT-GIN Cognizance Scale due to the absence of memory, limited computational primitives, lack of active inference, and a rudimentary form of goal-directed behavior. Energy efficiency and robustness, while present to a moderate degree within the simulation context, remain largely unquantified. Overall, while providing valuable theoretical insights into minimal cognitive behavior and self-organization in active matter, the system currently demonstrates a low level of CT-GIN readiness. Future development towards higher CT-GIN readiness would require incorporating memory mechanisms, more complex embodied computation, active inference capabilities, and enhanced robustness and scalability.

### **13.3 CT-GIN Refinement Directions:**

*   **Vector ID:** M13.3
*   **Vector Type:** Recommendations
    *   * **Integrate Memory:** Incorporate memory mechanisms into the pursuer model to enable learning and history-dependent behavior, allowing adaptation based on past experiences beyond immediate reactive responses.
    *   **Enhance Embodied Computation:** Explore richer computational primitives and architectures within the hydrodynamic system itself, moving beyond basic vector operations towards potentially neuromorphic or reservoir computing approaches embedded in the material behavior.
    *   **Implement Active Inference:** Design mechanisms for the pursuer to develop and utilize internal models of the target and environment, enabling predictive steering and action selection to minimize surprise or prediction error.
    *   **Quantify and Optimize Energy Efficiency:** Develop metrics and methods to quantify energy consumption and dissipation, and explore steering strategies that optimize pursuit and cooperative motion for minimal energy expenditure.
    *   **Improve Robustness and Scalability:** Investigate and enhance robustness of emergent behaviors against a wider range of perturbations, and explore scalability of the model and its emergent properties to multi-agent systems and complex environments.
    *   **Explore Experimental Realization:** Pursue experimental realization of the proposed steering mechanisms in synthetic microswimmers to validate the theoretical predictions and explore practical challenges and opportunities for implementation of cognitive micro-robotic systems.

## M14: CT-GIN Knowledge Graph

*   **Vector ID:** M14
*   **Vector Type:** Visualization

### **14.1. CT-GIN Knowledge Graph:**
* **Content:**
[__N/A - Text-based output, cannot insert image.__]

## M15: Relationship Vectors
*   **Vector ID:** M15
*   **Vector Type:** Relationships
*   Relationships:
        | Source Vector ID | Target Vector ID | Relationship Type |
        | ------------- | ------------- | ----------------- |
        | M2.1 | M2.2 | EnergyTransduction |
        | M2.2 | M2.4 | EnergyDissipation |
        | M4.2 | M4.3 | Adjunction |
        | M7.2 | M8.1 | Monad |
        | M8.1 | M9.1 | CognitiveMapping |

## M16: CT-GIN Template Self-Improvement Insights

*   **Vector ID:** M16
*   **Vector Type:** Feedback

### **Template Feedback:**

*    **Vector ID:** M16.1
*   **Vector Type:** Text
Provide specific, actionable feedback on the *CT-GIN template itself*, based on this analysis:
    *   **Missing Probes:** The template is generally comprehensive for this theoretical paper. However, for future analyses, especially of experimental works, probes related to *fabrication complexity*, *material scalability*, and *long-term stability/degradation* of system components could be beneficial in Module M1 and M8.2 (Robustness).
    *   **Unclear Definitions:** The definitions are mostly clear. The distinction between "Adaptive Plasticity" and "Memory" could be further clarified. Perhaps emphasizing *persistent modification* of internal state *beyond stimulus offset* more strongly in the "Memory" definition would be useful to differentiate it more decisively from adaptive responses.
    *   **Unclear Node/Edge Representations:** The guidance for GIN mapping was adequate. For textual output, no issues encountered. For a visual output, perhaps more illustrative examples for annotating nodes and edges with attributes directly in the template instructions could be helpful.
    *   **Scoring Difficulties:** Subjectivity in scoring, especially for "Cognitive Proximity" (M9.2), is inherent. Providing more detailed behavioral anchors for each level in the CT-GIN Cognizance Scale rubric, with specific example behaviors, would likely improve inter-rater reliability and consistency. For "Robustness" (M8.2), specifying typical perturbation types to consider during scoring (e.g., environmental noise, parameter drift, component failure) could provide more concrete guidance.
    *   **Data Extraction/Output Mapping:** Data extraction and mapping to the template was generally straightforward for this theoretical paper. The structured template facilitated organized extraction and reporting.
    *   **Overall Usability:** The template is well-structured and logically organized, although quite detailed. For very complex papers, breaking down long sections (e.g., M4.2, M8.3) into subsections within the template could enhance readability and ease of analysis within the template structure itself.
    * **Specific Suggestions:**
        * Add "Fabrication Complexity", "Material Scalability", and "Long-Term Stability" probes under M1 and M8.2 robustnes.
        * Refine "Memory" definition (M3) to emphasize 'persistent change beyond stimulus'.
        * Enhance CT-GIN Cognizance Scale & Robustness Score rubrics (M9.2, M8.2) with more detailed behavioral anchors and examples for each level/score value to improve scoring consistency.
        * Consider optional sub-sectioning for long descriptive sections in template for improved readability during in-template analysis.
```