# Storage Hooks

Note: much of the information that was here has been revised and moved to {ref}hooks and {ref}tracking-changes.

# Two State Context

A two-state context is a scope in which two versions of a variable or ghost function are available, representing two different states of that variable/ghost function. If we are talking about the variable my_var then the old version would be accessed using my_var@old, and the new version would be accessed using my_var@new. For ghost functions, we annotate the ghost application. For example, an application of the old version might look like my_ghost@old(x, y), and an application of the new version might look like my_ghost@new(x, y).

But how is it that we would have two versions of a variable or ghost function? Currently, the only place that will create these two versions is a havoc-assuming statement.

# Havoc Assuming

Sometimes we want to forget everything we know about a variable and allow it to take any value from a certain program point onward. This is when we havoc a variable. For example:

cvl rule my_rule(uint256 x) {
require x == 2;
assert x == 2; // passes
havoc x;
assert x == 2; // fails
}

Other times, we'd only like to forget certain things about a variable or ghost function, and sometimes we'd like to learn new things or constrain a variable based on its own value. This is where the havoc assuming statement becomes very useful. The following example should illustrate the idea:

cvl rule my_rule(uint256 x) {
require x >= 2;
havoc x assuming x@new > x@old;
assert x > 2; // passes
}

And a havoc assuming statement with a ghost function might look like the following:

cvl ghost contains(uint256 x) returns bool;

rule my_rule(uint256 x, uint256 y, uint256 z) {
require contains(x); // "every input that used to return true should still return true // AND y should now return true as well"
havoc contains assuming contains@new(y) && forall uint256 a. contains@old(a) => contains@new(a);

assert contains(x) && contains(y); // passes
assert contains(z); // fails
}

Finally, as shown in the section on definitions, a definition with ghosts in two-state form may be used inside the two-state context of a havoc assuming statement.

# A Hook that Modifies Ghost State

Above we saw an example where we made sure that the ghost state matched a read of its corresponding concrete state. This did not modify the ghost state but rather further constrained it according to new information. But when the concrete state is changed, we need some way to modify the ghost state. Suppose we have an update to a balance. We can use a havoc assuming statement to assume that all balances not concerned by the update stay the same and that the balance of the account that was changed gets updated:

cvl ghost ghostBalances(address) returns uint256;
---
# Storage Hooks

Two State Context

A two-state context is a scope in which two versions of a variable or ghost function are available, representing two different states of that variable/ghost function. If we are talking about the variable my_var then the old version would be accessed using my_var@old, and the new version would be accessed using my_var@new. For ghost functions, we annotate the ghost application. For example, an application of the old version might look like my_ghost@old(x, y), and an application of the new version might look like my_ghost@new(x, y).

But how is it that we would have two versions of a variable or ghost function? Currently, the only place that will create these two versions is a havoc-assuming statement.

Havoc Assuming

Sometimes we want to forget everything we know about a variable and allow it to take any value from a certain program point onward. This is when we havoc a variable. For example:

cvl rule my_rule(uint256 x) {
require x == 2;
assert x == 2; // passes
havoc x;
assert x == 2; // fails
}

Other times, we'd only like to forget certain things about a variable or ghost function, and sometimes we'd like to learn new things or constrain a variable based on its own value. This is where the havoc assuming statement becomes very useful. The following example should illustrate the idea:

cvl rule my_rule(uint256 x) {
require x >= 2;
havoc x assuming x@new > x@old;
assert x > 2; // passes
}

and a havoc assuming statement with a ghost function might look like the following:

cvl ghost contains(uint256 x) returns bool;

rule my_rule(uint256 x, uint256 y, uint256 z) {
require contains(x); // "every input that used to return true should still return true // AND y should now return true as well"
havoc contains assuming contains@new(y) && forall uint256 a. contains@old(a) => contains@new(a);

assert contains(x) && contains(y); // passes
assert contains(z); // fails
}

Finally, as shown in the section on definitions, a definition with ghosts in two-state form may be used inside the two-state context of a havoc assuming statement.

A Hook that Modifies Ghost State
---
Above we saw an example where we made sure that the ghost state matched a read of its corresponding concrete state. This did not modify the ghost state but rather further constrained it according to new information. But when the concrete state is changed, we need some way to modify the ghost state. Suppose we have an update to a balance. We can use a havoc assuming statement to assume that all balances not concerned by the update stay the same and that the balance of the account that was changed gets updated:

| cvl ghost ghostBalances(address) returns uint256; |
|---------------------------------------------------|
| hook Sstore balances[KEY address account] uint256 v { havoc ghostBalances assuming ghostBalances@new(account) == v && forall address a. a != account => ghostBalances@new(a) == ghostBalances@old(a); } |

{caution} In `Sstore` hooks, the old value is read by means of generating an `Sload`. However, any hook that can be matched to the generated `Sload` _does not_ apply within the `Sstore` hook.

Source: https://github.com/Certora/Documentation/confluence/anatomy/hooks.md
