Uninterpreted Sorts

CVL specifications support both Solidity primitives (uint256, address, etc.) and custom types (e.g., mathint). Solidity types are interpreted, meaning they have specific semantics, such as arithmetic or comparison operations. However, in some cases, it is beneficial to use uninterpreted sorts, which do not carry the semantics associated with interpretation.

Syntax for Uninterpreted Sorts

To declare an uninterpreted sort in CVL, use the following syntax:

cvl sort MyUninterpSort; sort Foo;

These uninterpreted sorts can be utilized in various ways within a CVL specification:

- Declare Variables: cvl Foo x;
- Test Equality: cvl Foo x; Foo y; assert x == y;
- Use in Signatures: cvl ghost myGhost(uint256, Foo) returns Foo;

Example Usage

Consider the following example:

cvl sort Foo;
ghost bar(Foo, Foo) returns Foo;
rule myRule { Foo x; Foo y; Foo z = bar(x, y); assert x == y &amp;&amp; y == z; }

This example demonstrates the use of an uninterpreted sort Foo. The bar ghost function takes two arguments of type Foo and returns a value of the same type. The myRule rule declares variables x, y, and z, and asserts that they are all equal.

Using Uninterpreted Sorts with Ghosts

Uninterpreted sorts can also be employed in ghosts, as shown in the following example:

cvl ghost mapping(uint256 =&gt; Node) toNode; ghost mapping(Node =&gt; mapping(Node =&gt; bool)) reach { // Axioms for reachability relation axiom forall Node X. reach[X][X]; axiom forall Node X. forall Node Y. reach[X][Y] &amp;&amp; reach[Y][X] =&gt; X == Y; axiom forall Node X. forall Node Y. forall Node Z. reach[X][Y] &amp;&amp; reach[Y][Z] =&gt; reach[X][Z]; axiom forall Node X. forall Node Y. forall Node Z. reach[X][Y] &amp;&amp; reach[X][Z] =&gt; (reach[Y][Z] || reach[Z][Y]); }
definition isSucc(Node a, Node b) returns bool = // Definition for successor relationship reach[a][b] &amp;&amp; a != b &amp;&amp; (forall Node X. reach[a][X] &amp;&amp; reach[X][b] =&gt; (a == X || b == X));
rule checkGetSucc { uint256 key; uint256 afterKey = getSucc(key); assert reach[toNode[key]][toNode[afterKey]]; }

This example demonstrates the use of uninterpreted sorts (Node) in ghost mappings and functions, emphasizing their application in specifying relationships and properties without being bound by specific interpretations.

In summary, uninterpreted sorts in CVL provide a versatile tool for declaring abstract types and relationships, allowing for greater expressiveness in specification design.
---
CVL specifications support both Solidity primitives (uint256, address, etc.) and custom types (e.g., mathint). Solidity types are interpreted, meaning they have specific semantics, such as arithmetic or comparison operations. However, in some cases, it is beneficial to use uninterpreted sorts, which do not carry the semantics associated with interpretation.

Syntax for Uninterpreted Sorts

To declare an uninterpreted sort in CVL, use the following syntax:

cvl sort MyUninterpSort; sort Foo;

These uninterpreted sorts can be utilized in various ways within a CVL specification:

1. Declare Variables: cvl Foo x;
2. Test Equality: cvl Foo x; Foo y; assert x == y;
3. Use in Signatures: cvl ghost myGhost(uint256, Foo) returns Foo;

Example Usage

Consider the following example:

cvl sort Foo;
ghost bar(Foo, Foo) returns Foo;
rule myRule { Foo x; Foo y; Foo z = bar(x, y); assert x == y &amp;&amp; y == z; }

This example demonstrates the use of an uninterpreted sort Foo. The bar ghost function takes two arguments of type Foo and returns a value of the same type. The myRule rule declares variables x, y, and z, and asserts that they are all equal.

Using Uninterpreted Sorts with Ghosts

Uninterpreted sorts can also be employed in ghosts, as shown in the following example:

cvl ghost mapping(uint256 =&gt; Node) toNode; ghost mapping(Node =&gt; mapping(Node =&gt; bool)) reach { // Axioms for reachability relation axiom forall Node X. reach[X][X]; axiom forall Node X. forall Node Y. reach[X][Y] &amp;&amp; reach[Y][X] =&gt; X == Y; axiom forall Node X. forall Node Y. forall Node Z. reach[X][Y] &amp;&amp; reach[Y][Z] =&gt; reach[X][Z]; axiom forall Node X. forall Node Y. forall Node Z. reach[X][Y] &amp;&amp; reach[X][Z] =&gt; (reach[Y][Z] || reach[Z][Y]); }
definition isSucc(Node a, Node b) returns bool = // Definition for successor relationship reach[a][b] &amp;&amp; a != b &amp;&amp; (forall Node X. reach[a][X] &amp;&amp; reach[X][b] =&gt; (a == X || b == X));
rule checkGetSucc { uint256 key; uint256 afterKey = getSucc(key); assert reach[toNode[key]][toNode[afterKey]]; }

This example demonstrates the use of uninterpreted sorts (Node) in ghost mappings and functions, emphasizing their application in specifying relationships and properties without being bound by specific interpretations.

In summary, uninterpreted sorts in CVL provide a versatile tool for declaring abstract types and relationships, allowing for greater expressiveness in specification design.