import unittest
from util.ExcelHandler import ExcelHandle
import HtmlTestRunner


'''
Sanity_TestCases: Class defined to run sanity test cases.
'''

class Sanity_TestCases(unittest.TestCase):

    '''
    Setup Function: Create an object for Excel Handle class and access the functions defined in the class.
    Return value: row count, row number
    '''
    def setUp(self):
        self.obj = ExcelHandle()
        self.sheet_name = self.obj.open_excel_file("D:\\Result.xlsx", "Sheet1")[0]
        self.assertIn("Sheet1", str(self.sheet_name).strip())
        self.row_count = self.obj.get_row_count(self.sheet_name)
        self.row_list = list(range(2, self.row_count))
        global row_no
        row_no = 0
        row_no = iter(self.row_list)

    '''
    test_read_first_cell: Read the contents of a cell in the first row.
    '''
    def test_read_first_cell(self):
        self.cell_one = self.obj.read_celldata(self.sheet_name, int(next(row_no)))

    '''
    test_read_second_cell: Read the contents of a cell in the second row.
    '''
    def test_read_second_cell(self):
        self.cell_two = self.obj.read_celldata(self.sheet_name, int(next(row_no)))

    '''
    test_read_third_cell: Read the contents of a cell in the third row.
    '''
    def test_read_third_cell(self):
        self.cell_three = self.obj.read_celldata(self.sheet_name, int(next(row_no)))


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:\\report.html"))





