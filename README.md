# Qiana
Qiana is a logic framework for reasoning with contexts. Qiana takes as input logical formulas such as
> forall phi, x: says(Einstein, phi) => believes(x, phi)
> 
> forall phi: says(Einstein, phi) => phi
> 
> says(Einstein, not (forall x: glitters(x) => gold(x)))

These formulas say: everyone believes everything Einstein says; everything Einstein says is true; and Einstein says that not all that glitters is gold. Qiana can translate these formulas to first order logic, so that a standard first-order-logic reasoner such as [Vampire](https://vprover.github.io/) can do theorem proving on these formulas. 

<!--
It presents itself as a set of axiom schemes within standard first-order logic. Together, these axioms allow to operate a form of higher-order reasoning within first-order logic. \
In Qiana, this trick is used to implement contextual statements through a special $ist$ predicate.
$ist(c, \varphi)$ means that $\varphi$ is true in context $c$.
Qiana also comes with software that takes as input a given finite first-order theory $H$ and outputs another theory that is equisatisfiable with the closure of $H$ under the schemes of Qiana. 
Concretely, this software allows to perform automated theorem proving on arbitrary (finite) Qiana theories. 
To perform the theorem proving step you need a compatible theorem prover .

For example, here is the same statement in natural language, in the Qiana formal logic, and in the TPTP syntax used as input for the software.

- Romeo believes that Juliet is dead

- $\textit{ist}(\textit{Romeo}, \underline{\textit{dead}(\textit{Juliet})})$

- ist(Romeo, q_dead(q_Juliet))
-->

# Repository structure
This repository contains
1. our publication about Qiana, published at the conference KR 2024, which explains our formalism. The extended version includes appendices.
2. the code that transforms a theory with contexts into a first-order-logic theory
3. an example input with an example output

# Running the code
The code computes the Qiana closure of a given input theory. Both the input and the output are in [TPTP format](https://www.tptp.org/).

By convention, symbols starting with the letter q are quotations of the symbols that share the same name without the q. This is equivalent to underlining logic symbols in the article. For example, ```q_Alice``` is the quotation of ```Alice```. No symbol that is not a quotation should start with "q\_". The quotation of the usual first-order operators are available as "q_And", "q_Not", "q_Implies", and "q_Forall". In our example code, the total number of quoted variables is set to 3+the number of variables used in the input. 

To run the demo code on the provided example input, run
```
python3 Qiana.py ../example/input-example.p output.p
```

# Citing Qiana
If you use Qiana in scientific work, please cite our article

```
@inproceedings { Qiana, 
    author   = "Coumes, Simon and Paris, Pierre-Henri and Schwarzentruber, François and Suchanek, Fabian",
    title    = "Qiana: A First-Order Formalism to Quantify over Contexts and Formulas",
    booktitle = "KR",
    year     = 2024
}
```

# License
Qiana was developed by [Simon Coumes](https://perso.eleves.ens-rennes.fr/people/simon.coumes/index.html), [Pierre-Henri Paris](https://phparis.net/), [Fabian Suchanek](https://suchanek.name/), and [François Schwarzentruber](https://people.irisa.fr/Francois.Schwarzentruber/). The code in this repository is available under the MIT license, see the file LICENSE.md.

# Acknowledgments
This work was funded by the [NoRDF project](https://nordf.telecom-paris.fr/fr/) (ANR-20-CHIA-0012-01).
