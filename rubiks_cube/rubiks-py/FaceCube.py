#!/usr/bin/env python

from Facelet import Facelet
from Color import Color
from Corner import Corner
from Edge import Edge


registry = {}


class RegisteringType(type):
    def __init__(cls, name, bases, attrs):
        for key, val in attrs.iteritems():
            properties = getattr(val, 'register', None)
            if properties is not None:
                registry['%s.%s' % (name, key)] = properties


def register(*args):
    def decorator(f):
        f.register = tuple(args)
        return f
    return decorator


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Cube on the facelet level
class FaceCube(object):
    """ generated source for class FaceCube """
    f = [None] * 54

    #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #  Map the corner positions to facelet positions. cornerFacelet[URF.ordinal()][0] e.g. gives the position of the
    #  facelet in the URF corner position, which defines the orientation.<br>
    #  cornerFacelet[URF.ordinal()][1] and cornerFacelet[URF.ordinal()][2] give the position of the other two facelets
    #  of the URF corner (clockwise).
    cornerFacelet = [[Facelet.U9, Facelet.R1, Facelet.F3], [Facelet.U7, Facelet.F1, Facelet.L3], [Facelet.U1, Facelet.L1, Facelet.B3], [Facelet.U3, Facelet.B1, Facelet.R3],
            [Facelet.D3, Facelet.F9, Facelet.R7], [Facelet.D1, Facelet.L9, Facelet.F7], [Facelet.D7, Facelet.B9, Facelet.L7], [Facelet.D9, Facelet.R9, Facelet.B7]]

    #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #  Map the edge positions to facelet positions. edgeFacelet[UR.ordinal()][0] e.g. gives the position of the facelet in
    #  the UR edge position, which defines the orientation.<br>
    #  edgeFacelet[UR.ordinal()][1] gives the position of the other facelet
    edgeFacelet = [[Facelet.U6, Facelet.R2], [Facelet.U8, Facelet.F2], [Facelet.U4, Facelet.L2], [Facelet.U2, Facelet.B2], [Facelet.D6, Facelet.R8], [Facelet.D2, Facelet.F8],
            [Facelet.D4, Facelet.L8], [Facelet.D8, Facelet.B8], [Facelet.F6, Facelet.R4], [Facelet.F4, Facelet.L6], [Facelet.B6, Facelet.L4], [Facelet.B4, Facelet.R6]]

    #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #  Map the corner positions to facelet colors.
    cornerColor = [[Color.U, Color.R, Color.F], [Color.U, Color.F, Color.L], [Color.U, Color.L, Color.B], [Color.U, Color.B, Color.R], [Color.D, Color.F, Color.R], [Color.D, Color.L, Color.F],
            [Color.D, Color.B, Color.L], [Color.D, Color.R, Color.B]]

    #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #  Map the edge positions to facelet colors.
    edgeColor = [[Color.U, Color.R], [Color.U, Color.F], [Color.U, Color.L], [Color.U, Color.B], [Color.D, Color.R], [Color.D, Color.F], [Color.D, Color.L], [Color.D, Color.B],
            [Color.F, Color.R], [Color.F, Color.L], [Color.B, Color.L], [Color.B, Color.R]]

    def __init__(self, s=None):
        if s is None:
            s = "UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB"
        i = 0
        while i < len(s):
            print getattr(Color, s[i:i + 1])
            self.f[i] = getattr(Color, s[i:i + 1])
            i += 1
        print self.f

    #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #  Gives string representation of a facelet cube
    def to_String(self):
        """ generated source for method to_String """
        s = ""
        i = 0
        while i < 54:
            s += self.f[i].__str__()
            i += 1
        return s

    def toCubieCube(self):
        from CubieCube import CubieCube
        """ generated source for method toCubieCube """
        ori = int()
        ccRet = CubieCube()
        i = 0
        while i < 8:
            ccRet.cp[i] = Corner.URF
            i += 1
        i = 0
        while i < 12:
            ccRet.ep[i] = Edge.UR
            i += 1
        col1 = Color()
        col2 = Color()
        for i in Corner.values():
            while ori < 3:
                if self.f[self.cornerFacelet[i.ordinal()][ori].ordinal()] == Color.U or self.f[self.cornerFacelet[i.ordinal()][ori].ordinal()] == Color.D:
                    break
                ori += 1
            col1 = self.f[self.cornerFacelet[i.ordinal()][(ori + 1) % 3].ordinal()]
            col2 = self.f[self.cornerFacelet[i.ordinal()][(ori + 2) % 3].ordinal()]
            for j in Corner.values():
                if col1 == self.cornerColor[j.ordinal()][1] and col2 == self.cornerColor[j.ordinal()][2]:
                    ccRet.cp[i.ordinal()] = j
                    ccRet.co[i.ordinal()] = int((ori % 3))
                    break
        for i in Edge.values():
            for j in Edge.values():
                if self.f[self.edgeFacelet[i.ordinal()][0].ordinal()] == self.edgeColor[j.ordinal()][0] and self.f[self.edgeFacelet[i.ordinal()][1].ordinal()] == self.edgeColor[j.ordinal()][1]:
                    ccRet.ep[i.ordinal()] = j
                    ccRet.eo[i.ordinal()] = 0
                    break
                if self.f[self.edgeFacelet[i.ordinal()][0].ordinal()] == self.edgeColor[j.ordinal()][1] and self.f[self.edgeFacelet[i.ordinal()][1].ordinal()] == self.edgeColor[j.ordinal()][0]:
                    ccRet.ep[i.ordinal()] = j
                    ccRet.eo[i.ordinal()] = 1
                    break
        return ccRet
