def solution(rows, columns, queries):
    answer = []
    matrix = [[i*columns+j+1 for j in range(columns)]for i in range(rows)]
    for query in queries:
        min_num = rows*columns
        x_move,y_move = query[2]-query[0],query[3]-query[1]
        # 아래로 x_move 만큼 이동
        x,y = query[0]-1,query[1]-1
        for _ in range(1,x_move+1):
            # 현재 위치 저장
            if matrix[x+1][y] <= min_num:
                min_num = matrix[x+1][y]
            if matrix[x][y] <= min_num:
                min_num = matrix[x][y]
            temp = matrix[x][y]
            # 현재 위치에 넣어줌
            matrix[x][y] = matrix[x+1][y]
            matrix[x+1][y] = temp
            x += 1 # 자리 갱신
        # 오른쪽으로 y_move만큼 이동
        for _ in range(1,y_move+1):
            # 현재 위치 저장
            if matrix[x][y+1] <= min_num:
                min_num = matrix[x][y+1]
            if matrix[x][y] <= min_num:
                min_num = matrix[x][y]
            temp = matrix[x][y]
            # 현재 위치에 넣어줌
            matrix[x][y] = matrix[x][y+1]
            matrix[x][y+1] = temp
            y += 1 # 자리 갱신
        # 위로 X_move 만큼 이동
        for _ in range(1,x_move+1):
            # 현재 위치 저장
            if matrix[x-1][y] <= min_num:
                min_num = matrix[x-1][y]
            if matrix[x][y] <= min_num:
                min_num = matrix[x][y]
            temp = matrix[x][y]
            # 현재 위치에 넣어줌
            matrix[x][y] = matrix[x-1][y]
            matrix[x-1][y] = temp
            x -= 1 # 자리 갱신
        # 왼쪽으로 y_move-1 만큼 이동
        for _ in range(1,y_move):
            # 현재 위치 저장
            if matrix[x][y-1] <= min_num:
                min_num = matrix[x][y-1]
            if matrix[x][y] <= min_num:
                min_num = matrix[x][y]
            temp = matrix[x][y]
            # 현재 위치에 넣어줌
            matrix[x][y] = matrix[x][y-1]
            matrix[x][y-1] = temp
            y -= 1 # 자리 갱신
        answer.append(min_num)
    return answer
def solution(rows, columns, queries):
    answer = []
    matrix = [[i*columns+j+1 for j in range(columns)]for i in range(rows)]
    for query in queries:
        min_num = rows*columns
        x_move,y_move = query[2]-query[0],query[3]-query[1]
        # 아래로 x_move 만큼 이동
        x,y = query[0]-1,query[1]-1
        for _ in range(1,x_move+1):
            # 현재 위치 저장
            if matrix[x+1][y] <= min_num:
                min_num = matrix[x+1][y]
            if matrix[x][y] <= min_num:
                min_num = matrix[x][y]
            temp = matrix[x][y]
            # 현재 위치에 넣어줌
            matrix[x][y] = matrix[x+1][y]
            matrix[x+1][y] = temp
            x += 1 # 자리 갱신
        # 오른쪽으로 y_move만큼 이동
        for _ in range(1,y_move+1):
            # 현재 위치 저장
            if matrix[x][y+1] <= min_num:
                min_num = matrix[x][y+1]
            if matrix[x][y] <= min_num:
                min_num = matrix[x][y]
            temp = matrix[x][y]
            # 현재 위치에 넣어줌
            matrix[x][y] = matrix[x][y+1]
            matrix[x][y+1] = temp
            y += 1 # 자리 갱신
        # 위로 X_move 만큼 이동
        for _ in range(1,x_move+1):
            # 현재 위치 저장
            if matrix[x-1][y] <= min_num:
                min_num = matrix[x-1][y]
            if matrix[x][y] <= min_num:
                min_num = matrix[x][y]
            temp = matrix[x][y]
            # 현재 위치에 넣어줌
            matrix[x][y] = matrix[x-1][y]
            matrix[x-1][y] = temp
            x -= 1 # 자리 갱신
        # 왼쪽으로 y_move-1 만큼 이동
        for _ in range(1,y_move):
            # 현재 위치 저장
            if matrix[x][y-1] <= min_num:
                min_num = matrix[x][y-1]
            if matrix[x][y] <= min_num:
                min_num = matrix[x][y]
            temp = matrix[x][y]
            # 현재 위치에 넣어줌
            matrix[x][y] = matrix[x][y-1]
            matrix[x][y-1] = temp
            y -= 1 # 자리 갱신
        answer.append(min_num)
    return answer

# rows = 6
# columns =6 
# queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]

# rows = 3
# columns = 3
# queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]] 

rows = 100
columns = 97
queries = [[1,1,100,97]] 

print(solution(rows,columns,queries)) 
# rows = 6
# columns =6 
# queries = [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]

# rows = 3
# columns = 3
# queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]] 

rows = 100
columns = 97
queries = [[1,1,100,97]] 

print(solution(rows,columns,queries)) 