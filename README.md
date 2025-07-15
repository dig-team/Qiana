# Qiana
Qiana is a logic framework for reasoning with contexts. Qiana takes as input logical formulas such as
> forall phi, x: says(Einstein, phi) => believes(x, phi)
> 
> forall phi: says(Einstein, phi) => phi
> 
> says(Einstein, not (forall x: glitters(x) => gold(x)))

These formulas say: everyone believes everything Einstein says; everything Einstein says is true; and Einstein says that not all that glitters is gold. Qiana can translate these formulas to first order logic, so that a standard first-order-logic reasoner such as [Vampire](https://vprover.github.io/) can do theorem proving on these formulas. 

To learn more about Qiana, read the "Qiana-journal-preprint.pdf" file in the "publication" directory.

This repository contains
1. Our publication about Qiana, published at the conference KR 2024, which explains our formalism. The extended version includes appendices. A preprint of an upcoming journal version is also available.
2. The code that transforms a theory with contexts into a first-order-logic theory and runs the integrated prover on it, allowing automated reasoning within Qiana
4. An example input with an example output

# Using Qiana
## Installation
You can install Qiana in development mode directly from the repository:
```bash
pip install -e .
```

## Command Line Interface
After installation, you can use the `qiana` command directly:
```bash
qiana -h
```

Alternatively, you can still run the CLI script directly:
```bash
python3 src/script/qianaCLI.py -h
```

## Python package
After installation, you can import Qiana in your Python code:
```python
from qiana import QianaPipeline, run_qiana
```

If you prefer the old method, you can still drop the directory ```src/qiana``` in your own ```src``` dir and import Qiana with 
```from qiana import QianaPipeline, run_qiana```.

See the file ```docs/HACK.md``` or the docstring of these imports for more.

## Graphical User Interface
The GUI of Qiana is only meant for quick tests and as a demonstration. It can be quite brittle.
To run the GUI for Qiana, run the following from the src directory.
```
python3 src/script/qianaGUI.py
```

(On windows you might need to replaced "python3" with "python")

## Requirements

### Core Installation
The core Qiana package has no external dependencies and only requires Python 3.8+.

### GUI Dependencies
For GUI functionality, additional requirements are needed. These can be installed with:
```bash
pip install -e ".[gui]"
```

Or manually with:
```bash
pip install -r requirements_gui.txt
```

### System Dependencies
You also need to install Graphviz for diagram generation:
```bash
sudo apt install graphviz
```

On some systems you might need to install libxcb-cursor-dev to run PySide6 graphical applications:
```bash
sudo apt install libxcb-cursor-dev
```

## Integrated solver
Qiana uses the Vampire first-order theorem prover and comes bundled with the binary file for Linux as that is the one provided by the developers.
If you need to make Qiana run with Vampire on another platform, you can compile Vampire on your platform and drop the resulting file as ```[...]/qiana/reasoner/vampire```. See instructions on [Vampire's website](https://vprover.github.io/download.html).

In any case, the important part of Qiana is the computation of the Qiana closure and the solver is only bundled with it for convenience's sake.
You can use another TPTP prover such as GKC with:
```
qiana -c -o closure.p input_file.p && YOU_SOLVER closure.p
```


# Writing formulas
Qiana formulas are written as TPTP formulas.

## Conventions
The translation of the formalism of Qiana to TPTP formulas requires some arbitrary conventions.
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
| E | q_Eval |
| term | q_Term |
| Wft | q_Wft |
| Sub | q_Sub |

The quoted variables are written q_X1, q_X2, and so forth. Note that by default 5 quoted variables are used, so the complete list of quoted variables is q_X1, q_X2, q_X3, q_X4, and q_X5.

## Simplified syntax
By default, your input nees to be full TPTP formulas including headers, such as:
```
fof(formula1, axiom, love(romeo,juliet) => like(romeo,juliet)).
fof(formula2, axiom, love(romeo,juliet)).
fof(goal, conjecture, like(romeo,juliet)).
```

With the ```--simplifiedInput``` flag, you can ommit these headers. Note that the dots are still required between formulas and that the conjecture has to be negated (we are looking for a contradiction).

```
love(romeo,juliet) => like(romeo,juliet).
love(romeo,juliet).
~like(romeo,juliet).
```

## Macros
Qiana's ability to do high order reasoning relies on "quoted formulas", terms that represent formulas. They are notably used to represent what is true within a context.
To make writing these easier, we provide "context macros" that automatically quote formula to make valide statements about contexts.
We show bellow some examples of the formula in natural language, the formula with macros, and the formula without macros.


```
Juliet believes Romeo is pretty.
!believes(juliet,pretty(romeo)).
ist(believes(juliet), q_pretty(q_romeo)).
```

Remark that this example uses the simplified syntax. 
To use macros, call Qiana with the flag ```--expandMacros```.

# On logic signatures
The signature at hand will automatically be deduced from the input TPTP formulas. However quoted symbols and predicates are not used for this (because it would be impossible to always know if they quote a function or a predicate). For this reason, each function or predicate that needs to be present in the signature of the logic should appear unquoted in the input formulas.
This can always be done by adding a tautological formula with the symbol in question to the input. For example:
```
fof(trivial_arity_2, axiom, ![X1] : ((p(f(x1,X1),f(X1,X1))) => (p(f(x1,X1),f(X1,X1))))).
```

# Modifying the code
If you want to read or update the code of Qiana, or even if you want to use it as a Python package rather than a standalone utility, read the file ```docs/HACK.md```.

# Citing Qiana
If you use Qiana in scientific work, please cite [our article](https://suchanek.name/work/publications/kr-2024.pdf)

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
