def verify_sudoku(matrix):
    nums = []
    count_all = 0

        
    for i in range(0, len(matrix)):

        if len(nums) != len(set(nums)):
            return False

        nums = []
        for j in range(0, len(matrix[i])):
                nums.append(matrix[i][j])


    L2 = []

    for i in range(len(matrix[0])):
        row = []
        for item in matrix:
            row.append(item[i])
        L2.append(row)

    nums = []

        
    for i in range(0, len(L2)):

        if len(nums) != len(set(nums)):
            return False

        nums = []
        for j in range(0, len(L2[i])):

            nums.append(L2[i][j])

    return True




array = [[1,2,3,    4,5,6,      7,8,9],
        [7,8,9,     1,2,3,      4,5,6],
        [4,5,6,     7,8,9,      1,2,3],

        [3,1,2,     8,4,5,      9,6,7],
        [6,9,7,     3,1,2,      8,4,5],
        [8,4,5,     6,9,7,      3,1,2],

        [2,3,1,     5,7,4,      6,9,8],
        [9,6,8,     2,3,1,      5,7,4],
        [5,7,4,     9,6,8,      2,3,1]]

print(verify_sudoku(array))
