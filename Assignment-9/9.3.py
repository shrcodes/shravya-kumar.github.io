'''A balanced delimiter starts with an opening character ((, [, {), ends with a matching closing character (), ], } respectively), and has only other matching delimiters in between.
Input is provided as a single string. Your output should be True or False according to whether the string is balanced.'''
def areBracketsBalanced(expr):
	stack = []

	# Traversing the Expression
	for char in expr:
		if char in ["(", "{", "["]:

			# Push the element in the stack
			stack.append(char)
		else:

			if not stack:
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return False
			if current_char == '{':
				if char != "}":
					return False
			if current_char == '[':
				if char != "]":
					return False
	if stack:
		return False
	return True

if __name__ == "__main__":
	expr = "([)]"

	# Function call
	if areBracketsBalanced(expr):
		print("True")
	else:
		print("False")
