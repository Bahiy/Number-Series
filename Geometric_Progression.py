# Function that generates geometric progression
def generate_geometric_progression(a, r, n):
    # Initialize an empty list to store the geometric progression
    progression = []
    
    # Initialize the current term to the first term of the progression
    current_term = a
    
    # Generate the geometric progression up to the nth term
    for i in range(n):
        # Append the current term to the progression list
        progression.append(current_term)
        
        # Calculate the next term by multiplying the current term by the common ratio
        current_term *= r
    
    # Return the generated geometric progression
    return progression

# Example usage
a = 3  # First term
r = 2  # Common ratio
n = 10  # Number of terms to generate

# Generate geometric progression
progression = generate_geometric_progression(a, r, n)

# Print the generated geometric progression
print(f'Geometric sequence with {n} elements is {progression}')