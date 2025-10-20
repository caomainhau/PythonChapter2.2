def sublists(lst):
    result = [[]]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            result.append(lst[i:j])
    return result

print(sublists([1, 2, 3]))
