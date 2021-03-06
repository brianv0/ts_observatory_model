import math
import unittest

from lsst.ts.observatory.model import ObservatoryPosition
import lsst.utils.tests

class ObservatoryPositionTest(unittest.TestCase):

    def setUp(self):
        self.ra_truth = 41.010349
        self.dec_truth = -19.985964
        self.ang_truth = 175.993874013319
        self.alt_truth = 79.6715648342188
        self.az_truth = 353.018554127083
        self.pa_truth = 173.584814234084
        self.rot_truth = -2.40905977923582

        self.timestamp = 1672534239.91224
        self.ra_rad_truth = math.radians(self.ra_truth)
        self.dec_rad_truth = math.radians(self.dec_truth)
        self.ang_rad_truth = math.radians(self.ang_truth)
        self.band_filter_truth = 'y'
        self.tracking_truth = True
        self.alt_rad_truth = math.radians(self.alt_truth)
        self.az_rad_truth = math.radians(self.az_truth)
        self.pa_rad_truth = math.radians(self.pa_truth)
        self.rot_rad_truth = math.radians(self.rot_truth)

        self.op = ObservatoryPosition(self.timestamp, self.ra_rad_truth,
                                      self.dec_rad_truth, self.ang_rad_truth,
                                      self.band_filter_truth,
                                      self.tracking_truth, self.alt_rad_truth,
                                      self.az_rad_truth, self.pa_rad_truth,
                                      self.rot_rad_truth)

    def test_basic_information_after_creation(self):
        self.assertEqual(self.op.time, self.timestamp)
        self.assertEqual(self.op.ra, self.ra_truth)
        self.assertEqual(self.op.dec, self.dec_truth)
        self.assertEqual(self.op.ang, self.ang_truth)
        self.assertEqual(self.op.filter, self.band_filter_truth)
        self.assertTrue(self.op.tracking)
        self.assertEqual(self.op.alt, self.alt_truth)
        self.assertEqual(self.op.az, self.az_truth)
        self.assertEqual(self.op.pa, self.pa_truth)
        self.assertEqual(self.op.rot, self.rot_truth)

    def test_string_representation(self):
        instance_srep = "t=1672534239.9 ra=41.010 dec=-19.986 "\
                        "ang=175.994 filter=y track=True alt=79.672 "\
                        "az=353.019 pa=173.585 rot=-2.409"
        self.assertEqual(str(self.op), instance_srep)

class MemoryTestClass(lsst.utils.tests.MemoryTestCase):
    pass

def setup_module(module):
    lsst.utils.tests.init()

if __name__ == "__main__":
    lsst.utils.tests.init()
    unittest.main()
