from __future__ import absolute_import, division, print_function, unicode_literals

import torch
from tests.utils import jitVsGlow


def test_slice_basic():
    """Test of the PyTorch slice Node on Glow."""

    def slice_basic(a):
        b = a[1:]
        return b[0][1:]

    x = torch.rand((2, 3))

    jitVsGlow(slice_basic, x, expected_fused_ops={"aten::slice"})
