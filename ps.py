import psutil

info = "ps - программа для просмотра процессов\n"

def start_module(args):
	for prc in psutil.process_iter(["pid", "name"]):
		try:
			print(f"PID: {prc['pid']:<8}   Name: {prc['name']}")
		except:
			pass
