from typing import List, Tuple
import copy
import pdb
import json

class SubMatrixException(Exception):
    def __init__(self, message):
        self.message = message
        # Python3 specific
        super().__init__()
        # super(self, SubMatrixException).__init__()
        # Python< 3 specific

    def __str__(self):
        return self.message
    
class SquareSubMatrix:
    # Square matricies have the exact same number of rows and columns
    def __init__(self, matrix: List[List[int]], diag_offset:int):
        self.matrix = matrix
        self.diag_offset = diag_offset
        self.start_idx = [self.diag_offset, self.diag_offset]
        
        # Each 'recursion' into the matrix eliminates either two columns or
        # two rows
        self.length = len(self.matrix) - 2 * self.diag_offset

        self.max_submatrix_offset = None
        if len(self.matrix) % 2 == 0:
            self.max_submatrix_offset = (len(self.matrix) - 2) / 2
        else:
            self.max_submatrix_offset = (len(self.matrix) - 1) / 2
            

        # When the top most row is affected by rotation, we can
        # tell the user it is safe to descend into another square matrix
        # self.

        
    def rotate_idx_90(self, idx:List[int]) -> List[int]:
        return [len(self.matrix) - 1 - idx[1], idx[0]]

    def write_rotation(self, rotate_buffer):
        if len(rotate_buffer) == 1:
            return
        
        last_seen = rotate_buffer[0][0]
        
        for i in range(1, len(rotate_buffer)):
            current = rotate_buffer[i][0]
            rotate_buffer[i][0] = last_seen
            last_seen = current

        rotate_buffer[0][0] = last_seen
        
        for (index, value) in rotate_buffer:
            self.matrix[index[0]][index[1]] = value
        

    def rotate_edge(self):
        fix_idx = copy.copy(self.start_idx)
        
        # We index around the row in question, using each index as
        # a starting point, iterating through the 90deg rotation indicies,
        # replacing their values
        for i in range(0, self.length - 1):
            rotate_buffer = []

            current_idx = copy.copy(fix_idx)
            current_value = self.matrix[current_idx[0]][current_idx[1]]
            
            rotate_buffer.append([current_idx, current_value])
            
            current_idx = self.rotate_idx_90(current_idx)

            while (current_idx != fix_idx):
                first_iteration = False
                
                current_value = self.matrix[current_idx[0]][current_idx[1]]
                rotate_buffer.append([current_idx, current_value])

                current_idx = self.rotate_idx_90(current_idx)
                
            fix_idx[1] += 1

            self.write_rotation(rotate_buffer)

            
    def old_rotate_edge(self):
        # -2 because length is a length, not an index/offset, and the rotation
        # of index 0 will land on the same row and thus should not be rotated
        # twice
        begin_rotate_idx = list(self.start_idx)
        for i in range(0, self.length-1):
            prev_idx = tuple(begin_rotate_idx)

            current_value = self.matrix[current_idx[0]][current_idx[1]]
            rotate_value = current_value

            rotate_idx = current_idx
            
            for k in range(0, 4):
                rotate_idx = self.rotate_idx_90(rotate_idx)
                rotate_value = self.matrix[rotate_idx[0]][rotate_idx[1]]
                self.matrix[rotate_idx[0]][rotate_idx[1]] = current_value

                current_value = rotate_value

                if rotate_idx == tuple(begin_rotate_idx):
                    break
                
            begin_rotate_idx[1]+=1
    
    
class Solution:
    def get_sub_matrix(self, matrix:List[List[int]], diag_offset:int) -> SquareSubMatrix:
        # dimensions of described sub-array -
        #         len(matrix)-2*diag_depth x len(matrix)-2*diag_depth
        subarray_width = len(matrix)-2*diag_offset
        if subarray_width >= 1 :
            return SquareSubMatrix(diag_offset, matrix)
        else:
            raise SubMatrixExecption("Sub Matrix would have width: (len(matrix):%d)-2*(diag_offset:%d)" % (len(matrix), diag_offset))

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) % 2 == 0:
            max_submatrix_offset = int((len(matrix) - 2) / 2)
        else:
            max_submatrix_offset = int((len(matrix) - 1) / 2)


        for i in range(0, max_submatrix_offset+1):
            ssm = SquareSubMatrix(matrix, i)
            ssm.rotate_edge()
        
