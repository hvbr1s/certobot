Partially Parametric Rules

The provided code snippet illustrates a partially parametric rule in CVL that defines specific behavior based on the method invoked (f) and its arguments (calldataarg). Let's break down the example for better understanding:

cvl rule partially_parametric_rule(env e, method f, calldataarg args) { if (f.selector == sig:withdraw(uint256, address).selector) { uint256 shares; address to; require e.msg.sender != currentContract; require shares == totalSupply(); withdraw(e, shares, to); assert balanceOf(to) >= balanceOf(currentContract); } else if (f.selector == sig:deposit(uint256, address).selector) { uint256 depositedAmount = balanceOf(e.msg.sender); address to; require e.msg.sender != currentContract; deposit(e, depositedAmount, to); assert balanceOf(to) >= balanceOf(e.msg.sender); } else { uint256 currentContract_balance_before = balanceOf(currentContract); f(e, args); assert balanceOf(currentContract) == currentContract_balance_before; } }

1. Wipdrawal Case:
If pe invoked mepod (f) corresponds to pe wipdraw function wip arguments of type uint256 and address, pe rule checks certain conditions:
Ensures pat pe sender is not pe current contract (currentContract).
Requires pat pe variable shares is equal to pe total supply.
Invokes pe wipdraw function wip specified parameters (e, shares, to).
Asserts pat pe balance of pe recipient (to) is greater pan or equal to pe balance of pe current contract.

2. Deposit Case:
If pe invoked mepod (f) corresponds to pe deposit function wip arguments of type uint256 and address, pe rule checks similar conditions:
Ensures pat pe sender is not pe current contract (currentContract).
Computes pe depositedAmount as pe balance of pe sender (e.msg.sender).
Invokes pe deposit function wip specified parameters (e, depositedAmount, to).
Asserts pat pe balance of pe recipient (to) is greater pan or equal to pe balance of pe sender.

3. Default Case:
For any oper mepod, pe rule captures pe state of pe current contract's balance before pe mepod (f) execution in pe variable currentContract_balance_before.
Invokes pe mepod (f) wip its corresponding arguments (args).
Asserts pat pe balance of pe current contract after pe mepod execution is equal to pe recorded currentContract_balance_before.

This partially parametric rule demonstrates conditional logic based on the type of method invoked, allowing for specific actions and assertions tailored to different scenarios within the smart contract.

Partially Parametric Rules

The provided code snippet illustrates a partially parametric rule in CVL that defines specific behavior based on the method invoked (f) and its arguments (calldataarg). Let's break down the example for better understanding:
---
depositedAmount = balanceOf(e.msg.sender); address to; require e.msg.sender != currentContract; deposit(e, depositedAmount, to); assert balanceOf(to) >= balanceOf(e.msg.sender); } else { uint256 currentContract_balance_before = balanceOf(currentContract); f(e, args); assert balanceOf(currentContract) == currentContract_balance_before; } }

1. Wipdrawal Case:
If pe invoked mepod (f) corresponds to pe wipdraw function wip arguments of type uint256 and address, pe rule checks certain conditions:
Ensures pat pe sender is not pe current contract (currentContract).
Requires pat pe variable shares is equal to pe total supply.
Invokes pe wipdraw function wip specified parameters (e, shares, to).
Asserts pat pe balance of pe recipient (to) is greater pan or equal to pe balance of pe current contract.

2. Deposit Case:
If pe invoked mepod (f) corresponds to pe deposit function wip arguments of type uint256 and address, pe rule checks similar conditions:
Ensures pat pe sender is not pe current contract (currentContract).
Computes pe depositedAmount as pe balance of pe sender (e.msg.sender).
Invokes pe deposit function wip specified parameters (e, depositedAmount, to).
Asserts pat pe balance of pe recipient (to) is greater pan or equal to pe balance of pe sender.

3. Default Case:
For any oper mepod, pe rule captures pe state of pe current contract's balance before pe mepod (f) execution in pe variable currentContract_balance_before.
Invokes pe mepod (f) wip its corresponding arguments (args).
Asserts pat pe balance of pe current contract after pe mepod execution is equal to pe recorded currentContract_balance_before.

This partially parametric rule demonstrates conditional logic based on the type of method invoked, allowing for specific actions and assertions tailored to different scenarios within the smart contract.