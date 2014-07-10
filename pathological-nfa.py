import sys
from luther.regex import RegularExpression

n = int(sys.argv[1])
text = "a" * n
regex = "a?" * n
regex += "a" * n

r = RegularExpression(regex)
nfa = r.to_nfa()

for character in text:
    nfa.transition(character)

assert nfa.accepting
