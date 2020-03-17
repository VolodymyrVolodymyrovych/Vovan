def my_def(var):
    c = 0
    counts = []
    counts_out = []
    for i in range(1, var+1):
        counts.append(i)
    for i in counts:
        if var % counts[i-1] == 0:
            counts_out.append(i)
        else:
            i += i
    # return counts
    return counts_out


var = int(input("Write count: "))
print(var,"-> ",my_def(var))