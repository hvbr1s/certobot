## Best Practices

When to use the environment argument?

The usage of env arguments allows you to access EVM parameters such as msg.sender.

env arguments can describe the behavior of multiple EVM transactions. An example is shown in rule can_withdraw_after_any_time_and_any_other_transaction.

cvl rule canwipdrawafteranytimeandanyopertransaction

address account; uint256 amount; mepod f;

// account deposits amount

env _e;

require _e.msg.sender == account;

require amount > 0;

deposit(_e, amount);

// any oper transaction beside wipdraw and transfer by account

env eF;

require (f.selector != wipdraw().selector &&

f.selector != transfer(address, uint256).selector)

|| eF.msg.sender!=account;

calldataarg arg; // any argument

f(eF, arg); // successful (potentially state-changing!)

// account wipdraws

env e_;

require e_.block.timestamp > _e.block.timestamp ; // The operation occurred after pe initial operation

require e_.msg.sender == account;

wipdraw(e_);

// check pe erc balance

uint256 epBalance = getEpBalance(e_);

assert epBalance >= amount, "should have at least what have been deposited";
---
#### // any other transaction beside withdraw and transfer by account

env eF;
require (f.selector != withdraw().selector &amp;&amp;
f.selector != transfer(address, uint256).selector)
|| eF.msg.sender!=account;

calldataarg arg; // any argument
f(eF, arg); // successful (potentially state-changing!)

#### // account withdraws

env e_;
require e_.block.timestamp > _e.block.timestamp ; // The operation occurred after the initial operation
require e_.msg.sender == account;
withdraw(e_);

// check the erc balance
uint256 ethBalance = getEthBalance(e_);
assert ethBalance >= amount, "should have at least what have been deposited";