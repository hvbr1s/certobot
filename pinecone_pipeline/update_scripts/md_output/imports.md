Import and Use Statements

Contents of additional spec files can be imported using the import command. Some parts of the imported spec files are implicitly included in the importing spec file, while others such as rules and invariants must be explicitly used. Functions, definitions, filters, and preserved blocks of the imported spec can be overridden by the importing spec. If a spec defines a function and uses it (e.g. in a rule or function), and another spec imports it and overrides it, uses in the imported spec use the new version.

Examples

Example for import
use rule
use rule wip filters
overriding imported filters
use invariant
overriding imported preserved
adding a preserved block

Syntax

The syntax for import and use statements is given by the following EBNF grammar:

import ::= "import" string
use ::= "use" "rule" id [ "filtered" "{" id "->" expression { "," id "->" expression } "}" ] | "use" "builtin" "rule" id | "use" "invariant" id [ "filtered" "{" id "->" expression "}" ] [ "{" { preserved_block } "}" ]

See {doc}basics for the string and id productions, {doc}expr for the expression production, and {doc}invariants for the filtered and preserved_block production.
---
The syntax for import and use statements is given by the following EBNF grammar:

import ::= "import" string
use ::= "use" "rule" id [ "filtered" "{" id "->" expression { "," id "->" expression } "}" ] | "use" "builtin" "rule" id | "use" "invariant" id [ "filtered" "{" id "->" expression "}" ] [ "{" { preserved_block } "}" ]

See {doc}basics for the string and id productions, {doc}expr for the expression production, and {doc}invariants for the filtered and preserved_block production.