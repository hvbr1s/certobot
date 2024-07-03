# Ghost Variables

Ghost variables must be declared at the top level of a specification file. A ghost variable declaration includes the keyword ghost followed by the type and name of the ghost variable.

The type of a ghost variable may be either a CVL type or a mapping type. Mapping types are similar to solidity mapping types. They must have CVL types as keys, but may contain either CVL types or mapping types as values.

For example, the following are valid ghost declarations:

cvl ghost uint x;
ghost mapping(address => mapint) balances;
ghost mapping(uint => mapping(uint => mapint)) delegations;

while the following are invalid:

cvl ghost (uint, uint) x;
ghost mapping(mapping(uint => uint) => address) y;

# Simple Ghost Variable Example

This example uses an init_state axiom

# Ghost Mapping Example
---
# Ghost Functions

CVL also has support for "ghost functions". These serve a different purpose from ghost variables, although they can be used in similar ways.

Ghost functions must be declared at the top level of a specification file. A ghost function declaration includes the keyword ghost followed by the name and signature of the ghost function. Ghost functions should be used either:

- when there are no updates to the ghost as the deterministic behavior and axioms are the only properties of the ghost
- when updating the ghost - more than one entry is updated and then the havoc assuming statement is used.

Restrictions on ghost definitions:

A user-defined type, such as struct, array or interface is not allowed as the key or the output type of a ghost mapping.

Using ghost variables:

While verifying a rule or invariant, the Prover considers every possible initial value of a ghost variable (subject to its ghost-axioms, see below).

Within CVL, you can read or write ghosts using the normal variable syntax. For example:

cvl ghost mapping(address => mathint) balances;

function example(address user) { balances[user] = x; }

The most common reason to use a ghost is to communicate information from a hook back to the rule that triggered it. For example, the following CVL checks that a call to the contract method do_update(user) changes the contract variable userInfo[user] and does not change userInfo[other] for any other user:

cvl ghost mapping(address => bool) updated;

hook Sstore userInfo[KEY address u] uint i { updated[u] = true; }

rule updatechangesuser(address user) { updated[user] = false;
do_update(user);
assert updated[user] == true, "do_update(user) should affect user";
}

rule updatechangesno_other(address user, address other) { require user != other; require updated[other] == false;
do_update(user);
assert updated[other] == false;
}

Here the updated ghost is used to communicate information from the userInfo hook back to the updated_changes_user and updated_changes_no_other rules.
---
# Ghost axioms

Ghost axioms are properties that the Prover assumes whenever it makes use of a ghost.

# Global axioms

Sometimes we might want to constrain the behavior of a ghost in some particular way. In CVL this is achieved by writing axioms. Axioms are simply CVL expressions that the tool will then assume are true about the ghost. For example:

cvl ghost bar(uint256) returns uint256 { axiom forall uint256 x. bar(x) > 10; }

In any rule that uses bar, no application of bar could ever evaluate to a number less than or equal to 10.

# Initial state axioms

When writing invariants, initial axioms are a way to express the “constructor state” of a ghost function. They are used only when checking the base step of invariants. Before checking the initial state of an invariant, the Certora Prover adds a require for each init_state axiom. init_state axioms are not used in rules or the preservation check for invariants.

cvl ghost mathint sumBalances{ // assuming value zero at the initial state before constructor
init_state axiom sumBalances == 0; }

Restrictions on ghost axioms

A ghost axiom cannot refer to Solidity or CVL functions or to other ghosts. It can refer to the ghost itself. Since the signature of a ghost contains just parameter types without names, it cannot refer to its parameters. forall can be used in order to refer the storage referred to by the parameters. Example.

# Ghosts vs. persistent ghosts

A persistent ghost is a ghost that will never be havoced. The value of a non-persistent ghost will be havoc'ed when the Prover havocs the storage, a persistent ghost however will keep its value when storage is havoced.

In most cases, non-persistent ghosts are the natural choice for a specification that requires extra tracking of information.

We present two examples where persistent ghosts are useful.

Persistent ghosts that survive havocs

In the first example, we want to track the occurrence of a potential reentrant call:

cvl persistent ghost bool reentrancyhappened { initstate axiom !reentrancy_happened; }

hook CALL(uint g, address addr, uint value, uint argsOffset, uint argsLength, uint retOffset, uint retLength) uint rc { if (addr == currentContract) { reentrancyhappened = reentrancyhappened || executingContract == currentContract; } }

invariant noreentrantcalls !reentrancy_happened;
---
To see why a persistent ghost must be used here for the variable reentrancy_happened, consider the following contract:

solidity contract NotReentrant { function transfer1Token(IERC20 a) external { require (address(a) !=
address(this)); a.transfer(msg.sender, 1); } }

If we do not apply any linking or dispatching for the call done on the target a, the call to transfer would havoc. During a
havoc operation, the Prover conservatively assumes that almost any possible behavior can occur. In particular, it must
assume that during the execution of the a.transfer call, non-persistent ghosts can be updated arbitrarily (e.g. by other
contracts), and thus (assuming reentrancy_happened were not marked as persistent), the Prover considers the case where
reentrancy_happened is set to true due to the havoc. Thus, when the CALL hook executes immediately after, it does so
where the reentrancy_happened value is already true, and thus the value after the hook will remain true.

In the lower-level view of the tool, the sequence of events is as follows: 1. A call to a.transfer which cannot be resolved
and results in a havoc operation. Non-persistent ghosts are havoced, in particular reentrancy_happened
if it were not marked as such. 2. A CALL hook executes, updating reentrancy_happened based on its havoced value,
meaning it can turn to true.

Therefore even if the addresses of a and NotReentrant are distinct, we could still falsely detect a reentrant call as
reentrancy_happened was set to true due to non-determinism. The call trace would show reentrancy_happened as being
determined to be true due to a havoc in the "Ghosts State" view under "Global State".

Persistent ghosts that survive reverts

In this example, we use persistent ghosts to determine if a revert happened with user-provided data or not. This can help
distinguishing between compiler-generated reverts and user-specified reverts (but only in Solidity versions prior to 0.8.x).
The idea is to set a ghost to true if a REVERT opcode is encountered with a positive buffer size. As in early Solidity versions
the panic errors would compile to reverts with empty buffers, as well as user-provided requires with no message specified.

```cvl persistent ghost bool sawuserdefinedrevertmsg;

hook REVERT(uint offset, uint size) { if (size > 0) { sawuserdefinedrevertmsg = true; } }

rule markmethodsthathaveuserdefinedreverts(method f, env e, calldataarg args) { require !sawuserdefinedrevertmsg;

f@withrevert(e, args);

satisfy saw_user_defined_revert_msg;

}

To see why a regular ghost cannot be used to implement this rule, let's consider the following trivial contract:

```solidity contract Reverting { function noUserDefinedRevertFlows(uint a, uint b) external { uint c = a/b; // will see a potential
division-by-zero revert uint[] memory arr = new uint; uint d = arr[a+b]; // will see a potential out-of-bounds access revert; }

function userDefinedRequireMsg(uint a) external {
require(a != 0, "a != 0");
}

function emptyRequire(uint a) external {
require(a != 0);
}

}

It is expected for the method userDefinedRequireMsg to satisfy the rule, and it should be the only method to satisfy it.
Assuming saw_user_defined_revert_msg was defined as a regular, non-persistent ghost, the rule would not be satisfied for
userDefinedRequireMsg: in case the input argument a is equal to 0, the contract reverts, and the value of
saw_user_defined_revert_msg is reset to its value before the call, which must be false (because the rule required it
before the call). In this case, after the call saw_user_defined_revert_msg cannot be set to true and thus the satisfy fails.
Applying the same reasoning, it is clear that the same behavior happens for reverting behaviors of
---
# Ghosts

Ghosts are a way of defining additional variables for use during verification. These variables are often used to communicate information between rules and hooks, as well as to define deterministic function summaries.

Ghosts can be seen as an extension to the state of the contracts under verification. In case a call reverts, the ghost values will revert to their pre-state. Additionally, if an unresolved call is handled by a havoc, the ghost values will also havoc. Ghosts are considered part of the state of the contracts, and when calls are invoked with storageVar statements, they are restored to their saved state. An exception to this rule is persistent ghosts, which are never havoced or reverted.

# Syntax

The syntax for ghost declarations is given by the following EBNF grammar:

ghost ::= "ghost" type id (";" | "{" axioms "}") | "ghost" id "(" cvl_types ")" "returns" type (";" | "{" axioms "}")

persistentghost ::= "persistent" "ghost" type id (";" | "{" axioms "}") | "persistent" "ghost" id "(" cvltypes ")" "returns" type (";" | "{" axioms "}")

type ::= basictype | "mapping" "(" cvltype "=>" type ")"

axiom ::= [ "init_state" ] "axiom" expression ";"

See the documentation for types and expressions for more details.

# Declaring ghost variables

Ghost variables must be declared at the top level of a specification file. A ghost variable declaration includes the keyword ghost followed by the type and name of the ghost variable.

The type of a ghost variable may be a CVL type or a mapping type. Mapping types are similar to Solidity mapping types, with CVL types as keys and either CVL types or mapping types as values.

Examples of valid ghost declarations:

cvl ghost uint x;
ghost mapping(address => mapint) balances;
ghost mapping(uint => mapping(uint => mapint)) delegations;

Examples of invalid ghost declarations:
---
cvl ghost (uint, uint) x; // tuples are not CVL types ghost mapping(mapping(uint =&gt; uint) =&gt; address) y; // mappings cannot be keys

simple ghost variable example

This example uses an init_state axiom

ghost mapping example

# Ghost Functions

CVL also has support for "ghost functions". These serve a different purpose from ghost variables, although they can be used in similar ways.

Ghost functions must be declared at the top level of a specification file. A ghost function declaration includes the keyword ghost followed by the name and signature of the ghost function. Ghost functions should be used either: - when there are no updates to the ghost as the deterministic behavior and axioms are the only properties of the ghost - when updating the ghost - more than one entry is updated and then the havoc assuming statement is used.

ghost function example

Restrictions on ghost definitions

A user-defined type, such as struct, array or interface is not allowed as the key or the output type of a ghost mapping. Using ghost variables

While verifying a rule or invariant, the Prover considers every possible initial value of a ghost variable (subject to its {ref}ghost-axioms, see below).

Within CVL, you can read or write ghosts using the normal variable syntax. For example:

cvl ghost mapping(address =&gt; mathint) balances;
function example(address user) { balances[user] = x; }

The most common reason to use a ghost is to communicate information from a hook back to the rule that triggered it. For example, the following CVL checks that a call to the contract method do_update(user) changes the contract variable userInfo[user] and does not change userInfo[other] for any other user:

cvl ghost mapping(address =&gt; bool) updated;
hook Sstore userInfo[KEY address u] uint i { updated[u] = true; }
rule updatechangesuser(address user) { updated[user] = false;
do_update(user);
assert updated[user] == true, "do_update(user) should affect user";
}
rule updatechangesno_other(address user, address other) { require user != other; require updated[other] == false;
do_update(user);
---
# assert updated[other] == false;

Here the updated ghost is used to communicate information from the userInfo hook back to the updated_changes_user and updated_changes_no_other rules.

# Ghost axioms

Ghost axioms are properties that the Prover assumes whenever it makes use of a ghost.

# Global axioms

Sometimes we might want to constrain the behavior of a ghost in some particular way. In CVL this is achieved by writing axioms. Axioms are simply CVL expressions that the tool will then assume are true about the ghost. For example:

cvl ghost bar(uint256) returns uint256 { axiom forall uint256 x. bar(x) &gt; 10; }

In any rule that uses bar, no application of bar could ever evaluate to a number less than or equal to 10.

# Initial state axioms

When writing invariants, initial axioms are a way to express the “constructor state” of a ghost function. They are used only when checking the base step of invariants. Before checking the initial state of an invariant, the Certora Prover adds a require for each init_state axiom. init_state axioms are not used in rules or the preservation check for invariants.

cvl ghost mathint sumBalances{ // assuming value zero at the initial state before constructor
init_state axiom sumBalances == 0; }

# Restrictions on ghost axioms

A ghost axiom cannot refer to Solidity or CVL functions or to other ghosts. It can refer to the ghost itself. Since the signature of a ghost contains just parameter types without names, it cannot refer to its parameters. forall can be used in order to refer the storage referred to by the parameters. Example.

# Persistent ghosts vs. persistent ghosts

A persistent ghost is a ghost that will never be havoc. The value of a non-persistent ghost will be havoc'ed when the Prover havocs the storage, a persistent ghost however will keep its value when storage is havoced.

In most cases, non-persistent ghosts are the natural choice for a specification that requires extra tracking of information.

We present two examples where persistent ghosts are useful.
---
In the first example, we want to track the occurrence of a potential reentrant call[^reentrancy]:

cvl persistent ghost bool reentrancyhappened
initstate axiom !reentrancy_happened;
hook CALL(uint g, address addr, uint value, uint argsOffset, uint argsLengp, uint retOffset, uint retLengp) uint rc { if (addr == currentContract) { reentrancyhappened = reentrancyhappened || executingContract == currentContract; } }
invariant noreentrantcalls !reentrancy_happened;

To see why a persistent ghost must be used here for the variable reentrancy_happened, consider the following contract:

solidity contract NotReentrant { function transfer1Token(IERC20 a) external { require (address(a) != address(this)); a.transfer(msg.sender, 1); } }

If we do not apply any linking or dispatching for the call done on the target a, the call to transfer would havoc. During a havoc operation, the Prover conservatively assumes that almost any possible behavior can occur. In particular, it must assume that during the execution of the a.transfer call, non-persistent ghosts can be updated arbitrarily (e.g. by other contracts), and thus (assuming reentrancy_happened were not marked as persistent), the Prover considers the case where reentrancy_happened is set to true due to the havoc. Thus, when the CALL hook executes immediately after, it does so where the reentrancy_happened value is already true, and thus the value after the hook will remain true.

In the lower-level view of the tool, the sequence of events is as follows: 1. A call to a.transfer which cannot be resolved and results in a havoc operation. Non-persistent ghosts are havoced, in particular reentrancy_happened if it were not marked as such. 2. A CALL hook executes, updating reentrancy_happened based on its havoced value, meaning it can turn to true.

Therefore even if the addresses of a and NotReentrant are distinct, we could still falsely detect a reentrant call as reentrancy_happened was set to true due to non-determinism. The call trace would show reentrancy_happened as being determined to be true due to a havoc in the "Ghosts State" view under "Global State".

Persistent ghosts that survive reverts

In this example, we use persistent ghosts to determine if a revert happened with user-provided data or not. This can help distinguishing between compiler-generated reverts and user-specified reverts (but only in Solidity versions prior to 0.8.x). The idea is to set a ghost to true if a REVERT opcode is encountered with a positive buffer size. As in early Solidity versions the panic errors would compile to reverts with empty buffers, as well as user-provided requires with no message specified.

cvl persistent ghost bool sawuserdefinedrevertmsg;
hook REVERT(uint offset, uint size) { if (size > 0) { sawuserdefinedrevertmsg = true; } }
rule markmepodspapaveuserdefinedreverts(mepod f, env e, calldataarg args) { require !sawuserdefinedrevertmsg;
f@wiprevert(e, args);
satisfy saw_user_defined_revert_msg;

To see why a regular ghost cannot be used to implement this rule, let's consider the following trivial contract:

solidity contract Reverting { function noUserDefinedRevertFlows(uint a, uint b) external { uint c = a/b; // will see a potential division-by-zero revert uint[] memory arr = new uint; uint d = arr[a+b]; // will see a potential out-of-bounds access revert; }

function userDefinedRequireMsg(uint a) external { require(a != 0, "a != 0"); }

function emptyRequire(uint a) external { require(a != 0); }
---
It is expected for the method userDefinedRequireMsg to satisfy the rule, and it should be the only method to satisfy it. Assuming saw_user_defined_revert_msg was defined as a regular, non-persistent ghost, the rule would not be satisfied for userDefinedRequireMsg: in case the input argument a is equal to 0, the contract reverts, and the value of saw_user_defined_revert_msg is reset to its value before the call, which must be false (because the rule required it before the call). In this case, after the call saw_user_defined_revert_msg cannot be set to true and thus the satisfy fails. Applying the same reasoning, it is clear that the same behavior happens for reverting behaviors of noUserDefinedRevertFlows and emptyRequire, which do not have user-defined revert messages. This means that if saw_user_defined_revert_msg is not marked persistent, the rule cannot distinguishing between methods that may revert with user-defined messages and methods that may not.

Source: https://github.com/Certora/Documentation/cvl/ghosts.md
