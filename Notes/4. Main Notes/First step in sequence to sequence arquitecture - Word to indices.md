2026-09-27 12:32
Tags: Math Theory Comprehension

---

Initially a index of almost every word in the dictionary is initialized, {"the": 1, "cat": 4521, ...}.
(important note, in current models this mapping is no lonfer used, the way its done its by sub word tokanizers ej. BPE which split words into pieces)

When our input sentence is passed to the model, we find the corresponding word to the index in the dictionary. for those unknown its set to 0.

$$\mathbf{o}_w \in \{0,1\}^{V}, \quad (\mathbf{o}_w)_k = 1, \text{ all other entries } 0$$
The formula above represents the O as one-hot vector and the w standing for the word, with $\in$$\in$ meaing, "is a elemnt of" or simply "is a", and V is the vocabulary size. 

So the one hot vector of the word, is a elemnt is a list of leangt V made up of either 0 or 1
and  The one hot vector is equal to one in the K entry and all other entries are 0 

> The one hot vector for a word, is a list as long as the vocabulary, made up of all zeros except for the 1 where the index mach
>
> Important to mention that in practice one hot vectors are not built, code just keeps the Ids, and fetches them from the embedding directly


---
# Questions

1. Is vocabulary then used in this context as the input sentence? and not as the initial matrix? 
     No, The fixed list of _all_ words the model knows, with their IDs
2. So do you end up with as many one-hot vectors as words in the input sentence? And what is the leanght of the one-hot-vectors?
     Yes, and each one hot vectors is as long as the vocabulary
3. Im guessing the vocab here is only for the input language not both?
     Yes, there are two vocabs, one per language
---
# References
[[Sequence to Sequence Learning with Neural Networks]]
[[Seq2Seq Animation.mp4]]
[[One-Hot-Encoding]]