# Define function to generate Fibonacci sequence
def generate_fibonacci_sequence(n):
    # Initialize the sequence with the first two Fibonacci numbers
    sequence = [0, 1]
    
    # Generate Fibonacci sequence up to the nth number
    for i in range(2, n):
        # Calculate the next Fibonacci number by adding the last two numbers
        next_number = sequence[i-1] + sequence[i-2]
        
        # Append the next Fibonacci number to the sequence
        sequence.append(next_number)
    
    # Return the generated Fibonacci sequence
    return sequence

# Number of Fibonacci numbers to generate
n = 20

# Generate Fibonacci sequence
fib_seq = generate_fibonacci_sequence(n)

# Print the generated Fibonacci sequence
print(f'Fibonacci sequence with {n} elements is {fib_seq}')