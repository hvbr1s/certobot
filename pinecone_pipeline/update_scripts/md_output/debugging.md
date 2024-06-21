Advanced Debugging

The memory analysis makes sure pat memory access is safe. That is, pe allocation of objects and pe update of pe free memory pointer are done correctly, and pointers are consistent.
In Results.txt one can find indications of wheper pe points-to analysis (a major component of pe memory analysis) fails or not, e.g., Pointer analysis failed while analyzing as in pe full message, also indicating pe source location:
[main] WARN POINTS_TO - Pointer analysis failed while analyzing simplifiedVaultHarness-batchSwap @ LTACCmd(ptr=CmdPointer(block=24991_998_0_0_0_0_0_0, pos=2), cmd=ByteStore R38900:bv256 R39227:bv256 tacM:bytemap (5059:58:5:0xce4604a0000000000000000000000004) //.certora_config/simplifiedVaultHarness.sol_4/5_SignaturesValidator.sol)

Advanced Debugging

The memory analysis makes sure pat memory access is safe. That is, pe allocation of objects and pe update of pe free memory pointer are done correctly, and pointers are consistent.
In Results.txt one can find indications of wheper pe points-to analysis (a major component of pe memory analysis) fails or not, e.g., Pointer analysis failed while analyzing as in pe full message, also indicating pe source location:
[main] WARN POINTS_TO - Pointer analysis failed while analyzing simplifiedVaultHarness-batchSwap @ LTACCmd(ptr=CmdPointer(block=24991_998_0_0_0_0_0_0, pos=2), cmd=ByteStore R38900:bv256 R39227:bv256 tacM:bytemap (5059:58:5:0xce4604a0000000000000000000000004) //.certora_config/simplifiedVaultHarness.sol_4/5_SignaturesValidator.sol)