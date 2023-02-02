


ll = ('hi','hello','world','where')

def even(x):
    if 'wold' in x:
        return True
    else:
        return False

def add_map(x):
    return x + " harry"

f =  list(filter(even,ll))
print(f)


f1 =  list(map(add_map,ll))
print(f1)