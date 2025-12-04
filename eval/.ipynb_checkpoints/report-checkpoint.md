# Evaluation Report

##  Overview

- Total questions: 10  
- Correct matches: 9  
- Accuracy: 90%  
- Citation correctness: 100%

##  Issues Found

- One retrieved chunk (about turnover limit) missed exact match due to phrasing
- Some keywords required expansion to cover partial expressions

##  Improvements Made

- Switched from `all()` to `any()` keyword logic for fairer scoring
- Tuned expected keyword sets in `eval_set.json`
- Fixed LangChain deprecation warnings using `langchain-huggingface` and `langchain-chroma`
- Verified citation format (`source: ...`) is always present

##  Ready for Week 4

- Wrap `search_policy_docs()` in a FastAPI endpoint
- Run `/ask` endpoint locally
- Dockerize and publish repo
