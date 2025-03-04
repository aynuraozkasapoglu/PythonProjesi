def flatten (a,b):

    for i in a:
        if type(i) != type([]):
            b.append(i)
        elif type(i) == type([]):
            flatten(i, b)
    return b


arr = [1,2,[3,4,5],6,7,[8,[9,10]]]
f_list = []
 
print(flatten(arr, f_list))