class Matrix:
    def __init__(self, mat: list):
        self.rows = len(mat)
        self.cols = len(mat[0])
        self.matrix = mat

    def get_all_4by4_mat(self) -> list:
        '''
        Returns all 4 by 4 matrices as a list
        '''
        n = self.rows
        m = self.cols
        mat = self.matrix
        all_sub_mats = []
        for r in range(n-3):
            for c in range(m-3):
                sub_mat = [
                    mat[r][c:c+4],
                    mat[r+1][c:c+4],
                    mat[r+2][c:c+4],
                    mat[r+3][c:c+4]
                ]

                all_sub_mats.append(sub_mat)
        
        return all_sub_mats


if __name__ == "__main__":
    # fp = open('problem_011/data.txt')
    # matrix = []
    # for line in fp:
    #     str_row = line.replace('\n', '').split(" ")
    #     matrix.append(list(int(i) for i in str_row))
    
    # fp.close()

    # mat = Matrix(matrix)

    # res = mat.get_all_4by4_mat()

    # print(res[-1])
    pass


