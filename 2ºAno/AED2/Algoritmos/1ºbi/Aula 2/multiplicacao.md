ALGORITHM MULTIPLICATION(A, B)
    Input: Arrays A and B representing two numbers with digits in reverse order
    Output: An integer representing the product of the two numbers

    SHIFT_A ← 1
    TOTAL ← 0

    for each NUM in A do
        MID ← 0
        SHIFT_B ← 1
        for each NUM_B in B do
            MID ← MID + ((NUM * SHIFT_A) * (NUM_B * SHIFT_B))
            SHIFT_B ← SHIFT_B × 10
        end for
        TOTAL ← TOTAL + MID
        SHIFT_A ← SHIFT_A × 10
    end for

    return TOTAL
