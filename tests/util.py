# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from nose.tools import assert_raises, assert_equal, assert_less, \
    assert_less_equal, assert_not_equal, assert_greater, \
    assert_greater_equal, ok_
from numpy.testing import assert_allclose

le = assert_less_equal
lt = assert_less
eq = assert_equal
neq = assert_not_equal
ge = assert_greater_equal
gt = assert_greater
raises = assert_raises
ok = ok_
allclose = assert_allclose
