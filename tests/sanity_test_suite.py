"""
Sanity test suite
"""
from controller.test_base import TestBase


class SanityTestSuite(TestBase):
    setup_done = False

    def __init__(self, *args, **kwargs):
        TestBase.__init__(self, *args, **kwargs)
        #super(SanityTestSuite, self).__init__()

    def setUp(self):
        if self.setup_done:
            return
        self.setup_done = True
        self.sheet_name = self.excel_handler.open_excel_file(self.current_folder_path[0] +
                                                             self.config.get('FileSection', 'ExcelSheetLocation').replace("'", ""),
                                                             self.config.get('WorkSheet', 'SanitySheet').replace("'", ""))[0]

    def test_read_first_cell(self):
        self.cell_one = self.excel_handler.read_cell_data(self.sheet_name, 2)
        self.key = self.event_handler.search_for_event_key(self.cell_one)

        if not self.key:
            raise AssertionError("Key Not Found")
        else:
            self.event_name = self.event_handler.search_for_event_id(self.key)
            self.log.info("Key name is: " + self.event_name)
            self.event_id = self.event_handler.search_for_event_value(self.key)
            self.log.info("Key name is: " + self.event_id)

    def test_read_second_cell(self):
        self.cell_one = self.excel_handler.read_cell_data(self.sheet_name, 3)
        self.key = self.event_handler.search_for_event_key(self.cell_one)

        if not self.key:
            raise AssertionError("Key Not Found")
        else:
            self.event_name = self.event_handler.search_for_event_id(self.key)
            self.log.info("Key name is: " + self.event_name)

    def test_read_third_cell(self):
        self.cell_one = self.excel_handler.read_cell_data(self.sheet_name, 4)
        self.key = self.event_handler.search_for_event_key(self.cell_one)

        if not self.key:
            raise AssertionError("Key Not Found")
        else:
            self.event_name = self.event_handler.search_for_event_id(self.key)
            self.log.info("Key name is: " + self.event_name)

    def test_read_fourth_cell(self):
        self.cell_one = self.excel_handler.read_cell_data(self.sheet_name, 5)
        self.key = self.event_handler.search_for_event_key(self.cell_one)

        if not self.key:
            raise AssertionError("Key Not Found")
        else:
            self.event_name = self.event_handler.search_for_event_id(self.key)
            self.log.info("Key name is: " + self.event_name)

    def test_read_fifth_cell(self):
        self.cell_one = self.excel_handler.read_cell_data(self.sheet_name, 6)
        self.key = self.event_handler.search_for_event_key(self.cell_one)

        if not self.key:
            raise AssertionError("Key Not Found")
        else:
            self.event_name = self.event_handler.search_for_event_id(self.key)
            self.log.info("Key name is: " + self.event_name)
