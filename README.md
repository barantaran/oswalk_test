# File Path Lookup Test

## How to Run

Clone this repo with submodule.
```
> git clone --recurse-submodules -j8 https://github.com/barantaran/oswalk_test.git
```
Then:
```
> cd oswalk_test
```
Use venv or smth to run python scripts, e.g.:
```
> python -m venv .venv
> .venv\Scripts\activate
```

Populate filesystem with file to lookup.
```
> python copy_file.py
```

Run test:

```
> python run_test.py
```

This will execute performance tests comparing different file path reverse single-branch lookup implementations.

My results are:

Stupid implementation:
Execution completed in: 0.0010 seconds


Oswalk:
Execution completed in: 0.0270 seconds
