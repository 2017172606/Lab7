
class not2DError(Exception):
# Error for 1D list
    def __str__(self):
        return '[ERROR]: list is not 2D.'

class unevenListError(Exception):
# Error for uneven list
    def __str__(self):
        return '[ERROR]: inner lists are not same in length.'

class improperMatrixError(Exception):
# Error for incompatible matmul pair
    def __str__(self):
        return '[ERROR]: [a][b]*[c][d] not b==c.'


def mul1d(arr1,arr2):
    # arr1 * arr2
    # [1,2,3] * [4,5,6]
    # return  1*4 + 2*5 + 3*6
    sum = 0
    for i in range(len(arr1)):
        sum+=arr1[i]*arr2[i]
    return sum

class list_D2(list):
    def __init__(self,arr):
        
        ### YOUR CODE HERE ###
        for i in arr:
            if not isinstance(i, list):
                raise not2DError
        
        if len(set([len(i) for i in arr])) > 1:
            raise unevenListError()
        
        ######

        self.extend(arr)

    def __str__(self):

        ### YOUR CODE HERE ###
        
        return f'list_2D: {len(self)}*{len(self[0])}'
    
        ######

    def transpose(self):

        ### YOUR CODE HERE ###

        return list_D2(list(map(list, zip(*self))))
        
        # 2차원 배열을 zip(*2차원배열) 을 적용하면 전치가 된다.
        # [[1, 2, 3, 4],[5, 6, 7, 8]] 을 zip으로 엮으면, (1,5) (2, 6) (3, 7), (4,8) 로 된다.
        ######


    def __matmul__(self, others):
        
        ### YOUR CODE HERE ###
        

        if len(self[0]) != len(others):
            raise improperMatrixError()
        
        
        result = []
        for row in self:
            result_row = []
            for col in zip(*others):
                result_row.append(mul1d(row, col))
            result.append(result_row)   
        return list_D2(result)
    
        # original matrix의 행과, other matrix의 열의 내적 계산 및, 이를 result_row에 더함
        # 이를 result에 추가해서 행렬 구성 및 list_D2 에 넣음으로써 새로운 객체 생성.
        ######

    def avg(self):

        ### YOUR CODE HERE ###
        return sum(sum(row) for row in self) / (len(self) * len(self[0]) if self else 1)
        
        # 행에 해당하는 값 합산 후 갯수만큼 나누기, but self 가 비어있을 때 0을 반환하면 zero division 관련
        # 문제 발생함에 따라 1로 저장

        ######
