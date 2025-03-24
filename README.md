# File Path Lookup Test

## How to Run

Clone this repo.
Use venv or smth.
Checkout submodule (I use pixeljs as a dataset).
Populate filesystem with file to lookup.

Run:

```powershell
python run_test.py
```

This will execute performance tests comparing different file path reverse single-branch lookup implementations.

My results are:

Stupid implementation:
Execution completed in: 0.0010 seconds

Oswalk:
Execution completed in: 0.0000 seconds
