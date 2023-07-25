import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
s = stack.Stack()

for char in string:
     s.push(char)

rev = ""
while not s.is_empty():
     rev += s.pop()
     
print(rev)