import unittest, os
from getdiskusage import getdiskusage

class TestGetDiskUsage(unittest.TestCase):

    def test_getdiskusage(self):
        # set the root path for the module
        root_path = f'{os.getcwd()}/'
        # create the ENV var
        os.environ['ROOT_PATH'] = root_path
        # mock for file object with local path prepended to file names
        test_file_mock = { 'files': [
                            {f'{root_path}test/README.md': 8},
                            {f'{root_path}test/test.txt': 8}
                            ]}

        self.assertEqual(getdiskusage('test'), test_file_mock)

if __name__ == '__main__':
    unittest.main()
