# String Operations

# 1) String Concatenation
# 2) String Repetition
# 3) Indexing
# 4) Slicing
# 5) Membership


# String

a = 'Codegnan'
a
# 'Codegnan'

a = 'Python'
b = 'Programming'

a + b
# 'PythonProgramming'

type(a)
# <class 'str'>


# 1) String Concatenation

a = 'Python'
b = 'Programming'

a + b
# 'PythonProgramming'

fname = 'vishnu'
lname = 'priya'

fname + lname
# 'vishnupriya'


# 2) String Repetition

'a' * 10
# 'aaaaaaaaaa'

'-codegnan-' * 10
# '-codegnan--codegnan--codegnan--codegnan--codegnan--codegnan--codegnan--codegnan--codegnan--codegnan-'


# 3) Indexing
# Indexing means accessing a particular character.

s = 'codegnan'

s[0]
# 'c'

s[-1]
# 'n'

s[4]
# 'g'


# 4) String Slicing
# Slicing means accessing a group of characters.

names = 'lakshmi vishnupriya sadhana'

names[:]
# 'lakshmi vishnupriya sadhana'

names[:7]
# 'lakshmi'

names[8:19]
# 'vishnupriya'

names[20:27]
# 'sadhana'

names[0:]
# 'lakshmi vishnupriya sadhana'

names[-1:]
# 'a'

names[-1::]
# 'a'

names[-1:-1]
# ''

names[::-1]
# 'anahdas ayirpunhsiv imhskal'

names[-1:-8]
# ''

names[-1:-8:-1]
# 'anahdas'


# 5) Membership Operators
# in, not in

'a' in names
# True

'vishnupriya' not in names
# False

'z' not in names
# True


# Built-in Functions

len(names)
# 27

ord('a')
# 97

ord('A')
# 65

chr(10)
# '\n'

chr(100)
# 'd'

max(names)
# 'y'

min(names)
# ' '

sorted(names)
# [' ', ' ', 'a', 'a', 'a', 'a', 'a', 'd', 'h',
#  'h', 'h', 'i', 'i', 'i', 'k', 'l', 'm', 'n',
#  'n', 'p', 'r', 's', 's', 's', 'u', 'v', 'y']


# Case Conversion Methods

s = "Python Programming language"

s.upper()
# 'PYTHON PROGRAMMING LANGUAGE'

s.lower()
# 'python programming language'

s.title()
# 'Python Programming Language'

s.swapcase()
# 'pYTHON pROGRAMMING LANGUAGE'

s.capitalize()
# 'Python programming language'

"Víßhñú".casefold()
# 'vísshñú'


# Alignment Methods

s.center(50, '-')
# '-----------Python Programming language------------'

s.center(20, '*')
# 'Python Programming language'

s.center(30, '*')
# '*Python Programming language**'

s.ljust(50, '-')
# 'Python Programming language-----------------------'

s.rjust(50, '-')
# '-----------------------Python Programming language'

'23'.zfill(4)
# '0023'

'123456'.zfill(2)
# '123456'

'8'.zfill(4)
# '0008'


# Searching Methods

s = 'python programming language'

s.find('p')
# 0

s.rfind('p')
# 7

s.index('p')
# 0

s.rindex('p')
# 7

s.find('z')
# -1

s.count('a')
# 3

s.count('p')
# 2


# Replace Method

s.replace('p', '1')
# '1ython 1rogramming language'

s.replace('m', '2')
# 'python progra22ing language'


# Translation Methods

s.maketrans('aeiou', '#$@*&')
# {97: 35, 101: 36, 105: 64, 111: 42, 117: 38}

s.translate(s.maketrans('aeiou', '#$@*&'))
# 'pyth*n pr*gr#mm@ng l#ng&#g$'


# Encoding and Decoding

text = "Hello"

text.encode()
# b'Hello'

b'Hello'.decode()
# 'Hello'
