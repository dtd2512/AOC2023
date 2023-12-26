import os
from enum import Enum
from functools import reduce
from math import gcd

class ModuleType(Enum):
    FLIPFLOP = "%"
    CONJUCTION = "&"
    BROADCASTER = "broadcaster"

class PulseType(Enum):
    LOW = 0
    HIGH = 1

class Module:
    def __init__(self, name, type, dests):
        self.name = name
        self.type = type
        self.dests = dests
        self.mem = False if self.type == ModuleType.FLIPFLOP else {}

    def __str__(self):
        return "%s%s%s:%s"%(self.name, self.type, self.dests, self.mem)

def init_conjuction(modules: dict):
    for name, module in modules.items():
        for dest in module.dests:
            if dest in modules and modules[dest].type == ModuleType.CONJUCTION:
                modules[dest].mem[name] = PulseType.LOW
    return modules

def parse_input(input_filename: str):
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, input_filename)
    modules = {}
    with open(input_filepath) as file:
        for line in file.readlines():
            name, dests = line.rstrip().split(" -> ")
            dests = [d for d in dests.split(", ")]
            if name == "broadcaster": 
                type = ModuleType.BROADCASTER
            else:
                type = ModuleType(name[0])
                name = name[1:]
            modules[name] = Module(name, type, dests)
    return init_conjuction(modules)

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)