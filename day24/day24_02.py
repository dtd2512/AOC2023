import day24_lib as lib
import z3 

INPUT_FILENAME = "input_24.txt"

def find_rock_xyzv(note: tuple):
    x, y, z, vx, vy, vz = z3.Reals("x y z vx vy vz")
    solver = z3.Solver()
    for i in range(3):
        t = z3.Real(f"t{i}")
        p,v = note[i]
        solver.add(x + t * vx == p[0] + v[0] * t)
        solver.add(y + t * vy == p[1] + v[1] * t)
        solver.add(z + t * vz == p[2] + v[2] * t)
    solver.check()
    return sum(solver.model()[xyz].as_long() for xyz in [x, y, z])

def main():
    note = lib.parse_input(INPUT_FILENAME)
    print("Sum xyz: ", find_rock_xyzv(note))

if __name__ == "__main__":
    main()