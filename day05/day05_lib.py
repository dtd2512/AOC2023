import re

class SeedChain:
    def __init__(self, seed, soil, fertilizer, water, light, temperature, humidity, location):
        self.seed = seed
        self.soil = soil
        self.fertilizer = fertilizer
        self.water = water
        self.light = light
        self.temperature = temperature
        self.humidity = humidity
        self.location = location

    def __str__(self):
        return "{0},{1},{2},{3},{4},{5},{6},{7}".format(self.seed, self.soil, self.fertilizer, self.water, self.light, self.temperature, self.humidity, self.location)
    

def build_seed_chain(seed_num: int, S2S, S2F, F2W, W2L, L2T, T2H, H2L: dict):
    seed = seed_num
    soil = get_map(seed, S2S)
    fertilizer = get_map(soil, S2F)
    water = get_map(fertilizer, F2W)
    light = get_map(water, W2L)
    temperature = get_map(light, L2T)
    humidity = get_map(temperature, T2H)
    location = get_map(humidity, H2L)
    return SeedChain(seed, soil, fertilizer, water, light, temperature, humidity, location)


def parse_input(input_filepath: str):
    with open(input_filepath) as file:
        lines = file.read()
    tokens = lines.split("\n\n")
    if len(tokens) != 8: return None

    seeds = parse_seeds(tokens[0])
    s2s = parse_maps(tokens[1])
    s2f = parse_maps(tokens[2])
    f2w = parse_maps(tokens[3])
    w2l = parse_maps(tokens[4])
    l2t = parse_maps(tokens[5])
    t2h = parse_maps(tokens[6])
    h2l = parse_maps(tokens[7])

    return seeds, s2s, s2f, f2w, w2l, l2t, t2h, h2l


def parse_seeds(input: str):
    return list(map(int, re.findall(r'\d+', input)))


def parse_maps(input: str):
    nums = list(map(int, re.findall(r'\d+', input)))
    if len(nums) % 3 !=0: return None
    chunks = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
    return chunks(nums, 3)


def get_map(k: int, maps: [[int]]):
    v = k
    for m in maps:
        if m[1] <= k and k < m[1] + m[2]: 
            v = m[0] + k - m[1]
            break
    return v