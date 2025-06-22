# Black-Scholes Option Pricer

This repository contains a Python implementation of the Black-Scholes-Merton model for pricing European call and put options.

## Overview

The Black-Scholes model provides a theoretical framework for estimating the fair value of European-style options. It calculates option prices based on the following financial parameters:

- `S`: Current price of the underlying asset  
- `K`: Strike price of the option  
- `T`: Time to expiration (in years)  
- `r`: Risk-free interest rate  
- `sigma`: Volatility of the underlying asset

## Code Description

The script defines a function that calculates both call and put option prices using the Black-Scholes formula. It uses Python's `math` module for basic mathematical operations and `scipy.stats.norm` for cumulative distribution functions.

### Example Parameters
```python
S = 45      # Underlying asset price
K = 40      # Strike price
T = 2       # Time to expiration (in years)
r = 0.1     # Risk-free interest rate
sigma = 0.1 # Volatility
```

Output:
```
Call Option Price: $12.27  
Put Option Price: $0.02
```

## Requirements
- Python 3  
- scipy
