import sys
import os
import time

def get_file(prefix):
	try:
		files = [f for f in os.listdir(".") if f[-3:] == ".py" and f != "000_main.py"]
		if prefix == "":
			# get most recently changed file
			return sorted((os.path.getmtime(f),f) for f in files)[-1][1]
		else:
			# get first file that matches prefix
			prefix = prefix.zfill(3)
			for file in files:
				if file.startswith(prefix):
					return file
	except:
		pass
	return None

def run(args):
	file = args[0]
	args = " ".join(args[1:])
	print()
	print(time.strftime("%I:%M:%S %p"))
	print(file)
	print("-" * len(file))
	print()
	start = time.monotonic()
	try:
		success = False
		success = os.system(f"python {file} {args}") == 0
	except KeyboardInterrupt:
		pass
	stop = time.monotonic()
	elapsed = time.strftime('%H:%M:%S', time.gmtime(stop - start))
	print()
	print("-" * len(file))
	print(f"Completion time: {elapsed}")
	print()
	return success

def main_loop():
	while True:
		# get input
		args = input("Enter a problem number: ")
		if args.lower() in ["quit", "exit", "qqq"]:
			break
		args = args.split(" ")
		file = get_file(args[0])
		# run
		if file is None:
			print("File not found.")
		else:
			args[0] = file
			while not run(args):
				if input("Retry? [Y/n]").lower() == 'n':
					break

if __name__ == "__main__":
	try:
		main_loop()
	except (EOFError, KeyboardInterrupt):
		pass
