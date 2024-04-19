# Function that generates arithmetic progression
def generate_arithmetic_progression(a, d, n):
    # Initialize an empty list to store the arithmetic progression
    progression = []
    
    # Initialize the current term to the first term of the progression
    current_term = a
    
    # Generate the arithmetic progression up to the nth term
    for i in range(n):
        # Append the current term to the progression list
        progression.append(current_term)
        
        # Calculate the next term by adding the common difference to the current term
        current_term += d
    
    # Return the generated arithmetic progression
    return progression

# Example usage
a = 2  # First term
d = 3  # Common difference
n = 10  # Number of terms to generate

# Generate arithmetic progression
progression = generate_arithmetic_progression(a, d, n)

# Print the generated arithmetic progression
print(f'Arithmetic sequence with {n} elements is {progression}')