from functools import lru_cache


@lru_cache
def calculate_fuel(mass):
    return (mass // 3) - 2


def calculate_fuel_recursive(mass):
    subfuel = 0
    while (fuel := calculate_fuel(mass)) > 0:
        subfuel += fuel
        mass = fuel
    return subfuel


def part1(lines):
    modules = [int(line.strip()) for line in lines if line.strip()]
    total_fuel = sum(calculate_fuel(mass) for mass in modules)
    print("[part 1] Total fuel:", total_fuel)


def part2(lines):
    modules = [int(line.strip()) for line in lines if line.strip()]
    total_fuel = sum(calculate_fuel_recursive(mass) for mass in modules)
    print("[part 2] Total fuel:", total_fuel)
