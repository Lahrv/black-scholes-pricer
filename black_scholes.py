import math
from scipy.stats import norm

def black_scholes_call_put(S, K, T, r, sigma):
    """
    Calculate the Black-Scholes price for a European call and put option.

    Parameters:
    S (float): Current stock price
    K (float): Strike price
    T (float): Time to expiration in years
    r (float): Risk-free interest rate (annual)
    sigma (float): Volatility of the underlying asset (annual)

    Returns:
    tuple: (call_price, put_price)
    """
    d1 = (math.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * math.sqrt(T))
    d2 = d1 - sigma * math.sqrt(T)

    call_price = S * norm.cdf(d1) - K * math.exp(-r * T) * norm.cdf(d2)
    put_price = K * math.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return call_price, put_price

# Example usage
if __name__ == "__main__":
    # Sample parameters
    S = 45      # Underlying price
    K = 40      # Strike price
    T = 2       # Time to expiration (years)
    r = 0.1     # Risk-free rate (10%)
    sigma = 0.1 # Volatility (10%)

    call, put = black_scholes_call_put(S, K, T, r, sigma)

    print(f"Call Option Price: ${call:.2f}")
    print(f"Put Option Price: ${put:.2f}")
