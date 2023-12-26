import day20_lib as lib
from day20_lib import ModuleType
from collections import deque

INPUT_FILENAME = "input_20.txt"

def count_pulses(modules: dict):
    num_low = 0
    num_high = 0
    for _ in range(1000):
        num_low += 1
        queue = deque([("broadcaster", d, 0) for d in modules["broadcaster"].dests])
        while queue:
            s, d, p = queue.popleft()
            if p: num_high += 1
            else: num_low += 1
            if d not in modules: continue

            module = modules[d]
            if module.type == ModuleType.FLIPFLOP:
                if p: continue
                module.mem = not module.mem
                out_p = module.mem
            else:
                module.mem[s] = p
                out_p = not all(module.mem.values())
            for _d in module.dests:
                queue.append((module.name, _d, out_p))
    return num_low, num_high

def main():
    modules = lib.parse_input(INPUT_FILENAME)
    num_low, num_high = count_pulses(modules)
    print("Result: ", num_low*num_high)

if __name__ == "__main__":
    main()