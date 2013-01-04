#!/usr/bin/env python
import collections

val = ['U', 'R', 'F', 'D', 'L', 'B']

Color = collections.namedtuple('Color', ' '.join(val))
Color = Color(*range(0, len(val)))
