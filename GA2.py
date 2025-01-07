import random

# Define the function for (x, y)
def my_function(x, y):
    return (x + y) * 2

# Define the function for x
def my_function_x(x):
    return 2 * x  # Example function for x

# Function to create a random binary string
def create_random_chromosome(length):
    return ''.join(random.choice('01') for _ in range(length))

# Function to perform crossover
def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)  # Random crossover point
    child1 = parent1[:crossover_point] + parent2[crossover_point:]  # Combine halves
    child2 = parent2[:crossover_point] + parent1[crossover_point:]  # Combine halves
    return child1, child2

# Function to perform mutation
def mutate(chromosome, mutation_rate):
    new_chromosome = list(chromosome)  # Convert string to list for mutability
    for i in range(len(new_chromosome)):
        if random.random() < mutation_rate:  # Mutate with a certain probability
            new_chromosome[i] = '1' if new_chromosome[i] == '0' else '0'  # Flip the bit
    return ''.join(new_chromosome)  # Convert back to string

# Genetic algorithm to find the minimum function value
def genetic_algorithm(population_size, chromosome_length, mutation_rate, max_generations):
    # Create initial population
    population = [create_random_chromosome(chromosome_length) for _ in range(population_size)]

    best_value = float('inf')
    best_chromosome = None

    for generation in range(max_generations):
        # Calculate fitness for the population
        fitness = []
        for chromosome in population:
            x_decimal = int(chromosome[:chromosome_length // 2], 2)  # First half for x
            y_decimal = int(chromosome[chromosome_length // 2:], 2)  # Second half for y
            fit_value = my_function(x_decimal, y_decimal)
            fitness.append((fit_value, chromosome))

            # Update best value
            if fit_value < best_value:
                best_value = fit_value
                best_chromosome = chromosome

        # Sort population by fitness (ascending order)
        population = [chromosome for _, chromosome in sorted(fitness)]

        # Create next generation (offspring)
        next_generation = []
        while len(next_generation) < population_size:
            parent1 = random.choice(population[:population_size // 2])  # Select from the top half
            parent2 = random.choice(population[:population_size // 2])  # Select from the top half

            # Perform crossover
            child1, child2 = crossover(parent1, parent2)
            next_generation.extend([mutate(child1, mutation_rate), mutate(child2, mutation_rate)])

        population = next_generation[:population_size]  # Keep population size constant

    # Convert best chromosome back to decimal to find x and y
    best_x = int(best_chromosome[:chromosome_length // 2], 2)
    best_y = int(best_chromosome[chromosome_length // 2:], 2)

    return (best_x, best_y), best_value

# Parameters
population_size = 20  # Number of chromosomes
chromosome_length = 12  # Total length of the chromosome (for x and y)
mutation_rate = 0.1  # Probability of mutation
max_generations = 100  # Maximum number of generations

# Run the genetic algorithm
best_point, best_value = genetic_algorithm(population_size, chromosome_length, mutation_rate, max_generations)

# Final output
print(f"Best point found: {best_point} with function value: {best_value}")
