def isValidSudoko():
    one_set = set()
    board = []
    for i in range(9):
        for j in range(9):
            if board[i][j].isdigit():
                row = '(' + str(i) + ')' + board[i][j]
                col = board[i][j] + '(' + str(j) + ')'
                small_square = '(' + str(i//3) + ')' + board[i][j] + '(' + str(j//3) + ')'
                if row in one_set or col in one_set or small_square in one_set:
                    return False
                one_set.update([row, col, small_square])
    return True




a = 4
print(id(a))
def test(a):
    print(id(a))

test(a)
class MyClass():
     def __init__(self):
         self.__superprivate = "Hello"
         self._semiprivate = ", world!"


b = MyClass()
print(b.__dict__)