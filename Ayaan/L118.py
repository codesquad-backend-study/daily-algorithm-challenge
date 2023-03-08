def generate(numRows):
        result = []
        if numRows == 1:
            return [1]
        
        row = [1]
        result.append(row)
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