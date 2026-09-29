2026-09-27 13:09
Tags:

---
One-hot encoding represents a category (e.g. a word) as a vector whose length equals the number of possible categories (e.g. the vocabulary size). All entries are 0 except a single 1 at that category's index.


> It is used because it lets you feed categories into a model without implying a false order or size.
> One-Hot Vectors are equally distant from each other, so no category is favoured 

---
# Questions
1. I dont understand how having a list of zeros and a single 1 helps the model learn anything 
      It doesnt help the model learn anything but it lets it select a row, since zeroes cancel everything out $$  
\underbrace{[0,\ 1,\ 0]}_{\text{"cat"}}  
\times  
\underbrace{\begin{bmatrix} 0.2 & -0.5 \\ \mathbf{0.7} & \mathbf{0.1} \\ -0.3 & 0.9 \end{bmatrix}}_{E}  
= [0.7,\ 0.1]  
$$This means that when the training updates it updates only that row.
        Ej When the model makes a mistake on a sentence containing "cat", the gradient flows back to $E$. Because of the one-hot, the gradient is zero everywhere except row "cat": $$\frac{\partial \mathcal{L}}{\partial E} = \mathbf{o}_{\text{cat}} \left(\frac{\partial \mathcal{L}}{\partial \mathbf{e}_{\text{cat}}}\right)^\top$$ So each sentence nudges only the rows of the words it contains.




2. .
     .
3. .
4. 
---
# References

