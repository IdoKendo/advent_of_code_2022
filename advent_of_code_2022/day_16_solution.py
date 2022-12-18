import itertools
from dataclasses import dataclass

import networkx as nx
from advent_of_code_2022.common import read_input


@dataclass(frozen=True, eq=True)
class Valve:
    room_name: str
    flow_rate: int
    rooms: str


def parse_input_to_valves(input_file_path: str) -> dict[str, Valve]:
    valves = {}
    for line in read_input(input_file_path):
        match line.split():
            case ["Valve", room_name, "has", "flow", rate, "tunnel", "leads", "to", "valve", next_room]:
                valves[room_name] = Valve(
                    room_name=room_name,
                    flow_rate=int(rate.split("=")[-1].replace(";", "")),
                    rooms=next_room,
                )
            case ["Valve", room_name, "has", "flow", rate, "tunnels", "lead", "to", "valves", *next_rooms]:
                valves[room_name] = Valve(
                    room_name=room_name,
                    flow_rate=int(rate.split("=")[-1].replace(";", "")),
                    rooms="".join(r.strip() for r in next_rooms),
                )
            case _:
                pass
    return valves


def turn_off_valves(
    start: Valve,
    valves_to_turn: set[Valve],
    shortest_paths: dict[tuple[str, str], int],
    time_passed: int = 0,
    rate: int = 0,
    flow: int = 0,
    path: list[str] | None = None,
    time_left: int = 30,
    paths: list[tuple[list[str], int]] | None = None,
) -> None:
    if len(valves_to_turn) == 0:
        flow += (time_left - time_passed) * rate
        paths.append((path, flow))
        return
    for valve in valves_to_turn:
        new_time = shortest_paths.get((start.room_name, valve.room_name), 0) + 1
        if new_time == 1 or time_passed + new_time > time_left:
            new_flow = (time_left - time_passed) * rate
            paths.append((path, flow + new_flow))
            continue
        new_flow = rate * new_time
        turn_off_valves(
            valve,
            valves_to_turn=valves_to_turn - {valve},
            shortest_paths=shortest_paths,
            time_passed=time_passed + new_time,
            rate=rate + valve.flow_rate,
            flow=flow + new_flow,
            path=path + [valve.room_name],
            time_left=time_left,
            paths=paths,
        )


def find_most_pressure_released(
    input_file_path: str = "input.txt", num_of_workers: int = 1, time_left: int = 30
) -> int:
    valves = parse_input_to_valves(input_file_path)
    graph = nx.Graph()
    edges = []
    for source, valve in valves.items():
        for destination in valve.rooms.split(","):
            edges.append((source, destination))
    graph.add_edges_from(edges)
    shortest_paths = {}
    for source, destination in itertools.product(valves.keys(), valves.keys()):
        if source == destination:
            continue
        shortest_paths[(source, destination)] = len(nx.shortest_path(graph, source, destination)) - 1
    valves_to_turn = {valve for valve in valves.values() if valve.flow_rate != 0}
    max_flow = 0
    if num_of_workers == 1:
        paths = []
        turn_off_valves(valves["AA"], valves_to_turn, shortest_paths, path=[], time_left=time_left, paths=paths)
        max_flow = max(p[1] for p in paths)
    if num_of_workers == 2:
        max_flow = 0
        for idx in range(len(valves)):
            for combination in itertools.combinations(valves_to_turn, idx):
                valves_1 = set(combination)
                valves_2 = valves_to_turn - valves_1
                paths = []
                turn_off_valves(valves["AA"], valves_1, shortest_paths, path=[], time_left=time_left, paths=paths)
                best_1 = max(p[1] for p in paths)
                paths = []
                turn_off_valves(valves["AA"], valves_2, shortest_paths, path=[], time_left=time_left, paths=paths)
                best_2 = max(p[1] for p in paths)
                if best_1 + best_2 > max_flow:
                    max_flow = best_1 + best_2
    return max_flow


def main():
    print(find_most_pressure_released())
    print(find_most_pressure_released(num_of_workers=2, time_left=26))


if __name__ == "__main__":
    main()
