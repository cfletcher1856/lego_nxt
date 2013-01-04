#!/usr/bin/env python
import collections

val = ['URF', 'UFL', 'ULB', 'UBR', 'DFR', 'DLF', 'DBL', 'DRB']

Corner = collections.namedtuple('Corner', ' '.join(val))
Corner = Corner(*range(0, len(val)))
