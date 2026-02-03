"""
Docstring for thinkpython_problem.ex_10_1
we need to create a function that gives the sum of the nested lists

"""
t = [[1, 2], [3], [4, 5, 6]]

def nested_sum(t):
    total = 0
    for nested in t:
        total += sum(nested)
    return total
print(nested_sum(t))