import unittest

# works on all platforms
import os
# get the directory containing your running .sikuli
myPath = os.path.dirname(getBundlePath())
if not myPath in sys.path: sys.path.append(myPath)

import test1

suite = unittest.TestLoader().loadTestsFromTestCase(UnitTestA)
unittest.TextTestRunner(verbosity=2).run(suite)