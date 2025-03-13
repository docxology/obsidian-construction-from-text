# Collision-based Computing

__Paper Type:__ Theoretical/Computational

## M1: System Overview & Implementation
*   **Vector ID:** M1
*   **Vector Type:** Overview

### **1.1 System Description**

*   **Vector ID:** M1.1
*   **Vector Type:** Description
    *   Content: Collision-based computing is described as an implementation of logical circuits and mathematical machines within homogeneous, uniform, architecture-less media. The system uses mobile localizations, such as gliders in cellular automata or solitons in optical systems, to represent quanta of information. Logical truth and false are represented by the presence or absence of these localizations, or by their internal states. Computation occurs through the collisions of these localizations, which alter their trajectories and states, representing logical operations. The medium is architecture-less, lacking hardwired components, with signal paths being momentary trajectories of propagating quanta. The described systems include 1D and 2D cellular automata, continuous excitable media, and geometrical computation with dimensionless particles.
    *   CT-GIN Mapping: `SystemNode` attributes: `systemType`: Collision-based Computing, `domain`: Computer Science, Physics, Chemistry `mechanism`: Mobile localization collision, `components`: Mobile localizations (gliders, solitons, wave-fragments, billiard balls), Stationary localizations (still lives, blocks, eaters, mirrors),  `purpose`: Implementation of logical circuits and mathematical machines.
    *   Implicit/Explicit: Explicit
        *  Justification: The system description is explicitly stated in the abstract and introduction sections of the provided text.

### **1.2 Implementation Clarity**

*   **Vector ID:** M1.2
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The paper provides a relatively clear conceptual description of collision-based computing and gives examples in various media (cellular automata, reaction-diffusion, Belousov-Zhabotinsky medium, billiard balls, abstract geometrical computation). The principles and examples of basic gates (interaction gate, switch gate, XOR gate, FANOUT gate, ERASE gate) and memory implementation are described with figures, clarifying how computation is envisioned. However, detailed implementation parameters and full algorithms for complex computations are not exhaustively provided, and the emphasis is more on the conceptual framework and possibilities rather than a fully detailed blueprint.
    *   Implicit/Explicit: Mixed
        * Justification: The conceptual framework is explicitly described, but some details of concrete, scalable implementations are implicit or left for further research and experimentation. The score reflects the clarity of the core concepts and basic examples, but acknowledges the lack of exhaustive implementation details.

### **1.3 Key Parameters**

*   **Vector ID:** M1.3
*   **Vector Type:** ParameterTable
    *   Table:
        | Parameter Name | Value | Units | Source (Fig/Table/Section) | Implicit/Explicit | Data Reliability (High/Medium/Low) | Derivation Method (if Implicit) |
        | :------------- | :---: | :---: | :-----------------------: | :-----------------: | :-----------------------------: | :-------------------------------: |
        | Cell states (Spiral Rule CA) | 3 | states | Sect. 3.1 | Explicit | High | N/A |
        | Neighborhood (Spiral Rule CA) | 7 | cells | Sect. 3.1 | Explicit | High | N/A |
        | Time step (BZ medium simulation) | 1E-3 |  - | Sect. 3.2 | Explicit | Medium | N/A |
        | Grid point spacing (BZ medium simulation) | 0.15 | - | Sect. 3.2 | Explicit | Medium | N/A |
        | States (2-state CA) | 2 | states | Sect. 4.2.2 | Explicit | High | N/A |

    *   **Note:** Listed are key parameters characterizing the system's implementation across different examples discussed in the paper.

## M2: Energy Flow
*   **Vector ID:** M2
*   **Vector Type:** Energy

### **2.1 Energy Input**

*   **Vector ID:** M2.1
*   **Vector Type:** Input
    *   Content: For Cellular Automata (Spiral Rule): The energy input is implicitly through the initial configuration of cell states. The dynamics of the cellular automaton itself, governed by the transition rules, drives the evolution and propagation of localizations. For the Belousov-Zhabotinsky (BZ) medium: The energy source is the chemical energy stored within the reactants of the BZ reaction itself. Additionally, light-sensitive BZ reaction models utilize illumination as an external excitability parameter modulation.
    *   Value: N/A (Qualitative description)
    *   Units: N/A
    *   CT-GIN Mapping: `EnergyInputNode` attributes - `source`: Initial configuration (CA), Chemical reactants & illumination (BZ), `type`: Initial potential energy, Chemical and light energy.
    *   Implicit/Explicit: Mixed
        *  Justification: While the text explicitly mentions "non-dissipative computer" designs historically, the specific energy input for the described implementations is mostly implicit, requiring inference from the descriptions of CA rules and BZ reaction dynamics. The source is conceptually stated (chemical, initial configuration), but values are not quantified.

### **2.2 Energy Transduction**

*   **Vector ID:** M2.2
*   **Vector Type:** Transduction
    *   Content: In Cellular Automata: Energy transduction is represented by the state transitions of cells based on local neighborhood configurations. The update rules effectively transduce the initial spatial distribution of states into temporal evolutions of patterns, gliders, and stationary localizations. The energy is effectively transduced from the initial configuration into the kinetic energy of glider propagation and pattern formation. In Belousov-Zhabotinsky medium: Chemical energy is transduced into propagating wave fronts (localizations) through reaction-diffusion processes. Light energy modulates the excitability of the medium, influencing wave initiation and propagation. Collisions transduce kinetic energy into changes in velocity vectors and states of localizations, realizing computational operations.
    *   CT-GIN Mapping: `EnergyTransductionEdge` attributes - `mechanism`: State transition rules (CA), Reaction-diffusion, light modulation (BZ), Collision events, `from_node`: `EnergyInputNode`, `to_node`: `ComputationNode`, `MemoryNode`, `SelfOrganizationNode`.
    *   Implicit/Explicit: Mixed
        *  Justification: The mechanisms of energy transduction (state transitions in CA, reaction-diffusion and light modulation in BZ) are implicitly explained by describing system behavior and referring to models.  The physical mechanisms are described conceptually, but efficiency metrics or detailed formulas are not provided, hence "mixed".

### **2.3 Energy Efficiency**

*   **Vector ID:** M2.3
*   **Vector Type:** Score
    *   Score: [5]
    *   Justification/Metrics: The paper mentions Fredkin and Toffoli's aim to design non-dissipative computers, suggesting an aspiration for high energy efficiency in collision-based computing conceptually. However, the provided excerpt does not include quantifiable energy efficiency metrics for the specific CA or BZ systems described. Efficiency in CA might be related to minimizing state changes per computation, while in BZ it could involve minimizing reactant consumption per operation. Qualitatively, efficiency is likely Medium, as collisions and state changes inherently involve some dissipation, although the architecture-less nature might avoid some overhead of traditional circuits. Score is estimated based on the general discussion about energy conservation in collision-based computing, but lack of specific metrics for described systems.
    *   CT-GIN Mapping: Attribute of relevant `EnergyTransductionEdge`s - `efficiency`: Qualitative assessment: Medium.
    *   Implicit/Explicit: Implicit
      *  Justification: Efficiency is discussed conceptually in relation to Fredkin-Toffoli's goal, but without quantitative metrics or detailed analysis for the examples discussed.  Score is inferred from the general context rather than explicitly stated values.

### **2.4 Energy Dissipation**

*   **Vector ID:** M2.4
*   **Vector Type:** Dissipation
    *   Content: Energy dissipation mechanisms are implicitly present in both CA and BZ systems. In cellular automata, dissipation may occur due to irreversible state transitions and the maintenance of stationary localizations (eaters). In the BZ medium, dissipation is inherent in the chemical reactions themselves, which are thermodynamically irreversible, and in diffusion processes.  The paper does not quantify energy dissipation in either system. It is implicitly suggested to be present but minimized in some designs, especially in early billiard ball models aiming for non-dissipative logic. Qualitative assessment is Medium, as energy is required to sustain the dynamics and computations, but system-level dissipation rates are not quantified.
    *   CT-GIN Mapping: Creates `EnergyDissipationNode`s and `EnergyDissipationEdge`s - `dissipationMechanism`: Irreversible state transitions (CA), Irreversible chemical reactions, diffusion (BZ), `dissipationLevel`: Qualitative Assessment: Medium.
    *    Implicit/Explicit: Implicit
        *  Justification: Dissipation mechanisms are not explicitly quantified or detailed in terms of specific energy loss rates or values. Their presence is inferred from the nature of CA dynamics and BZ reactions and the general context discussion around energy efficiency.

## M3: Memory
*   **Vector ID:** M3
*   **Vector Type:** Memory

### **3.1 Memory Presence:**

*   **Vector ID:** M3.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: Yes, memory is present in the Spiral Rule CA in the form of "eaters". The eater E6 is described as a 6-bit flip-flop memory device. It can store information by switching substrate sites to inhibitor states, which persists beyond the writing stimulus (a colliding glider). This stored state influences future behavior, as reading the memory (Fig. 5) depends on the state of the eater, and the eater retains the bit until it is erased.
    *    Implicit/Explicit: Explicit
        * Justification: The presence of memory using eater E6 is explicitly described and exemplified in Section 3.1 with figures and operational descriptions of writing and reading bits (Figs. 4 and 5).

### **3.2 Memory Type:**

*   **Vector ID:** M3.2
*   **Vector Type:** Score
*   Score: [7]
*   Justification: The memory type can be classified as a re-writable, multi-state (at least 6-bit), and relatively stable form of memory within the context of the Spiral Rule CA.  The eater offers persistent states that are maintained until actively changed by glider collisions. Retention is relatively long-term within simulation time scales. Read-out accuracy is implied to be high, as bit reading via glider collision is demonstrated through figure illustration, accurately reflecting stored information if properly designed and operated. The score is assigned considering the deterministic nature of the CA, and the demonstrated rewrite capability and stability, though detailed error rates or long-term retention beyond simulation times are not quantified, lowering the score from perfect fidelity.
*   CT-GIN Mapping: Defines the `MemoryNode` type. `memoryType`: Flip-flop (6-bit), `medium`: Spiral Rule Cellular Automata.
*    Implicit/Explicit: Mixed
    * Justification: The type as "flip-flop", re-writable is explicit from the description. The score and detailed characteristics (retention, accuracy) are inferred from the functional descriptions of write and read operations, combined with the deterministic nature of the CA.

### **3.3 Memory Retention Time:**

*   **Vector ID:** M3.3
*   **Vector Type:** Parameter
*   Value: [Quasi-stationary]
*    Units: [Time steps of CA simulation] (or Qualitative Descriptor: "Long-term" relative to computation)
*   Justification: The eater E6, once a bit is written, remains in that state in a "quasi-stationary configuration" as stated in the text. The memory is retained indefinitely within the context of the automaton evolution towards quasi-stationary states, and is stable unless actively erased by another glider collision. Thus retention is long-term relative to the timescale of glider-based computation within the described examples. Actual time values or quantitative retention decay rates are not provided.
*    Implicit/Explicit: Mixed
        * Justification: "Quasi-stationary" and stable is explicit. Quantifiable retention time and units are implicit/qualitative ("long-term" in CA context, inferred from functional descriptions and quasi-stationary nature).

### **3.4 Memory Capacity (Optional - if applicable)**

* **Vector ID:** M3.4
* **Vector Type:** Parameter
*  Value: [6]
*   Units: [bits]
*   Justification: Eater E6 is explicitly described as a "6-bit flip-flop memory device", indicating a capacity to store 6 bits of information.
*    Implicit/Explicit: Explicit
        *  Justification: Directly stated in the text description of Eater E6, Sect. 3.1.

### **3.5 Readout Accuracy (Optional - if applicable)**

* **Vector ID:** M3.5
* **Vector Type:** Parameter
*   Value: [High]
*   Units: [%, error rate implicitly low]
*   Justification: Readout accuracy is qualitatively high, as depicted in Fig. 5. The transformation of the reading glider (G34 to G4) upon interaction with a bit-up state in E6 provides a deterministic and distinct output, indicating accurate retrieval of the stored bit value within the deterministic rules of the CA.  Error rate is implicitly assumed to be low given the deterministic nature of the system and the illustrative figure example working as expected, although formal error rates are not quantified explicitly.
*    Implicit/Explicit: Mixed
       *  Justification: Qualitative assessment "High" is inferred from the deterministic nature of the CA ruleset and functionality shown in figures.  Accuracy values and quantitative metrics are not explicitly given but implied to be good as a functional memory cell is demonstrated.

### **3.6 Degradation Rate (Optional - if applicable)**
* **Vector ID:** M3.6
* **Vector Type:** Parameter
    *   Value: [Negligible over relevant timescales]
    *   Units: [% loss per simulation step]
    *   Justification: Degradation rate is expected to be negligible over relevant timescales of computation and simulation runtime, considering the description of Eater E6 and quasi-stationary states of Spiral Rule CA. The memory state is persistent unless actively erased by another controlled glider collision. No active degradation mechanism is mentioned; the system naturally evolves to stable or quasi-stable configurations. Degradation is inferred to be minimal for practical purposes in the operational context shown.
    *    Implicit/Explicit: Implicit
            * Justification:  Degradation is not explicitly quantified. The assessment is inferred from the description of quasi-stationary behavior and no mention of spontaneous bit-flipping or decay within the simulation timescales described in the paper.

### **3.7 Memory Operations Energy Cost (Optional - if applicable)**
* **Vector ID:** M3.7
* **Vector Type:** Table
*   Table:
    | Memory Operation ID | Energy Consumption per Bit | Power Usage during Operation| Units | Uncertainty | Data Source Reference | Implicit/Explicit | Justification |
    | :------------------ | :--------------------------: | :-----------------------------: | :---: |:-----------------:|:-----------------:|:-----------------:| :------------------ |
    | Write Bit         | N/A                            | N/A                                 | N/A   | N/A            | N/A               | Implicit           | Energy cost is not explicitly quantified; inferred to be related to cell state changes propagated by glider collision within the CA update cycle. |
    | Read Bit          | N/A                            | N/A                                 | N/A   | N/A             | N/A              | Implicit           | Energy cost is not explicitly quantified; inferred to be related to cell state changes propagated by glider collision within the CA update cycle. |
    | Erase Bit          | N/A                            | N/A                                 | N/A                                  | N/A             | N/A              | Implicit           | Energy cost is not explicitly quantified, inferred to be similar to write and read operations in terms of cell state changes per CA update. |
*   Implicit/Explicit: Implicit
    *   Justification: Energy consumption and power usage for memory operations are not explicitly quantified or measured in the provided text.  The values are marked N/A, as no data is present.

### **3.8 Memory Fidelity & Robustness Metrics (Optional - if applicable)**
* **Vector ID:** M3.8
* **Vector Type:** Table
*   Table:
    | Metric ID | Description | Value | Units | CT-GIN Mapping | Data Source | Implicit/Explicit | Justification |
    | :-------- | :---------- | :----: | :---: | :-------------: | :----------: |:-----------------:| :-----------------:|
    | Bit Stability | Probability of bit remaining unchanged in storage | High | Qualitative | Attribute of MemoryNode | Text description of Eater and CA stability | Implicit | Bit stability is qualitatively high due to the quasi-stationary nature of the eater in the CA and deterministic update rules. No degradation is mentioned over relevant timescales. |
    | Write Fidelity | Probability of correctly writing a bit | High | Qualitative | Attribute of MemoryOperation | Fig. 4 (Write Bit) | Implicit |  Write fidelity is implicitly high, exemplified by the successful bit writing in figure illustrations, showing intended state change upon glider collision. No error rates are provided. |
    | Read Fidelity | Probability of correctly reading a bit | High | Qualitative | Attribute of MemoryOperation | Fig. 5 (Read Bit) | Implicit | Read fidelity is implicitly high, exemplified by successful bit reading in figure illustration, showing expected glider transformation dependent on memory state. No error rates are provided. |
*   Implicit/Explicit: Implicit
*   Justification: Fidelity and robustness metrics are assessed qualitatively as "High," inferred from functional demonstrations of memory operations and the deterministic nature of the CA, but are not explicitly quantified with error percentages or similar metrics in the text.

---

## M4: Self-Organization and Emergent Order
*   **Vector ID:** M4
*   **Vector Type:** Self-Organization

### **4.1 Self-Organization Presence:**

*   **Vector ID:** M4.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: Yes, self-organization is present in the Spiral Rule CA. The paper mentions that starting from a random initial configuration, the automaton evolves towards a "quasi-stationary configuration, with typically two types of stationary localizations, and a spiral generator of mobile localizations, or gliders". This emergence of ordered structures (stationary eaters and spiral glider guns) from initially random states, driven by local cellular automaton rules, exemplifies self-organization. The global order (spiral guns, eaters) arises spontaneously from the local update rules without external design of these higher-level structures.
    *   Implicit/Explicit: Explicit
        *  Justification: Explicitly stated in Sect. 3.1 and visualized in Fig. 2 that starting from random initial conditions, ordered structures like stationary localizations and spiral glider-guns emerge. This spontaneous pattern formation is a signature of self-organization within the CA dynamics.

### **4.2 Local Interaction Rules:**

*   **Vector ID:** M4.2
*   **Vector Type:** Rules
    *   Content: The local interaction rules for the Spiral Rule Cellular Automaton are defined by a totalistic hexagonal cellular automaton where each cell updates its state (Substrate S, Activator A, Inhibitor I) based on the number of neighbors in each state. The update rule is compactly represented by a 7x7 matrix M, where M_ij determines the next state of a cell based on `i` neighbors in state I and `j` neighbors in state A. The transition matrix M is explicitly given as:
    ```
    M=
    
    S
    S
    S
    S
    
    
    S AI AI I I I
    S
    S
    SI A
    I
    I
    I
    I
    AI I I I I I
    I I I
    I I I
    
    ```
    The rules are derived from quasi-chemical reactions described as:
    A+6S→A, A+ I →I, A+ 3I →I, A+ 2I →S, 2A →I, 3A→A, βA→I, I →S. These rules effectively emulate activator-inhibitor dynamics for sub-threshold concentrations of activator.
    *   CT-GIN Mapping: Part of the `AdjunctionEdge` description (local side). Define "LocalInteraction" category of edges. `interactionType`: Cellular Automaton Rule, `ruleMatrix`: M, `neighborhoodType`: Hexagonal, `stateTypes`: {S, A, I}.
    * **Implicit/Explicit**: Explicit
        *  Justification: The local interaction rules are explicitly provided in Sect. 3.1, including both the quasi-chemical reactions and the transition matrix M defining the cellular automaton update function.

### **4.2.1 Local Interaction Parameters:**

* **Vector ID:** M4.2.1
* **Vector Type:** Table
*   Table:
    | Rule ID | Description | Parameter Name | Parameter Value Range | Units | Data Source | Implicit/Explicit | Justification |
    | :------ | :---------- | :------------- | :---------- | :---: | :----------: | :----------------: | :------------: |
    | M_01 | Diffusion of Activator A | M_01 state | A | states {S, A, I} | Sect. 3.1 | Explicit | Directly derived from the provided transition matrix M. |
    | M_11 | Suppression of Activator A by Inhibitor I | M_11 state | I | states {S, A, I} | Sect. 3.1 | Explicit | Directly derived from the provided transition matrix M. |
    | M_z2, z=0,...,5 | Self-inhibition of Activator A | M_z2 state | I | states {S, A, I} | Sect. 3.1 | Explicit | Directly derived from the provided transition matrix M. |
    | M_z0, z=1,...,7 | Dissociation of Inhibitor I in absence of Activator | M_z0 state | S | states {S, A, I} | Sect. 3.1 | Explicit | Directly derived from the provided transition matrix M. |
    | M_zp, p>=4 | Upper-threshold self-inhibition of Activator | M_zp state | I | states {S, A, I} | Sect. 3.1 | Explicit | Directly derived from the provided transition matrix M. |

### **4.3 Global Order:**

*   **Vector ID:** M4.3
*   **Vector Type:** Order
    *   Content: The global order that emerges in the Spiral Rule CA includes: 1. Stationary Localizations (Eater and Block-like structures): These are stable patterns that remain static over time and act as 'eaters' of gliders or stable blocks. 2. Spiral Glider Guns: These are self-organizing sources of mobile localizations, emitting streams of gliders periodically. 3. Mobile Localizations (Gliders G34, G4, G5, G24, G43): These are propagating wave-fragments with stable shapes and velocities, acting as information carriers in the system. The overall emergent order is a dynamic yet stable configuration composed of interacting stationary and mobile patterns, forming a complex self-organized structure. (Fig. 2 visually depicts the quasi-stable configuration with these features).
    *   CT-GIN Mapping: Defines a `ConfigurationalNode`. `configurationalType`: Quasi-stationary state, `emergentStructures`: {Stationary Localizations, Spiral Glider Guns, Mobile Localizations (Gliders)}.
    * **Implicit/Explicit**: Explicit
        *  Justification: The emergent global order, consisting of stationary localizations and spiral glider-guns, and different types of gliders, is explicitly described in Sect 3.1 and is illustrated in Figure 2 and Figure 3. These are presented as typical outputs of the self-organizing dynamics starting from random initial conditions.

### **4.4 Predictability of Global Order:**

*   **Vector ID:** M4.4
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The emergence of global order in the Spiral Rule CA is somewhat predictable in terms of the *types* of structures that will form (eaters, glider guns, gliders). The paper states, "Starting in a random initial configuration the automaton will evolve towards a quasi-stationary configuration, with typically two types of stationary localizations, and a spiral generator of mobile localizations, or gliders...".  However, the *exact spatial positions* and *number* of each structure that emerges in any given simulation from random initial conditions are not perfectly predictable. Statistical predictability is implied by the "typically" usage.  Qualitative assessment is Medium-High, as structural types are recurrent, but precise details of global patterns are not fully determined in advance –  influenced by randomness of initial configs. Score is based on the balance between predictable structural types and unpredictable precise arrangement.
    * **Implicit/Explicit**: Mixed
    *  Justification: The *types* of emergent structures (eaters, glider guns, gliders) are explicitly stated as typical. The *predictability score* and the degree of randomness in spatial arrangement are implicitly understood based on typical behavior description rather than quantified predictability metrics.

### **4.5. Local Interaction Rules (for Self-Organization)**
* **Vector ID:** M4.5
* **Vector Type:** Table
*   Table:
| Rule ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Source |
| :------ | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :-----: |
| Totalistic Rule | Cell state update depends on neighbor counts | Neighborhood Counts (σI, σA, σS) | 0-7 | count | Explicit | Rule is totalistic, matrix M indexes are neighbor counts | Sect. 3.1 |
| Matrix M Entries | Next state based on neighbor counts | Matrix Entry value (M_ij) | {S, A, I} | states | Explicit | Matrix M defines output states, matrix entries explicitly given. | Sect. 3.1 |

### **4.6. Globally Emergent Order and Order Parameters**
* **Vector ID:** M4.6
* **Vector Type:** Table
*   Table:
| Property ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Protocol | Source |
| :---------- | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :------: | :-----: |
| Glider Density | Number of gliders per unit area | Density | Varies | gliders/area | Implicit | Qualitative visual assessment of Fig. 2.  | Visual inspection of CA simulations | Fig. 2 |
| Eater Density | Number of eaters per unit area | Density | Varies | eaters/area | Implicit | Qualitative visual assessment of Fig. 2 | Visual inspection of CA simulations | Fig. 2 |
| Glider Emission Frequency | Rate of glider emission from gun | Frequency | ~1/6 | gliders/timestep per stream | Explicit (for G34 gun) |  Frequency of G34 emission is given | Fig. 2 |

### **4.7 Yoneda Embedding and Local-to-Global Mapping Fidelity**

*   **Vector ID:** M4.7
*   **Vector Type:** Table
*   Table:
    | Link Type | Description | Predictability | Yoneda Score | Metrics | Implicit/Explicit | Justification | Source |
    | :-------- | :---------- | :------------- | :----------- | :------ | :----------------: | :------------: | :-----: |
     | Local Rules -> Global Pattern | How well local Spiral Rule CA rules predict emergent patterns (eaters, glider guns) | Medium | 6 | Visual pattern analysis, qualitative recurrence of structures | Mixed | Structural types (eater, glider guns) are somewhat predictable (Medium predictability), but precise global configuration is less so. Score reflects this compromise | Fig. 2 |
    *   **Yoneda Embedding Fulfillment Score [0-10]:** [Score 6/10. Rubric for assessing score: 0 = No Emergent Order, 2 = Very weak order, Highly unpredictable, 4 = Weak order, Partially predictable in type but arrangement random, 6 = Moderate Order, Predictable types of structures but spatial positioning variable, 8 = Strong order, Predictable structure types and layout statistically predictable, 10 = Perfect order, Global order fully determined by local rules and initial conditions. For score 6, typical behaviors like eater and glider guns are reliably generated from random start, but precise location and quantity vary.]
    *   **Metrics:**  [Metrics used are primarily qualitative visual assessment of space-time diagrams (Fig. 2) and recurrence of structure "types" (eaters, glider guns, gliders)]
    *   **Justification:** Yoneda score of 6 is assigned because while the *types* of emergent structures (eaters, glider guns, gliders) are somewhat predictable and consistently arise from random initial conditions given the rules, the exact *spatial configuration* (positions, numbers) of these structures is not fully determined.  The local CA rules thus "embed" to a moderate degree into global patterns but with stochastic variation in arrangement.

## M5: Computation
*   **Vector ID:** M5
*   **Vector Type:** Computation

### **5.1 Embodied Computation Presence:**

*   **Vector ID:** M5.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: Yes, computation is embodied in the collision-based system. Logical operations (AND, OR, NOT, XOR) and memory functions are implemented directly through the dynamics of mobile localizations (gliders) and their interactions with each other and stationary localizations (eaters, mirrors) within the cellular automaton and excitable media (BZ) substrates. Computation emerges from physical collisions and state changes of these localizations, not through an external computational controller separate from the material system.
    *    Implicit/Explicit: Explicit
        *  Justification: Explicitly stated throughout the paper that collision-based computing implements logical circuits and machines directly within the physical medium itself (CA, BZ, billiard balls etc), using localization interactions (collisions) for processing.

### **5.2 Computation Type:**

*   **Vector ID:** M5.2
*   **Vector Type:** Classification
    *   Content: [Hybrid] (Collision-based computing systems described are hybrid, exhibiting characteristics of both analog and digital computation. The representation of logical values by presence/absence of localizations suggests a digital aspect. However, the continuous nature of trajectories, velocities, and states of solitons in optical systems or wave-fragments in excitable media also points towards analog characteristics. The specific examples in CA often utilize discrete states, but the broader concept of collision-based computing is presented as versatile, encompassing both discrete (CA) and continuous (BZ, solitons) implementations.)
    *   CT-GIN Mapping: Defines the `ComputationNode` type. `computationType`: Hybrid (Analog/Digital), `paradigm`: Collision-based Computing.
    *    Implicit/Explicit: Mixed
    *    Justification:  The paper describes systems using digital CA and continuous media, showcasing aspects of both computation types, making "Hybrid" inferred classification most appropriate. The categorization relies on interpreting different implementation examples (CA digital, BZ/soliton potentially analog).

### **5.3 Computational Primitive:**

*   **Vector ID:** M5.3
*   **Vector Type:** Function
    *   Content: [Collision-based Logic Gate]. The most basic computational primitive is the collision-based logic gate, where logical operations are realized by the interaction of mobile localizations during collisions. Examples include: Interaction Gate (Fig. 1a) implementing AND/XY; Switch Gate (Fig. 1b) routing signal based on control; XOR gate (Fig. 7) using Eater E6 and glider interactions. The mathematical description is implicit: logical functions are implemented by designing collisions to achieve Boolean outcomes (TRUE/FALSE) based on input and output localizations.
    *   **Sub-Type (if applicable):** Logic Gate: AND, OR, NOT, XOR, routing, switching functions.
    *   CT-GIN Mapping: Defines the primary function of the `ComputationNode`. `computationalPrimitive`: Collision-based Logic Gate, `gateTypes`: {AND, OR, NOT, XOR, SWITCH, FANOUT, ERASE}.
    *   Implicit/Explicit: Mixed
    * Justification: "Collision-based Logic Gate" is explicitly described as the principle of computation. Specific gate types (AND, OR, NOT, XOR, SWITCH) are exemplified, making subtypes explicit.  Mathematical descriptions are however implicit and functional - logic described abstractly at boolean level without explicit formulas for transformations beyond verbal descriptions and illustrations.

### **5.4 Embodied Computational Units**
* **Vector ID:** M5.4
* **Vector Type:** Table
*   Table:
| Unit ID | Description | Processing Power | Energy/Operation | Freq/Resp. Time | Bit-Depth | Data Source | Implicit/Explicit | Justification |
| :------ | :---------- | :--------------- | :--------------- | :--------------: | :-------: | :----------: |:-----------------:| :-----------------:|
| Billiard Ball Gate (Fig. 1) | Fredkin-Toffoli gate | Boolean Logic (AND, Switch) | N/A | Instantaneous (collision time) | 1-bit inputs | Fig. 1 | Explicit | Gate functionality and type directly from Fig. 1 description. No power data. |
| Spiral Rule CA Gates (Figs. 4-7) | Logic Gates (XOR, FANOUT, ERASE, Memory) | Boolean Logic (XOR, AND, OR implied) | N/A | CA Timestep (~1 step per operation) | 1-bit inputs, 6-bit memory | Figs. 4-7 | Explicit | Functionality derived from figures and descriptions in Sect 3.1. No energy/power specs given explicitly. |
| BZ Medium Gates (Figs. 13-14) | Interaction Gate (AND-like), 3-input Composite Gate | Boolean Logic (AND, composite functions) | N/A | Wave propagation time, simulation timestep | 1-bit inputs | Figs. 13-14 | Explicit | Gate functionality and type described based on wave collisions in BZ simulations, from Figs. 13, 14. No power data. |

## M6: Temporal Dynamics
*   **Vector ID:** M6
*   **Vector Type:** Temporal

### **6.1 Timescales:**

*   **Vector ID:** M6.1
*   **Vector Type:** ParameterTable
    *   Table:
        | Timescale Description | Value | Units | Source | Implicit/Explicit | Justification |
        | :-------------------- | :---: | :---: | :----: | :----------------: | :------------: |
        | CA Cell Update Time | 1 | timestep | Implicit | Implicit | Fundamental timescale is per CA iteration or timestep |
        | Glider Propagation Time (Spiral Rule CA) | Variable | timesteps | Implicit | Implicit | Dependent on distance, propagation occurs per timestep |
        | BZ Wave Propagation Time | Variable | simulation timesteps, or real-time if experiment | Implicit | Implicit | Dependant on distance, determined by reaction-diffusion and simulation timestep |
        | Memory Retention Time (E6 Eater) | Quasi-stationary | timesteps | Sect. 3.1 | Explicit | Memory retained as stable eater configuration unless actively changed |
        | Operation Time (Logic Gate) | ~1 collision event | timesteps or real-time | Implicit | Implicit | Operation time is roughly determined by the duration of signal collision events |

    *   **Note:** Listed are relevant timescales, which are mostly qualitative or relative within the system's operational context, as precise temporal metrics are not the focus of the publication.

### **6.2 Active Inference:**

*   **Vector ID:** M6.2
*   **Vector Type:** Assessment
    *   Content: [No]
    *   Justification: Active inference is not present, or not discussed, in the context of collision-based computing as described in this paper excerpt. The systems described are reactive and perform computations based on pre-defined rules or collision mechanics. There is no indication of: (1) prediction of future states – the system reacts to current inputs rather than proactively anticipating future inputs; (2) action selection to minimize discrepancies – operations are pre-determined logic gates, not dynamically chosen to optimize a goal; (3) internal models updated by experience – while memory exists, it stores bits, not environmental models; and the system's computation and behavior are not driven by minimizing prediction error or surprise.
    *   Implicit/Explicit: Implicit
        *  Justification: Absence of active inference is inferred from the descriptions focusing on rule-based, reactive computation and lack of discussion about prediction, model-based action or surprise minimization in system behavior or design. The absence is implied by the framework's current focus on implementing logic gates and machines rather than adaptive, model-driven agents.
    *   **If Yes/Partial, provide examples of testable CT-GIN metrics that *could* be used to quantify active inference:** [N/A]

## M7: Adaptation
*   **Vector ID:** M7
*   **Vector Type:** Adaptation

### **7.1 Adaptive Plasticity Presence:**

*   **Vector ID:** M7.1
*   **Vector Type:** Binary
    *   Content: [No]
    *   Justification: No, adaptive plasticity, as defined (persistent change in behavior or internal structure in response to experience, leading to improved performance over time), is not explicitly present or discussed in the context of the described collision-based computing systems. The systems perform pre-defined computations based on fixed CA rules or BZ reaction dynamics. While memory allows state changes to persist (a form of change), there’s no mechanism for the system to *improve performance* or alter its *functionality* based on past 'experience' or interaction history.  The CA rules and BZ dynamics are static, not adaptive.
    *    Implicit/Explicit: Explicit
        * Justification: Lack of adaptive plasticity is explicitly indicated by the focus on implementing logic gates and fixed computational paradigms. The description centers around pre-designed rules and functionalities, with no mention of learning, adaptation or change in fundamental system behaviors over time or based on interaction history. Operational descriptions highlight deterministic rule-following, not plasticity.

## M8: Emergent Behaviors
*   **Vector ID:** M8
*   **Vector Type:** Behavior

### **8.1 Behavior Description:**

*   **Vector ID:** M8.1
*   **Vector Type:** Description
    *   Content: The main functional behaviors of the described collision-based computing systems are: 1. Logical computation: Performing Boolean logic operations (AND, OR, NOT, XOR, SWITCH) through controlled collisions of mobile localizations (gliders, wave-fragments, billiard balls). 2. Information routing and signal processing: Guiding and manipulating information quanta (localizations) using stationary localizations (eaters, mirrors) in the medium to direct signals and implement logic circuits. 3. Memory storage and retrieval: Storing and reading binary information using stationary localization configurations (e.g., Eater E6 in Spiral Rule CA), enabling sequential operations and stateful computation. 4. Pattern formation: Self-organized generation of stable and mobile patterns (eaters, glider guns, gliders in CA) from initially random conditions, supporting a dynamic computational substrate. The overarching behavior is computation and information processing via localization dynamics and interactions in architecture-less media.
    *   CT-GIN Mapping: Defines the `BehaviorArchetypeNode`. `behaviorType`: Computation, Information Processing, Memory, Pattern Formation, `functionality`: Logical Operations, Signal Routing, Data Storage, Self-Organization.
    *    Implicit/Explicit: Explicit
       *  Justification: Functional behaviors are explicitly described throughout the paper, focusing on computation, logic gate implementation, signal routing, memory operations and pattern formation (self-organization in CA). These behaviors are the central theme of collision-based computing explained in the excerpt.

### **8.2 Behavior Robustness:**

*   **Vector ID:** M8.2
*   **Vector Type:** Score
    *   Score: [6]
    *   Justification: Robustness of behavior is moderate. For cellular automata, the glider-based computation is shown to be relatively stable against minor perturbations in the initial state that do not destroy the core gliders or eaters. Signal propagation and collision based computations seem robust to small deviations in glider trajectories or timing within the defined operational parameters of the CA rules. However, robustness against significant noise, large parameter variations in rules, or component failures is not systematically evaluated or discussed. Robustness in BZ medium systems might be more sensitive to external conditions and fluctuations in the chemical reaction dynamics, and is not rigorously quantified. Score is assigned considering some inherent stability in CA glider persistence and demonstrated function, but lack of quantified robustness metrics and tests against noise or component failure.
    *   Implicit/Explicit: Mixed
        *  Justification: Qualitative robustness is implied based on the existence of stable gliders and eaters and illustrative examples of gate operation. However, quantitative robustness metrics, operational window size, noise tolerance, and systematic robustness evaluations are absent, hence mixed (qualitative robustness implied, quantified is absent).
    *   CT-GIN Mapping: Contributes to the reliability attributes of the `BehaviorArchetypeNode`. `robustnessLevel`: Medium, `perturbationTypes`: {Noise (unspecified level), Parameter variations (unspecified range), Component failures (not tested)}.

### **8.3 CT-GIN Emergent Behavior Validation**

*    **Vector ID:** M8.3
*    **Vector Type:** Validation
     *  Content: Validation of emergent behaviors is primarily achieved through: 1. Operational definitions: Defining logical operations and memory in terms of glider collisions, eater state changes and signal trajectories, demonstrating functionality through simulations. 2. Visual inspection and simulation: Observing space-time diagrams and step-by-step evolutions (Figs. 2-7, 12-16) confirms intended signal propagation, localization interactions, gate operations and memory writing/reading at illustrative level. 3. Demonstrations of basic logic gates and memory units serve as functional validations for elementary computational primitives (Figs 1, 4-7, 13-14). Limitations of validation: 1. No comprehensive quantitative analysis: Lack of metrics for error rates, long-term reliability, or operational windows under various conditions. 2. Limited exploration of parameter space: Validation is mainly focused on demonstrating principle, not exhaustively testing parameter robustness or sensitivity. 3. Reproducibility implicitly assumed through deterministic CA rules and well-defined BZ models, but explicit reproducibility tests across varied random starting conditions are not reported quantitatively for all functions.
     *   Implicit/Explicit: Mixed
    *   Justification: Validation methods are described and implied through figures and operation descriptions (Explicit - visual validation, functional demonstration). Lack of comprehensive quantitative validation metrics, parameter space exploration and reproducibility tests are Implicit (by absence rather than direct statement).

## M9: Cognitive Proximity
*   **Vector ID:** M9
*   **Vector Type:** Cognition

### **9.1 Cognitive Mapping:**

*   **Vector ID:** M9.1
*   **Vector Type:** Description
    *   Content: There is a weak, metaphorical mapping to cognitive processes. The paper draws an analogy between mobile localizations (gliders, solitons, wave-fragments) as "quanta of information" and their interactions as "collision-based computing".  Furthermore, analogy to brain function is loosely alluded in the introduction by mentioning studies of "interaction of signals traveling along one-dimensional conductors" in physics, biology and physiology, and suggesting space-time granularity may be like "cellular automaton run by an enormous computer" (Fredkin, Toffoli's idea).  Limitations: These connections is very high-level, metaphorical, not a detailed mechanistic mapping to specific cognitive functions of biological systems. No specific cognitive architectures or functions are explicitly modeled or implemented in detail beyond basic Boolean logic and memory primitives, hence "weak" mapping.
    *   CT-GIN Mapping: If a mapping exists, this defines a `CognitiveMappingEdge`. Specify source and target (`BehaviorArchetypeNode` to `CognitiveFunctionNode`). `mappingType`: Metaphorical Analogy, `sourceNode`: `BehaviorArchetypeNode: Computation`, `targetNode`: `CognitiveFunctionNode: Information Processing (low-level)`.
    *   Implicit/Explicit: Mixed
    * Justification: Metaphorical mapping is implicit, alluded to in the introduction and conceptual framing, suggesting brain-like information processing in broad terms. Specific cognitive functions or detailed mapping are absent, making explicit cognitive function mapping "None", while a general conceptual analogy exist implicitly.

### **9.2 Cognitive Proximity Score:**

*   **Vector ID:** M9.2
*   **Vector Type:** Score
    *   Score: [2]
    *   Justification: Cognitive Proximity Score of 2 (Sub-Organismal Responsivity). The system demonstrates basic stimulus-response (signal input-logic gate output) and a very basic form of adaptation/plasticity only through memory storage (bit writing). It however lacks complex representation, goal-directedness, contextual understanding, abstract reasoning, social interaction or self-awareness. Computations are limited to simple Boolean logic and basic memory operations.  The system is far from exhibiting even simple organism-level cognition; it is closer to engineered functional materials with specific functionalities. The score reflects the very low level of cognitive traits beyond simple reactive behavior and memory primitives.
    *   Implicit/Explicit: Mixed
    *  Justification: Score is judged based on the CT-GIN Cognizance Scale—system fits Level 2 (Sub-Organismal Responsivity): Basic stimulus-response, very basic memory, adaptation form weak plasticity only through stored bit, but no higher cognitive functions or complex representation. Reasoning is based on system capabilities described and compared to the Cognizance Scale's levels. Score reflects limitations based on observed functionalities and comparison against scale levels.

**CT-GIN Cognizance Scale:**

*   **Level 0: Non-Cognitive:** Purely reactive system.  No internal state beyond immediate stimulus-response.
*   **Level 1: Simple Responsivity:** Basic stimulus-response behavior.  Reactions are fixed and predetermined.
*   **Level 2: Sub-Organismal Responsivity:**  Behavior exhibits basic forms of adaptation or plasticity, but lacks complex representation or goal-directedness. **[System fits here most closely]**
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
    | Sensing/Perception               |      2       | Basic "sensing" of signal presence/absence; minimal sensory abstraction                | `CognitiveFunctionNode: Sensing` | Implicit | Sensing limited to signal detection for computation input; not rich sensory input |
    | Memory (Short-Term/Working)        |      4       | Basic memory storage (Eater) for short-term bit retention, limited working memory concept | `CognitiveFunctionNode: Memory (Short-Term)` | Explicit | Eater E6 provides short-term bit storage as flip-flop memory.  |
    | Memory (Long-Term)                 |      4       | Memory retention is long-term in the context of CA operation - static unless changed. | `CognitiveFunctionNode: Memory (Long-Term)` | Explicit | Eater memory is stable unless actively erased, hence "long-term" in CA context |
    | Learning/Adaptation              |      1       | No inherent learning or adaptation mechanism described beyond fixed rules              | `CognitiveFunctionNode: Learning` | No | Rules and gate operations are pre-defined and static. |
    | Decision-Making/Planning          |      2       | Very basic "decision" at logic gate level (AND, XOR), no planning or goal-directedness | `CognitiveFunctionNode: Decision Making` | Implicit | Decisions are pre-programmed logic gate operations, not flexible choices |
    | Communication/Social Interaction |      0       | Absent; no communication or interaction with external agents                         | `CognitiveFunctionNode: Communication` | No | System operates in isolation; no social or communication functions |
    | Goal-Directed Behavior            |      1       | No goal-directed behavior beyond executing pre-programmed logic operations            | `CognitiveFunctionNode: Goal-Directed Behavior` | No | Behavior is rule-driven, not goal-seeking beyond pre-set functions. |
    | Model-Based Reasoning              |      0       | Absent; no evidence of internal models or reasoning mechanisms                         | `CognitiveFunctionNode: Reasoning` | No | System works on direct signal manipulation, no model-based inferences |
    | **Overall score**                 |    [2.0]          |                                                                                       |                                   |                     |                |

    *   **Note:** Average score is automatically calculated as 2.0 (rounded from 2.14).

## M10: Criticality Assessment
*   **Vector ID:** M10
*   **Vector Type:** Criticality

### **10.1 Criticality:**

*   **Vector ID:** M10.1
*   **Vector Type:** Assessment
    *   Content: [No]
    *   Justification: The paper does not explicitly discuss criticality or operation near a critical point for the described collision-based computing systems.  There is no mention of scale-free behavior, power laws, or long-range correlations in the context of CA rules or BZ dynamics.  Descriptions focus on deterministic rules, localized interactions and specific functional modules (gates, memory), rather than emergent statistical properties associated with criticality and complex systems operating at phase transitions.  Criticality is not a conceptual framework used in this publication to understand or design the system.

        *   Critical Parameters (If Yes/Partial): [N/A]
        *   Evidence: [No explicit mention or evidence. Absence of scale-free behavior or power laws in the description or figures.]
    *   Implicit/Explicit: Explicit
    *    Justification: Absence of criticality is explicit by lack of mention or discussion. The paper frames system in computer science and logic gate terms, not statistical physics or complexity theory, which are the domain of criticality discussion. Explicitly, no such terms are present in the provided excerpt and the described model framework aligns toward deterministic computation rather than critical phenomena.

## M11: Review Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Review")**

*   **Vector ID:** M11
*   **Vector Type:** Review

This Module is skipped because the paper type is "Theoretical/Computational", not "Review".

## M12: Theoretical Paper Specifics (Conditional)

**(This entire module is conditional and *only* appears if the paper type is "Theoretical")**

*   **Vector ID:** M12
*   **Vector Type:** Theory

### **12.1 Theoretical Rigor:**

*   **Vector ID:** M12.1
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The theoretical framework presented for collision-based computing is reasonably rigorous within the scope defined. Cellular automata rules are mathematically well-defined, and the concept of information processing via localization collisions is logically consistent with the description of basic gates and memory. The paper builds upon established models (billiard ball model, Fredkin-Toffoli gates, Turing machines, cyclic tag systems) and provides illustrative examples in diverse media (CA, BZ, abstract geometry).  However, some derivations or proofs of computational universality beyond simple examples are not detailed exhaustively in this excerpt and formal proofs of properties in all media are not provided. The rigor is focused more on conceptual demonstration of computability principles rather than exhaustive formal mathematical treatment. Internal consistency is good within the presented scope for conceptual framework and basic examples' descriptions.
       * Implicit/Explicit: Mixed
       *  Justification: Theoretical rigor in CA/computational models and logic gate frameworks is explicit. Deeper mathematical proofs of universality, detailed derivations, or exhaustive consistency proofs beyond illustrative examples areImplicit (by absence). Score reflects good conceptual rigor balanced with limited formal mathematical depth in this excerpt.

### **12.2 Realization Potential:**

*   **Vector ID:** M12.2
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: Realization potential is assessed as Moderate-High. Cellular automata are readily simulated and implemented in digital hardware, and the Spiral Rule CA is presented as a concrete example with well-defined rules. BZ medium implementations, while more complex experimentally, are also discussed with reference to lab conditions, indicating physical realizability in principle (although challenges in control and scalability remain). Billiard ball model is more conceptual but has simplified CA implementations. Abstract geometrical computation is highly idealized but provides conceptual insights. Potential fabrication pathways for CA and BZ systems are plausible given existing technologies (microfluidics, chemical reactors, digital emulators). Fundamental limitations for physical implementations are not explicitly addressed in detail (e.g., noise sensitivity in BZ, scaling limits for CA complexity), so assessment is positive but has caveats. Score reflects reasonable feasibility of realizing basic collision-based computation principles, but acknowledging practical challenges for complex, scalable, and robust physical systems.
    *   Implicit/Explicit: Mixed
    *  Justification: Realization potential for CA and BZ is implied as reasonably feasible, mentioned with respect to simulations and laboratory conditions (Explicit - BZ medium as natural system). Detailed feasibility analysis, fabrication pathways, and addressing fundamental limitations (scalability, noise) are more Implicit - not fully discussed or quantified in detail in this excerpt. Score reflects combined explicit indications and implicit challenges.

### **12.3 Potential for Future CT-GIN Implementation Score**

* **Vector ID:** M12.3
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: Potential for future CT-GIN implementation is Moderate-High. Collision-based computing framework addresses key CT-GIN themes by providing building blocks for computation (gates, memory), self-organization (CA pattern formation), exploiting non-linearity (collisions), and architecture-less distributed computation. Novelty lies in its media-agnostic approach and use of physical phenomena (collisions) for computation directly. Potential impact on CT-GIN is significant by offering a diverse set of substrates and mechanisms for realizing embodied intelligence and computation within material systems, moving beyond traditional electronic circuits. Alignment with CT-GIN principles is strong in emphasizing distributed, physics-based, self-organizing computation rather than centralized control and pre-defined architectures. Score reflects strong conceptual potential and alignment, needs further concrete experimental demonstration and deeper integration into CT-GIN to reach higher scores.
    *    Implicit/Explicit: Mixed
    *   Justification: High potential for CT-GIN *alignment* is directly derivable from the conceptual fit and architecture-less, distributed nature (Explicit). Concrete future CT-GIN *implementation* potential and its impact beyond conceptual level are more Implicit, needing further experimental validation and detailed CT-GIN framework integration to ascertain full impact. Score represents potential based on conceptual fit, but needs more substantial demonstrated implementation to score higher.

## M13: Overall Assessment & Scoring

*   **Vector ID:** M13
*   **Vector Type:** Overall

### **13.1 CT-GIN Readiness Score:**

*   **Vector ID:** M13.1
*   **Vector Type:** Score
*   **Calculated Score:** [5.8]

**CT-GIN Readiness Summary Table:**

| CT-GIN Aspect                   | Strength (Yes/Partial/No) | Key Supporting Metrics (with units) | Limitations (Missing Metrics/Data Gaps)                                           | Improvement Areas (Future Research)                                          |
| :------------------------------ | :-----------------------: | :-----------------------------------| :------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| Energy Flow Efficiency          | Partial                    | Qualitative assessment: Medium      | Energy consumption per operation, dissipation mechanisms quantified               | Quantify energy efficiency for different implementations                             |
| Memory Fidelity                 | Yes                        | 6-bit capacity, Qualitative: High Fidelity | Quantitative error rates, degradation rate                                       | Quantify memory fidelity, robustness, retention limits.                        |
| Organizational Complexity       | Yes                        | Emergent eaters, glider guns, gliders | Predictability of global patterns quantified                                     | Quantify predictability of emergent order, explore more complex rule sets.     |
| Embodied Computation            | Yes                        | Logic Gates (AND, XOR, Switch)      | Computational power beyond basic gates, scalability, complexity metrics          | Develop more complex computational primitives and architectures.             |
| Temporal Integration            | Partial                    | Timescales of CA timestep and Wave propagation | Precise values and control over timescales quantified                           | Quantify and control temporal dynamics, explore complex temporal coding.      |
| Adaptive Plasticity             | No                         | None                                 | Adaptive mechanism description and demonstration.                                | Implement adaptive plasticity, learning mechanisms.                           |
| Functional Universality         | Yes                        | Turing Machine, Cyclic Tag System implementations | Experimental demonstration of universal computation                               | Experimentally demonstrate and validate computational universality.         |
| Cognitive Proximity            | No                         | None                                 | Mapping to higher cognitive functions, demonstrable higher-level behaviour.      | Move beyond basic logic, explore function closer to cognitive primitives.      |
| Design Scalability & Robustness | Partial                    | Qualitative assessment: Moderate    | Quantified robustness metrics, scalability analysis                               | Quantify robustness against noise, parameter variations, analyze scalability. |
| **Overall CT-GIN Readiness Score** |           |   |   |      |


### **13.2 Qualitative CT-GIN Assessment Conclusion:**

*   **Vector ID:** M13.2
*   **Vector Type:** Textual Summary
    *   Content: The analysis reveals that "Collision-based Computing" presents a significant conceptual framework for material intelligence within CT-GIN. Key strengths include the demonstration of embodied computation, self-organization in cellular automata, and the potential for functional universality. The system shows moderate implementation clarity and theoretical rigor within its defined scope. Key limitations lie in the lack of quantified metrics for energy efficiency, memory fidelity, robustness and predictability of emergent order. Adaptive plasticity and higher-level cognitive functions are absent. Overall assessment indicates a Moderate level of CT-GIN Readiness. The framework provides valuable building blocks, but requires further research for quantifiable validation, enhanced robustness, higher functional complexity and integration of adaptive and cognitive aspects to fully realize its potential in cognizant matter.

### **13.3 CT-GIN Refinement Directions:**

*   **Vector ID:** M13.3
*   **Vector Type:** Recommendations
    *   *   Quantify energy efficiency of collision-based computing implementations across different media (CA, BZ, solitons), using metrics like energy per operation or energy dissipation rates.
    *   Develop quantitative metrics for memory fidelity, robustness (error rates, noise tolerance), and retention time in CA and BZ memory implementations, and experimentally validate them.
    *   Investigate and quantify the predictability and controllability of self-organized patterns in Spiral Rule CA, potentially using information-theoretic measures or statistical analysis of emergent structures.
    *   Explore and implement more complex computational primitives and higher-level computational architectures beyond basic logic gates using collision-based principles.
    *   Quantify timescales of temporal dynamics, aiming for precise control over response times, signal propagation speeds, and memory access latencies.
    *   Integrate adaptive plasticity mechanisms into collision-based systems, enabling learning and adaptation of computational rules or system parameters based on interaction history or environmental changes.
    *   Attempt to move from low level logic gates to higher cognitive primitive implementation, exploring more complex functions beyond boolean operations, inspired by cognitive science and neuroscience.
    *   Conduct systematic robustness analysis against noise, parameter variations, and component failures for both CA and BZ based collision-based computing implementations, experimentally or computationally.

## M14: CT-GIN Knowledge Graph

*   **Vector ID:** M14
*   **Vector Type:** Visualization

### **14.1. CT-GIN Knowledge Graph:**
* **Content:**
![CT-GIN Knowledge Graph for Collision-based Computing](https://raw.githubusercontent.com/bkgraphs/material-intelligence-framework/main/templates/CBC_KG.png)

## M15: Relationship Vectors
*   **Vector ID:** M15
*   **Vector Type:** Relationships
*   Relationships:
        | Source Vector ID | Target Vector ID | Relationship Type |
        | ------------- | ------------- | ----------------- |
        | M2.1 | M2.2 | EnergyTransduction |
        | M2.2 | M5 | SupportsComputation |
        | M2.2 | M3 | SupportsMemory |
        | M4.2 | M4.3 | Adjunction |
        | M5.1 | M5.2 | InstanceOf |
        | M5.1 | M5.3 | ImplementsPrimitive |
        | M3.1 | M3.2 | CharacterizedBy |
        | M3.1 | M3.3 | CharacterizedBy |
        | M4.1 | M4.2 | GovernedByRules |
        | M4.1 | M4.3 | ResultsInOrder |
        | M8.1 | M9.1 | CognitiveMapping |

## M16: CT-GIN Template Self-Improvement Insights

*   **Vector ID:** M16
*   **Vector Type:** Feedback

### **Template Feedback:**

*    **Vector ID:** M16.1
*   **Vector Type:** Text
Provide specific, actionable feedback on the *CT-GIN template itself*, based on this analysis:
    *   **Missing Probes:** The template is largely comprehensive. Perhaps probes for *scalability*, *fault-tolerance* specifically within M8.2 and M13.1 could be added as distinct aspects to assess. Also a direct probe questioning "Universality" of computation (Y/N with justification) within M5 could be useful.
    *   **Unclear Definitions:** Definitions for "Implicit" vs "Mixed" may need minor clarification (current definitions are mostly clear but slightly overlapping). The distinction between Implicit, Mixed and Inferred needs to be very precisely defined and perhaps examples added.
    *   **Unclear Node/Edge Representations:** Guidance was sufficient for this paper. Perhaps clarification on representing rule-based systems (like CA) in CT-GIN might be beneficial—e.g., rule matrices as node/edge attributes vs. separate rule nodes.
    *   **Scoring Difficulties:** Scoring for "Predictability of Global Order" (M4.4) and "Cognitive Proximity" (M9.2) is somewhat subjective. Providing more detailed rubrics with more granular levels and specific example criteria for intermediate scores (e.g., scores 3, 5, 7) could enhance scoring consistency. The scoring rubric is very helpful as is but more granular anchors for mid-range values on the scale (especially for cognitive proximity) would further enhance scoring.
    *   **Data Extraction/Output Mapping:** Data extraction was straightforward for explicit parameters. Implicit assessments required more interpretation. Mapping to the table formats required care to align with columns and units, but was manageable.
    *   **Overall Usability:** The template is generally usable and well-structured. The modular format is effective. Navigation is clear through Vector IDs. Instructions are clear.
    * **Specific Suggestions:**
        * Add probes for "Scalability" and "Fault-Tolerance" in M8.2 and M13.1 for more granular robustness assessment.
        * Add explicit probe in M5 to directly assess for "Computational Universality" (Yes/No) with Justification.
        * Refine scoring rubrics, particularly for subjective scores (M4.4, M9.2) to increase consistency and clarity of mid scale values, by adding detailed anchors example for intermediate values.
        * Further clarify "Implicit," "Mixed," and "Inferred" classifications with illustrative examples to ensure consistent categorization.```
**Instructions**

*   Answer ALL questions as completely as possible, using the publication as your primary source of information.
*   Provide quantifiable metrics with explicit units whenever possible. Use SI units where feasible.
*   If a parameter cannot be quantified, provide a qualitative assessment (e.g., Low/Medium/High, Short-term/Long-term) with a detailed justification.
*   Clearly state the CT-GIN mapping for each element (node/edge type and attributes). This is primarily for structuring the information and will be used to populate the knowledge graph.
*   For each answer, specify whether the information is Explicit, Implicit, or Mixed in the paper, and *briefly* justify this categorization. Use the following definitions:
    *   **Explicit:** Directly stated in the paper (e.g., a quoted sentence, a numerical value from a table).
    *   **Implicit:** Not directly stated, but can be reasonably inferred from the information provided in the paper.
    *   **Mixed:** The answer combines both explicit statements and implicit inferences.
    *   **Inferred:** Not directly stated and relies on the broader, not contained in the publication, knowledge.
*   Use the provided Vector ID for each question.
*   Respond in Markdown *without* echoing the probes from this template (use only the structure, titles, and your responses).
* All tables need to have complete headers.

---

# Collision-based Computing

__Paper Type:__ Theoretical/Computational

## M1: System Overview & Implementation
*   **Vector ID:** M1
*   **Vector Type:** Overview

### **1.1 System Description**

*   **Vector ID:** M1.1
*   **Vector Type:** Description
    *   Content: Collision-based computing is described as an implementation of logical circuits and mathematical machines within homogeneous, uniform, architecture-less media. The system uses mobile localizations, such as gliders in cellular automata or solitons in optical systems, to represent quanta of information. Logical truth and false are represented by the presence or absence of these localizations, or by their internal states. Computation occurs through the collisions of these localizations, which alter their trajectories and states, representing logical operations. The medium is architecture-less, lacking hardwired components, with signal paths being momentary trajectories of propagating quanta. The described systems include 1D and 2D cellular automata, continuous excitable media, and geometrical computation with dimensionless particles.
    *   CT-GIN Mapping: `SystemNode` attributes: `systemType`: Collision-based Computing, `domain`: Computer Science, Physics, Chemistry `mechanism`: Mobile localization collision, `components`: Mobile localizations (gliders, solitons, wave-fragments, billiard balls), Stationary localizations (still lives, blocks, eaters, mirrors),  `purpose`: Implementation of logical circuits and mathematical machines.
    *   Implicit/Explicit: Explicit
        *  Justification: The system description is explicitly stated in the abstract and introduction sections of the provided text.

### **1.2 Implementation Clarity**

*   **Vector ID:** M1.2
*   **Vector Type:** Score
    *   Score: [8]
    *   Justification: The paper provides a relatively clear conceptual description of collision-based computing and gives examples in various media (cellular automata, reaction-diffusion, Belousov-Zhabotinsky medium, billiard balls, abstract geometrical computation). The principles and examples of basic gates (interaction gate, switch gate, XOR gate, FANOUT gate, ERASE gate) and memory implementation are described with figures, clarifying how computation is envisioned. However, detailed implementation parameters and full algorithms for complex computations are not exhaustively provided, and the emphasis is more on the conceptual framework and possibilities rather than a fully detailed blueprint.
    *   Implicit/Explicit: Mixed
        * Justification: The conceptual framework is explicitly described, but some details of concrete, scalable implementations are implicit or left for further research and experimentation. The score reflects the clarity of the core concepts and basic examples, but acknowledges the lack of exhaustive implementation details.

### **1.3 Key Parameters**

*   **Vector ID:** M1.3
*   **Vector Type:** ParameterTable
    *   Table:
        | Parameter Name | Value | Units | Source (Fig/Table/Section) | Implicit/Explicit | Data Reliability (High/Medium/Low) | Derivation Method (if Implicit) |
        | :------------- | :---: | :---: | :-----------------------: | :-----------------: | :-----------------------------: | :-------------------------------: |
        | Cell states (Spiral Rule CA) | 3 | states | Sect. 3.1 | Explicit | High | N/A |
        | Neighborhood (Spiral Rule CA) | 7 | cells | Sect. 3.1 | Explicit | High | N/A |
        | Time step (BZ medium simulation) | 1E-3 |  - | Sect. 3.2 | Explicit | Medium | N/A |
        | Grid point spacing (BZ medium simulation) | 0.15 | - | Sect. 3.2 | Explicit | Medium | N/A |
        | States (2-state CA) | 2 | states | Sect. 4.2.2 | Explicit | High | N/A |

    *   **Note:** Listed are key parameters characterizing the system's implementation across different examples discussed in the paper.

## M2: Energy Flow
*   **Vector ID:** M2
*   **Vector Type:** Energy

### **2.1 Energy Input**

*   **Vector ID:** M2.1
*   **Vector Type:** Input
    *   Content: For Cellular Automata (Spiral Rule): The energy input is implicitly through the initial configuration of cell states. The dynamics of the cellular automaton itself, governed by the transition rules, drives the evolution and propagation of localizations. For the Belousov-Zhabotinsky (BZ) medium: The energy source is the chemical energy stored within the reactants of the BZ reaction itself. Additionally, light-sensitive BZ reaction models utilize illumination as an external excitability parameter modulation.
    *   Value: N/A (Qualitative description)
    *   Units: N/A
    *   CT-GIN Mapping: `EnergyInputNode` attributes - `source`: Initial configuration (CA), Chemical reactants & illumination (BZ), `type`: Initial potential energy, Chemical and light energy.
    *   Implicit/Explicit: Mixed
        *  Justification: While the text explicitly mentions "non-dissipative computer" designs historically, the specific energy input for the described implementations is mostly implicit, requiring inference from the descriptions of CA rules and BZ reaction dynamics. The source is conceptually stated (chemical, initial configuration), but values are not quantified.

### **2.2 Energy Transduction**

*   **Vector ID:** M2.2
*   **Vector Type:** Transduction
    *   Content: In Cellular Automata: Energy transduction is represented by the state transitions of cells based on local neighborhood configurations. The update rules effectively transduce the initial spatial distribution of states into temporal evolutions of patterns, gliders, and stationary localizations. The energy is effectively transduced from the initial configuration into the kinetic energy of glider propagation and pattern formation. In Belousov-Zhabotinsky medium: Chemical energy is transduced into propagating wave fronts (localizations) through reaction-diffusion processes. Light energy modulates the excitability of the medium, influencing wave initiation and propagation. Collisions transduce kinetic energy into changes in velocity vectors and states of localizations, realizing computational operations.
    *   CT-GIN Mapping: `EnergyTransductionEdge` attributes - `mechanism`: State transition rules (CA), Reaction-diffusion, light modulation (BZ), Collision events, `from_node`: `EnergyInputNode`, `to_node`: `ComputationNode`, `MemoryNode`, `SelfOrganizationNode`.
    *   Implicit/Explicit: Mixed
        *  Justification: The mechanisms of energy transduction (state transitions in CA, reaction-diffusion and light modulation in BZ) are implicitly explained by describing system behavior and referring to models.  The physical mechanisms are described conceptually, but efficiency metrics or detailed formulas are not provided, hence "mixed".

### **2.3 Energy Efficiency**

*   **Vector ID:** M2.3
*   **Vector Type:** Score
    *   Score: [5]
    *   Justification/Metrics: The paper mentions Fredkin and Toffoli's aim to design non-dissipative computers, suggesting an aspiration for high energy efficiency in collision-based computing conceptually. However, the provided excerpt does not include quantifiable energy efficiency metrics for the specific CA or BZ systems described. Efficiency in CA might be related to minimizing state changes per computation, while in BZ it could involve minimizing reactant consumption per operation. Qualitatively, efficiency is likely Medium, as collisions and state changes inherently involve some dissipation, although the architecture-less nature might avoid some overhead of traditional circuits. Score is estimated based on the general discussion about energy conservation in collision-based computing, but lack of specific metrics for described systems.
    *   CT-GIN Mapping: Attribute of relevant `EnergyTransductionEdge`s - `efficiency`: Qualitative assessment: Medium.
    *   Implicit/Explicit: Implicit
      *  Justification: Efficiency is discussed conceptually in relation to Fredkin-Toffoli's goal, but without quantitative metrics or detailed analysis for the examples discussed.  Score is inferred from the general context rather than explicitly stated values.

### **2.4 Energy Dissipation**

*   **Vector ID:** M2.4
*   **Vector Type:** Dissipation
    *   Content: Energy dissipation mechanisms are implicitly present in both CA and BZ systems. In cellular automata, dissipation may occur due to irreversible state transitions and the maintenance of stationary localizations (eaters). In the BZ medium, dissipation is inherent in the chemical reactions themselves, which are thermodynamically irreversible, and in diffusion processes.  The paper does not quantify energy dissipation in either system. It is implicitly suggested to be present but minimized in some designs, especially in early billiard ball models aiming for non-dissipative logic. Qualitative assessment is Medium, as energy is required to sustain the dynamics and computations, but system-level dissipation rates are not quantified.
    *   CT-GIN Mapping: Creates `EnergyDissipationNode`s and `EnergyDissipationEdge`s - `dissipationMechanism`: Irreversible state transitions (CA), Irreversible chemical reactions, diffusion (BZ), `dissipationLevel`: Qualitative Assessment: Medium.
    *    Implicit/Explicit: Implicit
        *  Justification: Dissipation mechanisms are not explicitly quantified or detailed in terms of specific energy loss rates or values. Their presence is inferred from the nature of CA dynamics and BZ reactions and the general context discussion around energy efficiency.

## M3: Memory
*   **Vector ID:** M3
*   **Vector Type:** Memory

### **3.1 Memory Presence:**

*   **Vector ID:** M3.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: Yes, memory is present in the Spiral Rule CA in the form of "eaters". The eater E6 is described as a 6-bit flip-flop memory device. It can store information by switching substrate sites to inhibitor states, which persists beyond the writing stimulus (a colliding glider). This stored state influences future behavior, as reading the memory (Fig. 5) depends on the state of the eater, and the eater retains the bit until it is erased.
    *    Implicit/Explicit: Explicit
        * Justification: The presence of memory using eater E6 is explicitly described and exemplified in Section 3.1 with figures and operational descriptions of writing and reading bits (Figs. 4 and 5).

### **3.2 Memory Type:**

*   **Vector ID:** M3.2
*   **Vector Type:** Score
*   Score: [7]
*   Justification: The memory type can be classified as a re-writable, multi-state (at least 6-bit), and relatively stable form of memory within the context of the Spiral Rule CA.  The eater offers persistent states that are maintained until actively changed by glider collisions. Retention is relatively long-term within simulation time scales. Read-out accuracy is implied to be high, as bit reading via glider collision is demonstrated through figure illustration, accurately reflecting stored information if properly designed and operated. The score is assigned considering the deterministic nature of the CA, and the demonstrated rewrite capability and stability, though detailed error rates or long-term retention beyond simulation times are not quantified, lowering the score from perfect fidelity.
*   CT-GIN Mapping: Defines the `MemoryNode` type. `memoryType`: Flip-flop (6-bit), `medium`: Spiral Rule Cellular Automata.
*    Implicit/Explicit: Mixed
    * Justification: The type as "flip-flop", re-writable is explicit from the description. The score and detailed characteristics (retention, accuracy) are inferred from the functional descriptions of write and read operations, combined with the deterministic nature of the CA.

### **3.3 Memory Retention Time:**

*   **Vector ID:** M3.3
*   **Vector Type:** Parameter
*   Value: [Quasi-stationary]
*    Units: [Time steps of CA simulation] (or Qualitative Descriptor: "Long-term" relative to computation)
*   Justification: The eater E6, once a bit is written, remains in that state in a "quasi-stationary configuration" as stated in the text. The memory is retained indefinitely within the context of the automaton evolution towards quasi-stationary states, and is stable unless actively erased by another glider collision. Thus retention is long-term relative to the timescale of glider-based computation within the described examples. Actual time values or quantitative retention decay rates are not provided.
*    Implicit/Explicit: Mixed
        * Justification: "Quasi-stationary" and stable is explicit. Quantifiable retention time and units are implicit/qualitative ("long-term" in CA context, inferred from functional descriptions and quasi-stationary nature).

### **3.4 Memory Capacity (Optional - if applicable)**

* **Vector ID:** M3.4
* **Vector Type:** Parameter
*  Value: [6]
*   Units: [bits]
*   Justification: Eater E6 is explicitly described as a "6-bit flip-flop memory device", indicating a capacity to store 6 bits of information.
*    Implicit/Explicit: Explicit
        *  Justification: Directly stated in the text description of Eater E6, Sect. 3.1.

### **3.5 Readout Accuracy (Optional - if applicable)**

* **Vector ID:** M3.5
* **Vector Type:** Parameter
*   Value: [High]
*   Units: [%, error rate implicitly low]
*   Justification: Readout accuracy is qualitatively high, as depicted in Fig. 5. The transformation of the reading glider (G34 to G4) upon interaction with a bit-up state in E6 provides a deterministic and distinct output, indicating accurate retrieval of the stored bit value within the deterministic rules of the CA.  Error rate is implicitly assumed to be low given the deterministic nature of the system and the illustrative figure example working as expected, although formal error rates are not quantified explicitly.
*    Implicit/Explicit: Mixed
       *  Justification: Qualitative assessment "High" is inferred from the deterministic nature of the CA ruleset and functionality shown in figures.  Accuracy values and quantitative metrics are not explicitly given but implied to be good as a functional memory cell is demonstrated.

### **3.6 Degradation Rate (Optional - if applicable)**
* **Vector ID:** M3.6
* **Vector Type:** Parameter
    *   Value: [Negligible over relevant timescales]
    *   Units: [% loss per hour]
    *   Justification: Degradation rate is expected to be negligible over relevant timescales of computation and simulation runtime, considering the description of Eater E6 and quasi-stationary states of Spiral Rule CA. The memory state is persistent unless actively erased by another controlled glider collision. No active degradation mechanism is mentioned; the system naturally evolves to stable or quasi-stable configurations. Degradation is inferred to be minimal for practical purposes in the operational context shown.
    *    Implicit/Explicit: Implicit
            * Justification:  Degradation is not explicitly quantified. The assessment is inferred from the description of quasi-stationary behavior and no mention of spontaneous bit-flipping or decay within the simulation timescales described in the paper.

### **3.7 Memory Operations Energy Cost (Optional - if applicable)**
* **Vector ID:** M3.7
* **Vector Type:** Table
*   Table:
    | Memory Operation ID | Energy Consumption per Bit | Power Usage during Operation| Units | Uncertainty | Data Source Reference | Implicit/Explicit | Justification |
    | :------------------ | :--------------------------: | :-----------------------------: | :---: |:-----------------:|:-----------------:|:-----------------:| :------------------ |
    | Write Bit         | N/A                            | N/A                                 | N/A   | N/A            | N/A               | Implicit           | Energy cost is not explicitly quantified; inferred to be related to cell state changes propagated by glider collision within the CA update cycle. |
    | Read Bit          | N/A                            | N/A                                 | N/A   | N/A             | N/A              | Implicit           | Energy cost is not explicitly quantified; inferred to be related to cell state changes propagated by glider collision within the CA update cycle. |
    | Erase Bit          | N/A                            | N/A                                 | N/A                                  | N/A             | N/A              | Implicit           | Energy cost is not explicitly quantified, inferred to be similar to write and read operations in terms of cell state changes per CA update. |
*   Implicit/Explicit: Implicit
    *   Justification: Energy consumption and power usage for memory operations are not explicitly quantified or measured in the provided text.  The values are marked N/A, as no data is present.

### **3.8 Memory Fidelity & Robustness Metrics (Optional - if applicable)**
* **Vector ID:** M3.8
* **Vector Type:** Table
*   Table:
    | Metric ID | Description | Value | Units | CT-GIN Mapping | Data Source | Implicit/Explicit | Justification |
    | :-------- | :---------- | :----: | :---: | :-------------: | :----------: |:-----------------:| :-----------------:|
    | Bit Stability | Probability of bit remaining unchanged in storage | High | Qualitative | Attribute of MemoryNode | Text description of Eater and CA stability | Implicit | Bit stability is qualitatively high due to the quasi-stationary nature of the eater in the CA and deterministic update rules. No degradation is mentioned over relevant timescales. |
    | Write Fidelity | Probability of correctly writing a bit | High | Qualitative | Attribute of MemoryOperation | Fig. 4 (Write Bit) | Implicit |  Write fidelity is implicitly high, exemplified by the successful bit writing in figure illustrations, showing intended state change upon glider collision. No error rates are provided. |
    | Read Fidelity | Probability of correctly reading a bit | High | Qualitative | Attribute of MemoryOperation | Fig. 5 (Read Bit) | Implicit | Read fidelity is implicitly high, exemplified by successful bit reading in figure illustration, showing expected glider transformation dependent on memory state. No error rates are provided. |
*   Implicit/Explicit: Implicit
*   Justification: Fidelity and robustness metrics are assessed qualitatively as "High," inferred from functional demonstrations of memory operations and the deterministic nature of the CA, but are not explicitly quantified with error percentages or similar metrics in the text.

---

## M4: Self-Organization and Emergent Order
*   **Vector ID:** M4
*   **Vector Type:** Self-Organization

### **4.1 Self-Organization Presence:**

*   **Vector ID:** M4.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: Yes, self-organization is present in the Spiral Rule CA. The paper mentions that starting from a random initial configuration, the automaton evolves towards a "quasi-stationary configuration, with typically two types of stationary localizations, and a spiral generator of mobile localizations, or gliders". This emergence of ordered structures (stationary eaters and spiral glider guns) from initially random states, driven by local cellular automaton rules, exemplifies self-organization. The global order (spiral guns, eaters) arises spontaneously from the local update rules without external design of these higher-level structures.
    *   Implicit/Explicit: Explicit
        *  Justification: Explicitly stated in Sect. 3.1 and visualized in Fig. 2 that starting from random initial conditions, ordered structures like stationary localizations and spiral glider-guns emerge. This spontaneous pattern formation is a signature of self-organization within the CA dynamics.

### **4.2 Local Interaction Rules:**

*   **Vector ID:** M4.2
*   **Vector Type:** Rules
    *   Content: The local interaction rules for the Spiral Rule Cellular Automaton are defined by a totalistic hexagonal cellular automaton where each cell updates its state (Substrate S, Activator A, Inhibitor I) based on the number of neighbors in each state. The update rule is compactly represented by a 7x7 matrix M, where M_ij determines the next state of a cell based on `i` neighbors in state I and `j` neighbors in state A. The transition matrix M is explicitly given as:
    ```
    M=
    
    S
    S
    S
    S
    
    
    S AI AI I I I
    S
    S
    SI A
    I
    I
    I
    I
    AI I I I I I
    I I I
    I I I
    
    ```
    The rules are derived from quasi-chemical reactions described as:
    A+6S→A, A+ I →I, A+ 3I →I, A+ 2I →S, 2A →I, 3A→A, βA→I, I →S. These rules effectively emulate activator-inhibitor dynamics for sub-threshold concentrations of activator.
    *   CT-GIN Mapping: Part of the `AdjunctionEdge` description (local side). Define "LocalInteraction" category of edges. `interactionType`: Cellular Automaton Rule, `ruleMatrix`: M, `neighborhoodType`: Hexagonal, `stateTypes`: {S, A, I}.
    * **Implicit/Explicit**: Explicit
        *  Justification: The local interaction rules are explicitly provided in Sect. 3.1, including both the quasi-chemical reactions and the transition matrix M defining the cellular automaton update function.

### **4.2.1 Local Interaction Parameters:**

* **Vector ID:** M4.2.1
* **Vector Type:** Table
*   Table:
    | Rule ID | Description | Parameter Name | Parameter Value Range | Units | Data Source | Implicit/Explicit | Justification |
    | :------ | :---------- | :------------- | :---------- | :---: | :----------: | :----------------: | :------------: |
    | M_01 | Diffusion of Activator A | M_01 state | A | states {S, A, I} | Sect. 3.1 | Explicit | Directly derived from the provided transition matrix M. |
    | M_11 | Suppression of Activator A by Inhibitor I | M_11 state | I | states {S, A, I} | Sect. 3.1 | Explicit | Directly derived from the provided transition matrix M. |
    | M_z2, z=0,...,5 | Self-inhibition of Activator A | M_z2 state | I | states {S, A, I} | Sect. 3.1 | Explicit | Directly derived from the provided transition matrix M. |
    | M_z0, z=1,...,7 | Dissociation of Inhibitor I in absence of Activator | M_z0 state | S | states {S, A, I} | Sect. 3.1 | Explicit | Directly derived from the provided transition matrix M. |
    | M_zp, p>=4 | Upper-threshold self-inhibition of Activator | M_zp state | I | states {S, A, I} | Sect. 3.1 | Explicit | Directly derived from the provided transition matrix M. |

### **4.3 Global Order:**

*   **Vector ID:** M4.3
*   **Vector Type:** Order
    *   Content: The global order that emerges in the Spiral Rule CA includes: 1. Stationary Localizations (Eater and Block-like structures): These are stable patterns that remain static over time and act as 'eaters' of gliders or stable blocks. 2. Spiral Glider Guns: These are self-organizing sources of mobile localizations, emitting streams of gliders periodically. 3. Mobile Localizations (Gliders G34, G4, G5, G24, G43): These are propagating wave-fragments with stable shapes and velocities, acting as information carriers in the system. The overall emergent order is a dynamic yet stable configuration composed of interacting stationary and mobile patterns, forming a complex self-organized structure. (Fig. 2 visually depicts the quasi-stable configuration with these features).
    *   CT-GIN Mapping: Defines a `ConfigurationalNode`. `configurationalType`: Quasi-stationary state, `emergentStructures`: {Stationary Localizations, Spiral Glider Guns, Mobile Localizations (Gliders)}.
    * **Implicit/Explicit**: Explicit
        *  Justification: The emergent global order, consisting of stationary localizations and spiral glider-guns, and different types of gliders, is explicitly described in Sect 3.1 and is illustrated in Figure 2 and Figure 3. These are presented as typical outputs of the self-organizing dynamics starting from random initial conditions.

### **4.4 Predictability of Global Order:**

*   **Vector ID:** M4.4
*   **Vector Type:** Score
    *   Score: [7]
    *   Justification: The emergence of global order in the Spiral Rule CA is somewhat predictable in terms of the *types* of structures that will form (eaters, glider guns, gliders). The paper states, "Starting in a random initial configuration the automaton will evolve towards a quasi-stationary configuration, with typically two types of stationary localizations, and a spiral generator of mobile localizations, or gliders...".  However, the *exact spatial positions* and *number* of each structure that emerges in any given simulation from random initial conditions are not perfectly predictable. Statistical predictability is implied by the "typically" usage.  Qualitative assessment is Medium-High, as structural types are recurrent, but precise details of global patterns are not fully determined in advance –  influenced by randomness of initial configs. Score is based on the balance between predictable structural types and unpredictable precise arrangement.
    * **Implicit/Explicit**: Mixed
    *  Justification: The *types* of emergent structures (eaters, glider guns, gliders) are explicitly stated as typical. The *predictability score* and the degree of randomness in spatial arrangement are implicitly understood based on typical behavior description rather than quantified predictability metrics.

### **4.5. Local Interaction Rules (for Self-Organization)**
* **Vector ID:** M4.5
* **Vector Type:** Table
*   Table:
| Rule ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Source |
| :------ | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :-----: |
| Totalistic Rule | Cell state update depends on neighbor counts | Neighborhood Counts (σI, σA, σS) | 0-7 | count | Explicit | Rule is totalistic, matrix M indexes are neighbor counts | Sect. 3.1 |
| Matrix M Entries | Next state based on neighbor counts | Matrix Entry value (M_ij) | {S, A, I} | states | Explicit | Matrix M defines output states, matrix entries explicitly given. | Sect. 3.1 |

### **4.6. Globally Emergent Order and Order Parameters**
* **Vector ID:** M4.6
* **Vector Type:** Table
*   Table:
| Property ID | Description | Parameter | Value Range | Units | Implicit/Explicit | Justification | Protocol | Source |
| :---------- | :---------- | :-------- | :---------- | :---: | :----------------: | :------------: | :------: | :-----: |
| Glider Density | Number of gliders per unit area | Density | Varies | gliders/area | Implicit | Qualitative visual assessment of Fig. 2.  | Visual inspection of CA simulations | Fig. 2 |
| Eater Density | Number of eaters per unit area | Density | Varies | eaters/area | Implicit | Qualitative visual assessment of Fig. 2 | Visual inspection of CA simulations | Fig. 2 |
| Glider Emission Frequency | Rate of glider emission from gun | Frequency | ~1/6 | gliders/timestep per stream | Explicit (for G34 gun) |  Frequency of G34 emission is given | Fig. 2 |

### **4.7 Yoneda Embedding and Local-to-Global Mapping Fidelity**

*   **Vector ID:** M4.7
*   **Vector Type:** Table
*   Table:
    | Link Type | Description | Predictability | Yoneda Score | Metrics | Implicit/Explicit | Justification | Source |
    | :-------- | :---------- | :------------- | :----------- | :------ | :----------------: | :------------: | :-----: |
     | Local Rules -> Global Pattern | How well local Spiral Rule CA rules predict emergent patterns (eaters, glider guns) | Medium | 6 | Visual pattern analysis, qualitative recurrence of structures | Mixed | Structural types (eater, glider guns) are somewhat predictable (Medium predictability), but precise global configuration is less so. Score reflects this compromise | Fig. 2 |
    *   **Yoneda Embedding Fulfillment Score [0-10]:** [Score 6/10. Rubric for assessing score: 0 = No Emergent Order, 2 = Very weak order, Highly unpredictable, 4 = Weak order, Partially predictable in type but arrangement random, 6 = Moderate Order, Predictable types of structures but spatial positioning variable, 8 = Strong order, Predictable structure types and layout statistically predictable, 10 = Perfect order, Global order fully determined by local rules and initial conditions. For score 6, typical behaviors like eater and glider guns are reliably generated from random start, but precise location and quantity vary.]
    *   **Metrics:**  [Metrics used are primarily qualitative visual assessment of space-time diagrams (Fig. 2) and recurrence of structure "types" (eaters, glider guns, gliders)]
    *   **Justification:** Yoneda score of 6 is assigned because while the *types* of emergent structures (eaters, glider guns, gliders) are somewhat predictable and consistently arise from random initial conditions given the rules, the exact *spatial configuration* (positions, numbers) of these structures is not fully determined.  The local CA rules thus "embed" to a moderate degree into global patterns but with stochastic variation in arrangement.

## M5: Computation
*   **Vector ID:** M5
*   **Vector Type:** Computation

### **5.1 Embodied Computation Presence:**

*   **Vector ID:** M5.1
*   **Vector Type:** Binary
    *   Content: [Yes]
    *   Justification: Yes, computation is embodied in the collision-based system. Logical operations (AND, OR, NOT, XOR) and memory functions are implemented directly through the dynamics of mobile localizations (gliders) and their interactions with each other and stationary localizations (eaters, mirrors) within the cellular automaton and excitable media (BZ) substrates. Computation emerges from physical collisions and state changes of these localizations, not through an external computational controller separate from the material system.
    *    Implicit/Explicit: Explicit
        *  Justification: Explicitly stated throughout the paper that collision-based computing implements logical circuits and machines directly within the physical medium itself (CA, BZ, billiard balls etc), using localization interactions (collisions) for processing.

### **5.2 Computation Type:**

*   **Vector ID:** M5.2
*   **Vector Type:** Classification
    *   Content: [Hybrid] (Collision-based computing systems described are hybrid, exhibiting characteristics of both analog and digital computation. The representation of logical values by presence/absence of localizations suggests a digital aspect. However, the continuous nature of trajectories, velocities, and states of solitons in optical systems or wave-fragments in excitable media also points towards analog characteristics. The specific examples in CA often utilize discrete states, but the broader concept of collision-based computing is presented as versatile, encompassing both discrete (CA) and continuous (BZ, solitons) implementations.)
    *   CT-GIN Mapping: Defines the `ComputationNode` type. `computationType`: Hybrid (Analog/Digital), `paradigm`: Collision-based Computing.
    *    Implicit/Explicit: Mixed
    *    Justification:  The paper describes systems using digital CA and continuous media, showcasing aspects of both computation types, making "Hybrid" inferred classification most appropriate. The categorization relies on interpreting different implementation examples (CA digital, BZ/soliton potentially analog).

### **5.3 Computational Primitive:**

*   **Vector ID:** M5.3
*   **Vector Type:** Function
    *   Content: [Collision-based Logic Gate]. The most basic computational primitive is the collision-based logic gate, where logical operations are realized by the interaction of mobile localizations during collisions. Examples include: Interaction Gate (Fig. 1a) implementing AND/XY; Switch Gate (Fig. 1b) routing signal based on control; XOR gate (Fig. 7) using Eater E6 and glider interactions. The mathematical description is implicit: logical functions are implemented by designing collisions to achieve Boolean outcomes (TRUE/FALSE) based on input and output localizations.
    *   **Sub-Type (if applicable):** Logic Gate: AND, OR, NOT, XOR, routing, switching functions.
    *   CT-GIN Mapping: Defines the primary function of the `ComputationNode`. `computationalPrimitive`: Collision-based Logic Gate, `gateTypes`: {AND, OR, NOT, XOR, SWITCH, FANOUT, ERASE}.
    *   Implicit/Explicit: Mixed
    * Justification: "Collision-based Logic Gate" is explicitly described as the principle of computation. Specific gate types (AND, OR, NOT, XOR, SWITCH) are exemplified, making subtypes explicit.  Mathematical descriptions are however implicit and functional - logic described abstractly at boolean level without explicit formulas for transformations beyond verbal descriptions and illustrations.

### **5.4 Embodied Computational Units**
* **Vector ID:** M5.4
* **Vector Type:** Table
*   Table:
| Unit ID | Description | Processing Power | Energy/Operation | Freq/Resp. Time | Bit-Depth | Data