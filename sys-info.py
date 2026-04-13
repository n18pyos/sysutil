import os
import toml

info = "sys-info - программа для показа архитектуры\n"

def start_module(args):
	op = open(os.environ.get("SYS_INFO_PATH"), "r")
	t = toml.load(op)
	print("\n")
	print(toml.dumps(t))
	print("\n")
