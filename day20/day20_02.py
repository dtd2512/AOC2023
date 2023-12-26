import day20_lib as lib
from day20_lib import ModuleType
from collections import deque

INPUT_FILENAME = "input_20.txt"

def count_num_presses(modules: dict):
    to_rx = next(iter([name for name, module in modules.items() if "rx" in module.dests]))
    seen = {name: False for name, module in modules.items() if to_rx in module.dests}
    cycles = {}
    count = 0
    while True:
        count += 1
        queue = deque([("broadcaster", d, 0) for d in modules["broadcaster"].dests])
        while queue:
            s, d, p = queue.popleft()
            if d not in modules: continue

            module = modules[d]
            if module.name == to_rx and p == 1:
                seen[s] = not seen[s]
                if s not in cycles: cycles[s] = count
                if all(seen.values()): return lib.lcm(cycles.values())

            if module.type == ModuleType.FLIPFLOP:
                if p: continue
                module.mem = not module.mem
                out_p = module.mem
            else:
                module.mem[s] = p
                out_p = not all(_p == 1 for _p in module.mem.values())
            for dest in module.dests:
                queue.append((module.name, dest, out_p))

def main():
    modules = lib.parse_input(INPUT_FILENAME)
    print("Result: ", count_num_presses(modules))

if __name__ == "__main__":
    main()