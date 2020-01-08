import re

string = 'The first set of parentheses in a regex string will be group 1. The second set will be group 2. By passing the integer 1 or 2 to the group() match object method, you can grab different parts of the matched text. Passing 0 or nothing to the group() method will return the entire matched text. Enter the following into the interactive shell:'

regexcomp = re.compile(r'\d')


mo = regexcomp.findall(string)

print(mo)


'''>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
>>> mo = phoneNumRegex.search('My number is 415-555-4242.')
>>> print('Phone number found: ' + mo.group())
Phone number found: 415-555-4242 

Import the regex module with import re.

Create a Regex object with the re.compile() function. (Remember to use a raw string.)

Pass the string you want to search into the Regex object’s search() method. This returns a Match object.

Call the Match object’s group() method to return a string of the actual matched text.

'''