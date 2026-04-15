import psutil

info = "ps - программа для просмотра процессов\n"

def start_module(args):
	for prc in psutil.process_iter(["pid", "name"]):
		try:
			info = prc.as_dict(attrs=["pid", "name"])
			print(f"PID: {info['pid']:<8}   Name: {info['name']}")
		except:
			pass
