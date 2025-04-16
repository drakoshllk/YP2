def count_array_entries(S, J):
    counter = 0
    for i in range(len(J)):
        counter += S.count(J[i])
    return counter

J, S = "ab", "aabbccd"
print(count_array_entries(S, J))