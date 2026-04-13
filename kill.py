import os
import signal

info = "kill - программа для принудительного завершения процесса\nkill pid/self\n"

def start_module(args):
	if args[0] == "self":
		print("killing self...")
		os.kill(os.getpid(), signal.SIGKILL)
	else:
		os.kill(int(args[0]), signal.SIGKILL)
