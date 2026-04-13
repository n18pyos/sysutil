import psutil

info = "ps - программа для просмотра процессов\n"

def start_module(args):
	for prc in psutil.process_iter(["pid", "name"]):
		try:
			print(f"PID: {data['pid']:<8}   Name: {data['name']}")
		except:
			pass
