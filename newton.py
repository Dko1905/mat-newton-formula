# Calculate future numbers using Newtons formula.

def diff(a, b):
	if a > b:
		return a - b
	else:
		return b - a

def calc(input, n):
	t = input[0] + input[1] * n
	for x in range(len(input) - 2):
		div = 1
		for y in range(x + 1):
			div *= y + 2
		top = input[x + 2] * n
		for y in range(x, 1):
			top *= n - (y + 1)
		t += top/div
	return t

def calc_tree(input):
	output = []
	output.append(input[0])
	for i in range(len(input) - 1):
		for x in range(len(input) - 1 - i):
			input[x] = diff(input[x + 1], input[x])
		output.append(input[0])
	return output

def main():
	input_array = input("Enter array of the numbers in one line, without spaces. (0,1,2,3): ").split(',')
	input_array = [int(numeric_string) for numeric_string in input_array]
	input_variables = calc_tree(input_array)
	print("Calculated variables are", input_variables)
	n = int(input("Please write the number you want to get. (n): "))
	result = calc(input_variables, n)
	print("Result is ", n)

if __name__ == "__main__":
	main()
