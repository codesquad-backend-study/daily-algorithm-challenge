def generate(numRows):
        result = []
        
        row = [1]
        result.append(row)
        if numRows == 1:
            return result
        
        row = [1,1]
        result.append(row)
        for i in range(2, numRows):
            sumRow = []
            for j in range(0, len(row)-1):
                sumRow.append(row[j] + row[j+1])
            row = sumRow
            row.insert(0, 1)
            row.append(1)
            result.append(row)
        return result
    
result = generate(5)
print(result)