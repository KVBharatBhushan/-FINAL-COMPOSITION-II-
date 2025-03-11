import pandas as pd
import numpy as np
from numba import njit, prange

@njit
def is_prime(n):
    """Efficient check to verify if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@njit(parallel=True)
def find_primes_with_suffix(start, end, suffix):
    """Find all prime numbers ending with a specific suffix."""
    primes = []
    for x in prange(start, end + 1):
        # Use string concatenation instead of f-strings
        prefix = str(x).zfill(2)  # Ensures XX is 2 digits (with leading zeros if necessary)
        candidate = int(prefix + suffix)  # Construct the full number
        if is_prime(candidate):
            primes.append(candidate)
    return primes

def save_to_excel(primes, output_path):
    """Save the prime numbers to an Excel file."""
    df = pd.DataFrame(primes, columns=["Prime Numbers"])
    df.to_excel(output_path, index=False)
    print(f"Prime numbers saved to {output_path}")

# Define the range, suffix, and output path
start = 0  # XX from 00
end = 99   # XX to 99
suffix = "562949953421312999"  # Suffix for the prime numbers
output_path = "E:\\My PenDrive\\PRIME NUMBERS SUMMARY\\SPACE PROGRAMMING SERIES\\INFINITYHANUMANKVHANUMAN\\XYZ_2^49_999_PRIMES.xlsx"

# Find primes and save them to an Excel file
try:
    print("Processing, please wait...")
    primes = find_primes_with_suffix(start, end, suffix)
    save_to_excel(primes, output_path)
    print("Processing completed successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
