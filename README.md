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

## Command Line Interface
The main way to use Qiana as a tool is to use the Command Line Interface.
To learn how to run the CLI, run 
```
python3 src/script/qianaCLI.py -h
```

## Graphical User Interface
The GUI of Qiana is only meant for quick tests and as a demonstration. It can be quite brittle.
To run the GUI for Qiana, run the following from the src directory.
```
python3 src/script/qianaGUI.py
```

(On windows you might need to replaced "python3" with "python")

## Requirements

The GUI version has additional requirements.

The following python packages can be install with pip
```
pip install pydotplus
pip install pyside6
```

In some system you might need to install libxcb-cursor-dev to run PySide6 graphical applications, which is useful for the GUI of Qiana.
Installing with apt
```
sudo apt install libxcb-cursor-dev
```

You also need to install Graphviz
```
sudo apt install graphviz
```

# Writting Qiana formulas in TPTP
The following conventions are used within this tool to translate formal mathematical notations to TPTP formulas.
For any function or predicate ```f``` or ```p```, their quotation is written ```q_f``` (resp ```q_p```).
No other symbol may start with ```q_``` except the ones listed bellow. In particular, because functions and predicates cannot start with an uppercase letter, we list bellow all the symbols starting with ```q_``` followed by an uppercase letter that are allowed.

| Qiana      | TPTP translation      |
| ------------- | ------------- |
| $\mathbb{Q}$ | q_Quote |
| $\textbf{T}$ | q_Truth |
| $\underline{\neg}$ | q_Neg |
| $\underline{\land}$ | q_And |
| $\underline{\lor}$ | q_Or |
| $\underline{\forall}$ | q_Forall |
| E | eval |
| isTerm | term |
| Wft | wft |
| sub | sub |

The quoted variables are written q_X1, q_X2, and so forth. Note that by default 5 quoted variables are used, so the complete list of quoted variables is q_X1, q_X2, q_X3, q_X4, and q_X5.

# On logic signatures
The signature at hand will automatically be deduced from the input TPTP formulas. However quoted symbols and predicates are not used for this (because it would be impossible to always know if they quote a function or a predicate). For this reason, each function or predicate that needs to be present in the signature of the logic should appear unquoted in the input formulas.
This can always be done by adding a tautological formula with the symbol in question to the input. For example:
```
fof(trivial_arity_2, axiom, ![X1] : ((p(f(x1,X1),f(X1,X1))) => (p(f(x1,X1),f(X1,X1))))).
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
