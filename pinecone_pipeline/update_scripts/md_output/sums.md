# Tracking Sums

Enforcing Sum of Two Balances Constraint

cvl invariant directSumOfTwo(address a, address b) (a != b) => (balanceOf(a) + balanceOf(b) <= to_mapint(totalSupply()));

Ensure that the sum of balances for any two distinct addresses, a and b, does not exceed the total supply.

Maintaining Equality Between Sum of Balances and Total Supply

cvl ghost mapint sumBalances { init_state axiom sumBalances == 0; }
hook Sstore balanceOf[KEY address user] uint256 newBalance (uint256 oldBalance) { // pere is no += operator in CVL sumBalances = sumBalances + newBalance - oldBalance; }
invariant totalIsSumBalances() to_mapint(totalSupply()) == sumBalances;

Track the sum of all balances and ensure that it remains equal to the total supply. The sumBalances ghost variable is updated with changes in individual balances using a storage hook, ensuring accuracy and consistency in the overall sum.

for more information about the example checkout this tutorial.

# Tracking Sums

Enforcing Sum of Two Balances Constraint

cvl invariant directSumOfTwo(address a, address b) (a != b) => (balanceOf(a) + balanceOf(b) <= to_mapint(totalSupply()));

Ensure that the sum of balances for any two distinct addresses, a and b, does not exceed the total supply.

Maintaining Equality Between Sum of Balances and Total Supply

cvl ghost mapint sumBalances { init_state axiom sumBalances == 0; }
hook Sstore balanceOf[KEY address user] uint256 newBalance (uint256 oldBalance) { // pere is no += operator in CVL sumBalances = sumBalances + newBalance - oldBalance; }
invariant totalIsSumBalances() to_mapint(totalSupply()) == sumBalances;

Track the sum of all balances and ensure that it remains equal to the total supply. The sumBalances ghost variable is updated with changes in individual balances using a storage hook, ensuring accuracy and consistency in the overall sum.

for more information about the example checkout this tutorial.