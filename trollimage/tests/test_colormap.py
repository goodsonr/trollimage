#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2013 Martin Raspaud

# Author(s):

#   Martin Raspaud <martin.raspaud@smhi.se>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""Test colormap.py
"""


import unittest
from trollimage import colormap
import numpy as np

class TestColormapClass(unittest.TestCase):
    """Test case for the colormap object.
    """
    def test_colormap(self):
        """Test features of the colormap class
        """
        cm_ = colormap.Colormap((1, (1.0, 1.0, 0.0)),
                                (2, (0.0, 1.0, 1.0)),
                                (3, (1, 1, 1)),
                                (4, (0, 0, 0)))

        data = np.array([1, 2, 3, 4])

        channels = cm_.colorize(data)
        for i in range(3):
            self.assertTrue(np.allclose(channels[i],
                                        cm_.colors[:, i],
                                        atol=0.001))
        

def suite():
    """The suite for test_colormap.
    """
    loader = unittest.TestLoader()
    mysuite = unittest.TestSuite()
    mysuite.addTest(loader.loadTestsFromTestCase(TestColormapClass))
    
    return mysuite