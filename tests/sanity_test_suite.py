"""
Sanity test suite
"""
from controller.test_base import TestBase


class SanityTestSuite(TestBase):
    #setup_done = False
    sheet_name = ""
    #row_no = 1
    row_list = ""

    def __init__(self, *args, **kwargs):
        TestBase.__init__(self, *args, **kwargs)
        #super(SanityTestSuite, self).__init__()

    # def setUp(self):
    #     if SanityTestSuite.setup_done:
    #         return
    #     SanityTestSuite.setup_done = True
    #     SanityTestSuite.sheet_name = TestBase.excel_handler.open_excel_file(TestBase.current_folder_path[0] +
    #                                                                  TestBase.config.get('FileSection', 'ExcelSheetLocation').replace("'", ""),
    #                                                                  TestBase.config.get('WorkSheet', 'SanitySheet').replace("'", ""))[0]

    @classmethod
    def setUpClass(cls):
        SanityTestSuite.sheet_name = TestBase.excel_handler.open_excel_file(TestBase.current_folder_path[0] +
                                                                            TestBase.config.get('FileSection', 'ExcelSheetLocation').replace("'", ""),
                                                                            TestBase.config.get('WorkSheet', 'SanitySheet').replace("'", ""))[0]
        SanityTestSuite.row_count = TestBase.excel_handler.get_column_count(SanityTestSuite.sheet_name)
        SanityTestSuite.row_range = list(range(2, SanityTestSuite.row_count))
        SanityTestSuite.row_list = iter(SanityTestSuite.row_range)

    def test_BB_PWR_TC01_read_first_cell(self):
        self.cell_one = TestBase.excel_handler.read_cell_data(SanityTestSuite.sheet_name, int(next(SanityTestSuite.row_list)))
        self.key = TestBase.event_handler.search_for_event_key(self.cell_one)

        if not self.key:
            raise AssertionError("Key Not Found")
        else:
            self.event_name = TestBase.event_handler.search_for_event_id(self.key)
            TestBase.log.info("Key name is: " + self.event_name)
            self.event_id = TestBase.event_handler.search_for_event_value(self.key)
            TestBase.log.info("Key name is: " + self.event_id)

    def test_BB_PWR_TC03_read_second_cell(self):
        self.cell_one = TestBase.excel_handler.read_cell_data(SanityTestSuite.sheet_name, int(next(SanityTestSuite.row_list)))
        self.key = TestBase.event_handler.search_for_event_key(self.cell_one)

        if not self.key:
            raise AssertionError("Key Not Found")
        else:
            self.event_name = TestBase.event_handler.search_for_event_id(self.key)
            TestBase.log.info("Key name is: " + self.event_name)

    def test_BB_PWR_TC05_read_third_cell(self):
        self.cell_one = TestBase.excel_handler.read_cell_data(SanityTestSuite.sheet_name, int(next(SanityTestSuite.row_list)))
        self.key = TestBase.event_handler.search_for_event_key(self.cell_one)

        if not self.key:
            raise AssertionError("Key Not Found")
        else:
            self.event_name = self.event_handler.search_for_event_id(self.key)
            TestBase.log.info("Key name is: " + self.event_name)

    def test_BB_PWR_TC07_read_fourth_cell(self):
        self.cell_one = TestBase.excel_handler.read_cell_data(SanityTestSuite.sheet_name, int(next(SanityTestSuite.row_list)))
        self.key = TestBase.event_handler.search_for_event_key(self.cell_one)

        if not self.key:
            raise AssertionError("Key Not Found")
        else:
            self.event_name = self.event_handler.search_for_event_id(self.key)
            TestBase.log.info("Key name is: " + self.event_name)

    def test_BB_PWR_TC09_read_fifth_cell(self):
        self.cell_one = TestBase.excel_handler.read_cell_data(SanityTestSuite.sheet_name, int(next(SanityTestSuite.row_list)))
        self.key = TestBase.event_handler.search_for_event_key(self.cell_one)

        if not self.key:
            raise AssertionError("Key Not Found")
        else:
            self.event_name = TestBase.event_handler.search_for_event_id(self.key)
            TestBase.log.info("Key name is: " + self.event_name)
