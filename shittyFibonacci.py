import sys
import time

# setting to 0 = infinite max digits, meaning you can get even more massive numbers (default is 4900 max digits)
sys.set_int_max_str_digits(0)

def wordTrimming(word):
	temp = word.replace(word[0], '')
	output = temp.replace(word[len(word)-1], '')
	return output

def fibonacci(n):
	if n == 0:
		return 0, 1
	else:
		a, b = fibonacci(n // 2)
		c = a * (b * 2 - a)
		d = a * a + b * b
		if n % 2 == 0:
			return c, d
		else:
			return d, c + d
def fib_output(n):
	return fibonacci(n)[0]

print("========================================")

mode = input("single value query or multi-value query? s/m: ")
while mode.lower() != "m" and mode.lower() != "s":
	print("not accepted.")
	mode = input("single-value query or multi-value query? s/m: ")

match mode.lower():
	case "m":
		initialTime = time.time()
		with open("fib-values-multi.txt", "w") as f:
			listRange = int(input("enter index limit: "))
			for i in range(listRange):
				val = wordTrimming(str((i + 1, fib_output(i))))
				fileEntry = '\n' + val
				f.write(fileEntry)
	case "s":
		initialTime = time.time()
		with open("fib-values-single.txt", "w") as file:
			query = int(input("enter query: "))
			fileEntry = (fib_output(query))
			file.write(wordTrimming(str(fileEntry)))

duration = time.time() - initialTime
print("==============FILE GENERATED=============")
print(f" Duration: {duration}s")