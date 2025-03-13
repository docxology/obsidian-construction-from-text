# Non-reciprocal multifarious self-organization

__Paper Type:__ Experimental

## M1: System Overview & Implementation
*   **Vector ID:** M1
*   **Vector Type:** Overview

### **1.1 System Description**

*   **Vector ID:** M1.1
*   **Vector Type:** Description
    *   Content: The system is a theoretical model of shape-shifting self-organization using programmable non-reciprocal interactions between tiles on a 2D lattice. It uses two types of tiles, A and B, which interact with each other through reciprocal and non-reciprocal interactions. The system is designed to autonomously transition between a predefined sequence of self-assembled structures (up to four in the examples shown) starting from an initial seed configuration. The core components are the tiles, interaction matrices (reciprocal U and non-reciprocal Rnr), and a Monte Carlo simulation environment that models the system's dynamics. The purpose is to demonstrate that non-reciprocal interactions can enable programmable dynamical control of self-assembled structures and transitions between them, mimicking aspects of living systems' self-organization capabilities.
    *   CT-GIN Mapping: `SystemNode` attributes: `systemType: Theoretical Model`, `domain: Material Science, Self-Assembly`, `mechanism: Non-reciprocal interactions-driven transitions`, `components: Tiles (A, B), Reciprocal interaction matrix (U), Non-reciprocal interaction matrix (Rnr), Monte Carlo simulation`, `purpose: Programmable shape-shifting, Dynamical control of self-assembly`.
    *   Implicit/Explicit: Mixed
        *  Justification: The system components and purpose are explicitly stated, such as the use of tiles A and B and the goal of shape-shifting. However, the detailed operational description is mixed with implicit assumptions about the Monte Carlo simulation and the precise implementation of interaction matrices, which are further detailed in the methods section but require interpretation to fully grasp the operational aspect.

### **1.2 Implementation Clarity**

*   **Vector ID:** M1.2
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The implementation clarity is reasonably high for a theoretical paper. The model is described conceptually with figures illustrating the interactions and transitions. The Methods section provides details on defining the interaction matrices and the Monte Carlo simulation procedure. However, certain specifics of the parameter selection and the precise algorithmic steps within the Monte Carlo simulation are not exhaustively detailed, requiring some implicit understanding of common practices in computational physics and statistical mechanics. The connection between the abstract model and potential physical implementations in soft matter systems is discussed but remains at a conceptual level.
    *   Implicit/Explicit: Mixed
        * Justification: The overall implementation strategy is explicit using Monte Carlo simulations and interaction matrices. However, the fine-grained details of the algorithm and parameter choices are somewhat implicit, assuming a certain level of background knowledge in computational modeling.

### **1.3 Key Parameters**

*   **Vector ID:** M1.3
*   **Vector Type:** ParameterTable
    *   Table:
        | Parameter Name | Value | Units | Source (Fig/Table/Section) | Implicit/Explicit | Data Reliability (High/Medium/Low) | Derivation Method (if Implicit) |
        | :------------- | :---: | :---: | :-----------------------: | :-----------------: | :-----------------------------: | :-------------------------------: |
        | ε (Reciprocal Interaction Strength) | Variable | kT | Fig. 2, 3, 4 | Explicit | High | N/A |
        | μ (Chemical Potential) | Variable | kT | Fig. 2, 3, 4 | Explicit | High | N/A |
        | λ (Non-reciprocal Interaction Strength) | Variable | kT | Fig. 2, 3, 4 | Explicit | High | N/A |
        | M (Number of Tiles/Structure) | 1600 | tiles | Fig. 2, 3, 4 | Explicit | High | N/A |
        | Pattern Size | 40x40 | lattice units | Fig. 2, 3, 4 | Explicit | High | N/A |

    *   **Note:** N/A

## M2: Energy Flow
*   **Vector ID:** M2
*   **Vector Type:** Energy

### **2.1 Energy Input**

*   **Vector ID:** M2.1
*   **Vector Type:** Input
    *   Content: The model operates under non-equilibrium conditions, implicitly requiring continuous energy input to sustain the shape-shifting dynamics. While not explicitly stated as an external energy source, the stochastic nature of the Monte Carlo simulation and the implementation of non-reciprocal interactions serve as a continuous driver of the system away from equilibrium. In a physical realization, this energy input would likely need to be supplied externally, e.g., through chemical potential gradients, light, or mechanical agitation.
    *   Value: N/A (Conceptual, not explicitly quantified)
    *   Units: N/A
    *   CT-GIN Mapping: `EnergyInputNode`: attributes - `source: Implicitly Stochastic Dynamics/Non-reciprocal interactions`, `type: Non-Equilibrium Drive`.
    *   Implicit/Explicit: Implicit
        *  Justification:  The paper describes non-equilibrium dynamics and energy-consuming processes in living systems as motivation. The model's shape-shifting behavior itself implies a constant energy input to overcome energy barriers and drive transitions, even though an explicit energy source is not defined in the model formulation.

### **2.2 Energy Transduction**

*   **Vector ID:** M2.2
*   **Vector Type:** Transduction
    *   Content: The primary energy transduction mechanism is the conversion of the implicit non-equilibrium drive (through non-reciprocal interactions and stochasticity) into changes in the configurational energy of the tile system. The non-reciprocal interactions (Rnr matrix) introduce directionality, which biases the system towards transitions between different self-assembled structures. The reciprocal interactions (U matrix) define the equilibrium energy landscape, while the non-reciprocal ones dynamically reshape this landscape, enabling transitions.  The system moves through configuration space driven by Metropolis Monte Carlo dynamics, accepting moves that lower or, probabilistically, increase the Hamiltonian based on the reciprocal interactions, but modified by the non-reciprocal interactions which bias transitions in a specific sequence.
    *   CT-GIN Mapping: `EnergyTransductionEdge`: attributes - `mechanism: Non-reciprocal Interaction-Biased Stochastic Dynamics`, `from_node: EnergyInputNode`, `to_node: Configurational Changes (Implicitly represented by state changes in tile lattice)`.
    *   Implicit/Explicit: Mixed
        *  Justification: The concept of energy being transduced into configurational changes is explicit in the model description, especially in the context of non-equilibrium dynamics. The specific mechanism is detailed but requires some interpretation to fully map the abstract Monte Carlo steps to physical energy transduction processes in a potential material realization.

### **2.3 Energy Efficiency**

*   **Vector ID:** M2.3
*   **Vector Type:** Score
    *   Score: [3]
    *   Justification/Metrics: Energy efficiency is not explicitly quantified or discussed in the paper. The system is presented as a conceptual model, and energy efficiency is not a primary focus. Based on the Metropolis Monte Carlo method and the need to overcome energy barriers for transitions, the process is likely to be intrinsically thermodynamically inefficient.  A qualitative assessment would be Low, as the system is driven by stochastic processes, and many attempted moves might be rejected, and energy is likely dissipated in random fluctuations and heat due to the stochastic tile rearrangements and lattice updates. There is no mention of energy recovery or optimization in the transition process.
    *   CT-GIN Mapping: Attribute of `EnergyTransductionEdge`s: `efficiency: Low (Qualitative Assessment)`.
    *   Implicit/Explicit: Implicit
      *  Justification: Efficiency is not explicitly addressed, but the nature of Monte Carlo simulation, the discussion of energy-consuming processes in living systems, and the absence of energy optimization mechanisms implicitly point to low energy efficiency.

### **2.4 Energy Dissipation**

*   **Vector ID:** M2.4
*   **Vector Type:** Dissipation
    *   Content: Energy dissipation mechanisms are not explicitly detailed or quantified in the paper. In the context of the Monte Carlo simulation, dissipation is implicitly represented by the probabilistic rejection of moves that increase the system's Hamiltonian and the overall stochastic nature of the dynamics. In a physical implementation, dissipation would likely occur through thermal fluctuations, friction between tiles as they rearrange, and potentially through irreversible aspects of the non-reciprocal interactions themselves.  Quantification is not provided and would require further analysis or simulation focusing on entropy production and heat fluxes which is briefly touched upon with entropy production calculations in Fig 2g, showing temporal dynamics of entropy production, but not quantified in absolute terms of dissipated energy. Qualitatively, dissipation is likely to be Medium to High due to the stochastic nature of the dynamics and the continuous transitions between structures.
    *   CT-GIN Mapping: Creates `EnergyDissipationNode`s and `EnergyDissipationEdge`s: `EnergyDissipationNode`: attributes - `mechanism: Stochastic relaxation, tile rearrangement, thermal fluctuations`, `EnergyDissipationEdge`: attributes - `from_node: EnergyTransductionEdge, to_node: EnergyDissipationNode`.
    *    Implicit/Explicit: Mixed
        *  Justification: The concept of energy dissipation is implicitly linked to the non-equilibrium nature of the system and the stochastic dynamics. Figure 2g shows entropy production, indicating non-equilibrium activity and thus dissipation, but a detailed breakdown or quantification of specific dissipation mechanisms is not explicitly provided.

## M3: Memory
*   **Vector ID:** M3
*   **Vector Type:** Memory

### **3.1 Memory Presence:**

*   **Vector ID:** M3.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: The system exhibits memory in the form of the programmed sequence of self-assembled structures. The non-reciprocal interactions are designed to drive transitions between these structures in a predefined order (e.g., S(1) → S(2) → S(3) → S(4)). The current structure influences the future state by biasing transitions towards the next structure in the sequence. This persistence of structural information and its influence on future states constitutes memory. The system ‘remembers’ the programmed sequence and progresses through it.
    *    Implicit/Explicit: Mixed
        * Justification: The paper explicitly states the goal of choreographing sequential formation of self-assembled structures and achieving shape-shifting. This sequential dependence inherently implies a form of memory where the current state influences the future trajectory, even though “memory” as a specific module isn't discussed using this exact terminology.

### **3.2 Memory Type:**

*   **Vector ID:** M3.2
*   **Vector Type:** Score
*   Score: [6]
*   Justification: The memory type can be characterized as a form of sequential state memory. It is encoded in the design of the non-reciprocal interaction matrix Rnr, which programs the transitions between specific structural states. Retention: The system retains the sequence information as long as the non-reciprocal interactions are active. The structures are stable for certain parameter ranges (multifarious assembly regime), indicating a level of retention for each state before transitioning. Capacity: The capacity is limited by the number of programmable transitions in the sequence, shown up to four in the examples. The capacity is discrete, represented by the number of stored structural configurations and transition rules. Read-out accuracy: The readout is through the observable structure of tiles on the lattice. Accuracy is reflected in how faithfully the system assembles and transitions through the desired sequence of structures, assessed by overlap metrics in Fig. 2g and frequency of shifts in Fig. 4.  The memory resembles associative memory in that it retrieves and transitions through a sequence of patterns when initiated with a seed. It is not re-writable in the sense of dynamically altering the sequence during runtime, as the sequence is predefined in the interaction matrices. It is more akin to a read-only sequence memory.
*   CT-GIN Mapping: Defines the `MemoryNode` type: `MemoryNode` attributes: `memoryType: Sequential State Memory`, `encodingMechanism: Non-reciprocal Interaction Matrix (Rnr)`, `readoutMechanism: Structural Configuration (Tile Lattice)`, `retention: Medium-term (while non-reciprocal interactions are active)`, `capacity: Limited by programmed sequence length (discrete states)`, `readoutAccuracy: Quantifiable by overlap metrics, shift frequency`.
*    Implicit/Explicit: Mixed
    * Justification: The memory type is inferred from the system's behavior and design. While the paper doesn't explicitly categorize it as "sequential state memory", the description of programmed transitions and the system's ability to progress through a sequence of structures directly implies this type of memory function. The retention, capacity, and readout mechanisms are deducible from the experimental setup and reported metrics, although not explicitly labeled as "memory characteristics".

### **3.3 Memory Retention Time:**

*   **Vector ID:** M3.3
*   **Vector Type:** Parameter
*   Value: Long-term (relative to simulation time, limited by simulation duration, and parameter stability regions but concept is of persistence until next programmed transition)
*    Units: Simulation steps (τ) and potentially indefinitely if parameters remain constant in ideal model conditions.
*   Justification: The retention time of each structural state is demonstrated by the period during which the system dwells in each configuration before transitioning to the next. Figure 2f and 2g show the system maintaining each structure for a considerable duration within the simulation timescale (up to ~10^7 τ or more depending on parameters). The stability analysis in terms of parameter space in Fig. 3 also indicates regions where multifarious assembly and shape-shifting are stable regimes. In principle, within the simulation, and assuming stable parameters (ε, μ, λ), the system would remain in each state indefinitely until the non-reciprocal interactions trigger the next transition in the sequence.  The retention is "long-term" in the context of the presented simulations, representing persistence until the conditions for transition are met by designed non-reciprocal interactions rather than temporal decay.
*    Implicit/Explicit: Mixed
        * Justification: The retention time is qualitatively demonstrated by the graphs showing stable phases and time evolution of overlap in Fig. 2 and Fig. 4. However, a specific quantitative value for retention *time* in real-world units or a systematic study of decay rates leading to loss of memory is not explicitly provided. "Long-term" is a relative qualitative assessment based on the simulation timescale.

### **3.4 Memory Capacity (Optional - if applicable)**

* **Vector ID:** M3.4
* **Vector Type:** Parameter
*  Value: 4 (demonstrated sequence length)
*   Units: Distinct structural states (in demonstrated example). In principle, capacity could be higher depending on design of U and Rnr matrices.
*   Justification: The paper demonstrates shape-shifting between four predefined structures (Fig. 2f,g).  The capacity is directly related to the number of distinct structures encoded in the interaction matrices and the length of the programmed transition sequence. While the example uses four structures, the methodology is presented as being scalable in principle to "many such transitions" and encoding "m desired structures", suggesting a capacity that is determined by the design and complexity of the interaction matrices and not fundamentally limited to four. The capacity is discrete, measured in terms of the number of uniquely addressable structural states within the sequence.
*    Implicit/Explicit: Explicit
        *  Justification: The number of structures (four) in the depicted example is explicitly shown.  The potential for scaling to "m desired structures" is also explicitly mentioned, making the concept of capacity related to sequence length explicit.

### **3.5 Readout Accuracy (Optional - if applicable)**

* **Vector ID:** M3.5
* **Vector Type:** Parameter
*   Value:  > 95% (overlap), Frequency of Shifts (quantified in Fig 4)
*   Units: Overlap (dimensionless, percentage of tile matching with target structure for fidelity), Frequency (fraction of successful shifts)
*   Justification: Readout accuracy is quantified using the overlap metric in Fig. 2g, showing overlap values reaching above 0.95, indicating high fidelity in retrieving the target structures.  Further accuracy is assessed by the "frequency of shifts" in Fig. 4b-j, representing the fraction of successful transitions to the next structure in the sequence. This metric indicates how reliably the system progresses through the programmed memory sequence.  Both overlap and shift frequency serve as measures of readout accuracy by quantifying how closely the realized structures and transitions match the intended, programmed sequence.
*    Implicit/Explicit: Explicit
       *  Justification: The overlap metric and frequency of shifts are explicitly defined and used in the paper to assess the system's performance in terms of structural fidelity and successful transitions, which directly relate to readout accuracy from the memory (sequence of structures).

### **3.6 Degradation Rate (Optional - if applicable)**
* **Vector ID:** M3.6
* **Vector Type:** Parameter
    *   Value: N/A (Not Quantified), potentially related to "Premature Shifting" rate in Fig 4m. Stability discussed qualitatively in relation to parameter space (Fig 3).
    *   Units: N/A
    *   Justification: Degradation rate of the memory (sequence or structural states) is not explicitly quantified as a parameter in the paper. However, related concepts are discussed: "premature shifting" (Fig. 4m) could be interpreted as a form of degradation where the system transitions too early before fully forming the current structure, and the parameter space analysis (Fig. 3) indicates regions where the "shape-shifter regime" is stable.  The stability boundaries in Fig 3 and associated Extended Data Figures suggest parameter ranges within which the programmed sequence is robust, and outside of which, performance may degrade (e.g., dispersion regime). A quantitative degradation rate is not provided, but the concept of robustness and parameter-dependent stability implicitly touches upon aspects related to memory degradation.
    *    Implicit/Explicit: Implicit
            * Justification: Degradation is not explicitly quantified, but related concepts like "premature shifting" and stability regions implicitly address the robustness and potential for "memory" degradation under parameter variations or noise, even though a specific rate is not provided.

### **3.7 Memory Operations Energy Cost (Optional - if applicable)**
* **Vector ID:** M3.7
* **Vector Type:** Table
*   Table:
    | Memory Operation ID | Energy Consumption per Bit | Power Usage during Operation| Units | Uncertainty | Data Source Reference | Implicit/Explicit | Justification |
    | :------------------ | :--------------------------: | :-----------------------------: | :---: |:-----------------:|:-----------------:|:-----------------:| :------------------ |
    | Structure Retrieval (Self-Assembly) | N/A | N/A | kT (units of ε, μ, λ) | N/A | N/A | Implicit | Not quantified in bits or absolute energy units, only relative energy scales (ε, μ, λ) are considered. |
    | State Transition (Shape-Shifting) | N/A | N/A | kT (units of ε, μ, λ) | N/A | N/A | Implicit | Not quantified in bits or absolute energy units, only relative energy scales (ε, μ, λ) and entropy production (ΔΣ) are considered. |
*   Implicit/Explicit: Implicit
    *   Justification: The energy cost of memory operations (retrieval and transition) is not explicitly quantified in terms of energy per bit or power usage. The paper primarily focuses on the qualitative demonstration of shape-shifting and parameter space analysis. Energy scales are introduced through the interaction parameters ε, μ, and λ (in units of kT), providing a relative energy context, but not a bit-level quantification of energy consumption for memory operations. The entropy production ΔΣ in Fig. 2g gives a measure of non-equilibrium activity related to transitions but is not directly translated into energy cost per memory operation in standard information theory terms.

### **3.8 Memory Fidelity & Robustness Metrics (Optional - if applicable)**
* **Vector ID:** M3.8
* **Vector Type:** Table
*   Table:
    | Metric ID | Description | Value | Units | CT-GIN Mapping | Data Source | Implicit/Explicit | Justification |
    | :-------- | :---------- | :----: | :---: | :-------------: | :----------: |:-----------------:| :-----------------:|
    | Overlap (O) | Measure of structural similarity to target pattern | > 0.95 (peaks) | Dimensionless | Attribute of `MemoryNode` readout | Fig. 2g | Explicit | Quantifies fidelity of retrieved structure. |
    | Shift Frequency (f) | Fraction of successful transitions to next structure in sequence | Variable (parameter-dependent, Fig 4) | Fraction (dimensionless) | Attribute of `MemoryNode` transition reliability | Fig. 4 | Explicit | Quantifies robustness of sequential memory transitions. |
    | Premature Shift Rate | Fraction of shifts occurring before full self-assembly of current structure | Variable (parameter-dependent, Fig 4m, qualitative Low fraction reported) | Fraction (dimensionless) | Negative robustness characteristic of `MemoryNode` | Fig. 4m | Explicit | Quantifies a type of memory failure mode related to robustness. |
*   Implicit/Explicit: Explicit
*   Justification: Memory fidelity and robustness metrics are explicitly defined and utilized in the paper (overlap, shift frequency, premature shift rate) to evaluate the performance of the shape-shifting system as a memory system capable of storing and sequentially recalling structural states. These metrics are directly derived from the simulation outputs and used for parameter space exploration (Fig 3 and 4).

---

## M4: Self-Organization and Emergent Order
*   **Vector ID:** M4
*   **Vector Type:** Self-Organization

### **4.1 Self-Organization Presence:**

*   **Vector ID:** M4.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: The system demonstrates self-organization as the predefined structures (patterns) spontaneously emerge from local interactions between tiles. Starting from an initial seed, the tiles interact based on the reciprocal interaction matrix U, leading to the assembly of a globally ordered structure. The global structure (the specific pattern) is not programmed directly but emerges from the local interaction rules encoded in U and the stochastic dynamics of tile attachment and detachment on the lattice. The desired structures are encoded in the interaction potentials, guiding self-assembly via local interactions. The non-reciprocal interactions then orchestrate transitions *between* these self-organized states, further highlighting the dynamic self-organization aspect.
    *   Implicit/Explicit: Explicit
        *  Justification: The paper explicitly uses terms like "self-assembly" and "self-organization" to describe the process of pattern formation from local tile interactions. The figures illustrate the emergence of global structures from initially disordered states (or seeds), emphasizing the spontaneous character of order arising from local rules.

### **4.2 Local Interaction Rules:**

*   **Vector ID:** M4.2
*   **Vector Type:** Rules
    *   Content: The local interaction rules are defined by the reciprocal interaction matrix Ur and the non-reciprocal interaction matrix Rnr.
        *   **Reciprocal Interactions (Ur):**  Defined by equation (1) and visualized in Figure 1b. If a pair of tiles A and B in a horizontal or vertical orientation (A/B or A\B) is part of the "desired structures" set ℐr, then there is a reciprocal interaction energy of -ε (favorable, attractive). Otherwise, the interaction energy is 0. This rule is directionless (A with B is the same as B with A) and depends only on the tile types and their relative orientation (H or V).
        *   **Non-reciprocal Interactions (Rnr):** Defined by equation (4) and visualized in Figure 1c and 1d. These interactions are directional and asymmetric (A approaching B is different from B approaching A). If a specific directional approach (e.g., B approaching A from the left - B↗A) is part of the non-reciprocal interaction set ℐnr, then there's an interaction strength λ which modifies the transition probability in the Monte Carlo simulation according to equation (6) and (7). The exact form of ℐnr is defined in equation (5). For a transition S(ℓ) → S(ℓ+1),  ℐnr(S(ℓ)→S(ℓ+1)) comprises interactions like S(ℓ) ↙S(ℓ+1), S(ℓ+1)↗S(ℓ), S(ℓ+1)↘S(ℓ), and S(ℓ) ↖S(ℓ+1) for neighboring tiles i,j and i-1,j, i+1,j, i,j-1 and i,j+1. These non-reciprocal interactions are crucial for driving the system out of equilibrium and causing transitions between the equilibrium self-assembled structures.
        *   **Monte Carlo Dynamics:**  The interaction rules are embedded within a generalized Monte Carlo simulation. The probability of changing a tile at position (i,j) from σ<sub>i,j</sub> to σ’ is given by  p = min{1, exp(Λ<sub>i,j</sub> −Δ<0xE2><0x84><0x8B>)}. Δ<0xE2><0x84><0x8B> is the change in Hamiltonian (Eq. 3) based on reciprocal interactions (Ur), and Λ<sub>i,j</sub>  (Eq. 7) incorporates the non-reciprocal interactions (Rnr) that bias the transitions.

    *   CT-GIN Mapping: Part of the `AdjunctionEdge` description (local side). These define the "LocalInteraction" category of edges:  `AdjunctionEdge`: attributes - `interactionType: Reciprocal (Ur) / Non-reciprocal (Rnr)`, `ruleType: Pairwise Interaction Potential`, `potentialFunction: Ur (Eq. 1), Rnr (Eq. 4)`, `directionality: Reciprocal (symmetric), Non-reciprocal (asymmetric)`, `parameters: ε (for Ur), λ (for Rnr)`.
    * **Implicit/Explicit**: Explicit
        *  Justification: The local interaction rules are explicitly defined by equations (1), (4), (5), (6), and (7), and visualized in Figure 1b, 1c, and 1d. The descriptions of reciprocal and non-reciprocal interaction matrices and their roles are clearly stated in the main text and methods.

### **4.2.1 Local Interaction Parameters:**

* **Vector ID:** M4.2.1
* **Vector Type:** Table
*   Table:
    | Rule ID | Description | Parameter Name | Parameter Value Range | Units | Data Source | Implicit/Explicit | Justification |
    | :------ | :---------- | :------------- | :---------- | :---: | :----------: | :----------------: | :------------: |
    | Reciprocal Interaction Rule (Equation 1) | Strength of attraction between interacting tiles | ε | Variable, explored in figures | kT | Methods, Figures 2, 3, 4 | Explicit |  ε is explicitly defined as the interaction strength in Eq 1 and varied across figures. |
    | Non-reciprocal Interaction Rule (Equation 4) | Strength of directional transition bias | λ | Variable, explored in figures | kT | Methods, Figures 2, 3, 4 | Explicit | λ is explicitly defined as the non-reciprocal interaction strength in Eq 4 and varied across figures. |
    | Chemical Potential Rule (Equation 3) | Controls tile density | μ | Variable, explored in figures | kT | Methods, Figures 2, 3, 4 | Explicit | μ is explicitly defined as chemical potential in Eq 3 and varied across figures. |

### **4.3 Global Order:**

*   **Vector ID:** M4.3
*   **Vector Type:** Order
    *   Content: The global order that emerges is a set of predefined 2D square lattice patterns of tiles (A and B). In the examples, up to four distinct patterns (S(1), S(2), S(3), S(4)) are designed, each being a random permutation of 1600 tiles arranged on a 40x40 grid. These patterns represent the "desired structures" that the system self-assembles into and transitions between. The order is characterized by the specific arrangement of A and B tiles in the 2D lattice, forming a global pattern that is spatially extended and distinguishable from a disordered or random configuration.  The system cycles through a sequence of these ordered states due to the non-reciprocal interactions. Examples of these structures are schematically depicted in Figure 1a, 1e and shown for different phases in Figure 2a-e.
    *   CT-GIN Mapping: Defines a `ConfigurationalNode`: `ConfigurationalNode` attributes: `orderType: 2D Lattice Pattern`, `patternGeometry: Square Grid (40x40 in example)`, `componentTypes: Tiles A and B`, `patternSpecificity: Predefined, random permutation based`, `orderMetric: Overlap with target pattern`.
    * **Implicit/Explicit**: Explicit
        *  Justification: The paper explicitly describes the "desired structures" as predefined patterns on a 2D lattice. Figure 1 and 2 visually represent these ordered structures, and the text details their construction as random permutations of tiles, clearly defining the nature of the global order that emerges through self-assembly.

### **4.4 Predictability of Global Order:**

*   **Vector ID:** M4.4
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The predictability of the global order is high, but not perfect. For appropriate parameter ranges (multifarious assembly and shape-shifter regions in Fig. 3), the system reliably self-assembles into the designed patterns starting from a seed, and sequentially transitions through the programmed sequence. Quantitatively, the overlap metric (Fig. 2g) shows high overlap (> 0.95) with target patterns, indicating a strong tendency to form the intended order.  However, predictability is not absolute. As shown in Figures 2 and 3, deviations occur: "chimera" formation (Fig. 2b) represents a less predictable outcome where unintended structures emerge, and the "dispersion" regime (Fig 2d) indicates a failure to form any ordered structure. Figure 4 shows a "frequency of shifts," which is less than 1 for all λ, indicating that not all realizations perfectly follow the intended sequence, implying some stochasticity and deviations from perfect predictability.  Furthermore, "premature shifts" (Fig 4m) represent another form of deviation from perfectly predictable sequential order.  Overall, within the designed parameter windows, the system exhibits high, but not flawless, predictability of global order.
    * **Implicit/Explicit**: Mixed
    *  Justification: The high overlap scores and the demonstration of shape-shifting behavior (Fig. 2, 4) explicitly show a high degree of predictability in pattern formation and sequential transitions. However, the existence of error regimes (chimera, dispersion), the shift frequency being less than 100%, and the phenomenon of premature shifting, all explicitly shown and discussed, demonstrate that the predictability is not absolute and has limitations due to stochasticity and parameter sensitivity. Score of 8 balances high success but acknowledges imperfections.
    *   CT-GIN Mapping: Contributes to the `AdjunctionEdge` weight: `AdjunctionEdge` attributes: `predictabilityScore: 8`, `predictabilityMetrics: Overlap (O), Shift Frequency (f), Premature Shift Rate`.

### **4.5. Local Interaction Rules (for Self-Organization)**
* **Vector ID:** M4.5
* **Vector Type:** Table
*   Table:
| Rule ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Source |
| :------ | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :-----: |
| Reciprocal Attraction | Tiles in desired structures attract | ε | Variable | kT | Explicit | Equation (1), Fig 1b | Methods |
| Non-reciprocal Bias | Directional bias for transitions | λ | Variable | kT | Explicit | Equation (4), Fig 1c, 1d | Methods |
| Monte Carlo Acceptance | Probabilistic updates based on interactions | Temperature (implicitly in kT) | Fixed (implicitly) | kT | Implicit | Equations (6), (7) | Methods |

### **4.6. Globally Emergent Order and Order Parameters**
* **Vector ID:** M4.6
* **Vector Type:** Table
*   Table:
| Property ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Protocol | Source |
| :---------- | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :------: | :-----: |
| Structural Pattern | 2D Tile arrangement  | Visual inspection, Overlap (O) | Variable (patterns S1-S4) | Dimensionless | Explicit | Fig. 2a, 2e, 2f, 2g | Monte Carlo Simulation | Results |
| Sequence of Patterns | Order of structures over time | Sequence Index (S1->S2->S3->S4) | Predefined | Index (dimensionless) | Explicit | Fig. 2f, 2g | Programmed non-reciprocal interactions | Results|
| Error Rate | Deviations from desired patterns (chimera, dispersion, premature shifts) | Error (1-O), Shift Frequency (f), Premature Shift Rate | Variable (parameter dependent) | Dimensionless | Explicit | Fig. 2b, 2c, 2d, Fig. 3, 4 | Monte Carlo Simulation | Results |

### **4.7 Yoneda Embedding and Local-to-Global Mapping Fidelity**

*   **Vector ID:** M4.7
*   **Vector Type:** Table
*   Table:
    | Link Type | Description | Predictability | Yoneda Score | Metrics | Implicit/Explicit | Justification | Source |
    | :-------- | :---------- | :------------- | :----------- | :------ | :----------------: | :------------: | :-----: |
     | Local Interactions -> Global Structure | Local rules (Ur, Rnr) define emergent pattern sequence | High (Score 8, see M4.4) | 7 | Overlap (O), Shift Frequency (f) | Mixed | High predictability within parameter regimes but with non-deterministic elements and errors. Yoneda score reflects fidelity of mapping but acknowledges imperfections. | Fig. 2, 4 |
    *   **Yoneda Embedding Fulfillment Score [0-10]:** [7]
    *   **Metrics:**  Overlap (O), Shift Frequency (f), Qualitative assessment of error regimes (chimera, dispersion, premature shifts).
    *   **Justification:** The Yoneda embedding score of 7 reflects a good but not perfect fulfillment. The local interaction rules effectively guide the system toward the desired global structures and their sequential transitions. The high predictability score (M4.4) and overlap metrics support a substantial degree of fidelity in the local-to-global mapping. However, imperfections exist. The emergence of error regimes (chimera, dispersion), and the non-unity shift frequency, and premature shift rate, demonstrate that the mapping is not deterministic and contains stochastic elements and potential deviations from the ideal programmed sequence. A score of 7 acknowledges that the local rules are strongly indicative of the global order but are not foolproof and do not guarantee perfect, error-free self-organization and shape-shifting in every realization, reflecting the probabilistic nature of the Monte Carlo dynamics and the complexity of non-equilibrium self-assembly.

## M5: Computation
*   **Vector ID:** M5
*   **Vector Type:** Computation

### **5.1 Embodied Computation Presence:**

*   **Vector ID:** M5.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: The system exhibits embodied computation because the transitions between self-assembled structures are not externally programmed step-by-step but are intrinsic to the interaction rules and the dynamics of the tile system itself. The non-reciprocal interactions, encoded in the Rnr matrix, physically embody the "program" for sequential transitions. The system "computes" the next structural state based on the current state and these embodied interaction rules, through the stochastic dynamics of tile rearrangements governed by the Metropolis Monte Carlo algorithm. The computation is distributed across the tile lattice, as each tile's behavior is governed by local interactions, and the global shape-shifting emerges from the collective dynamics without a central controller explicitly dictating each transition step.
    *    Implicit/Explicit: Mixed
        *  Justification: The paper describes the "design rule" as being composed of reciprocal and non-reciprocal interactions that enable the shape-shifting. The dynamics are governed by local interactions and Monte Carlo steps. While "embodied computation" is not explicitly stated as a framework, the description of the system's autonomous transitions based on internal interactions and dynamics implicitly demonstrates the presence of embodied computation.

### **5.2 Computation Type:**

*   **Vector ID:** M5.2
*   **Vector Type:** Classification
    *   Content: [Analog]
    *   CT-GIN Mapping: Defines the `ComputationNode` type: `ComputationNode` attributes: `computationType: Analog`.
    *    Implicit/Explicit: Implicit
    *    Justification: The computation is analog because it relies on continuous physical interactions and probabilistic dynamics, rather than discrete digital operations.  The interaction energies (ε, μ, λ) are continuous parameters. The Monte Carlo algorithm operates probabilistically, with acceptance probabilities that are continuous functions of energy differences, not sharp digital switching. The shape-shifting process is a continuous evolution in configuration space, not a sequence of discrete digital states. While the *patterns* are discrete, the *underlying computational mechanism* controlling transitions is analog, based on continuous interaction potentials and stochastic dynamics.

### **5.3 Computational Primitive:**

*   **Vector ID:** M5.3
*   **Vector Type:** Function
    *   Content: The most basic computational primitive can be described as a **biased stochastic state transition**.
    *   **Description:** At each step in the Monte Carlo simulation, the system explores possible transitions from the current configuration to a new configuration by attempting to change the type of a tile at a randomly chosen lattice site.  The decision to accept or reject this transition is probabilistically biased by the interaction potentials.
        *  **Reciprocal Interactions (Ur):**  Favor transitions that reduce the system's Hamiltonian (move towards equilibrium self-assembly of the current structure).
        *  **Non-reciprocal Interactions (Rnr):** Introduce a directional bias, favoring transitions from the current structure S(ℓ) to the next structure S(ℓ+1) in the programmed sequence.  This bias is encoded in the Λ<sub>i,j</sub> term in the acceptance probability (Eq. 7), which is a sum of non-reciprocal interaction strengths, and is specific to the desired sequential transitions.
        *  **Stochasticity:** The acceptance rule (min{1, exp(Λ<sub>i,j</sub> −Δ<0xE2><0x84><0x8B>)}) incorporates thermal fluctuations and probabilistic acceptance of moves that might transiently increase energy, allowing the system to escape local energy minima and explore configuration space for transitions.
    *   **Mathematical Description:** The computational primitive is fundamentally embodied in the Metropolis Monte Carlo acceptance probability, p = min{1, exp(Λ<sub>i,j</sub> −Δ<0xE2><0x84><0x8B>)}, where Λ<sub>i,j</sub> encodes the non-reciprocal transition bias, and Δ<0xE2><0x84><0x8B> encodes the reciprocal energy change. This probability function, acting locally at each lattice site within the Monte Carlo iteration, represents the primitive computational step that collectively drives the shape-shifting behavior.
    *   **Sub-Type (if applicable):** State Transition: Biased Stochastic.

    *   CT-GIN Mapping: Defines the primary function of the `ComputationNode`: `ComputationNode` attributes: `computationalPrimitive: Biased Stochastic State Transition`, `primitiveFunction: Metropolis Monte Carlo Acceptance Probability p = min{1, exp(Λ<sub>i,j</sub> −Δ<0xE2><0x84><0x8B>)}`, `biasMechanism: Non-reciprocal Interactions (Rnr)`, `stochasticityType: Thermal Fluctuations (Monte Carlo)`.
    *   Implicit/Explicit: Mixed
    * Justification:  While not explicitly stated as "biased stochastic state transition" primitive, the description of the Monte Carlo algorithm, the roles of reciprocal and non-reciprocal interactions, and the probabilistic nature of transitions strongly imply that this is the fundamental computational operation performed locally within the system, leading to global shape-shifting.  The mathematical formulation of the acceptance probability (Eq. 6 and 7) embodies this primitive.

### **5.4 Embodied Computational Units**
* **Vector ID:** M5.4
* **Vector Type:** Table
*   Table:
| Unit ID | Description | Processing Power | Energy/Operation | Freq/Resp. Time | Bit-Depth | Data Source | Implicit/Explicit | Justification |
| :------ | :---------- | :--------------- | :--------------- | :--------------: | :-------: | :----------: |:-----------------:| :-----------------:|
| Lattice Site (Tile Position) | Location where tile type can be changed | Variable (context-dependent, local interactions determine transition probability) | N/A (energy per site change not explicitly quantified) | Lattice Sweep Time (τ) | N/A (analog, not bit-based) | Methods Section, Fig 1, 2 | Implicit | Lattice site considered as a basic computational unit where state-change decisions are made based on local interactions. Processing power and energy per operation are not quantified in standard computational terms.  Frequency is related to lattice sweep time. Bit-depth is not applicable as computation is analog |

## M6: Temporal Dynamics
*   **Vector ID:** M6
*   **Vector Type:** Temporal

### **6.1 Timescales:**

*   **Vector ID:** M6.1
*   **Vector Type:** ParameterTable
    *   Table:
        | Timescale Description | Value | Units | Source | Implicit/Explicit | Justification |
        | :-------------------- | :---: | :---: | :----: | :----------------: | :------------: |
        | Lattice Sweep Time (τ) | Defined as unit time step | Simulation steps | Methods Sec. | Explicit | Basic unit in Monte Carlo simulation. |
        | Retrieval Time (τ<sub>retrieval</sub>) | Variable, scaling with pattern size (Fig. 4l) | 10<sup>5</sup> - 10<sup>7</sup> τ (approx., depends on M) | Fig. 4l, 4k | Explicit | Time for seed growth to 95% overlap, depends on pattern size M. |
        | Shift Time (τ<sub>shift</sub>) | Variable, scaling with pattern size (Fig. 4l) | 10<sup>5</sup> - 10<sup>7</sup> τ (approx., depends on M) | Fig. 4l, 4k | Explicit | Time for overlap to shift from 95% of structure i to 95% of structure i+1, depends on pattern size M. |
        | Simulation Time Limit | 4 x 10<sup>6</sup> τ | Simulation steps | Fig. 4b-j, 3 | Explicit | Time limit for shift frequency characterization and phase diagram exploration. |

### **6.2 Active Inference:**

*   **Vector ID:** M6.2
*   **Vector Type:** Assessment
    *   Content: [No]
    *   Justification: The system does not exhibit active inference as described by minimizing surprise or prediction error based on an internal model of its environment.
        *   **Prediction of future states:** The system is programmed to transition to the next structure in a predefined sequence, but this is not based on predicting external environmental changes or minimizing surprise. The "prediction" is internal, driven by the non-reciprocal interactions to progress to the next structural state in the programmed sequence, irrespective of any external environment.
        *   **Action Selection to minimize discrepancies:** The tile rearrangements (actions) are directed towards forming the next structure in the sequence, but not explicitly to minimize discrepancies between an internal "model" and sensory input from an environment. The system operates in isolation; there is no environment being modeled, and no external feedback loop guiding action selection based on surprise minimization.
        *   **Internal models updated by experience:** The interaction matrices (U and Rnr) are fixed and pre-programmed. There is no mechanism for the system to update these "internal models" based on its "experience" or dynamics. The system follows a predefined sequence of transitions regardless of any outcomes or environmental influences.

    *   Implicit/Explicit: Explicit
        *  Justification:  While the system displays sequential behavior, it lacks the key characteristics of active inference: environmental modeling, surprise minimization, and model updating based on experience.  The system's transitions are purely driven by pre-programmed internal rules (non-reciprocal interactions) and not by interaction with or modeling of an external environment to minimize prediction errors, as per the definition of Active Inference explored in the background text.
    *   **If Yes/Partial, provide examples of testable CT-GIN metrics that *could* be used to quantify active inference:** N/A

## M7: Adaptation
*   **Vector ID:** M7
*   **Vector Type:** Adaptation

### **7.1 Adaptive Plasticity Presence:**

*   **Vector ID:** M7.1
*   **Vector Type:** Binary
    *   Content: [No]
    *   Justification: The system does not exhibit adaptive plasticity.
        *   **No changes in behavior or internal structure in response to experience:** The system's behavior (sequential shape-shifting) and internal structure (interaction matrices U and Rnr) are fixed and pre-programmed. It performs the same sequence of transitions every time, regardless of past "experience". There's no learning or modification of its behavior or internal parameters based on interactions with an environment or feedback from its own performance over time.
        *   **No improved performance or altered functionality *over time* due to experience:** The system's performance metrics (overlap, shift frequency) are characterized for different parameter settings but do not show adaptation or improvement *within* a single simulation run or over repeated runs based on experience.  The system does not "learn" to shift more efficiently or to correct errors based on past transitions. The behavior is pre-determined and static for a given set of parameters.

    *    Implicit/Explicit: Explicit
        * Justification: The paper describes a pre-programmed shape-shifting system.  Adaptation, learning, or plasticity are not mentioned as features of the model. The system follows a fixed sequence of transitions defined by the static interaction matrices and does not modify its behavior or internal rules in response to any feedback or experience, unlike truly adaptive or learning systems.

### **7.2 Adaptation Mechanism:**

*   **Vector ID:** M7.2
*   **Vector Type:** Description
    *   Content: N/A
    *   CT-GIN Mapping: N/A
    *    Implicit/Explicit: N/A
        *  Justification: N/A

## M8: Emergent Behaviors
*   **Vector ID:** M8
*   **Vector Type:** Behavior

### **8.1 Behavior Description:**

*   **Vector ID:** M8.1
*   **Vector Type:** Description
    *   Content: The main functional behavior of the system is **sequential shape-shifting**. This refers to the system's ability to autonomously transition through a predefined sequence of self-assembled structural patterns (S(1) → S(2) → S(3) → S(4)). Starting with an initial seed of the first structure, the system self-assembles and stabilizes in that structure (multifarious assembly), then autonomously transitions to the next structure in the sequence, and so on. This behavior emerges from the programmed non-reciprocal interactions and the stochastic dynamics of the tile system. The observable behavior is the temporal evolution of the structural configuration of tiles on the lattice, changing from one stable pattern to another in a defined order.
    *   CT-GIN Mapping: Defines the `BehaviorArchetypeNode`:  `BehaviorArchetypeNode` attributes: `behaviorType: Sequential Shape-Shifting`, `description: Autonomous transitions between predefined self-assembled structures in a programmed sequence`, `observableOutcome: Temporal evolution of tile lattice configuration, sequence of structural patterns S(1)->S(2)->S(3)->S(4)`.
    *    Implicit/Explicit: Explicit
       *  Justification: "Shape-shifting" and "sequential transitions" are explicitly used throughout the paper to describe the primary behavior.  Figures 1, 2, and 4 visually and graphically demonstrate this shape-shifting behavior through snapshots of configurations and overlap metrics over time.

### **8.2 Behavior Robustness:**

*   **Vector ID:** M8.2
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The behavior exhibits moderate robustness.
        *   **Parameter Variations:** The parameter space analysis (Fig. 3) shows that the shape-shifter regime exists within a defined window of parameters (ε, μ, λ).  Outside this range, the system transitions to other regimes (dispersion, chimera, liquid), indicating sensitivity to parameter variations. However, within the shape-shifter regime, the sequential transitions are shown to be relatively reliable.
        *   **Noise:** The Monte Carlo simulation inherently incorporates stochastic noise (thermal fluctuations). The system functions despite this noise, demonstrating robustness to a certain level of inherent stochasticity in its dynamics.
        *   **Imperfections & Component Failures:** As a theoretical model, component failures or imperfections are not explicitly tested. However, the reliance on statistical mechanics and emergent behavior from a large ensemble of tiles suggests a degree of inherent fault tolerance and resilience to minor local imperfections. The use of random permutations to define patterns also indicates a degree of robustness to specific tile arrangements; the patterns are defined statistically, not by precise tile-by-tile specification.
        *   **Quantifiable Robustness:** Figure 4 shows "frequency of shifts", which, while less than 100%, indicates a reasonable level of reliability in sequence transitions under the simulated conditions for parameter ranges within the shape-shifter regime. The system is not extremely fragile (score of 0-3), as it demonstrably performs shape-shifting in simulations. It is not perfectly robust (score of 10), as its behavior is parameter-dependent and prone to error regimes. A score of 7 reflects moderate robustness within the designed operational window.
    *   Implicit/Explicit: Mixed
        *  Justification: Robustness to inherent stochasticity is implicit due to the use of Monte Carlo simulation. Parameter sensitivity is explicitly explored in Fig. 3 and 4 and their analysis of different regimes.  Robustness to component failures and imperfections is inferred from general principles of statistical mechanics and emergent phenomena, although not directly tested or quantified in the paper.  The shift frequency metric (Fig. 4) provides a quantitative measure of reliability but shows it is not perfect.

### **8.3 CT-GIN Emergent Behavior Validation**

*    **Vector ID:** M8.3
*    **Vector Type:** Validation
     *  Content: The claims of emergent shape-shifting behavior are primarily validated through **computational simulations** using Monte Carlo methods.
        *   **Operational Definitions:**  Emergent behaviors are operationally defined through metrics like "overlap" (O) with target patterns (Methods Section, Error Calculation) to quantify self-assembly fidelity, and "shift frequency" (Fig. 4) to measure the reliability of sequential transitions.  Regimes like "chimera," "liquid," and "dispersion" are also operationally defined by visual inspection of configurations and quantitative metrics like error, density, and energy (Extended Data Figs. 1-4, Fig. 3a).
        *   **Control Experiments:** "Control" in this context is represented by varying parameters (ε, μ, λ) and observing different emergent regimes (phase diagrams in Fig. 3, Extended Data Figs 1-4). The equilibrium case (λ=0, Fig 3a, Extended Data Fig. 1) serves as a baseline to demonstrate the effect of non-reciprocal interactions (λ>0) in inducing shape-shifting.
        *   **Quantitative Analysis:**  Quantitative analysis is extensively used through overlap metrics (Fig. 2g, 4k), shift frequency histograms (Fig. 4b-j), timescale scaling (Fig. 4l), and phase diagrams (Fig. 3, Extended Data Figs 1-4) mapping different regimes as a function of (ε, μ, λ). Entropy production (ΔΣ, Fig. 2g) is used as a non-equilibrium measure.
        *   **Robustness/Reliability/Reproducibility:** Robustness is explored parametrically (Fig. 3, 4) and through frequency of shifts (Fig. 4). Reproducibility is implied by averaging results over multiple independent realizations (5-10 in Fig. 3). The shift yield analysis (Fig. 4m) further assesses reliability by quantifying correct, premature, and waiting shifts.
        *   **Limitations of Validation:** Validation is limited to computational simulations of a simplified lattice model.  Experimental validation in a physical material system is not provided in this paper. The model is theoretical and idealized, and mapping to real material systems (nucleic acids, peptides, colloids mentioned in the introduction) would require further theoretical and experimental work.  The simulations are performed for finite timescales (e.g., 4 x 10<sup>6</sup> τ), and long-term stability or behavior over much longer timescales are not exhaustively validated.

    *   Implicit/Explicit: Mixed
    *   Justification:  Validation methods are largely explicit in describing the simulation protocols, metrics, and parameter variations used. The operational definitions of behaviors and metrics are clear. However, the *interpretation* of these computational results as validation for "emergent shape-shifting" and their relevance to material intelligence requires some implicit acceptance of the model's validity and its potential mapping to physical systems. The limitations of computational validation and lack of experimental confirmation are also implicitly acknowledged by the theoretical nature of the paper.

## M9: Cognitive Proximity
*   **Vector ID:** M9
*   **Vector Type:** Cognition

### **9.1 Cognitive Mapping:**

*   **Vector ID:** M9.1
*   **Vector Type:** Description
    *   Content: The paper draws an analogy between the shape-shifting self-organization model and the "hallmark of living systems" – their ability to self-organize into diverse structures and choreograph sequential formations, exemplified by the "cell cycle". The design rule is compared to the "Hopfield neural network model" in the context of multifarious assembly and memory retrieval. The concept of "versatility of building blocks" in living systems is used as a motivation for multifarious assembly. The idea of "programmable non-reciprocal interactions" is presented as a "paradigm" for automated dynamical control of self-assembled structures and transitions, drawing inspiration from biological self-organization. The system is presented as a step towards "shape-shifting soft-matter structures" and "shape-shifter regime," implicitly borrowing language from adaptive or intelligent systems.
        *   **Limitations:** The cognitive mapping is metaphorical and primarily serves as inspiration. The system does not perform complex cognitive functions like problem-solving, learning from arbitrary environments, or goal-directed behavior beyond following a pre-programmed sequence. The analogy to neural networks is limited to the associative memory aspect of pattern retrieval, not the richer computational capabilities of neural systems. The comparison to living systems is at the level of basic self-organization and sequential dynamics, not higher-level cognition or consciousness.
    *   CT-GIN Mapping: Defines a `CognitiveMappingEdge`: `CognitiveMappingEdge` attributes: `sourceNode: BehaviorArchetypeNode (Sequential Shape-Shifting)`, `targetNode: CognitiveFunctionNode (Sequential Memory/State Transition)`, `mappingType: Biological Analogy/Metaphorical`, `analogyTargets: Living Systems, Cell Cycle, Hopfield Neural Network, Associative Memory`, `limitations: Metaphorical only, no higher-level cognitive functions, simple sequential memory`.
    *   Implicit/Explicit: Explicit
    * Justification: The paper explicitly draws analogies to living systems and neural networks to motivate and contextualize the research. Terms like "programmable," "control," "shape-shifting," and "organization" carry implicit cognitive connotations.  However, the limitations of these analogies are also implicitly present as the focus remains on basic self-assembly and sequential transitions, not complex cognition.

### **9.2 Cognitive Proximity Score:**

*   **Vector ID:** M9.2
*   **Vector Type:** Score
    *   Score: [2]
    *   Justification: Cognitive Proximity Score: Level 2 - **Sub-Organismal Responsivity**.
        *   **Level 2 Justification:** The system exhibits a basic form of sequential memory and a programmed response (shape-shifting sequence). The behavior is more than simple stimulus-response (Level 1) as the transitions depend on the current structural state and not just immediate external stimuli. The sequential progression through states can be seen as a rudimentary form of "adaptation" to internal programming, albeit not to external environmental changes. However, it lacks complex representation, goal-directedness, or adaptation to unforeseen situations. The "memory" is a predefined sequence, not a dynamic, adaptable memory system. The system remains at a sub-organismal level of responsivity, exhibiting very basic sequential dynamics inspired by biological systems but far from exhibiting genuine cognition. It is above Level 1 due to the sequential nature of response but falls short of Level 3 due to the lack of true adaptive autonomy or goal-directed behavior in response to a dynamic environment.
    *   Implicit/Explicit: Mixed
    *  Justification: The cognitive proximity score is based on interpreting the system's demonstrated capabilities against the CT-GIN Cognizance Scale. The sequential memory and programmed transitions are explicit features of the system, placing it beyond Level 1 (Simple Responsivity). However, the lack of environmental interaction, model updating, and goal-directed behavior, which are *implicit* absences, firmly limit it to Level 2 (Sub-Organismal Responsivity), well below higher levels of cognition. The score reflects a mixed assessment based on what is present and conspicuously absent in terms of cognitive functions.

**CT-GIN Cognizance Scale:**

*   **Level 0: Non-Cognitive:** Purely reactive system.  No internal state beyond immediate stimulus-response.
*   **Level 1: Simple Responsivity:** Basic stimulus-response behavior.  Reactions are fixed and predetermined.
*   **Level 2: Sub-Organismal Responsivity:**  Behavior exhibits basic forms of adaptation or plasticity, but lacks complex representation or goal-directedness. **[Current Level]**
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
    | Sensing/Perception               |      0       | Absent. No sensory input or perception of environment. System operates in isolation.     | None                                | Explicit          | No sensory mechanisms described.          |
    | Memory (Short-Term/Working)        |      3       | Sequential state. Remembers current structure in sequence for a limited time until transition. | `MemoryNode`                       | Mixed             | Sequential transition implies short-term state memory, but limited complexity.  |
    | Memory (Long-Term)                 |      4       | Pre-programmed sequence of structures, encoded in interaction matrices. Static.     | `MemoryNode`                       | Explicit          | Sequence is pre-programmed and persistent. |
    | Learning/Adaptation              |      0       | Absent. No adaptive behavior. Fixed interaction rules, no learning from experience.    | None                                | Explicit          | No learning mechanisms described.         |
    | Decision-Making/Planning          |      1       | Basic sequential transition, but pre-determined, not flexible decision-making.        | None                                | Implicit          | Sequence is fixed, no dynamic choices.     |
    | Communication/Social Interaction |      0       | Absent. No interaction with other agents or communication functionalities.           | None                                | Explicit          | No communication mechanisms described.     |
    | Goal-Directed Behavior            |      2       | Sequence progression is a pre-programmed "goal," not in response to external goals.    | None                                | Implicit          | Goal is internally defined sequence progression. |
    | Model-Based Reasoning              |      0       | Absent. No internal model of environment or reasoning based on a model.              | None                                | Explicit          | No model-based reasoning mechanisms.     |
    | **Overall score**                 |      ~1.25     |                                                                                       |                                   |                     |                |

    *   **Note:** Average is calculated excluding Sensing/Perception, Communication and Model-Based Reasoning, which are strictly zero, summing scores of Memory (ST), Memory (LT), Learning, Decision Making, Goal-Directed Behavior (3+4+0+1+2)/5 = 2. Summing all, including the zeros, average is (3+4+0+1+2)/8 = 1.25

## M10: Criticality Assessment
*   **Vector ID:** M10
*   **Vector Type:** Criticality

### **10.1 Criticality:**

*   **Vector ID:** M10.1
*   **Vector Type:** Assessment
    *   Content: [Unclear]
    *   Justification: The paper does not explicitly address or assess whether the system operates near a critical point or displays scale-free behavior, power laws, or long-range correlations.
        *   **Critical Parameters:** No parameters are explicitly identified as critical in the context of criticality or phase transitions in the scale-free behavior sense. Parameters ε, μ, and λ are varied, and phase diagrams are explored (Fig. 3, Extended Data Figs), but the focus is on regimes of self-assembly and shape-shifting, not explicitly on criticality.
        *   **Evidence:** The paper presents phase diagrams showing different regimes (multifarious assembly, shape-shifter, chimera, liquid, dispersion) as a function of parameters (ε, μ, λ).  Phase transitions *between* these regimes are evident and described. However, it is unclear if these phase transitions are *critical* in the sense of exhibiting scale-free behavior, diverging correlation lengths, or power-law distributions of observables.  The paper does not provide analyses of correlation functions, susceptibility, or other indicators of criticality commonly studied in statistical physics.  The focus is on functional transitions between self-organized states, not on the detailed nature of phase boundaries in terms of criticality.
    *   Implicit/Explicit: Explicit
    *    Justification: Criticality and scale-free behavior are not mentioned or analyzed in the paper. While phase transitions between different regimes are shown, the paper lacks any explicit evidence or discussion related to criticality in the statistical physics sense. The assessment remains "Unclear" due to the absence of relevant analysis, not because of contradictory evidence.

## M11: Review Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Review")**

N/A - Paper Type is Experimental.

## M12: Theoretical Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Theoretical")**

N/A - Paper Type is Experimental (although heavily theoretical modeling).

## M13: Overall Assessment & Scoring

*   **Vector ID:** M13
*   **Vector Type:** Overall

### **13.1 CT-GIN Readiness Score:**

*   **Vector ID:** M13.1
*   **Vector Type:** Score
*   **Calculated Score:** [5.14]

**CT-GIN Readiness Summary Table:**

| CT-GIN Aspect                   | Strength (Yes/Partial/No) | Key Supporting Metrics (with units) | Limitations (Missing Metrics/Data Gaps)                                           | Improvement Areas (Future Research)                                          |
| :------------------------------ | :-----------------------: | :-----------------------------------| :------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| Energy Flow Efficiency          | No                        | N/A                                 | Quantified energy efficiency, detailed dissipation mechanisms                      | Energy optimization strategies, efficiency metrics quantification               |
| Memory Fidelity                 | Yes                       | Overlap (>0.95), Shift Frequency (Variable) | Degradation rate quantification, error correction mechanisms                    | Robustness against noise and imperfections, error correction strategies        |
| Organizational Complexity       | Yes                       | Sequence length (4), Pattern size (40x40) | Number of distinct patterns explored in sequence, complexity scaling analysis | Exploration of larger sequences, more complex patterns, hierarchical organization |
| Embodied Computation            | Yes                       | Lattice Sweep Time (τ)                 | Processing power, energy per operation, computational primitives characterization in detail | Characterization of computational power, relation to algorithmic complexity  |
| Temporal Integration            | Yes                       | τ<sub>retrieval</sub>, τ<sub>shift</sub> (units of τ) | Detailed timescale characterization, adaptation timescale                      | Explore wider range of timescales, implement adaptive temporal control          |
| Adaptive Plasticity             | No                        | N/A                                 | Mechanisms for adaptation, learning, plasticity                                  | Implement adaptive interaction rules, learning mechanisms, environmental feedback |
| Functional Universality         | No                        | N/A                                 | Demonstration of diverse behaviors beyond shape-shifting                          | Extend model to perform other functions beyond sequential transitions          |
| Cognitive Proximity            | No                        | Cognitive Proximity Score (2)        | Higher-level cognitive function implementation, Active Inference metrics           | Incorporate environmental interaction, goal-directedness, model-based reasoning |
| Design Scalability & Robustness | Partial                   | Shift Frequency (Variable)           | Scalability to larger systems, robustness to wide range of perturbations          | Systematic robustness testing, scaling analysis, fault tolerance mechanisms.  |
| **Overall CT-GIN Readiness Score** |        |   |   |      |


### **13.2 Qualitative CT-GIN Assessment Conclusion:**

*   **Vector ID:** M13.2
*   **Vector Type:** Textual Summary
    *   Content: The paper presents a conceptually strong theoretical model of non-reciprocal multifarious self-organization demonstrating sequential shape-shifting. **Key Strengths** include the clear articulation of the model, quantitative validation through simulations, and the demonstration of sequential memory encoded in non-reciprocal interactions. The system exhibits self-organization, embodied computation, and temporal dynamics, laying a foundation for exploring more complex material intelligence.  **Key Limitations** lie in the purely theoretical nature of the work, lacking experimental validation.  Energy efficiency and robustness are not rigorously quantified, and higher-level cognitive functions like adaptation or model-based reasoning are absent. The cognitive proximity remains low, at a sub-organismal level.  **Overall Assessment**: The model represents a significant step within CT-GIN's scope by providing a concrete, computationally validated example of programmable sequential behavior in a material-like system. However, it is at an early stage of CT-GIN readiness (score ~ 5), primarily demonstrating basic self-organization and sequential memory but lacking crucial aspects like energy efficiency optimization, robust adaptation, and higher-level cognitive functionalities needed for more advanced cognizant matter implementations. The potential for future development within CT-GIN is substantial if expanded to incorporate adaptive mechanisms, more complex computational primitives, and experimental realization.

### **13.3 CT-GIN Refinement Directions:**

*   **Vector ID:** M13.3
*   **Vector Type:** Recommendations
    *   * **Experimental Validation:**  Crucially, translate the theoretical model to a physical material system (colloids, DNA origami, etc.) to experimentally validate the shape-shifting behavior. Develop experimental techniques to realize non-reciprocal interactions in soft matter.
    *   **Energy Efficiency Analysis and Optimization:** Quantify energy consumption and dissipation in the model and its potential physical realizations. Explore design strategies to improve energy efficiency of shape-shifting transitions, possibly through thermodynamic optimization or energy recovery mechanisms.
    *   **Adaptive Plasticity and Learning:** Integrate mechanisms for adaptive plasticity, allowing the system to modify its transition sequences or structural patterns based on feedback or experience. Explore reinforcement learning or Hebbian learning-inspired rules for dynamically updating interaction parameters.
    *   **Enhanced Cognitive Functionalities:** Move beyond sequential memory to implement more complex cognitive functions, such as goal-directed behavior in response to simulated environments, simple forms of pattern recognition, or rudimentary decision-making based on internal "models."
    *   **Robustness and Scalability Analysis:** Conduct systematic robustness testing against noise, parameter variations, and simulated component failures. Analyze scalability to larger system sizes and more complex patterns, investigating potential limitations and strategies for improved robustness and scalability.
    *   **Criticality and Phase Transition Characterization:**  Investigate whether the transitions between shape-shifting regimes exhibit critical phenomena. Analyze correlation lengths, susceptibility, and other indicators of criticality to better understand the system's behavior near phase boundaries and potential for emergent complexity.
    *   **Hierarchical Organization:** Explore hierarchical self-organization by designing tiles with internal states or modular assemblies to increase complexity and potentially enable more sophisticated computational and adaptive behaviors.

## M14: CT-GIN Knowledge Graph

*   **Vector ID:** M14
*   **Vector Type:** Visualization

### **14.1. CT-GIN Knowledge Graph:**
* **Content:**
```
Nodes:

[SystemNode]: Shape-Shifting Self-Organization Model (Rectangle, Blue)
    Attributes: systemType="Theoretical Model", domain="Material Science, Self-Assembly", ... purpose="Programmable shape-shifting"

[EnergyInputNode]: Stochastic Dynamics/Non-reciprocal Interactions (Oval, Red)
    Attributes: source="Implicitly Stochastic Dynamics/Non-reciprocal interactions", type="Non-Equilibrium Drive"

[ConfigurationalNode]: Sequence of Lattice Patterns (Diamond, Green)
    Attributes: orderType="2D Lattice Pattern", patternGeometry="Square Grid (40x40)", ... orderMetric="Overlap"

[MemoryNode]: Sequential State Memory (Hexagon, Purple)
    Attributes: memoryType="Sequential State Memory", encodingMechanism="Rnr Matrix", ... readoutAccuracy="Overlap, Shift Frequency"

[ComputationNode]: Biased Stochastic State Transition (Parallelogram, Orange)
    Attributes: computationType="Analog", computationalPrimitive="Biased Stochastic State Transition", ...

[BehaviorArchetypeNode]: Sequential Shape-Shifting (Trapezoid, Teal)
    Attributes: behaviorType="Sequential Shape-Shifting", description="Autonomous transitions between patterns", ... reliabilityScore=7

Edges:

[EnergyTransductionEdge]: Stochastic Dynamics -> Configurational Changes (Solid Arrow, Red)
    Attributes: mechanism="Non-reciprocal Interaction-Biased Stochastic Dynamics", efficiency="Low (Qualitative)"

[AdjunctionEdge]: Local Interactions <-> Global Structure (Dashed Arrow, Green)
    Attributes: interactionType="Reciprocal/Non-reciprocal", ruleType="Pairwise Potential", predictabilityScore=7, predictabilityMetrics="Overlap, Shift Frequency"

[CognitiveMappingEdge]: Shape-Shifting Behavior -> Sequential Memory (Dotted Arrow, Purple)
    Attributes: mappingType="Biological Analogy", analogyTargets="Living Systems, Neural Network", limitations="Metaphorical, simple memory"

[TemporalEvolutionEdge]: Time -> System State (Curved Arrow, Black)
      Attributes: timescales = {τ_retrieval, τ_shift}

Relationships:

EnergyInputNode --EnergyTransductionEdge--> ConfigurationalNode
ConfigurationalNode --AdjunctionEdge--> SystemNode
MemoryNode --related_to--> ConfigurationalNode
ComputationNode --related_to--> SystemNode
BehaviorArchetypeNode --CognitiveMappingEdge--> MemoryNode
Time --TemporalEvolutionEdge--> ConfigurationalNode

Key Parameters Annotated on Nodes/Edges:
    ε (kT) on [AdjunctionEdge] (Reciprocal Interaction Parameter)
    λ (kT) on [AdjunctionEdge] (Non-reciprocal Interaction Parameter)
    μ (kT) on [SystemNode] (Chemical Potential)
    Pattern Size (40x40) on [ConfigurationalNode]
    τ on [TemporalEvolutionEdge] (Lattice Sweep Time Unit)
    Overlap (O) on [ConfigurationalNode], [MemoryNode], [BehaviorArchetypeNode] (Fidelity, Readout Accuracy)
    Shift Frequency (f) on [MemoryNode], [BehaviorArchetypeNode] (Reliability, Robustness)

```

## M15: Relationship Vectors
*   **Vector ID:** M15
*   **Vector Type:** Relationships
*   Relationships:
        | Source Vector ID | Target Vector ID | Relationship Type |
        | ------------- | ------------- | ----------------- |
        | M2.1 | M2.2 | Energy Flow |
        | M2.2 | M4.3 | Embodiment |
        | M4.2 | M4.3 | Emergence |
        | M4.3 | M3.1 | Memory Encoding |
        | M4.3 | M8.1 | Behavior Expression |
        | M5.1 | M8.1 | Computation Drives Behavior |
        | M9.1 | M8.1 | Cognitive Analogy |

## M16: CT-GIN Template Self-Improvement Insights

*   **Vector ID:** M16
*   **Vector Type:** Feedback

### **Template Feedback:**

*    **Vector ID:** M16.1
*   **Vector Type:** Text
Provide specific, actionable feedback on the *CT-GIN template itself*, based on this analysis:
    *   **Missing Probes:** The template is comprehensive. Perhaps a probe for "Scalability" within M1, addressing potential scalability of implementation to larger system sizes and more complex behaviors, could be added.  Also, perhaps a probe in M10 related to "Noise Sensitivity" to specifically inquire about robustness to stochastic noise in the system would be beneficial.
    *   **Unclear Definitions:**  The definition of "Cognitive Proximity" and especially the levels in the Cognizance Scale are still somewhat subjective and require careful judgment. More granular descriptors for each level in the scale, or providing more concrete examples for each score level, could enhance clarity and inter-rater reliability.
    *   **Unclear Node/Edge Representations:** The guidance for mapping to GIN nodes/edges is generally sufficient. However, for more complex systems, further guidance on handling hierarchical structures or nested systems within the GIN could be useful.  For example, clarifying how to represent sub-components or modules within the knowledge graph.
    *   **Scoring Difficulties:** Assigning scores, especially for "Cognitive Proximity" (M9.2) and "Cognitive Function Checklist" (M9.3), remains somewhat subjective despite the scale. Providing more operational guidelines within the justification prompts, or perhaps reference exemplars for different score levels could improve consistency.  For memory type score (M3.2) perhaps clearer examples or a more structured rubric defining the 0-10 scale ranges (e.g. 0-2 no memory, 2-4 very basic, volatile, 4-6 short term, 6-8 medium term etc).
    *   **Data Extraction/Output Mapping:** The template facilitates systematic data extraction. The table formats are effective.  For complex papers, automatically pre-filling tables with identified parameters upon section jump could be a useful feature to speed up processing, if technically feasible in a digital tool.
    *   **Overall Usability:** The template is generally well-structured and usable. The modular design with Vector IDs makes it organized. The conditional modules are helpful to streamline analysis depending on paper type.
    * **Specific Suggestions:**
        *  Add "Scalability Potential" probe to M1.
        *  Add "Noise Sensitivity" probe to M10.
        *  Refine Cognitive Proximity Scale with more granular level descriptors and examples for score level calibration.
        *  Consider developing a more detailed rubric or scoring guidelines for Memory Type (M3.2) and Cognitive Function Checklist (M9.3).
        *  For digital implementation, explore possibilities of semi-automated table pre-filling with parameter identification.