'''Write a Python class to find validity of a string of parentheses, '(', ')',
'{', '}', '[' and ']. These brackets must be close in the correct order, for
example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid'''
class BracketValidator:
    def __init__(self, input_string):
        self.input_string = input_string
    def is_valid(self):
        stack = []
        for char in self.input_string:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if not stack:
                    return False
                current_char = stack.pop()
                if current_char == "(":
                    if char != ")":
                        return False
                    if current_char == "{":
                        if char != "}":
                            return False
                    if current_char == "[":
                        if char != "]":
                            return False
        if stack:
            return False
        return True


