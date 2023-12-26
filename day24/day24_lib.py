import os

def parse_input(input_filename: str):
    base_path = os.path.abspath(os.path.dirname(__file__))
    input_filepath = os.path.join(base_path, input_filename)
    note = []
    with open(input_filepath) as file:
        for line in file:
            tokens = line.rstrip().split("@")
            p = tuple(map(int, tokens[0].split(", ")))
            v = tuple(map(int, tokens[1].split(", ")))
            note.append((p,v))
    return tuple(note)

# Direction Vector = (a,b) -> Normal Vector = (b,-a)
# Line passes through point (x0,y0)
# -> Linear_equation b(x-x0)-a(y-y0) = 0 <-> bx - ay + (ay0-bx0) = 0
def build_linear_equation(p, v: tuple):
    a = v[0]; b = v[1]
    x0 = p[0]; y0 = p[1]
    return (b, -a, a*y0-b*x0)