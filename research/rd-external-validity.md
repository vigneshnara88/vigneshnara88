# RD external validity / AIPW_RD

Frontend and R/Python package development supporting a research extension to regression discontinuity designs.

**Core research ideas and intellectual direction:** Prof. Kirill Borusyak, Dr Luther Yap and Dr Sid George.

A regression discontinuity (RD) design studies a treatment rule that changes at a threshold. Imagine a programme that admits applicants scoring at least 70: applicants just below and just above that score may provide a useful comparison. Under the design's assumptions, their outcome difference tells us about the effect at that margin.

The policy question can be broader. What if we want to inform a decision about applicants whose backgrounds differ from those near the cutoff? An effect for the local group does not automatically describe a population with a different mix of characteristics, particularly when different people benefit differently.

**Extending external validity means examining how that local evidence can inform a wider target population, and what additional assumptions and information the connection needs.** Observed characteristics help describe the difference between the local comparison and the target population; a transparent method makes the modelling choices behind the extension visible.

The package focuses on averaging a modelled contrast at the boundary over a target distribution of observed characteristics. This is more specific than claiming to know the treatment effect at every value far from the cutoff. The distinction matters: changing the population over which an effect is averaged and identifying effects at different running-variable values are related but separate questions.

## Why the software interface matters

Research software turns a methodological idea into a workflow another researcher can inspect: identify the outcome, running variable and covariates; choose a specification; estimate the target; and inspect the result and its uncertainty. Clear interfaces and output conventions make these decisions easier to communicate and compare.

My work focused on the frontend and package interfaces: R and Python wrappers, command-line usage, examples, documentation, structured estimation outputs, implementation support and diagnostics. The aim was to make the researchers' approach easier to use and inspect.

The AIPW_RD research repository remains private because it supports unpublished collaborative work.

[Back to profile](../README.md)
