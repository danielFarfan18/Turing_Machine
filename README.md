# Final_Proyect_Programming
 Marcos Daniel Rodríguez Farfán
## Turing Machine

A touring machine is defined by the 7 tuple (Q, Sigma, Gamma(Γ), q0, b, F, f).
Q: Finite and non-empty set of states of the control unit.
Sigma: Finite confnt of input symbols or alphabet of the input string.
Gamma(Γ): Finite set of ribbon symbols or string alphabet
q0: Initial state
b: blank space
F: Set of final acceptance states (non-empty and subset of Q)
f: transition function

This program will read a txt or def file to create a turing machine, use the following example of syntaxis to create your file.

@Q={q0,q1,q2,q3,q4}
@sigma={0,1}
@gamma={0,1,X,Y,b}
@q0=q0
@b=b
@F={q4}
@f={(q0 0)->(q1 X R),(q0 Y)->(q3 Y R),(q1 0)->(q1 0 R),(q1 1)->(q2 Y L),(q1 Y)->(q1 Y R),(q2 0)->(q2 0 L),(q2 X)->(q0 X R),(q2 Y)->(q2 Y L),(q3 Y)->(q3 Y R),(q3 b)->(q4 b R)}

# Test strings
@test={000111,0011,00001111,0101010,00000001111111,01,0100110}
@val={accepted,accepted,accepted,rejected,accepted,accepted,rejected}

Requirements:
libraries: re, prettytable, argparse
