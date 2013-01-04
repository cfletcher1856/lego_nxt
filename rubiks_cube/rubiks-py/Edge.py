#!/usr/bin/env python
import collections

val = ['UR', 'UF', 'UL', 'UB', 'DR', 'DF', 'DL', 'DB', 'FR', 'FL', 'BL', 'BR']

Edge = collections.namedtuple('Edge', ' '.join(val))
Edge = Edge(*range(0, len(val)))
