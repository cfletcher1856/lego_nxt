#!/usr/bin/env python

from java2python.mod.include.overloading import overloaded

from Corner import Corner
from Edge import Edge
from FaceCube import FaceCube

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
# Cube on the cubie level
class CubieCube(object):
    """ generated source for class CubieCube """
    #  initialize to Id-Cube
    #  corner permutation
    cp = [Corner.URF, Corner.UFL, Corner.ULB, Corner.UBR, Corner.DFR, Corner.DLF, Corner.DBL, Corner.DRB]

    #  corner orientation
    co = [0, 0, 0, 0, 0, 0, 0, 0]

    #  edge permutation
    ep = [Edge.UR, Edge.UF, Edge.UL, Edge.UB, Edge.DR, Edge.DF, Edge.DL, Edge.DB, Edge.FR, Edge.FL, Edge.BL, Edge.BR]

    #  edge orientation
    eo = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    #  ************************************** Moves on the cubie level ***************************************************
    cpU = [Corner.UBR, Corner.URF, Corner.UFL, Corner.ULB, Corner.DFR, Corner.DLF, Corner.DBL, Corner.DRB]
    coU = [0, 0, 0, 0, 0, 0, 0, 0]
    epU = [Edge.UB, Edge.UR, Edge.UF, Edge.UL, Edge.DR, Edge.DF, Edge.DL, Edge.DB, Edge.FR, Edge.FL, Edge.BL, Edge.BR]
    eoU = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cpR = [Corner.DFR, Corner.UFL, Corner.ULB, Corner.URF, Corner.DRB, Corner.DLF, Corner.DBL, Corner.UBR]
    coR = [2, 0, 0, 1, 1, 0, 0, 2]
    epR = [Edge.FR, Edge.UF, Edge.UL, Edge.UB, Edge.BR, Edge.DF, Edge.DL, Edge.DB, Edge.DR, Edge.FL, Edge.BL, Edge.UR]
    eoR = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cpF = [Corner.UFL, Corner.DLF, Corner.ULB, Corner.UBR, Corner.URF, Corner.DFR, Corner.DBL, Corner.DRB]
    coF = [1, 2, 0, 0, 2, 1, 0, 0]
    epF = [Edge.UR, Edge.FL, Edge.UL, Edge.UB, Edge.DR, Edge.FR, Edge.DL, Edge.DB, Edge.UF, Edge.DF, Edge.BL, Edge.BR]
    eoF = [0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0]
    cpD = [Corner.URF, Corner.UFL, Corner.ULB, Corner.UBR, Corner.DLF, Corner.DBL, Corner.DRB, Corner.DFR]
    coD = [0, 0, 0, 0, 0, 0, 0, 0]
    epD = [Edge.UR, Edge.UF, Edge.UL, Edge.UB, Edge.DF, Edge.DL, Edge.DB, Edge.DR, Edge.FR, Edge.FL, Edge.BL, Edge.BR]
    eoD = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cpL = [Corner.URF, Corner.ULB, Corner.DBL, Corner.UBR, Corner.DFR, Corner.UFL, Corner.DLF, Corner.DRB]
    coL = [0, 1, 2, 0, 0, 2, 1, 0]
    epL = [Edge.UR, Edge.UF, Edge.BL, Edge.UB, Edge.DR, Edge.DF, Edge.FL, Edge.DB, Edge.FR, Edge.UL, Edge.DL, Edge.BR]
    eoL = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    cpB = [Corner.URF, Corner.UFL, Corner.UBR, Corner.DRB, Corner.DFR, Corner.DLF, Corner.ULB, Corner.DBL]
    coB = [0, 0, 1, 2, 0, 0, 2, 1]
    epB = [Edge.UR, Edge.UF, Edge.UL, Edge.BR, Edge.DR, Edge.DF, Edge.DL, Edge.BL, Edge.FR, Edge.FL, Edge.UB, Edge.DB]
    eoB = [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1]

    #  this CubieCube array represents the 6 basic cube moves
    moveCube = [None] * 6

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """

    @register(object, Corner, int, Edge, int)
    def __init___0(self, cp, co, ep, eo):
        """ generated source for method __init___0 """
        self.__init__()
        i = 0
        while i < 8:
            self.cp[i] = cp[i]
            self.co[i] = co[i]
            i += 1
        i = 0
        while i < 12:
            self.ep[i] = ep[i]
            self.eo[i] = eo[i]
            i += 1

    @classmethod
    def Cnk(cls, n, k):
        """ generated source for method Cnk """
        i = int()
        j = int()
        s = int()
        if n < k:
            return 0
        if k > n / 2:
            k = n - k
        while i != n - k:
            s *= i
            s /= j
            j += 1
        return s

    @classmethod
    @overloaded
    def rotateLeft(cls, arr, l, r):
        """ generated source for method rotateLeft """
        temp = arr[l]
        i = l
        while i < r:
            arr[i] = arr[i + 1]
            i += 1
        arr[r] = temp

    @classmethod
    @overloaded
    def rotateRight(cls, arr, l, r):
        """ generated source for method rotateRight """
        temp = arr[r]
        i = r
        while i > l:
            arr[i] = arr[i - 1]
            i -= 1
        arr[l] = temp

    @classmethod
    @register(object, Edge, int, int)
    def rotateLeft_0(cls, arr, l, r):
        """ generated source for method rotateLeft_0 """
        temp = arr[l]
        i = l
        while i < r:
            arr[i] = arr[i + 1]
            i += 1
        arr[r] = temp

    @classmethod
    @register(object, Edge, int, int)
    def rotateRight_0(cls, arr, l, r):
        """ generated source for method rotateRight_0 """
        temp = arr[r]
        i = r
        while i > l:
            arr[i] = arr[i - 1]
            i -= 1
        arr[l] = temp

    def toFaceCube(self):
        """ generated source for method toFaceCube """
        fcRet = FaceCube()
        print fcRet.cornerFacelet
        n = 0
        for c in Corner:
            i = c
            j = self.cp[i]
            ori = self.co[i]
            while n < 3:
                face = fcRet.cornerFacelet[i] = (n + ori) % 3
                fcRet.f[face] = fcRet.cornerColor[j][n]
                n += 1
        n = 0
        for e in Edge:
            i = e
            j = self.ep[i]
            ori = self.eo[i]
            while n < 2:
                face = fcRet.edgeFacelet[i] = (n + ori) % 2
                fcRet.f[face] = fcRet.edgeColor[j][n]
                n += 1
        return fcRet

    def cornerMultiply(self, b):
        """ generated source for method cornerMultiply """
        cPerm = [None] * 8
        cOri = [None] * 8
        for corn in Corner:
            cPerm[corn] = self.cp[b.cp[corn]]
            oriA = self.co[b.cp[corn]]
            oriB = b.co[corn]
            ori = 0

            if oriA < 3 and oriB < 3:
                ori = int((oriA + oriB))
                if ori >= 3:
                    ori -= 3
            elif oriA < 3 and oriB >= 3:
                ori = int((oriA + oriB))
                if ori >= 6:
                    ori -= 3
            elif oriA >= 3 and oriB < 3:
                ori = int((oriA - oriB))
                if ori < 3:
                    ori += 3
            elif oriA >= 3 and oriB >= 3:
                ori = int((oriA - oriB))
                if ori < 0:
                    ori += 3
            cOri[corn] = ori
        for c in Corner:
            self.cp[c] = cPerm[c]
            self.co[c] = cOri[c]

    def edgeMultiply(self, b):
        """ generated source for method edgeMultiply """
        ePerm = [None] * 12
        eOri = [None] * 12
        for edge in Edge:
            ePerm[edge] = self.ep[b.ep[edge]]
            eOri[edge] = int(((b.eo[edge] + self.eo[b.ep[edge]]) % 2))
        for e in Edge:
            self.ep[e] = ePerm[e]
            self.eo[e] = eOri[e]

    def multiply(self, b):
        """ generated source for method multiply """
        self.cornerMultiply(b)

    def invCubieCube(self, c):
        """ generated source for method invCubieCube """
        for edge in Edge:
            c.ep[self.ep[edge]] = edge
        for edge in Edge:
            c.eo[edge] = self.eo[c.ep[edge]]
        for corn in Corner:
            c.cp[self.cp[corn]] = corn
        for corn in Corner:
            ori = self.co[c.cp[corn]]
            if ori >= 3:
                c.co[corn] = ori
            else:
                c.co[corn] = int(-ori)
                if c.co[corn] < 0:
                    c.co[corn] += 3

    def getTwist(self):
        """ generated source for method getTwist """
        ret = 0
        i = Corner.URF
        while i < Corner.DRB:
            ret = int((3 * ret + self.co[i]))
            i += 1
        return ret

    def setTwist(self, twist):
        """ generated source for method setTwist """
        twistParity = 0
        i = Corner.DRB - 1
        while i >= Corner.URF:
            self.co[i] = int((twist % 3))
            twistParity = twistParity + self.co[i]
            twist = twist / 3
            i = i - 1
        self.co[Corner.DRB] = int(((3 - twistParity % 3) % 3))
        print "Done with setTwist()"

    def getFlip(self):
        """ generated source for method getFlip """
        ret = 0
        i = Edge.UR
        while i < Edge.BR:
            ret = int((2 * ret + self.eo[i]))
            i += 1
        return ret

    def setFlip(self, flip):
        """ generated source for method setFlip """
        flipParity = 0
        i = Edge.BR - 1
        while i >= Edge.UR:
            self.eo[i] = int((flip % 2))
            flipParity = flipParity + self.eo[i]
            flip = flip / 2
            i = i - 1
        self.eo[Edge.BR] = int(((2 - flipParity % 2) % 2))
        print "Done with setFlip()"
        print self.eo

    def cornerParity(self):
        """ generated source for method cornerParity """
        s = 0
        i = Corner.DRB
        while i >= Corner.URF + 1:
            j = i - 1
            while j >= Corner.URF:
                if self.cp[j] > self.cp[i]:
                    s += 1
                j = j - 1
            i -= 1
        return int((s % 2))

    def edgeParity(self):
        """ generated source for method edgeParity """
        s = 0
        i = Edge.BR
        while i >= Edge.UR + 1:
            j = i - 1
            while j >= Edge.UR:
                if self.ep[j] > self.ep[i]:
                    s += 1
                j = j - 1
            i = i - 1
        print "Done with edgeParity()"
        return int((s % 2))

    def getFRtoBR(self):
        """ generated source for method getFRtoBR """
        a = 0
        x = 0
        edge4 = [None] * 4
        j = Edge.BR
        while j >= Edge.UR:
            __x_0 = x
            x += 1
            if Edge.FR <= self.ep[j] and self.ep[j] <= Edge.BR:
                a += self.Cnk(11 - j, x + 1)
                edge4[3 - __x_0] = self.ep[j]
            j -= 1
        b = 0
        j = 3
        while j > 0:
            k = 0
            while edge4[j] != j + 8:
                self.rotateLeft(edge4, 0, j)
                k += 1
            b = (j + 1) * b + k
            j -= 1
        return int((24 * a + b))

    def setFRtoBR(self, idx):
        """ generated source for method setFRtoBR """
        x = int()
        sliceEdge = [Edge.FR, Edge.FL, Edge.BL, Edge.BR]
        otherEdge = [Edge.UR, Edge.UF, Edge.UL, Edge.UB, Edge.DR, Edge.DF, Edge.DL, Edge.DB]
        b = idx % 24
        a = idx / 24
        for e in Edge:
            self.ep[e] = Edge.DB
        j = 1
        k = int()
        for j in range(4):
            k = b % (j + 1)
            b /= j + 1
            k -= 1
            while k > 0:
                self.rotateRight(sliceEdge, 0, j)

        x = 3
        j = Edge.UR
        brord = Edge.BR
        while j <= brord:
            __x_2 = x
            x -= 1
            if a - self.Cnk(11 - j, x + 1) >= 0:
                self.ep[j] = sliceEdge[3 - x]
                a -= self.Cnk(11 - j, __x_2 + 1)
            j += 1

        x = 0
        j = Edge.UR
        brord = Edge.BR
        while j <= brord:
            __x_3 = x
            x += 1
            if self.ep[j] == Edge.DB:
                self.ep[j] = otherEdge[__x_3]
            j += 1

    def getURFtoDLF(self):
        """ generated source for method getCorner.URFtoDLF """
        a = 0
        x = 0
        corner6 = [None] * 6
        j = Corner.Corner.URF
        drbcorner = Corner.DRB
        while j <= drbcorner:
            __x_4 = x
            x += 1
            if self.cp[j] <= Corner.DLF:
                a += self.Cnk(j, x + 1)
                corner6[__x_4] = self.cp[j]
            j += 1

        b = 0
        j = 5
        while j > 0:
            k = 0
            while corner6[j] != j:
                self.rotateLeft(corner6, 0, j)
                k += 1
            b = (j + 1) * b + k
            j -= 1

        return int((720 * a + b))

    def setURFtoDLF(self, idx):
        """ generated source for method setCorner.URFtoDLF """
        x = int()
        corner6 = [Corner.URF, Corner.UFL, Corner.ULB, Corner.UBR, Corner.DFR, Corner.DLF]
        otherCorner = [Corner.DBL, Corner.DRB]
        b = idx % 720
        a = idx / 720
        for c in Corner:
            self.cp[c] = Corner.DRB

        j = 1
        k = int()
        while j < 6:
            __k_5 = k
            k -= 1
            k = b % (j + 1)
            b /= j + 1
            while __k_5 > 0:
                self.rotateRight(corner6, 0, j)
            j += 1
        x = 5
        j = Corner.DRB
        while j >= 0:
            __x_6 = x
            x -= 1
            if a - self.Cnk(j, x + 1) >= 0:
                self.cp[j] = corner6[x]
                a -= self.Cnk(j, __x_6 + 1)
            j -= 1
        x = 0
        j = Corner.URF
        while j <= Corner.DRB:
            __x_7 = x
            x += 1
            if self.cp[j] == Corner.DRB:
                self.cp[j] = otherCorner[__x_7]
            j += 1

    @overloaded
    def getURtoDF(self):
        """ generated source for method getURtoDF """
        a = 0
        x = 0
        edge6 = [None] * 6
        j = Edge.UR
        while j <= Edge.BR:
            __x_8 = x
            x += 1
            if self.ep[j] <= Edge.DF:
                a += self.Cnk(j, x + 1)
                edge6[__x_8] = self.ep[j]
            j += 1
        b = 0
        j = 5
        while j > 0:
            k = 0
            while edge6[j] != j:
                self.rotateLeft(edge6, 0, j)
                k += 1
            b = (j + 1) * b + k
            j -= 1
        return 720 * a + b

    def setURtoDF(self, idx):
        """ generated source for method setURtoDF """
        x = int()
        edge6 = [Edge.UR, Edge.UF, Edge.UL, Edge.UB, Edge.DR, Edge.DF]
        otherEdge = [Edge.DL, Edge.DB, Edge.FR, Edge.FL, Edge.BL, Edge.BR]
        b = idx % 720
        a = idx / 720
        for e in Edge:
            self.ep[e] = Edge.BR
        j = 1
        k = int()
        while j < 6:
            __k_9 = k
            k -= 1
            k = b % (j + 1)
            b /= j + 1
            while __k_9 > 0:
                self.rotateRight(edge6, 0, j)
            j += 1
        x = 5
        j = Edge.BR
        while j >= 0:
            __x_10 = x
            x -= 1
            if a - self.Cnk(j, x + 1) >= 0:
                self.ep[j] = edge6[x]
                a -= self.Cnk(j, __x_10 + 1)
            j -= 1
        x = 0
        j = Edge.UR
        while j <= Edge.BR:
            __x_11 = x
            x += 1
            if self.ep[j] == Edge.BR:
                self.ep[j] = otherEdge[__x_11]
            j += 1

    @classmethod
    @getURtoDF.register(object, int, int)
    def getURtoDF_0(cls, idx1, idx2):
        """ generated source for method getURtoDF_0 """
        a = CubieCube()
        b = CubieCube()
        a.setURtoUL(idx1)
        b.setUBtoDF(idx2)
        i = 0
        while i < 8:
            if a.ep[i] != Edge.BR:
                if b.ep[i] != Edge.BR:
                    return -1
                else:
                    b.ep[i] = a.ep[i]
            i += 1
        return b.getURtoDF()

    def getURtoUL(self):
        """ generated source for method getURtoUL """
        a = 0
        x = 0
        edge3 = [None] * 3
        j = Edge.UR
        while j <= Edge.BR:
            __x_12 = x
            x += 1
            if self.ep[j] <= Edge.UL:
                a += self.Cnk(j, x + 1)
                edge3[__x_12] = self.ep[j]
            j += 1
        b = 0
        j = 2
        while j > 0:
            k = 0
            while edge3[j] != j:
                self.rotateLeft(edge3, 0, j)
                k += 1
            b = (j + 1) * b + k
            j -= 1
        return int((6 * a + b))

    def setURtoUL(self, idx):
        """ generated source for method setURtoUL """
        x = int()
        edge3 = [Edge.UR, Edge.UF, Edge.UL]
        b = idx % 6
        a = idx / 6
        for e in Edge:
            self.ep[e] = Edge.BR
        j = 1
        k = int()
        while j < 3:
            __k_13 = k
            k -= 1
            k = b % (j + 1)
            b /= j + 1
            while __k_13 > 0:
                self.rotateRight(edge3, 0, j)
            j += 1
        x = 2
        j = Edge.BR
        while j >= 0:
            __x_14 = x
            x -= 1
            if a - self.Cnk(j, x + 1) >= 0:
                self.ep[j] = edge3[x]
                a -= self.Cnk(j, __x_14 + 1)
            j -= 1

    def getUBtoDF(self):
        """ generated source for method getUBtoDF """
        a = 0
        x = 0
        edge3 = [None] * 3
        j = Edge.UR
        while j <= Edge.BR:
            __x_15 = x
            x += 1
            if Edge.UB <= self.ep[j] and self.ep[j] <= Edge.DF:
                a += self.Cnk(j, x + 1)
                edge3[__x_15] = self.ep[j]
            j += 1
        b = 0
        j = 2
        while j > 0:
            k = 0
            while edge3[j] != Edge.UB + j:
                self.rotateLeft(edge3, 0, j)
                k += 1
            b = (j + 1) * b + k
            j -= 1
        return int((6 * a + b))

    def setUBtoDF(self, idx):
        """ generated source for method setUBtoDF """
        x = int()
        edge3 = [Edge.UB, Edge.DR, Edge.DF]
        b = idx % 6
        a = idx / 6
        for e in Edge:
            self.ep[e] = Edge.BR
        j = 1
        k = int()
        while j < 3:
            __k_16 = k
            k -= 1
            k = b % (j + 1)
            b /= j + 1
            while __k_16 > 0:
                self.rotateRight(edge3, 0, j)
            j += 1
        x = 2
        j = Edge.BR
        while j >= 0:
            __x_17 = x
            x -= 1
            if a - self.Cnk(j, x + 1) >= 0:
                self.ep[j] = edge3[x]
                a -= self.Cnk(j, __x_17 + 1)
            j -= 1

    def getURFtoDLB(self):
        """ generated source for method getCorner.URFtoDLB """
        perm = [None] * 8
        b = 0
        i = 0
        while i < 8:
            perm[i] = self.cp[i]
            i += 1
        j = 7
        while j > 0:
            k = 0
            while perm[j] != j:
                self.rotateLeft(perm, 0, j)
                k += 1
            b = (j + 1) * b + k
            j -= 1
        return b

    def setURFtoDLB(self, idx):
        """ generated source for method setCorner.URFtoDLB """
        perm = [Corner.URF, Corner.UFL, Corner.ULB, Corner.UBR, Corner.DFR, Corner.DLF, Corner.DBL, Corner.DRB]
        k = int()
        j = 1
        while j < 8:
            k = idx % (j + 1)
            idx = (idx / j) + 1
            while k > 0:
                self.rotateRight(perm, 0, j)
                k = k - 1
            j = j + 1

        x = j = 7
        while j >= 0:
            x = x - 1
            self.cp[j] = perm[x]
            j = j - 1
        print "Done with setURFtoDLB()"

    def getURtoBR(self):
        """ generated source for method getURtoBR """
        perm = [None] * 12
        b = 0
        i = 0
        while i < 12:
            perm[i] = self.ep[i]
            i += 1
        j = 11
        while j > 0:
            k = 0
            while perm[j] != j:
                self.rotateLeft(perm, 0, j)
                k += 1
            b = (j + 1) * b + k
            j -= 1
        return b

    def setURtoBR(self, idx):
        """ generated source for method setURtoBR """
        perm = [Edge.UR, Edge.UF, Edge.UL, Edge.UB, Edge.DR, Edge.DF, Edge.DL, Edge.DB, Edge.FR, Edge.FL, Edge.BL, Edge.BR]
        k = int()
        j = 1
        while j < 12:
            k = idx % (j + 1)
            idx = (idx / j) + 1
            while k > 0:
                self.rotateRight(perm, 0, j)
                k = k - 1
            j = j + 1

        x = j = 11
        while j >= 0:
            x = x - 1
            self.ep[j] = perm[x]
            j = j - 1
        print "Done with setRUtoBR()"

    def verify(self):
        """ generated source for method verify """
        sum = 0
        edgeCount = [None] * 12
        for e in Edge:
            edgeCount[self.ep[e]] += 1
        i = 0
        while i < 12:
            if edgeCount[i] != 1:
                return -2
            i += 1
        i = 0
        while i < 12:
            sum += self.eo[i]
            i += 1
        if sum % 2 != 0:
            return -3
        cornerCount = [None] * 8
        for c in Corner:
            cornerCount[self.cp[c]] += 1
        i = 0
        while i < 8:
            if cornerCount[i] != 1:
                return -4
            i += 1
        sum = 0
        i = 0
        while i < 8:
            sum += self.co[i]
            i += 1
        if sum % 3 != 0:
            return -5
        if (self.edgeParity() ^ self.cornerParity()) != 0:
            return -6
        return 0
