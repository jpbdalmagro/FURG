def sort(vector):
    for i in range(len(vector)):
        min_index = i
        for j in range(i + 1, len(vector)):
            if vector[j] < vector[min_index]:
                min_index = j
        vector[i], vector[min_index] = vector[min_index], vector[i]
    return vector

A = [5, 4, 3, 2, 1]
A = sort(A)
print(A)
