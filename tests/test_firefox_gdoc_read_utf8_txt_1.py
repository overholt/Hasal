from lib.perfBaseTest import PerfBaseTest


class TestSikuli(PerfBaseTest):

    def setUp(self):
        self.set_variable(test_target=self.env.TEST_TARGET_ID_1_PAGE_CONTENT_WITH_UTF8_TXT)
        super(TestSikuli, self).setUp()

    def test_firefox_gdoc_read_utf8_txt_1(self):
        self.sikuli_status = self.sikuli.run_test(self.env.test_name, self.env.output_name, test_url=self.test_url)
