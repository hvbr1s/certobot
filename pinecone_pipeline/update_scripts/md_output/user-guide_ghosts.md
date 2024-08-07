# Tracking changes with ghosts and hooks

Sometimes it is useful for a rule to observe changes to a particular part of storage, or otherwise track the behavior of a contract while it is executing. For example, while verifying an ERC20 contract, we may want to observe each update to any user balance so that we can keep our own running tally of the total supply.

Ghosts and hooks are designed for this purpose. Ghosts are additional variables that you can add to use during verification. They are similar to contract storage variables — they are rolled back when a contract function reverts or when the storage is reset.

Hooks are blocks of CVL code that get executed when a contract performs a certain instruction. For example, a store hook will be run whenever the contract updates a storage variable, while a call hook will be run whenever the contract makes an external call.

Together, hooks and ghosts let you keep track of what the contract does during execution.

TODO: This section is incomplete. For references, see: - The "Ghosts and hooks" lectures from the stanford and paris workshops - ghost-variables and hooks in the reference manual

% TODO: DOC-353 % % This guide works through some common examples of using ghosts and % hooks to monitor contracts. For full details see the reference manual on % hooks and ghosts. % % {contents} % % % ## Running example % % TODO: - ERC 20 - Offline signed transaction feature % % % ## Using store hooks to track sums % % TODO: The usual thing - `sumOfBalances` ghost - changes hook - `totalSupplyIsSumOfBalances` - `init_state` axiom % % Caveats - The Prover doesn't know `sumOfBalances` is the sum; can't relate sum of balances % to individual balances (sum of two balances example) % % % ## Using load hooks to TODO % % TODO: Use an invariant about the total supply maybe?

Source: https://github.com/Certora/Documentation/user-guide/ghosts.md
---
# Running example

TODO

- ERC 20
- Offline signed transaction feature

# Using store hooks to track sums

TODO

The usual thing

- sumOfBalances ghost
- changes hook
- totalSupplyIsSumOfBalances
- init_state axiom

Caveats

- The Prover doesn't know sumOfBalances is the sum; can't relate sum of balances to individual balances (sum of two balances example)

# Using load hooks to TODO

TODO

Use an invariant about the total supply maybe?

Source: https://github.com/Certora/Documentation/user-guide/ghosts.md
