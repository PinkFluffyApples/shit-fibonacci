import sys

# setting to 0 = infinite max digits, meaning you can get even more massive numbers (default is 4900 max digits)
sys.set_int_max_str_digits(0)

def dataTrimming(word):
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

print("======SAIF'S SHIT FIB VALUE THING======\n")
mode = input("single value query or multi-value query? s/m: ")
while mode.lower() != "m" and mode.lower() != "s":
	print("not accepted.")
	mode = input("single value query or multi-value query? s/m: ")

match mode.lower():
	case "m":
		with open("fib-values-multi.txt", "w") as file:
			LIST_RANGE = int(input("enter highest index required: "))
			for i in range(LIST_RANGE):
				index = i + 1
				fileEntry = (index, fib_output(i))
				file.write(dataTrimming(str(fileEntry)) + '\n')
				print(index)
	case "s":
		with open("fib-values-single.txt", "w") as file:
			query = int(input("enter query: "))
			fileEntry = (fib_output(query))
			file.write(dataTrimming(str(fileEntry)) + '\n')

print("======FILE GENERATED======")