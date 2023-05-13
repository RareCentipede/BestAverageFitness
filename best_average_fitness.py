def main():
    schema_pool_1 = ['11111', '1111*', '111**', '11***', '1****']
    schema_pool_2 = ['00000', '0000*', '000**', '00***', '0****']

    for schema1, schema2 in zip(schema_pool_1, schema_pool_2):
        assert len(schema1) == len(schema2), "Schema lengths must be equal"

        population1 = generate_population(schema1, len(schema1))
        population2 = generate_population(schema2, len(schema2))

        average_fitness1 = average_fitness(population1, len(schema1))
        average_fitness2 = average_fitness(population2, len(schema2))

        print(f"Average fitness of schema 1 {schema1}: {average_fitness1}")
        print(f"Average fitness of schema 2 {schema2}: {average_fitness2}")
        print()


def generate_population(schema: str, k: int) -> list:
    assert len(schema) == k, "Schema length must be equal to k"

    population = []
    schema_list = []
    schema_list = string_to_list(schema)
    schema_list_z = schema_list.copy()
    schema_list_o = schema_list.copy()

    if '*' in schema_list:
        for i, dig in enumerate(schema_list):
            if dig == '*':
                schema_list_z[i] = '0'
                schema_str = ''.join(schema_list_z)
                population += generate_population(schema_str, k)

                schema_list_o[i] = '1'
                schema_str = ''.join(schema_list_o)
                population += generate_population(schema_str, k)
    else:
        population.append(schema)

    return list(dict.fromkeys(population))


def string_to_list(string):
    list1 = []
    list1[:0] = string
    return list1


def average_fitness(population: list, k: int) -> float:
    sum = 0
    for schema in population:
        bin_sum = binary_dig_sum(schema)
        sum += ga_cost_func(k, bin_sum)

    return sum / len(population)


# Compute the sum of digits of a binary number
def binary_dig_sum(bin: int) -> int:
    sum = 0
    bin_str = str(bin)  # Convert to string
    for dig in bin_str:
        sum += int(dig)

    return sum


# Cost function of the genetic algorithm
def ga_cost_func(k: int, bin_sum: int) -> int:
    if bin_sum == k:
        return k
    else:
        return k - 1 - bin_sum


if __name__ == "__main__":
    main()
