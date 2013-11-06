
Decomposition of Quantum Circuits


##################################################################################################################
The project is aimed at decomposing any quantum circuit with complex unitary gates to a quantum circuit with single
qubit and CNOT gates.
###################################################################################################################

The code presently takes single qubit gate with arbitrary number of control bits. However, currently for testing purposes, the code is configured to work with 3-qubits only.The decomposed circuit output is presented in .qasm file.

USAGE: python QcircDecomp.py

The inputs have to be presented in "inputs.txt" in the format <qbits>,<matrix elements>,<cbits>

Program output for the sample input in "inputs.txt" can be found in "sample.qasm"
