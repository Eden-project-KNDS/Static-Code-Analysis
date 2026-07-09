# Static Code Analysis Tool

A Python static code analysis tool that detects performance anti-patterns and code quality issues using **Semgrep**. The tool scans your Python codebase, identifies problematic patterns, assigns performance costs, and provides an overall code quality assessment.

## Overview

This project automates the detection of common Python performance anti-patterns through:
1. **Semgrep scanning** - Uses pattern-based rules to identify code issues
2. **Cost calculation** - Assigns performance costs to detected anti-patterns
3. **Quality assessment** - Provides an overall code quality rating

## Detected Anti-Patterns

### 1. List Initialization in Loop
```python
# Anti-pattern
my_list = []
for item in data:
    my_list.append(item * 2)

# Better approach
my_list = [item * 2 for item in data]
```
- **Issue**: Multiple function call overheads in each iteration
- **Cost**: 50 points
- **Solution**: Use list comprehensions instead

### 2. String Concatenation in Loop
```python
# Anti-pattern
result = ""
for word in words:
    result += word

# Better approach
result = "".join(words)
```
- **Issue**: Creates new string objects in memory on each iteration
- **Cost**: 200 points
- **Solution**: Use `str.join()` for efficient concatenation

### 3. Iterating with `range(len())`
```python
# Anti-pattern
for i in range(len(sequence)):
    print(sequence[i])

# Better approach
for item in sequence:
    print(item)
```
- **Issue**: Slightly slower than direct iteration in CPython
- **Cost**: 100 points
- **Solution**: Iterate directly over the sequence

## Quick Start

### Prerequisites
- Python 3.7+
- Semgrep installed
- Conda (recommended for environment setup)

### Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Static-Code-Analysis
   ```

2. **Create the conda environment**
   ```bash
   conda env create -f environment.yml
   conda activate staticAnalyzer
   ```

3. **Install Semgrep** (if not already installed)
   ```bash
   pip install semgrep
   ```

### Usage

Run the complete analysis pipeline:
```bash
bash run_analysis.sh
```

Or run individual components:

1. **Run Semgrep scan only**
   ```bash
   semgrep scan --config=python_anti_patterns.yaml --json -o semgrep_results.json .
   ```

2. **Parse results and calculate cost**
   ```bash
   python3 parser.py semgrep_results.json
   ```

## Output & Scoring

The tool calculates a performance cost score:

| Score | Assessment | Recommendation |
|-------|------------|-----------------|
| 0-500 | **Optimal** |  Code follows best practices |
| 501-1000 | **Semi-optimal** |  Some improvements needed |
| 1001+ | **Not optimal** |  Multiple issues found |

### Example Output
```
Your cost is: 350
Code is optimal
```

##  Project Structure

```
├── run_analysis.sh              # Main pipeline script
├── parser.py                    # JSON parser and cost calculator
├── python_anti_patterns.yaml    # Semgrep rules configuration
├── main.py                      # Example file with anti-patterns
├── bad_data.py                  # Test data with anti-patterns
├── environment.yml              # Conda environment configuration
├── semgrep_results.json         # Generated scan results
└── README.md                    # This file
```

##  Configuration

Edit `python_anti_patterns.yaml` to customize rules:
- Add new anti-pattern rules
- Modify existing patterns
- Adjust severity levels (INFO, WARNING, ERROR)
- Update cost values

##  Files Description

- **run_analysis.sh**: Orchestrates the entire analysis pipeline
- **parser.py**: Parses Semgrep JSON output and calculates total cost
- **python_anti_patterns.yaml**: Defines pattern-matching rules for Semgrep
- **main.py**: Example Python file demonstrating the detected anti-patterns
- **bad_data.py**: Additional test file with anti-patterns



##  Support

For issues or questions, please refer to the project repository.