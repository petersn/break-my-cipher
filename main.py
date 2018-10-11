#!/usr/bin/python

import argparse
import lark

with open("grammar.txt") as f:
	parser = lark.Lark(f.read(), start="main")

def main(args):
	with open(args.input_cipher) as f:
		text = f.read()
	print text
	ast = parser.parse(text)
	print ast.pretty()

argument_parser = argparse.ArgumentParser()
argument_parser.add_argument("input_cipher", metavar="input.cipher")

if __name__ == "__main__":
	args = argument_parser.parse_args()
	main(args)

