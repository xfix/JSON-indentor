#!/usr/bin/python2
with open("raw.txt") as input_file:
    text = input_file.read()
istack = []
str_length = 0
indent = 0
current_string = ""
text = text.replace("\n{", "{")
for char in text:
    if char == '\n':
        print current_string
        current_string = " " * indent
        str_length = 0
    elif not (char == '{' or char == '}' or char == '[' or char == ']' or char == ','):
        str_length += 1
        current_string += char
    elif char == '}' or char == ']':
        print current_string
        current_string = " " * indent
        print current_string + char
        indent = istack.pop()
        current_string = " " * indent
        str_length = 0
    elif char == '{' or char == '[':
        istack.append(indent)
        indent = str_length + istack[-1]
        print current_string + char
        current_string = " " * indent
        str_length = 0
    elif char == ',':
        print current_string + char
        current_string = " " * indent
        str_length = 0
