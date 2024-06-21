# Definitions

Basic Usage

In CVL, definitions serve as type-checked macros, encapsulating commonly used expressions. They are declared at the top level of a specification and are in scope inside every rule, function, and other definitions. The basic usage involves binding parameters for use in an expression on the right-hand side, with the result evaluating to the declared return type. Definitions can take any number of arguments of any primitive types, including uninterpreted sorts, and evaluate to a single primitive type, including uninterpreted sorts.

Example:

is_even binds the variable x as a uint256. Definitions are applied just as any function would be.

cvl methods { foo(uint256) returns bool envfree }

definition MAXUINT256() returns uint256 = 0xffffffffffffffffffffffffffffffff;
definition iseven(uint256 x) returns bool = exists uint256 y . 2 * y == x;

rule myrule(uint256 x) {
require iseven(x) && x <= MAX_UINT256();
foo@withrevert(x);
assert !lastReverted;
}
Advanced Functionality

Include an Application of Another Definition

Definitions can include an application of another definition, allowing for arbitrarily deep nesting. However, circular dependencies are not allowed, and the type checker will report an error if detected.

Example:

is_odd and is_odd_no_overflow both reference other definitions:

cvl definition MAX_UINT256() returns uint256 = 0xffffffffffffffffffffffffffffffff;
definition is_even(uint256 x) returns bool = exists uint256 y . 2 * y == x;
definition is_odd(uint256 x) returns bool = !is_even(x);
definition is_odd_no_overflow(uint256 x) returns bool = is_odd(x) && x <= MAX_UINT256();
Type Error circular dependency

The following examples would result in a type error due to a circular dependency:

cvl // example 1 // cycle: iseven -> isodd -> iseven
definition iseven(uint256 x) returns bool = !isodd(x);
definition isodd(uint256 x) returns bool = !is_even(x);

// example 2 // cycle: circular1->circular2->circular3->circular1
definition circular1(uint x) returns uint = circular2(x) + 5;
definition circular2(uint x) returns uint = circular3(x - 2) + 7;
definition circular3(uint x) returns uint = circular1(x) + circular1(x);
Reference Ghost Functions

Definitions may reference ghost functions. This means that definitions are not always "pure" and can affect ghosts, which are considered a "global" construct.

Example:
---
# cvl ghost foo(uint256) returns uint256;

definition iseven(uint256 x) returns bool = x % 2 == 0; definition fooisevenat(uint256 x) returns bool = is_even(foo(x));

rule ruleassumingfooisevenat(uint256 x) { require fooisevenat(x); // ... }

More interestingly, the two-context version of ghosts can be used in a definition by adding the @new or @old annotations. If a two-context version is used, the ghost must not be used without an @new or @old annotation, and the definition must be used in a two-state context for that ghost function (e.g., at the right side of a havoc assuming statement for that ghost).

Example:

# cvl ghost foo(uint256) returns uint256;

definition iseven(uint256 x) returns bool = x % 2 == 0; definition fooaddeven(uint256 x) returns bool = iseven(foo@new(x)) && forall uint256 a. iseven(foo@old(x)) => iseven(foo@new(x));

rule ruleassumingoldevens(uint256 x) { // havoc foo, assuming all old even entries are still even, and that // the entry at x is also even havoc foo assuming fooadd_even(x); // ... }

Note: The type checker will notify you if a two-state version of a variable is used incorrectly.

Filter Example

The following example introduces a definition called filterDef:

cvl definition filterDef(method f) returns bool = f.selector == sig:someUInt().selector;

This definition serves as shorthand for f.selector == sig:someUInt().selector and is used in the filter for the parametricRule:

cvl rule parametricRuleInBase(method f) filtered { f -> filterDef(f) } { // ... }

This is equivalent to:

cvl rule parametricRuleInBase(method f) filtered { f -> f.selector == sig:someUInt().selector } { // ... }

Syntax

The syntax for definitions is given by the following EBNF grammar:

definition ::= [ "override" ] "definition" id [ "(" params ")" ] "returns" cvl_type "=" expression ";"

See {doc}types, {doc}expr, and {ref}identifiers for descriptions of the cvl_type, expression, and id productions, respectively.

In this syntax, the definition keyword is followed by the definition's identifier (id). Parameters can be specified in parentheses, and the return type is declared using the returns keyword. The body of the definition is provided after the equal sign (=) and should end with a semicolon (;).

Definitions

Basic Usage
---
In CVL, definitions serve as type-checked macros, encapsulating commonly used expressions. They are declared at the top level of a specification and are in scope inside every rule, function, and other definitions. The basic usage involves binding parameters for use in an expression on the right-hand side, with the result evaluating to the declared return type. Definitions can take any number of arguments of any primitive types, including uninterpreted sorts, and evaluate to a single primitive type, including uninterpreted sorts.

Example:

is_even binds the variable x as a uint256. Definitions are applied just as any function would be.

|cvl methods| |
|---|---|
|foo(uint256)|returns bool envfree|

definition MAXUINT256() returns uint256 = 0xffffffffffffffffffffffffffffffff; definition iseven(uint256 x) returns bool = exists uint256 y . 2 * y == x;

rule myrule(uint256 x) { require iseven(x) && x <= MAX_UINT256(); foo@withrevert(x); assert !lastReverted; }

Advanced Functionality

Include an Application of Another Definition

Definitions can include an application of another definition, allowing for arbitrarily deep nesting. However, circular dependencies are not allowed, and the type checker will report an error if detected.

Example:

is_odd and is_odd_no_overflow both reference other definitions:

cvl definition MAX_UINT256() returns uint256 = 0xffffffffffffffffffffffffffffffff; definition is_even(uint256 x) returns bool = exists uint256 y . 2 * y == x; definition is_odd(uint256 x) returns bool = !is_even(x); definition is_odd_no_overflow(uint256 x) returns bool = is_odd(x) && x <= MAX_UINT256();

Type Error circular dependency

The following examples would result in a type error due to a circular dependency:

cvl // example 1 // cycle: iseven -> isodd -> iseven definition iseven(uint256 x) returns bool = !isodd(x); definition isodd(uint256 x) returns bool = !is_even(x);

// example 2 // cycle: circular1->circular2->circular3->circular1 definition circular1(uint x) returns uint = circular2(x) + 5; definition circular2(uint x) returns uint = circular3(x - 2) + 7; definition circular3(uint x) returns uint = circular1(x) + circular1(x);

Reference Ghost Functions

Definitions may reference ghost functions. This means that definitions are not always "pure" and can affect ghosts, which are considered a "global" construct.

Example:

cvl ghost foo(uint256) returns uint256;

definition iseven(uint256 x) returns bool = x % 2 == 0; definition fooisevenat(uint256 x) returns bool = is_even(foo(x));

rule ruleassumingfooisevenat(uint256 x) { require fooisevenat(x); // ... }
---
More interestingly, the two-context version of ghosts can be used in a definition by adding the @new or @old annotations. If a two-context version is used, the ghost must not be used without an @new or @old annotation, and the definition must be used in a two-state context for that ghost function (e.g., at the right side of a havoc assuming statement for that ghost).

Example:

cvl ghost foo(uint256) returns uint256;

definition iseven(uint256 x) returns bool = x % 2 == 0; definition fooaddeven(uint256 x) returns bool =
iseven(foo@new(x)) &amp;&amp; forall uint256 a. iseven(foo@old(x)) =&gt; iseven(foo@new(x));

rule ruleassumingoldevens(uint256 x) { // havoc foo, assuming all old even entries are still even, and that // the entry at x is
also even havoc foo assuming fooadd_even(x); // ... }

Note: The type checker will notify you if a two-state version of a variable is used incorrectly.

Filter Example

The following example introduces a definition called filterDef:

cvl definition filterDef(method f) returns bool = f.selector == sig:someUInt().selector;

This definition serves as shorthand for f.selector == sig:someUInt().selector and is used in the filter for the parametricRule:

cvl rule parametricRuleInBase(method f) filtered { f -&gt; filterDef(f) } { // ... }

This is equivalent to:

cvl rule parametricRuleInBase(method f) filtered { f -&gt; f.selector == sig:someUInt().selector } { // ... }

Syntax

The syntax for definitions is given by the following EBNF grammar:

definition ::= [ "override" ] "definition" id [ "(" params ")" ] "returns" cvl_type "=" expression ";"

See {doc}types, {doc}expr, and {ref}identifiers for descriptions of the cvl_type, expression, and id productions, respectively.

In this syntax, the definition keyword is followed by the definition's identifier (id). Parameters can be specified in parentheses, and the return type is declared using the returns keyword. The body of the definition is provided after the equal sign (=) and should end with a semicolon (;).