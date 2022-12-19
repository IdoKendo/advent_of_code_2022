import re
from dataclasses import dataclass

import numpy as np
from advent_of_code_2022.common import read_input


@dataclass
class Recipe:
    ore: int
    clay: int
    obsidian: int


@dataclass
class Blueprint:
    number: int
    ore_recipe: Recipe
    clay_recipe: Recipe
    obsidian_recipe: Recipe
    geode_recipe: Recipe

    @property
    def array(self) -> np.array:
        return np.array(
            (
                (self.ore_recipe.ore, self.ore_recipe.clay, self.ore_recipe.obsidian, 0),
                (self.clay_recipe.ore, self.clay_recipe.clay, self.clay_recipe.obsidian, 0),
                (self.obsidian_recipe.ore, self.obsidian_recipe.clay, self.obsidian_recipe.obsidian, 0),
                (self.geode_recipe.ore, self.geode_recipe.clay, self.geode_recipe.obsidian, 0),
            )
        )


def parse_input_to_blueprints(input_file_path: str) -> list[Blueprint]:
    lines = read_input(input_file_path)
    blueprints = []
    for line in lines:
        if not line:
            continue
        nums = list(map(int, re.findall(r"\d+", line)))
        blueprints.append(
            Blueprint(
                number=nums[0],
                ore_recipe=Recipe(ore=nums[1], clay=0, obsidian=0),
                clay_recipe=Recipe(ore=nums[2], clay=0, obsidian=0),
                obsidian_recipe=Recipe(ore=nums[3], clay=nums[4], obsidian=0),
                geode_recipe=Recipe(ore=nums[5], clay=0, obsidian=nums[6]),
            )
        )
    return blueprints


def prune_states(states: np.array, max_costs: list[int], time_left: int) -> np.array:
    states = states.copy()
    for state in states:
        for idx in range(3):
            deficit = max_costs[idx] - state[idx]
            max_useful_quantity = max_costs[idx] + deficit * time_left
            if state[idx + 4] >= max_useful_quantity:
                state[idx + 4] = max_useful_quantity

    for idx in range(7, -1, -1):
        indices = np.argsort(states[:, idx], kind="stable")
        states = states[indices]

    new_states = np.zeros(states.shape, dtype=states.dtype)
    n = 0

    for idx in range(len(states)):
        redundant = np.any(np.all(states[idx] <= states[idx + 1 :], axis=1))  # noqa: E203
        if not redundant:
            new_states[n] = states[idx]
            n += 1

    return new_states[:n]


def mine_geodes(blueprint: np.array, time_limit: int) -> int:
    max_costs = [max(blueprint[i, j] for i in range(4)) for j in range(4)]
    states = np.zeros([1, 8], dtype=np.uint32)
    states[0, 0] = 1

    for minutes_passed in range(time_limit):
        new_states = np.zeros([0, 8], dtype=np.uint32)
        for state in states:
            robots = state[:4]
            resources = state[4:]
            state_size = len(new_states)
            new_states = np.resize(new_states, (state_size + 1, 8))
            new_states[state_size] = np.append(robots, resources + robots)
            for idx, robot_cost in enumerate(blueprint):
                if idx < 3 and robots[idx] >= max_costs[idx]:
                    continue
                if np.all(resources >= robot_cost):
                    new_robots = robots.copy()
                    new_robots[idx] += 1
                    new_resources = resources + robots - robot_cost
                    state_size = len(new_states)
                    new_states = np.resize(new_states, (state_size + 1, 8))
                    new_states[state_size] = np.append(new_robots, new_resources)
        states = prune_states(new_states, max_costs, time_limit - minutes_passed - 1)

    return max(states[:, 7])


def calculate_blueprints_quality_level(
    input_file_path: str = "input.txt", time_limit: int = 24, blueprints_count: int = 0
) -> int:
    blueprints = parse_input_to_blueprints(input_file_path)
    if blueprints_count > 0:
        blueprints = blueprints[:blueprints_count]
    quality = []
    for blueprint in blueprints:
        geode_count = mine_geodes(blueprint.array, time_limit=time_limit)
        if not blueprints_count:
            quality.append(geode_count * blueprint.number)
        else:
            quality.append(geode_count)
    result = np.product(quality) if blueprints_count else sum(quality)
    return result


def main():
    print(calculate_blueprints_quality_level())
    print(calculate_blueprints_quality_level(time_limit=32, blueprints_count=3))


if __name__ == "__main__":
    main()
