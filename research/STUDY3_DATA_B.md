# Study 3 Data — Group B: Handoff Chain
Paper: Graph Neural Networks for NLP: A Survey (arXiv 2106.06090)

---

## Handoff1 — T1 Test Context (after Part 1)

# Handoff - GNN-NLP Survey - Part 1

## Current Goal
Covered introduction, graph-based NLP background, and GNN foundations (Sections 1–3). Built understanding of why graphs are needed for NLP and the core mechanics of the four GNN filter types and two pooling types.

## Key Concepts Introduced
- Graph filtering (f_filter) → refines node embeddings using adjacency matrix A and prior embeddings H; does NOT change graph structure
- Graph pooling (f_pool) → takes graph + node embeddings, outputs SMALLER graph with fewer nodes; changes structure to produce graph-level embeddings
- GCN (Kipf & Welling 2016) → spectral-based filter; uses renormalization trick Ã=A+I; single shared parameter θ per layer; 1-hop neighborhood per layer
- GraphSAGE (Hamilton et al. 2017) → spatial-based; samples a FIXED random subset of neighbors rather than using full neighborhood
- GAT (Velickovic et al. 2018) → attention-based; dynamically assigns attention scores αij via LeakyReLU + softmax; intermediate layers concatenate multi-head outputs; final layer averages them
- GGNN (gated GNN) → recurrent-based; uses GRU to update node states; parameters shared across layers; considers edge type and direction via matrix A ∈ R^{dn×2dn}
- MPNN (Gilmer et al. 2017) → general spatial framework: message function fM + update function fU; runs K-step message passing for K-hop reach
- Flat pooling → max-pool or average-pool over node embeddings in one step; BiLSTM aggregation is more expressive but not permutation-invariant
- Hierarchical pooling → coarsens graph step-by-step via node sub-sampling (DiffPool) or supernodes; each pooling layer followed by graph filters

## Key Claims & Findings
- Traditional graph algorithms (random walk, LPA) lack unified learning framework and ignore node/edge features — GNNs address both limitations
- GCN approximates λmax≈2 and constrains θ=θ'_0=−θ'_1 to reduce overfitting and matrix operations
- GCN renormalization trick (In + D^{-1/2}AD^{-1/2} → D̃^{-1/2}ÃD̃^{-1/2}) prevents gradient explosion/vanishing
- BiLSTM flat pooling demonstrated better expressive power than max/avg pooling (Hamilton et al. 2017; Zhang et al. 2019)

## Open Questions / Limitations Noted
- Standard deep learning (CNNs, RNNs) not directly applicable to graph-structured data due to irregular structure and varying neighbor sizes
- Graph construction from raw NLP text sequences is a demanding prerequisite step not yet covered

## Completed Coverage
- Section 1: Introduction and survey taxonomy (4 axes: graph construction, representation learning, encoder-decoder models, applications)
- Section 2: Traditional graph algorithms for NLP (random walk, clustering, matching, label propagation) and their limitations
- Section 3: GNN foundations — graph filtering (spectral/spatial/attention/recurrent) and graph pooling (flat/hierarchical)

## Carry-Forward from Prior Parts
- (none — this is Part 1)

## Next Section Preview
- Part 2 covers Section 4: graph construction methods for NLP — both static (11 types: dependency, constituency, AMR, IE, discourse, KG, coreference, similarity, co-occurrence, topic, app-driven) and dynamic graph construction

## Background
→ read ~/Desktop/context-relay/research/STUDY3_CONTENT.md for full paper text

---

## Handoff2 (after Part 2)

# Handoff - GNN-NLP Survey - Part 2

## Current Goal
Covered Section 4 in full: static graph construction (11 types) and dynamic graph construction. Built understanding of how raw NLP text is converted to graph inputs for GNN processing.

## Key Concepts Introduced
- Static graph construction → built during preprocessing using parsing tools or rules; fixed before training; 11 types catalogued
- Dependency graph → nodes=words, edges=dependency relations (wi, reli,j, wj) + sequential edges preserving word order
- Constituency graph → nodes include non-terminal (NP, VP, S) and terminal (word) nodes; captures phrase-level structure unlike word-level dependency
- AMR graph → rooted, labeled, directed, acyclic graph (DAG); semantically equivalent sentences share the same AMR (e.g., "Paul described himself as a fighter" and "Paul's description of himself: a fighter")
- IE graph → extracts (subject, predicate, object) triples via OpenIE; collapses coreferent phrases into one node (contrast: coreference graph keeps them as linked nodes)
- Coreference graph → explicitly links phrases/words referring to the same entity; does NOT collapse nodes (unlike IE graph)
- Similarity graph → nodes at any granularity (entity/sentence/doc); edges weighted by cosine similarity or TF-IDF; sparsified by k-NN or ε-threshold
- Co-occurrence graph → edge weights = co-occurrence frequency or PMI within fixed sliding window
- Topic graph → nodes = documents ∪ latent topics (from LDA); undirected edges connect doc to its topics
- Dynamic graph construction → learns adjacency matrix jointly with downstream task end-to-end; no fixed preprocessing
- Graph sparsification → kNN-style (keep top-K neighbors per node) or ε-neighborhood (mask scores below threshold); also Frobenius norm regularization for implicit sparsity

## Key Claims & Findings
- Static graph limitation: graph construction and representation learning stages are disjoint — errors in construction cannot be corrected later
- Dynamic graph: combining learned implicit graph with intrinsic graph structure improves performance (Li et al. 2018; Chen et al. 2020f; Liu et al. 2021a)
- Dynamic graph pair-wise similarity has O(n²) complexity — scalability issue for large graphs; anchor-based approximation (Chen et al. 2020f) achieves linear complexity
- Three learning paradigms for dynamic graphs: (1) joint end-to-end, (2) layer-adaptive (different graph per GNN layer), (3) iterative (Chen et al. 2020f)
- Hybrid static graphs combine multiple graph types (e.g., dependency + coreference) by merging edge sets with relation-specific types

## Open Questions / Limitations Noted
- Static graph construction requires extensive domain expertise and is error-prone
- Dynamic graph construction for heterogeneous graphs is much less explored than for homogeneous graphs
- Dynamic graph construction does not clearly outperform static in all NLP applications

## Completed Coverage
- Section 4.1: Static graph construction (dependency, constituency, AMR, IE, discourse, KG, coreference, similarity, co-occurrence, topic, app-driven, hybrid)
- Section 4.2: Dynamic graph construction (similarity metric learning, sparsification, combining intrinsic+implicit, learning paradigms)

## Carry-Forward from Prior Parts
- GCN uses fixed 1-hop aggregation with shared θ; GAT uses dynamic attention weights αij — this distinction matters when choosing encoder for static vs. dynamic graphs
- GraphSAGE samples fixed-size neighbor set — relevant for scalability discussion in dynamic graph construction
- GGNN considers edge type and direction via relation-specific parameters — critical for multi-relational static graphs (AMR, KG)

## Next Section Preview
- Part 3 covers Section 5: graph representation learning for NLP — handling homogeneous graphs (static and dynamic), multi-relational graphs (R-GCN, R-GGNN, R-GAT), and heterogeneous graphs (Levi transform, meta-path, HAN, HGT)

## Background
→ read ~/Desktop/context-relay/research/STUDY3_CONTENT.md for full paper text

---

## Handoff3 — T2 Test Context (after Part 3)

# Handoff - GNN-NLP Survey - Part 3

## Current Goal
Covered Section 5: graph representation learning techniques for homogeneous, multi-relational, and heterogeneous graphs. Built understanding of how GNNs are adapted for the diverse graph structures arising in NLP.

## Key Concepts Introduced
- Homogeneous graph (|T|=1, |R|=1) → standard GCN/GAT/GraphSAGE apply directly; heterogeneous graphs must be converted first
- Bidirectional GNN → aggregates incoming (N⊣) and outgoing (N⊢) neighbors separately, then fuses; Xu et al. 2018b: concatenate; Chen et al. 2020g (BiGGNN): gated fusion via Fuse(a,b)=z⊙a+(1−z)⊙b; Ribeiro et al. 2019b: general framework applicable to any GNN
- Multi-relational graph (|T|=1, |R|>1) → converted from heterogeneous by adding "default", "reverse", and "self-loop" edge types
- R-GCN (Schlichtkrull et al. 2018) → applies relation-specific weight matrices W_r^(k) per edge type; over-parameterization addressed by basis decomposition (W_r = Σ a_rb V_b) or block-diagonal decomposition
- R-GGNN (Beck et al. 2018) → relational GGNN using relation-specific parameters W_r, b_r; captures long-distance relations; originally developed for graph-to-sequence
- R-GAT → two variants: Wang et al. 2020c adds relational attention heads; Wang et al. 2020h uses edge type embedding as absolute difference of mean source/target node vectors
- Gating mechanism → addresses over-smoothing in deep multi-relational GNNs; gates blend input features and aggregated features: h^(k)=σ(u^(k))⊙g^(k) + h^(k−1)⊙(1−g^(k−1))
- Levi graph transformation → converts each edge ei,j into a new node v_{ei,j}; resulting bipartite graph has |R'|=1; reduces AMR's 100+ edge types to homogeneous graph
- Graph transformer (structure-aware self-attention) → modifies attention score u_ij to incorporate edge embedding e_ij; Shaw et al. 2018: adds e_ij to key; Zhu et al. 2019/Xiao et al. 2019: also adds to value; Cai & Lam 2020: uses bidirectional path-based relation encoding
- HAN (Wang et al. 2019b) → meta-path-based heterogeneous GNN; two-level attention: node-level aggregation per meta-path + meta-path-level attention to weight different paths
- HGT (Hu et al. 2020) → graph transformer for heterogeneous graphs; uses meta-relations <τ(vi), φ(ei,j), τ(vj)>; adds relative temporal encoding for time-dependent graphs

## Key Claims & Findings
- Directed-GCN (Marcheggiani & Titov 2017) solves over-parameterization by sharing projection weights across edges of same direction, keeping only relation-specific biases
- Comp-GCN (Vashishth et al. 2019) generalizes R-GCN, Weighted-GCN, and Directed-GCN into one framework for joint node+relation learning
- MHGRN (Feng et al. 2020) extends R-GCN to pass messages over all K-hop paths directly, unifying GNNs and path-based models for heterogeneous graphs
- AMR graphs may contain more than 100 edge types — direct multi-relational GNN application is computationally burdensome; Levi transform is the standard solution

## Open Questions / Limitations Noted
- Over-smoothing problem when stacking multiple GNN layers; gating mechanism is one mitigation but not a complete solution
- Meta-path-based heterogeneous GNNs require additional domain expert knowledge to define meta-paths
- Graph transformer's self-attention treats graph as fully connected — may not fully exploit sparse graph topology, especially for multi-relational/heterogeneous inputs

## Completed Coverage
- Section 5.1: GNNs for homogeneous graphs (static edge-as-connectivity, dynamic, bidirectional)
- Section 5.2: GNNs for multi-relational graphs (R-GCN, R-GGNN, R-GAT, gating, graph transformer)
- Section 5.3: GNNs for heterogeneous graphs (Levi transform, HAN, MEIRec, HGAT, MHGRN, HGT)

## Carry-Forward from Prior Parts
- GCN: fixed 1-hop, shared θ; GAT: dynamic attention αij; GraphSAGE: fixed-size neighbor sample; GGNN: GRU-based, edge-type-aware — all serve as base models for multi-relational extensions
- Static graphs (AMR, dependency, KG) are the primary inputs to multi-relational GNNs
- Dynamic graph: O(n²) similarity computation limits scalability; intrinsic + implicit combination helps

## Next Section Preview
- Part 4 covers Section 6: GNN-based encoder-decoder models — Seq2Seq background, Graph2Seq (GNN encoder + RNN/Transformer decoder), Graph2Tree (tree decoders: BFS and DFS), Graph2Graph (graph transformation for IE and semantic parsing)

## Background
→ read ~/Desktop/context-relay/research/STUDY3_CONTENT.md for full paper text

---

## Handoff4 (after Part 4)

# Handoff - GNN-NLP Survey - Part 4

## Current Goal
Covered Section 6: GNN-based encoder-decoder models. Built understanding of Graph2Seq, Graph2Tree, and Graph2Graph frameworks, including their graph encoders, decoders, and key techniques.

## Key Concepts Introduced
- Seq2Seq limitations → fixed-dimensional intermediate vector is information bottleneck; exposure bias (training uses ground truth, inference uses predictions); linearizing graphs causes significant information loss
- Attention mechanism (Bahdanau 2015) → soft alignment between input and output sequences; coverage mechanism (Tu et al. 2016) penalizes repeatedly attending same positions via coverage vector ct = Σ a_{t'}
- Copying mechanism (Vinyals 2015; Gu 2016) → p_gen decides whether to generate from vocabulary or copy from input; Chen et al. 2020h extends to node-level copying for multi-token graph nodes
- Graph2Seq → GNN encoder (GCN/GGNN/GraphSAGE/GAT) + RNN or Transformer decoder; uses bidirectional message passing for directed graphs with separate parameters per edge direction
- Graph2Tree → handles structured tree outputs (math equations, semantic parsing); graph encoder + tree decoder; BFS decoder generates non-terminal nodes first, then recursively branches; DFS decoder generates root→left children→right children in sequence
- Graph2Tree attention → separate attention modules for word nodes (V1) and parse-tree nodes (V2): cv1=Σα_t(v)z_v, cv2=Σβ_t(v)z_v; final context = concat(cv1, cv2, st)
- Graph2Graph → transforms input graph to output graph; three subtypes: node transformation, edge transformation, node-edge-co-transformation; used for IE and semantic parsing
- Graph2Graph for IE → hierarchy graph encoder (word-level + sentence-level nodes with dependency/adjacent/interactive edges) + parallel decoder predicting co-reference links and entity relations jointly

## Key Claims & Findings
- Graph2Seq outperforms Seq2Seq in NMT, AMR-to-text, summarization, QG, KG-to-text, SQL-to-text, code summarization, and semantic parsing tasks
- Initializing node/edge embeddings with BiRNN before applying GNN encoder consistently helps (Bastings 2017; Marcheggiani 2018; many others); BERT+BiRNN and RoBERTa+BiRNN also explored
- Chen et al. 2020g: training Graph2Seq with hybrid loss (cross-entropy + RL) reduces exposure bias
- Tree2Seq (Eriguchi 2016) and Set2Seq (Vinyals 2016) are Seq2Seq extensions but cannot model arbitrary graph-structured data
- Li et al. 2020b (Graph2Tree): using separate attention for word nodes vs. parse-tree nodes outperforms single unified attention

## Open Questions / Limitations Noted
- Graph2Seq inherits Seq2Seq limitations (exposure bias, cross-entropy training discrepancy between train/inference)
- Graph2Seq also inherits GNN limitations: over-smoothing, multi-relational/heterogeneous graph modeling, scalability to large KGs
- Graph2Graph challenge: input and output graphs have different node concepts (e.g., input: word tokens; output: AMR logits); annotation costs limit dataset sizes

## Completed Coverage
- Section 6.1: Seq2Seq models (overview, attention, copying, coverage, exposure bias, scheduled sampling)
- Section 6.2: Graph2Seq models (graph encoders, node/edge embedding init, sequential decoding, special techniques)
- Section 6.3: Graph2Tree models (graph construction, GNN encoder, dual attention, BFS/DFS tree decoders)
- Section 6.4: Graph2Graph models (overview, IE application methodology)

## Carry-Forward from Prior Parts
- R-GCN, R-GGNN, R-GAT, Levi graph transform → all used as encoders in Graph2Seq/Graph2Tree for multi-relational inputs
- Bidirectional GNN (separate params for in/out/self edges) → standard practice in Graph2Seq encoders
- Dynamic graph construction (Chen et al. 2020g) → used inside Graph2Seq for QG task
- AMR graph (rooted DAG, 100+ edge types) → Levi transform + R-GGNN is standard encoding approach

## Next Section Preview
- Part 5 covers Section 7 first half: NLP applications — NMT, summarization, structural-data-to-text, question generation, MRC, KBQA, open-domain QA, community QA, dialog systems, text classification

## Background
→ read ~/Desktop/context-relay/research/STUDY3_CONTENT.md for full paper text

---

## Handoff5 (after Part 5)

# Handoff - GNN-NLP Survey - Part 5

## Current Goal
Covered Section 7 first half (NMT, summarization, QG, MRC, KBQA, open-domain QA, community QA, dialog, text classification). Built understanding of how GNN techniques are deployed in concrete NLP tasks.

## Key Concepts Introduced
- NMT graph construction patterns → dependency graph (Bastings 2017), SRL-based dependency (Marcheggiani 2018), AMR graph (Beck 2018; Song 2019), lattice graph for segmentation ambiguity (Xiao 2019), relative position graph (Shaw 2018), multi-modal graph (Yin 2020), hybrid document graph for long-dependency (Xu 2020b)
- Multi-hop MRC → constructs entity graph from passages; nodes = entity mentions; edges = exact-match, co-occurrence, coreference, SRL relations; hierarchical graphs also used (token→sentence→paragraph→document)
- Gating RGCN for MRC → most widely used multi-relational GNN in MRC; variant adds question-aware gating (Tang et al. 2020c)
- Conversational MRC dynamic graph → Chen et al. 2020e: dynamically builds passage graph per conversation turn using attention + kNN sparsification; end-to-end trainable
- KBQA MHGRN (Feng et al. 2020b) → passes messages over all paths of length ≤ K; concatenates graph representation with question+candidate answer text representation for scoring
- KBQA QA-GNN (Yasunaga et al. 2021) → constructs joint graph: QA context node connected to KG subgraph via rz,q and rz,a relation types; uses pre-trained LM for relevance scoring
- Semi-supervised text classification → single heterogeneous corpus graph with word + document nodes; edges = PMI (word-word) and TF-IDF (word-doc); Yao et al. 2019b: vanilla GCN with one-hot features already outperforms prior state-of-the-art
- Dynamic text classification graph → Chen et al. 2020f: word-per-node graph per document; Gaussian kernel for edge weights (Henaff 2015)
- Dialog state tracking → Chen et al. 2020a: three graph types (token schema graph, utterance graph, domain slot graph); recurrent attention GNN with GRU-like gating for state update
- Community QA → multi-modal graph (visual words from YOLO3 + text); APPNP-based hierarchical graph pooling for matching q/a pairs

## Key Claims & Findings
- Xu et al. 2020b (document-level NMT): hybrid graph with intra-sentential (sequential+dependency) and inter-sentential (lexical+coreference) edges addresses long-dependency problem; evaluated on WMT benchmarks with BLEU
- Yao et al. 2019b: GCN with one-hot node features alone outperforms previous state-of-the-art for text classification on 20NEWS, Ohsumed, MR datasets
- GNN-based MRC multi-tasking (predicting answer span + supporting facts + answer type) improves supervision signal quality (Qiu 2019; Fang 2020b; Chen 2020e)
- Ran et al. 2019 (numerical MRC): constructs graph with numbers as nodes and arithmetic relations as edges; DROP benchmark

## Open Questions / Limitations Noted
- Semi-supervised text classification with corpus-level graph cannot handle unseen documents (inductive setting requires per-document graphs)
- GNN-based dialog systems: dynamic graph construction via variational inference (Chen et al. 2018b) is promising but complex
- Open-domain QA: heterogeneous graph fusion of KB + unstructured documents still faces challenges with incomplete KB information and entity alignment errors

## Completed Coverage
- Section 7.1: NLG (NMT, summarization, structural-data-to-text, question generation)
- Section 7.2: MRC and QA (multi-hop MRC, conversational MRC, numerical MRC, KBQA, open-domain QA, community QA)
- Section 7.3: Dialog systems (dialog state tracking, response generation, utterance selection)
- Section 7.4: Text classification (semi-supervised and supervised, static and dynamic)

## Carry-Forward from Prior Parts
- R-GCN, R-GGNN, Levi graph, bidirectional GNN → deployed in NMT and summarization encoders as established techniques
- Graph2Seq architecture → used across NMT, summarization, QG, structural-data-to-text
- AMR graph construction + R-GGNN/graph transformer → dominant approach for AMR-to-text (Beck 2018; Cai & Lam 2020; Song 2018/2019)
- GGNN with edge-type-aware message passing → extended for directed graphs in QG (Chen 2020g, 2020h)

## Next Section Preview
- Part 6 covers Section 7 second half (text matching, topic modeling, sentiment, KG tasks, IE, parsing, reasoning, SRL) and Sections 8–9 (challenges, future directions, conclusion)

## Background
→ read ~/Desktop/context-relay/research/STUDY3_CONTENT.md for full paper text

---

## Handoff6 — T3 Test Context (after Part 6)

# Handoff - GNN-NLP Survey - Part 6

## Current Goal
Covered Section 7 second half (text matching, topic modeling, sentiment, KG completion/alignment, IE, parsing, reasoning, SRL), Section 8 (challenges and future directions), and Section 9 (conclusion). Survey is now fully read.

## Key Concepts Introduced
- KGC encoder-decoder → GNN encoder maps entities to embeddings; decoder is a scoring function; common scoring: DistMult (eTs Mreo, diagonal Mr), ComplEx, ConvE, Conv-TransE; trained with negative sampling; RGCN uses DistMult
- KGC benchmarks → FB15k-237, WN18RR, NELL-995; evaluated by MRR and Hits@N (n=1,3,10)
- KGA (Knowledge Graph Alignment) → finds corresponding entities across different KGs; RDGCN (Wu et al. 2019b): relation-aware dual-graph GCN; MuGNN (Cao et al. 2019c): KG self-attention + cross-KG attention; DBP15K benchmark (Chinese/Japanese/French→English)
- IE joint learning → GraphRel (Fu et al. 2019): 2-phase prediction of entities then relations; Luan et al. 2019: shared entity span representations refined by relation/coreference context; Sun et al. 2019b: entity detection then joint inference on entity+relation types
- SRL (Semantic Role Labeling) → predicate-argument structure recovery ("who did what to whom"); syntax-aware uses dependency/constituency graphs as input; Zhang et al. 2020f: probability-weighted edge graph from parser output to reduce error propagation
- Math word problem Graph2Tree (Li et al. 2020b) → first GNN application to MWP; GNN encodes input syntactic tree; BFS tree decoder generates equation in coarse-to-fine order
- Sentiment classification → majority use dependency tree graph; GCN (Zhang 2019b), GAT (Huang & Carley 2019), Graph Transformer (Tang 2020a), R-GAT (Wang 2020c) all applied; common embedding: GloVe+BiLSTM or BERT
- Graph4NLP library → open-source toolkit at github.com/graph4ai/graph4nlp; built on DGL + PyTorch; 4 layers: Data/Module/Model/Application; covers text classification, semantic parsing, NMT, KG completion, NLG

## Key Claims & Findings
- Dynamic graph construction: most existing approaches focus on homogeneous graphs; dynamic construction for heterogeneous graphs is underexplored; pair-wise similarity is O(n²) — Chen et al. 2020f anchor-based approximation achieves linear complexity
- Transformers are special GNNs operating on fully-connected dynamic graphs via self-attention — but cannot directly handle graph-structured inputs or exploit sparse topology
- Pre-training GNNs for NLP is largely unexplored (He et al. 2020; Sun et al. 2020a; Chen et al. 2020b are rare examples) compared to Transformer pre-training (BERT, GPT)
- Graph2Graph for AMR parsing: most methods represent either input or output as graph, not both jointly — joint graph-to-graph AMR parsing is an open future direction
- KGC trade-off: training all triples on full KG (efficient, Shang 2019) vs. training each triple on separate subgraph (expressive, Teru 2020; Xie 2020)
- Yao et al. 2019b finding survives to final section: one-hot GCN outperforms prior SotA on text classification (referenced in challenges as motivating semi-supervised GNN research)

## Open Questions / Limitations Noted
- Dynamic graph construction does not consistently outperform static graph construction — ceiling unclear
- Multi-relational GNNs face hard trade-off: over-parameterization (separate W_r per relation) vs. expressiveness loss (parameter sharing/decomposition)
- Graph transformers use attention-map as fully-directed graph — may not best exploit sparse graph topology, especially for multi-relational/heterogeneous inputs
- KG alignment: heterogeneous schemas across KGs, incomplete KG data, and limited seed alignments remain unsolved
- Graph2Graph: unpaired training examples, large vocabulary for AMR targets, and annotation cost limit progress
- Scalability of GNNs to large-scale KGs remains a challenge across KGC, KGA, and open-domain QA

## Completed Coverage
- Section 7.5–7.12: Text matching, topic modeling, sentiment classification, KGC, KGA, IE, parsing (syntax+semantics), reasoning (MWP, NLI, commonsense), SRL
- Section 7.13: Graph4NLP library and related tools (PyTorch Geometric, DGL, Dive into Graphs)
- Section 8: General challenges (dynamic graph construction, GNNs vs Transformers, Graph2Graph, KG in NLP, multi-relational GNNs)
- Section 9: Conclusion

## Carry-Forward from Prior Parts
- GCN fixed 1-hop shared θ; GAT dynamic attention; GraphSAGE fixed-size sample; GGNN GRU+edge-type-aware → base models underlying ALL application-specific GNNs throughout survey
- R-GCN basis decomposition → addresses over-parameterization by expressing W_r as linear combination of B shared bases
- AMR: rooted DAG, 100+ edge types → Levi transform standard; bidirectional path-based relation encoding for graph transformers
- Graph2Seq/Graph2Tree → dominant encoder-decoder frameworks for NLG tasks; BiRNN node init + GNN encoder + RNN/Transformer decoder is canonical architecture
- Dynamic graph O(n²) pair-wise similarity → scalability bottleneck identified in both Section 4 (construction) and Section 8 (challenges)

## Next Section Preview
- Survey complete. No further parts.

## Background
→ read ~/Desktop/context-relay/research/STUDY3_CONTENT.md for full paper text

---
Note: Handoff1 = T1 test context, Handoff3 = T2 test context, Handoff6 = T3 test context
