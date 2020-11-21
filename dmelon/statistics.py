#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import numpy as np


def edof(N, window, overlap):
    window = window / np.linalg.norm(window)
    nskip = window.size - overlap
    nseg = np.ceil(N / nskip) + 1
    num = 2 * nseg
    den = 0
    for m in range(1, np.around(nseg).astype(np.int)):
        upper_limit = m * nskip
        b = np.zeros_like(window)
        b[: len(window[upper_limit:])] = window[upper_limit:]
        den += (1 - (m / nseg)) * np.dot(window, b) ** 2
    den = 1 + 2 * den
    return num / den