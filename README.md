# Qiana
Qiana is first and foremost a logic framework for contextual reasoning.
It presents itself as a set of axiom schemes within standard first-order logic. Together, these axioms allow to operate a form of higher-order reasoning within first-order logic. \
In Qiana, this trick is used to implement contextual statements through a special $ist$ predicate.
$ist(c, \varphi)$ means that $\varphi$ is true in context $c$.
Qiana also comes with software that takes as input a given finite first-order theory $H$ and outputs another theory that is equisatisfiable with the closure of $H$ under the schemes of Qiana. 
Concretely, this software allows to perform automated theorem proving on arbitrary (finite) Qiana theories. 
To perform the theorem proving step you need a compatible theorem prover such as [Vampire](https://vprover.github.io/).

# Repository structure
This repository contains all available materials relative to the Qiana logic as of August 2024.
This notably includes:
1. The long form of the article "Qiana: A First-Order Formalism to Quantify over Contexts and Formulas", which explains what Qiana is and how it works in details.
The longform includes appendices not included in the KR2024 publication.
2. The demo code to compute the Qiana closure of a given input first-order theory.

The article is available in the "publication" folder while the rest of the repository is dedicated to the demo code.

# Runing the code
This demo code computes the Qiana closure of a given input theory. 
Both the input and the output are presented in TPTP format.

By convention, symbols starting with the letter q are quotations of the symbols that share the same name without the q. This is equivalent to underlining logic symbols in the article.
For exemple, ```q_Alice``` is the quotation of ```Alice```. No symbol that is not a quotation should start with "q\_". \
The quotation of the usual first-order operators are available as "q_And", "q_Not", "q_Implies", and "q_Forall".

In this example code, the total number of quoted variables is set to 3+the number of variables used in the input. 

To call the example code with input in the file "input.p" to output the qiana closure in the file "output.p", on a linux machine you can run

```
python3 Qiana.py input.p output.p
```

On a windows machine you can run
```
python Qiana.py input.p output.p
```

To run the demo code on the provided example input, run
```
python3 Qiana.py input-example.p output.p
```

# Citing
Qiana is awaiting publication in the proceedings of the KR2024 conference. 
The Bibtex code for citing Qiana will be added here once the proceedings are released.

# License
The demo code in this repository is available under the MIT license. See the LICENSE.md file.