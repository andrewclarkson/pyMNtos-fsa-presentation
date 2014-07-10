import re
import sys

n = sys.argv[1]

text = "a" * int(n)
regex = "(a?){n}a{n}".replace("n", n)

r = re.compile(regex)
r.match(text)
