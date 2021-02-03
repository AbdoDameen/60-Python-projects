class game_of_life:
    def GameOfLife(self, board: List[List[int]]) -> None:



        neighbors=[(1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1)]
        rows=len(board)
        columns=len(board[0])

        copy_board=[[board[row][col] for col in range(columns)] for row in range(rows)]

        for row in range(rows):
            for col in range(columns):

                live_neighbors=0
                for neighbor in neighbors:
                    r=(row + neighbor[0])
                    c=(col + neighbor[1])

                    if (r < rows and r >=0) and (c < columns and c >=0) and (copy_board[r][c]==1):
                        live_neighbors+=1

                if copy_board[rows][columns]==1 and (live_neighbors < 2 or live_neighbors>3):
                    board[row][col]=0

                if copy_board[row][col]==0 and live_neighbors==3:
                    board[row][col]=1
