# Chemical_Equation_Balancer

## Overview
This Python script balances chemical equations using a randomized coefficient approach. It allows users to input chemical formulas in various formats, including:
- **Molecular formula** (e.g., `C3H6O2`)
- **Condensed formula of organic molecules** (e.g., `CH3COOCH3`)
- **Formulas with brackets** (e.g., `Ca3(PO4)2`)

The script parses the input, identifies elements and their occurrences, and determines the appropriate coefficients to balance the equation.

## Features
- **Supports diverse chemical formula formats**
- **Handles subscripts and bracketed groups**
- **Uses a randomized approach to find balancing coefficients**
- **Automatically simplifies coefficients using the greatest common divisor (GCD)**

## Requirements
- Python 3.x
- No additional libraries are required (only built-in Python modules are used)

## Usage
1. Run the script in a Python environment.
2. Enter the number of reactant and product molecules when prompted.
3. Input the chemical formulas of reactants and products.
4. The script will compute and display the balanced equation.

### Example Run
**Input:**
```
How many reactant molecules? --> 2
How many product molecules? --> 2
Chemical formula of reactant molecule 1 --> H2
Chemical formula of reactant molecule 2 --> O2
Chemical formula of product molecule 1 --> H2O
```

**Output:**
```
2 H2 + O2 = 2 H2O
```

## How It Works
1. **Input Handling:** Prompts user for the number and formulas of reactants and products.
2. **Formula Parsing:** Extracts atomic composition from each formula, handling subscripts and bracketed groups.
3. **Matrix Setup:** Constructs a system of linear equations based on atomic conservation.
4. **Randomized Search:** Generates random coefficient sets until a valid solution is found.
5. **Simplification:** Reduces coefficients to their simplest form.
6. **Equation Output:** Prints the balanced chemical equation.

## Limitations
- The randomized approach may take longer for complex equations.
- Does not guarantee the minimal integer solution immediately.

## Future Improvements
- Implement a deterministic matrix-based method for faster balancing.
- Add support for ionic equations and charge balancing.
- Enhance input validation and error handling.

