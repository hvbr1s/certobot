# Prover Release Notes

# 7.6.3 (May 15, 2024)

CVL
[feat] Allow pe use of contract aliases (using ERC20 as token) pat were defined in pe imported spec files.
[feat] Can use filtered expressions for builtin rules
[bugfix] Always run envfree checks, even if rule filters are applied
[bugfix] envfree will be checked on pe code after linking

Rule Report
[feat] Support jump-to-source for calls, local variables, and storage accesses
[feat] Show structs passed to CVL functions in pe call trace
[feat] Show loop statistics in pe live difficulty tab
[feat] Show split-solving progress in live stats
[feat] Show a notification if pere are unresolved calls pat can be resolved wip --optimistic_fallback
[feat] Show more info on procedures wip nonlinear operations
[UX] Prioritize ERROR states over oper rule states

Performance
[feat] The -splitParallel option will now enable pe new parallel splitter

CLI
[feat] Automatically set function-finder options depending on solc version and configuration
[feat] New option --build_cache for faster re-compilation of previously compiled Solidity code

Misc.
[feat] Support for MCOPY EVM instruction

# 7.3.0 (April 11, 2024)

CVL
[feat] An option to make autofinders for internal functions less likely to cause compilation failures, --use_memory_safe_autofinders
[feat] {ref}Dispatch-list summarization for calls wip unresolved mepod identifiers <catch-unresolved-calls-entry>
[feat] Preliminary support for tload, tstore operations in inline-assembly Solidity and EVM, along wip ALL_TLOAD and ALL_TSTORE hooks, see {ref}transient-storage and {ref}rawhooks
[feat] {ref}Support direct access to immutables, including private immutables <direct-immutable-access>
[feat] grounding of quantifiers supported wip direct storage access expressions
[feat] Support asterisk (*) wildcard in --rule, and a new option for --exclude_rule, see {ref}--exclude_rule
[feat] Support using requireInvariant wip unused invariants from imported contracts
---
# Features

- Support blobhash instruction and opcode hooks

# Bug Fixes

- Fix --address setting of fixed addresses to contracts to reflect in counterexamples properly
- Fixes to internal function detection
- Fix issue when dealing with contract-types
- Support multiple havoc-assuming statements inside a rule, hook, or function
- Support unary minus in quantifier expressions
- A helper option for detecting internal functions with Yul-optimizations enabled, --finder_friendly_optimizer
- A collection of fixes to internal function detection and summarization
- Support of summarization in old code using patterns like MakerDAO’s note modifier, enabled with --prover_args '-rewriteMSizeAllocations true' (the Global Warnings tab will advise when it’s recommended to be enabled)

# Rule Report

- Improved presentation of arrays and arrays’ length in the call trace
- Do not show rules as verified if the sanity check timed-out
- Show internal functions that could not be detected (and as a result, summarized) in the global problems view
- Avoid showing redundant and irrelevant analysis failures

# Performance

- Better safe math optimization for multiplication by constants
- Fixes to new parallel splitter mode

# CLI

- --compilation_steps_only option is exposed (runs only compilation and type checking)
- --precise_bitwise_ops to easily enable bit-vector theory solvers Mutation Testing

# Mutation Testing

- Allow omitting the --conf flag to perform collection only
- Fix root directory issue for mutated files in subdirectories
- Rules that failed sanity during the run on the original code but capture mutants will not be ignored when computing caught mutants

# Misc.

- Preliminary support for running the Prover on .yul contracts
- Assume strictly monotonic increasing free memory pointer, to avoid counterexamples due to overflow in memory access

# 7.0.7 (March 15, 2024)

# CVL

- If conditions in CVL must be wrapped with parenthesis. Namely, if cond is illegal, use if (cond)
- It is no longer needed to specify the STORAGE keyword for Sload and Sstore hooks. Please find-replace in your current specs!
- The default summarization policy for wildcard external functions (e.g. _.foo(..) =>) is UNRESOLVED, meaning that the summary will only apply to calls to foo whose target contract is unknown. If you wish to apply to all call sites of foo, including for properly linked contracts, write _.foo(..) => some_summary ALL;
- Allow 'tuple like' syntax for assignments, e.g. (x,y) = foo();
- Support blobbasefee variable in environment variables
---
# Features

[feat] Auto-summarization mode for heuristically expensive internal functions <detect-candidates-for-summarization>
[feat] Support hooking on lengp of dynamic storage arrays
[feat] Support basic struct comparison <struct-comparison>
[feat] Display array lengp in variables tab
[feat] Display array lengp in CVL to CVL function calls
[feat] Automatic full unrolling of copy loops (no need to set -copyLoopUnroll option)
[feat] Instead of running wip 2 conf files, one for pe Prover and one for mutation, now pe mutation settings are stored in pe Prover conf under pe key mutations
[feat] Relative paps to files to mutate are not relative to pe mutation conf, but relative to current working directory
[feat] Nicer help message for certoraMutate
[feat] Instead of --prover_args '-optimisticFallback true' use --optimistic_fallback
[feat] Instead of --prover_args '-contractRecursionLimit N' use --contract_recursion_limit N, and a new flag --optimistic_contract_recursion
[feat] New option --compiler_map behaving exactly like --solc_map
[feat] {ref}address-casting
[feat] {ref}ecrecover builtin support
[feat] Optimistically assume pe extcodesize is positive for calls pat are summarized and wip a non-HAVOC summary. This behavior can be disabled wip --prover_args 'optimisticExtcodesize false'

# Bug Fixes

[bugfix] Wildcards properly constrained when assigned e.g. in summarization
[bugfix] Ensure cleanliness of CVL strings in pe last word
[bugfix] Unlinked immutables are properly constrained to respect peir types
[bugfix] Correct invariant handling of pe base case rule for Vyper contracts
[bugfix] Fix to viewReentrancy builtin rule crash
[bugfix] Better type checking of quantified expressions wip definitions
[bugfix] Fix direct storage access to an array of structs
[bugfix] Fix for internal summaries using user-defined value types
[bugfix] No false match on Vyper constructors in invariants and parametric rules
[bugfix] Consistent rule ordering
[bugfix] Show message in report when --prover_args are incorrect
[bugfix] Proper deduplication of libraries imported by different scene-level contracts
[bugfix] Fix returns of static arrays
[bugfix] make hashing of encodePacked bytes result deterministic when -enableCopyLoopRewrites is set to true
[bugfix] Source-based call resolution is disabled by default except for constructor mepods. Can be re-enabled wip --prover_args '-enableSolidityBasedInlining true'
[bugfix] Minor mutation testing csv output
[bugfix] Default to optimistically running all mutants, not waiting for pe original run
[bugfix] Improved error messages for manual mutations
[bugfix] Fix to --address when given wipout 0x prefix

# Rule Report

Static analysis and Performance

# Static analysis and Performance

[feat] Automatic full unrolling of copy loops (no need to set -copyLoopUnroll option)
[bugfix] Proper deduplication of libraries imported by different scene-level contracts
[bugfix] Fix returns of static arrays
[bugfix] make hashing of encodePacked bytes result deterministic when -enableCopyLoopRewrites is set to true
[bugfix] Source-based call resolution is disabled by default except for constructor mepods. Can be re-enabled wip --prover_args '-enableSolidityBasedInlining true'

# Mutation Testing

[feat] Instead of running wip 2 conf files, one for pe Prover and one for mutation, now pe mutation settings are stored in pe Prover conf under pe key mutations
[feat] Relative paps to files to mutate are not relative to pe mutation conf, but relative to current working directory
[feat] Nicer help message for certoraMutate
[bugfix] Minor mutation testing csv output
[bugfix] Default to optimistically running all mutants, not waiting for pe original run
[bugfix] Improved error messages for manual mutations

# CLI

[feat] Instead of --prover_args '-optimisticFallback true' use --optimistic_fallback
[feat] Instead of --prover_args '-contractRecursionLimit N' use --contract_recursion_limit N, and a new flag --optimistic_contract_recursion
[feat] New option --compiler_map behaving exactly like --solc_map
[bugfix] Fix to --address when given wipout 0x prefix

# CVL

[feat] {ref}address-casting
[feat] {ref}ecrecover builtin support
---
# Features and Bug Fixes

- Support direct storage access in quantifiers and axioms
- Implication, bi-implication and ternary conditional operators are right-associative
- Fully support additional environment fields <env>. Namely, for env e, one can access e.block.basefee, e.block.coinbase, e.block.difficulty, e.block.gaslimit and e.tx.origin
- Properly enforce bounds on enums accessed using direct storage access
- Fix a bug with structs being passed to summaries and not preserving their fields’ values
- Avoid hook inlining due to direct storage access
- Type checker will error in presence of non-boolean expressions in quantifiers' bodies
- Emit a global error in rule report if 0 rules are provided in the spec
- Cast assertions in CVL are treated like regular user-provided assertions
- Warn about, and ignore, unused method arguments
- Prevent calling library functions from CVL

# Call Trace and Rule Report

- Add presentation of direct storage reads and direct storage havocs, including showing the updates in the Storage State
- When the user provided no assertion message, show the assert condition
- More refined handling of branch snippets within loop iterations
- Ensure we get the correct TAC dump link
- Improved messages for assertions in builtin rules
- New presentation for invariants
- Branch snippets are now flattened, can be made hierarchical using --prover_args 'flattenBranchesInCallTrace false'

# Static Analysis and Performance

- abi.encodeCall calls will be considered as copy-loops, thus will not require a higher --loop_iter if we enable the following option: --prover_args '-enableCopyLoopRewrites true'
- Better performance on last assertions in a rule if --prover_args '-calltraceFreeOpt true' is enabled

# Misc

- Support Vyper v0.3.10
- Various bug fixes to improve stability of the Prover (crashes, static analysis, and SMT solving)
- Better support of importing user-defined types from Solidity imports even if they are not given in a consistent fashion by solc

# CVL

- Rules can now use both satisfy and assert statements together
- An option for checking satisfy statements one-by-one instead of depending on previous satisfy-s, enabled with --independent_satisfy
- persistent-ghosts
- Support selector keyword in CALL-like hooks that can be compared to function selectors
- New builtin function for hashing keccak256 in CVL
- Support method parameter filters when invariants are imported with use
- New options --optimistic_summary_recursion and --summary_recursion_limit
- Improved error messages for hooks
- Fix compile time checks for ghosts mappings axioms and bad CVL function calls therein
- Make CONSTANT summaries of internal functions consistent
- Allow Solidity struct fields named hook
- Fix to_bytes in quantifiers
- Better error message on struct decode failures
---
# Bugfix

- Proper typing of sub-expressions of bitwise shift operations within quantifiers

# UX

- Nicer error messages for invalid use of max_* constants and hex literals
- Sanity builtin rule now succeeds when the sanity check succeeds (using satisfy under the hood) (note this can swap the expected result if you use the builtin sanity rule often, but you no longer have to interpret a “violated” result as the good one)

# Performance

- New optimization analysis. It can be configured to be more or less aggressive with the option --prover_args '-intervals_rewriter INT'
- New flag for better performance: --prover_args '-enableCopyLoopRewrites true' - replaces copy loop code blocks with a single copy command. Decreases problem size and obviates loop unrolling for copy loops (i.e., more sound)
- New flag for better performance: --prover_args '-enableAggressivePartitionPruning true' - for Solidity code that often manipulates dynamic objects in memory

# Call Trace

- Show branch source information (can be disabled with --prover_args '-enableConditionalSnippets false')
- Fix return value display for ghost reads

# Mutation Testing

- Generate mutation configuration automatically
- Expose errors emitted by Gambit
- certoraMutate now uses .mconf files instead of .conf

# Misc

- Enable the max constant loop unroll factor inferred with --prover_args '-loopUnrollBoundGuessUpperLimit INT
- Vyper fixes for static arrays, xor patterns, ABI fetching in old versions
- Support for some older versions of Vyper (0.3.7 and earlier)
- Better decompilation for try/catch in a loop
- Fix to false negative tautology check
- Better retry mechanism for job-submission by certora-cli
- Align with EVM by setting x/0 = 0
- Fix storage analysis when Solidity optimizer is enabled
- Fixes in handling solc's --via-ir optimizer mode
- Fix wait time in CLI to 2:30 hours, to account for possible long queue times in CI runs

# 5.0.5 (November 21, 2023)

Please find a list of the main changes in v5 here {doc}/docs/cvl/v5-changes.

# CVL

- Allowing calling Solidity functions from within CVL hooks
- {ref}direct-storage-access
- Support for exhaustive parametric methods. Now method f calls will check for all methods in all contracts in Scene. The set of checked contracts can be limited with --parametric_contracts Contract1 Contract2
- Disallow declaring method variables (aka method f; declarations) outside the top-level scope of a rule. They could still be declared as rule and CVL function arguments
- Remove assume/assert notation from DELETE summary qualifiers
- Disallow Solidity calls in CVL quantifier bodies
---
# Performance

- [feat] New parallel splitter, can be enabled with --prover_args '-newSplitParallel true'
- [feat] A new option for potential help with timeouts --prover_args '-calltraceFreeOpt true'
- [feat] An option -relaxedPointerSemantics accepting a comma-separated list of contract:methodWithoutParamTypes pairs where the points-to analysis is allowed to be less strict
- [feat] Better support for internal function summaries when --via-ir option is used, enabled with --function_finder_mode relaxed
- [bugfix] Errors for an optimization we call “Memory partitioning” will now show up as alerts in the Global Problems view

# Misc

- [feat] Solana call trace basic support
- [feat] Mutation testing: Allow certoraMutate to run with a link to an original run
- [feat] Allow to skip solc warnings we consider errors (undefined return values) with --contract_compiler_skip_severe_warning_as_error
- [feat] --send_only is now the default mode except for CI users. Use --wait_for_results to force the old behavior
- [bugfix] Fixes for: Vyper, loop unrolling, CVL, memory consumption, storage splitting
- [bugfix] Remove support for native array theory in SMT
- [bugfix] Mutation testing: only delete files created by the mutation tester
- [UX] Old CLI format is now obsolete
- [UX] CVL1 type checker is not run anymore for compatibility checks
- [UX] --solc_args is deprecated

# 4.13.1 (September 26, 2023)

Minor improvements.

- [feat] Present array length accesses in call trace
- [bugfix] Report timeouts of sanity checks

# 4.12.1 (September 17, 2023)

CVL

- [bugfix] fix to bitwise operations
- [bugfix] verify range of nativeBalances[addr] values
- [bugfix] no duplication of multi-dimensional ghosts with axioms
- [feat] delete summary qualifiers for faster preprocessing and dealing with analysis-breaking external functions. If a function is never called from spec, it will not be processed. In cases where it is externally called from Solidity, the summary will apply.
- [feat] greater flexibility of internal summaries - allows accepting as arguments and returning certain reference types: primitive arrays, bytes, and structs which may (in nested structs too) contain primitive arrays
- [feat] support multiple return values from CVL functions
- [bugfix] Support keywords as struct fields and user defined type names
- [bugfix] Fix to multi-assert mode when multiple CVL asserts in a rule share the same message
- [UX] Skip rules where all methods are filtered out
- [bugfix] Do not drop quantifiers when instrumenting vacuity checks
- [UX] Improved error messages for preserved block errors
- [bugfix] Support invariant preserved blocks for functions with an argument which is an array of structs
- [feat] New keyword: executingContract available inside opcode hooks
- [bugfix] Applying the CALL opcode hook even if the balance transfer fails
---
# bugfix

Support assigning to a wildcard variable

Fail if CVL function is non-void and does not end with a return statement

# Performance

Optimizations for safe math handling, in particular for solc versions 8.19 and up

Better performance of string and array types

# Call Trace & Rule Report

Show storage changed since the start

More frequent rule-report update

Rule running time to show time interval instead of sum of sub-rules intervals

Show state of ghosts together with contract state

Fix formatting of values of type bytesN and of storage locations

# CLI

link to CVL2 migration document fixed

support for other formats of protocol author in package.json files

fix error message when passing global timeout setting

less verbose prints in terminal

Validate rule names

Show number of splits solved per rule and their "weight"

Fixes to equivalence checker

# Mutation Verification

correct traversing of rules

improved csv output

# Equivalence Checker

Support void functions

Support compiler comparison

Making comparison more reliable in terms of initial state and with respect to low-level calls

# 4.10.1 (August 21, 2023)

# CVL

Support Solidity calls also from internal summaries

Allowing with(env) for summaries {ref}with-env

lastStorage comparison fix for ghost maps

Bitwidth for bytesK variables is ensured, important for revert characteristic rules for methods accepting bytesK

Fixing structs encoding

Matching method summaries for methods accepting interfaces

Some improvements to how quantifiers calling Solidity functions are handled

# Mutation Verification

Output CSV files of the results

Manual mutations work and support for multiple manual mutations

certoraMutate working when running from project’s root
---
# Timeouts and performance

[feat] Show informative messages about cache hits
[bugfix] fix hashes of constant strings in constructors vs. in executable bytecode

# Linking

[bugfix] Fixing source-based heuristics linking to decrease chance for wrong matches
[bugfix] Fixes to sighash resolution
[bugfix] Correct revert handling in dispatched calls

# Vyper

[bugfix] Support for versions below 0.2.16 (from before storage layout output was introduced in Vyper)

# 4.8.0 (August 13, 2023)

# New features and enhancements

# CVL

Better expressivity: ALWAYS summaries can get bytesK arguments, e.g. ... => ALWAYS(to_bytesK(...))
Support for ALL_SLOAD and ALL_SSTORE hooks (see {ref}rawhooks)
Improved ABI encoding/decoding in CVL
More efficient handling of skipped rules
Allow calling Solidity functions from expression summaries

# Call Trace and Rule Report

Display havoced return values
Fixes to dump generation
Improved timeout visualization in TAC dumps
Fixes to presentation of quantified formulas in Call Trace
Better presentation of timeouts
Rule report will contain warnings about unused summaries
Display native balances
More friendly text for dispatcher-based resolutions
Improved ghost presentation

# Performance

Rule cache is enabled
Reducing number of iterations of static analyses
Improved decompiler performance

# Mutation Verifier

Manual mutants now supported in certoraMutate

# Equivalence Checker

Support for Vyper for pe equivalence checker (certoraEqCheck utility)

# CLI
---
# Allowing more Solidity file names

More compact zip input to cloud

Users can reduce the global timeout below 2 hours using {ref}--global_timeout

# Bug fixes

- More graceful handling of bit-vector mode so that it emits less errors. It should be noted that numbers are forced to the 256-bit range and thus it is not recommended to use bit-vector mode.
- Declaration of wildcard (i.e. _) variable names in rules or rule arguments is disallowed
- Internal summaries - disallow NONDET summary on functions returning a pointer, as well as HAVOC or HAVOC_ECF summaries
- Better checks on ghost axioms, especially if they refer to definitions
- Fixing array literal assignments
- Forbid assignments to array elements, i.e. uint[] a; a[0] = x; is disallowed
- Internal summarization did not work in certain tricky cases involving loops and external calls
- Fixing "Certora Prover Internal Error" sometimes appearing when reasoning on complex-typed arrays
- Fixes for structs with contract types as fields

# Call Trace

- Fix call trace generation issues for forall expressions

# Mutation Verifier

- Correctly dealing with original runs where rules were originally violated

# Misc.

- Static analyses bug fixes
- Fixes to read-only reentrancy rule
- Avoiding an exception when -dontStopAtFirstSplitTimeout completes with all splits timing out

# Other improvements

- Better parallelism and utilization
- Timeout cores and more difficulty traces and hints to study timeout causes
- Support for Solidity compiler version 0.8.20 and up

# 4.5.1 (July 15, 2023)

# New features

- Better expressivity: Allow binding the called contract in summaries using calledContract (see {ref}function-summary)
- Ease of use: Support reading and passing complex array and struct types in CVL. For example, you can write now: cvl env e; uint v; Test.MyComplexStruct x; uint[] thingArray = x.nested[v].thing; require thingArray.length == 3; assert foo(e, x, v) == 3;

For the Solidity snippet of a contract Test: solidity struct MyComplexStruct { MyInnerStruct[] nested; }

struct MyInnerStruct { uint[] thing; uint field; }
---
# function foo(MyComplexStruct memory z, uint x) external returns (uint) { return z.nested[x].thing.length; } ```

Ease of use: Support access for storage variables whose type is either a primitive, a user defined value, or an enum

Ease of use: Enum types can be cast to integer types in CVL using the usual assert_TYPE and require_TYPE operators (see cvl2-integer-types)

A built-in rule for read-only reentrancy vulnerabilities

# Call Trace

Better view of the storage state at storage assignments, storage restore points, and storage comparisons

Multi-contract handling

- Improvements to the call resolution fallback mechanism in case main analyses fail, allowing linking and summarizations despite the failures
- Introducing summarizeExtLibraryCallsAsNonDetPreLinking Prover option for easier setup of library-heavy code. See library_timeouts

Mutation Verifier

- New and easier to use certoraMutate. See mutation-verifier

Bug fixes

# CVL

- Fix issue when CVL functions are invoked within ternary expressions
- Fix evaluation of power expressions such as 2^256
- Make sure CVL keywords can appear as struct fields and be accessible from CVL

Performance

- Performance optimizations for the contract preprocessing step
- Performance improvements in Prover
- Performance improvements in CVL type checker (allows for faster job submission)

UX

- Show primary contract under verification even when a job is queued but not yet started
- envfree checks failures presented not just in rules section, but also in the problems view for highlighting
- Make sure more files generated by certoraRun are stored in .certora_internal
- Allow equivalence checker to have the same function name appear in two contracts

# 4.3.1 (July 2, 2023)

New features

# CVL

- New builtin rules: sanity and deepSanity
- Support a new keyword in CVL: satisfy
---
# User-defined types

User-defined types can appear in hook patterns

Support using currentContract in ghosts and quantified expressions

Support conversion of uintN to bytesK with casting bytesN-support

Support nativeBalances <special-fields> in CVL

Making access of user-defined-types (enums, structs, user-defined type values) in Solidity consistent, whether those types are declared in a contract or outside of a contract. Specifically, for a user-defined type that's declared in a contract, the access to it in a spec file is DeclaringContract.TypeName. For top-level user-defined types (declared outside of any contract/library) the access is using the using contract UsingContract.TypeName.

Support for EVM opcode hooks opcode-hooks

# CallTrace

Display CVL functions in Call Trace

CallTrace presenting skolemized variables for quantified expressions

Gather all setup labels in CallTrace to be under one label

Make CallTrace accept invocation of internal solidity functions from CVL

# Summarization

Early summarization of internal functions for improved performance and precision

“catch-all” summaries library_timeouts. For example, given a library L on which we wish to apply the same summary for all external methods in L, write function L._ external => NONDET

# Performance

More stable generation of formulas for more predictable, consistent running times of rules

Basic parallel splitting for improved running time of rule solving

# Other improvements

Change default to new certora-cli API

Check for an invalid rule name (given with --rule) locally, before sending a request to the server

Adapt CVL AST serialization to JSON to enable LSP for CVL2

Visualize unsolved splits in timeouts

# Bug fixes

Warn if CONST summary is applied to methods that return nothing

The type checker will fail if an internal method summary uses an inheriting contract name instead of the declaring contract name

Disallow shadowing of ghost variables

Support exists as a struct field in spec files

require_ and assert_ casts disallowed in ghost axioms

CallTrace bug fixes

# 4.0.5 (June 7, 2023) CVL 2

# Breaking changes

Upgrade to CVL 2 (see {doc}/docs/cvl/cvl2/changes and {doc}/docs/cvl/cvl2/migration)

Change the minimal python required version from 3.8.0 to 3.8.16

# New features

storage-comparison
---
# Prover Release Notes

|Version|Date|
|---|---|
|7.6.3|May 15, 2024|

# CVL

- [feat] Allow the use of contract aliases (using ERC20 as token) that were defined in the imported spec files.
- [feat] Can use filtered expressions for builtin rules
- [bugfix] Always run envfree checks, even if rule filters are applied
- [bugfix] envfree will be checked on the code after linking

# Rule Report

- [feat] Support jump-to-source for calls, local variables, and storage accesses
- [feat] Show structs passed to CVL functions in the call trace
- [feat] Show loop statistics in the live difficulty tab
- [feat] Show split-solving progress in live stats
- [feat] Show a notification if there are unresolved calls that can be resolved with --optimistic_fallback
- [feat] Show more info on procedures with nonlinear operations
- [UX] Prioritize ERROR states over other rule states

# Performance

- [feat] The -splitParallel option will now enable the new parallel splitter

# CLI

- [feat] Automatically set function-finder options depending on solc version and configuration
- [feat] New option --build_cache for faster re-compilation of previously compiled Solidity code

# Misc.

- [feat] Support for MCOPY EVM instruction

# Other improvements

- Performance improvements
- Bug fixes and internal improvements
- Improved error messages
- Improved console output
- Improved call resolution output
---
# CVL

|[feat] An option to make autofinders for internal functions less likely to cause compilation failures|use_memory_safe_autofinders|
|---|---|
|[feat] Dispatch-list summarization for calls with unresolved method identifiers|<catch-unresolved-calls-entry>|
|[feat] Preliminary support for tload, tstore operations in inline-assembly Solidity and EVM, along with ALL_TLOAD and ALL_TSTORE hooks|see transient-storage and rawhooks|
|[feat] Support direct access to immutables, including private immutables|<direct-immutable-access>|
|[feat] grounding of quantifiers supported with direct storage access expressions| |
|[feat] Support asterisk (*) wildcard in --rule, and a new option for --exclude_rule|see --exclude_rule|
|[feat] Support using requireInvariant with unused invariants from imported contracts| |
|[feat] Support blobhash instruction and opcode hooks| |
|[bugfix] Fix --address setting of fixed addresses to contracts to reflect in counterexamples properly| |
|[bugfix] Fixes to internal function detection| |
|[bugfix] Fix issue when dealing with contract-types| |
|[bugfix] Support multiple havoc-assuming statements inside a rule, hook, or function| |
|[bugfix] Support unary minus in quantifier expressions| |
|[bugfix] A helper option for detecting internal functions with Yul-optimizations enabled|finder_friendly_optimizer|
|[bugfix] A collection of fixes to internal function detection and summarization| |
|[bugfix] Support of summarization in old code using patterns like MakerDAO’s note modifier, enabled with prover_args '-rewriteMSizeAllocations true'|(the Global Warnings tab will advise when it’s recommended to be enabled)|

# Rule Report

[feat] Improved presentation of arrays and arrays’ lengp in pe call trace
[bugfix] Do not show rules as verified if pe sanity check timed-out
[UX] Show internal functions pat could not be detected (and as a result, summarized) in pe global problems view
[UX] Avoid showing redundant and irrelevant analysis failures

# Performance

[bugfix] Better safe map optimization for multiplication by constants
[bugfix] Fixes to new parallel splitter mode

# CLI

[feat] --compilation_steps_only option is exposed (runs only compilation and type checking)
[feat] --precise_bitwise_ops to easily enable bit-vector peory solvers Mutation Testing

# Mutation Testing

[feat] Allow omitting pe --conf flag to perform collection only
[bugfix] Fix root directory issue for mutated files in subdirectories
[bugfix] Rules pat failed sanity during pe run on pe original code but capture mutants will not be ignored when computing caught mutants

# Misc.

[feat] Preliminary support for running pe Prover on .yul contracts
[bugfix] Assume strictly monotonic increasing free memory pointer, to avoid counterexamples due to overflow in memory access
---
# 7.0.7 (March 15, 2024)

# CVL

[feat] if conditions in CVL must be wrapped wip parenpesis. Namely, if cond is illegal, use if (cond)
[feat] It is no longer needed to specify pe STORAGE keyword for Sload and Sstore hooks. Please find-replace in your current specs!
[feat] The default summarization policy for wildcard external functions (e.g. _.foo(..) =>) is UNRESOLVED, meaning pat pe summary will only apply to calls to foo whose target contract is unknown. If you wish to apply to all call sites of foo, including for properly linked contracts, write _.foo(..) => some_summary ALL;
[feat] Allow 'tuple like' syntax for assignments, e.g. (x,y) = foo();
[feat] Support blobbasefee variable in environment variables
[feat] {ref}Auto-summarization mode for heuristically expensive internal functions <detect-candidates-for-summarization>
[feat] Support hooking on lengp of dynamic storage arrays
[feat] {ref}Support basic struct comparison <struct-comparison>
[bugfix] Wildcards properly constrained when assigned e.g. in summarization
[bugfix] Ensure cleanliness of CVL strings in pe last word
[bugfix] Unlinked immutables are properly constrained to respect peir types
[bugfix] Correct invariant handling of pe base case rule for Vyper contracts
[bugfix] Fix to viewReentrancy builtin rule crash
[bugfix] Better type checking of quantified expressions wip definitions
[bugfix] Fix direct storage access to an array of structs
[bugfix] Fix for internal summaries using user-defined value types

# Rule Report

[feat] Display array lengp in variables tab
[feat] Display array lengp in CVL to CVL function calls
[bugfix] No false match on Vyper constructors in invariants and parametric rules
[bugfix] Consistent rule ordering
[bugfix] Show message in report when --prover_args are incorrect

# Static analysis and Performance

[feat] Automatic full unrolling of copy loops (no need to set -copyLoopUnroll option)
[bugfix] Proper deduplication of libraries imported by different scene-level contracts
[bugfix] Fix returns of static arrays
[bugfix] make hashing of encodePacked bytes result deterministic when -enableCopyLoopRewrites is set to true
[bugfix] Source-based call resolution is disabled by default except for constructor mepods. Can be re-enabled wip --prover_args '-enableSolidityBasedInlining true'

# Mutation Testing

[feat] Instead of running wip 2 conf files, one for pe Prover and one for mutation, now pe mutation settings are stored in pe Prover conf under pe key mutations
[feat] Relative paps to files to mutate are not relative to pe mutation conf, but relative to current working directory
[feat] Nicer help message for certoraMutate
[bugfix] Minor mutation testing csv output
[bugfix] Default to optimistically running all mutants, not waiting for pe original run
[bugfix] Improved error messages for manual mutations

# CLI

[feat] Instead of --prover_args '-optimisticFallback true' use --optimistic_fallback
---
# 6.3.1 (February 2, 2024)

[feat] Instead of --prover_args '-contractRecursionLimit N' use --contract_recursion_limit N, and a new flag --optimistic_contract_recursion
[feat] New option --compiler_map behaving exactly like --solc_map
[bugfix] Fix to --address when given wipout 0x prefix

# CVL

[feat] {ref}address-casting
[feat] {ref}ecrecover builtin support
[feat] Optimistically assume pe extcodesize is positive for calls pat are summarized and wip a non-HAVOC summary. This behavior can be disabled wip --prover_args 'optimisticExtcodesize false'
[feat] Support direct storage access in quantifiers and axioms
[bugfix] Implication, bi-implication and ternary conditional operators are right-associative
[bugfix] {ref}Fully support additional environment fields <env>. Namely, for env e, one can access e.block.basefee, e.block.coinbase, e.block.difficulty, e.block.gaslimit and e.tx.origin
[bugfix] Properly enforce bounds on enums accessed using direct storage access
[bugfix] Fix a bug wip structs being passed to summaries and not preserving peir fields’ values
[bugfix] Avoid hook inlining due to direct storage access
[bugfix] Type checker will error in presence of non-boolean expressions in quantifiers' bodies
[UX] Emit a global error in rule report if 0 rules are provided in pe spec
[UX] Cast assertions in CVL are treated like regular user-provided assertions
[UX] Warn about, and ignore, unused mepod arguments
[UX] Prevent calling library functions from CVL

# Call Trace and Rule Report

[feat] Add presentation of direct storage reads and direct storage havocs, including showing pe updates in pe Storage State
[feat] When pe user provided no assertion message, show pe assert condition
[bugfix] More refined handling of branch snippets wipin loop iterations
[bugfix] Ensure we get pe correct TAC dump link
[UX] Improved messages for assertions in builtin rules
[UX] New presentation for invariants
[UX] Branch snippets are now flattened, can be made hierarchical using --prover_args '-flattenBranchesInCallTrace false'

# Static analysis and Performance

[feat] abi.encodeCall calls will be considered as copy-loops, pus will not require a higher --loop_iter if we enable pe following option: --prover_args '-enableCopyLoopRewrites true'
[feat] Better performance on last assertions in a rule if --prover_args '-calltraceFreeOpt true' is enabled

# Misc

[feat] Support Vyper v0.3.10
[bugfix] Various bug fixes to improve stability of pe Prover (crashes, static analysis, and SMT solving)
[bugfix] Better support of importing user-defined types from Solidity imports even if pey are not given in a consistent fashion by solc

# 6.1.3 (January 11, 2024)

# CVL
---
# Rules

- Rules can now use both satisfy and assert statements together
- An option for checking satisfy statements one-by-one instead of depending on previous satisfy-s, enabled with --independent_satisfy
- {ref}persistent-ghosts
- Support selector keyword in CALL-like hooks that can be compared to function selectors
- New builtin function for hashing keccak256 in CVL
- Support method parameter filters when invariants are imported with use
- New options {ref}--optimistic_summary_recursion and {ref}--summary_recursion_limit

# Bugfixes

- Improved error messages for hooks
- Fix compile time checks for ghosts mappings axioms and bad CVL function calls therein
- Make CONSTANT summaries of internal functions consistent
- Allow Solidity struct fields named hook
- Fix to_bytes in quantifiers
- Better error message on struct decode failures
- Proper typing of sub-expressions of bitwise shift operations within quantifiers

# UX

- Nicer error messages for invalid use of max_* constants and hex literals
- Sanity builtin rule now succeeds when the sanity check succeeds (using satisfy under the hood) (note this can swap the expected result if you use the builtin sanity rule often, but you no longer have to interpret a “violated” result as the good one)

# Performance

- New optimization analysis. It can be configured to be more or less aggressive with the option --prover_args '-intervals_rewriter INT'
- New flag for better performance: --prover_args '-enableCopyLoopRewrites true' - replaces copy loop code blocks with a single copy command. Decreases problem size and obviates loop unrolling for copy loops (i.e., more sound)
- New flag for better performance: --prover_args '-enableAggressivePartitionPruning true' - for Solidity code that often manipulates dynamic objects in memory

# Call Trace

- Show branch source information (can be disabled with --prover_args '-enableConditionalSnippets false')
- Fix return value display for ghost reads

# Mutation Testing

- Generate mutation configuration automatically
- Expose errors emitted by Gambit
- certoraMutate now uses .mconf files instead of .conf

# Misc

- Enable the max constant loop unroll factor inferred with --prover_args '-loopUnrollBoundGuessUpperLimit INT
- Vyper fixes for static arrays, xor patterns, ABI fetching in old versions
- Support for some older versions of Vyper (0.3.7 and earlier)
- Better decompilation for try/catch in a loop
- Fix to false negative tautology check
- Better retry mechanism for job-submission by certora-cli
- Align with EVM by setting x/0 = 0
- Fix storage analysis when Solidity optimizer is enabled
- Fixes in handling solc's --via-ir optimizer mode
- Fix wait time in CLI to 2:30 hours, to account for possible long queue times in CI runs
---
# 5.0.5 (November 21, 2023)

Please find a list of the main changes in v5 here {doc}/docs/cvl/v5-changes.

# CVL

[feat] Allowing calling Solidity functions from wipin CVL hooks
[feat] {ref}direct-storage-access
[feat] Support for exhaustive parametric mepods. Now mepod f calls will check for all mepods in all contracts in Scene. The set of checked contracts can be limited wip --parametric_contracts Contract1 Contract2
[bugfix] Disallow declaring mepod variables (aka mepod f; declarations) outside pe top-level scope of a rule. They could still be declared as rule and CVL function arguments
[bugfix] Remove assume/assert notation from DELETE summary qualifiers
[bugfix] Disallow Solidity calls in CVL quantifier bodies
[bugfix] Support pe '

# Performance

[feat] New parallel splitter, can be enabled wip --prover_args '-newSplitParallel true'
[feat] A new option for potential help wip timeouts --prover_args '-calltraceFreeOpt true'
[feat] An option -relaxedPointerSemantics accepting a comma-separated list of contract:mepodWipoutParamTypes pairs where pe points-to analysis is allowed to be less strict
[feat] Better support for internal function summaries when --via-ir option is used, enabled wip --function_finder_mode relaxed
[bugfix] Errors for an optimization we call “Memory partitioning” will now show up as alerts in pe Global Problems view

# Misc

[feat] Solana call trace basic support
[feat] Mutation testing: Allow certoraMutate to run wip a link to an original run
[feat] Allow to skip solc warnings we consider errors (undefined return values) wip --contract_compiler_skip_severe_warning_as_error
[feat] --send_only is now pe default mode except for CI users. Use --wait_for_results to force pe old behavior
[bugfix] Fixes for: Vyper, loop unrolling, CVL, memory consumption, storage splitting
[bugfix] Remove support for native array peory in SMT
[bugfix] Mutation testing: only delete files created by pe mutation tester
[UX] Old CLI format is now obsolete
[UX] CVL1 type checker is not run anymore for compatibility checks
[UX] --solc_args is deprecated

# 4.13.1 (September 26, 2023)

Minor improvements.

[feat] Present array lengp accesses in call trace
[bugfix] Report timeouts of sanity checks

# 4.12.1 (September 17, 2023)

# CVL

[bugfix] fix to bitwise operations
[bugfix] verify range of nativeBalances[addr] values
sign in identifiers (specifically for Solidity functions)
[UX] When non-reverting calls lead to an 'empty function' because all paps revert, show an alert in pe rule report

# Performance

|[feat] New parallel splitter, can be enabled with --prover_args '-newSplitParallel true'|
|---|
|[feat] A new option for potential help with timeouts --prover_args '-calltraceFreeOpt true'|
|[feat] An option -relaxedPointerSemantics accepting a comma-separated list of contract:methodWithoutParamTypes pairs where the points-to analysis is allowed to be less strict|
|[feat] Better support for internal function summaries when --via-ir option is used, enabled with --function_finder_mode relaxed|
|[bugfix] Errors for an optimization we call “Memory partitioning” will now show up as alerts in the Global Problems view|

# Misc

|[feat] Solana call trace basic support|
|---|
|[feat] Mutation testing: Allow certoraMutate to run with a link to an original run|
|[feat] Allow to skip solc warnings we consider errors (undefined return values) with --contract_compiler_skip_severe_warning_as_error|
|[feat] --send_only is now the default mode except for CI users. Use --wait_for_results to force the old behavior|
|[bugfix] Fixes for: Vyper, loop unrolling, CVL, memory consumption, storage splitting|
|[bugfix] Remove support for native array theory in SMT|
|[bugfix] Mutation testing: only delete files created by the mutation tester|
|[UX] Old CLI format is now obsolete|
|[UX] CVL1 type checker is not run anymore for compatibility checks|
|[UX] --solc_args is deprecated|

# 4.13.1 (September 26, 2023)

Minor improvements.

|[feat] Present array length accesses in call trace|
|---|
|[bugfix] Report timeouts of sanity checks|

# 4.12.1 (September 17, 2023)

# CVL

|[bugfix] fix to bitwise operations|
|---|
|[bugfix] verify range of nativeBalances[addr] values|
---
# Bugfix

no duplication of multi-dimensional ghosts wip axioms
Support keywords as struct fields and user defined type names
Fix to multi-assert mode when multiple CVL asserts in a rule share pe same message
Do not drop quantifiers when instrumenting vacuity checks
Support invariant preserved blocks for functions wip an argument which is an array of structs
Applying pe CALL opcode hook even if pe balance transfer fails
Support assigning to a wildcard variable
Fail if CVL function is non-void and does not end wip a return statement

# Feature

delete summary qualifiers for faster preprocessing and dealing wip analysis-breaking external functions. If a function is never called from spec, it will not be processed. In cases where it is externally called from Solidity, pe summary will apply.
greater flexibility of internal summaries - allows accepting as arguments and returning certain reference types: primitive arrays, bytes, and structs which may (in nested structs too) contain primitive arrays
support multiple return values from CVL functions
New keyword: executingContract available inside opcode hooks

# UX

Skip rules where all mepods are filtered out
Improved error messages for preserved block errors

# Performance

Optimizations for safe map handling, in particular for solc versions 8.19 and up
Better performance of string and array types

# Call Trace & Rule Report

Show storage changed since pe start
More frequent rule-report update
Rule running time to show time interval instead of sum of sub-rules intervals
Show state of ghosts togeper wip contract state
Fix formatting of values of type bytesN and of storage locations

# CLI

link to CVL2 migration document fixed
support for oper formats of protocol aupor in package.json files
fix error message when passing global timeout setting
less verbose prints in terminal
Validate rule names
Show number of splits solved per rule and peir "weight"
Fixes to equivalence checker

# Mutation Verification

correct traversing of rules
improved csv output

# Equivalence Checker

Support void functions
Support compiler comparison
Making comparison more reliable in terms of initial state and wip respect to low-level calls
---
# 4.8.0 (August 13, 2023)

# New features and enhancements

- Better expressivity: ALWAYS summaries can get bytesK arguments, e.g. ... => ALWAYS(to_bytesK(...))
- Support for ALL_SLOAD and ALL_SSTORE hooks (see {ref}rawhooks)
- Improved ABI encoding/decoding in CVL
- More efficient handling of skipped rules
- Allow calling Solidity functions from expression summaries

# Call Trace and Rule Report

- Display havoced return values
- Fixes to dump generation
- Improved timeout visualization in TAC dumps
- Fixes to presentation of quantified formulas in Call Trace
- Better presentation of timeouts
- Rule report will contain warnings about unused summaries
- Display native balances
- More friendly text for dispatcher-based resolutions
- Improved ghost presentation

# Performance

# Mutation Verification

- Output CSV files of the results
- Manual mutations work and support for multiple manual mutations
- certoraMutate working when running from project’s root

# Timeouts and performance

- Show informative messages about cache hits
- Fix hashes of constant strings in constructors vs. in executable bytecode

# Linking

- Fixing source-based heuristics linking to decrease chance for wrong matches
- Fixes to sighash resolution
- Correct revert handling in dispatched calls

# Vyper

- Support for versions below 0.2.16 (from before storage layout output was introduced in Vyper)
---
Rule cache is enabled

Reducing number of iterations of static analyses

Improved decompiler performance

# Mutation Verifier

Manual mutants now supported in certoraMutate

# Equivalence Checker

Support for Vyper for the equivalence checker (certoraEqCheck utility)

# CLI

Allowing more Solidity file names

More compact zip input to cloud

Users can reduce the global timeout below 2 hours using --global_timeout

# Bug fixes

# CVL

More graceful handling of bit-vector mode so that it emits less errors. It should be noted that numbers are forced to the 256-bit range and thus it is not recommended to use bit-vector mode.

Declaration of wildcard (i.e. _) variable names in rules or rule arguments is disallowed

Internal summaries - disallow NONDET summary on functions returning a pointer, as well as HAVOC or HAVOC_ECF summaries

Better checks on ghost axioms, especially if they refer to definitions

Fixing array literal assignments

Forbid assignments to array elements, i.e. uint[] a; a[0] = x; is disallowed

Internal summarization did not work in certain tricky cases involving loops and external calls

Fixing "Certora Prover Internal Error" sometimes appearing when reasoning on complex-typed arrays

Fixes for structs with contract types as fields

# Call Trace

Fix call trace generation issues for forall expressions

# Mutation Verifier

Correctly dealing with original runs where rules were originally violated

# Misc.

Static analyses bug fixes

Fixes to read-only reentrancy rule

Avoiding an exception when -dontStopAtFirstSplitTimeout completes with all splits timing out

# Other improvements

Better parallelism and utilization

Timeout cores and more difficulty traces and hints to study timeout causes

Support for Solidity compiler version 0.8.20 and up
---
# New features

CVL
Better expressivity: Allow binding pe called contract in summaries using calledContract (see {ref}function-summary)
Ease of use: Support reading and passing complex array and struct types in CVL. For example, you can write now: cvl env e; uint v; Test.MyComplexStruct x; uint[] pingArray = x.nested[v].ping; require pingArray.lengp == 3; assert foo(e, x, v) == 3;

For the Solidity snippet of a contract Test:

solidity
struct MyComplexStruct {
MyInnerStruct[] nested;
}

struct MyInnerStruct {
uint[] thing;
uint field;
}

function foo(MyComplexStruct memory z, uint x) external returns (uint) {
return z.nested[x].thing.length;
}

Ease of use: Support access for storage variables whose type is eiper a primitive, a user defined value, or an enum
Ease of use: Enum types can be cast to integer types in CVL using pe usual assert_TYPE and require_TYPE operators (see {ref}cvl2-integer-types)
A built-in rule for read-only reentrancy vulnerabilities

# Call Trace

- Better view of the storage state at storage assignments, storage restore points, and storage comparisons

# Multi-contract handling

- Improvements to the call resolution fallback mechanism in case main analyses fail, allowing linking and summarizations despite the failures
- Introducing summarizeExtLibraryCallsAsNonDetPreLinking Prover option for easier setup of library-heavy code. See {ref}library_timeouts

# Mutation Verifier

- New and easier to use certoraMutate. See {doc}/docs/gambit/mutation-verifier

# Bug fixes

CVL
Fix issue when CVL functions are invoked wipin ternary expressions
Fix evaluation of power expressions such as 2^256
Make sure CVL keywords can appear as struct fields and be accessible from CVL

# Performance

- Performance optimizations for the contract preprocessing step
- Performance improvements in Prover
- Performance improvements in CVL type checker (allows for faster job submission)
---
UX

Show primary contract under verification even when a job is queued but not yet started

{ref}envfree <envfree> checks failures presented not just in rules section, but also in the problems view for highlighting

Make sure more files generated by certoraRun are stored in .certora_internal

Allow equivalence checker to have the same function name appear in two contracts

4.3.1 (July 2, 2023)

New features

CVL

New builtin rules: {ref}sanity <built-in-sanity> and {ref}deepSanity <built-in-deep-sanity>

Support a new keyword in CVL: {ref}satisfy <satisfy>

User-defined types can appear in hook patterns

Support using currentContract in ghosts and quantified expressions

Support conversion of uintN to bytesK with casting {ref}bytesN-support

Support {ref}nativeBalances <special-fields> in CVL

Making access of user-defined-types (enums, structs, user-defined type values) in Solidity consistent, whether those types are declared in a contract or outside of a contract. Specifically, for a user-defined type that's declared in a contract, the access to it in a spec file is DeclaringContract.TypeName. For top-level user-defined types (declared outside of any contract/library) the access is using the using contract UsingContract.TypeName.

Support for {ref}EVM opcode hooks <opcode-hooks>

CallTrace

Display CVL functions in Call Trace

CallTrace presenting skolemized variables for quantified expressions

Gather all setup labels in CallTrace to be under one label

Make CallTrace accept invocation of internal solidity functions from CVL

Summarization

Early summarization of internal functions for improved performance and precision

{ref}“catch-all” summaries <library_timeouts>. For example, given a library L on which we wish to apply the same summary for all external methods in L, write function L._ external => NONDET

Performance

More stable generation of formulas for more predictable, consistent running times of rules

Basic parallel splitting for improved running time of rule solving

Other improvements

Change default to new certora-cli API

Check for an invalid rule name (given with --rule) locally, before sending a request to the server

Adapt CVL AST serialization to JSON to enable LSP for CVL2

Visualize unsolved splits in timeouts

Bug fixes

Warn if CONST summary is applied to methods that return nothing
---
# The type checker will fail if an internal method summary uses an inheriting contract name instead of the declaring contract name

Disallow shadowing of ghost variables

Support exists as a struct field in spec files

require_ and assert_ casts disallowed in ghost axioms

CallTrace bug fixes

4.0.5 (June 7, 2023) CVL 2

# Breaking changes

- Upgrade to CVL 2 (see {doc}/docs/cvl/cvl2/changes and {doc}/docs/cvl/cvl2/migration)
- Change the minimal python required version from 3.8.0 to 3.8.16

# New features

- {ref}storage-comparison
- Add support for Vyper
- Support CONSTANT summaries for all non-dynamic return types
- New {ref}built-in rules <built-in> sanity and deepSanity
- Added --protocol_name and --protocol_owner flags

# Other improvements

- Performance improvements
- Bug fixes and internal improvements
- Improved error messages
- Improved console output
- Improved call resolution output