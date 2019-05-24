# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

from numpy.testing import assert_allclose, assert_array_almost_equal
import pytest

__all__ = ['allclose', 'approx']

allclose = assert_allclose


def approx(x, y, digits=7):
    return assert_array_almost_equal(x, y, decimal=digits)
