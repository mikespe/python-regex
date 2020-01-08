import re

string = 'The first set of parentheses in a regex string will be group 1. The second set will be group 2. By passing the integer 1 or 2 to the group() match object method, you can grab different parts of the matched text. Passing 0 or nothing to the group() method will return the entire matched text. Enter the following into the interactive shell:'

regexcomp = re.compile(r'\d')


mo = regexcomp.findall(string)

print(mo)
