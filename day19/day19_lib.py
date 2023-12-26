import os
import re
from operator import gt, lt

OPERATORS = {"<": lt, ">": gt}

class Condition:
    def __init__(self, key=None, comparsion=None, value=None, target=None):
        self.key = key
        self.comparsion = comparsion
        self.value = value
        self.target = target
        self.simple = False if key else True

    def __str__(self):
        return "%s%s%s:%s"%(self.key, self.comparsion, self.value, self.target) if self.simple else self.target

def build_ratings(s_ratings: str):
    reg = lambda s: tuple(map(int, re.findall(r'[0-9]+', s)))
    ratings = []
    for s_rating in s_ratings:
        m = reg(s_rating)
        ratings.append({"x": m[0], "m": m[1], "a": m[2], "s": m[3]})
    return ratings

def build_workflows(s_workflows: list):
    workflows = {}
    for s_workflow in s_workflows:
        rules = []
        tokens = s_workflow.split("{")
        name = tokens[0]
        for rule in tokens[1][:-1].split(","):
            if re.match(r'\w+(<|>)\w+:\w+', rule):
                condition, target = rule.split(":")
                key, comparsion, *value = tuple(condition)
                rules.append(Condition(key, comparsion, int("".join(value)), target))
            else:
                rules.append((Condition(target=rule)))
        workflows[name] = rules
    return workflows

def parse_input(input_filename: str):
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, input_filename)
    with open(input_filepath) as file:
        tokens = file.read().split("\n\n")
        return build_workflows(tokens[0].split()), build_ratings(tokens[1].split())