
class SimpleMatrix:
   def __init__(self, matrix):
      self._matrix = matrix
      self._rows = rows
      self._columns = columns

   def first_echelon_form(self):
      col_counter = 0
      piv_r = 0
      prev_piv = -1
      while (col_counter < self._columns):
         zeroc = False
         for zi in range(piv_r,self._rows):
            if self._matrix[i][c] != 0:
               zeroc = True
               piv_r = i
               break

         # the column is zero
         if zeroc:
            pass
            
   def exchange_rows(self, row1, row2):
      row1 -= 1
      row2 -= 1
      temp = []
      for i in range(len(self._matrix[row1])):
         temp.append(self._matrix[row1][i])
      self._matrix[row1] = self._matrix[row2]
      self._matrix[row2] = temp

   def print_matrix(self):
      for r in range(len(self._matrix)):
         row_string = ""
         for c in range(len(self._matrix[r])):
            row_string += str(self._matrix[r][c]) + ", "

         print row_string

   def multiply_row_by_const(self, row, const):
      row -=1
      for c in range(len(self._matrix[row])):
         newval = float(self._matrix[row][c]) * const
         self._matrix[row][c] = newval

matrix = [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]
simplematrix = SimpleMatrix(matrix, 3, 3)
simplematrix.exchange_rows(1, 2)
simplematrix.multiply_row_by_const(3, 1.0/7.0)
simplematrix.print_matrix()
