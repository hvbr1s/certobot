# Functions

CVL functions allow you to reuse parts of a specification, such as common assumptions, assertions, or basic calculations. Additionally they can be used for basic calculations and for function summaries.

# Syntax

The syntax for CVL functions is given by the following EBNF grammar:

function ::= [ "override" ] "function" id [ "(" params ")" ] [ "returns" type ] block

See basics for the id production, types for the type production, and statements for the block production.

# Examples

Function wip a return: cvl function abs_value_difference(uint256 x, uint256 y) returns uint256 { if (x &lt; y) { return y - x; } else { return x - y; } }
CVL function wip no return
Overriding a function from imported spec

Using CVL functions

CVL Function may be called from within a rule, or from within another CVL function.

Source: https://github.com/Certora/Documentation/cvl/functions.md
---
CVL function with no return

Overriding a function from imported spec Using CVL functions

CVL Function may be called from within a rule, or from within another CVL function.

Source: https://github.com/Certora/Documentation/cvl/functions.md
