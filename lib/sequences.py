#!/usr/bin/env python3

def print_fibonacci(n):
    if n <= 0:
        print([])  # Print an empty list when n == 0
        return
    
    fibonacci_sequence = [0, 1]
    
    for _ in range(2, n):
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    
    print(fibonacci_sequence[:n])