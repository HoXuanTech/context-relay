# Study 3 Content: GNN-NLP Survey Sections + Ground Truth

## Paper Info
Title: Graph Neural Networks for Natural Language Processing: A Survey
Authors: Lingfei Wu, Yu Chen, Kai Shen, Xiaojie Guo, Hanning Gao, Shucheng Li, Jian Pei, Bo Long
URL: https://arxiv.org/abs/2106.06090
Published: Foundations and Trends in Machine Learning (arXiv:2106.06090v2, Oct 2022)
Total words extracted (paper body, excl. references): ~45,870

---

## Part 1 — Introduction, Graph Basics, and GNN Foundations (Sections 1–3, pp. 1–13)


GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
Graph Neural Networks for Natural Language Processing:
A Survey
Lingfei Wu∗ LWU@EMAIL .WM.EDU
Pinterest, USA
Yu Chen∗ HUGOCHAN 2013@ GMAIL .COM
Rensselaer Polytechnic Institute, USA
Kai Shen† SHENKAI @ZJU .EDU .CN
Zhejiang University, China
Xiaojie Guo XIAOJIE .GUO @JD.COM
IBM T.J. Watson Research Center, USA
Hanning Gao GHNQWERTY @GMAIL .COM
Central China Normal University, China
Shucheng Li‡ SHUCHENGLI @SMAIL .NJU .EDU .CN
Nanjing University, China
Jian Pei JPEI @CS.SFU .CA
Simon Fraser University, Canada
Bo Long BO.LONG @JD.COM
JD.COM, China
Abstract
Deep learning has become the dominant approach in coping with various tasks in Natural Language
Processing (NLP). Although text inputs are typically represented as a sequence of tokens, there is
a rich variety of NLP problems that can be best expressed with a graph structure. As a result, there
is a surge of interests in developing new deep learning techniques on graphs for a large number
of NLP tasks. In this survey, we present a comprehensive overview on Graph Neural Networks
(GNNs) for Natural Language Processing. We propose a new taxonomy of GNNs for NLP, which
systematically organizes existing research of GNNs for NLP along three axes: graph construction,
graph representation learning, and graph based encoder-decoder models. We further introduce
a large number of NLP applications that are exploiting the power of GNNs and summarize the
corresponding benchmark datasets, evaluation metrics, and open-source codes. Finally, we discuss
various outstanding challenges for making the full use of GNNs for NLP as well as future research
directions. To the best of our knowledge, this is the ﬁrst comprehensive overview of Graph Neural
Networks for Natural Language Processing.
Keywords: Graph Neural Networks, Natural Language Processing, Deep Learning on Graphs
1. Introduction
Deep learning has become the dominant approach in coping with various tasks in Natural Language
Processing (NLP) today, especially when operated on large-scale text corpora. Conventionally, text
*. Both authors contributed equally to this research.
†. This research is done when Kai Shen is an intern at JD.COM.
‡. Shucheng Li is also with National Key Lab for Novel Software Technology, Nanjing University.
1
arXiv:2106.06090v2  [cs.CL]  20 Oct 2022





LINGFEI WU AND YU CHEN , ET AL .
sequences are considered as a bag of tokens such as BoW and TF-IDF in NLP tasks. With recent
success of Word Embeddings techniques (Mikolov et al., 2013; Pennington et al., 2014), sentences
are typically represented as a sequence of tokens in NLP tasks. Hence, popular deep learning
techniques such as recurrent neural networks (Schuster and Paliwal, 1997) and convolutional neural
networks (Krizhevsky et al., 2012) have been widely applied for modeling text sequence.
However, there is a rich variety of NLP problems that can be best expressed with a graph struc-
ture. For instance, the sentence structural information in text sequence (i.e. syntactic parsing trees
like dependency and constituency parsing trees) can be exploited to augment original sequence data
by incorporating the task-speciﬁc knowledge. Similarly, the semantic information in sequence data
(i.e. semantic parsing graphs like Abstract Meaning Representation graphs and Information Extrac-
tion graphs) can be leveraged to enhance original sequence data as well. Therefore, these graph-
structured data can encode complicated pairwise relationships between entity tokens for learning
more informative representations.
Unfortunately, deep learning techniques that were disruptive for Euclidean data (e.g, images)
or sequence data (e.g, text) are not immediately applicable to graph-structured data, due to the
complexity of graph data such as irregular structure and varying size of node neighbors. As a result,
this gap has driven a tide in research for deep learning on graphs, especially in development of
graph neural networks (GNNs) (Wu et al., 2022; Kipf and Welling, 2016; Defferrard et al., 2016;
Hamilton et al., 2017a).
This wave of research at the intersection of deep learning on graphs and NLP has inﬂuenced a
variety of NLP tasks (Liu and Wu, 2022). There has seen a surge of interests in applying and devel-
oping different GNNs variants and achieved considerable success in many NLP tasks, ranging from
classiﬁcation tasks like sentence classiﬁcation (Henaff et al., 2015; Huang and Carley, 2019), se-
mantic role labeling (Luo and Zhao, 2020; Gui et al., 2019), and relation extraction (Qu et al., 2020;
Sahu et al., 2019), to generation tasks like machine translation (Bastings et al., 2017; Beck et al.,
2018a), question generation (Pan et al., 2020; Sachan et al., 2020), and summarization (Fernandes
et al., 2019; Yasunaga et al., 2017). Despite the successes these existing research has achieved, deep
learning on graphs for NLP still encounters many challenges, namely,
• Automatically transforming original text sequence data into highly graph-structured data.
Such challenge is profound in NLP since most of the NLP tasks involving using the text
sequences as the original inputs. Automatic graph construction from the text sequence to uti-
lize the underlying structural information is a crucial step in utilizing graph neural networks
for NLP problems.
• Properly determining graph representation learning techniques. It is critical to come up with
specially-designed GNNs to learn the unique characteristics of different graph-structures data
such as undirected, directed, multi-relational and heterogeneous graphs.
• Effectively modeling complex data. Such challenge is important since many NLP tasks in-
volve learning the mapping between the graph-based inputs and other highly structured output
data such as sequences, trees, as well as graph data with multi-types in both nodes and edges.
In this survey, we will present for the ﬁrst time a comprehensive overview ofGraph Neural Net-
works for Natural Language Processing. Our survey is timely for both Machine Learning and NLP
communities, which covers relevant and interesting topics, including automatic graph construction
2





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
Figure 1: The taxonomy, which systematically organizes GNNs for NLP along four axes: graph
construction, graph representation learning, encoder-decoder models, and the applications.
for NLP, graph representation learning for NLP, various advanced GNNs-based encoder-decoder
models (i.e. graph2seq, graph2tree, and graph2graph) for NLP, and the applications of GNNs in
various NLP tasks. We highlight our main contributions as follows:
• We propose a new taxonomy of GNNs for NLP, which systematically organizes existing re-
search of GNNs for NLP along four axes: graph construction, graph representation learning,
and graph based encoder-decoder models.
• We present the most comprehensive overview of the state-of-the-art GNNs-based approaches
for various NLP tasks. We provide detailed descriptions and necessary comparisons on vari-
ous graph construction approaches based on the domain knowledge and semantic space, graph
representation learning approaches for various categories of graph-structures data, GNNs-
3





LINGFEI WU AND YU CHEN , ET AL .
based encoder-decoder models given different combinations of inputs and output data types.
• We introduce a large number of NLP applications that are exploiting the power of GNNs,
including how they handle these NLP tasks along three key components (i.e., graph con-
struction, graph representation learning, and embedding initialization), as well as providing
corresponding benchmark datasets, evaluation metrics, and open-source codes.
• We outline various outstanding challenges for making the full use of GNNs for NLP and
provides discussions and suggestions for fruitful and unexplored research directions.
The rest of the survey is structured as follows. Section 2 reviews the NLP problems from a
graph perspective, and then brieﬂy introduces some representative traditional graph-based methods
for solving NLP problems. Section 3 elaborates basic foundations and methodologies for graph neu-
ral networks, which are a class of modern neural networks that directly operate on graph-structured
data. We also provide a list of notations used throughout this survey. Section 4 focuses on introduc-
ing two major graph construction approaches, namely static graph construction and dynamic graph
construction for constructing graph structured inputs in various NLP tasks. Section 5 discusses var-
ious graph representation learning techniques that are directly operated on the constructed graphs
for various NLP tasks. Section 6 ﬁrst introduces the typical Seq2Seq models, and then discusses
two typical graph-based encoder-decoder models for NLP tasks (i.e., graph-to-tree and graph-to-
graph models). Section 7 discusses 12 typical NLP applications using GNNs bu providing the
summary of all the applications with their sub-tasks, evaluation metrics and open-source codes.
Section 8 discusses various general challenges of GNNs for NLP and pinpoints the future research
directions. Finally, Section 9 summarizes the paper. The taxonomy, which systematically orga-
nizes GNN for NLP approaches along four axes: graph construction, graph representation learning,
encoder-decoder models, and the applications is illustrated in Fig.1.
2. Graph Based Algorithms for NLP
In this section, we will ﬁrst review the NLP problems from a graph perspective, and then brieﬂy
introduce some representative traditional graph-based methods for solving NLP problems.
2.1 Natural Language Processing: A Graph Perspective
The way we represent natural language reﬂects our particular perspective on it, and has a fundamen-
tal inﬂuence on the way we process and understand it. In general, there are three different ways of
representing natural language. The most simpliﬁed way is to represent natural language as a bag of
tokens. This view of natural language completely ignores the speciﬁc positions of tokens appearing
in text, and only considers how many times a unique token appears in text. If one randomly shufﬂes
a given text, the meaning of the text does not change at all from this perspective. The most repre-
sentative NLP technique which takes this view is topic modeling (Blei et al., 2003) which aims to
model each input text as a mixture of topics where each topic can be further modeled as a mixture
of words.
A more natural way is to represent natural language as a sequence of tokens. This is how human
beings normally speak and write natural language. Compared to the above bag perspective, this
view of natural language is able to capture richer information of text, e.g., which two tokens are
4





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
consecutive and how many times a word pair co-occurs in local context. The most representative
NLP techniques which take this view include the linear-chain CRF (Lafferty et al., 2001) which
implements sequential dependencies in the predictions, and the word2vec (Mikolov et al., 2013)
which learns word embeddings by predicting the context words of a target word.
The third way is to represent natural language as a graph. Graphs are ubiquitous in NLP. While
it is probably most apparent to regard text as sequential data, in the NLP community, there is a long
history of representing text as various kinds of graphs. Common graph representations of text or
world knowledge include dependency graphs, constituency graphs, AMR graphs, IE graphs, lexical
networks, and knowledge graphs. Besides, one can also construct a text graph containing multiple
hierarchies of elements such as document, passage, sentence and word. In comparison with the
above two perspectives, this view of natural language is able to capture richer relationships among
text elements. As we will introduce in next section, many traditional graph-based methods (e.g., ran-
dom walk, label propagation) have been successfully applied to challenging NLP problems includ-
ing word-sense disambiguation, name disambiguation, co-reference resolution, sentiment analysis,
and text clustering.
2.2 Graph Based Methods for Natural Language Processing
In this previous subsection, we have discussed that many NLP problems can be naturally translated
into graph-based problems. In this subsection, we will introduce various classical graph-based
algorithms that have been successfully applied to NLP applications. Speciﬁcally, we will ﬁrst brieﬂy
illustrate some representative graph-based algorithms and their applications in the NLP ﬁeld. And
then we further discuss their connections to GNNs. For a comprehensive coverage of traditional
graph-based algorithms for NLP, we refer the readers to (Mihalcea and Radev, 2011).
2.2.1 R ANDOM WALK ALGORITHMS
Approach Random walk is a class of graph-based algorithms that produce random paths in a
graph. In order to do a random walk, one can start at any node in a graph, and repeatedly choose
to visit a random neighboring node at each time based on certain transition probabilities. All the
visited nodes in a random walk then form a random path. After a random walk converges, one can
obtain a stationary distribution over all the nodes in a graph, which can be used to either select
the most salient node in a graph with high structural importance by ranking the probability scores
or measure the relatedness of two graphs by computing the similarity between two random walk
distributions.
Applications Random walk algorithms have been applied in various NLP applications includ-
ing measures of semantic similarity of texts (Ramage et al., 2009) and semantic distance on se-
mantic networks (Hughes and Ramage, 2007), word-sense disambiguation (Mihalcea, 2005; Tarau
et al., 2005), name disambiguation (Minkov et al., 2006), query expansion (Collins-Thompson and
Callan, 2005), keyword extraction (Mihalcea and Tarau, 2004), and cross-language information re-
trieval (Monz and Dorr, 2005). For example, given a semantic network and a word pair, Hughes and
Ramage (2007) computed a word-speciﬁc stationary distribution using a random walk algorithm,
and measured the distance between two words as the similarity between the random walk distribu-
tions on this graph, biased on each input word in a given word pair. To solve a name disambiguation
task on email data, Minkov et al. (2006) built a graph of email-speciﬁc items (e.g., sender, receiver
and subject) from a corpus of emails, and proposed a “lazy” topic-sensitive random walk algorithm
5





LINGFEI WU AND YU CHEN , ET AL .
which introduces a probability that the random walk would stop at a given node. Given an email
graph and an ambiguous name appearing in an input email, a random walk is performed biased
toward the text of the given email, and the name is resolved to the correct reference by choosing
the person node that has the highest score in the stationary distribution after convergence. To solve
the keyword extraction task, Mihalcea and Tarau (2004) proposed to perform a random walk on
a co-occurrence graph of words, and rank the importance of the words in the text based on their
probability scores in the stationary distribution.
2.2.2 G RAPH CLUSTERING ALGORITHMS
Approach Common graph clustering algorithms include spectral clustering, random walk cluster-
ing and min-cut clustering. Spectral clustering algorithms make use of the spectrum (eigenvalues) of
the Laplacian matrix of the graph to perform dimensionality reduction before conducting clustering
using existing algorithms like K-means. Random walk clustering algorithms operate by conducting
a t-step random walk on the graph, as a result, each node is represented as a probability vector
indicating the t-step generation probabilities to all of the other nodes in the graph. Any clustering
algorithm can be applied on the generation-link vectors. Note that for graph clustering purposes, a
small value of t is more preferred because we are more interested in capturing the local structural
information instead of the global structural information (encoded by the stationary distribution after
a random walk converges). The min-cut algorithms can also be used to partition the graph into
clusters.
Applications Graph clustering algorithms have been successfully applied to solve the text clus-
tering task. For instance, Erkan (2006) proposed to use the n-dim probabilistic distribution derived
from a t-step random walk on a directed generation graph (containing n document nodes) as the
vector representation of each document in a corpus. Then these document representations can be
consumed by a graph clustering algorithm to generate document clusters. Note that the generation
graph is constructed by computing the generation probability of each ordered document pair in the
corpus following the language-model approach proposed by Ponte and Croft (1998).
2.2.3 G RAPH MATCHING ALGORITHMS
Approach Graph matching algorithms aim to compute the similarity between two graphs. Among
them, Graph Edit Distance is the most commonly used method to measure the dissimilarity of two
graphs. It computes the distance as the number of changes (i.e., add, delete, substitute) needed to
transform one graph into the other. Then the dissimilarity score can be converted into the similarity
score.
Applications Graph matching algorithms have applications in the textual entailment task that aims
at deciding whether a given sentence can be inferred from text. For example, Haghighi et al. (2005)
assumed that a hypothesis is entailed from the text when the cost of matching the hypothesis graph
to the text graph is low, and thus applied a graph matching algorithm to solve the problem.
2.2.4 L ABEL PROPAGATION ALGORITHMS
Approach Label propagation algorithms (LPAs) is a class of semi-supervised graph-based algo-
rithms that propagate labels from labeled data points to previously unlabeled data points. Basically,
LPAs operate by propagating and aggregating labels iteratively across the graph. At each iteration,
6





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
each node changes its label based on the labels that its neighboring nodes possess. As a result, the
label information diffuses through the graph.
Applications LPA have been widely used in the network science literature for discovering com-
munity structures in complex networks. In the literature of NLP, LPA have been successfully ap-
plied in word-sense disambiguation (Niu et al., 2005) and sentiment analysis (Goldberg and Zhu,
2006). These applications usually focus on the semi-supervised learning setting where labeled data
is scarce, and leverage the LPA algorithm for propagating labels from limited labeled examples to a
large amount of similar unlabeled examples with the assumption that similar examples should have
similar labels.
2.2.5 L IMITATIONS AND CONNECTIONS TO GNN S
Although traditional graph-based algorithms have been successfully applied in many NLP tasks,
they have several limitations. First of all, they have limited expressive power. They mostly focus on
capturing the structural information of graphs but do not consider the node and edge features which
are also very important for many NLP applications. Secondly, there is not a uniﬁed learning frame-
work for traditional graph-based algorithms. Different graph-based algorithms have very different
properties and settings, and are only suitable to some speciﬁc use cases.
The above limitations of traditional graph-based algorithms call for a uniﬁed graph-based learn-
ing framework with strong expressive power on modeling both the graph structures and node/edge
properties. Recently, GNNs have gained increasing attention as a special class of neural networks
which can model arbitrary graph-structured data. Most GNN variants can be regarded as a mes-
sage passing based learning framework. Unlike traditional message passing based algorithms like
LPA which operates by propagating labels across a graph, GNNs typically operate by transforming,
propagating and aggregating nodes/edge features through several neural layers so as to learn bet-
ter graph representations. As a general graph-based learning framework, GNNs can be applied to
various graph-related tasks such as node classiﬁcation, link prediction and graph classiﬁcation.
3. Graph Neural Networks
In the previous chapter, we have illustrated various conventional graph-based methods for different
NLP applications. In this chapter, we will elaborate basic foundations and methodologies for graph
neural networks (GNNs) which are a class of modern neural networks which directly operate on
graph-structured data (Wu et al., 2022). To facilitate the description of the technologies, we list all
the notations used throughout this survey in Table 1, which includes variables and operations in the
domain of both the graph neural networks and NLP.
Table 1: Notation
Graph Basics
A graph G
Edge set E
Vertex (node) set V
7





LINGFEI WU AND YU CHEN , ET AL .
The number of vertexes (nodes) n
The number of edges m
A single vertex(node) vi∈V vi
A single edge ei,j(connecting vertex vi and vertex vj∈E ei,j
The neighbours of a vertex (node) vi N(vi)
Adjacent matrix of a graph A
Laplacian matrix L
Diagonal degree matrix D
The initial attributes of vertex vi∈V xi
The initial attributes of edge ei,j∈E ri,j
The embedding of vertex vi∈V hi
The embedding of edge ei,j∈E ei,j
NLP Basics
V ocabulary V
Source language s
Target language t
Corpus of words/aligned sentences used for training C
The ith word in corpus C wi
The embedding of word wi wi
The embedding vector’s dimensionality d
The number of words n
The ith document in source(target) language docs
i (doct
i)
Representation of document docs
i (doct
i) ds
i (dt
i)
The ith paragraph in source(target) language paras
i (parat
i)
Representation of paragraph paras
i (parat
i) ps
i (pt
i)
The ith sentence in source(target) language sents
i (sentt
i)
Representation of sentence sents
i (sentt
i) ss
i (st
i)
3.1 Foundations
Graph neural networks are essentially graph representation learning models and can be applied to
node-focused tasks and graph-focused tasks. GNNs learn embeddings for each node in the graph
and aggregate the node embeddings to produce the graph embeddings. Generally, the learning
process of node embeddings utilizes graph structure and input node embeddings, which can be
summarized as:
h(l)
i = fﬁlter(A, H(l−1)) (1)
where A∈ Rn×n is the adjacency matrix of the graph, H(l−1) ={h(l−1)
1 , h(l−1)
2 , ..., h(l−1)
n }∈
Rn×d denotes the input node embeddings at the l− 1-th GNN layer, and H(l) is the updated node
embeddings. d is the dimension of h(l−1)
i . We refer to the process depicted in Eq.(1) as graph
ﬁltering and fﬁlter(·,·) is named as a graph ﬁlter. The speciﬁc models then differ only in how
8





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
fﬁlter(·,·) is chosen and parameterized. Graph ﬁltering does not change the structure of graph, but
reﬁnes the node embeddings. Graph ﬁltering layers are stacked to L layers to generate ﬁnal node
embeddings.
Since graph ﬁltering does not change the graph structure, pooling operations are introduced
to aggregate node embeddings to generate graph-level embeddings inspired by CNNs. In GNN
models, the graph pooling takes a graph and its node embeddings as inputs and then generates a
smaller graph with fewer nodes and its corresponding new node embeddings. The graph pooling
operation can be summarized as follows:
A′, H′ = fpool(A, H) (2)
where fpool(·,·) A∈ Rn×n and A′∈ Rn′×n′
are the adjacency matrices before and after graph
pooling. H∈ Rn×d and H′∈ Rn′×d′
are the node embeddings before and after graph pooling. n′
is set to be 1 in most cases to get the embedding for the entire graph.
3.2 Methodologies
3.2.1 G RAPH FILTERING
There exists a variety of implementations of graph ﬁlter f in Eq.(1), which could be roughly cat-
egorized into spectral-based graph ﬁlters, spatial-based graph ﬁlters, attention-based graph ﬁlters
and recurrent-based graph ﬁlters. Conceptually, the spectral-based graph ﬁlters are based on spec-
tral graph theory while the spatial-based methods compute a node embedding using its spatially
close neighbor nodes on the graph. Some spectral-based graph ﬁlters can be converted to spatial-
based graph ﬁlters. The attention-based graph ﬁlters are inspired by the self-attention mechanism
(Vaswani et al., 2017) to assign different attention weights to different neighbor nodes. Recurrent-
based graph ﬁlters introduce gating mechanism, and the model parameters are shared across differ-
ent GNN layers. Next, we will explain these four types of graph ﬁlters in detail by introducing some
of their representative GNN models.
Spectral-based Graph Filters Inspired by graph signal processing, Defferrard et al. proposed a
spectral graph theoretical formulation of CNNs, which generalizes CNNs to graphs and provides the
same linear computational complexity and constant learning complexity as classical CNNs. A more
typical example of spectral-based graph ﬁlters is Graph Convolutional Networks (GCN) (Kipf and
Welling, 2016). Spectral convolution on graphs is deﬁned as the multiplication of a signalxi∈ Rn
(a scalar for node vi) with the ﬁlter fﬁlter = diag(θ) parameterized by θ ∈ Rn in the Fourier
domain:
fﬁlter∗ xi = Uf(Λ)UTxi (3)
where U is the matrix of eigenvectors of the normalized graph LaplacianL = In− D− 1
2 AD− 1
2 . In
is the identity matrix, D is the degree matrix and Λ is the eigenvalues of L.
However, the computation of the full eigen-decomposition is prohibitively expensive. To solve
this problem, Defferrard et al. (2016) uses a truncated expansion in terms of Chebyshev polynomials
Tp(x) up to Pth-order to approximate gθ(Λ). Eq. (3) can be represented as follows:
f′
ﬁlter∗ xi≈
P∑
p=0
θ′
pTp(˜L)xi (4)
9





LINGFEI WU AND YU CHEN , ET AL .
where ˜L = 2
λmax L− In. λmax is the largest eigenvalue of L. θ′
k∈ RP is a vector of Chebyshev
coefﬁcients. The Chebyshev polynomials can be deﬁned recursively: Tk(xi) = 2 xiTk−1(xi)−
Tk−2(xi), with T0(xi) = 1 and T1(xi) = xi. Eq.(4) is a Kth-order polynomial in the Laplacian,
which shows that every central node depends only on nodes in the P -hop range.
Therefore, a neural network model based on graph convolution can stack multiple convolutional
layers using Eq. (4). By limiting the layer-wise convolution operation to P = 1 and stacking
multiple convolutional layers, Kipf and Welling (2016) proposed a multi-layer Graph Convolutional
Network (GCN). It further approximates λmax≈ 2 and Eq. (4) is simpliﬁed to:
f′
ﬁlter∗ h(l)
i ≈ θ′
0h(l)
i + θ′
1(L− In)h(l)
i = θ′
0h(l)
i − θ′
1D− 1
2 AD− 1
2h(l)
i (5)
with two free parametersθ′
0 and θ′
1. To alleviate the problem of overﬁtting and minimize the number
of operations (such as matrix multiplications), it is beneﬁcial to constrain the number of parameters
by setting a single parameter θ = θ′
0 =−θ′
1:
fﬁlter∗ h(l)
i ≈ θ(In + D− 1
2 AD− 1
2 )h(l)
i (6)
Repeat application of this operator may cause numerical instability and explosion/vanishing gra-
dients, Kipf and Welling (2016) proposed to use a renormalization trick: In + D− 1
2 AD− 1
2 →
˜D− 1
2 ˜A ˜D− 1
2 , with ˜A = A + In and ˜Dii =∑
j ˜Aij. Finally, the deﬁnition can be generalized with a
signal H∈ Rn×d with d input channels (i.e. a d-dimensional feature vector for each node) and F
ﬁlters or feature maps as follows:
H(l) = σ( ˜D− 1
2 ˜A ˜D− 1
2H(l−1)W(l−1)) (7)
Here, W(l−1) is a layer-speciﬁc trainable weight matrix and σ(·) denotes an activation function.
H(l)∈ Rn×d is the activated node embeddings at (l− 1)-th layer.
Spatial-based Graph Filters Analogous to the convolutional operation of a conventional CNN,
spatial-based graph ﬁlters operate the graph convolutions based on a node’s spatial relations. The
spatial-based graph ﬁlters derive the updated representation for the target node via convolving its
representation with its neighbors’ representations. On the other hand, spatial-based graph ﬁlters
hold the idea of information propagation, namely, message passing. The spatial-based graph con-
volutional operation essentially propagates node information as messages along the edges. Here
we introduce two typical GNNs based on spatial-based graph ﬁlters are Message Passing Neural
Network (MPNN) (Gilmer et al., 2017) and GraphSage (Hamilton et al., 2017a).
MPNN (Gilmer et al., 2017) proposes a general framework of spatial-based graph ﬁlters fﬁlter
which is a composite function consisting of fU and fM. It treats graph convolutions as a message
passing process in which information can be passed from one node to another along the edges
directly. MPNN runs K-step message passing iterations to let information propagate further to K-
hop neighboring nodes. The message passing function, namely the spatial-based graph ﬁlter, on the
target node vi is deﬁned as
h(l)
i = fﬁlter(A, H(l−1)) = fU(h(l−1)
i ,
∑
vj∈N(vi)
fM(h(l−1)
i , h(l−1)
j , ei,j)), (8)
where h(0)
i = xi, fU(·) and fM(·) are the update and message aggregate functions with learnable
parameters, respectively. After deriving the hidden representations of each node, h(L)
i (L is the
10





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
number of graph convolution layers) can be passed to an output layer to perform node-level predic-
tion tasks or to a readout function to perform graph-level prediction tasks. MPNN is very general to
include many existing GNNs by applying different functions of fU(·) and fM(·).
Considering that the number of neighbors of a node can vary from one to a thousand or even
more, it is inefﬁcient to take the full size of a node’s neighborhood in a giant graph with thousands
of millions of nodes. GraphSage (Hamilton et al., 2017a) adopts sampling to obtain a ﬁxed number
of neighbors for each node as
fﬁlter(A, H(l−1)) = σ(W(l)· fM(h(l−1)
i ,{h(l−1)
j ,∀vj∈ N(vi)})), (9)
where N(vi) is a random sample of the neighboring nodes of nodevi. The aggregation function can
be any functions that are invariant to the permutations of node orderings such as mean, sum or max
operations.
Attention-based Graph Filters The original versions of GNNs take edge connections of the in-
put graph as ﬁxed, and do not dynamically adjust the connectivity information during the graph
learning process. Motivated by the above observation, and inspired by the successful applications
of multi-head attention mechanism in the Transformer model (Vaswani et al., 2017; Velickovic et al.,
2018) proposed the Graph Attention Network (GAT) by introducing the multi-head attention mech-
anism to the GNN architecture which is able to dynamically learn the weights (i.e., attention scores)
on the edges when performing message passing. More speciﬁcally, when aggregating embeddings
from neighboring nodes for each target node in the graph, the semantic similarity between the target
node and each neighboring node will be considered by the multi-head attention mechanism, and
important neighboring nodes will be assigned higher attention scores when performing the neigh-
borhood aggregation. For the l-th layer, GAT thus uses the following formulation of the attention
mechanism,
αij =
exp(LeakyReLU(⃗ u(l)T [ ⃗W (l)h(l−1)
i || ⃗W (l)h(l−1)
j ]))
∑
vk∈N(vi) exp(LeakyReLU(⃗ u(l)T [ ⃗W (l)h(l−1)
i || ⃗W (l)h(l−1)
k ]))
(10)
where ⃗ u(l) and ⃗W (l) are the weight vector and weight matrix at l-th layer, respectively, and || is
the vector concatenation operation. Note that N(vi) is the 1-hop neighborhood of vi including
itself. After obtaining the attention scores αij for each pair of nodes vi and vj, the updated node
embeddings can be computed as a linear combination of the input node features followed by some
nonlinearity σ, formulated as,
h(l)
i = fﬁlter(A, H(l−1)) = σ(
∑
vj∈N(vi)
αij ⃗W (l)h(l−1)
j ) (11)
In order to stabilize the learning process of the above self-attention, inspired by Vaswani et al.
(2017), multiple independent self-attention mechanisms are employed and their outputs are con-
catenated to produce the following node embedding:
fﬁlter(A, H(l−1)) =||K
k=1σ(
∑
vj∈N(vi)
αk
ij ⃗W (l)
k h(l−1)
j ), (12)
11





LINGFEI WU AND YU CHEN , ET AL .
while the ﬁnal GAT layer (i.e., theL-th layer for a GNNs with L layers) employs averaging instead
of concatenation to combine multi-head attention outputs.
fﬁlter(A, H(L−1)) = σ( 1
K
K∑
k=1
∑
vj∈N(vi)
αk
ij ⃗W (L)
k h(L−1)
j ) (13)
Recurrent-based Graph Filters A typical example of recurrent-based graph ﬁlters is the Gated
Graph Neural Networks (GGNN)-ﬁlter. The biggest modiﬁcation from typical GNNs to GGNNs is
the use of Gated Recurrent Units (GRU) (Cho et al., 2014). Analogous to RNN, GGNN unfolds the
recurrence in a ﬁxed T time steps and uses back propagation through time to calculate the gradients.
The GGNN-ﬁlter also takes the edge type and edge direction into consideration. To this end, ei,j
denotes the directed edge from node vi to node vj and the edge type of ei,j is ti,j. The propagation
process of recurrent-based ﬁlterfﬁlter in GGNN can be summarized as follows:
h(0)
i = [xT
i , 0]T (14)
a(l)
i = AT
i:[h(l−1)
1 ...h(l−1)
n ]T (15)
h(l)
i = GRU(a(l)
i , h(l−1)
i ) (16)
where A∈ Rdn×2dn is a matrix determining how nodes in the graph communicating with each
other. n is the number of nodes in the graph. Ai: ∈ Rd×2d are the two columns of blocks in
A corresponding to node vi. In Eq. (14), the initial node feature xi are padded with extra zeros
to make the input size equal to the hidden size. Eq. (15) computes a(l)
i ∈ R2d by aggregating
information from different nodes via incoming and outgoing edges with parameters dependent on
the edge type and direction. The following step uses a GRU unit to update the hidden state of node
v by incorporating a(l)
i and the previous timestep hidden state h(l−1)
i .
3.2.2 G RAPH POOLING
Graph pooling layers are proposed to generate graph-level representations for graph-focused down-
stream tasks, such as graph classiﬁcation and prediction based on the node embedding learned from
the graph ﬁltering. This is because the learned node embeddings are sufﬁcient for node-focused
tasks, however, for graph-focused tasks, a representation of the entire graph is required. To this
end, we need to summarize the node embeddings information and the graph structure information.
The graph pooling layers can be classiﬁed into two categories: ﬂat graph pooling and hierarchical
graph pooling. The ﬂat graph pooling generates the graph-level representation directly from the
node embeddings in a single step. In contrast, the hierarchical graph pooling contains several graph
pooling layers and each of the pooling layer follows a stack of graph ﬁlters. In this section, we
brieﬂy introduce several representative ﬂat pooling layers and hierarchical pooling layers.
Flat Graph Pooling Ideally, an aggregator function would be invariant to permutations of its in-
put while maintaining a large expressive capacity. The graph pooling operation fpool is commonly
implemented as Max-pooling and Average-pooling. Another popular choices are the variants of the
Max-pooling and Average pooling operations by following a fully-connected layer (FC) transfor-
mation. The resulting max pooling and FCmax can be expressed as:
ri = max(H:,i) or ri = max(WH:,i) (17)
12





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
where i denotes the i-th channel of the node embedding andH:,i∈ Rn×1 is a vector. W is a matrix
that denotes to the trainable parameters of the FCmax pooling layer.ri is a scalar and the ﬁnal graph
embedding R = [ r1, r2, ..., rn]T . Finally, a powerful but less common pooling operation is the
BiLSTM aggregation function which is not permutation invariant on the set of node embeddings.
However, it has been often demonstrated to have better expressive power than other ﬂat pooling
operations (Hamilton et al., 2017a; Zhang et al., 2019e).
Hierarchical Graph Pooling Hierarchical graph pooling coarsens the graph step by step to learn
the graph-level embeddings. Hierarchical pooling layers can be divided into two categories accord-
ing to the ways to coarsen the graph. One type of hierarchical pooling layer coarsens the graph
by sub-sampling the most important nodes as the nodes of the coarsened graph (Gao et al., 2019).
Another type of hierarchical pooling layer combines nodes in the input graph to form supernodes,
which serve as the nodes of the coarsened graph (Ying et al., 2018; Ma et al., 2019). After sub-
sampling nodes or generating supernodes, the hierarchical graph pooling fpool can be summarized
as: (1) generating graph structure for the coarsened graph; (2) generating node features for the
coarsened graph. The graph structure for the coarsened graph is generated from the input graph:
A′ = COARSEN (A) (18)
where A∈ Rn×n is the adjacent matrix of the input graph, and A′∈ Rn′×n′
is the adjacent matrix
of the coarsened graph. f(.) is the graph sub-sampling or supernodes generating function.
4. Graph Construction Methods for NLP
In the previous section, we have discussed the basic foundations and methods of GNNs once given a
graph input. Unfortunately, for most of the NLP tasks, the typical inputs are sequence of text rather
than graphs. Therefore, how to construct a graph input from sequences of text becomes a demanding
step in order to leverage the power of GNNs. In this chapter, we will focus on introducing two major
graph construction approaches, namely static graph construction and dynamic graph construction
for constructing graph structured inputs in various NLP tasks.
4.1 Static Graph Construction
The static graph construction approach aims to construct the graph structures during preprocessing
typically by leveraging existing relation parsing tools (e.g., dependency parsing) or manually de-
ﬁned rules. Conceptually, a static graph incorporates different domain/external knowledge hidden
in the original text sequences, which augments the raw text with rich structured information.
In this subsection, we summarize various static graph construction methods in the GNN for NLP
literature and group them into totally eleven categories. We assume that the input is a document
doc ={para1, para2, ..., paran}, which consists of n paragraph denoted as para. Similarly, a
paragraph consists of m sentences denoted as parai ={sent1, sent2, ..., sentm}. Each sentence
then consists of l words denoted as senti ={w1, w2, ..., wl}.
4.1.1 S TATIC GRAPH CONSTRUCTION APPROACHES
Dependency Graph Construction The dependency graph is widely used to capture the depen-
dency relations between different objects in the given sentences. Formally, given a paragraph, one
13





---

## Part 2 — Graph Construction Methods for NLP (Section 4, pp. 14–26)


LINGFEI WU AND YU CHEN , ET AL .
Table 2: Two major graph construction approaches: static and dynamic graph constructions
Approaches Techniques References
Static Graph
Dependency Graph
Zhang et al. (2019b); Guo et al. (2019a); Zhang and Qian (2020); Fei et al. (2020)Bastings et al. (2017); Nguyen and Grishman (2018); Ji et al. (2019); Liu et al. (2018b)Xu et al. (2018c); Zhang et al. (2018d); Song et al. (2018e); Li et al. (2017)Do and Rehbein (2020); Yan et al. (2019); Marcheggiani et al. (2018); Zhou et al. (2020b)Vashishth et al. (2018); Xia et al. (2020); Jin et al. (2020a); Huang and Carley (2019)Sahu et al. (2019); Cui et al. (2020c); Xu et al. (2020b); Zhang et al. (2020f)Liu et al. (2019d); Li et al. (2020b); Wang et al. (2020c); Tang et al. (2020a)Qian et al. (2019); Pouran Ben Veyseh et al. (2020); Wang et al. (2020f)Constituency Graph Li et al. (2020b); Marcheggiani and Titov (2020); Xu et al. (2018c)
AMR Graph
Liao et al. (2018); Wang et al. (2020d,e); Ribeiro et al. (2019a)Jin and Gildea (2020); Jin et al. (2020a); Cai and Lam (2020b)Bai et al. (2020); Beck et al. (2018a); Yao et al. (2020)Zhang et al. (2020b); Zhao et al. (2020a); Zhu et al. (2019a)Song et al. (2020, 2018c, 2019); Damonte and Cohen (2019)Information ExtractionWu et al. (2020b); Vashishth et al. (2018)Graph Huang et al. (2020b); Gupta et al. (2019)Discourse Graph Song et al. (2018e); Li et al. (2020c); Yasunaga et al. (2017); Xu et al. (2020a)
Knowledge Graph
Ye et al. (2019); Yang et al. (2019); Gupta et al. (2019); Xu et al. (2020c)Sun et al. (2020b); Xu et al. (2019b); Wang et al. (2019c)Kapanipathi et al. (2020); Zhang et al. (2019a, 2020g); Sun et al. (2018a)Malaviya et al. (2020); Huang et al. (2020b); Schlichtkrull et al. (2018); Sun et al. (2019a)Bansal et al. (2019); Saxena et al. (2020); Koncel-Kedziorski et al. (2019)Teru et al. (2020); Lin et al. (2019a); Ghosal et al. (2020); Feng et al. (2020a)Wu et al. (2019a,b, 2020b,c)Wang et al. (2019d,a, 2020h, 2019e)Zhao et al. (2020b); Shang et al. (2019); Jin et al. (2019); Nathani et al. (2019a)Sorokin and Gurevych (2018a); Cao et al. (2019c); Han et al. (2020); Xie et al. (2020)
Coreference Graph Sahu et al. (2019); Qian et al. (2019); Xu et al. (2020b,a)De Cao et al. (2018); Luan et al. (2019)Topic Graph Linmei et al. (2019); Li et al. (2020c)
Similarity Graph ConstructionXia et al. (2019); Yao et al. (2019a); Yasunaga et al. (2017)Linmei et al. (2019); Zhou et al. (2020a); Wang et al. (2020b)Liu et al. (2019b); Hu et al. (2020b); Jia et al. (2020); Li et al. (2020c)
Co-occurrence Graph Christopoulou et al. (2019); Zhang and Qian (2020); Hu et al. (2020b)Zhang et al. (2020d); Yao et al. (2019a); De Cao et al. (2018)Edouard et al. (2017); Zhu et al. (2018); Liu et al. (2019b)
App-driven Graph
Ding et al. (2019a); Yin et al. (2020); Luo and Zhao (2020); Ding et al. (2019b)Sui et al. (2019); Tang et al. (2020b); Ran et al. (2019); Hu et al. (2019a)Gui et al. (2019); Li and Goldwasser (2019); Xiao et al. (2019); Xu et al. (2018a)Qu et al. (2020); Bogin et al. (2019b); Huo et al. (2019); Shao et al. (2020)Fernandes et al. (2019); Liu et al. (2020); Huang et al. (2019); Linmei et al. (2019)Bogin et al. (2019a); LeClair et al. (2020); Qiu et al. (2019); Zheng et al. (2020)Ferreira and Freitas (2020); Zheng and Kordjamshidi (2020); Fang et al. (2020a)Allamanis et al. (2018); Christopoulou et al. (2019); Thayaparan et al. (2019)
Dynamic graph
Graph SimilarityNode Embedding BasedChen et al. (2020e,g,f,d)Metric LearningStructure-awareLiu et al. (2019a, 2021a)Graph Sparsiﬁcation TechniquesChen et al. (2020e,g,f)Combining Intrinsic andChen et al. (2020f); Liu et al. (2021a)Implicit Graph Structures
can obtain the dependency parsing tree (e.g., syntactic dependency tree or semantic dependency
parsing tree) by using various NLP parsing tools (e.g., Stanford CoreNLP (Lee et al., 2011)). Then
one may extract the dependency relations from the dependency parsing tree and convert them into
a dependency graph (Xu et al., 2018b; Song et al., 2018d). Moreover, since the given paragraph
has sequential information while the graph nodes are unordered, one may introduce the sequential
links to reserve such vital information in the graph structure (Sahu et al., 2019; Qian et al., 2019;
Xu et al., 2018c; Li et al., 2017). Next, we will discuss a representative dependency graph con-
struction method given the inputs para and its extracted parsing tree, including three key steps: 1)
constructing dependency relation, 2) constructing sequential relation, and 3) ﬁnal graph conversion.
An example for the dependency graph is shown in Fig. 2.
14





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
Step 1: Dependency Relations. Given the sentences in a speciﬁc paragraph, one ﬁrst obtains the
dependency parsing tree for each sentence. We denote dependency relations in the dependency tree
as (wi, reli,j, wj), where wi, wj are the word nodes linked by an edge type reli,j. Conceptually,
an edge denotes a dependency relation ” wi depends on wj with relation reli,j”. We deﬁne the
dependency relation set asRdep.
Step 2: Sequential Relations. The sequential relation encodes the adjacent relation of the elements
in the original paragraph. Speciﬁcally, for dependency graph constructing, we deﬁne the sequential
relation setRseq⊆V×V , whereV is the basic element (i.e., word) set. For each sequential relation
(wi, wi+1)∈R seq, it means wi is adjacent to wi+1 in the given paragraph.
Step 3: Dependency Graph. The dependency graphG(V,E) consists of the word nodes and two
relations discussed above. Given the paragraph para, dependency relation set Rdep, and the se-
quential relation setRseq, ﬁrstly, for each relation (wi, reli,j, wj)∈R dep, one adds the nodes vi
(for the word wi) and vj (for the word wj) and a directed edge from node vi to node vj with edge
type reli,j. Secondly, for each relation (wi, wj)∈R seq, one adds two nodes vi (for the word wi)
and vj (for the word wj) and an undirected edge between nodes vi and vj with speciﬁc sequential
type.
are there ada jobs outside austin
aux
expl
obj
nmod
case
are there ada jobs outside austin
S
VP
S
VP
NP
PP
Text input: are there ada jobs outside austin
Dependency 
parsing
Constituency 
parsing
Figure 2: An example is shown for the dependency graph (left) and the constituency graph (right),
respectively. The text input is from JOBS640 (Luke, 2005) dataset.
Constituency Graph Construction The constituency graph is another widely used static graph
that is able to capture phrase-based syntactic relations in one or more sentences. Unlike dependency
parsing, which only focuses on one-to-one correspondences between single words (i.e., word level),
constituency parsing models the assembly of one or several corresponded words (i.e., phrase level).
Thus it provides a new insight about the grammatical structure of a sentence. In this following
subsection, we will discuss the typical approach for constructing a constituency graph (Li et al.,
2020b; Marcheggiani and Titov, 2020; Xu et al., 2018c). We ﬁrst explain the basic concepts of
the constituency relations and then illustrate the constituency graph construction procedure. An
example for the Constituency graph is shown in Fig. 2.
Step 1: Constituency Relations. In linguistics, constituency relation means the relation following
the phrase structure grammars instead of the dependency relation and dependency grammars. Gen-
erally, the constituency relation derives from the subject(noun phrase NP)-predicate(verb phrase
VP) relation. In this part, we only discuss the constituency relation deriving from the constituency
parsing tree. Unlike the dependency parsing tree, in which all nodes have the same type, the con-
stituency parsing tree distinguishes between the terminal and non-terminal nodes. Non-terminal
categories of the constituency grammar label the parsing tree’s interior nodes (e.g., S for sentence,
15





LINGFEI WU AND YU CHEN , ET AL .
and NP for noun phrase). In contrast, the leaf nodes are labeled by terminal categories (words in
sentences). The nodes set can be denoted as: 1) non-terminal nodes set Vnt (e.g. S and NP) and 2)
terminal nodes setVwords. The constituency relation set are associated with the tree’s edges, which
can be denoted asRcons⊆V nt× (Vnt +Vwords).
Step 2: Constituency Graph. A constituency graphG(V,E) consists of both the non-terminal nodes
Vnt and the terminal nodes Vwords, and the constituency edges as well as the sequential edges.
Similar to the dependency graph, given a paragraph para and the constituency relation setRcons,
for each constituency relation (wi, reli,j, wj)∈R cons, one adds the nodes vi (for the word wi) and
vj (for the word wj) and a directed edge from nodevi to node vj. And then for each word nodes pair
(vi, vj) for the words which are adjacent in the original text, one adds an undirected edge between
them with the speciﬁc sequential type. These sequential edges are used to reserve the sequential
information (Li et al., 2020b; Xu et al., 2018c).
nameperson
describe-01
“Paul”
fighter:ARG2
:ARG1
:ARG0 :name :op1
Figure 3: An example of AMR graph, the original sentence is ”Pual’s description of himself: a
ﬁghter”.
AMR Graph Construction The AMR graphs are rooted, labeled, directed, acyclic graphs, which
are widely used to represent the high-level semantic relations between abstract concepts of the
unstructured and concrete natural text. Different from the syntactic idiosyncrasies, the AMR is
the high-level semantic abstraction. More concretely, the different sentences that are semantically
similar may share the same AMR parsing results, e.g., ”Paul described himself as a ﬁghter” and
”Paul’s description of himself: a ﬁghter”, as shown in Fig. 3. Despise the fact that the AMR is biased
toward English, it is a powerful auxiliary representation for linguistic analysis (Song et al., 2018c;
Damonte and Cohen, 2019; Wang et al., 2020d). Similar to the previously introduced dependency
and constituency trees, an AMR graph is derived from an AMR parsing tree. Next, we focus on
introducing the general procedure of constructing the AMR graph based on the AMR parsing tree.
We will discuss the basic concept of AMR relation and then show how to convert the relations into
an AMR graph.
Step 1: AMR Relations. Conceptually, there are two types of nodes in the AMR parsing tree: 1)
the name (e.g. ”Paul”) is the speciﬁc value of the node instance and 2) the concepts are either
English words (e.g. ”boy”), PropBank framesets (Kingsbury and Palmer, 2002) (e.g. ”want-01”), or
special keywords. The name nodes are the unique identities, while the concept nodes are shared by
different instances. The edges that connect nodes are called relations (e.g. :ARG0 and :name). One
may extract these AMR relations from the node pairs with edges, which is denoted as(ni, ri,j, nj)∈
Ramr.
Step 2: AMR Graph. The AMR graphG(V,E), which is rooted, labeled, directed, acyclic graph
(DAG), consists of the AMR nodes and AMR relations discussed above. Similar to the dependency
and constituency graphs, given the sentence sent and the AMR relation setRamr, for each relation
16





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
(ni, ri,j, nj)∈R amr, one adds the nodes vi (for the AMR node ni) and vj (for the AMR node nj)
and add a directed edge from node vi to node vj with edge type ri,j
Text input: Paul, a renowned 
computer scientist, grew up in 
Seattle. He attended Lakeside 
School.
grew up in 
attended
Paul
He
a renowned … 
Seattle
Lakeside 
SchoolCoreference
OpenIE
Figure 4: An example for IE graph construction which contains both the Co-reference process and
the Open Information Extraction process.
Information Extraction Graph Construction The information extraction graph (IE Graph) aims
to extract the structural information to represent the high-level information among natural sentences,
e.g., text-based documents. These extracted relations that capture relations across distant sentences
have been demonstrated helpful in many NLP tasks (Wu et al., 2020b; Vashishth et al., 2018; Gupta
et al., 2019). In what follows, we will discuss the technical details on how to construct an IE graph
for a given paragraph para (Huang et al., 2020b; Vashishth et al., 2018). We divide this process
into two three basic steps: 1) coreference resolution, 2) constructing IE relations, and 3) graph
construction.
Step 1: Coreference Resolution. Coreference resolution is the basic procedure for informa-
tion extraction task which aims to ﬁnd expressions that refer to the same entities in the text se-
quence (Huang et al., 2020b). As shown in Figure 4, the name ”Pual”, the noun-term ”He” and ”a
renowned computer scientist” may refer to the same object (person). Many NLP tools such as Ope-
nIE (Angeli et al., 2015) provide coreference resolution function to achieve this goal. We denotes
the coreference cluster C as a set of phrases referring to the same object. Given a paragraph, one
can obtain the coreference setsC ={C1, C2, ..., Cn} extracting from unstructured data.
Step 2: IE Relations. To construct an IE graph, the ﬁrst step is to extract the triples from the para-
graphs, which could be completed by leveraging some well-known information extraction systems
(i.e. OpenIE (Angeli et al., 2015)). We call each triple (subject, predicate, object) as a relation,
which is denoted (ni, ri,j, nj)∈R ie. It is worth noting if two triples differ only by one argument,
and the other arguments overlap, one only keep the longer triple.
Step 3: IE Graph Construction. The IE graph G(V,E) consists of the IE nodes and IE rela-
tions discussed above. Given the paragraph para and the IE relation set Rie, for each relation
(ni, ri,j, nj)∈R ie, one adds the nodes vi (for the subject ni) and vj (for the object nj) and add a
directed edge from node vi to node vj with the corresponding predicate types (Huang et al., 2020b).
And then, for each coreference cluster Ci∈C , one may collapse all coreferential phrases in Ci
into one node. This could help greatly reduce the number of nodes and eliminate the ambiguity by
keeping only one node.
Discourse Graph Construction Many NLP tasks suffer from long dependency challenge when
the candidate document is too long. The discourse graph, which describes how two sentences are
logically connected to one another, are proved effective to tackle such challenge (Christensen et al.,
2013). In the following subsection, we will brieﬂy discuss the discourse relations between given
sentences and then introduce the general procedure to construct the discourse graphs (Song et al.,
2018e; Li et al., 2020c; Yasunaga et al., 2017; Xu et al., 2020a).
17





LINGFEI WU AND YU CHEN , ET AL .
Step 1: Discourse Relation. The discourse relations derive from the discourse analysis, which aims
to identify sentence-wise ordering constraints over a set of sentences. Given two sentences senti
and sentj, one can deﬁne the discourse relation as (senti, sentj), which represents the discourse
relation ”sentence sentj can be placed after sentence senti.” The discourse analysis has been ex-
plored for years, and many theories have been developed for modeling discourse relations such
as the Rhetorical Structure Theory (RST) (Mann and Thompson, 1987) and G-Flow (Christensen
et al., 2013). In many NLP tasks, given a document doc, one ﬁrstly segmentsdoc into sentences set
V ={sent1, sent2, ..., sentm}. Then one applies discourse analysis to get the pairwise discourse
relation set denoted asRsep⊆V×V .
Step 2: Discourse Graph. The discourse graphG(V,E) consists of the sentences nodes and dis-
course relations discussed above. Given the document doc and the discourse relation setRdis, for
each relation (senti, sentj)∈R dis, one adds the nodes vi (for the sentence senti) and vj (for the
sentence sentj) and add a directed edge from node vi to node vj.
Question: who acted in the movies directed by the director of [Some Mother's Son] 
Answer: Don Cheadle, Joaquin Phoenix
[Some Mother's Son]
Hotel Rwanda
Terry George
Reservation Road 
directed_by
starred_actors
Don Cheadle
starred_actors Joaquin Phoenix
Get the concept sub-
graph from KB
directed_by
directed_by
Figure 5: An example for knowledge graph construction, where the knowledge base (KB) used and
the generated concept graph are both from the dataset MetaQA (Zhang et al., 2018a).
Knowledge Graph Construction Knowledge Graph (KG) that captures entities and relations
can greatly facilitate learning and reasoning in many NLP applications. In general, the KGs can be
divided into two main categories depending on their graph construction approaches. Many applica-
tions treat the KG as the compact and interpretable intermediate representation of the unstructured
data (e.g., the document) (Wu et al., 2020b; Koncel-Kedziorski et al., 2019; Huang et al., 2020b).
Conceptually, it is almost similar to the IE graph, which we have discussed previously. On the
other hand, many other works (Wu et al., 2020c; Ye et al., 2019; Bansal et al., 2019; Yang et al.,
2019) incorporate the existing knowledge bases such as Y AGO (Suchanek et al., 2008)) and Con-
ceptNet (Speer et al., 2017) to further enhance the performance of downstream tasks (Zhao et al.,
2020b). In what follows, we will brieﬂy discuss the second category of KG from the view of the
graph construction.
The KG can be denoted as G(V,E), which is usually constructed by elements in knowledge
base. Formally, one deﬁnes the triple (e1, rel, e2) as the basic elements in the knowledge base, in
which e1 is the source entity, e2 is the target entity, and rel is the relation type. Then one adds two
nodes v1 (for the source element e1) and v2 (for the target element e2) in the KG and add a directed
edge from node v1 to node v2 with edge type rel. An example of such KG is shown in Fig. 5.
18





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
It is worth noting that the KG plays different roles in various applications. In some applications
(e.g. knowledge graph completion and knowledge base question answering), KG is always treated
as part of the inputs. In this scenario (Ye et al., 2019; Zhang et al., 2020g; Li et al., 2019; Wu
et al., 2020a), researchers typically use the whole KGG as the learning object. But for some other
applications (e.g. natural language translation), the KG can be treated as the data augmentation
method. In this case, the whole KG such as ConceptNet (Speer et al., 2017) is usually too large and
noisy for some domain-speciﬁc applications (Kapanipathi et al., 2020; Lin et al., 2019a), and thus
it is not suitable to use the whole graph as inputs. In contrast, as shown in Figure 5, one instead
usually constructs subgraphs from the given query (it is often the text-based inputs like the queries
in the reading comprehension task) (Xu et al., 2019a; Teru et al., 2020; Kapanipathi et al., 2020).
The construction methods could may vary dramatically in the literature. Here, we only present
one representative method for illustration purpose (Teru et al., 2020). The ﬁrst thing for constructing
KG is to fetch the term instances in the given query. Then, they could link the term instances to the
concepts in the KG by some matching algorithms such as max-substring matching. The concepts
are regarded as the initial nodes in the extracted subgraph. Next step is to fetch the 1-hop neighbors
of the initial nodes in the KG. Additionally, one may calculate the relevance of the neighbors with
the initial nodes by applying some graph node relevance model such as the Personalized PageRank
(PPR) algorithm (Page et al., 1999). Then based on the results, one may further prune out the edges
with relevance score that is below the conﬁdence threshold and remove the isolated neighbors. The
remaining ﬁnal subgraph is then used to feed any graph representation learning module later.
Coreference Graph Construction In linguistics, coreference (or co-reference) occurs when two
or more terms in a given paragraph refer to the same object. Many works have demonstrated that
such phenomenon is helpful for better understanding the complex structure and logic of the corpus
and resolve the ambiguities (Xu et al., 2020b; De Cao et al., 2018; Sahu et al., 2019). To effec-
tively leverage the coreference information, the coreference graph is constructed to explicitly model
the implicit coreference relations. Given a set of phrases, a coreference graph can link the nodes
(phrases) which refer to the same entity in the text corpus. In the following subsection, we focus on
the coreference graph construction for a paragraph para consisting of m sentences. We will brieﬂy
discuss the coreference relation and then discuss the approaches for building the coreference graph
in various NLP tasks (De Cao et al., 2018; Sahu et al., 2019; Qian et al., 2019; Xu et al., 2020b,a;
Luan et al., 2019). It is worth noting that although it is similar to the IE graph’s ﬁrst step, the coref-
erence graph will explicitly model the coreference relationship by graph instead of collapse into one
node.
Step 1: Coreference Relation. The coreference relations can be obtained easily by the coreference
resolution system, as discussed in IE graph construction. Similarly, we can obtain the coreference
clustersC given a speciﬁc paragraph. All phrases in a clusterCi∈C refer to the same object.
Step 2: Coreference Graph. The coreference graph are built on the coreference relation setRcoref .
It can be generally divided into two main category depending on the node type: 1) phrases (or
mentions) (Koncel-Kedziorski et al., 2019; Luan et al., 2019; De Cao et al., 2018), 2) words (Sahu
et al., 2019). For the ﬁrst class, the coreference graph G consists of all mentions in relation set
Rcoref . For each phrase pair pi, pj in cluster Ck∈C , one may add an undirected edge between
node vi (for the phrase pi) and node vj (for the phrase pj). For the second case, the coreference
graphG consists of words. One minor difference is that one only links the ﬁrst word of each phrase
for each associated phrases.
19





LINGFEI WU AND YU CHEN , ET AL .
Sentence  
TF-IDF vector
Sentence
souness backs smith 
for scotland 
uk will stand firm on 
eu rebate 
qpr keeper day heads 
for preston
former ni minister 
scott dies
Cranes: Flying giant 
returning to Ireland 
after 300 years
Figure 6: An example for similarity graph construction. We use sentences as nodes and initialize
their features with TF-IDF vectors.
Similarity Graph Construction The similarity graphs aim to quantify the similarity between
nodes, which are widely used in many NLP tasks (Liu et al., 2019b; Linmei et al., 2019; Yasunaga
et al., 2017). Since the similarity graph is typically application-oriented, we focus on the basic pro-
cedure of constructing the similarity graph for various types of elements such as entities, sentences
and documents, and neglect the application speciﬁc details. It is worth noting that the similarity
graph construction is conducted during preprocessing and is not jointly trained with the remaining
learning system in an end-to-end manner. One example of similarity graph is shown in Fig. 6.
Step 1: Similarity Graph. Given a corpus C, in a similarity graph G(V,E), the graph nodes can
be deﬁned in different granularity levels such as entities, sentences and documents. We denote the
basic node set asV regardless of speciﬁc node types. One can calculate the node features by various
mechanisms such as TF-IDF for sentences (or documents) (Liu et al., 2019b; Yasunaga et al., 2017)
and embeddings for entities (Linmei et al., 2019). Then, similarity scores between node pairs can
be computed by various metrics such as cosine similarity (Liu et al., 2019b; Linmei et al., 2019;
Yasunaga et al., 2017), and used to indicate edge weights of the node pairs.
Step 2: Sparse mechanism. The initial similarity graph is typically dense even some edge weights
are very small or even negative. These values can be treated as noise, which plays little roles in
the similarity graph. Thus various sparse techniques are proposed to further improve the quality
of graph by sparsifying a graph. One widely used sparse method is k-NN (Liu et al., 2019b).
Speciﬁcally, for nodevi and its’ neighbor set N(vi), one only reserves edges by keeping k largest
edge weights and dropping the remaining edges. The other widely used method isϵ−sparse (Linmei
et al., 2019; Yasunaga et al., 2017). In particular, one will remove the edges whose weights are
smaller than the certain threshold ϵ.
Co-occurrence Graph Construction The co-occurrence graph aims to capture the co-occurrence
relation between words in the text, which is widely used in many NLP tasks (Christopoulou et al.,
2019; Zhang and Qian, 2020; Zhang et al., 2020d). The co-occurrence relation, which describes
the frequency of two words that co-occur within a ﬁx-sized context window, is an important feature
20





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
Text input: To be, or not to be: …
Co-occurrence graph
or be
to not
to be or not
to 2 2 1
be 2 1 2
or 2 1 1
not 1 2 1
Co-occurrence matrix
1
2
2
1
2
2
Figure 7: An example for co-occurrence graph construction where edge weights stand for the co-
occurrence frequency between words. We set the window size as 3.
capturing the semantic relationship among words in the corpus. In what follows, we will ﬁrst present
the approaches of obtaining the co-occurrence relations and then discuss the basic procedure of
building a co-occurrence graph for a corpus C. An example of co-occurrence graph can be seen in
Fig. 7.
Step 1: Co-occurrence Relation. The co-occurrence relation is deﬁned by the co-occurrence matrix
of the given corpus C. For a speciﬁc paragraph para consists of m sentences, the co-occurrence
matrix describes how words occur together. One may denote the co-occurrence the matrix as M∈
R|V|×|V|, where|V| is the vocabulary size of C. Mwi,wj describes how many times word wi, wj
occur together within a ﬁx-size sliding windows in the corpusC. After obtaining the co-occurrence
matrix, there are two typical methods to calculate the weights between words: 1) co-occurrence
frequency (Zhang et al., 2020d; Christopoulou et al., 2019; Zhang and Qian, 2020; Edouard et al.,
2017; Zhu et al., 2018) and 2) point-wise mutual information (PMI) (Yao et al., 2019a; Hu et al.,
2020b, 2019c).
Step 2: Co-occurrence Graph. The co-occurrence graphG(V,E) consists of the words nodes and
co-occurrence relations discussed above. Given the corpus C and the co-occurrence relation set
Rco, for each relation (wi, wj)∈R co, one adds the nodes vi (for the word wi) and vj (for the
word wj) and add an undirected edge from node vi to node vj initialized with the aforementioned
calculated edge weights.
Business
There was the $5 million Deutsche Bank Championship to 
prepare for and the Ryder Cup is a few weeks away, but the 
first order of business for Jim Furyk yesterday was to make 
sure his wife and children were headed for safety.
Dolphin groups, or "pods", rely on socialites to keep them 
from collapsing, scientists claim.
A sports psychologist says how footballers should prepare 
themselves for the high-pressure penalties.
Research
Sports
Figure 8: An example for topic graph construction, where the dash line stands for the topic modeling
process by leveraging the LDA algorithm on dataset AG news (Zhang et al., 2015).
Topic Graph Construction The topic graph is built on several documents, which aims to model
the high-level semantic relations among different topics (Linmei et al., 2019; Li et al., 2020c). In
21





LINGFEI WU AND YU CHEN , ET AL .
particular, given a set of documents D ={doc1, doc2, ..., docm}, one ﬁrst learns the latent topics
denoted asT using some topic modeling algorithms such as LDA (Blei et al., 2003). Then one
could construct the topic graphG(V,E) withV =D∪T . The undirected edge between the node
vi (for a document) and the node vj (for a topic) is built only if the document has that topic. An
example of topic graph is shown in Fig. 8.
SQL query input: SELECT company WHERE assets > val0 AND sales > val0 AND industry_rank ≤ val1
Application 
driven 
SELECT ANDcompany
assets> val0sales
industry_rank ≤ val1
Figure 9: An example for application-driven graph construction, which is specially designed for
SQL query input.
App-driven Graph Construction The app-driven graphs refer to the graph specially designed
for speciﬁc NLP tasks (Gui et al., 2019; Ding et al., 2019a; Yin et al., 2020; Luo and Zhao, 2020),
which cannot be trivially covered by the previously discussed static graph types. In some NLP
tasks, it is common to represent unstructured data by structured formation with application-speciﬁc
approaches. For example, the SQL language can be naturally represented by the SQL parsing
tree. Thus it can be converted to the SQL graph (Xu et al., 2018a; Bogin et al., 2019a; Huo et al.,
2019; Bogin et al., 2019b). Since these graphs are too specialized based on the domain knowledge,
there are no uniﬁed pattern to summarize how to build an app-driven graph. An example of such
application-driven graph like SQL graph is illustrated in Fig. 9. In Sec. 7, we will further discuss
how these graph construction methods are used in various popular NLP tasks.
4.1.2 H YBRID GRAPH CONSTRUCTION AND DISCUSSION
Most previous static graph construction methods only consider one speciﬁc relation between nodes.
Although the obtained graphs capture the structure information well to some extent, they are also
limited in exploiting different types of graph relations. To address this limitation, there is an in-
creasing interest in building a hybrid graph by combing several graphs together in order to enrich
the semantic information in graph (Jia et al., 2020; Sahu et al., 2019; Xu et al., 2018c; Zeng et al.,
2020; Xu et al., 2020b,a; Christopoulou et al., 2019; Yao et al., 2019a). The method of constructing
a hybrid graph is mostly application speciﬁc, and thus we only present some representative approach
for such a graph construction.
To capture multiple relations, a common strategy is to construct a heterogeneous graph, which
contains multiple types of nodes and edges. Without losing generality, we assume that one may
create a hybrid graphGhybrid with two different graph sourcesGa(Va,Ea) andGb(Vb,Eb). Graphs
a, b are two different graph types such as dependency graph and constituency graph. Given these
textual inputs, if Ga andGb share the same node sets (i.e., Va =Vb), we merge the edge sets by
annotating relation-speciﬁc edge types (Xu et al., 2018c; Sahu et al., 2019; Zeng et al., 2020; Xu
et al., 2020b,a). Otherwise, we merge the Va andVb to get the hybrid node set, denoted as V =
22





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
Va∪Vb (Jia et al., 2020; Christopoulou et al., 2019). Then we generateEa andEb toE by mapping
the source and target nodes fromVa andVb toV.
4.2 Dynamic Graph Construction
Although static graph construction has the advantage of encoding prior knowledge of the data into
the graph structure, it has several limitations. First of all, extensive human efforts and domain ex-
pertise are needed in order to construct a reasonably performant graph topology. Secondly, the man-
ually constructed graph structure might be error-prone (e.g., noisy or incomplete). Thirdly, since the
graph construction stage and graph representation learning stage are disjoint, the errors introduced
in the graph construction stage cannot be corrected and might be accumulated to later stages, which
can result in degraded performance. Lastly, the graph construction process is often informed solely
by the insights of the NLP practitioners, and might be sub-optimal for the downstream prediction
task.
Graph 
sparsiﬁcation
Graph similarity 
metric learning
Data points
{ X , A
(0)
}
<latexit sha1_base64="DGc8/z44oBE/vqylnbUvf91FXtk=">AAADlHicfVLbattAEF1LvaTuzW6hL31ZagI2bV2ppKQPDTgNhT6UkkKdmFqOWK1WySarC9pRgln0Q/2cvvVvOpLl4FzcAcHozJmdM4cJMiU1OM7flmXfuXvv/saD9sNHj5887XSfHei0yLkY81Sl+SRgWiiZiDFIUGKS5YLFgRKHwdleVT88F7mWafIT5pmYxew4kZHkDBDyu63fnhLgnQvuxQxOgqi96V3IUIBUoTAVbnbL8sj0YVDSHeopfDpktC58K33jlPQ17bv07bI0oF6UM75s9Y08bdpL4+ki9k9vK5U4dokvoDd0rQ6vYlfIrwbA30o8Zwo1oRARAcvz9IKuwMh0cAVUW6swcsctj8BcZUiUQt9R+J8Jq88LYOtlXhqDrMEaGkpqN4tPqpUvHXBW1lxa4nd6ztCpg95M3CbpkSb2/c4fL0x5EYsEuGJaT10ng5lhOUiuBE4utMgYP2PHYoppwmKhZ6Y+qpJuIhLSKM3xS4DW6GqHYbHW8zhAZuWhvl6rwNtq0wKijzMjk6wAkfDFoKhQFFJaXSgNZS44qDkmjOcStVJ+wvCmAO+4jSa411e+mRy8H7pbww8/tnqjz40dG+QleUX6xCXbZES+kn0yJtzqWtvWyNq1X9if7D37y4JqtZqe5+RK2N//AbqgJWI=</latexit>
{ X , S }
<latexit sha1_base64="Iyotxq7FlLav7dxHgZQBwOo3fvA=">AAAChXicbVFNbxMxEPVugZbw0bQcuVhElVJBo90q0F4qClw4cCiCtJHisPJ6Z1u33g/Zs0WR5X/Cr+LGv8GbbCVoO5Klp/f8Zuw3aa2kwSj6E4RrDx4+Wt943Hvy9Nnzzf7W9qmpGi1gIipV6WnKDShZwgQlKpjWGniRKjhLrz61+tk1aCOr8jsuapgX/LyUuRQcPZX0fzEFyK5BsILjRZr3dthPmQFKlYFtefvBuR92iLuOHlGmfOeM06XwxSU2cvQ1HcZ070bapSzXXNxYEysvO7uzzDRFcnmf5HpsRU/dm1Xzb465XtIfRKNoWfQuiDswIF2dJP3fLKtEU0CJQnFjZnFU49xyjVIo8FMaAzUXV/wcZh6WvAAzt8sUHd3xTEbzSvtTIl2y/zosL4xZFKm/2WZlbmsteZ82azA/nFtZ1g1CKVaD8kZRrGi7EppJDQLVwgMutPRvpeKC+xTRL64NIb795bvgdH8Uj0dvv44Hxx+7ODbIS/KKDElMDsgx+UxOyISIIAyGQRzsh+vhXjgO362uhkHneUH+q/D9X8bIw2g=</latexit>
GNN y
<latexit sha1_base64="VUhgI3qY4V6LAwvPr5PUpKzXDn8=">AAAB8XicbVDLSgMxFL1TX7W+qi7dBIvgqsxIRZdFNy4r2Ae2Q8mkmTY0kwxJRhiG/oUbF4q49W/c+Tdm2llo64HA4Zx7ybkniDnTxnW/ndLa+sbmVnm7srO7t39QPTzqaJkoQttEcql6AdaUM0HbhhlOe7GiOAo47QbT29zvPlGlmRQPJo2pH+GxYCEj2FjpcRBhMwnCLJ0NqzW37s6BVolXkBoUaA2rX4ORJElEhSEca9333Nj4GVaGEU5nlUGiaYzJFI9p31KBI6r9bJ54hs6sMkKhVPYJg+bq740MR1qnUWAn84R62cvF/7x+YsJrP2MiTgwVZPFRmHBkJMrPRyOmKDE8tQQTxWxWRCZYYWJsSRVbgrd88irpXNS9Rv3yvlFr3hR1lOEETuEcPLiCJtxBC9pAQMAzvMKbo50X5935WIyWnGLnGP7A+fwBAWWRJQ==</latexit>
Learned graph
{ X ,
e
A }
<latexit sha1_base64="ejxQR6aBYsDP7JveJ3qSdjvPuXU=">AAACkXicbVFdaxQxFM1M/airtmv76EtwKWxRlxlZ0T5UVn0R9KGC2y5s1iGTudOmzXyQ3GlZQv6Pv8c3/42Z7RS03QuBwzk5uTfnprWSBqPoTxBu3Lv/4OHmo97jJ0+3tvvPdo5N1WgBU1GpSs9SbkDJEqYoUcGs1sCLVMFJevG51U8uQRtZlT9wWcOi4KelzKXg6Kmk/4spQHYJghUcz9K8t8euZAYoVQa25e1H537aIe47ekiZ8i9nnK6Eby6xkaMv6TCmr2+kfcpyzcWNNbHyvLM7y0xTJOfrJNdj1/TMvaJrBmCul/QH0ShaFb0L4g4MSFdHSf83yyrRFFCiUNyYeRzVuLBcoxQKfMfGQM3FBT+FuYclL8As7CpRR/c8k9G80v6USFfsvw7LC2OWRepvtrmZ21pLrtPmDebvF1aWdYNQiutGeaMoVrRdD82kBoFq6QEXWvpZqTjjPlH0S2xDiG9/+S44fjOKx6O338eDyacujk3ynLwgQxKTd2RCvpAjMiUi2ArGwWHwIdwND8JJ2N0Ng86zS/6r8Otf9HrI3Q==</latexit>
Combining intrinsic and implicit graph structures
Figure 10: Overall illustration of dynamic graph construction approaches. Dashed lines (in data
points on left) indicate the optional intrinsic graph topology.
In order to tackle the above challenges, recent attempts on GNN for NLP (Chen et al., 2020f,g;
Liu et al., 2021a, 2019a) have explored dynamic graph construction without resorting to human
efforts or domain expertise. Most dynamic graph construction approaches aim to dynamically learn
the graph structure (i.e., a weighted adjacency matrix) on the ﬂy, and the graph construction mod-
ule can be jointly optimized with the subsequent graph representation learning modules toward the
downstream task in an end-to-end manner. One good example of dynamic graph construction is
when constructing a graph capturing the semantic relationships among all the words in a text pas-
sage in the task of conversational machine reading comprehension (Reddy et al., 2019), instead of
building a ﬁxed static graph based on domain expertise, one can jointly train a graph structure learn-
ing module together with the graph embedding learning module in order to learn an optimal graph
structure considering not only the semantic meanings of the words but also the conversation history
and current question.
As shown in Fig. 10, these dynamic graph construction approaches typically consist of a graph
similarity metric learning component for learning an adjacency matrix by considering pair-wise
node similarity in the embedding space, and a graph sparsiﬁcation component for extracting a sparse
graph from the learned fully-connected graph. It is reported to be beneﬁcial to combine the intrinsic
graph structures and learned implicit graph structures for better learning performance (Li et al.,
2018c; Chen et al., 2020f; Liu et al., 2021a). Moreover, in order to effectively conduct the joint
graph structure and representation learning, various learning paradigms have been proposed. In
what follows, we will discuss all these effective techniques for dynamic graph construction. More
broadly speaking, graph structure learning for GNNs itself is a trending research problem in the
machine learning ﬁeld, and has been actively studied beyond the NLP community (Li et al., 2018c;
Norcliffe-Brown et al., 2018; Velickovic et al., 2020; Kalofolias and Perraudin, 2019; Franceschi
23





LINGFEI WU AND YU CHEN , ET AL .
et al., [n.d.]). However, in this survey, we will focus on its recent advances in the NLP ﬁeld. We
hereafter use dynamic graph construction and graph structure learning interchangeably.
4.2.1 G RAPH SIMILARITY METRIC LEARNING TECHNIQUES
Based on the assumption that node attributes contain useful information for learning the implicit
graph structure, recent work has explored to cast the graph structure learning problem as the prob-
lem of similarity metric learning deﬁned upon the node embedding space. The learned similarity
metric function can be later applied to an unseen set of node embeddings to infer a graph struc-
ture, thus enabling inductive graph structure learning. For data deployed in non-Euclidean domains
like graphs, the Euclidean distance is not necessarily the best metric for measuring node similar-
ity. Various similarity metric functions have been proposed for graph structure learning for GNNs.
According to the types of information sources utilized, we group these metric functions into two cat-
egories: Node Embedding Based Similarity Metric Learning and Structure-aware Similarity Metric
Learning.
Node Embedding Based Similarity Metric Learning Node embedding based similarity metric
functions are designed to learn a weighted adjacency matrix by computing the pair-wise node sim-
ilarity in the embedding space. Common metric functions include attention-based metric functions
and cosine-based metric functions.
Attention-based Similarity Metric Functions. Most of the similarity metric functions proposed
so far are based on the attention mechanism (Bahdanau et al., 2015; Vaswani et al., 2017). In order
to increase the learning capacity of dot product based attention mechanism, Chen et al. (2020e)
proposed a modiﬁed dot product by introducing learnable parameters, formulated as follows:
Si,j = (⃗ vi⊙ ⃗ u)T ⃗ vj (19)
where ⃗ uis a non-negative weight vector learning to highlight different dimensions of the node
embeddings, and⊙ denotes element-wise multiplication.
Similarly, Chen et al. (2020g) designed a more expressive version of dot product by introducing
a learnable weight matrix, formulated as follows:
Si,j = ReLU( ⃗W ⃗ vi)T ReLU( ⃗W ⃗ vj) (20)
where ⃗W is a d×d weight matrix, andReLU(x) = max(0, x) is a rectiﬁed linear unit (ReLU) (Nair
and Hinton, 2010) used to enforce the sparsity of the similarity matrix.
Cosine-based Similarity Metric Functions. Chen et al. (2020f) extended the vanilla cosine simi-
larity to a multi-head weighted cosine similarity to capture pair-wise node similarity from multiple
perspectives, formulated as follows:
Sp
i,j = cos( ⃗ wp⊙ ⃗ vi, ⃗ wp⊙ ⃗ vj)
Si,j = 1
m
m∑
p=1
Sp
ij
(21)
where ⃗ wp is a weight vector associated to the p-th perspective, and has the same dimension as the
node embeddings. Intuitively, Sp
i,j computes the pair-wise cosine similarity for the p-th perspective
where each perspective considers one part of the semantics captured in the embeddings. Besides
increasing the learning capacity, employing multi-head learners is able to stabilize the learning
process, which has also been observed in (Vaswani et al., 2017; Velickovic et al., 2018).
24





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
Structure-aware Similarity Metric Learning Inspired by structure-aware transformers (Zhu
et al., 2019b; Cai and Lam, 2020b), recent approaches employ structure-aware similarity metric
functions that additionally consider the existing edge information of the intrinsic graph beyond the
node information. For instance, Liu et al. (2019a) proposed a structure-aware attention mechanism
for learning pair-wise node similarity, formulated as follows:
Sl
i,j = softmax(⃗ uT tanh( ⃗W [⃗hl
i, ⃗hl
j, ⃗ vi, ⃗ vj, ⃗ ei,j])) (22)
where ⃗ vi represents the embedding of node i, ⃗ ei,j represents the embedding of the edge connecting
node i and j, ⃗hl
i is the embedding of node i in the l-th GNN layer, and ⃗ uand ⃗W are trainable weight
vector and weight matrix, respectively.
Similarly, Liu et al. (2021a) introduced a structure-aware global attention mechanism, formu-
lated as follows,
Si,j = ReLU( ⃗WQ⃗ vi)T (ReLU( ⃗WK⃗ vi) + ReLU( ⃗WR⃗ ei,j))√
d
(23)
where ⃗ ei,j is the embedding of the edge connecting node i and j, and ⃗WQ, ⃗WK, and ⃗WR are linear
transformations that map the node and edge embeddings to the latent embeddding space.
4.2.2 G RAPH SPARSIFICATION TECHNIQUES
Most graphs in real-world scenarios are sparse graphs. Similarity metric functions consider relations
between any pair of nodes and returns a fully-connected graph, which is not only computationally
expensive but also might introduce noise such as unimportant edges. Therefore, it can be beneﬁcial
to explicitly enforce sparsity to the learned graph structure. Besides applying the ReLU function in
the similarity metric functions (Chen et al., 2020g; Liu et al., 2021a), various graph sparsiﬁcation
techniques have been adopted to enhance the sparsity of the learned graph structure.
Chen et al. (2020g,e) applied a kNN-style sparsiﬁcation operation to obtain a sparse adjacency
matrix from the node similarity matrix computed by the similarity metric learning function, formu-
lated as follows:
⃗Ai,: = topk(⃗Si,:) (24)
where for each node, only the K nearest neighbors (including itself) and the associated similarity
scores are kept, and the remaining similarity scores are masked off.
Chen et al. (2020f) enforced a sparse adjacency matrix by considering only the ε-neighborhood
for each node, formulated as follows:
Ai,j =
{ Si,j Si,j > ε
0 otherwise (25)
where those elements in S which are smaller than a non-negative thresholdε are all masked off (i.e.,
set to zero).
Besides explicitly enforcing the sparsity of the learned graph by applying certain form of thresh-
old, sparsity has also been enforced implicitly in a learning-based manner. Chen et al. (2020f)
introduced the following regularization term to encourage sparse graphs.
1
n2||A||2
F (26)
where||·|| F denotes the Frobenius norm of a matrix.
25





LINGFEI WU AND YU CHEN , ET AL .
4.2.3 C OMBINING INTRINSIC GRAPH STRUCTURES AND IMPLICIT GRAPH STRUCTURES
Recent studies (Li et al., 2018c; Chen et al., 2020f; Liu et al., 2021a) have shown that it could hurt the
downstream task performance if the intrinsic graph structure is totally discard while doing dynamic
graph construction. This is probably because the intrinsic graph typically still carries rich and
useful information regarding the optimal graph structure for the downstream task. They therefore
proposed to combine the learned implicit graph structure with the intrinsic graph structure based on
the assumption that the learned implicit graph is potentially a “shift” (e.g., substructures) from the
intrinsic graph structure which is supplementary to the intrinsic graph structure. The other potential
beneﬁt is incorporating the intrinsic graph structure might help accelerate the training process and
increase the training stability. Since there is no prior knowledge on the similarity metric and the
trainable parameters are randomly initialized, it may usually take long time to converge.
Different ways for combining intrinsic and implicit graph structures have been explored. For
instance, Li et al. (2018c); Chen et al. (2020f) proposed to compute a linear combination of the nor-
malized graph Laplacian of the intrinsic graph structure L(0) and the normalized adjacency matrix
of the implicit graph structure f(A), formulated as follows:
˜A = λL(0) + (1− λ)f(A) (27)
where f : Rn×n→ Rn×n can be arbitrary normalization operations such as graph Laplacian oper-
ation (Li et al., 2018c) and row-normalization operation (Chen et al., 2020f). Instead of explicitly
fusing the two graph adjacency matrices, Liu et al. (2021a) proposed a hybrid message passing
mechanism for GNNs which fuses the two aggregated node vectors computed from the intrinsic
graph and the learned implicit graph, respectively, and then feed the fused vector to a GRU to
update node embeddings.
4.2.4 L EARNING PARADIGMS
Most existing dynamic graph construction approaches for GNNs consist of two key learning com-
ponents: graph structure learning (i.e., similarity metric learning) and graph representation learning
(i.e., GNN module), and the ultimate goal is to learn the optimized graph structures and representa-
tions with respect to certain downstream prediction task. How to optimize the two separate learning
components toward the same ultimate goal becomes an important question. Here we highlight three
representative learning paradigms. The most straightforward strategy (Chen et al., 2020g,e; Liu
et al., 2021a) is to jointly optimize the whole learning system in an end-to-end manner toward the
downstream (semi-)supervised prediction task. Another common strategy (Yang et al., 2018b; Liu
et al., 2019a; Huang et al., 2020a) is to adaptively learn the input graph structure to each stacked
GNN layer to reﬂect the changes of the intermediate graph representations. This is similar to how
transformer models learn different weighted fully-connected graphs in each layer. Unlike the above
two paradigms, Chen et al. (2020f) proposed an iterative graph learning framework by learning a
better graph structure based on better graph representations, and in the meantime, learning better
graph representations based on a better graph structure in an iterative manner. As a result, this iter-
ative learning paradigm repeatedly reﬁnes the graph structure and the graph representations toward
the optimal downstream performance.
26





---

## Part 3 — Graph Representation Learning for NLP (Section 5, pp. 27–42)


GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
5. Graph Representation Learning for NLP
In the previous section, we have presented various graph construction methods, including static
graph construction and dynamic graph construction. In this section, we will discuss various graph
representation learning techniques that are directly operated on the constructed graphs for various
NLP tasks. The goal of graph representation learning is to ﬁnd a way to incorporate informa-
tion of graph structures and attributes into a low-dimension embeddings via a machine learning
model (Hamilton et al., 2017b). To mathematically formalize this problem, we give the mathe-
matical notations for arbitrary graphs asG(V,E,T ,R), whereV is the node set,E is the edge set,
T ={T1, T2, ..., Tp} is the collection of node types, andR ={R1, ..., Rq} is the collection of edge
types.|·| is the number of elements. τ(·)∈T is the node type indicator function (e.g., τ(vi)∈T
is the type of node vi), and φ(·)∈R is the edge type indicator function (e.g., φ(ei,j)∈R is the
type of edge ei,j), respectively.
Generally speaking, the constructed graphs from the raw text data are either homogeneous or
heterogeneous graphs. Thus, in Section 5.1, we will discuss various graph representation learn-
ing methods for homogeneous graphs, including scenarios for the original homogeneous graph and
some converting from heterogeneous graphs. In Section 5.2, we will discuss the GNN-based meth-
ods for multi-relational graphs, and in Section 5.3, we will discuss the GNNs for dealing with the
heterogeneous graphs.
5.1 GNNs for Homogeneous Graphs
By deﬁnition, a graphG(V,E,T ,R), s.t.|T| = 1 ,|R| = 1 is called homogeneous graph. Most
graph neural networks such as GCN, GAT, and GraphSage are designed for homogeneous graphs,
which, however, can not ﬁt well in many NLP tasks. For example, given a natural language text,
the constructed dependency graph is arbitrary graph that contains multiple relations, which cannot
be exploited by traditional GNN methods directly. Thus, in this subsection, we will ﬁrst discuss the
various strategies for converting arbitrary graphs to homogeneous graphs, including static graphs
and dynamic graphs. Then, we will discuss the graph neural networks considering bidirectional
encoding.
5.1.1 S TATIC GRAPH : T REATING EDGE INFORMATION AS CONNECTIVITY
GNNs for dealing with the static graphs normally consists of two stages, namely, converting edge
information and node representation learning, as described in the following.
Converting Edge Information to Adjacent Matrix Basically, the edges are viewed as the con-
nection information between nodes. In this case, it is normal to discard the edge type information
and retain the connections to convert the heterogeneous graphs (Yang et al., 2019; Zhang et al.,
2019b; Yao et al., 2019a; Wu et al., 2019a; Li et al., 2019) to homogeneous graphs. After obtaining
such a graph, we can represent the topology of the graph as a uniﬁed adjacency matrix A. Specif-
ically, for an edge ei,j ∈ Ewhich connect node vi and vj, Ai,j denotes to the edge weight for
weighted static graph, or Ai,j = 1 for unweighted connections and Ai,j = 0 otherwise. The static
graphs can also be divided into directed and undirected graphs. For the undirected case, the adja-
cency matrix is symmetric matrix, which meansAi,j = Aj,i. And for the other case, it is always not
symmetric. The Ai,j is strictly deﬁned by the edge from node vi to node vj. It is worth noting that
the directed graphs can be transformed to undirected graphs (Yasunaga et al., 2017) by averaging
27





LINGFEI WU AND YU CHEN , ET AL .
the edge weights in both directions. The edge weights are rescaled, whose maximum edge weight
is 1 before feeding to the GNN.
Node Representation Learning Next, given initial node embedding X and adjacency matrix
A, the node representation is extracted base on the classical GNNs techniques. For undirected
graphs, most works (Liu et al., 2019d; Wang et al., 2018; Yao et al., 2019a; Zhang et al., 2020e)
mainly adopt graph representation learning algorithms such as GCN, GGNN, GAT, GraphSage,
etc. and stack them to explore deep semantic correlations in the graph. When it comes to the
directed graphs, few GNN methods such as GGNN, GAT still work (Chen et al., 2020e; Wang
et al., 2020g; Qiu et al., 2019; Yan et al., 2019; Ji et al., 2019; Sui et al., 2019). While for the
other GNNs that can not be directly applied into directed graphs, the simple strategy is to ignore the
directions (i.e., converting the directed graphs to undirected graphs) (Yasunaga et al., 2017; Wang
et al., 2018; Liu et al., 2019d). However, such methods allow the message to propagate in both
directions without constraints. To solve this problem, many efforts have been made to adapt the
GNN to directed graphs. For GCN, some spatial-based GCN algorithms are designed for directed
graphs such as DCNN (Atwood and Towsley, 2016). GraphSage can be easily extended to directed
graphs by modifying the aggregation function via specifying the edge directions and aggregating
them separately) (Xu et al., 2018b).
5.1.2 D YNAMIC GRAPH
Dynamic graphs that aim to learn the graph structure together with the downstream task jointly are
widely adopted by graph representation learning (Chen et al., 2020g,e,f; Hashimoto and Tsuruoka,
2017; Guo et al., 2019a). Early works mainly adopt the recurrent network by treating the graph node
embeddings as RNN’s state encodings (Hashimoto and Tsuruoka, 2017), which can be regarded as
the rudiment of GGNN. Then the classic GNNs such as GCN (Guo et al., 2019a), GAT (Cui et al.,
2020a), GGNN (Chen et al., 2020g,e) are utilized to learn the graph embedding effectively. Recent
researchers adopt attention-based or metric learning-based mechanisms to learn the implicit graph
structure (i.e., the graph adjacency matrixA) from unstructured texts. The learning process of graph
structure is jointly with the downstream tasks via an end-to-end fashion (Shaw et al., 2018; Chen
et al., 2020e; Luan et al., 2019; Chen et al., 2020g).
5.1.3 G RAPH NEURAL NETWORKS : B IDIRECTIONAL GRAPH EMBEDDINGS
In the previous sub-sections, we present the typical techniques for constructing and learning node
embeddings from the static homogeneous graphs. In this subsection, we provide a detailed discuss
on how to handle the edge directions. In reality, many graphs are directed acyclic graphs (DAG) (Cai
and Lam, 2020b), which information is propagated along the speciﬁc edge direction. However, some
researchers allow the information propagate equally in both directions (Yasunaga et al., 2017; Wang
et al., 2018; Liu et al., 2019d) and others discard the information containing in outgoing edges (Yan
et al., 2019; Wang et al., 2020g; Qiu et al., 2019; Ji et al., 2019; Sui et al., 2019), both of which will
lose some important structure information for the ﬁnal representation learning.
To deal with this, bidirectional graph neural network (bidirectional GNN) is proposed to learn
the node representation from both incoming and outgoing edges in a interleaved fashion. To in-
troduce different variants of bidirectional GNN, we ﬁrst give some uniﬁed mathematical notations.
For a speciﬁc node vi∈V in the graphG(V,E) and its neighbor nodes N(vi) (i.e. any node vj
28





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
satisfy ei,j ∈E or ej,i∈E ), we deﬁne the incoming (backward) nodes set as N⊣(vi) satisfying
ej,i∈E , vj∈ N⊣(vi) and outgoing (forward) nodes set as N⊢(vi) holding ei,j∈E , vj∈ N⊢(vi).
Xu et al. (2018b) ﬁrstly extend the GraphSage to a bi-directional version by calculating the
graph embedding separately for each direction and combine them at last. At each computation hop,
for each node in the graph, they aggregate the incoming nodes and outgoing nodes separately to get
backward and forward immediate-aggregated representation as follows:
h(k)
i,⊣ = σ(W(k)· f⊣
k (h(k−1)
i,⊣ ,{h(k−1)
j,⊣ ,∀vj∈ N⊣(vi)})),
h(k)
i,⊢ = σ(W(k)· f⊢
k (h(k−1)
i,⊢ ,{h(k−1)
j,⊢ ,∀vj∈ N⊢(vi)})),
(28)
where k∈{ 1, 2, ..., K} denotes the layer number, and h(k)
i,⊣ , h(k)
i,⊢ denote the backward and forward
aggregated results respectively. At the ﬁnal step, the ﬁnal forward and backward representation is
concatenated to calculate the ﬁnal bi-directional representation.
Although works effectively, the bidirectional GraphSage learns both directions separately. To
this end, Chen et al. (2020g) proposes the bidirectional GGNN to address this issue. Technically,
at each iteration, after obtaining aggregated vector representations h(k)
i,⊢ , h(k)
i,⊣, they opt to fuse them
into one vector as follows:
h(k)
N(vi) = Fuse(h(k)
i,⊢ , h(k)
i,⊣), (29)
where the function Fuse(·,·) is the gated sum of two information sources:
Fuse(a, b) = z⊙ a + (1− z)⊙ b, z = σ(Wz[a, b, a⊙ b, a− b] + bz) (30)
where a∈ Rd, b∈ Rd are inputs, Wz∈ Rd×4d, bz∈ Rd are learnable weights and σ(·) is the
sigmoid function. Then, a Gated Recurrent Unit (GRU) is used to update the node embeddings by
incorporating the aggregation information as follows:
h(k)
i = GRU(h(k−1)
i , h(k)
N(vi)). (31)
Unlike previous methods, which are specially designed for the speciﬁc GNN methods, Ribeiro
et al. (2019b) further proposes a general bidirectional GNN framework, which can be easily applied
to most existing GNNs. Technically, they ﬁrst encode the graph in two directions:
h(k)
i,⊣ = GNN(h(k−1)
i ,{h(k−1)
j :∀vj∈ N⊣(vi)}),
h(k)
i,⊢ = GNN(h(k−1)
i ,{h(k−1)
j :∀vj∈ N⊢(vi)}),
(32)
where GNN(·) can denote to any variant of GNNs. Similar to strategy in the bidirectional RNNs (Schus-
ter and Paliwal, 1997), they learn the forward and backward directions separately and concatenate
them together with the original node feature as follows:
h(k)
i = [h(k)
i,⊣ , h(k)
i,⊢ , h(k−1)
i ]. (33)
They stack several layers to achieve better performance. At last, theh(K)
i is employed in a sequence
input of a Bi-LSTM in depth-ﬁrst order to the ﬁnal node representation.
29





LINGFEI WU AND YU CHEN , ET AL .
5.2 Graph Neural Networks for Multi-relational Graphs
In practice, many graphs have various edge types, such as knowledge graph, AMR graph, etc.,
which can be formalized as multi-relational graphs. Formally, for a graph G, s.t. |T| = 1 and
|R| > 1 is deﬁned as multi-relational graphs. In this section, we introduce different techniques for
representing and learning the multi-relational graphs. Speciﬁcally, in Section. 5.2.1, we will discuss
the formalization for the multi-relational graphs from an original heterogeneous graph. In Section.
5.2.2 and 5.2.3, we will discuss the basic graph representation learning methods and transformers
for relational heterogeneous, respectively (we denote it as multi-relational graph neural network for
simpliﬁcation).
5.2.1 M ULTI-RELATIONAL GRAPH FORMALIZATION
Since heterogeneous graphs are commonly observed in NLP domian, such as knowledge graph,
AMR graph, etc, most of the researchers (Guo et al., 2019b; Ribeiro et al., 2019b; Beck et al.,
2018a; Damonte and Cohen, 2019; Koncel-Kedziorski et al., 2019) propose to convert it to a multi-
relational graph, which can be learned by relational GNN in Section. 5.2.2 and Section. 5.2.3.
As deﬁned before, the multi-relational graph is denoted as G(V,E,T ,R), s.t. |T| = 1 and
|R| >= 1. To get the multi-relational graph, technically, they ignore node types (i.e., project the
nodes to the uniﬁed embedding space regardless of original nodes or relational nodes). As for edges,
they assign the initial edges with the type ”default”. For each edge ei,j, they add a reverse edge ej,i
with type ”reverse”. Besides, for each node vi, they add the self-loops with the type ”self”. Thus
the converted graph is the multi-relational graph with|E| = 3 and|V| = 1.
5.2.2 M ULTI-RELATIONAL GRAPH NEURAL NETWORKS
The multi-relational GNN is the extension of classic GNN for multi-relational graphs, which has the
same node type but different edge types. They are originally introduced to encode relation-speciﬁc
graphs such as knowledge graphs (Schlichtkrull et al., 2018; Malaviya et al., 2020) and parsing
graphs (Beck et al., 2018a; Song et al., 2019), which have complicated relationships between nodes
with the same type. Generally, most multi-relational GNNs employ type-speciﬁc parameters to
model the relations individually. In this subsection, we will introduce the classic relational GCN (R-
GCN) (Schlichtkrull et al., 2018), relational GGNN (R-GGNN) (Beck et al., 2018a) and relational
GAT (R-GAT) (Wang et al., 2020c,h).
R-GCN The R-GCN (Schlichtkrull et al., 2018) is explicitly developed to handle highly multi-
relational graphs, especially knowledge bases. The R-GCN is a natural extension of the message-
passing GCN framework (Gilmer et al., 2017) which operates on local graph neighborhoods. They
group the incoming nodes according to the label types and then apply messaging passing separately.
Thus, the aggregation of node vi’s immediate neighbor nodes is deﬁned as
h(k)
i = σ(
∑
r∈E
∑
vj∈Nr(vi)
1
ci,r
W(k)
r h(k−1)
j + W(k)
0 h(k−1)
i ), (34)
where W(k)
r ∈ Rd×d, W(k)
0 ∈ Rd×d are trainable parameters, Nr(vi) is the neighborhoods of node
vi with relation r∈E , ci,r is the problem-speciﬁc normalization scalar such as|Nr(vi)|, and σ(·)
is the ReLU activation function. Intuitively, such a step projects neighbor nodes with different
30





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
relations by relation-speciﬁc transformation to uniﬁed feature space and then accumulates them
through a normalized sum. The self-connection with a special relation type is added to ensure the
node itself feature can be held.
However, modeling the multi-relations using separate parameters for each relation can lead to
severe over-parameterization, especially on the rare relations. Thus two regularization methods:
basis and basis-diagonal-decomposition are proposed to address this issue. Firstly, for basis de-
composition, each relation weight W(k)
r is deﬁned as follows:
W(k)
r =
B∑
b=1
a(k)
rb V(k)
b , (35)
where V(k)
b ∈ Rd×d is the basis anda(k)
rb is the associated coefﬁcients. This strategy actually regards
the relation matrices as the linear combination of shared basis, which can be seen as a form of weight
sharing between different relations.
In the basis-diagonal decomposition, each W(k)
r is deﬁned through the direct sum over a set of
low-dimensional matrices as
W(k)
r =
B⨁
b=1
Q(k)
br , (36)
where Q(k)
br ∈ Rd/B×d/B is the low-dimensional matrix. Thereby, the W(k)
r is represented by a
set of sub matrices as diag(Q(k)
1r , Q(k)
2r , ...,Q(k)
Br). This strategy can be seen as a matrix sparsity
constraint. It holds the hypothesis that the latent features can be represented by sets of variables that
are more tightly coupled within groups than across groups.
There are also some other GCN-based multi-relational graph neural networks for different pur-
poses. For example, Directed-GCN (Marcheggiani and Titov, 2017) is developed to exploit the
syntactic graph, which has massive and unbalanced relations. The basic idea of incorporating
edge-type information is similar to the R-GCN (Schlichtkrull et al., 2018), but they solve the over-
parameterization issue by sharing projection matrix weights for all edges with the same directions
but only keeping the relation-speciﬁc biases. The other example is weighted-GCN (Shang et al.,
2019), which adopt relation-speciﬁc transformation to learn relational information. The weighted-
GCN learns the weight score for each relation type end-to-end and inject it into the GCN framework.
In this way, the weighted-GCN is capable of controlling how much information each type con-
tributes to the aggregation procedure. As a combination model, the Comp-GCN (Vashishth et al.,
2019) generalizes several of the existing multi-relational GCN methods (i.e., R-GCN (Schlichtkrull
et al., 2018), Weighted-GCN (Shang et al., 2019) and Directed-GCN (Marcheggiani and Titov,
2017)) and jointly learn the nodes and relations representation.
R-GGNN The relational GGNN (Beck et al., 2018a) is originally developed for the graph-to-
sequence problem. It is capable of capturing long-distance relations. Similarly to R-GCN, R-GGNN
uses relation-speciﬁc weights to capture relation-speciﬁc correlations between nodes better. Thus,
31





LINGFEI WU AND YU CHEN , ET AL .
the propagation process of R-GGNN can be summarized as
r(k)
i = σ(
∑
vj∈N(vi)
1
cvi,r
Wr
φ(ei,j)h(k−1)
j + br
φ(ei,j)),
z(k)
i = σ(
∑
vj∈N(vi)
1
cvi,z
Wz
φ(ei,j)h(k−1)
j + bz
φ(ei,j)),
˜h(k)
i = ρ(
∑
vj∈N(vi)
1
cvi
Wφ(ei,j)(r(k)
j ⊙ h(k−1)
i ) + bφ(ei,j)),
h(k)
i = (1− z(k)
i )⊙ h(k−1)
i + z(k)
i ⊙ ˜h(k)
i ,
(37)
where Wr/z/·
φ(ei,j)∈ Rd×d, br/z/·
φ(ei,j) are trainable relation-speciﬁc parameters,σ(·) is the sigmoid func-
tion, cvi,r/z/· =|N(vi)|, and ρ(·) is the non-linear activation function such as tanh and ReLU.
R-GAT Wang et al. (2020c,h) propose to extend the classic GAT to ﬁt the multi-relational graphs.
In this section, we will discuss two R-GAT variants. Intuitively, neighbor nodes with different
relations should have different inﬂuences.
Wang et al. (2020c) propose to extend the homogeneous GAT with additional relational heads.
Technically, they propose the relational node representation as
h(k),m
i,rel =
∑
vj∈N(vi)
β(k),m
ij W(k),mh(k−1)
j (38)
where m∈ [1, M] is the m−th head and β(k),m
ij is the corresponding attention score for relation
head m, which is calculated as
s(k),m
ij = f(ei,j),
β(k),m
ij = softmaxj(s(k),m
ij ),
(39)
where s(k),m
ij is the similarity between node vi and vj, and f(·) : Rdk
→ R is the multi-layer trans-
formation (MLP) with non-linearity. The relational representation of node vi is the concatenation
with linear transformation of M heads’ results as:
h(k)
i,rel = g(||M
m=1h(k),m
i,rel ), (40)
where|| denotes the vector concatenation operation andg(·) : Rm×dk
→ Rdk
is the liner projection.
Thus, the ﬁnal node representation is the combination ofh(k)
i,rel and h(k)
i,att as follows:
h(k)
i = σ(W(k)(h(k)
i,rel||h(k)
i,att) + b(k)), (41)
where W(k)∈ Rd×d, b(k)∈ Rd are trainable parameters, σ(·) is the ReLU activation function.
Unlike the work by Wang et al. (2020c), which learn and fuse the relation-speciﬁc node embed-
ding regarding each type of edges, Wang et al. (2020h) develops a relation-aware attention mecha-
nism to calculate the attention score α(k),m
ij as
α(k),m
ij = softmaxj(s(k),m
ij ),
s(k),m
ij = σ(f (k),m([W(k),mh(k−1)
i ; W(k),mh(k−1)
j ; e(k−1)
i,j ])),
(42)
32





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
where W(k),m ∈ Rd×d is the learnable matrix, and f(·)(k),m : R3×d → R is the single linear
projection layer. They learn a global representation for each relation type r = φ(ei,j)∈R . Techni-
cally, for all edges with type r∈R , two node sets Sr and Tr. Sr are collected regarding the source
and target node set of relation r, respectively. Thus the edge type embedding tr can be calculated
by:
er =|
∑
o∈Sr Who
|Sr| −
∑
o∈Tr Who
|Tr| |. (43)
Thus the edge representation is the absolute difference between mean vectors of source and target
nodes connected by edges whose type are r.
Gating Mechanism The multi-relational graph neural networks also face the over-smoothing
problem when stacking several layers to exploit implicit correlations between distant neighbors
(i.e., not directly connected) (Tu et al., 2019a). To solve this, the gating mechanism, which com-
bines the nodes’ input features and aggregated features by gates, is introduced to the multi-relational
graph neural network (Tang et al., 2020b; De Cao et al., 2018; Tu et al., 2019a; Cao et al., 2019b).
Intuitively, the gating mechanism can be regarded as a trade-off between the original signals and the
learned information. It regulates how much of the update message that are propagated to the next
step, thus preventing the model from thoroughly overwriting the past information. Here we intro-
duce the gating mechanism by taking the classic R-GCN (Schlichtkrull et al., 2018) as an example,
which actually can be extended to arbitrary variants.
We denote the representation before activation σ(·) as
u(k)
i = f (k)(h(k−1)
i ), (44)
where f denotes to the aggregation function. Ultimately, the ﬁnal representation of node i’s rep-
resentation is a gated combination of the previous embedding hk
i and GNN output representation
σ(uk
i ) as:
h(k)
i = σ(u(k)
i )⊙ g(k)
i + h(k−1)
i ⊙ (1− g(k−1)
i ) (45)
where gk
i is the gating vectors, and σ(·) is often the tanh(·) function. The gating vectors are calcu-
lated by both the inputs and outputs as follows:
g(k)
i = σ(f (k)([u(k)
i , h(k−1)
i ])) (46)
where σ is the sigmoid activation function, and f (k)(·) : R2d→ R is the linear transformation. We
repeat calculating g(k)
i for d times to get the gating vector g(k)
i .
5.2.3 G RAPH TRANSFORMER
The transformer architecture (Vaswani et al., 2017) has achieved great success in NLP ﬁelds. Roughly
speaking, the transformer’s self-attention mechanism is a special procedure of fully connected im-
plicit graph learning, as we discussed in sec. 4.2.1, thus bridging the concept of GNN and trans-
former. However, the traditional transformer fails to leverage structure information. Inspired by
GAT (Velickovic et al., 2018), which combines the message passing with attention mechanism,
much literature incorporates structured information to the transformer (we name it as graph trans-
former) by developing structure-aware self-attention mechanism (Yao et al., 2020; Levi, 1942; Xiao
33





LINGFEI WU AND YU CHEN , ET AL .
et al., 2019; Zhu et al., 2019a; Cai and Lam, 2020b; Wang et al., 2020d). In this section, we will
discuss the techniques of structure-aware self-attention for the multi-relational graph.
As a preliminary knowledge, here we give a brief review of self-attention. To make it clear, we
omit the multi-head mechanism and only present the self-attention function. Formally, we denote
the input of self-attention as Q ={q1, q2, ...,qm}∈ Rm×dq
, K ={k1, k2, ...,kn}∈ Rn×dk
, V =
{v1, v2, ...,vn}∈ Rn×dv
. Then the output representation zi is calculated as
zi = Attention(qi, K, V) =
n∑
j=1
αi,jWvvj (47)
αi,j = softmaxj(ui,j) (48)
ui,j = (Wqqi)T (Wkkj)√
d
(49)
where Wq ∈ Rd×dq
, Wk ∈ Rd×dk
, Wv ∈ Rd×dv
are trainable parameters, and d is the model
dimension. Note that for graph transformer, the query, key and value all refer to the nodes’ embed-
ding:, namely, qi = ki = vi = hi. Thus, we will only use hi to represent query, key and value
considering simpliﬁcation in the following contents.
There are various graph transformers for relation graphs that incorporate the structure knowl-
edge, which can be categorized into two classes according to the self-attention function. One class
is the R-GAT-based methods which adopt relational GAT-like feature aggregation. Another class
reserves the fully connected graph while incorporating the structure-aware relation information to
the self-attention function.
R-GAT Based Graph Transformer. The GAT-based graph transformer (Yao et al., 2020) adopts
the GAT-like feature aggregation, which leverages the graph connectivity inductive bias. Techni-
cally, they ﬁrst aggregate neighbors with type-speciﬁc aggregation step and then fuse them through
feed-forward layer as follows:
zr,(k)
i =
∑
vj∈Nr(vi)
αk
i,jWv,(k)h(k−1)
j , r∈E
h(k)
i = FFN(k)(WO,(k)[zR1,(k)
i , ...,zRq,(k)
i ]),
(50)
where FFN (k)(·) denotes the feed-forward layer in transformer (Vaswani et al., 2017), and αi,j
denotes the dot-product score in eq. 49.
To incorporate the bi-directional information, Wang et al. (2020d) learns forward and backward
aggregation representation in graph transformer. Speciﬁcally, given the backward and forward fea-
tures (i.e., hi,⊢ and hi,⊣) for node vi, the backward aggregated featurez(k)
i,⊣ for node vi is formulated
by:
z(k)
i,⊣ =
∑
vj∈N⊣(vi)
αi,jWv,(k)a(k)
i,j ,
a(k)
i,j = f (k)([hi,⊢, ei,j; hj,⊣]),
(51)
34





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
where f (k)(·) : R3×d→Rd
is the linear transformation, and αi,j is the softmax score of incoming
neighbors’ dot-production results ui,j which can be formulated by:
ui,j =
(Wq,(k)hi,⊣)T (Wk,(k)a(k)
i,j )
√
d
. (52)
Then they adopt the gating mechanism to fuse bidirectional aggregated features to get the packaged
node representation:
g(k)
i = σ(f′k([z(k)
i,⊢; z(k)
i,⊣])),
p(k)
i = g(k)
i ⊙ z(k)
i,⊢ + (1− g(k)
i )⊙ z(k)
i,⊣
(53)
where f′(·) : R2×d → Rd, and σ(·) is the sigmoid activation function. They calculate the the
forward and backward node representation based on the packaged representation, respectively:
[o(k)
i,⊢ , o(k)
i,⊣] = FFN(k)(p(k)
i ),
h(k)
i,⊢ = LayerNorm(k)(o(k)
i,⊢ + h(k−1)
i,⊢ ),
h(k)
i,⊣ = LayerNorm(k)(o(k)
i,⊣ + h(k−1)
i,⊣ ),
(54)
where FFN(·) : Rd→ R2×d is the feed-forward function, and LayerNorm (·) is the layer normal-
ization (Ba et al., 2016). The ﬁnal node representation is the concatenation of the last layer K’s
bidirectional representations:
h(K)
i = f′′K([h(K)
i,⊢ , h(K)
i,⊣ ]), (55)
where f′′(K)(·) : R2×d→ Rd is the linear transformation.
Structure-aware Self-attention Based Graph Transformer. Unlike the R-GAT-based graph trans-
former, which purely relies on the given graph structure as connectivity, the structure-aware self-
attention-based graph transformer reserves the original self-attention architecture, allowing non-
neighbor nodes’ communication. We will ﬁrstly discuss the structure-aware self-attention mecha-
nism and then present its unique edge embedding representation.
Shaw et al. (2018) ﬁrstly attempts to model the relative relations between words (nodes) in the
neural machine translation task. Technically, they consider the relation embedding when calculating
node-wise similarity in eq. 49 as follows:
u(k)
i,j =
(Wq,(k)h(k−1)
i )T (Wk,(k)h(k−1)
j ) + (Wq,(k)h(k−1)
i )Tei,j
√
d
. (56)
Motivated by Shaw et al. (2018), Xiao et al. (2019); Zhu et al. (2019a) propose to extend the
conventional self-attention architecture to explicitly encode the relational embedding between nodes
pairs in the latent space as
u(k)
i,j =
(Wq,(k)h(k−1)
i )T (Wk,(k)h(k−1)
j + Wr,(k)ei,j)
√
d
,
h(k)
i =
n∑
j=1
αk
i,j(Wv,(k)h(k−1)
j + Wf,(k)ei,j).
(57)
35





LINGFEI WU AND YU CHEN , ET AL .
To adopt the bidirectional relations, Cai and Lam (2020b) extends the traditional self-attention
as follows:
u(k)
i,j =
[Wq,(k)(h(k−1)
i + ei,j)]T [Wk,(k)(h(k−1)
j + ej,i)]
√
d
. (58)
Given the learnt attention for each relation, edge embedding representation is the next critical
step for incorporating the structure-information. Shaw et al. (2018) simply learns the relative po-
sition encoding w.r.t the nodes’ absolute positions. Technically, they employ 2K + 1 latent labels
([−K, K]) and project j− i to one speciﬁc label embedding for node pair(vi, vj) to fetch the edge
embedding ei,j. Xiao et al. (2019) adopts the similar idea as Shaw et al. (2018). They deﬁne a
relative position embedding table and fetch the edge embedding by looking up from it.
Zhu et al. (2019a); Cai and Lam (2020b) learn the edge representationei,j by the path from node
vi to node vj. For Zhu et al. (2019a), the natural way is to view the path as a string, which is added
to the vocabulary to vectorize it. Other ways are further proposed to learn from labels’ embedding
along the path, such as 1) taking average, 2) taking sum, 3) encoding them using self-attention, and
4) encoding them using CNN ﬁlters. Cai and Lam (2020b) propose the shortest path based relation
encoder. Concretely, they ﬁrstly fetch the labels’ embedding sequence along the path. Then they
employ the bi-directional GRUs for sequence encoding. The last hidden states of the forward and
backward GRU networks are ﬁnally concatenated to represent the relation embeddingei,j.
5.3 Graph Neural Networks for Heterogeneous Graph
In practice, many graphs have various node and edge types, such as knowledge graph, AMR graph,
etc., which are called heterogeneous graphs. Formally, for a graph G, s.t. |T| > 1 or|R| >
1, it is called heterogeneous graph. Beside transforming the heterogeneous to relation graphs, as
introduced in the previous subsection, sometimes it is required to fully leverage the type information
for both nodes and edges (Hu et al., 2020a; Fan et al., 2019; Feng et al., 2020a; Wang et al., 2020b;
Linmei et al., 2019; Zhang et al., 2019f). Thus, in Section. 5.3.1, we ﬁrst introduce a pre-processing
technique for heterogeneous graph. Then, in Section. 5.3.2 and 5.3.3, we will introduce two typical
graph representation learning methods specially for heterogeneous graphs.
5.3.1 L EVI GRAPH TRANSFORMATION
Since most existing GNN methods are only designed for homogeneous conditions and there is a
massive computation burden when dealing with lots of edge types (Beck et al., 2018a) (e.g. an
AMR graph may contain more than 100 edge types), it is typical to effectively to treat the edges
as nodes in the heterogeneous graphs (Beck et al., 2018a; Xu et al., 2018c; Sun et al., 2019b; Guo
et al., 2019b).
One of the important graph transformation techniques is Levi Graph Transformation. Techni-
cally, for each edge ei,j with edge label φ(ei,j), we will create a new node vei,j. Thus the new
graph is denoted asG′(V′,E′,T′,R′), where the node set isV′ =V∪{ vei,j}, the node label set is
T′ =T ∪{φ(e)i,j}. We cut off the direct edge between node vi, vj and the add two direct edges
between: 1) vi, vei,j, and 2) vei,j , vj. After converting all edges in E, the new graph G′ will be a
bipartite graph, s.t. |R′| = 1 . An example of transforming AMR graph to desired levi-graph is
illustrated in Fig. 11. The obtained graph is a simpliﬁed heterogeneous levi graph that has a single
edge type but unrestricted node types, which can then be learnt by heterogeneous GNNs described
in Section 5.3.
36





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
nameperson
describe-01
"Paul"
fighter:ARG2
:ARG1
:ARG0
:name :op1
fighter
describe-01
person
name
"Paul"
:ARG2
:ARG1
:ARG0
:name
:op1
Figure 11: An example for transforming AMR graph to Levi-graph.
5.3.2 M ETA-PATH BASED HETEROGENEOUS GNN
Meta-path, a composite relation connecting two objects, is a widely used structure to capture the
semantics. Take movie data IMDB for example, there are three types of nodes, including movie, ac-
tor, and director. The meta-path M ovie→ Actor→ M ovie, which covers two movie sets and one
actor, describes the co-actor relations. Thus different relations between nodes in the heterogeneous
graph can be easily revealed by meta-paths.
First, we provide the meta-level (i.e., schema-level) description of a heterogeneous graph for
better understanding. We follow the setting of heterogeneous information network (HIN) (Sun
et al., 2011) and give the concept of Network Schema. The network schema is a meta template for
the heterogeneous graph G(V,E) with the node type mapping: V →T and edge type mapping:
E →R. We denote it as MG(T ,R). A meta path is a path on the network schema denoted as
Φ = T1
R1
→ T2
R2
→ ...
Rl
→ Tl+1, where Ti∈T is the schema’s node and Ri∈R is the corresponding
relation node. What’s more, we denote the meta-path set as {Φ1, Φ2, ...,Φp}. For each node Ti on
the meta-path Φj, we denote it as T Φj
i . Then we combine the network schema with the concrete
heterogeneous graph. For each node vi in the heterogeneous graph and one meta-pathΦj, we deﬁne
the meta-path-based neighbors asNΦj(vi), which contains all nodes including itself linked by meta-
path Φj. An example of meta-path based heterogeneous graph is shown in Fig. 12. Conceptually,
the neighbor set can have multi-hop nodes depending on the length of the meta-path.
a1 d1
m1
a2 d2
m2
m3
actor movie director
a m a
d m d
Heterogeneous graph Meta-paths
Figure 12: An example of meta-path based heterogeneous graph.
Most meta-path-based GNN methods adopt the attention-based aggregation strategy (Wang
et al., 2020b; Fan et al., 2019). Technically, they can be generally divided into two stages. Firstly,
37





LINGFEI WU AND YU CHEN , ET AL .
they aggregate the neighborhoods along each meta-paths, which can be named as “node-level ag-
gregation”. After this, the nodes receive neighbors’ information via different meta-path. Next, they
apply meta-path level attention to learn the semantic impact of different meta-path. In this way, they
can learn the optimal combination of neighbors connected by multiple meta-paths. In the following,
we will discuss two typical heterogeneous GNN models (Wang et al., 2020b; Fan et al., 2019).
HAN (Wang et al., 2019b) Due to the heterogeneity of nodes in graphs, different nodes have
different feature spaces, which brings a big challenge for GNN to handle various initial node em-
bedding. To tackle this issue, the type-speciﬁc transformation is adopted to project various nodes to
a uniﬁed feature space as follows:
h′
i = Wτ(vi)hi. (59)
We overwrite the notationhi to denote the transformed node embedding in HAN’s discussion.
• Node-level Aggregation. For the nodevi and its’ neighbor node setNΦk(vi) on the meta-path
Φk, the aggregated feature of node vi can be represented by:
zi,Φk = σ(
∑
vj∈NΦk(vi)
αΦk
i,j hj)
αΦk
i,j = softmaxj(uΦk
i,j )
uΦk
i,j = Attention(hi, hj; Φk) = σ(W[hi, hj]),
(60)
where W∈ R1×2d is the trainable parameter. To make the training process more stable, they
further extend the attention by the multi-head mechanism. The ﬁnal representation of zi,Φj
is the concatenation of L heads’ results. Given p meta-paths, we can obtain the aggregated
embedding via the previous nodel-level aggregation step as{ZΦ1, ...,ZΦp}, where ZΦj is the
collection of all nodes’ representation for meta-path Φj.
• Meta-path Level Aggregation. Generally, different meta-path conveys different semantic
information. To this end, they aim to learn the importance of each meta-path as:
(βΦ1, ..., βΦp) = Meta Attn(ZΦ1, ...,ZΦp), (61)
where βΦj denotes the learned importance score for meta-path Φj, and Meta Attn() is the
attention-based scorer. Technically, for each meta-path, they ﬁrst learn the semantic-level
importance for each node. Then they average them to get the meta-path level importance. It
can be formulated by:
oΦk = 1
|V|
∑
vi∈V
qT f(zi,Φk),
βΦk = softmaxk(oΦk),
(62)
where f(·) : Rd→ Rd is the MLP with tanh non-linearity.
Finally, we can obtain the ﬁnal node representation as:
zi =
p∑
k=1
βΦkzi,Φk . (63)
38





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
MEIRec The MEIRec (Fan et al., 2019) is a heterogeneous GNN-based recommend system. In
the speciﬁc recommendation system condition, they restrict the heterogeneous graph’s type amount
and meta-path’s length and propose a special heterogeneous graph neural network, particularly to
fully utilize rich structure information. Considering that the type-speciﬁc transformation requires
huge parameters when the amount of nodes is large, they propose an efﬁcient uniﬁed embedding
learning method. For each node, they fetch the terms in the vocabulary and then average them to
get the vector representation.
• Node-level Aggregation. Unlike HAN (Hu et al., 2020a), which collect all nodes along the
meta-path as neighbors, they treat different hop of neighbors differently. Given the meta-
path Φj, they deﬁne the neighbors of node vi as NΦj(vi)o, o∈ [1, 2, ..., O] where o denotes
the hop. They learn the representation recursively. Take (o)−hop neighbors for example,
for each nodes in NΦj(vi)o, they ﬁrst collect the immediate-neighbors from (o + 1)-hop
neighbors and learn the representation to obtain (o)-hop representation. Then they repeat this
procedure to obtain (o− 1)-hop nodes’ representation. Finally, vi’s representation for meta-
path Φj is generated. Formally, for vk∈ NΦj(vi)o, they deﬁne its’ immediate neighbor set as
NΦj(vk)∈ NΦj(vi)o+1. Node vj’s representation zk,Φj is formulated as:
zk,Φj = g({zl,Φj , vl∈ NΦj(vk)}), (64)
where g(·) is the aggregation function. In MEIRec, it can be the average function, LSTM
function, or the CNN function depend on the nodes’ type. Besides, the last hop ( (O)-hop)’s
nodes are represented by initial node embedding.
• Meta-path Level Aggregation. Given p meta-path with the starting nodesvi, we can obtain p
aggregated embedding by the previous step. Then we adopt a similar procedure as node-level
aggregation as follows:
zi = g({zi,Φj , j∈ [1, ..., p]}), (65)
where g(·) is the aggregation function, as we discussed before.
5.3.3 R-GNN BASED HETEROGENEOUS GNN
Although the meta-path is an effective tool to organize the heterogeneous graph, it requires addi-
tional domain expert knowledge. To this end, most researchers adopt a similar idea from R-GNN
by using type-speciﬁc aggregation. For clarity, we name these methods as R-GNN based heteroge-
neous GNN and introduce several typical variants of this category in the following.
HGAT HGAT (Linmei et al., 2019) is proposed for encoding heterogeneous graph which con-
tains various node types but single edge types. In other words, the edge only represents connectiv-
ity. Intuitively, for a speciﬁc node, different types of neighbors may have different relevance. To
fully exploit diverse structure information, HGAT ﬁrstly focuses on global types’ relevance learning
(type-level learning) and then learns the representation for speciﬁc nodes (node-level learning).
• Type-level learning. Technically, for a speciﬁc nodevi and its’ neighbors N(vi), HGAT get
the type-speciﬁc neighbor representation as:
z(k)
t =
∑
vj∈Nt(vi)
h(k−1)
j , t∈T . (66)
39





LINGFEI WU AND YU CHEN , ET AL .
Note that we overwrite Nt(vi) which denotes the neighbors with node type t. Then they
calculate the relevance of each type by attention mechanism:
st = σ(qT [h(k−1)
i , z(k)
t ]),
αt = exp(st)∑
t′∈T exp(st′) ,
(67)
where q is the trainable vector.
• Node-level learningSecondly, they apply R-GCN (Schlichtkrull et al., 2018) like aggregation
procedure for a different type of nodes. Formally, for the nodevi and the type relevance scores
{αt}, t∈T , HGAT calculate each neighbors’ attention score as follows:
bi,j = σ(qT
1 ατ(vj)[h(k−1)
i , h(k−1)
j ]),
βi,j = exp(bi,j)∑
vm∈N(vi) exp(bi,m) ,
(68)
where q1 is the trainable vector. Finally, HGAT applies layer-wise heterogeneous GCN to
learn the node representation, which is formulated as:
h(k)
i = σ(
∑
t∈T
∑
vj∈Nt(vi)
W(k)
t h(k−1)
j ). (69)
MHGRN MHGRN (Feng et al., 2020a) is an extension of R-GCN, which can leverage multi-hop
information directly on heterogeneous graphs. Generally, it borrows the idea of relation path (e.g.,
meta-path) to model the relation of two not k-hop connected nodes and extend the existing R-GNN
to the path-based heterogeneous graph representation learning paradigm. The K-hop relation path
between node vi, vj is denoted as:
Φk ={(vi, ei,1, ..., ek−1,j, vj)|(vi, ei,1, v1), ...,(vk−1, ek−1,j)∈E} . (70)
Note that the heterogeneous graph may contain more than one k-hop relation path.
• k-hop feature aggregation. First, to make the GNN aware of the node type, they project the
nodes’ initial feature to the uniﬁed embedding space by type-speciﬁc linear transformation
(the same as eq. 59). Considering simpliﬁcation, we overwrite nodes’ feature notation h to
represent the uniﬁed features. Then given node vi, they aim to aggregate k-hop (k∈ [1, K])
neighbors’ feature as follows:
zΦk
i =
∑
(vj,ej,1,...,ek−1,i,vi)∈Φk
α(vj, ej,1, ..., ek−1,i, vi)∑
(vj,...,vi)∈Φk α(vj, ..., vi)
l=K∏
l=1
o=K∏
o=1
Wl
rohj,
(1≤ k≤ K)
(71)
where Wl
ro, 1≤ l≤ K, 1≤ o≤ K is the learnable matrix, ro denotes o−th hop’s edge,
α(j, v1, ..., vk, vi) is the attention score among all k-hop paths between node vj and vi. We
use zi to denote the learned embedding for node vi.
40





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
• Fusing different relation paths . Next, they fuse relation paths with different length via
attention mechanism:
z′
i =
K∑
k=1
Attention(q, zΦk
i )zΦk
i , (72)
where q is the task-speciﬁc vector (in MHGRN, it is the text-based query vector), Attention() :
Rd→ R is the normalized attention score. Note that we omit the details of α(j, v1, ..., vk, vi)
and Attention() since they are task-speciﬁc functions. At last, the ﬁnal representation of node
vi is the shortcut connection between zi and original feature hi as follows:
zi = σ(W1z′
i + W2hi), (73)
where W1, W2 is the learnable weights.
HGT The HGT (Hu et al., 2020a) is the graph transformer for heterogeneous graphs, which build
meta-relations among nodes on top of the network schema, as we discuss in the meta-path-based
heterogeneous GNN paragraph. Unlike most previous works that assume the graph structure is
static (i.e., time-independent), they propose a relative temporal encoding strategy to learn the time
dependency.
The meta-relation is a triple based on the network schema. For each edge ei,j which links node
vi and vj, the meta-relation is deﬁned asΦvi,ei,jvj =< τ (vi), φ(ei,j), τ(vj) >. To further represent
the time-dependent relations, they add the timestamps to the start nodes when adding directed edges.
Generally, the GNN is deﬁned as:
h(k)
i = Aggregation(k)
vj∈N(vi)(Attention(k)(vi, ei,j, vj)Message(k)(vi, ei,j, vj)), (74)
where N(vi) denotes the incoming nodes. We will brieﬂy discuss three basic meta-relation based
operations: attention, message message passing, and aggregation, as well as the relative temporal
encoding strategy.
• Attention operation. The Attention(·,·,·) operation is the mutual attention that calculates the
weight of two connected nodes grounded by their meta-relations. Speciﬁcally, they employ
multi-head attention based on meta-relations, which is formulated as:
Attn headi(vi, ei,j, vj) =
f lineari
τ(vi)(hi)WATT
φ(ei,j)g lineari
τ(vj)(hj)T EΦvi,ei,j vj
√
d
,
Attention(vi, ei,j, vj) = sof tmaxvj∈N(vi)(||H
h=1Attn headi(vi, ei,j, vj))
(75)
where H is the number of heads, f lineari
τ(·), g lineari
τ(·) : Rd/H→ Rd/H are the node-type-
speciﬁc transformation functions for source nodes and target nodes respectively, WATT
φ(·) is
the edge-type-speciﬁc matrix, andEΦvi,ei,j vj is the meta-path-speciﬁc scalar weight.
• Message passing operation. The Message(·) is the heterogeneous message passing function.
Similar to the Attention (·,·,·) above, they incorporate the meta-relations into the message
passing process as follows:
msg headi(vi, ei,j), vj) = m lineari
τ(vi)(hi)WMSG
φ(ei,j),
Message(vi, ei,j, vj) =||H
h=1msg headh(vi, ei,j, vj)
(76)
41





LINGFEI WU AND YU CHEN , ET AL .
where m linear(·) : Rd/H→ Rd/H is the node-type-speciﬁc transformation, and WMSG
φ(·) is
the edge-type-speciﬁc matrix.
• Aggregation operation. For aggregation operation, since the Attention () function’s results
have been normalized by softmax function, they simply use average function as Aggregation(·).
Finally, they employ meta-path-speciﬁc projection followed by residual connection to learn
the ﬁnal representation of each nodes as follows:
z(k)
i =
∑
vj∈N(vi)
(Attention(k)(vi, ei,j, vj)Message(k)(vi, ei,j, vj)),
h(k)
i = A linearΦvi,ei,j vj (σ(z(k)
i )) + h(k−1),
(77)
where A linearΦvi,ei,j vj (·) : Rd→ Rd is the meta-relation-speciﬁc projection.
• Relative Temporal Encoding To tackle the graph’s time dependency, they propose the Rel-
ative Temporal Encoding mechanism to each node’s embedding. Technically, they calculate
the timestamp difference of target and source nodes as δi,j = T (vj)− T (vi), where T (·) is
the timestamp of the node. Then they project the time gap to the speciﬁc embedding space.
This temporal encoding is added to the source nodes’ representation before GNN encoding.
6. GNN Based Encoder-Decoder Models
Encoder-decoder architecture is one of the most widely used machine learning framework in the
NLP ﬁeld, such as the Sequence-to-Sequence (Seq2Seq) models(Sutskever et al., 2014; Cho et al.,
2014). Given the great power of GNNs for modeling graph-structured data, very recently, many
research efforts have been made to develop GNN-based encoder-decoder frameworks including
Graph-to-Tree (Li et al., 2020b; Zhang et al., 2020c) and Graph-to-Graph (Guo et al., 2019c; Shi
et al., 2020) models. In this section, we will ﬁrst introduce the typical Seq2Seq models, and then
discuss various graph-based encoder-decoder models for various NLP tasks.
are there ada jobs outside austin
aux
expl
obj
nmod
case
Text input: are there ada jobs outside austin
Parse
Graph encoder
. . .
x0 
x1 
. 
. 
xn
x0 
x1 
. 
. 
xn
x0 
x1 
. 
. 
xn
x0 
x1 
. 
. 
xn
. . .
x0 
x1 
. 
. 
xn
x0 
x1 
. 
. 
xn
x0 
x1 
. 
. 
xn
x0 
x1 
. 
. 
xn
Pooling
x0 
x1 
. 
. 
. 
. 
. 
. 
xn
Decoding language ( ANS , ada ) , job ( ANS ) , \+ loc 
( ANS , austin )
Sequence decoder
language S1 , job S2, \+ loc S3
ANS , ada
ANS 
ANS  , austin
Graph constructor
S1
S2
S3
Tree decoder
Figure 13: Overall architecture for graph based encoder-decoder model which contains both the
Graph2Seq and Graph2Tree models. Input and output are from JOBS640 dataset (Luke, 2005) .
Nodes like S1, S2 stand for sub-tree nodes, which new branches are generated from.
42





---

## Part 4 — GNN-Based Encoder-Decoder Models (Section 6, pp. 43–56)


GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
6.1 Sequence-to-Sequence Models
Sequence-to-Sequence (Seq2Seq) learning (Sutskever et al., 2014; Cho et al., 2014) is one of the
most widely used machine learning paradigms in the NLP ﬁeld. In this section, we ﬁrst give a brief
overview of Seq2Seq learning and introduce some typical Seq2Seq techniques. Then we pinpoint
some known limitations of Seq2Seq learning as well as its solutions, namely, incorporating more
structured encoder-decoder models as alternatives to Seq2Seq models so as to encode more complex
data structures.
6.1.1 O VERVIEW
Sequence-to-Sequence (Seq2Seq) models were originally developed by Sutskever et al. (2014) and
Cho et al. (2014) for solving general sequence-to-sequence problems (e.g., machine translation).
The Seq2Seq model is an end-to-end encoder-decoder framework which learns to map a variable-
length input sequence to a variable-length output sequence. Basically, the idea is to use an RNN-
based encoder to read the input sequence (i.e., one token at a time), to build up a ﬁxed-dimensional
vector representation, and then use an RNN-based decoder to generate the output sequence (i.e.,
one token at a time) conditioned on the encoder output vector. The decoder is essentially a RNN
language model except that it is conditioned on the input sequence. One of the most common
Seq2Seq variants is to apply a Bidirectional LSTM encoder to encode the input sequence, and
apply a LSTM decoder to decode the output sequence (Sutskever et al., 2014). Other Seq2Seq
variants replace LSTM with Gated Recurrent Units (GRUs) (Cho et al., 2014), Convolutional Neural
Networks (CNNs) (Gehring et al., 2017) or Transformer models (Vaswani et al., 2017).
Despite the promising achievements in many NLP applications such as machine translation,
the original Seq2Seq models suffer a few issues such as the information bottleneck of the ﬁxed-
dimensional intermediate vector representation, and the exposure bias of cross-entropy based se-
quence training. In the original Seq2Seq architecture, the intermediate vector representation be-
comes an information bottleneck because it summarizes the rich information of the input sequence
as a ﬁxed-dimensional embedding, which serves as the only knowledge source for the decoder to
generate a high-quality output sequence. In order to increase the learning capacity of the original
Seq2Seq models, many effective techniques have been proposed.
6.1.2 A PPROACH
The attention mechanism (Bahdanau et al., 2015; Luong et al., 2015) was developed to learn the
soft alignment between the input sequence and output sequence. Speciﬁcally, at each decoding step
t, an attention vector indicating a probability distribution over the source words is computed as
et
i = f(⃗hi, ⃗ st)
⃗ at = softmax(⃗ et),
(78)
where f can be arbitrary neural network computing the relatedness between the decoder state ⃗ st
and encoder hidden state state ⃗hi. One common option is to apply an additive attention mechanism
f(⃗hi, ⃗ st) = ⃗ vT tanh( ⃗Wh⃗hi + ⃗Ws⃗ st + b) where ⃗ v, ⃗Wh, ⃗Ws and b are learnable weights. Given the
attention vector ⃗ at at the t-th decoding step, the context vector can be computed as a weighted sum
of the encoder hidden states, formulated as
⃗h∗
t =
∑
i
at
i⃗hi, (79)
43





LINGFEI WU AND YU CHEN , ET AL .
The computed context vector will be concatenated with the decoder state, and fed through some
neural network for producing a vocabulary distribution.
The copying mechanism (Vinyals et al., 2015; Gu et al., 2016) was introduced to directly copy
tokens from the input sequence to the output sequence in a learnable manner. This can be very help-
ful in some scenarios where the output sequence refers to some named entities or out-of-vocabulary
tokens in the input sequence. Speciﬁcally, at each decoding step t, a generation probability will be
calculated for deciding whether to generate a token from the vocabulary or copy a token from the
input sequence by sampling from the attention distribution ⃗ at. The generation probability can be
computed as
pgen = σ( ⃗ wT
h∗⃗h∗
t + ⃗ wT
s ⃗ st + ⃗ wT
x ⃗ xt + bptr)), (80)
where ⃗ wh∗, ⃗ ws, ⃗ wx and bptr are learnable weights, σ is a sigmoid function, and pgen is a scalar
between 0 and 1.
The coverage mechanism (Tu et al., 2016) was proposed to encourage the full utilization of
different tokens in the input sequence. This can be useful in some NLP tasks such as machine
translation. Speciﬁcally, at each decoding step t, a coverage vector ⃗ ct which is the aggregated
attention vectors over all previous decoding steps will be computed as
⃗ ct =
t−1∑
t′=0
⃗ at′
. (81)
In order to encourage better utilization of those source tokens that have not received enough attention
scores so far, the above coverage vector will be used as extra input to the aforementioned attention
mechanism Eq. (78), that is,
et
i = f(⃗hi, ⃗ st, ct
i) (82)
To avoid generating repetitive text, a coverage loss is calculated at each decoding step to penalize
repeatedly attending to the same locations, formulated as,
covlosst =
∑
i
min(at
i, ct
i) (83)
The above coverage loss essentially penalizes the overlap between the attention vector and the cov-
erage vector, and is bounded to ∑
i at
i = 1 . It will be reweighted and added to the overall loss
function.
The exposure bias occurs when during the training phase, the ground-truth token is used as the
input (i.e., for better supervision) to the decoder for predicting the next token, while in the infer-
ence phase, the decoder’s prediction from the previous time step is used as the input for next step
prediction (due to no access to the ground-truth token). In order to reduce this gap between training
and inference phases and thus increase the generalization ability of the original Seq2Seq models,
scheduled sampling (Bengio et al., 2015) was proposed to alleviate this issue by taking as input
either the decoder’s prediction from the previous time step or the ground truth with some proba-
bility for next step prediction, and gradually decreasing the probability of feeding in the ground
truth at each iteration of training. The celebrated Seq2Seq models equipped with the above effec-
tive techniques have achieved great successes in a wide range of NLP applications such as neural
machine translation (Bahdanau et al., 2015; Luong et al., 2015; Gehring et al., 2017), text summa-
rization (Nallapati et al., 2016; See et al., 2017; Paulus et al., 2018), text generation (Song et al.,
2017), speech recognition (Zhang et al., 2017a), and dialog systems (Serban et al., 2016, 2017).
44





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
6.1.3 D ISCUSSIONS
Seq2Seq models were originally developed to solve sequence-to-sequence problems, that is, to map
a sequential input to a sequential output. However, many NLP applications naturally admit graph-
structured input data such as dependency graphs (Fu et al., 2019; Chen et al., 2020g), constituency
graphs (Li et al., 2020b; Marcheggiani and Titov, 2020), AMR graphs (Beck et al., 2018a; Song
et al., 2019), IE graphs (Cao et al., 2019b; Huang et al., 2020b) and knowledge graphs (Nathani
et al., 2019a; Wu et al., 2019b). In comparison with sequential data, graph-structured data is able
to encode rich syntactic or semantic relationships among objects. Moreover, even if the raw input
is originally represented in a sequential form, it can still beneﬁt from explicitly incorporating rich
structural information (e.g., domain-speciﬁc knowledge) to the sequence. The above situations
essentially call for an encoder-decoder framework for learning a graph-to-X mapping where X can
stand for a sequence, tree or even graph. Existing Seq2Seq models face a signiﬁcant challenge in
learning an accurate mapping from graph to the appropriate target due to its incapability of modeling
complex graph-structured data.
Various attempts have been made in order to extend Seq2Seq models to handle Graph-to-
Sequence problems where the input is graph-structured data. A simple and straightforward ap-
proach is to directly linearize the structured graph data into the sequential data (Iyer et al., 2016;
G´omez-Bombarelli et al., 2018; Liu et al., 2017), and apply the Seq2Seq models to the resulting
sequence. However, this kind of approaches suffer signiﬁcant information loss, which leads to
downgraded performance. The root cause of RNN’s incapability of modeling complex structured
data is because it is a linear chain. In light of this, some research efforts have been devoted to
extend Seq2Seq models. For instance, Tree2Seq (Eriguchi et al., 2016) extends Seq2Seq models
by adopting Tree-LSTM (Tai et al., 2015) which is a generalization of chain-structured LSTM to
tree-structured network topologies. Set2Seq (Vinyals et al., 2016) is an extension of Seq2Seq mod-
els that goes beyond sequences and handles the input set using the attention mechanism. Although
these Seq2Seq extensions achieve promising results on certain classes of problems, none of them
can model arbitrary graph-structured data in a principled way.
6.2 Graph-to-Sequence Models
6.2.1 O VERVIEW
To address the aforementioned limitations of Seq2Seq models on encoding rich and complex data
structures, recently, a number of graph-to-sequence encoder-decoder models for NLP tasks have
been proposed (Bastings et al., 2017; Beck et al., 2018a; Song et al., 2018d; Xu et al., 2018b). This
kind of Graph2Seq models typically adopt a GNN based encoder and a RNN/Transformer based
decoder. Compared to the Seq2Seq paradigm, the Graph2Seq paradigm is better at capturing the
rich structure information of the input text and can be applied to arbitrary graph-structured data.
Graph2Seq models have shown superior performance in comparison with Seq2Seq models in a
wide range of NLP tasks including neural machine translation (Bastings et al., 2017; Marcheggiani
et al., 2018; Beck et al., 2018a; Song et al., 2019; Xu et al., 2020b; Yao et al., 2020; Yin et al.,
2020; Cai and Lam, 2020c), AMR-to-text (Beck et al., 2018a; Song et al., 2018d; Damonte and
Cohen, 2019; Ribeiro et al., 2019b; Zhu et al., 2019a; Wang et al., 2020e; Guo et al., 2019b; Yao
et al., 2020; Wang et al., 2020d; Cai and Lam, 2020c; Bai et al., 2020; Song et al., 2020; Zhao et al.,
2020a; Zhang et al., 2020b; Jin and Gildea, 2020), text summarization (Fernandes et al., 2019; Xu
et al., 2020a; Huang et al., 2020b; Zhang et al., 2020a), question generation (Chen et al., 2020g;
45





LINGFEI WU AND YU CHEN , ET AL .
Wang et al., 2020g), KG-to-text (Koncel-Kedziorski et al., 2019), SQL-to-text (Xu et al., 2018a),
code summarization (Liu et al., 2021a), and semantic parsing (Xu et al., 2018c).
6.2.2 A PPROACH
Most proposed Graph2Seq models were designed for tackling particular NLG tasks. In the fol-
lowings, we will discuss some common techniques adopted in a wide rage of Graph2Seq variants,
which include both graph-based encoding techniques and sequential decoding techniques.
Graph-based Encoders Early Graph2Seq methods and their follow-up works (Bastings et al.,
2017; Marcheggiani et al., 2018; Damonte and Cohen, 2019; Guo et al., 2019b; Xu et al., 2020a,b;
Zhang et al., 2020a,b) mainly used some typical GNN variants as the graph encoder inclduing GCN,
GGNN, GraphSAGE and GAT. Since the edge direction in a NLP graph often encodes critical in-
formation about the semantic relations between two vertices, it is often extremely helpful to capture
the bidirectional information of text (Devlin et al., 2019). In the literature of Graph2Seq paradigm,
some efforts have been made to extend the existing GNN models to handle directed graphs. The
most common strategy is to introduce separate model parameters for different edge directions
(i.e., incoming/outgoing/self-loop edges) when performing neighborhood aggregation (Marcheg-
giani et al., 2018; Song et al., 2018d, 2019; Xu et al., 2020b; Yao et al., 2020; Wang et al., 2020e;
Guo et al., 2019b).
Besides the edge direction information, many graphs in NLP applications are actually multi-
relational graphs where the edge type information is very important for the downstream task. In
order to encode edge type information, some works (Simonovsky and Komodakis, 2017; Chen
et al., 2018b; Ghosal et al., 2020; Wang et al., 2020c; Schlichtkrull et al., 2018; Teru et al., 2020)
have extended them by having separate model parameters for different edge types (i.e., similar
ideas have been used for encoding edge directions). However, in many NLP applications (e.g.,
KG-related tasks), the total number of edge types is large, hence the above strategy can have severe
scalability issues. To this end, some works (Beck et al., 2018a; Koncel-Kedziorski et al., 2019; Yao
et al., 2020; Ribeiro et al., 2019b; Guo et al., 2019b; Chen et al., 2020h) proposed to bypass this
problem by converting a multi-relational graph to a Levi graph (Levi, 1942) and then utilize existing
GNNs designed for homogeneous graphs as encoders. Another commonly adopted technique is to
explicitly incorporate edge embeddings into the message passing mechanism (Marcheggiani et al.,
2018; Song et al., 2018d, 2019; Zhu et al., 2019a; Wang et al., 2020d; Cai and Lam, 2020c; Wang
et al., 2020e; Song et al., 2020; Liu et al., 2021a; Jin and Gildea, 2020).
Besides the above widely used GNN variants, some Graph2Seq works also explored other GNN
variants such as GRN (Song et al., 2018d, 2019) and GIN (Ribeiro et al., 2019b). Notably, GRN
is also capable of handling multi-relational graphs by explicitly including edge embeddings in the
LSTM-style message passing mechanism.
Node & Edge Embeddings Initialization For GNN based approaches, initialization of nodes
and edges is extremely critical. While both CNNs and RNNs are good at capturing local depen-
dencies among consecutive words in text, GNNs do well in capturing local dependencies among
neighboring nodes in a graph. Many works on Graph2Seq have shown beneﬁts of initializing node
and/or edge embeddings by applying CNNs (Bastings et al., 2017; Marcheggiani et al., 2018) or
bidirectional RNNs (BiRNNs) (Bastings et al., 2017; Marcheggiani et al., 2018; Fernandes et al.,
2019; Xu et al., 2018b,a; Koncel-Kedziorski et al., 2019; Cai and Lam, 2020c; Wang et al., 2020g;
Chen et al., 2020g; Liu et al., 2021a) to the word embedding sequence before applying the GNN
46





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
based encoder. Some works also explored to initialize node/edge embeddings with BERT embed-
dings+BiRNNs (Xu et al., 2020a; Chen et al., 2020g) or RoBERTa+BiRNNs (Huang et al., 2020b).
Sequential Decoding Techniques Since the main difference between Seq2Seq and Graph2Seq
models is on the encoder side, common decoding techniques used in Seq2Seq models such as at-
tention mechanism (Bahdanau et al., 2015; Luong et al., 2015), copying mechanism (Vinyals et al.,
2015; Gu et al., 2016), coverage mechanism (Tu et al., 2016), and scheduled sampling (Bengio
et al., 2015) can also be adopted in Graph2Seq models with potential modiﬁcations.
Some efforts have been made to adapt common decoding techniques to the Graph2Seq paradigm.
For example, in order to copy the whole node attribute containing multi-token sequence from the
input graph to the output sequence, Chen et al. (2020h) extended the token-level copying mech-
anism to the node-level copying mechanism. To combine the beneﬁts of both sequential encoder
and graph encoder, Pan et al. (2020); Sachan et al. (2020) proposed to fuse their outputs to a single
vector before feeding it to a decoder. Huang et al. (2020b) designed separate attention modules for
sequential encoder and graph encoder, respectively.
av
i = attn v(⃗ st, ⃗hv
i )
⃗ cv =
∑
i
av
i ⃗hv
i
as
j = attn s(⃗ st, ⃗hs
j, ⃗ cv)
⃗ cs =
∑
i
as
j⃗hs
j
⃗ c= ⃗ cv||⃗ cs
(84)
where ⃗hv
i and ⃗hs
j are the graph encoder outputs and sequential encoder outputs, respectively.⃗ cis the
concatenation of the graph context vector ⃗ cv and sequential context vector ⃗ cs.
In order to tackle the limitations (e.g., exposure bias and discrepancy between the training and
inference phases) of cross-entropy based sequential training, Chen et al. (2020g) proposed to train
the Graph2Seq system by minimizing a hybrid loss combining both cross-entropy loss and rein-
forcement learning (Williams, 1992) loss. While LSTM or GRU based decoders are the most
commonly used decoder in Graph2Seq models, some works also employed a Transformer based
decoder (Koncel-Kedziorski et al., 2019; Zhu et al., 2019a; Yin et al., 2020; Wang et al., 2020d; Cai
and Lam, 2020c; Bai et al., 2020; Wang et al., 2020e; Song et al., 2020; Zhao et al., 2020a; Jin and
Gildea, 2020).
6.2.3 D ISCUSSIONS
There are some connections and differences between Graph2Seq models and Transformer-based
Seq2Seq models, and many of them have already been discussed above when we talk about the
connections and differences between GNNs and Transformer models. It is worth noting that there
is a recent trend in combining the beneﬁts of the both paradigms, thus making them less distin-
guishable. Many recent works designed various graph transformer based generation models (as we
discussed above) which employ a graph-based encoder combining both the beneﬁts of GNNs and
Transformer, and a RNN/Transformer based decoder.
Despite the great success of Graph2Seq models, there are some open challenges. Many of
these challenges are essentially the common challenges of applying GNNs for graph representation
47





LINGFEI WU AND YU CHEN , ET AL .
learning, including how to better model multi-relational or heterogeneous graphs, how to scale to
large-scale graphs such as knowledge graphs, how to conduct joint graph structure and representa-
tion learning, how to tackle the over-smoothing issue and so on. In addition, Graph2Seq models
also inherit many challenges that Seq2Seq models have, e.g., how to tackle the limitations of cross-
entropy based sequential training (e.g., exposure bias and discrepancy between the training and
inference phases).
+
21
-
4
5
* *
3
1
2
5
6
3
4
7
8
Left node generation
Right node generation
Left sub-tree embedding
+
21
-4
5
*
*
3
S2S1
1
2
3
Sibling feeding
Begin a new branch decoding
Parent feeding
Sequential decoding
Figure 14: Equation: ( 1 * 2 ) + ( 4 - 3 ) * 5. Left: a DFS-based tree decoder example, the number
stands for the order of the decoding actions. Right: a BFS based tree decoder example. Nodes like
S1, S2 stand for sub-tree nodes, and once a sub-tree node generated, decoder will start a new branch
for a new descendant decoding process. The number stands for the order of different branching
decoding processes.
6.3 Graph-to-Tree Models
6.3.1 O VERVIEW
Compared to Graph2Seq model, which considers the structural information in the input side, many
NLP tasks also contain outputs represented in a complex structured, such as trees, which are also
rich in structural information at the output side, e.g., syntactic parsing(Ji et al., 2019)(Yang and
Deng, 2020), semantic parsing(Li et al., 2020b)(Xu et al., 2018c), math word problem solving(Li
et al., 2020b)(Zhang et al., 2020c). It is a natural choice for us to consider the structural information
of these outputs. To this end, some Graph2Tree models are proposed to incorporate the structural
information in both the input and output side, which make the information ﬂow in the encoding-
decoding process more complete.
6.3.2 A PPROACH
To illustrate how the Graph2Tree model works, we will introduce how different components of the
Graph2Tree model operate here, including: graph construction, graph encoder, attention mecha-
nism, and tree decoder.
Graph construction The graph construction module, which is usually highly related to speciﬁc
tasks, could be divided into two categories: one with auxiliary information and one without auxiliary
information. For the former, Li et al. (2020b) use syntactic graph in both semantic parsing and
math word problem solving tasks, which consists of the original sentence and the syntactic pasing
48





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
tree (dependency and constituency tree). And the input graph in (Yin et al., 2018) considers the
graph composed of the abstract syntax tree (AST) of a fragment of source code. For the latter, the
input can usually form a task graph itself without auxiliary information. For example, Zhang et al.
(2020c) employ the relationship between different numbers in the math word problem in the graph
construction module.
Graph encoder Graph encoder is used for embedding the input graph into the latent representa-
tion. To implementing the graph encoder module, several graph2tree models use relatively sim-
ple GNN models, such as GCN(Kipf and Welling, 2016), GGNN(Li et al., 2015), and Graph-
SAGE(Hamilton et al., 2017a). For (Li et al., 2020b), it uses a bidirectional variant of the GraphSage
model, and Zhang et al. (2020c) exploit the GCN model before a transformer layer. And Yin et al.
(2018) simply adopt the GGNN model as its neural encoder.
Attention The attention module is a key component in an encoder-decoder framework, which
carry the important information for bridging the input and output semantics. In the graph2tree
model, the input graph often contains different types of nodes(Li et al., 2020b)(Zhang et al., 2020c),
while the traditional attention module can not distinguish between these nodes. In (Li et al., 2020b),
the author uses the separate attention module to calculate the attention vector for different nodes
in the input graph where some nodes is from the original sentence, and others are composed of the
nodes in parsing trees generated by the external parser. It has been validated that distinguishing these
two types of nodes could facilitate better learning process than the original attention module. This
idea is similar to the application of Tree2Seq(Eriguchi et al., 2016) attention module in machine
translation.
Speciﬁcally in (Li et al., 2020b), the decoder generates the tree structure by representing some
branching nodes as non-terminal nodes, i.e., node S1 in Figure 14. Once these nodes generated, the
decoder will start a new sequential decoding process. The decoder hidden state st at time step t is
calculated a st = fdecoder(yt−1, st−1; spar; ssib), (85)
where the spar, ssib stand for the parent node hidden state and sibling node hidden state as illustrated
in Figure 14. After the current hidden state generated, the output module including attention layer
is calculated as follows:
αt(v) = exp(score(zv, st))
exp(∑V1
k=1 score(zk, st))
,∀v∈V 1 (86)
βt(v) = exp(score(zv, st))
exp(∑V2
k=1 score(zk, st))
,∀v∈V 2 (87)
cv1 =
∑
αt(v)zv,∀v∈V 1 (88)
cv2 =
∑
βt(v)zv,∀v∈V 2 (89)
where zv denotes to the learned node embedding for node v,V1 denotes to the node set including
all words from original sentences, andV2 denotes to another node set including all other nodes. We
then concatenate the context vector cv1, context vector cv2 and decoder hidden state st to compute
the ﬁnal attention hidden state at this time step as:
49





LINGFEI WU AND YU CHEN , ET AL .
˜st = tanh(Wc· [cv1; cv2; st] + bc), (90)
where Wc and bc are learnable parameters. The ﬁnal context vector ˜st is further fed to the output
layer which is a softmax function after a feed-forward layer.
Tree decoder The output of some applications (i.e., semantic parsing, code generation, and math
word problem) contain structural information, for example, the output in math word problem is
a mathematical equation, which can be expressed naturally by the data structure of the tree. To
generate these kinds of outputs, tree decoders are widely used in these tasks. Tree decoders can
be divided into two main parts as shown in Figure 14, namely, dfs (depth ﬁrst search) based tree
decoder, and bfs (breadth ﬁrst search) based tree decoder.
For bfs-based decoders(Li et al., 2020b; Dong and Lapata, 2016; Alvarez-Melis and Jaakkola,
2016), the main idea is to represent all the sub-trees in the tree as non-terminal nodes, and then use
sequence decoding to generate intermediate results. If the results contains non-terminals, then we
start branching (begin a new decoding process) with this node as the new root node, until the entire
tree is expanded.
For dfs-based decoders(Zhang et al., 2020c; Yin et al., 2018), they regards the entire tree gener-
ation process as a sequence of actions. For example, in the generation of a binary tree (mathematical
equation) in (Zhang et al., 2020c), the root node is generated in priority at each step, following by
the generation of the left child node. After all the left child nodes are generated, a bottom-up manner
is adopted to begin the generation of the right child nodes.
In addition, the tree decoder is constantly evolving, and some techniques are proposed to collect
more information during the decoding process or leverage the information from the input or output,
such as parent feeding(Dong and Lapata, 2016), sibling feeding(Li et al., 2020b), sub-tree copy(Yin
et al., 2018), tree based re-ranking(Do and Rehbein, 2020) and other techniques. At the same
time, the wide application of the transformer model also brings about many transformer based tree
decoders(Sun et al., 2020c)(Li et al., 2020a), which proves the wide application of tree decoder and
Graph2tree model.
6.4 Graph-to-Graph Models
The graph-to-graph models that are typically utilized for solving graph transformation problem as a
graph encoder-decoder model. The graph encoder generates the latent representation of each node
in the graph or generate one graph-level latent representation for the whole graph via the GNNs. The
graph decoder then generates the output target graphs based on the node-level or graph-level latent
representations from the encoder. In this section, we ﬁrst introduce graph-to-graph transformation
problem and the typical NLP applications that can be formalized as graph-to-graph transformation
problems. Then, we introduce the speciﬁc techniques for a Graph-to-graph model for information
extraction.
6.4.1 O VERVIEW
Graph-to-graph transformation Graph-to-graph models aims to deal with the problem of deep
graph transformation (Guo et al., 2018). The goal of graph transformation is to transform an in-
put graph in the source domain to the corresponding output graphs in the target domain via deep
learning. Emerging as a new while important problem, deep graph transformation has multiple ap-
50





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
plications in many areas, such as molecule optimization (Shi et al., 2020; Zhou et al., 2020a; Do
et al., 2019) and malware conﬁnement in cyber security (Guo et al., 2019c). Considering the entities
that are being transformed during the translation process, there are three categories of sub-problems:
node transformation, edge transformation, and node-edge-co-transformation. For node transforma-
tion, only the node set or nodes’ attributes in the input graph can change during the transformation
process. For edge transformation, only the graph topology or edge’ attributes in the input graph
can change during the transformation process. While for node-edge-co-transformation, both the
attributes of nodes and edges can change.
Graph-to-Graph for NLP Since the natural language or information knowledge graphs can be
naturally formalized as graphs with a set of nodes and their relationships, many generation tasks
in the domain of NLP can be formalized as a graph transformation problem, which can further
be solved by the graph-to-graph models. In this way, the semantic structural information of both
the input and output sentences can be fully utilized and captured. Here, two important NLP tasks
(i.e., information extraction and semantic parsing), which can be formalized as the graph-to-graph
problems, are introduced as follows.
Graph Transformation for Information Extraction. Information extraction is to extract the
structured information from a text, which usually consists of name entity recognition, relation ex-
traction and co-reference linking. The problem of information extraction can be formalized as a
graph transformation problem, where the input is the dependency or constituency graph of a text
and the output is the information graph. In input dependency or constituency graph, each node rep-
resents a word token and each edge represent the dependency relationship between two nodes. In
output information graph, each node represent a name entity and each edge represent the either the
semantic relation the co-reference link between two entities. In this way, the information extraction
is about generating the output information graph given the input dependency or constituency graph.
Graph Transformation for Semantic Parsing. The task of semantic parsing is about mapping
natural language to machine interpretable meaning representations, which in turn can be expressed
in many different formalisms, including lambda calculus, dependency-based compositional seman-
tics, frame semantics, abstract meaning representations (AMR), minimal recursion semantics, and
discourse representation theory (Fancellu et al., 2019). Explicitly or implicitly, a representation in
any of these formalisms can be expressed as a directed acyclic graph (DAG). Thus, semantic pars-
ing can also be formalized as a graph transformation problem, where the input is the dependency
or constituency graph and the output is the directed acyclic graph for semantics. For example, the
semantic formalism for AMR can be encoded as a rooted, directed, acyclic graph, where nodes
represent concepts, and labeled directed edges represent the relationships between them (Flanigan
et al., 2014; Fu et al., 2021).
Sequence-to-graph transformation can be regarded as a special case of the graph-to-graph,
where the input sequence is a line-graph. Sequence-to-graph models are popularly utilized for AMR
parsing tasks, where the goal is to learning the mapping from a sentence to its AMR graph (Zhang
et al., 2019c). To generate the AMR tree with indexed node, the approach to parsing is formalized
as a two-stage process: node prediction and edge prediction. The whole process is implemented by
an pointer-network, where the encoder is a multi-layer bi-direction-RNN and the nodes in the target
graphs are predicted in sequence. After this, the edges among each pair of nodes are predicted based
on the learnt embedding of the ending nodes.
51





LINGFEI WU AND YU CHEN , ET AL .
6.4.2 A PPROACH
In this subsection, we introduce an example graph-to-graph model in dealing with the task of infor-
mation extraction by describing its challenges and methodologies.
Challenges for Graph-to-Graph IE. There are three main challenges in solving the graph-to-
graph IE problem: (1) Different resolution between the input and output graphs. The nodes in the
input dependency graph represent word tokens, while the nodes in the output information graph
represent name entities; (2) Difﬁcult to involve both the sentence-level and word-level. To learn the
word embedding in the graph encoder, it is important to consider both the word interactions in a
sentence and the sentence interactions in a text; and (3) Difﬁcult to model the dependency between
entity relations and co-reference links in the graph decoder. The generation process of entity relation
and co-reference links are dependent on each other. For example, if words “Tom” and “He” in two
separate sentences have a co-reference link, and “Tom” and “London” has the relation of “born In”,
then “He” and “London” should also have the relation of “born In”.
Methodology. To solve the above mentioned challenges for the graph-to-graph IE task, here
we introduce an end-to-end encoder-decoder based graph-to-graph transformation model, which
transforms the input constructed graphs of text into the information graphs which contains name
entities as well as co-reference links and relations among entities. The whole model consists of
a hierarchy graph encoder for span embedding and a parallel decoder with co-reference link and
entity relation generation.
First, to construct the initial graphs, the dependency information are formalized into a hetero-
geneous graph which consists of nodes representing word tokens (i.e., word-level nodes) and nodes
representing sentences (i.e., sentence-level nodes). There are also three types of edges in the graph.
One type of edges represent the dependency relationships between word-level nodes (i.e., depen-
dency edges). One type of edges represent the adjacent relationship between sentence-level nodes
(i.e., adjacent edges). The last type of edges represent the belongingness between the word-level
and sentence-level nodes (i.e., interactive edges).
Second, the constructed heterogeneous graph is inputted into the encoder, which is based on a
hierarchy graph convolution neural network. Speciﬁcally, for each layer, the conventional message
passing operations are ﬁrst conducted along the dependency and adjacent edges to update the em-
bedding of word-level and sentence-level nodes. Then, the conventional message passing operations
are conducted along the interactive edges based on the newly updated word-level and sentence-level
nodes’ embedding. After several layers of propagation, the embedding of word-evel nodes will
contains both the dependency and sentence-level information.
Third, based on the words’ embedding from the encoder, the name entities can be ﬁrst extracted
via BIO Tagging (Marquez et al., 2005). Thus, the entity-level embedding are then constructed
by summing all of the embedding of the words it contains. Given the entity embedding, to model
the dependency between the co-reference links and relations between entities, a parallel graph de-
coder (Guo et al., 2018) that involves both co-reference link and entity relation generation processes
is utilized. Speciﬁcally, given the entity embedding hi and hj of a pair of name entities vi and vj,
the initial generated latent representation of co-reference link c0
i,j is computed as:
c0
i,j =
∑C
m=1
(σ(hm
i ¯µj) + σ(hm
j ¯νi)), (91)
where σ(hm
i ¯µj) means the deconvolution contribution of node vi to its edge representations with
node vj, which is made by the m-th entry of its node representations, and ¯µj represents one entry
52





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
of the deconvolution ﬁlter vector ¯µ∈ RN×1 that is related to node vj. The initial relation latent
representation e0
i,j between a pair of name entities vi and vj can also be computed in the same way.
C refers to the length of name entity embedding.
Given the initial latent representation of co-reference links and relations, the co-reference link
representation cl
i,j at the l-th layer is computed as follows:
cl
i,j = σ(¯φl−1
j
∑N
k1=1
[cl−1; el−1]l−1
i,k1xk1) + σ( ¯ψl
i
∑N
k2=1
[cl−1; el−1]l−1
k2,jxk1), (92)
where ¯φl−1
j
∑N
k1=1[cl−1; el−1]l−1
i,k1xk1 can be interpreted as the decoded contribution of node vi to
its edge representations with node vj, and ¯φl−1
j refers to the element of deconvolution ﬁlter vector
that is related to node vj. The output of the last “edge” deconvolution layer denotes the probability
of the existence of an edge in the target graph. All the symbols σ refers to the activation functions.
[cl−1; el−1] refers to the concatenation of all the co-reference and relation representations at(l− 1)-
th layer.
7. Applications
In this chapter, we will discuss a large variety of typical NLP applications using GNNs, including
natural language generation, machine reading comprehension, question answering, dialog system,
text classiﬁcation, text matching, topic modeling, sentiment classiﬁcation, knowledge graph, infor-
mation extraction, semantic and syntactic parsing, reasoning, and semantic role labelling. We also
provide the summary of all the applications with their sub-tasks and evaluation metrics in Table 3.
7.1 Natural Language Generation
Natural language generation (NLG) aims to generate high-quality, coherent and understandable
natural languages given various form of inputs like text, speech and etc while we only focus on
the linguistic form. Modern natural language generation methods usually take the form of encoder-
decoder, which encodes the input sequences into latent space and predicts a collection of words
based on the the latent representation. Most modern NLG pipelines can be divided into two steps:
Encoding and Decoding, which are processed by two module: encoder and decoder. In this section,
we provide a comprehensive overview of the auto-regressive graph-based methodologies which
exploit graph structures in encoder in this thriving area covering 1) neural machine translation, 2)
summarization, 3) question generation, 4) structural-data to text.
7.1.1 N EURAL MACHINE TRANSLATION
Background and Motivation The classic neural machine translation (NMT) system aims to map
the source language’s sentences into the target language without changing the semantic meaning.
Most prior works (Bahdanau et al., 2015; Luong et al., 2015) adopt the attention-based sequence-to-
sequence learning diagram, especially the RNN-based language model. Compared with the tradi-
tional machine translation models, these methods can produce much better performance without
speciﬁc linguistic knowledge. However, these methods suffer from the long-dependency prob-
lem. With the development of attention mechanism, fully-attention-based models such as Trans-
former (Vaswani et al., 2017), which captures the implicit correlations by self-attention, have made
a breakthrough and achieved a new state-of-art. Although these works achieve great success, they
53





LINGFEI WU AND YU CHEN , ET AL .
Table 3: Typical NLP applications and relevant works using GNNs
Application Task Evaluation References
NLG
Neural BLEU Bastings et al. (2017); Beck et al. (2018b); Cai and Lam (2020b)Machine Guo et al. (2019b); Marcheggiani et al. (2018); Shaw et al. (2018)Translation Song et al. (2019); Xiao et al. (2019); Xu et al. (2020b); Yin et al. (2020)
Summarization ROUGE
Xu et al. (2020a); Wang et al. (2019b); Li et al. (2020c)Fernandes et al. (2019); Wang et al. (2020b)Cui et al. (2020a); Jia et al. (2020); Zhao et al. (2020c)Jin et al. (2020a); Yasunaga et al. (2017); LeClair et al. (2020)
BLEU, METEOR
Bai et al. (2020); Jin and Gildea (2020); Xu et al. (2018a)Structural-data Beck et al. (2018b); Cai and Lam (2020a); Zhu et al. (2019b)to Text Cai and Lam (2020b); Ribeiro et al. (2019b); Song et al. (2020)Wang et al. (2020d); Yao et al. (2018); Zhang et al. (2020b)Natural QuestionBLEU, METEOR,Chen et al. (2020h); Liu et al. (2019d); Pan et al. (2020)Generation ROUGE Wang et al. (2020f); Sachan et al. (2020); Su et al. (2020)
MRC and QA
F1, Exact Match
De Cao et al. (2018); Cao et al. (2019b); Chen et al. (2020e)Machine Reading Qiu et al. (2019); Schlichtkrull et al. (2018); Tang et al. (2020b)Comprehension Tu et al. (2019a); Song et al. (2018b)Fang et al. (2020a); Zheng and Kordjamshidi (2020)Knowledge Base F1, AccuracyFeng et al. (2020a); Sorokin and Gurevych (2018a)Question Answering Santoro et al. (2017); Yasunaga et al. (2021)Open-domain Hits@1, F1 Han et al. (2020); Sun et al. (2019a, 2018a)Question AnsweringCommunity nDCG, PrecisionHu et al. (2019c, 2020b)Question Answering
Dialog Systems
Dialog State TrackingAccuracy Chen et al. (2018b, 2020a)Dialog ResponseBLEU, METEOR,Hu et al. (2019a); Bai et al. (2021)Generation ROUGENext Utterance SelectionRecall@K Liu et al. (2021b)
Text Classiﬁcation Accuracy Chen et al. (2020f); Defferrard et al. (2016); Henaff et al. (2015)Huang et al. (2019); Hu et al. (2020a); Liu et al. (2020)
Text Matching Accuracy, F1Chen et al. (2017c); Liu et al. (2019b)
Topic Modeling Topic Coherence ScoreLong et al. (2020); Yang et al. (2020)Zhou et al. (2020a); Zhu et al. (2018)
Sentiment Classiﬁcation Accuracy, F1
Zhang and Qian (2020); Pouran Ben Veyseh et al. (2020)Chen et al. (2020c); Tang et al. (2020a)Sun et al. (2019c); Wang et al. (2020c); Zhang et al. (2019b)Ghosal et al. (2020); Huang and Carley (2019); Chen et al. (2020d)
Knowledge Graph
Knowledge
Hits@N
Malaviya et al. (2020); Nathani et al. (2019a); Teru et al. (2020)Graph Bansal et al. (2019); Schlichtkrull et al. (2018); Shang et al. (2019)Completion Wang et al. (2019d,e); Zhang et al. (2020g)Knowledge Cao et al. (2019c); Li et al. (2019); Sun et al. (2020b)Graph Wang et al. (2018, 2020h); Ye et al. (2019)Alignment Xu et al. (2019b); Wu et al. (2019b)
Information Extraction
Named Entity
Precision, Recall, F1
Luo and Zhao (2020); Ding et al. (2019a); Gui et al. (2019)Recognition Jin et al. (2019); Sui et al. (2019)
Relation Extraction Qu et al. (2020); Zeng et al. (2020); Sahu et al. (2019)Guo et al. (2019a); Zhu et al. (2019c)Joint Learning Models Fu et al. (2019); Luan et al. (2019); Sun et al. (2019b)
Parsing Syntax-related Accuracy Do and Rehbein (2020); Ji et al. (2019); Yang and Deng (2020)
Semantics-related Bai et al. (2020); Zhou et al. (2020b)Shao et al. (2020); Bogin et al. (2019a,b)
Reasoning
Math Word
Accuracy
Li et al. (2020b); Lee et al. (2020); Wu et al. (2020c)Problem Solving Zhang et al. (2020c); Ferreira and Freitas (2020)Natural Language Kapanipathi et al. (2020); Wang et al. (2019c)InferenceCommonsense Zhou et al. (2018b); Lin et al. (2019b,a)Reasoning
Semantic Role Labelling Precision, Recall,Marcheggiani and Titov (2020); Xia et al. (2020); Zhang et al. (2020f)F1 Li et al. (2018b); Marcheggiani and Titov (2017); Fei et al. (2020)
54





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
rarely take the structural information into account, such as the syntactic structure. Recently, with the
help of powerful GNNs, many researchers further boost the performance by mining the structural
knowledge contained in the unstructured texts.
Methodologies Most GNN-based NMT methods cast the conventional seq2seq diagram to the
Graph2Seq architecture. They ﬁrstly convert the input texts to graph-structured data, and then
employ the GNN-based encoder to exploit the structural information. In this section, we introduce
and summarize some representative GNN-related techniques adopted in recent NMT approaches
regarding graph construction and representation learning.
• Graph Construction. Various static graphs have been introduced to the NMT task to tackle
corresponding challenges. Bastings et al. (2017); Beck et al. (2018b); Cai and Lam (2020b);
Guo et al. (2019b) ﬁrst converted the given texts into syntactic dependency graph. Such
structure doesn’t take semantic relations of words into account. Intuitively, it is beneﬁcial to
represent the redundant sentences by high-level semantic structure abstractions. To this end,
Marcheggiani et al. (2018) construct the semantic-role-labeling based dependency graph for
the given texts. What’s more, Beck et al. (2018b); Song et al. (2019) construct the AMR
graph for the sentences which can cover more semantic correlations. Besides the classic
graph types, some speciﬁcally designed graphs (app-driven graphs) are proposed to address
the unique challenges. Although source sentences in NMT are determined, either word-level
or subword-level segmentations have multiple choices to split a source sequence with differ-
ent word segments or different subword vocabulary sizes. Such a phenomenon is proposed
to affect the performance of NMT (Xiao et al., 2019). They propose the lattice graph, which
incorporates different segmentation of source sentences. Shaw et al. (2018) construct the rel-
ative position graph to explicitly model the relative position feature. Yin et al. (2020) build
the multi-modal graph to introduce visual knowledge to NMT, which presents the input sen-
tences and corresponding images in a uniﬁed graph to capture the semantic correlations better.
Despite the single-type static graph, Xu et al. (2020b) construct the hybrid graph considering
multiple relations for document-level NMT to address the severe long-dependency issue. In
detail, they construct the graph considering both intra-sentential and inter-sentential relations.
For intra-sentential relations, they link the words with sequential and dependency relations.
For inter-sentential relations, they link the words in different sentences with lexical (repeated
or similar) and coreference correlations.
• Graph Representation Learning . Most of the constructed graphs in this line are hetero-
geneous graphs, which contain multiple node or edge types and can’t be exploited directly
by typical GNNs. Thus, researchers adopt various heterogeneous graph representation tech-
niques. Bastings et al. (2017); Marcheggiani et al. (2018) regard the dependency graphs
as multi-relational graphs and apply directed-GCN to learn the graph representation. Simi-
larly, Beck et al. (2018b) ﬁrstly convert the constructed multi-relational graph to levi-graph
and apply relational GGNN, which employs edge-type-speciﬁc parameters to exploit the rich
structure information. Xu et al. (2020b) regard the edge as connectivity and treat the edge
direction as edge types, such as ”in”, ”out”, and ”self”. Then they apply relational GCN to
encode the document graph. Guo et al. (2019b) convert the heterogeneous graph to levi-graph
and adopt the densely connected GCN to learn the embedding. Song et al. (2019) propose
a special type-aware heterogeneous GGNN to learn the node embedding and edge represen-
55





LINGFEI WU AND YU CHEN , ET AL .
tation jointly. Speciﬁcally, they ﬁrst learn the edge representation by fusing both the source
node and edge type’s embeddings. Then for each node, they aggregate the representation
from its incoming and outgoing neighbors and utilize a RNN based module to update the
representation.
Besides the extension of traditional GNNs, Transformer is further explored to learn from the
structural inputs in NMT. Unlike traditional Transformer which adopt absolute sinusoidal po-
sition embedding to ensure the self-attention learn the position-speciﬁc feature, Shaw et al.
(2018); Xiao et al. (2019) adopt position-based edge embedding to capture the position cor-
relations and make the transformer learn from the graph-based inputs. Cai and Lam (2020b)
learn the bidirectional path-based relation embedding and add it to the node embedding when
calculating self-attention. They then ﬁnd the shortest path from the given graph for any two
nodes and apply bidirectional GRU to further encode the path to get the relation representa-
tion. Yin et al. (2020) apply graph-transformer-based encoder to learn the multi-modal graph.
Firstly, for text modal’s nodes, they get the initial embedding by summing up the word embed-
ding and position embedding. As for visual nodes, they apply a MLP layer to project them to
the uniﬁed space as text nodes. Secondly for each modal, they apply multi-head self-attention
to learn the intra-modal representation. Thirdly, they employ GAT-based cross-modal fusion
to learn the cross-modal representation.
• Special Techniques. In order to allow information ﬂow from both directions, some technqies
are designed for incorporating direction information. For example, Bastings et al. (2017);
Marcheggiani et al. (2018); Beck et al. (2018b) add the corresponding reverse edge as an
additional edge type ”reverse”. The self-loops edge type are also added as type ”self”. For
another example, Guo et al. (2019b) ﬁrst add a global node and the edges from this global
node to other nodes are marked with type ”global”. In addition, they further add bidirectional
sequential links with type ”forward” and ”backward” between nodes existing in the input
texts.
Benchmarks and Evaluation Common benchmarks for NMT from text include News Com-
mentary v11, WMT14, WMT16, WMT19 for training, newstest2013, newstest2015, newstest2016,
newsdev2019, newstest2019 for evaluation and testing. As for multi-modal NMT task, Multi30K
dataset (Elliott et al., 2016) is widely used by previous works. As for evaluation metrics, BLEU is
the a typical metric to evaluate the similarity between the generated and real output texts.
7.1.2 S UMMARIZATION
Background and Motivation Automatic summarization is the task of producing a concise and
ﬂuent summary while preserving key information content and overall meaning (Allahyari et al.,
2017). It is a well-noticed but challenging problem due to the need of searching in overwhelmed
textural data in real world. Broadly, there are two main classic settings in this task: 1) extractive
summarization and 2) abstractive summarization. Extractive summarization task focus on selecting
sub-sentences from the given text to reduce redundancy, which is formulated as a classiﬁcation prob-
lem. In contrast, abstractive summarization follows the neural language generation task. It normally
adopts the encoder-decoder architecture to generate the textual summary. Compared to the extrac-
tive summarization, the abstractive summarization setting is more challenging but more attractive
since it can produce non-existing expressions. Traditional approaches (Gehrmann et al., 2018; Zhou
56





---

## Part 5 — NLP Applications: First Half (Section 7 pp. 57–70: NMT, Summarization, Code, QA, Dialog, Text Classification)


GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
et al., 2018a; Liu, 2019) simply regard the inputs as sequences and apply the encoder like LSTM,
Transformer, etc. to learn the latent representation, which fail to utilize the rich structural infor-
mation implicitly existing in the natural inputs. Many researchers ﬁnd that structural knowledge is
beneﬁcial to address some troublesome challenges, e.g., long-dependency problem, and thus pro-
pose the GNN-based techniques (Wang et al., 2020b; Fernandes et al., 2019) to explicitly leverage
the structural information to boost the performance.
Methodologies Most GNN-based summarization approaches ﬁrstly construct the graph to repre-
sent the given natural texts. Then they employ GNN-based encoders to learn the graph representa-
tion. After that, for extractive summarization models, they adopt the classiﬁer to select candidate
subsentences to compose the ﬁnal summary. As for abstractive summarization, they mostly adopt
the language decoder with maximizing the outputs’ likelihood to generate the summary. In the fol-
lowing, we introduce some representative GNN-related techniques from the recent summarization
methods.
• Graph Construction. Here we introduce the different ways to construct suitable and effective
graph for different types of inputs, including sign-documents, multi-documents and codes.
Single-document based. Fernandes et al. (2019) construct the hybrid graph, including se-
quential and coreference relation. To tackle the issue such as semantic irrelevance and de-
viation, Jin et al. (2020b) construct the semantic dependency graph and cast it as the multi-
relational graph for the given texts. To capture the typical long-dependency in document-
level summarization, Xu et al. (2020a) construct the hybrid graph. They ﬁrst construct the
discourse graph by RST parsing and then add co-reference edges between co-reference men-
tions in the document. To better capture the long-dependency relation in sentence-level and
enrich the semantic correlations, Wang et al. (2020b) regards both the sentences and the con-
taining words as nodes and construct a similarity graph to model the semantic relations. To
model the redundant relation between sentences, Jia et al. (2020) propose to construct the
hybrid heterogeneous graph containing three types of nodes: 1) named entity, 2) word, and 3)
sentence as well as four types of edges: 1) sequential, 2) containing, 3) same, and 4) similar.
However, the methods above are mostly focused on the cross-sentence relations and overlook
the inter-sentence, especially the topic information. To this end, Cui et al. (2020a) and Zhao
et al. (2020c) construct the topic graph by introducing additional topic words to discover the
latent topic information. On top of that, Zhao et al. (2020c) mine the sub-graph of non-topic
nodes to represent the original texts while preserving the topic information.
Multi-document based. Yasunaga et al. (2017) decompose the given document clusters
into sentences and construct the discourse graph by Personalized Discourse Graph algorithm
(PDG). Li et al. (2020c) split the documents into paragraphs and constructs three individual
graphs: 1) similarity graph, 2) discourse graph, and 3) topic graph to investigate the effective-
ness.
Code based. To fully represent the code information in the code summarization task, Fer-
nandes et al. (2019) construct the speciﬁc code graph for the given program clips. They ﬁrst
break up the identiﬁer tokens (i.e., variables, methods, etc.) into sub-tokens by programming
language heuristics. Then they construct the graph to organize the sub-tokens according to
sequential positions and lexically usage. LeClair et al. (2020) propose another way by ﬁrstly
57





LINGFEI WU AND YU CHEN , ET AL .
parsing the given programs into abstract syntax trees (AST) and then converting them to pro-
gram graphs.
• Graph Representation Learning
In the literature of summarization tasks, both homogeneous GNNs and heterogeneous GNNs
have been explored to learn the graph representation. For homogeneous graphs, Li et al.
(2020c) apply self-attention-based GAT to learn the representation on the fully-connected
graph. Speciﬁcally, they introduce Gaussian kernel to mine the edge importance between
nodes from the graph’s topology. Zhao et al. (2020c) adopt the GAT-based graph transformer,
which regards the similarity learned by self-attention as edge weight. For heterogeneous
graphs, some researchers cast the heterogeneous graphs to homogeneous graphs by special
techniques. For example, some works(LeClair et al., 2020; Yasunaga et al., 2017; Xu et al.,
2020a) ignore both the edges and nodes’ types by treating the edge as connectivity. Cui et al.
(2020a) project the nodes to the uniﬁed embedding space to diminish the heterogeneity. After
that, some classic GNNs are employed such as GCN (Xu et al., 2020a; LeClair et al., 2020;
Yasunaga et al., 2017), GAT (Cui et al., 2020a). For example, Fernandes et al. (2019) employ
the relational GGNN to learn type-speciﬁc relations between nodes. Wang et al. (2020b); Jia
et al. (2020) ﬁrstly split the heterogeneous graph into two sub-graphs according to nodes’
type (i.e., words graph and sentence graph) and then apply GAT-based cross-attention on two
sub-graphs to learn the representation iteratively.
• Embedding Initialization The quality of the initial node embedding plays an important role
in the overall performance of GNN-based methods. For graphs whose nodes are words, most
approaches adopt the pre-trained word embeddings such as BERT (Li et al., 2020c; Xu et al.,
2020a; Cui et al., 2020a), ALBERT (Jia et al., 2020). Besides, since the topic graph (Cui et al.,
2020a) introduces additional topic nodes, they initialize them by the latent representation
of topic modeling. Jin et al. (2020b) apply Transformer to learn the contextual-level node
embedding. For nodes such as sentence-level nodes, which are composed of words, Yasunaga
et al. (2017) adopt the GRU to learn the sentences’ embedding (i.e., the node embeddings)
from the corresponding word sequences. They adopt the last hidden state as the sentences’
representation. Similarly, Wang et al. (2020b) adopt CNN to capture the ﬁne-grained n-gram
feature and then employ Bi-LSTM to get the sentences’ feature vectors. Jia et al. (2020) apply
the average pooling function to the ALBERT’s encoder outputs to represent the sentence
nodes, while Zhao et al. (2020c) initialize the nodes (utterances) by CNN and the topic words
by LDA.
Benchmarks and Evaluation Common benchmarks for automatic summarization from docu-
ments include CNN/DailyMail (See et al., 2017), NYT (Sandhaus, 2008), WikiSum (Liu et al.,
2018c), MultiNews (Fabbri et al., 2019). As for code based summarization, Java (Alon et al.,
2018) and Python (Barone and Sennrich, 2017) are widely used. As for evaluation metrics, BLEU,
ROUGE and human evaluation are commonly used.
7.1.3 S TRUCTURAL -DATA TO TEXT
Background and Motivation Despite the natural texts, many NLP applications evolve the data
which is represented by explicit graph structure, such as SQL queries, knowledge graphs, AMR,
58





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
etc. The task of structural-data is to generate the natural language from structural-data input. Tradi-
tional works (Pourdamghani et al., 2016, 2014) apply the linearization mechanisms which map the
structural-data to sequential data and adopt the Seq2Seq architecture to generate the texts. To fully
capture the rich structure information, recent efforts focus on GNN-based techniques to handle this
task. In the following, we introduce GNN techniques for three typical cases, namely AMR-to-text
generation, SQL-to-text generation and RDF-to-text generation.
Methodologies Most GNN-based AMR-to-text and SQL-to-text approaches typically construct
domain-speciﬁc graphs such as AMR graphs and SQL-parsing-based graphs to organize the inputs.
RDF-to-text generation often uses the graph structure inherent in the RDF triples. Following that,
they apply Graph2Seq consisting of GNN encoders and sequential decoders to generate neural lan-
guage outputs. This section summarizes various graph construction methods and the techniques
employed to exploit the informative graphs.
• Graph Construction. Regarding the AMR-to-text Generation, the input AMRs can be nor-
mally represented as directed heterogeneous graphs according to the relations (Damonte and
Cohen, 2019; Song et al., 2020; Bai et al., 2020; Zhu et al., 2019a; Zhang et al., 2020b; Yao
et al., 2020; Beck et al., 2018b; Cai and Lam, 2020b; Jin and Gildea, 2020; Ribeiro et al.,
2019b; Wang et al., 2020e,d; Song et al., 2018d). To incorporate the conventional GNNs
specializing in homogeneous-graph learning, Damonte and Cohen (2019); Yao et al. (2020);
Beck et al. (2018b); Cai and Lam (2020a); Ribeiro et al. (2019b) convert the AMR graphs to
levi-graph. In addition, for each edge, they (Damonte and Cohen, 2019; Beck et al., 2018b;
Yao et al., 2020; Cai and Lam, 2020a) add the reverse edges and self-loops to allow infor-
mation ﬂows in both directions. Besides the default, reverse, and self-loop edges, Yao et al.
(2020) also introduces fully-connected edges to model indirect nodes and connected edges,
which treat original edges as connectivity without direction to model connection information.
Zhao et al. (2020a) split the given AMR graphGAMR into two directed sub-graphs: 1) concept
graphGc, and 2) line graphGl. They ﬁrstly treat the edge as connectivity to get the concept
graph. Then for each edge inGAMR , they create a node inGl. Two nodes inGl are connected
if they share the same nodes in GAMR . The two sub-graphs are connected by original con-
nections inGAMR . To leverage multi-hop connection information, they preserve the 1− K
order neighbors in the adjacency matrices. Regarding the SQL inputs, the SQL queries can
be parsed by many SQL tools 1 into many sub-clauses without loss, which naturally contain
rich structure information. Xu et al. (2018a,b) construct the directed and homogeneous SQL-
graph based on the sub-clauses by some hand-craft rules. Regarding the RDF triple inputs,
Marcheggiani and Perez-Beltrachini (2018); Gao et al. (2020) treat the relation in a triple as
an additional node in the graph connecting to the subject and object entity nodes.
• Graph Representation Learning. Ribeiro et al. (2019b); Gao et al. (2020) treat the obtained
levi-graphs as directed homogeneous graphs and learn the representation by bidirectional
GNNs. Ribeiro et al. (2019b) also proposes a bidirectional embedding learning framework
that traverses the directed graphs in the original and the reversal direction. Xu et al. (2018a)
apply classic graph2seq architecture (Xu et al., 2018b) with bidirectional GraphSage methods
to learn the embedding of SQL graph via two ways, including 1) pooling-based mechanism
and 2) node-based mechanism, which means add a supernode connecting to other nodes,
1. http://www.sqlparser.com.
59





LINGFEI WU AND YU CHEN , ET AL .
to investigate the inﬂuence of graph embedding. Some approaches directly employ multi-
relational GNN to encode the obtained multi-relational graphs. For example, Damonte and
Cohen (2019) adopt directed-GCN to exploit the AMR graphs considering both heterogeneity
and parameter-overhead. Beck et al. (2018b) propose relational GGNN to capture diverse
semantic correlations. Song et al. (2018d) employ a variance of GGNN to exploit the multi-
relational AMR graphs by aggregating the bidirectional node and edge features and then
fusing them via a LSTM network. Zhao et al. (2020a) propose a heterogeneous GAT to
exploit the AMR graphs in different grains. Firstly, they apply GAT to each sub-graph to
learn the bidirectional representation separately. Then they apply cross-attention to explore
the dependencies between the two sub-graphs. Zhang et al. (2020b) propose the multi-hop
GCN, which dynamically fuses the1−K order neighbors’ features to control the information
propagate in a range of orders. Wang et al. (2020e) apply relational GAT with bidirectional
graph embedding mechanism by incorporating the edge types into the attention procedure to
learn type-speciﬁc attention weights.
Transformer architectures are also utilized to encode the AMR or SQL graphs. Yao et al.
(2018) ﬁrstly apply GAT-based graph Transformer in each homogeneous sub-graphs and then
concatenate sub-graphs representation to feed the feed-forward layer. Some works Zhu et al.
(2019a); Song et al. (2020); Bai et al. (2020); Cai and Lam (2020a); Jin and Gildea (2020)
adopt the structure-aware graph transformer (Zhu et al., 2019a; Cai and Lam, 2020b), which
injecting the relation embedding learned by shortest path to the self-attention to involve the
structure features. Speciﬁcally, Jin and Gildea (2020) explore various shortest path algorithms
to learn the relation representation of arbitrary two nodes. Similarly, Wang et al. (2020d)
employ the graph Transformer, which leverages the structure information by incorporating
the edge types into attention-weight learning formulas.
• Special Mechanisms. Damonte and Cohen (2019) apply the Bi-LSTM encoder following
the GNN encoder to further encode the sequential information. Despite the language gener-
ation procedure, to better preserve the structural information, Zhu et al. (2019a); Bai et al.
(2020); Wang et al. (2020e) introduce the graph reconstruction on top of the latent graph
representation generated by graph transformer encoder.
Benchmarks and Evaluation Common benchmarks for AMR-to-text generation task include
LDC2015E85, LDC2015E86, LDC2017T10, and LDC2020T02. As for the SQL-to-text genera-
tion task, WikiSQL (Zhong et al., 2017) and Stackoverﬂow (Iyer et al., 2016) are widely used by
previous works. The RDF-to-text generation task often uses WebNLG (Gardent et al., 2017) and
New York Times (NYT) (Riedel et al., 2010). As for evaluation metrics, the AMR-to-text generation
task mostly adopts BLEU, Meteor, CHRF++, and human evaluation including meaning similarity
and readability. While BLEU-4 are widely used for SQL-to-text task. The RDF-to-text generation
task uses BLEU, Meteor and TER.
7.1.4 N ATURAL QUESTION GENERATION
Background and Motivation The natural question generation (QG) task aims at generating nat-
ural language questions from certain form of data, such as KG (Kumar et al., 2019; Chen et al.,
2020h), tables (Bao et al., 2018), text (Du et al., 2017; Song et al., 2018a) or images (Li et al.,
2018a), where the generated questions need to be answerable from the input data. Most prior
60





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
work (Du et al., 2017; Song et al., 2018a; Kumar et al., 2019) adopts a Seq2Seq architecture which
regards the input data as sequential data without considering its rich structural information. For
instance, when encoding the input text, most previous approaches (Du et al., 2017; Song et al.,
2018a) typically ignore the hidden structural information associated with a word sequence such as
the dependency parsing tree. Even for the setting of QG from KG, most approaches (Kumar et al.,
2019) typically linearize the KB subgraph to a sequence and apply a sequence encoder. Failing to
utilize the graph structure of the input data may limit the effectiveness of QG models. As for the
multi-hop QG from text setting which requires reasoning over multiple paragraphs or documents, it
is beneﬁcial to capture the relationships among different entity mentions across multiple paragraphs
or documents. In summary, modeling the rich structures of the input data is important for many
QG tasks. Recently, GNNs have been successfully applied to the QG tasks (Liu et al., 2019d; Chen
et al., 2020g; Wang et al., 2020g).
Methodologies Most GNN-based QG approaches adopt a Graph2Seq architecture where a GNN-
based encoder is employed to model the graph-structured input data, and a sequence decoder is
employed to generate a natural language question. In this section, we introduce and summarize
some representative GNN-related techniques adopted in recent QG approaches.
• Graph Construction. Different graph construction strategies have been proposed to suit the
various needs of different QG settings by prior GNN-based approaches. Some works (Liu
et al., 2019d; Wang et al., 2020g; Chen et al., 2020g; Pan et al., 2020) converted the pas-
sage text to a graph based on dependency parsing or semantic role labeling for QG from text.
As for multi-hop QG from text, in order to model the relationships among entity mentions
across multiple paragraphs or documents, an entity graph is often constructed. For instance,
Su et al. (2020) constructed an entity graph with the named entities in context as nodes and
edges connecting the entity pairs appearing in the same sentence or paragraph. In addition, an
answer-aware dynamic entity graph was created on the ﬂy by masking out entities irrelevant
to the answers. Sachan et al. (2020) built a so-called context-entity graph containing three
types of nodes (i.e., named-entity mentions, coreferent entities, and sentence-ids) and added
edges connecting them. Unlike the above approaches that build a static graph based on prior
knowledge, Chen et al. (2020g) explored dynamic graph construction for converting the pas-
sage text to a graph of word nodes by leveraging the attention mechanism. As for QG from
KG, graph construction is not needed since the KG is already provided. A common option is
to extract a k-hop subgraph surrounding the topic entity as the input graph when generating a
question (Chen et al., 2020h).
• Graph Representation Learning. Common GNN models used by existing QG approaches
include GCN (Liu et al., 2019d; Su et al., 2020), GAT (Wang et al., 2020g), GGNN (Chen
et al., 2020g,h; Pan et al., 2020), and graph transformer (Sachan et al., 2020). In order to
model the edge direction information, Chen et al. (2020g) and Chen et al. (2020h) extended
the GGNN model to handle directed edges. In order to model multi-relational graphs, Chen
et al. (2020h) explored two graph encoding strategies: i) converting a multi-relational graph
to a Levi graph (Levi, 1942) and applying a regular GGNN model, or ii) extending the GGNN
model by incorporating the edge information in the message passing process. Pan et al.
(2020) also extended the GGNN model by bringing in the attention mechanism from GAT
and introducing edge type aware linear transformations for message passing between node
61





LINGFEI WU AND YU CHEN , ET AL .
pairs. Sachan et al. (2020) proposed a graph-augmented transformer model employing a
relation-aware multi-head attention mechanism similar to Zhu et al. (2019b); Cai and Lam
(2020b). Pan et al. (2020); Sachan et al. (2020) found it beneﬁcial to additionally model the
sequential information in the input text besides the graph-structured information. Pan et al.
(2020) separately applied a sequence encoder to the document text, and a graph encoder to
the semantic graph representation of the document constructed from semantic role labeling or
dependency parsing. The outputs of the sequence encoder and graph encoder would then be
fused and fed to a sequence decoder for question generation. The model was jointly trained on
question decoding and content selection sub-tasks. Sachan et al. (2020) ran both the structure-
aware attention network on the input graph and the standard attention network on the input
sequence, and fused their output embeddings using some non-linear mapping function to learn
the ﬁnal embeddings for the sequence decoder. During the training, a contrastive objective
was proposed to predict supporting facts, serving as a regularization term in addition to the
main cross-entropy loss for sequence generation.
Benchmarks and Evaluation Common benchmarks for QG from text include SQuAD (Rajpurkar
et al., 2016), NewsQA (Trischler et al., 2017), and HotpotQA (Yang et al., 2018a). As for QG from
KG, WebQuestions (Kumar et al., 2019) and PathQuestions (Kumar et al., 2019) are widely used by
previous works. As for evaluation metrics, BLEU-4, METEOR, ROUGE-L and human evaluation
(e.g., syntactically correct, semantically correct, relevant) are common metrics. Complexity is also
used to evaluate the performance of multi-hop QG systems.
7.2 Machine Reading Comprehension and Question Answering
7.2.1 M ACHINE READING COMPREHENSION
Background and Motivation The task of Machine Reading Comprehension (MRC) aims to an-
swer a natural language question using the given passage. Signiﬁcant progress has been made in the
MRC task thanks to the development of various (co-)attention mechanisms that capture the interac-
tion between the question and context (Hermann et al., 2015; Cui et al., 2017; Seo et al., 2017; Xiong
et al., 2017b). Considering that the traditional MRC setting mainly focuses on one-hop reasoning
which is relatively simple, recently, more research efforts have been made to solve more challeng-
ing MRC settings. For instance, the multi-hop MRC task is to answer a natural language question
using multiple passages or documents, which requires the multi-hop reasoning capacity. The con-
versational MRC task is to answer the current natural language question in a conversation given a
passage and the previous questions and answers, which requires the capacity of modeling conver-
sation history. The numerical MRC task requires the capacity of performing numerical reasoning
over the passage. These challenging MRC tasks call for the learning capacity of modeling complex
relations among objects. For example, it is beneﬁcial to model relations among multiple documents
and the entity mentions within the documents for the multi-hop MRC task. Recently, GNNs have
been successfully applied to various types of MRC tasks including multi-hop MRC (Song et al.,
2018b; Cao et al., 2019a; Qiu et al., 2019; Cao et al., 2019b; Fang et al., 2020b; Tang et al., 2020c;
Zheng and Kordjamshidi, 2020; Tu et al., 2019b; Ding et al., 2019b), conversational MRC (Chen
et al., 2020e), and numerical MRC (Ran et al., 2019).
Methodologies GNN-based MRC approaches typically operate by ﬁrst constructing an entity
graph or hierarchical graph capturing rich relations among nodes in the graph, and then apply-
62





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
ing a GNN-based reasoning module for performing complex reasoning over the graph. Assuming
the GNN outputs already encode the semantic meanings of the node itself and its neighboring struc-
ture, a prediction module will ﬁnally be applied for predicting answers. The graph construction
techniques and graph representation techniques developed for solving the MRC task vary between
different approaches. In this section, we introduce and summarize some representative GNN-related
techniques adopted in recent MRC approaches.
• Graph Construction . In order to apply GNNs for complex reasoning in the MRC task,
one critical step is graph construction. Building a high-quality graph capturing rich relations
among useful objects (e.g., entity mentions, paragraphs) is the foundation for conducting
graph-based complex reasoning. Most GNN-based MRC approaches conduct static graph
construction by utilizing domain-speciﬁc prior knowledge. Among all existing GNN-based
MRC approaches, the most widely adopted strategy for static graph construction is to con-
struct an entity graph using carefully designed rules. These approaches (Song et al., 2018b;
Cao et al., 2019a; Qiu et al., 2019; Cao et al., 2019b; Tang et al., 2020c; Zheng and Kord-
jamshidi, 2020; Ran et al., 2019) usually extract entity mentions from questions, paragraphs
and candidate answers (if given) as nodes, and connect the nodes with edges capturing dif-
ferent types of relations such as exact match, co-occurrence, coreference and semantic role
labeling. Edge connectivity with different granularity levels in terms of context window (e.g.,
sentence, paragraph and document) might also be distinguished for better modeling perfor-
mance (Qiu et al., 2019; Cao et al., 2019b). For instance, Cao et al. (2019b) distinguished
cross-document edge and within-document edge when building an entity graph. As for the
numerical MRC task, the most important relations are probably the arithmetic relations. In
order to explicitly model numerical reasoning, Ran et al. (2019) constructed a graph con-
taining numbers in the question and passage as nodes, and added edges to capture various
arithmetic relations among the numbers. Besides building an entity graph capturing various
types of relations among entity mentions, some approaches (Tu et al., 2019b; Fang et al.,
2020b; Zheng et al., 2020) opt to build a hierarchical graph containing various types of nodes
including entity mentions, sentences, paragraphs and documents, and connect these nodes
using predeﬁned rules. For example, Zheng et al. (2020) constructed a hierarchical graph that
contains edges connecting token nodes and sentence nodes, sentence nodes and paragraph
nodes as well as paragraph nodes and document nodes.
Very recently, dynamic graph construction techniques without relying on hand-crafted rules
have also been explored for the MRC task and achieved promising results. Unlike static graph
construction techniques that have been widely explored in the MRC literature, dynamic graph
construction techniques are less studied. In comparison to static graph construction, dynamic
graph construction aims to build a graph on the ﬂy without relying on domain-speciﬁc prior
knowledge, and is typically jointly learned with the remaining learning modules of the system.
Recently, Chen et al. (2020e) proposed a GNN-based model for the conversational MRC task,
which is able to dynamically build a question and conversation history aware passage graph
containing each passage word as a node at each conversation turn by leveraging the attention
mechanism. A kNN-style graph sparsiﬁcation operation was conducted so as to further extract
a sparse graph from the fully-connected graph learned by the attention mechanism. The
learned sparse graph will be consumed by the subsequent GNN-based reasoning module, and
the whole system is end-to-end trainable.
63





LINGFEI WU AND YU CHEN , ET AL .
• Graph Representation Learning. Most GNN-based MRC approaches rely on a GNN model
for performing complex reasoning over the graph. In the literature of the MRC task, both ho-
mogeneous GNNs and multi-relational GNNs have been explored for node representation
learning. Even though most GNN-based MRC approaches construct a multi-relational or het-
erogeneous graph, some of them still apply a homogeneous GNN model such as GCN (Zheng
and Kordjamshidi, 2020; Ding et al., 2019b), GAT (Qiu et al., 2019; Fang et al., 2020b; Zheng
et al., 2020) and Graph Recurrent Network (GRN) (Song et al., 2018b). Unlike other works
that apply a GNN model to a single graph, Chen et al. (2020e) proposed a Recurrent Graph
Neural Network (RGNN) for processing a sequence of passage graphs for modeling conver-
sational history. The most widely used multi-relational GNN model in the MRC task is the
RGCN model (Schlichtkrull et al., 2018). Many approaches (Cao et al., 2019a,b; Tu et al.,
2019b; Ran et al., 2019) adopt a gating RGCN variant which in addition introduces a gating
mechanism regulating how much of the update message propagates to the next step. Tang
et al. (2020c) further proposed a question-aware gating mechanism for RGCN, that is able
to regulate the aggregated message according to the question, and even bring the question
information into the update message.
• Node Embedding Initialization . Many studies have shown that the quality of the initial
node embeddings play an important role in the overall performance of GNN-based models.
Most approaches use pre-trained word embeddings such as GloVe (Pennington et al., 2014),
ELMo (Peters et al., 2018), BERT (Devlin et al., 2019) and RoBERTa (Liu et al., 2019c)
to initialize tokens. Some works (Cao et al., 2019b; Chen et al., 2020e) also concatenated
linguistic features to word embeddings to enrich the semantic meanings. On top of the initial
word embeddings, most approaches choose to further apply some transformation functions
such as MLP for introducing nonlinearity (Tang et al., 2020c), BiLSTM for capturing local
dependency of the text (Cao et al., 2019a; Chen et al., 2020e; Fang et al., 2020b), co-attention
layer for fusing questions to passages (Qiu et al., 2019; Tu et al., 2019b; Chen et al., 2020e;
Fang et al., 2020b).
• Special Techniques In order to increase the richness of the supervision signals, some ap-
proaches adopt the multi-tasking learning strategy to predict not only the answer span, but
also the supporting paragraph/sentence/fact and answer type (Qiu et al., 2019; Fang et al.,
2020b; Zheng and Kordjamshidi, 2020; Chen et al., 2020e).
Benchmarks and Evaluation Common multi-hop MRC benchmarks include HotpotQA (Yang
et al., 2018a), WikiHop (Welbl et al., 2018) and ComplexWebQuestions (Talmor and Berant, 2018).
Common conversational MRC benchmarks include CoQA (Reddy et al., 2019), QuAC (Choi et al.,
2020) and DoQA (Campos et al., 2019). DROP (Dua et al., 2019) is a benchmark created for
the numerical MRC task. As for evaluation metrics, F1 and EM (i.e., exact match) are the two
most widely used evaluation metrics for the MRC task. Besides, the Human Equivalence Score
(HEQ) (Choi et al., 2020; Campos et al., 2019) is used to judge whether a system performs as well
as an average human. HEQ-Q and HEQ-D are accuracies at the question level and dialog level,
respectively.
64





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
7.2.2 K NOWLEDGE BASE QUESTION ANSWERING
Background and Motivation Knowledge Base Question Answering (KBQA) has emerged as an
important research topic in the past few years (Yih et al., 2015; Zhang et al., 2018a; Chen et al.,
2019). The goal of KBQA is to automatically ﬁnd answers from the KG given a natural language
question. Recently, due to its nature capability of modeling relationships among objects, GNNs
have been successfully applied for performing the multi-hop KBQA task which requires reasoning
over multiple edges of the KG to arrive at the right answer. A relevant task is open domain QA (Sun
et al., 2018a, 2019a) which aims to answer open domain questions by leveraging hybrid knowledge
sources including corpus and KG. Here we only focus on the QA over KG setting, while the GNN
applications in the open domain QA task will be introduced in other sections.
Methodologies In this section, we introduce and summarize some representative GNN-related
techniques adopted in the recent KBQA research.
• Graph Construction. Semantic parsing based KBQA methods (Yih et al., 2015) aims at con-
verting natural language questions to a semantic graph which can be further executed against
the KG to ﬁnd the correct answers. In order to better model the structure of the semantic
graph, Sorokin and Gurevych (2018b) proposed to use GNNs to encode the candidate seman-
tic graphs. Speciﬁcally, they used a similar procedure as Yih et al. (2015) to construct multiple
candidate semantic graphs given the question, and chose the one which has the highest match-
ing score to the question in the embedding space. Feng et al. (2020b); Yasunaga et al. (2021)
focused on a different multi-choice QA setting which is to select the correct answer from the
provided candidate answer set given the question and the external KG. For each candidate
answer, Feng et al. (2020b) proposed to extract from the external KG a “contextualized” sub-
graph according to the question and candidate answer. This subgraph serves as the evidence
for selecting the corresponding candidate answer as the ﬁnal answer. Speciﬁcally, they ﬁrst
recognized all the entity mentions in the question and candidate answer set, and linked them
to entities in the KG. Besides these linked entities in the KG, any other entities that appeared
in any two-hop paths between pairs of mentioned entities in the KG as well as the correspond-
ing edges were also added to the subgraph. Yasunaga et al. (2021) constructed a joint graph
by regarding the QA context as an additional node (QA context node) and connecting it to the
topic entities in the KG subgraph. Speciﬁcally, they introduced two new relation types rz,q
and rz,a for capturing the relationship between the QA context node and the relevant entities
in the KG. The speciﬁc relation type is determined by whether the KG entity is found in the
question portion or the answer portion of the QA context.
• Graph Representation Learning In order to better model the constructed multi-relational
or heterogeneous graphs, basic GNNs need to be extended to handle edge types or node
types. To this end, Sorokin and Gurevych (2018b) extended GGNN (Zhang et al., 2020e) to
include edge embeddings in message passing. After learning the vector representations of
both the question and every candidate semantic graph, they used a simple reward function to
select the best semantic graph for the question. The ﬁnal node embedding of the question
variable node (q-node) in each semantic graph was extracted and non-linearly transformed
to obtain the graph-level representation. Feng et al. (2020b) designed a Multi-hop Graph
Relation Network (MHGRN) to unify both GNNs and path-based models. Speciﬁcally, they
considered both node type and edge type information of the graph by introducing node type
65





LINGFEI WU AND YU CHEN , ET AL .
speciﬁc linear transformation, and node type and relation type aware attention in message
passing. In addition, instead of performing one hop message passing at each time, inspired by
path-based models (Santoro et al., 2017; Lin et al., 2019b), they proposed to pass messages
directly over all the paths of lengths up to K. Graph-level representations were obtained
via attentive pooling over the output node embeddings, and would be concatenated with the
text representation of question and each candidate answer to compute the plausibility score.
Similarly, Yasunaga et al. (2021) extended GAT by introducing node type and edge type aware
message passing to handle multi-relational graphs. They in addition employed a pre-trained
language model for KG node relevance scoring in the initial stage and ﬁnal answer selection
stage.
Benchmarks and Evaluation Common benchmarks for KBQA include WebQuestionsSP (Yih
et al., 2016), MetaQA (Zhang et al., 2018a), QALD-7 (Usbeck et al., 2017), CommonsenseQA (Tal-
mor et al., 2019), and OpenbookQA (Mihaylov et al., 2018). F1 and accuracy are common metrics
for evaluating KBQA methods.
7.2.3 O PEN -DOMAIN QUESTION ANSWERING
Background and Motivation The task of open-domain question answering aims to identify an-
swers to the natural question given a large scale of open-domain knowledge (e.g. documents,
knowledge base and etc.). Untill recent times, the open-domain question answering (Bordes et al.,
2015; Zhang et al., 2018a) has been mostly exploited through knowledge bases such as Personalized
PageRank (Haveliwala, 2002), which actually closely related to the Knowledge based Question An-
swering task (KBQA) in techniques. The knowledge based methods beneﬁt from obtaining external
knowledge easily through graph structure. However, these methods limit in the missing information
of the knowledge base and ﬁxed schema. Other attempts have been made to answer questions from
massive and unstructured documents (Chen et al., 2017a). Compared to the KB based methods,
these methods can fetch more information but suffer from the difﬁculty of retrieve relevant and key
information from redundant external documents.
Methodologies In this section, we introduce and summarize some representative GNN-related
techniques in the recent open-domain question answering research.
• Graph Construction. Most of the GNN based methods address the mentioned challenges
by constructing a heterogeneous graph with both knowledge base and unstructured docu-
ments (Han et al., 2020; Sun et al., 2018a, 2019a). Han et al. (2020); Sun et al. (2018a) ﬁrstly
extract the subgraph from external knowledge base named Personalized PageRank (Haveli-
wala, 2002). Then they fetch a relevant text corpus from Wikipedia and fuse them to the
knowledge graph. Speciﬁcally, they represent the documents by words’ encoding and link
the nodes (the nodes in the knowledge graph are entities) which appear in the document.
Sun et al. (2019a) propose a iteratively constructed heterogeneous graph method from both
knowledge base and text corpus. Initially, the graph depends only on the question. Then for
each iteration, they expand the subgraph by choosing nodes from which to ”pull” information
about, from the KB or corpus as appropriate.
• Graph Representation Learning Sun et al. (2018a, 2019a) ﬁrst initialize the nodes’ embed-
ding with pre-trained weight for entities and LSTM encoding for documents. They further
66





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
propose different update rule for both entities and documents. For entities, they apply R-
GCN (Schlichtkrull et al., 2018) on the sub-graph only from the knowledge base and then
take average of the linked words’ feature in the connected documents. The entities’ represen-
tation is the combination of: 1) the previous entities themselves’ representation, 2) question
encoding, 3) knowledge-subgraph’s aggregation results, and 4) related documents’ aggrega-
tion results. For documents’ update operation, they aggregate the features from connected
entities. Sun et al. (2018a) adopt similar idea for heterogeneous graph representation learn-
ing. Technically, before encoding entities, they incorporate the connected words’ embedding
in the documents to the entities. Then for nodes, they propose GCN with attention weight to
aggregate neighbor entities. Note that the question is employed in the attention mechanism to
guide the learning process. The documents’ updating process is in the same pattern.
Benchmarks and Evaluation Common benchmarks for Open-domain Question answering in-
clude WebQuestionsSP (Yih et al., 2016), MetaQA (Zhang et al., 2018a), Complex WebQues-
tions 1.1 (Complex WebQ) (Talmor and Berant, 2018), and WikiMovies-10K (Miller et al., 2016).
Hits@1 and F1 scores are the common evaluation metrics for this task (Sun et al., 2018a, 2019a;
Han et al., 2020).
7.2.4 C OMMUNITY QUESTION ANSWERING
Background and Motivation The task of community question answering aims to retrieve the
relevant answer from QA forums such as Stack Overﬂow or Quora. Different from the traditional
MRC (QA) task, CQA systems are able to harness tacit knowledge (embedded in their diverse com-
munities) or explicit knowledge (embedded in all resolved questions) in answering of an enormous
number of new questions posted each day. Nevertheless, the growing number of new questions
could make CQA systems without appropriate collaboration support become overloaded by users’
requests.
Methodologies In this section, we introduce and summarize some representative GNN-related
techniques adopted in the recent CQA research.
• Graph Construction. Most of the GNN-based methods construct a multi-modal graph for
existing question/answer pairs (Hu et al., 2019d, 2020c). For the given q/a pair (q, a), both of
them construct the question/answerGq/Ga graph separately. Since in real community based
forums, the question/answer pairs may contain both visual and text contents, they employ a
multi-modal graph to represent them jointly. Hu et al. (2019d) ﬁrstly employ object detection
models such as YOLO3 (Redmon and Farhadi, 2018) to fetch visual objects. The objects are
represented by their labels (visual words more accurately). The visual objects are treated as
words in the answers which are modeled with textural contents equally. Then they regard
each textural words as vertex and link them with undirected occurrence edges. Hu et al.
(2020c) adopt the same idea as (Hu et al., 2019d) for building occurrence graph for both
textural contents and visual words. But for extracting visual words from images, they employ
unsupervised Meta-path Link Prediction for Visual Labeling. Concretely, they deﬁne the
meta-path over image and words and build the heterogeneous image-word graph.
• Graph Representation Learning. Most of the GNN-based community question answering
models adapt the GNN models to capture structure information. Given the question/answer
67





LINGFEI WU AND YU CHEN , ET AL .
pair (q, a), Hu et al. (2019d) stacks the graph pooling network to capture the hierarchical
semantic-level correlations between nodes. Conceptually, the graph pooling network extract
the high-level semantic representation for both question and answer graphs. Formally, it con-
sists of two GCN-variant APPNP (Klicpera et al., 2019) encoders. Generally, one APPNP
is employed to learn the high-level semantic cluster distribution for each vertex. The other
APPNP network is used to learn the immediate node representation. The ﬁnal node represen-
tation is the fusion of the two encoders’ results. Hu et al. (2020c) employ the APPNP to learn
the importance of each vertex’s neighbors.
Benchmarks and Evaluation Common benchmarks for Community Question Answering in-
clude Zhihu and Quora released by MMAICM (Hu et al., 2018). The normalized discounted
cumulative gain (nDCG) and precision are common metrics for evaluating Community Question
Answering methods (Hu et al., 2018, 2020c, 2019d).
7.3 Dialog Systems
Background and Motivation Dialog system (Williams et al., 2014; Chen et al., 2017b) is a com-
puter system that can continuously converse with a human. In order to build a successful dialog
system, it is important to model the dependencies among different interlocutors or utterances within
a conversation. Due to the ability of modeling complex relations among objects, recently, GNNs
have been successfully applied to various dialog system related tasks including dialog state track-
ing (Chen et al., 2018b, 2020a) which aims at estimating the current dialog state given the conver-
sation history, dialog response generation (Hu et al., 2019a) which aims at generating the dialog
response given the conversation history, and next utterance selection (Liu et al., 2021b) which aims
at selecting the next utterance from a candidate list given the conversation history.
Methodologies In this section, we introduce and summarize some representative GNN-related
techniques adopted in the recent dialog systems research.
• Graph Construction. Building a high-quality graph representing a structured conversation
session is challenging. A real-world conversation can have rich interactions among speakers
and utterances. Here, we introduce both static and dynamic graph construction techniques
used in recent GNN-based approaches. For static graphs, most GNN-based dialog systems
rely on prior domain knowledge to construct a graph. For instance, in order to apply GNNs
to model multi-party dialogues (i.e., involving multiple interlocutors), Hu et al. (2019a) con-
verted utterances in a structured dialogue session to a directed graph capturing response rela-
tionships between utterances. Speciﬁcally, they created an edge for every pair of utterances
from the same speaker following the chronological order of the utterances. Chen et al. (2018b)
built a directed heterogeneous graph according to the domain ontology that consists of edges
among slot-dependent nodes and slot-independent nodes. Chen et al. (2020a) constructed
three types of graphs including a token-level schema graph according to the original ontol-
ogy scheme, a utterance graph according to the dialogue utterance, and a domain-speciﬁc
slot-level schema graph connecting two slots from the same domain or share the same candi-
date values. Liu et al. (2021b) constructed a graph connecting utterance nodes that are adja-
cent or belong to dependent topics. Regarding the dynamic graph construction, unlike most
GNN-based approaches that rely on prior knowledge for constructing static graph, Chen et al.
(2018b) jointly optimized the graph structure and the parameters of GNN by approximating
68





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
posterior probability of the adjacency matrix (i.e., modeled as a latent variable following a
factored Bernoulli distribution) via variational inference (Hoffman et al., 2013).
• Graph Representation LearningVarious GNN models have been applied in dialog systems.
For instance, Liu et al. (2021b) applied GCN to facilitate reasoning over all utterances. Chen
et al. (2020a) proposed a graph attention matching network to learn the representations of
ontology schema and dialogue utterance simultaneously, and a recurrent attention graph neu-
ral network which employs a GRU-like gated cell for dialog state updating. Inspired by the
hierarchical sequence-based HRED model for dialog response generation, Hu et al. (2019a)
proposed an utterance-level graph-structured encoder which is a gated GNN variant, and is
able to control how much the new information (from the preceding utterance nodes) should
be considered when updating the current state of the utterance node. They also designed a
bi-directional information ﬂow algorithm to allow both forward and backward message pass-
ing over the directed graph. In order to model multi-relational graphs, Chen et al. (2018b)
designed a R-GCN like GNN model employing edge type speciﬁc weight matrices.
• Node Embedding Initialization In terms of node embedding initialization for GNN models,
Hu et al. (2019a) applied a BiLSTM to ﬁrst encode the local dependency information in the
raw text sequence. Liu et al. (2021b) used the state-of-the-art pre-trained ALBERT embed-
dings (Lan et al., 2019) to initialize the node embeddings. Chen et al. (2020a) included token
embeddings, segmentation embeddings as well as position embeddings to capture the rich
semantic meanings of the nodes.
Benchmarks and Evaluation Common dialog state tracking benchmarks include PyDial (Casanueva
et al., 2017) and MultiWOZ (Budzianowski et al., 2018; Eric et al., 2020). Ubuntu Dialogue Cor-
pus (Lowe et al., 2015) and MuTual (Cui et al., 2020b) are often used for evaluating dialog response
generation and next utterance selection systems. As for evaluation metrics, BLEU, METEOR and
ROUGE-L are common metrics for evaluating dialog response generation systems. Besides auto-
matic evaluation, human evaluation (e.g., grammaticality, ﬂuency, rationality) is often conducted.
Accuracy is the most widely used metric for evaluating dialog state tracking systems. Recall at k is
often used in the next utterance selection task.
7.4 Text Classiﬁcation
Background and Motivation Traditional text classiﬁcation methods heavily rely on feature en-
gineering (e.g., BOW, TF-IDF or more advanced graph path based features) for text representation.
In order to learn “good” representations from text, various unsupervised approaches have been pro-
posed for word or document representation learning, including word2vec (Mikolov et al., 2013),
GloVe (Pennington et al., 2014), topic models (Blei et al., 2003; Larochelle and Lauly, 2012), au-
toencoder (Miao et al., 2016; Chen and Zaki, 2017), and doc2vec (Le and Mikolov, 2014; Kiros
et al., 2015). These pre-trained word or document embeddings can further be consumed by a
MLP (Joulin et al., 2017), CNN (Kim, 2014) or LSTM (Liu et al., 2016; Zhang et al., 2018b)
module for training a supervised text classiﬁer. In order to better capture the relations among words
in text or documents in corpus, various graph-based approaches have been proposed for text clas-
siﬁcation. For instance, Peng et al. (2018) proposed to ﬁrst construct a graph of words, and then
apply a CNN to the normalized subgraph. Tang et al. (2015) proposed a network embedding based
69





LINGFEI WU AND YU CHEN , ET AL .
approach for text representation learning in a semi-supervised manner by converting a partially la-
beled text corpora to a heterogeneous text network. Recently, given the strong expressive power,
GNNs have been successfully applied to both semi-supervised (Yao et al., 2019b; Liu et al., 2020;
Hu et al., 2019e) and supervised (Defferrard et al., 2016; Huang et al., 2019; Zhang et al., 2020e)
text classiﬁcation.
Methodologies GNN-based text classiﬁcation approaches typically operate by ﬁrst constructing
a document graph or corpus graph capturing rich relations among nodes in the graph, and then
applying a GNN to learn good document embeddings which will later be fed into a softmax layer
for producing a probabilistic distribution over a class of labels. The graph construction techniques
and graph representation techniques developed for solving the text classiﬁcation task vary between
different approaches. In this section, we introduce and summarize some representative GNN-related
techniques adopted in recent text classiﬁcation approaches.
• Graph Construction. Semi-supervised text classiﬁcation leverages a small amount of la-
beled data with a large amount of unlabeled data during training. Utilizing the relations among
labeled and unlabeled documents is essential for performing well in this semi-supervised set-
ting. Regarding the static graph construction, recently, many GNN-based semi-supervised
approaches (Yao et al., 2019b; Liu et al., 2020; Hu et al., 2019e) have been proposed for
text classiﬁcation to better model the relations among words and documents in the corpus.
These approaches typically construct a single heterogeneous graph for the whole corpus con-
taining word nodes and document nodes, and connect the nodes with edges based on word
co-occurrence and document-word relations (Yao et al., 2019b; Liu et al., 2020). Hu et al.
(2019e) proposed to enrich the semantics of the short text with additional information (i.e.,
topics and entities), and constructed a Heterogeneous Information Network (HIN) contain-
ing document, topic and entity nodes with document-topic, document-entity and entity-entity
edges based on several predeﬁned rules. One limitation of semi-supervised text classiﬁcation
is its incapability of handling unseen documents in the testing phase. In order to handle the
inductive learning setting, some GNN-based approaches (Defferrard et al., 2016; Huang et al.,
2019; Zhang et al., 2020e) proposed to instead build an individual graph of unique words for
each document by leveraging word similarity or co-occurrence between words within cer-
tain ﬁxed-sized context window. In comparison to static graph construction, dynamic graph
construction does not rely on domain-speciﬁc prior knowledge, and the graph structure can
be jointly learned with the remaining learning modules of the system. Henaff et al. (2015)
proposed to jointly learn a graph of unique words for each input text using a Gaussian kernel.
Chen et al. (2020f) proposed to regard each word in text as a node in a graph, and dynamically
build a graph for each document.
• Graph Representation Learning Early graph-based text classiﬁcation approaches (Henaff
et al., 2015; Defferrard et al., 2016) were motivated by extending CNNs to graph CNNs
which can directly model graph-structured textual data. With the fast growth of the GNN
research, recent work started to explore various GNN models for text classiﬁcation including
GCN (Yao et al., 2019b; Chen et al., 2020f), GGNN (Zhang et al., 2020e) and message passing
mechanism (MPM) (Huang et al., 2019). Liu et al. (2020) introduced a TensorGCN which
ﬁrst performs intra-graph convolution propagation and then performs inter-graph convolution
70





---

## Part 6 — NLP Applications: Second Half + Challenges, Future Directions, Conclusion (Section 7 cont. pp. 71–83, Sections 8–9 pp. 84–88)


GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
propagation. Hu et al. (2019e) proposed a Heterogeneous GAT (HGAT) based on a dual-level
(i.e., node-level and type-level) attention mechanism.
• Node Embedding Initialization Node embedding initialization is critical for the GNN per-
formance. Interestingly, Yao et al. (2019b) observed in their experiments that by using only
one-hot representation, a vanilla GCN (Yao et al., 2019b) without any external word em-
beddings or knowledge already outperformed state-of-the-art methods for text classiﬁcation.
Nevertheless, most GNN-based approaches (Defferrard et al., 2016; Hu et al., 2019e; Huang
et al., 2019; Liu et al., 2020; Zhang et al., 2020e) still use pre-trained word embeddings to ini-
tialize node embeddings. Chen et al. (2020f) further applied a BiLSTM to a sequence of word
embeddings to capture the contextual information of text for node embedding initialization.
• Special Techniques As a common trick used in text classiﬁcation, some GNN-based ap-
proaches removed stop words during preprocessing (Henaff et al., 2015; Yao et al., 2019b;
Zhang et al., 2020e).
Benchmarks and Evaluation Common benchmarks for evaluating text classiﬁcation methods
include 20NEWS (Lang, 1995), Ohsumed (Hersh et al., 1994), Reuters (Lewis et al., 2004), Movie
Review (MR) (Pang and Lee, 2004), AGNews (Zhang et al., 2015), Snippets (Phan et al., 2008),
TagMyNews (Vitale et al., 2012), and Twitter1. Accuracy is the most common evaluation metric.
7.5 Text Matching
Background and Motivation Most existing text matching approaches operate by mapping each
text into a latent embedding space via some neural networks such as CNNs (Hu et al., 2014; Pang
et al., 2016) or RNNs (Wan et al., 2016), and then computing the matching score based on the
similarity between the text representations. In order to model the rich interactions between two
texts at different granularity levels, sophisticated attention or matching components are often care-
fully designed (Lu and Li, 2013; Palangi et al., 2016; Yang et al., 2016). Recently, there are a
few works (Chen et al., 2020i; Liu et al., 2019b) successfully exploring GNNs for modeling the
complicated interactions between text elements in the text matching literature.
Methodologies In this section, we introduce and summarize some representative GNN-related
techniques adopted in recent text matching approaches.
• Graph Construction Chinese short text matching heavily relies on the quality of word seg-
mentation. Instead of segmenting each sentence into a word sequence during preprocessing
which can be erroneous, ambiguous or inconsistent, Chen et al. (2020i) proposed to con-
struct a word lattice graph from all possible segmentation paths. Speciﬁcally, the word lattice
graph contains all character subsequences that match words in a lexicon as nodes, and adds
an edge between two nodes if they are adjacent in the original sentence. As a result, the
constructed graph encodes multiple word segmentation hypotheses for text matching. In or-
der to tackle long text matching, Liu et al. (2019b) proposed to organize documents into a
graph of concepts (i.e., a keyword or a set of highly correlated keywords in a document), and
built a concept interaction heterogeneous graph that consists of three types of edges includ-
ing keyword-keyword, keyword-concept and sentence-concept edges. Speciﬁcally, they ﬁrst
1. https://www.nltk.org/
71





LINGFEI WU AND YU CHEN , ET AL .
constructed a keyword co-occurrence graph, and based on that, they grouped keywords into
concepts by applying community detection algorithms on the keyword co-occurrence graph.
Finally, they assigned each sentence to the most similar concept.
• Graph Representation Learning Liu et al. (2019b) applied a GCN model to learn mean-
ingful node embeddings in the constructed graph. Chen et al. (2020i) designed a GNN-based
graph matching module which allows bidirectional message passing across nodes in both text
graphs. In order to obtain graph-level embeddings from the learned node embeddings, max
pooling (Liu et al., 2019b) or attentive pooling (Chen et al., 2020i) techniques were adopted.
• Node Embedding Initialization As for node embedding initialization, Chen et al. (2020i)
used the BERT embeddings while Liu et al. (2019b) ﬁrst computed a match vector for each
node in the graph.
Benchmarks and Evaluation Common benchmarks for text matching include LCQMC (Liu
et al., 2018a), BQ (Chen et al., 2018a), CNSE (Liu et al., 2019b), and CNSS (Liu et al., 2019b).
Accuracy and F1 are the most widely used evaluation metrics.
7.6 Topic Modeling
Background and Motivation The task of topic modeling aims to discover the abstract “topics”
that emerge in a corpus. Typically, a topic model learns to represent a piece of text as a mixture
of topics where a topic itself is represented as a mixture of words from a vocabulary. Classical
topic models include graphical model based methods (Blei et al., 2003, 2010), autoregressive model
based methods (Larochelle and Lauly, 2012), and autoencoder based methods (Miao et al., 2016;
Chen and Zaki, 2017; Isonuma et al., 2020). Recent works (Zhu et al., 2018; Zhou et al., 2020a;
Yang et al., 2020) have explored GNN-based methods for topic modeling by explicitly modeling
the relationships between documents and words.
Methodologies In this section, we introduce and summarize some representative GNN-related
techniques adopted in recent topic modeling approaches.
• Graph Construction How to construct a high-quality graph which naturally captures useful
relationships between documents and words is the most important for GNN applications in
the topic modeling task. Various graph construction strategies have been proposed for GNN-
based topic models. In order to explicitly model the word co-occurrence, Zhu et al. (2018)
extracted the biterms (i.e., word pairs) within a ﬁxed-length text window for every document
from a sampled mini-corpus, and built an undirected biterm graph where each node represents
a word, and each edge weight indicates the frequency of the corresponding biterm in the mini-
corpus. Zhou et al. (2020a) built a graph containing documents and words in the corpus as
nodes, and added edges to connect document nodes and word nodes based on co-occurrence
information where the edge weight matrix is basically the TF-IDF matrix. Yang et al. (2020)
converted a corpus to a bi-partite graph containing document nodes and word nodes, and the
edge weight indicates the frequency of the word in the document.
• Graph Representation Learning Given a graph representation of the corpus, Zhu et al.
(2018) designed a GCN-based autoencoder model to reconstruct the input biterm graph. In
72





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
addition, residual connections were introduced to the GCN architecture so as to avoid over-
smoothing when stacking many GCN layers. Similarly, Zhou et al. (2020a) designed a GCN-
based autoencoder model to restore the original document representations. Notably, Zhu et al.
(2018); Zhou et al. (2020a) reused the adjacency matrix as the node feature matrix which
captures the word co-occurrence information. During the inference time, for both of the
autoencoder-based methods, the weight matrix of the decoder network can be interpreted as
the (unnormalized) word distributions of the learned topics. Given the observations that Prob-
abilistic Latent Semantic Indexing (pLSI) (Hofmann, 1999) can be interpreted as stochastic
block model (SBM) (Abbe, 2017) on a speciﬁc bi-partite graph, and GAT can be interpreted
as the semi-amortized inference of SBM, Yang et al. (2020) proposed a GAT-based topic
modeling network to model the topic structure of non-i.i.d documents. As for node embed-
ding initialization, they used pre-trained word embeddings to initialize word node features,
and term frequency vectors to initialize document node features.
Benchmarks and Evaluation Common benchmarks for the topic modeling task include 20NEWS
(Lang, 1995), All News (Thompson, 2017), Grolier (Wang et al., 2019g), NYTimes (Wang et al.,
2019g), and Reuters (Lewis et al., 2004). As for evaluation metrics, since it is challenging to anno-
tate the ground-truth topics for a document, topic coherence score and case study on learned topics
are typical means of judging the quality of the learned topics. Besides, with the topic representations
of text output by a topic model, the performance on downstream tasks such as text classiﬁcation can
also be used to evaluate topic models.
7.7 Sentiment Classiﬁcation
Background and Motivation The sentiment classiﬁcation task aims to detect the sentiment (i.e.,
positive, negative or neutral) of a piece of text (Pang et al., 2002). Unlike general sentiment classiﬁ-
cation, aspect level sentiment classiﬁcation aims at identifying the sentiment polarity of text regard-
ing a speciﬁc aspect, and has received more attention (Pontiki et al., 2014). While most works focus
on sentence level and single domain sentiment classiﬁcation, some attempts have been made on
document level (Chen et al., 2020c) and cross-domain (Ghosal et al., 2020) sentiment classiﬁcation.
Early works on sentiment classiﬁcation heavily relied on feature engineering (Jiang et al., 2011).
Recent attempts (Tang et al., 2016; Huang and Carley, 2018) leveraged the expressive power of
various neural network models such as LSTM (Hochreiter and Schmidhuber, 1997), CNN (LeCun
and Bengio, 1998) or Memory Networks (Sukhbaatar et al., 2015). Very recently, more attempts
have been made to leverage GNNs to better model syntactic and semantic meanings of text for the
sentiment classiﬁcation task.
Methodologies GNN-based sentiment classiﬁcation approaches typically operate by ﬁrst con-
structing a graph representation (e.g., dependency tree) of the text, and then applying a GNN to
learn good text embeddings which will be used for predicting the sentiment polarity. The graph
construction techniques and graph representation techniques developed for solving the sentiment
classiﬁcation task vary between different approaches. In this section, we introduce and summarize
some representative GNN-related techniques adopted in recent sentiment classiﬁcation approaches.
• Graph Construction Most GNN-based approaches (Zhang et al., 2019b; Sun et al., 2019c;
Huang and Carley, 2019; Pouran Ben Veyseh et al., 2020; Tang et al., 2020a; Wang et al.,
73





LINGFEI WU AND YU CHEN , ET AL .
2020c) for sentence level sentiment classiﬁcation used a dependency tree structure to repre-
sent the input text. Besides using a dependency graph for capturing syntactic information,
Zhang and Qian (2020) in addition constructed a global lexical graph to encode the corpus
level word co-occurrence information, and further built a concept hierarchy on both the syn-
tactic and lexical graphs. Ghosal et al. (2020) constructed a subgraph from ConceptNet (Speer
et al., 2017) using seed concepts extracted from text. To capture the document-level sentiment
preference information, Chen et al. (2020c) built a bipartite graph with edges connecting sen-
tence nodes to the corresponding aspect nodes for capturing the intra-aspect consistency, and
a graph with edges connecting sentence nodes within the same document for capturing the
inter-aspect tendency.
• Graph Representation Learning Both the design of GNN models and quality of initial
node embeddings are critical for the overall performance of GNN-based sentiment classi-
ﬁcation methods. Common GNN models adopted in the sentiment classiﬁcation task include
GCN (Zhang et al., 2019b; Sun et al., 2019c; Pouran Ben Veyseh et al., 2020; Zhang and Qian,
2020), GAT (Huang and Carley, 2019; Chen et al., 2020c) and Graph Transformer (Tang et al.,
2020a). To handle multi-relational graphs, R-GCN (Ghosal et al., 2020) and R-GAT (Wang
et al., 2020c) were also applied to perform relation-aware message passing over graphs. Most
approaches used GloVe+BiLSTM (Sun et al., 2019c; Tang et al., 2020a; Wang et al., 2020c;
Tang et al., 2020a) or BERT (Huang and Carley, 2019; Pouran Ben Veyseh et al., 2020; Chen
et al., 2020c; Wang et al., 2020c; Tang et al., 2020a) to initialize node embeddings.
• Special Techniques One common trick used in aspect level sentiment classiﬁcation is to
include position weights or embeddings (Zhang et al., 2019b; Zhang and Qian, 2020) to em-
phasize more on tokens closer to the aspect phase.
Benchmarks and Evaluation Common benchmarks for evaluating sentiment classiﬁcation meth-
ods include Twitter (Dong et al., 2014), SemEval sentiment analysis datasets (Pontiki et al., 2014,
2015, 2016), MAMS (Jiang et al., 2019), and Amazon-reviews (Blitzer et al., 2007). Accuracy and
F1 are the most common evaluation metrics.
7.8 Knowledge Graph
Knowledge graph (KG), which represents the real world knowledge in a structured form, has at-
tracted a lot of attention in academia and industry. KG can be denoted as a set of triples of the form
⟨subject, relation, object⟩. There are three main tasks in term of KG, namely, knowledge graph
embedding (KGE), knowledge graph completion (KGC), and Knowledge Graph Alignment (KGA).
KGE aims to map entities and relations into low-dimensional vectors, which usually regarded as the
sub-task in KGC and KGA. In this section, we will give a overview of the graph-based approaches
to KGC and KGA.
7.8.1 K NOWLEDGE GRAPH COMPLETION
Background and Motivation The purpose of KGC is to predict new triples on the basis of ex-
isting triples, so as to further extend KGs. KGC is usually considered as a link prediction task.
Formally, the knowledge graph is represented by G = (V,E,R), in which entities vi∈V , edges
(vs, r, vo) ∈ E, and r ∈ Ris a relation type. This task scores for new facts (i.e. triples like
⟨subject, relation, object⟩) to determine how likely those edges are to belong toE.
74





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
Methodologies. KGC can be solved with an encoder-decoder framework. To encode the local
neighborhood information of an entity, the encoder can be chosen from a variety of GNNs such
as GCN(Malaviya et al., 2020; Shang et al., 2019), R-GCN (Schlichtkrull et al., 2018; Teru et al.,
2020) and Attention-based GNNs (Nathani et al., 2019b; Bansal et al., 2019; Zhang et al., 2020g;
Wang et al., 2019d). Then, the encoder maps each entity (subject entity and object entity) vi∈V
to a real-valued vector ei∈ Rd. Relation can be represented as an embedding er or a matrix Mr.
Following the framework concluded by Wang et al. (2019e), the GNN encoder in a multi-relational
graph (such as KG) can be formulated as:
a(l)
v = AGGREGAT El(h(l−1)
r,u ,∀u∈N r
v )
h(l)
v = COM BIN El(h(l−1)
r0,v , a(l)
v )
(93)
where h(l−1)
r,u denotes the message passing from the neighbor nodeu under relation r at the l th layer.
For example, RGCN (Schlichtkrull et al., 2018) setsh(l−1)
r,u = W (l−1)
r h(l−1)
u and AGGREGAT E(·)
be mean pooling. Since the knowledge graph is very large, the update of the node representation
Eq.93 is efﬁciently implemented by using sparse matrix multiplications to avoid explicit summation
over neighborhoods in practice.
The decoder is a knowledge graph embedding model and can be regarded as a scoring func-
tion. The most common decoders of knowledge graph completion includes translation-based mod-
els (TransE (Bordes et al., 2013)), tensor factorization based models (DistMult (Yang et al., 2014),
ComplEx(Trouillon et al., 2016)) and neural network base models (ConvE (Dettmers et al., 2018b)).
In Table 4 , we summarize these common scoring functions following Ji et al. (2020). Re(·) denotes
the real part of a vector,∗ denotes convolution operator, ω denotes convolution ﬁlters andg(·) is a
non-linear function. For example, RGCN uses DistMult as a scoring function, and DistMult can per-
form well on the standard link prediction benchmarks when used alone. In DistMult, every relation
r is represented by a diagonal matrix Mr∈ Rd×d and a triple is scored as f(s, r, o) = eT
s Mreo.
At last, the model is trained with negative sampling, which randomly corrupts either the subject
or the object of each positive example. To optimize KGC models, cross-entropy loss (Schlichtkrull
et al., 2018; Wang et al., 2019e; Zhang et al., 2020g; Malaviya et al., 2020) and margin-based
loss (Teru et al., 2020; Nathani et al., 2019a) are common loss functions used for optimizing KGC
models.
Benchmarks and Evaluation Common KGC benchmark datasets include FB15k-237 (Dettmers
et al., 2018a), WN18RR (Toutanova et al., 2015), NELL-995 (Xiong et al., 2017a) and Kinship (Lin
et al., 2018). Two commonly used evaluation metrics are mean reciprocal rank (MRR) and Hits at
n (H@n), where n is usually 1, 3, or 10.
7.8.2 K NOWLEDGE GRAPH ALIGNMENT
Background and Motivation . KGA aims at ﬁnding corresponding nodes or edges referring to
the same entity or relationship in different knowledge graphs. KGA, such as cross-lingual knowl-
edge graphs alignment, is useful for constructing more complete and compact KGs. Let G1 =
(V1,E1,R1) and G2 = (V2,E2,R2) be two different KGs, and S ={(vi1, vi2)|vi1∈V 1, vi2∈V 2}
be a set of pre-aligned entity pairs between G1 and G2. The core task of KGA is entity or relation
alignment, which is deﬁned as ﬁnding new entity or relation alignments based on the existing ones.
75





LINGFEI WU AND YU CHEN , ET AL .
Table 4: KGC Scoring Function.
Model Ent. embed. Rel. embed. Scoring Function f(s, r, o)
DistMult
es, eo∈ Rd Mr∈ Rd×d eT
s Mreo
(Schlichtkrull et al., 2018)
(Wang et al., 2019e)
(Bansal et al., 2019)
ComplEx es, eo∈ Cd er∈ Cd Re(er, es, ¯et) = Re(∑K
k=1 eres ¯et)(Wang et al., 2019e)
ConvKB es, eo∈ Rd er∈ Rd concat(σ([es, er, eo]∗ ω))· w(Nathani et al., 2019a)
ConvE Ms∈ Rdw×dh, eo∈ Rd Mr∈ Rdw×dh σ(vec(σ([Ms; Mr]∗ ω))W)eo(Wang et al., 2019d)
Conv-TransE
es, eo∈ Rd er∈ Rd g(vec(M(es, er))W)eo(Shang et al., 2019)
(Malaviya et al., 2020)
Methodologies. GNN-based KGA or entity alignment approaches mostly use GNN models to
learn the representations of the entities and relations in different KGs. Then, entity/relation align-
ment can be performed by computing the distance between two entities/relations. GCN is widely
used in (Wang et al., 2018; Xu et al., 2019b; Wu et al., 2019a). To further capture the relation infor-
mation existing in multi-relational KGs, Wu et al. (2019b) proposed a Relation-aware Dual-Graph
Convolutional Network (RDGCN), which also applied a graph attention mechanism. Similarly, Ye
et al. (2019) also introduced relation information by proposing a vectorized relational graph convo-
lutional network (VR-GCN). Cao et al. (2019c) proposed a Multi-channel Graph Neural Network
model (MuGNN) containing a KG self-attention module and a cross-KG attention module to en-
code two KGs via multiple channels. GAT is another common model, which is applied in (Li et al.,
2019; Sun et al., 2020b; Wang et al., 2020h). Moreover, Sun et al. (2020b); Wu et al. (2019b,a) also
introduced a gating mechanism to control the aggregation of neighboring information.
Entity/relation alignments are predicted by the distance between the entity/relation embeddings.
The distance measuring functions are mainly based on L1 norm (Ye et al., 2019; Wu et al., 2019b;
Wang et al., 2018; Wu et al., 2019a), L2 norm (Cao et al., 2019c; Li et al., 2019; Sun et al., 2020b),
cosine similarity (Xu et al., 2019b), and feed-forward neural network (Xu et al., 2019b; Wang et al.,
2020h).
Benchmarks and Evaluation. Common KGA benchmarks datasets includeDBP 15K (Sun et al.,
2017) and DW Y 100K (Sun et al., 2018b). DBP 15K contains three cross-lingual datasets:DBPZH−EN
(Chinese to English), DBPJA−EN (Japanese to English), and DBPFR−EN (French to English).
DW Y 100K is composed of two large-scale cross-resource datasets: DW Y− W D (DBpedia to
Wikidata) and DW Y− Y G (DBpedia to Y AGO3). Hits@N, which is calculated by measuring the
proportion of correctly aligned entities/relations in the top N list, is used as evaluation metric to
assess the performance of the models.
7.9 Information Extraction
Background and Motivation Information Extraction (IE) aims to extract entity pairs and their
relationships of a given sentence or document. IE is a signiﬁcant task because it contributes to the
automatic knowledge graph construction from unstructured texts. With the success of deep neural
76





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
networks, NN-based methods have been applied to information extraction. However, these methods
often ignore the non-local and non-sequential context information of the input text (Qian et al.,
2019). Furthermore, the prediction of overlapping relations, namely the relation prediction of pairs
of entities sharing the same entities, cannot be solved properly (Fu et al., 2019). To these ends,
GNNs have been widely used to model the interaction between entities and relations in the text.
Methodologies Information extraction composed of two sub-tasks: named entity recognition
(NER) and relation extraction (RE). NER predicts a label for each word in a sentence, which is
often regarded as a sequence tagging task (Qian et al., 2019). RE predicts a relation type for every
pair of entities in the text. When the entities are annotated in the input text, the IE task degrades into
an RE task (Sahu et al., 2019; Christopoulou et al., 2019; Guo et al., 2019a; Zhu et al., 2019c; Zhang
et al., 2019a, 2018d; Vashishth et al., 2018; Zeng et al., 2020; Song et al., 2018e). GNN-based IE
approaches typically operate via a pipeline approach. First, a text graph is constructed. Then, the
entities are recognized and the relationships between entity pairs are predicted. Very recently, re-
searchers starts to jointly learn the NER and RE to take advantage of the interaction between these
two sub-tasks (Fu et al., 2019; Luan et al., 2019; Sun et al., 2019b). Followings are the introduction
of different GNN-based techniques.
• Graph Construction Most GNN-based information extraction methods design speciﬁc rules
to construct static graphs. Because the input of IE task is usually a document containing mul-
tiple sentences, the nodes in the constructed graph can be words, entity spans and sentences
and the corresponding edges are word-level edges, span-level edges and sentence-level edges.
These nodes can be connected by syntactic dependency edges (Fu et al., 2019; Guo et al.,
2019a; Zhang et al., 2018d; Vashishth et al., 2018; Song et al., 2018e; Sahu et al., 2019), co-
reference edges (Luan et al., 2019; Zeng et al., 2020; Sahu et al., 2019), re-occurrence edges
(Qian et al., 2019), co-occurrence edges (Christopoulou et al., 2019; Zeng et al., 2020), adja-
cent word edges (Qian et al., 2019; Luan et al., 2019; Sahu et al., 2019) and adjacent sentence
edge (Sahu et al., 2019). Recently, dynamic graph construction has also been successfully
applied in IE tasks. (Luan et al., 2019) proposed a general IE framework using dynamically
constructed span graphs, which selected the most conﬁdent entity spans from the input docu-
ment and linked these span nodes with co-references and conﬁdence-weighted relation types.
(Sun et al., 2019b) ﬁrst constructs a static entity-relation bipartite graph and then investigates
the dynamic graph for pruning redundant edges.
• Graph Representation Learning To better capture non-local information of the input doc-
ument, a variety of GNN models are applied in the NER task and the RE task. In addition,
joint learning is a critical technique to reduce error propagation along the pipeline. For the
name entity recognition task, common GNN models such as GCN (Qian et al., 2019; Luo
and Zhao, 2020) are applied. GCN is the most common GNN models used in the relation
extraction task (Zhang et al., 2019a, 2018d; Vashishth et al., 2018; Zeng et al., 2020). To
learn edge type-speciﬁc representations, Sahu et al. (2019) introduces a labelled edge GCN
to keep separate parameters for each edge type. Inspired by the graph attention mechanism,
Guo et al. (2019a) proposes attention guided GCN to prune the irrelevant information from
the dependency trees. Recently, many joint learning models have been proposed to relieve the
error propagation in the pipeline IE systems and leverage the interaction between the NER
task and the RE task. Fu et al. (2019) proposes a GraphRel model containing 2 phases predic-
77





LINGFEI WU AND YU CHEN , ET AL .
tion of the entities and relations. Luan et al. (2019) introduces a general framework to couple
multiple information extraction sub-tasks by sharing entity span representations which are
reﬁned using contextualized information from relations and co-references. Sun et al. (2019b)
develops a paradigm that ﬁrst detected entity spans, and then performed a joint inference on
entity types and relation types.
Benchmarks and Evaluation. Common IE benchmark datasets contain NYT (Riedel et al., 2010),
WebNLG (Gardent et al., 2017), ACE2004, ACE2005, SciERC(Luan et al., 2018), TACRED (Zhang
et al., 2017b) and etc. Precision, recall and F1 are the most common evaluation metrics for IE.
7.10 Semantic and Syntactic Parsing
In this section, we mainly discuss applications of GNN for parsing, including syntax related and se-
mantics related parsing. For syntax related parsing, GNN has been employed in tasks of dependency
parsing(Ji et al., 2019)(Do and Rehbein, 2020) and constituency parsing(Yang and Deng, 2020). For
semantics related parsing, we will brieﬂy introduce semantic parsing and AMR (Abstract Meaning
Representation) parsing.
7.10.1 S YNTAX RELATED PARSING
Background and motivation The tasks related to syntax are mainly dependency parsing and
constituency parsing. Both of them aim to generate a tree with syntactic structure from natural
language sentences, conforming to predeﬁned formal grammar rules. Dependency parsing focuses
on the dependency relationship between words in sentence. Constituency parsing focuses on the
compositional relationship between different components in a sentence. Traditional approaches can
be divided into two directions: transition-based and graph-based. Transition-based methods(Andor
et al., 2016)(Ma et al., 2018) usually formalize this problem as a series of decisions on how to
combine different words into a syntactic structure. Graph-based methods(Kiperwasser and Gold-
berg, 2016)(Dozat and Manning, 2016)(Ji et al., 2019) ﬁrstly score all word pairs in a sentence on
the possibility of holding valid dependency relationship, and then exploit decoders to generate the
parse trees.
Methodologies Here, we mainly focus on graph-based parsers where graph neural network plays
the role of extracting high-order neighbor features.
• Dependency parsing. In graph-based parsers, we take each word as a node in a graph and
the key task is to learn a low-dimensional node representation with a neural encoder. To
incorporate more dependency structure information, Ji et al. (2019) proposes to employ GNN
as a encoder to incorporate high-order information. Their encoder contains both GNN and
Bi-LSTM, where the GNN accepts all node embeddings from Bi-LSTM and take them as
node embeddings in a complete graph. The constructed graphs are dynamic graphs where
edge weight can change consistently during training. There are two kinds of loss functions:
1) the ﬁrst one considers both tree structure and dependency relation labels; 2) the second
one are applied after each GNN layer where only tree structure is considered. Other than
the generation of dependency parsing trees, some other works focus on how to do reranking
among different candidates to choose a best parsing tree. Do and Rehbein (2020) demonstrate
that GNN can also work well as a encoder for dependency parsing trees in a neural reranking
model.
78





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
• Constituency parsing. Most approaches for constituency parsing are transition-based (Sagae
and Lavie, 2005; Dyer et al., 2016; Liu and Zhang, 2017; Yang and Deng, 2020) which gen-
erate the constituency parsing tree by executing an action sequences. Yang and Deng (2020)
proposes to use GNN to encode the partial tree in the decoding process which can generate
one token per step. Other methods usually generate the ﬁnal parsing tree by combining dif-
ferent sub-trees in a shift-reduce way. The authors believe that this strongly incremental way
is more closer to the way of human thinking.
Benchmark and Evaluation For syntactic parsing, two becnmark datasets are commonly used,
namely, PTB 3.0(Taylor et al., 2003) and UD 2.2(Nivre et al., 2018). As for evaluation, Accuracy,
including exact match accuracy and execution accuracy, and Smatch score(Cai and Knight, 2013)
are commanly used.
7.10.2 S EMANTICS RELATED PARSING
Background and Motivation For semantics related tasks, we will introduce two popular appli-
cations: SQL parsing and AMR parsing. Semantic parsing aims to generate machine-interpretable
representations from natural language, like SQL queries. AMR parsing is another young research
ﬁeld. AMR is represented as a rooted labeled directed acyclic graph form, and the goal of AMR
parsing aims to provide sentence-level semantic representations. It is widely used in many NLP
tasks like text summarization, machine translation and question answering(Zhou et al., 2020b).
Methodologies Here, we provide a summary of the techniques for two typical semantic related
parsing tasks, namely, SQL parsing and AMR parsing.
• SQL parsing. The main purpose of SQL parsing is to convert natural language into SQL
queries that can be successfully executed. Most of the traditional methods (Jia and Liang,
2016; Alvarez-Melis and Jaakkola, 2016; Dong and Lapata, 2016) are sequential encoder
based, which however, lost some other useful information at the source side, such as syntax
information and DB schema information. Thus, many GNN-based models are proposed. For
syntactic information, Li et al. (2020b); Xu et al. (2018c) use external parser to perform
syntactic parsing (i.e., constituency parsing and dependency parsing) on the raw sentence.
Then they exploit the syntactic parsing tree instead of the source sentence as input, and use
GNN to learn the syntactic structure and dependent information in this ”tree” graph. It has
been proved experimentally that the additional syntactic information is helpful for semantic
parsing tasks. SQL parsing problem becomes more complex if the DB schema of the training
and testing set are different (Yu et al., 2018). To this end, some works propose to model these
schema information to achieve better results. For example, Bogin et al. (2019a) takes the DB
schema as a graph and use GGNN to learn the node representation. Then they incorporate
schema information on both the encoder and decoder to generate the ﬁnal results. Bogin et al.
(2019b) employs GNN to globally select the overall structure of the output query which could
decrease the ambiguity of DB constants choice.
After the SQL queries are generated, reranking can be utilized to further improve the perfor-
mance. Reranking the candidates predicted by the model is helpful to reduce the likelihood
of picking some sub-optimal results. SQL queries are structured and it is a reasonable way to
use GNN to encode the SQL queries in the reranking model. For example, Do and Rehbein
79





LINGFEI WU AND YU CHEN , ET AL .
(2020) employs graph-based transformer to rearrange the results generated by the neural se-
mantic parser and achieved good results.
• AMR parsing . Similar to (Li et al., 2020b)(Xu et al., 2018c), syntactic information, es-
pecially dependency relation information, are also employed in AMR parsing. Zhou et al.
(2020b) considers both the dependency syntactic graph and the latent probabilistic graph.
Speciﬁcally, by learning a vector representation for the two graph structures and then fusing
them together, their model leverages the structure information in the source side and achieve
better performance compared to seq-to-graph-like models.
Benchmark and Evaluation For SQL parsing, three benchmark datasets are commanly used,
including ATIS(Dahl et al., 1994), GEO(Luke, 2005), WikiSQL(Zhong et al., 2017), SPIDER(Yu
et al., 2018). For AMR parsing, AMR annotation release(Knight et al., 2014, 2017) is a well-
recognized dataset. For evaluation metrics, accuracy, including exact match accuracy and execution
accuracy, as well as Smatch score(Cai and Knight, 2013).) are commonly used.
7.11 Reasoning
Reasoning is a signiﬁcant research direction for NLP. In recent years, GNN begins to play an impor-
tant role in NLP reasoning tasks, such as math word problem solving (Li et al., 2020b; Zhang et al.,
2020c), natural language inference (Kapanipathi et al., 2020; Wang et al., 2019c), common sense
reasoning (Lin et al., 2019a; Zhou et al., 2018b) and so on. In this subsection, we will give a brief
introduction for the three tasks and how graph neural networks are employed in these methods.
7.11.1 M ATH WORD PROBLEM SOLVING
Background and Motivation Math word problem solving aims to infer reasonable equations
from given natural language problem descriptions. It is important for exploring automatic solutions
to mathematical problems and improving the reasoning ability of neural networks. Most of the
traditional methods are based on the seq2seq (Wang et al., 2017) framework to generate the corre-
sponding equation directly from the source sentence in an end-to-end manner. This kind of methods
ignore some important information in natural sentences, such as 1) the relationship information be-
tween different mathematical elements (numbers) in the question, 2) the syntax information in the
question sentence, 3) external knowledge, and so on. Thus, GNN-based models are proposed as a
very good way to incorporate this information.
Methodologies Li et al. (2020b) is the ﬁrst to introduce GNN into math word problem solving.
Graph2tree considers both the input and output structure information. At the input side, GNN is
used to encode the input syntactic tree. After all the input nodes embedding are generated, on the
output side, considering the hierarchy of the equation, a BFS-based tree decoder is used to generate
the ﬁnal equation result in a coarse-to-ﬁne way. Zhang et al. (2020c) is another MWP automatic
solving model that uses graph data structure to model 1) the relationship between the numbers in the
problem, and 2) the relationship between different numbers with their corresponding descriptors. In
addition, some works introduce the external knowledge information in another way. For example,
Wu et al. (2020c) ﬁrst connects the entities in the problem description into graphs based on external
global knowledge information, and then uses GAT as encoder. This method can enhance the ability
of modeling the relationship between the entities in the problem, and has obtained good results.
80





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
Benchmarks and Evaluation For math word problem, three benchmark datasets are commonly
used, including MAWPS (Koncel-Kedziorski et al., 2016), MATH23K (Wang et al., 2017), and
MATHQA (Amini et al., 2019).
7.11.2 N ATURAL LANGUAGE INFERENCE
Background and Motivation Natural language inference (NLI) is another fundamental reason-
ing task. This task aims to predict the relationship between premise and hypothesis, and is often
formalized as a three-classiﬁcation problem (contradict, entails, neutral).
Methodologies Traditional methods are mostly based on neural encoder with attention, and most
of them are RNN models(Chen et al., 2017c). Considering the rich information contained in the
external knowledge base, some works try to use external information to improve the accuracy of
the model. For example, Wang et al. (2019c) uses graph-based attention model to incorporate the
information from introduced external knowledge source. Their experiments demonstrate that adding
the learned knowledge graph representation to the classiﬁer help to obtain good results. Considering
the introduced graph can have noisy information, Kapanipathi et al. (2020) employs a encoder with
a subgraph ﬁltering module using Personalized PageRank before a GCN layer where the ﬁltering
module can help to select context relevant sub-graphs from introduced knowledge graph to reduce
noisy information.
Benchmarks and Evaluation For NLI task, three benchmark datasets are commonly used, in-
cluding SNLI(Bowman et al., 2015), MultiNLI(Williams et al., 2018), and SciTail(Khot et al.,
2018).
7.11.3 C OMMONSENSE REASONING
Background and Motivation Commonsense reasoning helps neural models incorporate the ”com-
mon sense” or world knowledge during inference. Take the commonsense QA as example, we aim
to obtain a neural model tended to generate the answer which is more consistent with common-
sense from multiple answers that all logically ﬁt the requirements. In fact, large-scale pre-trained
models such as GPT-2(Radford et al., 2019), BERT(Devlin et al., 2019) with simple ﬁne-tuning can
achieve very good results. However, some external knowledge sources can help the model to bet-
ter characterize the question and the concepts in the answer, which will deﬁnitely help the overall
performance.
Methodologies Lin et al. (2019a) introduces graph neural networks to the common sense rea-
soning task. The model ﬁrst retrieves the concepts in the questions and options into an external
knowledge base to obtain a schema graph, and then uses GCN to incorporate information from this
retrieved graph to learned features. The learnt features would be fed to a simple score module for
each QA pair. Experiments on large benchmarks dataset, e.g., CommonsenseQA (Talmor et al.,
2019), demonstrate the effectiveness of the external knowledge base introduced by GNN.
Benchmarks and Evaluation We introduce some benchmark datasets for commonsense reason-
ing here: CommonsenseQA (Talmor et al., 2019); Event2Mind(Rashkin et al., 2018); SW AG(Zellers
et al., 2018); Winograd Schema Challenge(Levesque et al., 2012); ReCoRD(Zhang et al., 2018c).
81





LINGFEI WU AND YU CHEN , ET AL .
7.12 Semantic Role Labelling
Background and Motivation The problem of semantic role labeling (SRL) aims to recover the
predicate-argument structure of a sentence, namely, to determine essentially “who did what to
whom”, “when”, and “where. More formally, for every predicate, the SRL model must identify
all argument spans and label them with their semantic roles. Such high-level structures can be used
as semantic information for supporting a variety of downstream tasks, including dialog systems, ma-
chine reading and translation (Shen and Lapata, 2007; Liu and Gildea, 2010; Gao and V ogel, 2011).
Recent SRL works can mostly be divided into two categories, i.e., syntax-aware (Xia et al., 2020;
Marcheggiani and Titov, 2020) and syntax-agnostic (He et al., 2017, 2018) approaches according
to whether incorporating syntactic knowledge or not. Most syntax-agnostic works employ deep
BiLSTM or self-attention encoder to encode the contextual information of natural sentences, with
various kinds of scorers to predict the probabilities of BIO-based semantic roles (He et al., 2017) or
predicate-argument-role tuples (He et al., 2018). Motivated by the strong interplay between syntax
and semantics, researchers explore various approaches to integrate syntactic knowledge into syntax-
agnostic models considering that the semantic representations are closely related to syntactic ones.
For example, one can observe that many arcs in the syntactic dependency graph are mirrored in the
semantic dependency graph. Given these similarities and the availability of accurate syntactic parser
for many languages, it seems natural to exploit syntactic information when predicting semantics.
However, the last generation of SRL models powered by deep learning models put syntax aside
in favor of neural sequence models, namely LSTMs (Zhou et al., 2020a; Marcheggiani et al., 2017)
due to the challenges that (1) it is difﬁcult to effectively incorporate syntactic information into
neural SRL models, due to the sophisticated tree structure of syntactic relation; and (2) the syntactic
parsers are unreliable on account of the risk of erroneous syntactic input, which may lead to error
propagation and an unsatisfactory SRL performance. Given this situation, GNNs are emerging as
powerful tools to capture and incorporate the syntax patterns into deep neural network-based SRL
models. The nature property of GNN in capturing the complex relationship patterns in the structured
data makes it a good ﬁt for modeling syntactic dependency and constituency structures of sentences.
Methodologies The problem solved by the GNN-based SRL models can be divided into two cat-
egories. One is about argument prediction given the predicates in a sentence (Marcheggiani and
Titov, 2020, 2017; Li et al., 2018b). Formally, SRL can be cast as a sequence labeling problem
where given an input sentence, and the position of the predicate in the sentence, the goal is to
predict a BIO sequence of semantic roles for the words in sentences; Another is about end-to-end
semantic role triple extraction which aims to detect all the possible predicates and their correspond-
ing arguments in one shot (Fei et al., 2020; Xia et al., 2020). Technically, given a sentence, the SRL
model predicts a set of labeled predicate-argument-role triplets, while each triple contains a possi-
ble predicate token and two candidate tokens. Both of the above mentioned problems can be solved
based on the GNN-based SRL models, which consists of two parts, namely, graph construction and
graph representation learning.
• Graph Construction. The graphs are constructed based on the syntax information, which
can be extracted from two sources, one is syntactic dependency information and another is
syntactic constituents information. Most of the existing GNN-SRL models (Li et al., 2018b;
Fei et al., 2020; Marcheggiani and Titov, 2017; Zhang et al., 2020f; Xia et al., 2020) have
relied on syntactic dependency representations. In these methods, information from depen-
dency trees are injected into word representations using GNN or self-attention mechanisms.
82





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
Recently, Marcheggiani et al (Marcheggiani and Titov, 2020) incorporated the constituency
syntax into SRL models by conducting the message passing on a graph where nodes rep-
resent constituents. Based on the syntax information, the graphs constructed in the current
SRL models are divided into three main categories: (1) directed homogeneous graphs; (2)
heterogeneous graphs; and (3) probability weighted graphs. Most of the works (Marcheg-
giani and Titov, 2017; Li et al., 2018b; Fei et al., 2020) represent the syntax information as
a directed homogeneous graph where all the nodes are input word tokens and directed with
dependent edges. Other work (Xia et al., 2020) enhances SRL with heterogeneous syntactic
knowledge by combining various syntactic treebanks that follow different annotation guide-
lines and domains. Liu et al. (Liu et al., 2019a) also construct a heterogeneous syntactic graph
by incorporating several types of edges, including lexical relationships, syntactic dependency,
co-occurrence relationships. Some work (Zhang et al., 2020f) utilizes the probability matrix
of all dependency arcs for constructing an edge-weighted directed graph to eliminate the in-
ﬂuences of the error from the parsing results.
• Graph Representation Learning. As described in Section 6, various GNN models can be
utilized for graph representation learning. Here, we introduce the different roles that GNNs
play in different SRL models. In most of the works (Zhang et al., 2020f; Liu et al., 2019a;
Marcheggiani and Titov, 2017, 2020), GNN is utilized as an encoder to learn the ﬁnal repre-
sentations of words which follows a typical word embedding layer, such as BiLSTM. While
in some works (Xia et al., 2020; Fei et al., 2020), GNN is utilized to extract the initial words’
embedding, which are regarded as inputs of the encoder. For example, Xia et al. (Xia et al.,
2020) combines the syntax embedding extracted from GNN with the word embedding and
character embedding as the input. Fei (Fei et al., 2020) utilizes GNN to reﬁne the initial word
embedding which consists of word representation and part-of-speech (POS) tags, and then
input the reﬁned word embedding into the BiLSTM encoder.
Benchmarks and Evaluation There are two main benchmark datasets for the evaluation in the
domain of SRL: (1) CoNLL dataset concerns the recognition of semantic roles for the English
language, based on PropBank predicate-argument structures. Given a sentence, the task consists of
analyzing the propositions expressed by some target verbs of the sentence. In particular, for each
target verb all the constituents in the sentence which ﬁll a semantic role of the verb have to be
recognized. (2) Chinese Proposition Bank 1.0 (CPB1.0) which creates a corpus of text annotated
with information about basic semantic propositions (i.e., predicate-argument relations). The typical
evaluation metrics in SLR task are about metrics for classiﬁcation problem, such as precision, recall
and F1 of the correctly predicted arguments.
7.13 Related Libraries and Codes
Open-source implementations facilitate the research works of baseline experiments in graph neural
networks for NLP. Besides various paper codes were released individually, there is a recently re-
leased library called Graph4NLP 2, which is an easy-to-use library for R&D at the intersection of
Deep Learning on Graphs and Natural Language Processing. It provides both full implementations
of state-of-the-art models mentioned above for several NLP applications including text classiﬁ-
cation, semantic parsing, machine translation, KG completion, and natural language generation.
2. The codes and details of Graph4NLP library are provided at https://github.com/graph4ai/graph4nlp.
83





LINGFEI WU AND YU CHEN , ET AL .
Graph4NLP also provides ﬂexible interfaces to build customized models for researchers and devel-
opers with whole-pipeline support. Built upon highly-optimized runtime libraries including DGL
and Pytorch, Graph4NLP has both high running efﬁciency and great extensibility. The architecture
of Graph4NLP consists of four different layers: 1) Data Layer, 2) Module Layer, 3) Model Layer,
and 4) Application Layer. There are also some other related GNN-based libraries. Noticeably, Fey
and Lenssen (2019) published a geometric learning library in PyTorch named PyTorch Geometric,
which implements many GNNs. The Deep Graph Library (DGL) (Wang et al., 2019f) was released
which provides a fast implementation of many GNNs on top of popular deep learning platforms
such as PyTorch and MXNet. The Dive into Graphs (Liu et al., 2021c) was released recently as a
research-oriented library that integrates uniﬁed and extensible implementations of common graph
deep learning algorithms for several advanced tasks.
8. General Challenges and Future Directions
In this chapter, we will discuss various general challenges of GNNs for NLP and pinpoint the future
research directions. We believe putting more research efforts in these directions will further unleash
the great potential of GNNs in the NLP ﬁeld, and result in fruitful research outcomes.
8.1 Dynamic Graph Construction
As we see in Section 7, many NLP problems can be tackled from a graph perspective, and GNNs
are naturally applicable to and good at handling graph-structured data. Thus, the graph construc-
tion process plays an important role in the overall model performance. However, constructing a
high quality and task-speciﬁc graph requires a good amount of domain expertise and human effort.
Moreover, graph construction in NLP is often more art than science, informed solely by insight of
the practitioner, and involves many trials and errors. Even though a few of existing works already
explored dynamic graph construction, most GNN applications in NLP still heavily relied on domain
expertise for static graph construction.
The exploration of dynamic graph construction for NLP, is still at its early stage and faces several
challenges: ﬁrst of all, most works on dynamic graph construction focused only on homogeneous
graph construction (Chen et al., 2020g,e,f; Liu et al., 2021a, 2019a), and dynamic graph construction
for heterogeneous graphs (Yun et al., 2019; Zhao et al., 2021) is much less explored especially for
NLP tasks. Compared to homogeneous graphs, heterogeneous graphs are capable of carrying on
richer information on node types and edge types, and occur frequently in many NLP problems.
Dynamic graph construction for heterogeneous graphs is also supposed to be more challenging
because more types of information (e.g., node types, edge types) are expected to be learned from
data.
Second, most existing dynamic graph construction techniques rely on some form of pair-wise
node similarity computation whose time complexity is at least O(n2) where n is the number of
graph nodes. This results in scalability issues when scaling to large graphs such as KGs. Recently,
a scalable graph structure learning approach with linear time and memory complexity (in terms of
the number of nodes) was proposed by adopting the anchor-based approximation technique to avoid
explicit pair-wise node similarity computation (Chen et al., 2020f).
Finally, various efﬁcient transformers (Tsai et al., 2019; Katharopoulos et al., 2020; Choro-
manski et al., 2021; Peng et al., 2021; Shen et al., 2021; Wang et al., 2020a) were also developed
which could inspire the research in scalable dynamic graph construction considering their close
84





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
connections; (3) As observed in some previous works, dynamic graph construction does not clearly
outperform static graph construction in some NLP applications. There is still room for improve-
ment for dynamic graph construction techniques in terms of downstream task performance. Other
interesting future directions in this line include dynamically learning edge directions for graphs, and
combining static and dynamic graph construction for better performance.
8.2 GNNs vs Transformers for NLP
While GNNs have achieved promising results in a large variety of NLP ﬁelds, Transformers have
received much more attentions due to excellent performance in many NLP applications. However,
as we pointed out in the previous section, Transformers are type of special GNNs, which operated on
a fully connected dynamic graph constructed by employing self-attention mechanism. Since both
of them have their clear advantages over each other, there are several interesting direction worth
exploiting here.
Combining GNNs with Transformers for NLP The most beautiful thing about Transformers is
its simple use of its elegant model architecture directly on original text sequence, which separates
the graph data modeling inside transformer model from the inputs (and from the end user). How-
ever, the downside of this model choice is that the Transformers cannot directly operate on more
complex data like graph-structured data directly. In contrast, GNNs are more generic model archi-
tecture directly operating on graph data, which however are needed created by the end user with
either domain speciﬁc knowledge or other graph modeling techniques. Currently, Graph Trans-
formers are most popular models that adapt structure-aware self-attention mechanism to combine
the advantages of Transformers and GNNs. However, these approaches are purely replying on at-
tention mechanism to utilize the original graph topology information, which may not the best way
to explore the original graph input information, especially when graph inputs are multi-relational
and heterogeneous graphs.
Pre-training GNNs for NLP One of the most important trends in NLP over the past few years
is to develop large-scale pre-trained models (Devlin et al., 2018; Brown et al., 2020) most of which
are based on Transformer architectures. Recently, there are also many research efforts on pre-
training GNNs on graphs (Hu et al., 2019b; Qiu et al., 2020) using self-supervised learning methods.
However, there are very few attempts to pre-train GNNs for NLP (He et al., 2020; Sun et al., 2020a;
Chen et al., 2020b), which may exploit more types of data sources than Transformers since GNNs
can take both graph structured data (e.g., from KGs) and unstructured data (e.g., from free-form
text).
8.3 Graph-to-Graph for NLP
Since the natural language or information knowledge can be naturally formalized as graphs with a
set of nodes and their relationships, many generation tasks in the domain of NLP can be formalized
as a graph transformation problem, which can further be solved by the graph-to-graph models. In
this way, the semantic structural information of both the input and output sentences can be fully uti-
lized and captured. For example, the graph-to-graph transformation for AMR parsing is promising
and yet unexplored. Because AMR are naturally structured objects (e.g. tree structures), currently,
many semantic AMR parsing methods are based on deep graph generative models. These meth-
ods (Flanigan et al., 2014; Zhang et al., 2019d; Cai and Lam, 2020a) represent the semantics of
85





LINGFEI WU AND YU CHEN , ET AL .
a sentence as a semantic graph (i.e., a sub-graph of a knowledge base) and treat semantic parsing
as a semantic graph matching/generation process. These end-to-end deep graph generation tech-
niques for semantic parsing show powerful ability in automatically capturing semantic information.
However, current graph-based semantic parsing models only represent either the output AMR or the
input sentence as a graph, without jointly utilize the interactive relationship in both input and output,
and thus can not consider the complex relationship among the topology pattern of AMR logits and
input dependency/constituency parsing.
While utilizing the graph-to-graph model for NLP tasks, there are several general challenges
that deserve to be explored and solved in this domain: (1) Difﬁculty in building an end-to-end
graph transformation framework which can integrate several sub-tasks jointly. For example, it is
important to jointly tackle name entity recognition and relation extraction jointly in the information
extraction; (2) The different concepts of input and output graphs. In NLP tasks, we usually formalize
the dependency tree as the input graph and the output graph is usually has different concept from
the input graph. Thus, both the node set, and topology of the input and output graphs are different.
For example, in AMR parsing, the nodes in output graph are AMR logits, while the nodes in input
graphs are word tokens; (3) Difﬁculty in addressing the graph sparsity issue in NLP tasks. For
example, AMR parsing is a much harder task in that the target vocabulary size is much larger, while
the size of dataset is much smaller; (4) Unpaired graph-to-graph transformation. The annotations are
relatively expensive to produce and thus corpora have on the order of tens of thousands of sentences.
Utilizing the unpaired sample pairs is also important yet challenging.
8.4 Knowledge Graph in NLP
Knowledge graph has become an important component in many NLP tasks, such as question an-
swering, natural language generation, knowledge graph completion and alignment. It can be either
incorporated as an auxiliary information besides the input text to provide more knowledge (e.g., KG
augmentation), or as an target object to be learnt or extracted from (e.g., KGE and KGC).
Knowledge Graph Augmentation For many NLP tasks such as QA and NLG, it is increasingly
common to ﬁnd that the input data not only contain Query text or source text, but also incorporate
KG as auxiliary information for additional knowledge. There are several challenges with KG-
augmented tasks: (1) There may exist ambiguity when aligning entities in the input text to entities in
KG in some text-to-text generation tasks. For example, a person name appearing in the input text can
correspond to multiple entries in KG; (2) Since the scale of KG is often large, it takes considerable
effort to extract useful information from the KG and build knowledge subgraphs which can be
directly used by every sample as an auxiliary input. Generally, detailed and task-speciﬁc rules need
to be designed for KG node selection; (3) Entity alignment and knowledge subgraph construction
may involve inevitable errors propagating to the downstream tasks. To make better use of KGs, the
techniques for pre-processing KG, such as entity alignment and related entity/node selection, need
to be further explored and improved.
Knowledge Graph Embedding and Completion GNN-based KGE and KGC approaches con-
sider incorporating the neighborhood of a head entity or a tail entity. There is a trade-off between
all triples training on the same large KG (Shang et al., 2019)and each triple training on a separate
knowledge subgraph constructed from the original KG (Teru et al., 2020; Xie et al., 2020) . The
former one provides more computational efﬁciency while the latter one has more powerful model
86





GRAPH NEURAL NETWORKS FOR NLP: A S URVEY
expressiveness. Future research will focus on jointly reasoning text and KG by applying such meth-
ods and paying attention to the entities mentioned in the text (Bansal et al., 2019). Logic rules play
an important role to determine whether a triple is valid or not, which may be useful for KGE and
KGC (Xie et al., 2020).
Knowledge Graph Alignment Most of the existing GNN-based KG alignment models also face
three critical challenges to be further explored: (1) Different KGs usually have heterogeneous
schemas, and may mislead the representation learning , which makes it is difﬁcult to integrate
knowledge from different KGs (Cao et al., 2019c; Wu et al., 2019a); (2) The data in KG is usually
incomplete (Sun et al., 2020b) which needs pre-processing; (3) The seed alignments are limited (Li
et al., 2019). How to iteratively discover new entity alignments in the GNN-based framework is a
future direction (Wang et al., 2018; Li et al., 2019).
8.5 Multi-relational Graph Neural Networks
Multi-relational graphs, which adopt uniﬁed nodes but relation-speciﬁc edges, are widely observed
and explored in many NLP tasks. As we discussed in Section 5.2, most multi-relational GNNs,
which are capable of exploiting multi-relational graphs, are extended from conventional homoge-
neous GNNs. Technically, most of them either apply relation-speciﬁc parameters during neigh-
bor aggregation or split the heterogeneous graphs to homogeneous sub-graphs (Schlichtkrull et al.,
2018; Beck et al., 2018a). Although impressive progresses have been made, there is still a challenge
in handling over-parameterization problem due to the diverse relations existing in the graph. Al-
though several tricks such as parameter-sharing (e.g, see Directed-GCN (Marcheggiani and Titov,
2017)) and matrix-decomposition (e.g., see R-GCN (Schlichtkrull et al., 2018)) are widely used to
enhance the models’ generalization ability to address this issue, they still have limitations, such as
resulting in the potential loss of the models’ expression ability. There is a hard trade-off between
the over-parameterization and powerful model expression ability.
It is worth noting that various graph transformers have been introduced to exploit the multi-
relational graphs (Yao et al., 2020; Wang et al., 2020d). However, the challenge exists in how to
fully take advantage of the strong inductive bias (i.e., the graph topology) of the graphs by the trans-
formers which are naturally free of that. Currently, most of them simply regard the self-attention’s
map as a fully-directed graph. On top of that, researchers either apply sparsing mechanisms (Yao
et al., 2020) or allow remote connection (Shaw et al., 2018; Cai and Lam, 2020b) according to the
given graph. How to develop an effective and general architecture for multi-relational graphs (or
heterogeneous graphs) needs further exploration.
9. Conclusions
In this article, we conduct a comprehensive overview of various graph neural networks evolving
various NLP problems. Speciﬁcally, we ﬁrst provide the preliminary knowledge of typical GNN
models including graph ﬁlters and graph poolings. Then we propose a new taxonomy that system-
atically organizes GNNs for NLP approaches along three dimensions, namely, graph construction,
graph representation learning, and the overall encoder-decoder models. Given these speciﬁc tech-
niques at each stage of the NLP application pipelines, we discuss a wide range of NLP applications
from the perspective of graph construction, graph representation learning, and special techniques.
87





LINGFEI WU AND YU CHEN , ET AL .
Finally, the general challenges and future directions in this line are provided to further unleash the
great potential of GNNs in the NLP ﬁeld.
References
Emmanuel Abbe. 2017. Community detection and stochastic block models: recent developments.
The Journal of Machine Learning Research 18, 1 (2017), 6446–6531.
Mehdi Allahyari, Seyedamin Pouriyeh, Mehdi Asseﬁ, Saeid Safaei, Elizabeth D Trippe, Juan B
Gutierrez, and Krys Kochut. 2017. Text summarization techniques: a brief survey.arXiv preprint
arXiv:1707.02268 (2017).
Miltiadis Allamanis, Marc Brockschmidt, and Mahmoud Khademi. 2018. Learning to Represent
Programs with Graphs. In International Conference on Learning Representations . https:
//openreview.net/forum?id=BJOFETxR-
Uri Alon, Shaked Brody, Omer Levy, and Eran Yahav. 2018. code2seq: Generating sequences from
structured representations of code. arXiv preprint arXiv:1808.01400 (2018).
David Alvarez-Melis and Tommi S Jaakkola. 2016. Tree-structured decoding with doubly-recurrent
neural networks. (2016).
Aida Amini, Saadia Gabriel, Peter Lin, Rik Koncel-Kedziorski, Yejin Choi, and Hannaneh Ha-
jishirzi. 2019. Mathqa: Towards interpretable math word problem solving with operation-based
formalisms. arXiv preprint arXiv:1905.13319 (2019).
Daniel Andor, Chris Alberti, David Weiss, Aliaksei Severyn, Alessandro Presta, Kuzman Ganchev,
Slav Petrov, and Michael Collins. 2016. Globally Normalized Transition-Based Neural Networks.
In Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics
(Volume 1: Long Papers) . Association for Computational Linguistics, Berlin, Germany, 2442–
2452. https://doi.org/10.18653/v1/P16-1231
Gabor Angeli, Melvin Jose Johnson Premkumar, and Christopher D. Manning. 2015. Leveraging
Linguistic Structure For Open Domain Information Extraction. InProceedings of the 53rd Annual
Meeting of the Association for Computational Linguistics and the 7th International Joint Confer-
ence on Natural Language Processing (Volume 1: Long Papers). Association for Computational
Linguistics, Beijing, China, 344–354. https://doi.org/10.3115/v1/P15-1034
James Atwood and Don Towsley. 2016. Diffusion-Convolutional Neural Networks. In Advances
in Neural Information Processing Systems , D. Lee, M. Sugiyama, U. Luxburg, I. Guyon, and
R. Garnett (Eds.), V ol. 29. Curran Associates, Inc. https://proceedings.neurips.
cc/paper/2016/file/390e982518a50e280d8e2b535462ec1f-Paper.pdf
Jimmy Lei Ba, Jamie Ryan Kiros, and Geoffrey E Hinton. 2016. Layer normalization. arXiv
preprint arXiv:1607.06450 (2016).
Dzmitry Bahdanau, Kyunghyun Cho, and Yoshua Bengio. 2015. Neural Machine Translation by
Jointly Learning to Align and Translate. In 3rd International Conference on Learning Represen-
tations, Yoshua Bengio and Yann LeCun (Eds.).
88



---

## Ground Truth Questions

### T1 — Test Point 1 (after reading Part 1 only)

#### Category A: Conceptual Definitions (5 questions)

**Q1. [Conceptual definition]** What is the key difference between *graph filtering* and *graph pooling* as defined in Section 3 of the paper?

*Ground truth answer:* Graph filtering (f_filter) refines node embeddings using the graph structure and adjacency matrix but does NOT change the graph structure itself. Graph pooling (f_pool) takes a graph and its node embeddings as input and produces a SMALLER graph with fewer nodes and new node embeddings — it changes graph structure and is used to generate graph-level (whole-graph) embeddings. Filtering is stacked to produce final node embeddings; pooling aggregates them for graph-focused downstream tasks.

*Source:* Part 1, Section 3.1 Foundations / Section 3.2.2 Graph Pooling (pp. 8–9)

*Why this tests retention:* A vague summary says "GNNs use filtering and pooling" without capturing the structural distinction — filtering preserves graph topology while pooling coarsens it.

---

**Q2. [Conceptual definition]** How does the paper distinguish among the three ways of representing natural language, and which types of NLP techniques exemplify each?

*Ground truth answer:* (1) Bag of tokens — ignores position, only counts token frequency; exemplified by topic modeling (LDA), BoW, TF-IDF. (2) Sequence of tokens — captures order and co-occurrence; exemplified by linear-chain CRF and word2vec. (3) Graph — captures richer pairwise relationships; exemplified by dependency graphs, constituency graphs, AMR graphs, IE graphs, lexical networks, knowledge graphs.

*Source:* Part 1, Section 2.1 (pp. 4–5)

*Why this tests retention:* Summaries often collapse all three into "text can be a bag, sequence, or graph" without giving the specific example techniques.

---

**Q3. [Conceptual definition]** What two categories does the paper use to classify graph pooling layers, and how do they differ?

*Ground truth answer:* Flat graph pooling and hierarchical graph pooling. Flat pooling generates a graph-level representation directly from node embeddings in a single step (e.g., Max-pooling, Average-pooling, FCmax, BiLSTM aggregation). Hierarchical pooling coarsens the graph step-by-step through multiple pooling layers, each following a stack of graph filters; it either sub-samples the most important nodes or combines nodes into supernodes.

*Source:* Part 1, Section 3.2.2 Graph Pooling (pp. 12–13)

*Why this tests retention:* The flat/hierarchical distinction and the specific sub-types (subsampling vs. supernodes) are easily dropped in summaries.

---

**Q4. [Conceptual definition]** According to Section 2.2.5, what are the two main limitations of traditional graph-based algorithms that motivate the use of GNNs?

*Ground truth answer:* (1) Limited expressive power — traditional methods mostly capture structural information of graphs but do not consider node and edge features, which are important for NLP. (2) No unified learning framework — different graph-based algorithms have very different properties and settings and are only suitable for specific use cases. GNNs address both by providing a unified framework that transforms, propagates, and aggregates node/edge features through neural layers.

*Source:* Part 1, Section 2.2.5 Limitations and Connections to GNNs (p. 7)

*Why this tests retention:* Summaries often state "traditional methods are limited" without specifying the two precise limitations.

---

**Q5. [Conceptual definition]** What is a Message Passing Neural Network (MPNN) and what makes it general enough to subsume many existing GNNs?

*Ground truth answer:* MPNN (Gilmer et al., 2017) is a spatial-based graph filter framework that treats graph convolution as a message-passing process. It runs K-step iterations: for each target node v_i, a message function f_M computes messages from neighboring nodes (using node embeddings and edge features), and an update function f_U aggregates them to produce the new node embedding. MPNN is general because by choosing different f_U and f_M functions, one can recover many existing GNN architectures.

*Source:* Part 1, Section 3.2.1, Spatial-based Graph Filters (pp. 10–11)

*Why this tests retention:* The "generality through choice of f_U and f_M" is the key claim that is usually omitted.

---

#### Category B: Specific Claims (5 questions)

**Q6. [Specific claim]** What specific challenge does the paper identify about applying deep learning techniques designed for Euclidean data (such as images) to graph-structured data?

*Ground truth answer:* Deep learning techniques that were effective for Euclidean data (images) or sequence data (text) are not immediately applicable to graph-structured data due to the complexity of graph data — specifically its irregular structure and varying size of node neighborhoods. This gap drives the development of graph neural networks.

*Source:* Part 1, Section 1 Introduction (p. 2)

*Why this tests retention:* Summaries typically state "GNNs are needed for graphs" without preserving the precise diagnosis of "irregular structure and varying size of node neighbors."

---

**Q7. [Specific claim]** What problem does the renormalization trick in GCN (Kipf and Welling, 2016) solve, and what is the specific substitution it makes?

*Ground truth answer:* Repeated application of the spectral convolution operator (I_n + D^{-1/2} A D^{-1/2}) can cause numerical instability and exploding/vanishing gradients. The renormalization trick replaces I_n + D^{-1/2} A D^{-1/2} with D̃^{-1/2} Ã D̃^{-1/2}, where Ã = A + I_n and D̃_{ii} = Σ_j Ã_{ij} (i.e., adding self-loops to the adjacency matrix before normalizing).

*Source:* Part 1, Section 3.2.1, Spectral-based Graph Filters (p. 10)

*Why this tests retention:* The specific form of the trick (adding self-loops, Ã = A + I_n) is the kind of mathematical detail that gets dropped in any compression.

---

**Q8. [Specific claim]** What does the paper claim is the primary difference between GGNNs (Gated Graph Neural Networks) and typical GNNs?

*Ground truth answer:* The biggest modification from typical GNNs to GGNNs is the use of Gated Recurrent Units (GRU). GGNNs unfold the recurrence over a fixed T time steps and use backpropagation through time to compute gradients. The GGNN filter also takes both edge type and edge direction into consideration.

*Source:* Part 1, Section 3.2.1 Recurrent-based Graph Filters (p. 12)

*Why this tests retention:* Summaries conflate GGNNs with generic GNNs; the GRU + fixed-T-steps + edge-type specificity is the precise differentiator.

---

**Q9. [Specific claim]** What limitation does the paper identify about the BiLSTM aggregation function as a flat pooling operation?

*Ground truth answer:* The BiLSTM aggregation function is NOT permutation invariant on the set of node embeddings — unlike Max-pooling and Average-pooling. Despite this limitation, it has been often demonstrated to have better expressive power than other flat pooling operations (cited: Hamilton et al., 2017a; Zhang et al., 2019e).

*Source:* Part 1, Section 3.2.2 Graph Pooling (p. 13)

*Why this tests retention:* The permutation-invariance trade-off for expressive power is a subtle point that is lost in summaries.

---

**Q10. [Specific claim]** What three core challenges for GNNs in NLP does the introduction specifically enumerate?

*Ground truth answer:* (1) Automatically transforming original text sequence data into highly graph-structured data (automatic graph construction). (2) Properly determining graph representation learning techniques specially designed for unique characteristics of different graph structures (undirected, directed, multi-relational, heterogeneous). (3) Effectively modeling complex data — many NLP tasks involve learning mappings between graph-based inputs and highly structured outputs such as sequences, trees, and multi-type graphs.

*Source:* Part 1, Section 1 Introduction (p. 2)

*Why this tests retention:* All three challenges are listed as a bulleted set in the paper; summaries usually paraphrase them into one vague sentence.

---

#### Category C: Named Entities (5 questions)

**Q11. [Named entity]** Which specific GNN model is cited as the representative example of attention-based graph filters, and who proposed it?

*Ground truth answer:* Graph Attention Network (GAT), proposed by Velickovic et al. (2018). It introduces a multi-head attention mechanism to dynamically learn edge weights (attention scores) during message passing, computing semantic similarity between target and neighboring nodes and assigning higher attention scores to more important neighbors.

*Source:* Part 1, Section 3.2.1, Attention-based Graph Filters (p. 11)

*Why this tests retention:* The specific attribution to Velickovic et al. (2018) and the multi-head attention mechanism detail are both frequently lost.

---

**Q12. [Named entity]** What specific NLP tasks does the paper list as examples where GNNs have achieved success in classification tasks (as opposed to generation tasks)?

*Ground truth answer:* Classification tasks listed: sentence classification (Henaff et al., 2015; Huang and Carley, 2019), semantic role labeling (Luo and Zhao, 2020; Gui et al., 2019), and relation extraction (Qu et al., 2020; Sahu et al., 2019). Generation tasks listed for contrast: machine translation, question generation, and summarization.

*Source:* Part 1, Section 1 Introduction (p. 2)

*Why this tests retention:* The classification/generation distinction with specific task names is collapsed in summaries.

---

**Q13. [Named entity]** What paper or method does the survey cite as the representative NLP technique for the "bag of tokens" view of language?

*Ground truth answer:* Topic modeling (Blei et al., 2003) — specifically LDA (Latent Dirichlet Allocation) — is cited as the most representative technique for the bag-of-tokens view. It aims to model each input text as a mixture of topics where each topic can be further modeled as a mixture of words.

*Source:* Part 1, Section 2.1 (p. 4)

*Why this tests retention:* Summaries say "topic modeling" at best, rarely specifying LDA and Blei et al.

---

**Q14. [Named entity]** What does GraphSage (Hamilton et al., 2017a) do differently from earlier GNNs that makes it more efficient on large graphs?

*Ground truth answer:* GraphSage adopts sampling to obtain a fixed number of neighbors for each node, rather than using the full neighborhood. This addresses the inefficiency of processing all neighbors when a node can have thousands of neighbors in a large graph. The aggregation function N(v_i) is a random sample of neighboring nodes; the aggregation can be any permutation-invariant function (mean, sum, max).

*Source:* Part 1, Section 3.2.1, Spatial-based Graph Filters (p. 11)

*Why this tests retention:* The "fixed-size sampling" mechanism is the specific contribution that summaries omit.

---

**Q15. [Named entity]** What graph-based algorithm does the paper identify as the predecessor whose label-propagation paradigm is most directly analogous to GNN message passing?

*Ground truth answer:* Label Propagation Algorithms (LPAs). The paper states that "unlike traditional message passing based algorithms like LPA which operates by propagating labels across a graph, GNNs typically operate by transforming, propagating and aggregating nodes/edge features through several neural layers." LPA is the most direct predecessor — both propagate information iteratively across a graph, but GNNs use learnable neural transformations on features rather than label diffusion.

*Source:* Part 1, Section 2.2.5 Limitations and Connections to GNNs (p. 7)

*Why this tests retention:* The explicit LPA-to-GNN analogy is the key historical claim; summaries typically skip this lineage.

---

### T2 — Test Point 2 (after reading Parts 1–3; weighted ~3 P1, ~5 P2, ~7 P3)

**Q16. [P1 cross-reference]** The paper claims Transformers are a special case of GNNs. Based on the GNN foundations defined in Part 1 and the graph construction discussion in Parts 2–3, what type of graph does a Transformer operate on?

*Ground truth answer:* A Transformer operates on a fully connected dynamic graph constructed by using the self-attention mechanism. Every token attends to every other token, which corresponds to a complete graph where edge weights are computed dynamically via self-attention scores. This is discussed in Part 6 (Section 8.2) but the conceptual basis — attention-based graph filters as introduced for GAT in Part 1 — establishes the connection.

*Source:* Part 1 (GAT foundation) + Part 6 Section 8.2 GNNs vs. Transformers

*Why this tests retention:* Requires connecting the attention-based filter concept from Part 1 with the later explicit claim about Transformers.

---

**Q17. [P1 cross-reference]** The paper notes GCN limits layer-wise convolution to P=1. What consequence does this have for the receptive field of a GCN node, and how is it compensated?

*Ground truth answer:* Setting P=1 means each GCN layer only aggregates information from 1-hop neighbors (each central node depends only on nodes in the P-hop range). The receptive field is expanded by stacking multiple convolutional layers — each added layer increases the reachable neighborhood by one hop (K layers reaches K-hop neighbors).

*Source:* Part 1, Section 3.2.1 Spectral-based filters (p. 10)

*Why this tests retention:* The P=1 constraint and the multi-layer compensation is a specific technical detail, not just "GCN uses convolution."

---

**Q18. [P1 cross-reference]** When converting heterogeneous graphs to homogeneous graphs for use with standard GNNs (as described in Part 3), what information is typically discarded?

*Ground truth answer:* Edge type information is discarded. The conversion retains only connectivity (whether edges exist) and may encode edge weights as scalars, but multiple relation types are collapsed into a single adjacency matrix A where A_{i,j} = edge weight (or 1 for unweighted). This is described in Part 3, Section 5.1.1 "Static Graph: Treating Edge Information as Connectivity."

*Source:* Part 3, Section 5.1.1 (p. 27)

*Why this tests retention:* The specific cost of the conversion (losing edge type) is a key architectural trade-off.

---

**Q19. [P2]** What are the three steps involved in constructing a dependency graph from a paragraph, as described in Section 4.1.1?

*Ground truth answer:* (1) Constructing dependency relations — obtain the dependency parsing tree for each sentence; extract relations as (w_i, rel_{i,j}, w_j) triples where w_i depends on w_j with relation rel_{i,j}. (2) Constructing sequential relations — add sequential links between consecutive words to preserve positional information from the original text sequence. (3) Final graph conversion — map the collected nodes and edges into a formal graph G(V, E).

*Source:* Part 2, Section 4.1.1 Dependency Graph Construction (pp. 14–15)

*Why this tests retention:* The three-step structure, especially step 2 (sequential links for positional info), is easily lost.

---

**Q20. [P2]** What is the key characteristic of a "dynamic graph construction" approach versus a "static graph construction" approach?

*Ground truth answer:* Static graph construction builds the graph during preprocessing using existing NLP tools (e.g., dependency parsing) or manually defined rules; the graph structure is fixed before training. Dynamic graph construction (also called graph structure learning) learns the graph structure from data, constructing or refining graphs jointly with the downstream task during training. The paper notes that static construction encodes prior domain knowledge while dynamic construction enables task-specific, data-driven graph topology.

*Source:* Part 2, Section 4.2 Dynamic Graph Construction (pp. 23–24)

*Why this tests retention:* The "during training / jointly learned" aspect of dynamic construction versus "preprocessing / fixed" for static is the key contrast.

---

**Q21. [P2]** What is the time complexity problem identified for most dynamic graph construction techniques, and what solution is proposed to address it?

*Ground truth answer:* Most dynamic graph construction techniques rely on pair-wise node similarity computation, which has time complexity of at least O(n²) where n is the number of nodes. This causes scalability issues for large graphs such as knowledge graphs. A scalable solution using an anchor-based approximation technique that achieves linear time and memory complexity (avoiding explicit pair-wise computation) was proposed by Chen et al. (2020f).

*Source:* Part 2 / Part 6 (Section 8.1 Dynamic Graph Construction challenge, p. 84)

*Why this tests retention:* The specific O(n²) complexity and the anchor-based linear solution are concrete details that disappear from summaries.

---

**Q22. [P2]** What two types of graphs can be formed by combining intrinsic and implicit graph structures in dynamic construction, and why does the paper argue this combination is important?

*Ground truth answer:* (1) Intrinsic graph structures — derived from prior knowledge (e.g., dependency parse trees). (2) Implicit graph structures — learned from data via dynamic graph construction. The paper argues this combination is important because several studies showed that totally discarding the intrinsic graph structure while doing dynamic construction can hurt downstream task performance, likely because intrinsic graphs carry rich and reliable structured information.

*Source:* Part 2, Section 4.2.3 Combining Intrinsic and Implicit Graph Structures (p. 26)

*Why this tests retention:* The "hurts performance if discarded" finding is a specific empirical claim about a design decision.

---

**Q23. [P2]** What does the paper list as the eleven categories of static graph construction methods?

*Ground truth answer:* Dependency Graph, Constituency Graph, AMR Graph, Information Extraction Graph, Discourse Graph, Knowledge Graph, Coreference Graph, Topic Graph, Similarity Graph, Co-occurrence Graph, and Application-driven Graph. (Table 2 provides the full list with references for each.)

*Source:* Part 2, Section 4.1 (Table 2, pp. 13–14)

*Why this tests retention:* The count of 11 and the full enumeration (especially less-obvious ones like Discourse Graph, Topic Graph) is precisely what gets omitted.

---

**Q24. [P3]** What is the formal definition of a homogeneous graph as used in Section 5, and why do standard GNNs (GCN, GAT, GraphSage) fail to directly handle many NLP graphs?

*Ground truth answer:* A homogeneous graph G(V, E, T, R) is defined as one where |T| = 1 and |R| = 1 (exactly one node type and one edge type). Standard GNNs (GCN, GAT, GraphSage) are designed for homogeneous graphs. They fail to directly handle many NLP graphs because natural language graphs (e.g., dependency graphs) are arbitrary graphs containing multiple relation types — they are multi-relational or heterogeneous — which cannot be directly exploited by traditional GNN methods.

*Source:* Part 3, Section 5.1 GNNs for Homogeneous Graphs (p. 27)

*Why this tests retention:* The formal |T|=1, |R|=1 definition and the specific reason for failure are both lost in casual summaries.

---

**Q25. [P3]** What is R-GCN (Relational Graph Convolutional Network) and what problem does it address in multi-relational graphs?

*Ground truth answer:* R-GCN (Schlichtkrull et al., 2018) is a GNN model for multi-relational graphs that applies relation-specific transformation matrices to unify features across different relation types before aggregating them. It adds a self-connection with a special relation type to retain the node's own features. R-GCN addresses the challenge of modeling multiple relation types in a single framework. However, using separate parameters for each relation can cause over-parameterization; R-GCN uses matrix decomposition as a basis trick to address this.

*Source:* Part 3, Section 5.2 GNN for Multi-relational Graphs (pp. 30–32)

*Why this tests retention:* The matrix decomposition trick for over-parameterization is a specific mitigation that is always dropped.

---

**Q26. [P3]** How does the paper define a heterogeneous graph, and what is a "meta-path" in the context of heterogeneous GNNs?

*Ground truth answer:* A heterogeneous graph is G(V, E, T, R) where |T| > 1 or |R| > 1 (multiple node types and/or multiple edge types). A meta-path is a composite relation defined over a sequence of node and edge types that describes a semantic path connecting two nodes through different types. In heterogeneous GNNs, neighbor aggregation is performed along different meta-paths; "node-level aggregation" collects neighbors for each meta-path, then "meta-path level attention" learns the importance of different meta-paths.

*Source:* Part 3, Section 5.3 GNNs for Heterogeneous Graphs (pp. 37–38)

*Why this tests retention:* The two-level attention hierarchy (node-level + meta-path level) is specific and easily missed.

---

**Q27. [P3]** What is "structure-aware similarity metric learning" in dynamic graph construction, and how does it differ from purely node-embedding-based similarity?

*Ground truth answer:* Node-embedding-based similarity metrics assume that node attributes alone contain sufficient information to learn the implicit graph structure, computing similarity purely from node feature vectors. Structure-aware similarity metric learning additionally considers existing edge information (intrinsic graph structure) beyond node features — inspired by structure-aware transformers (Zhu et al., 2019b; Cai and Lam, 2020b). For example, Liu et al. (2019a) proposed a structure-aware attention mechanism that incorporates edge information into the similarity function.

*Source:* Part 2, Section 4.2.1 Graph Similarity Metric Learning (pp. 24–25)

*Why this tests retention:* The "edge information" as a second input beyond node embeddings is the precise differentiator.

---

**Q28. [P3]** What is the "over-smoothing" problem in GNNs and where is it mentioned as a challenge?

*Ground truth answer:* Over-smoothing refers to the phenomenon where, as more GNN layers are stacked, all node representations converge to similar values, losing discriminative information. The paper mentions it as a general challenge for GNNs in NLP (Section 8.1 and in the discussion of graph representation learning), noting that residual connections were introduced to GCN architectures to avoid over-smoothing when stacking many layers (Zhou et al., 2020a in Section 7 on summarization, p. 73). It is listed as part of the challenges for scaling graph representation learning.

*Source:* Part 3 (implicit in representation learning discussion) + Part 6 Section 8 (explicitly named)

*Why this tests retention:* The term is used but the specific technical solution (residual connections) is a detail that proves the reader actually read the text.

---

**Q29. [P3]** What is the Gated Graph Neural Network for multi-relational graphs (R-GGNN) and how does it extend GGNN?

*Ground truth answer:* R-GGNN extends GGNN (which uses GRU-based recurrent filters) to multi-relational graphs. The propagation rule r^(k)_i = σ(Σ ...) accumulates messages from neighbors across different relation types using relation-specific parameters. While GGNN processes a single graph with edge types and directions (as described in Part 1), R-GGNN specifically handles the case of multiple relation types by maintaining separate parameter matrices per relation, then uses GRU gating to update node states.

*Source:* Part 3, Section 5.2 (pp. 31–32)

*Why this tests retention:* R-GGNN is a distinct named model; conflation with basic GGNN loses the multi-relational extension.

---

**Q30. [P3]** According to the paper, what are the three sub-categories of GNN methods for homogeneous graphs in Section 5.1 and what distinguishes them?

*Ground truth answer:* (1) Static graph with edge information treated as connectivity — edge types are discarded, graph is collapsed to a single adjacency matrix A. (2) Bidirectional encoding — extends GNNs to handle directed graphs by separately computing incoming and outgoing neighbor sets (N⁻(v_i) for backward, N⁺(v_i) for forward), as in Xu et al. (2018b)'s bidirectional GraphSage extension. (3) Dynamic graphs treated as homogeneous — uses the dynamic graph construction output but processes it with standard homogeneous GNN methods.

*Source:* Part 3, Section 5.1 (pp. 27–29)

*Why this tests retention:* The bidirectional encoding as a distinct sub-category with the notation N⁻ and N⁺ is specific.

---

### T3 — Test Point 3 (after reading all 6 Parts; weighted 1 P1, 1 P2, 2 P3, 3 P4, 4 P5, 4 P6)

**Q31. [P1 → P6 connection]** The paper introduces GCN (Kipf and Welling, 2016) in Part 1 as a spectral method. In Part 6 Section 8.5 (Multi-relational GNNs), what limitation does R-GCN (which extends GCN to multi-relational graphs) face, and what specific trick is used to mitigate it?

*Ground truth answer:* R-GCN faces an over-parameterization problem because it uses separate parameter matrices for each relation type. As the number of relations grows, the number of parameters explodes, harming generalization. The mitigation is matrix decomposition as a basis trick (also called basis decomposition), which constrains the per-relation matrices to be linear combinations of a small set of shared basis matrices. Additionally, Directed-GCN (Marcheggiani and Titov, 2017) uses parameter-sharing as another strategy. These are noted as imperfect — they risk reducing the model's expression ability.

*Source:* Part 1 (GCN foundation) + Part 6, Section 8.5 Multi-relational GNNs (p. 87)

*Why this tests retention:* Requires holding the GCN definition from Part 1 and connecting it to the specific over-parameterization critique of R-GCN in Part 6.

---

**Q32. [P2 → P6 connection]** Section 4 (Part 2) introduces knowledge graphs as a type of static graph for NLP. Section 8.4 (Part 6) identifies three specific challenges for GNN-based KG alignment models. What are they?

*Ground truth answer:* (1) Different KGs usually have heterogeneous schemas, which may mislead representation learning and make it difficult to integrate knowledge from different KGs (Cao et al., 2019c; Wu et al., 2019a). (2) KG data is usually incomplete, which requires pre-processing (Sun et al., 2020b). (3) Seed alignments are limited (Li et al., 2019); how to iteratively discover new entity alignments in a GNN-based framework remains a future direction.

*Source:* Part 2 (KG introduced) + Part 6, Section 8.4 Knowledge Graph Alignment (p. 87)

*Why this tests retention:* The three specific challenges (schema heterogeneity, incompleteness, limited seeds) require reading Part 6 carefully.

---

**Q33. [P3 → P5 connection]** In Part 3, structure-aware self-attention is introduced for multi-relational graphs. In Part 5, which NLP application task is identified as using a "graph-augmented transformer" with a relation-aware multi-head attention mechanism, and which paper proposes it?

*Ground truth answer:* The Question Generation task (Natural Question Generation). Sachan et al. (2020) proposed a graph-augmented transformer model employing a relation-aware multi-head attention mechanism similar to Zhu et al. (2019b) and Cai and Lam (2020b). Pan et al. (2020) and Sachan et al. (2020) both found it beneficial to additionally model relational structure in question generation.

*Source:* Part 3 (structure-aware self-attention defined) + Part 5, Section 7 (QG application, p. 62)

*Why this tests retention:* Requires connecting the abstract mechanism from Part 3 to a specific named paper and task in Part 5.

---

**Q34. [P3 → P4 connection]** Graph2Seq models (Part 4) require an encoder for graph-structured inputs. What specific GNN architectures and embedding initialization strategies does the paper list as commonly used in Graph2Seq encoders?

*Ground truth answer:* For graph encoder: both homogeneous GNNs and multi-relational GNNs have been explored. For embedding initialization: (1) random initialization, (2) pre-trained word embeddings (GloVe, word2vec), (3) BERT embeddings + BiRNNs (Xu et al., 2020a; Chen et al., 2020g), (4) RoBERTa + BiRNNs (Huang et al., 2020b). The sequential decoding side reuses common Seq2Seq decoding techniques (attention, copying mechanism, coverage) since the main difference from Seq2Seq is on the encoder side.

*Source:* Part 4, Section 6.2.2 Graph2Seq Approach (pp. 46–47)

*Why this tests retention:* The BERT/RoBERTa + BiRNN initialization combination is a specific technical detail.

---

**Q35. [P4]** What are the three types of encoder-decoder models introduced in Section 6 as "GNN-based encoder-decoder models," and what distinguishes them by input/output type?

*Ground truth answer:* (1) Graph2Seq — graph input, sequence output. Used for tasks like machine translation, summarization, KG-to-text, SQL-to-text, code summarization, semantic parsing. (2) Graph2Tree — graph input, tree output (used for tasks where the output has hierarchical structure, e.g., semantic parsing, code generation, math word problem solving). (3) Graph2Graph — graph input, graph output (used for tasks like information extraction, AMR parsing, molecule optimization, retrosynthesis). The section also covers Seq2Seq as the baseline before introducing these.

*Source:* Part 4, Sections 6.1–6.4 (pp. 43–53)

*Why this tests retention:* The three-way taxonomy with specific task examples for each is frequently collapsed to "graph encoder-decoder models."

---

**Q36. [P4]** What is the "copying mechanism" introduced in the Seq2Seq framework, and why is it particularly useful for graph-based NLP?

*Ground truth answer:* The copying mechanism (Vinyals et al., 2015; Gu et al., 2016) allows the decoder to directly copy tokens from the input sequence to the output sequence in a learnable manner, rather than only generating from a fixed vocabulary. It is useful for tasks where the output should contain exact tokens from the input (e.g., named entities in summarization, variables in code generation). For graph-based NLP, where inputs may be structured as knowledge graph nodes or dependency parse tokens, copying allows the model to transfer specific node labels directly to the output.

*Source:* Part 4, Section 6.1.2 Approach (p. 44)

*Why this tests retention:* The Vinyals et al./Gu et al. attribution and the learnable copy (not just pointer) distinction are specific.

---

**Q37. [P4 + P5]** What three categories of sub-problems does the paper identify for Graph2Graph models, and which NLP task is used as the example to illustrate Graph2Graph approaches?

*Ground truth answer:* The three sub-problem categories are: (1) node transformation, (2) edge transformation, and (3) node-edge-co-transformation. Information extraction (IE) is used as the primary example task to illustrate Graph2Graph approaches in Section 6.4.2. The paper notes that Graph2Graph approaches have also been applied to molecule optimization and malware confinement in cyber security, but IE is the canonical NLP illustration.

*Source:* Part 4, Section 6.4 Graph2Graph (pp. 51–52)

*Why this tests retention:* The three transformation categories and the IE example together are specific; summaries often only mention "graph-to-graph" vaguely.

---

**Q38. [P5]** For the Neural Machine Translation (NMT) application, what is the main structural limitation of conventional seq2seq NMT systems that GNN-based methods address?

*Ground truth answer:* Conventional seq2seq NMT systems regard input text as sequences and apply encoders like LSTM or Transformer, which fail to utilize the rich structural information (syntactic structure) implicitly present in natural language inputs. GNN-based NMT methods cast the conventional seq2seq diagram to incorporate structural knowledge — specifically syntactic dependency graphs — to address challenges like the long-dependency problem.

*Source:* Part 5, NMT application (pp. 55–57)

*Why this tests retention:* The specific "long-dependency problem" as the challenge addressed by structural knowledge is a precise claim.

---

**Q39. [P5]** What evaluation metric is used for the Neural Machine Translation task and what metric is used for Named Entity Recognition, according to Table 3?

*Ground truth answer:* Neural Machine Translation uses BLEU. Named Entity Recognition (NER) uses Precision, Recall, and F1. (Table 3 in Section 7 provides a comprehensive mapping of NLP application tasks to their evaluation metrics.)

*Source:* Part 4/5, Table 3 (p. 54)

*Why this tests retention:* The specific NER evaluation metric (Precision/Recall/F1) vs. NMT's BLEU is the kind of factual detail that is retained from tables only by careful readers.

---

**Q40. [P5]** What GNN library do the authors introduce specifically for NLP, and what are its four architectural layers?

*Ground truth answer:* The authors introduce Graph4NLP. Its four architectural layers are: (1) Data Layer, (2) Module Layer, (3) Model Layer, and (4) Application Layer. Graph4NLP is built upon DGL and PyTorch, provides whole-pipeline support with flexible interfaces, and aims for both high running efficiency and extensibility.

*Source:* Part 6, Section 7 end / benchmark tools (p. 84)

*Why this tests retention:* The four-layer architecture name and the DGL+PyTorch foundation are specific to Graph4NLP and not mentioned elsewhere.

---

**Q41. [P5 + P6 cross-section]** The paper covers Math Word Problem (MWP) solving in Section 7 (Part 5/6). What three benchmark datasets are commonly used for MWP evaluation?

*Ground truth answer:* MAWPS (Koncel-Kedziorski et al., 2016), MATH23K (Wang et al., 2017), and MATHQA (Amini et al., 2019). All three are listed as commonly used benchmarks for math word problem solving.

*Source:* Part 5/6, Section 7 Math Word Problem (p. 81)

*Why this tests retention:* Three distinct dataset names with different authors/years; any two of three would be partial credit, all three requires exact reading.

---

**Q42. [P6]** Section 8.2 discusses "GNNs vs. Transformers." According to the paper, what is the key downside of Transformers that GNNs do not share?

*Ground truth answer:* Transformers cannot directly operate on complex data like graph-structured data; they are designed for sequential inputs and model graph topology only implicitly through attention. GNNs, in contrast, are a more generic model architecture that directly operates on graph data. The downside of Transformers is that "the graph data modeling [is] inside the transformer model" and separated from the inputs, meaning users cannot directly feed heterogeneous or multi-relational graph structure to the model.

*Source:* Part 6, Section 8.2 GNNs vs. Transformers (p. 85)

*Why this tests retention:* The specific claim that Transformers "cannot directly operate on more complex data like graph-structured data" is a nuanced position that is easy to misread as "Transformers are worse."

---

**Q43. [P6]** What specific scalability limitation does the paper identify for dynamic graph construction, and what future directions are proposed to address it beyond the anchor-based method?

*Ground truth answer:* The primary scalability limitation is O(n²) pair-wise node similarity computation. Beyond the anchor-based linear approximation (Chen et al., 2020f), the paper proposes that efficient transformer designs (Tsai et al., 2019; Katharopoulos et al., 2020; Choromanski et al., 2021; Peng et al., 2021; Shen et al., 2021; Wang et al., 2020a) could inspire scalable dynamic graph construction approaches. Additional future directions include: dynamically learning edge directions, and combining static and dynamic graph construction.

*Source:* Part 6, Section 8.1 Dynamic Graph Construction (pp. 84–85)

*Why this tests retention:* The list of efficient transformer papers and the two additional future directions (edge directions, static+dynamic hybrid) are specifics lost in any compression.

---

**Q44. [P6, multi-section]** What does the paper's conclusion (Section 9) identify as the three dimensions of the taxonomy it proposes, and how does this differ from the abstract's claim?

*Ground truth answer:* Section 9 Conclusion states the taxonomy organizes GNNs for NLP along "three dimensions: graph construction, graph representation learning, and the overall encoder-decoder models." However, the abstract says "three axes: graph construction, graph representation learning, and graph based encoder-decoder models" — matching. But the introduction (p. 3, Fig. 1) describes the taxonomy along FOUR axes: graph construction, graph representation learning, encoder-decoder models, AND applications. The paper is internally inconsistent — the abstract and conclusion say three, but Fig. 1 and the intro say four.

*Source:* Part 1 (Abstract + Section 1 p. 3) vs. Part 6 Section 9 (p. 87)

*Why this tests retention:* The abstract/conclusion vs. figure discrepancy (3 vs. 4 axes) requires having read both ends of the paper and noticing the inconsistency. Most summaries just say "three axes."

---

**Q45. [P5 + P6 multi-part]** For Knowledge Graph Completion (KGC), what is the trade-off the paper describes between training on the entire KG vs. training on per-triple subgraphs, and which approach offers what advantage?

*Ground truth answer:* Training all triples on the same large KG (e.g., Shang et al., 2019) provides more computational efficiency. Training each triple on a separate knowledge subgraph constructed from the original KG (e.g., Teru et al., 2020; Xie et al., 2020) provides more powerful model expressiveness. The paper frames this as a hard trade-off between computational efficiency and model expressiveness, and suggests future research should focus on jointly reasoning over text and KG while applying these methods.

*Source:* Part 5/6, Section 7 KGC (p. 75) + Section 8.4 (p. 86)

*Why this tests retention:* The efficiency vs. expressiveness trade-off framing with the specific paper citations on each side is the exact detail that disappears in summaries.
