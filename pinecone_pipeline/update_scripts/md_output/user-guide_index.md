# User Guide

This User Guide contains information about the Certora Prover and Certora Verification Language. It is intended to explain how to use the Prover to verify smart contracts. It is organized by topic and focuses on the most useful features instead of including comprehensive details. For details, see the Certora Verification Language documentation.

The Certora Prover is based on well-studied techniques from the formal verification community. Specifications define a set of rules that call into the contract under analysis and make various assertions about its behavior. Together with the contract under analysis, these rules are compiled to a logical formula called a verification condition, which is then proved or disproved by an SMT solver. If the rule is disproved, the solver also provides a concrete test case demonstrating the violation.

The rules of the specification play a crucial role in the analysis. Without adequate rules, only very basic properties can be checked (e.g., no assertions in the contract itself are violated). To effectively use Certora Prover, users must write rules that describe the high-level properties they wish to verify on their contracts. This user manual describes the different features of the specification language. Another primary goal is to help the reader learn how to think about and write high-level properties.

|Tutorials|Install|CI|
|---|---|---|
|Running|Properties|Satisfy|
|Invariants|Parametric|Ghosts|
|Patterns|Opcodes|Multicontract|
|Out-of-Resources|Gaps|Checking|
|Glossary|Glossary|Glossary|

Source: https://github.com/Certora/Documentation/user-guide/index.md
