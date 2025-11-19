fof(ax1, axiom, love(romeo,juliet)).
fof(ax2, axiom, drink(juliet,potion)).
fof(ax3, axiom, drink(juliet,potion) => ![C] : ist(C, q_dead(q_juliet))).
fof(ax4, axiom, ist(bel(romeo),q_dead(q_juliet)) => die(romeo)).
fof(concl, conjecture, die(romeo)).