from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

from edward.stats import bernoulli
from scipy import stats

sess = tf.Session()


def _assert_eq(val_ed, val_true):
    with sess.as_default():
        assert np.allclose(val_ed.eval(), val_true)


def _test(x, p):
    xtf = tf.constant(x)
    val_true = stats.bernoulli.logpmf(x, p)
    _assert_eq(bernoulli.logpmf(xtf, p), val_true)
    _assert_eq(bernoulli.logpmf(xtf, tf.constant(p)), val_true)
    _assert_eq(bernoulli.logpmf(xtf, tf.constant([p])), val_true)


def test_int_0d():
    _test(0, 0.5)
    _test(1, 0.75)


def test_float_0d():
    _test(0.0, 0.5)
    _test(1.0, 0.75)


def test_int_1d():
    _test([0, 1, 0], 0.5)
    _test([1, 0, 0], 0.75)


def test_float_1d():
    _test([0.0, 1.0, 0.0], 0.5)
    _test([1.0, 0.0, 0.0], 0.75)


def test_int_2d():
    _test(np.array([[0, 1, 0],[0, 1, 0]]), 0.5)
    _test(np.array([[1, 0, 0],[0, 1, 0]]), 0.75)


def test_float_2d():
    _test(np.array([[0.0, 1.0, 0.0],[0.0, 1.0, 0.0]]), 0.5)
    _test(np.array([[1.0, 0.0, 0.0],[0.0, 1.0, 0.0]]), 0.75)
