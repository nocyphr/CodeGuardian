apparently there is a `pip install lizard` that can be used to analyze cc for many languages using the command: `lizard <file_path>`

```python
import lizard

# Analyze a specific file
file_path = "path_to_your_file.py"
analysis_results = lizard.analyze_file(file_path)

# Get and print the average CCN for the file
average_ccn = analysis_results.average_cyclomatic_complexity
print(f"Average CCN for the file: {average_ccn}")

# List and print the CCN for each function
print("\nCCN per function:")
for function in analysis_results.function_list:
    print(f"Function: {function.name}, CCN: {function.cyclomatic_complexity}")
```