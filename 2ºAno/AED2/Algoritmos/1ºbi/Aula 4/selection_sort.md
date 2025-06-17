


     A = [1, 2, 3, 4]
     
     for i = 0 to lenght[A] - 1 do
        smallest = i
        for j = i + 1 to n do
            if A[j] < A[smallest]
                smallest = i
                
            end if
        end for

        temp = A[j]
        A[j] = A[smallest]
        A[smallest] = tmp

    end for
