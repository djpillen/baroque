import os
import shutil
import tempfile
import unittest

from baroque.baroque_project import BaroqueProject


class TestBaroque(unittest.TestCase):

    def setUp(self):
        self.tmp_dir = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.tmp_dir)

    def test_create_project(self):
        source_dir = os.path.join(self.tmp_dir, "source")
        destination_dir = os.path.join(self.tmp_dir, "destination")
        os.makedirs(source_dir)
        os.makedirs(destination_dir)
        project = BaroqueProject(source_dir, destination_dir)
        self.assertEqual(project.source_directory, source_dir)
        self.assertEqual(project.destination_directory, destination_dir)

    def test_characterize_source(self):
        shipment_src = os.path.join(self.tmp_dir, "test-shipment")
        os.makedirs(shipment_src)
        self.assertEqual(BaroqueProject(shipment_src, self.tmp_dir).characterize_source_directory(), "shipment")

    # def test_failure(self):
        # self.assertEqual(2+2, 5)


if __name__ == "__main__":
    unittest.main()
