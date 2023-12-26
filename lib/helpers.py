import sys
import os
import time
from contextlib import contextmanager



@contextmanager
def timeit(verbose=True):
	print("Begun:     " + time.strftime("%I:%M:%S %p"))
	start = time.monotonic()
	try:
		yield
	except: # KeyboardInterrupt:
		pass
	stop = time.monotonic()
	print("Ended:     " + time.strftime("%I:%M:%S %p"))
	elapsed = time.strftime('%H:%M:%S', time.gmtime(stop - start))
	print("Run Time:  " + elapsed)



##################################################################################################



short_time_fmt = '%I:%M:%S %p'
long_time_fmt  = '%I:%M:%S %p (%b %d, %Y)'


class ProgressBar:

	def __init__(self, max_ticks, width = 50):
		self.ticks       = 0
		self.max_ticks   = max_ticks
		self.width       = width
		self.print_width = 0

	def is_done(self):
		return self.ticks == self.max_ticks

	def tick(self):
		if self.is_done():
			return
		self.ticks += 1
		self.print()
		if self.ticks == self.max_ticks:
			print()

	def finish(self):
		if self.is_done():
			return
		self.ticks = self.max_ticks - 1
		self.tick()

	def print(self):
		p = lambda s: print(s, end = "", flush = True)

		p("\b" * self.print_width)

		percent          = int(self.ticks / self.max_ticks * 100)
		bar_len          = int(self.ticks / self.max_ticks * self.width)
		info             = "█" * bar_len + "░" * (self.width - bar_len)
		info            += f" {percent}% ({self.ticks}/{self.max_ticks})"
		info            += f" {time.strftime(short_time_fmt)}"
		self.print_width = len(info)

		p(info)

def tick(max_ticks, _pb = []):
	if len(_pb) == 0:
		_pb.append(ProgressBar(max_ticks))
	_pb[0].tick()
	if _pb[0].is_done():
		_pb.pop()



##################################################################################################



class Memory:
	'''
	A collection of useful methods for getting and printing total memory usage of the running python process. In addition, the current memory usage will be printed right before the program exits.
	'''
	def __init__(self):
		import atexit
		import psutil
		self.mem_usage = []
		atexit.register(print_mem_usage)

	def get_mem_usage(self):
		'''Get memory usage in MB.'''
		process = psutil.Process(os.getpid())
		mem     = int(process.memory_info().rss / 1000**2) # in MB
		return mem

	def snapshot(self):
		'''Record the current memory usage for end-of-program statistics.'''
		self.mem_usage.append(get_mem_usage())

	def print_mem_usage(self):
		'''Prints summary of memory usage just before program exits.'''
		print("~~~~~~~~~~~~")
		print("Memory usage")
		if len(self.mem_usage) > 0:
			print(f"Max    : {int(max(self.mem_usage))               } MB")
			print(f"Average: {int(sum(self.mem_usage)/len(mem_usage))} MB")
		print(f"At exit: {    int(self.get_mem_usage())              } MB")



##################################################################################################



@contextmanager
def do_print(verbose=True):
	'''Toggle printing to the console.'''
	if verbose:
		yield
	else:
		old_stdout = sys.stdout
		sys.stdout = open(os.devnull, "w")
		yield
		sys.stdout = old_stdout

def log(message, **kwargs):
	'''
	Logs a message to _log.txt in cwd (creating it if it doesn't exist). Pass the named parameter shutdown = True to shutdown the computer after logging the message.
	'''
	try:
		message = str(message) + "\n\n"
		with open("_log.txt", "a+") as f:
			f.write(f"<{time.strftime(long_time_fmt)}>\n")
			f.write(message)

		if kwargs["shutdown"] == True:
			shutdown()
	except:
		pass

def shutdown():
	'''Shutdown the computer.'''
	if os.name == "nt": # windows
		os.system("shutdown /s /f /t 0")
	else:
		os.system("shutdown -t now")



##################################################################################################



# use functools.cache instead
"""
def memoize(func, hash_func = lambda *x: tuple(x)):
	'''
	Convenient wrapper to make any function memoized (including recursive functions).
	hash_func describes how to make a dictionary key from the args given to func.
	This is useful when func is normally given unhashable args, like lists and other collections.
	'''
	m = {}
	def _memo(*args):
		try:
			return m[hash_func(*args)]
		except KeyError:
			f = func(*args)
			m[hash_func(*args)] = f
			return f
		except RecursionError:
			print("RecursionError in memoized function.")
			sys.exit(1)
	return _memo
"""