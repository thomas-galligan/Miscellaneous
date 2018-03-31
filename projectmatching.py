#Tom Galligan, 08/02/17


import xlrd #these need to be installed before use (use e.g. ''>>sudo easy_install xlrd' on Mac OS X)
import xlwt #same here
import numpy as np


#first define a function to read in the excel file for use in the algorithm
def read_excel(filename, n=0): 
    """Converts first sheet from an Excel file into an ndarray
    
    Parameters
    ----------
    filename : string
        Path to file.
        
    Returns
    -------
    ndarray with sheet contents (no conversion done)
    """
    contentstring = open(filename, 'rb').read()
    book  = xlrd.open_workbook(file_contents=contentstring)
    sheet = book.sheets()[n]
    array = np.zeros((sheet.ncols, sheet.nrows))
    
    for row in range(sheet.nrows):
        for col in range(sheet.ncols):
            array[col][row] = int(sheet.cell(row, col).value)
    
   

    print array
    return array




array = read_excel('/Users/Tom/OneDrive - The University of Oxford/MPhys Algorithm/allocationmatrix1516.xlsx', n=0) #read allocationmatrix file and save as an array

from munkres import Munkres, print_matrix #run the matching algorithm using the allocation matrix


m = Munkres()
indexes = m.compute(np.copy(array))

total = 0
for row, column in indexes:
    value = array[row][column]
    total += value
    print '(%d, %d) -> %d' % (row, column, value)
print 'total cost: %d' % total #print the final allocations along with the student's preference for the allocation
