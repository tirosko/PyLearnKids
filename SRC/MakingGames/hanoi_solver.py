
#!/usr/bin/env python3
"""Hanoi Tower solver — text mode.

Usage:
	python SRC/MakingGames/hanoi_solver.py N
Example:
	python SRC/MakingGames/hanoi_solver.py 3
Prints initial state like [3,2,1][][] and moves until [][][3,2,1]
"""

import argparse

labels = ["A", "B", "C"]

def print_pegs(pegs):
	def fmt(peg):
		return "[" + ",".join(map(str, peg)) + "]" if peg else "[]"
	print(fmt(pegs[0]) + fmt(pegs[1]) + fmt(pegs[2]))

moves_count = 0

def move(n, src, dst, aux, pegs):
	global moves_count
	if n == 0:
		return
	move(n-1, src, aux, dst, pegs)
	disk = pegs[src].pop()
	pegs[dst].append(disk)
	moves_count += 1
	print(f"Move {moves_count}: disk {disk} from {labels[src]} to {labels[dst]}")
	print_pegs(pegs)
	move(n-1, aux, dst, src, pegs)

def solve(n, start=0, target=2):
	global moves_count
	moves_count = 0
	pegs = [list(range(n, 0, -1)), [], []]
	print("Initial:")
	print_pegs(pegs)
	move(n, start, target, 3 - start - target, pegs)
	print(f"Done. Total moves: {moves_count}")

def parse_args():
	p = argparse.ArgumentParser(description="Hanoi Tower solver (text mode)")
	p.add_argument("n", nargs='?', type=int, default=3, help="number of disks (default 3)")
	return p.parse_args()

if __name__ == "__main__":
	args = parse_args()
	solve(args.n)

