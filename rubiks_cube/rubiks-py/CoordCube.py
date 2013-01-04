#!/usr/bin/env python

from CubieCube import CubieCube


def bsr(value, bits):
    minint = -2147483648
    if bits == 0:
        return value
    elif bits == 31:
        if value & minint:
            return 1
        else:
            return 0
    elif bits < 0 or bits > 31:
        raise ValueError('bad shift count')
    tmp = (value & 0x7FFFFFFE) // 2 ** bits
    if (value & minint):
        return (tmp | (0x40000000 // 2 ** (bits - 1)))
    else:
        return tmp


class CoordCube(object):
    """ generated source for class CoordCube """
    N_TWIST = 2187

    #  3^7 possible corner orientations
    N_FLIP = 2048

    #  2^11 possible edge flips
    N_SLICE1 = 495

    #  12 choose 4 possible positions of FR,FL,BL,BR edges
    N_SLICE2 = 24

    #  4! permutations of FR,FL,BL,BR edges in phase2
    N_PARITY = 2

    #  2 possible corner parities
    N_URFtoDLF = 20160

    #  8!/(8-6)! permutation of URF,UFL,ULB,UBR,DFR,DLF corners
    N_FRtoBR = 11880

    #  12!/(12-4)! permutation of FR,FL,BL,BR edges
    N_URtoUL = 1320

    #  12!/(12-3)! permutation of UR,UF,UL edges
    N_UBtoDF = 1320

    #  12!/(12-3)! permutation of UB,DR,DF edges
    N_URtoDF = 20160

    #  8!/(8-6)! permutation of UR,UF,UL,UB,DR,DF edges in phase2
    N_URFtoDLB = 40320

    #  8! permutations of the corners
    N_URtoBR = 479001600

    #  8! permutations of the corners
    N_MOVE = 18

    #  All coordinates are 0 for a solved cube except for UBtoDF, which is 114
    twist = int()
    flip = int()
    parity = int()
    FRtoBR = int()
    URFtoDLF = int()
    URtoUL = int()
    UBtoDF = int()
    URtoDF = int()

    #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #  Generate a CoordCube from a CubieCube
    def __init__(self, c):
        """ generated source for method __init__ """
        self.twist = c.getTwist()
        self.flip = c.getFlip()
        self.parity = c.cornerParity()
        self.FRtoBR = c.getFRtoBR()
        self.URFtoDLF = c.getURFtoDLF()
        self.URtoUL = c.getURtoUL()
        self.UBtoDF = c.getUBtoDF()
        self.URtoDF = c.getURtoDF()
        #  only needed in phase2

    #  A move on the coordinate level
    #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    def move(self, m):
        """ generated source for method move """
        self.twist = self.twistMove[self.twist][m]
        self.flip = self.flipMove[self.flip][m]
        self.parity = self.parityMove[self.parity][m]
        self.FRtoBR = self.FRtoBR_Move[self.FRtoBR][m]
        self.URFtoDLF = self.URFtoDLF_Move[self.URFtoDLF][m]
        self.URtoUL = self.URtoUL_Move[self.URtoUL][m]
        self.UBtoDF = self.UBtoDF_Move[self.UBtoDF][m]
        if self.URtoUL < 336 and self.UBtoDF < 336:
            self.URtoDF = self.MergeURtoULandUBtoDF[self.URtoUL][self.UBtoDF]

    def twistMove(self):
        a = CubieCube()
        for i in range(self.N_TWIST):
            a.setTwist(i)
            for j in range(6):
                for k in range(3):
                    a.cornerMultiply(CubieCube.moveCube(j))
                    self.twistMove[i][3 * j + k] = a.getTwist()
                a.cornerMultiply(CubieCube.moveCube[j])

    def flipMove(self):
        a = CubieCube()
        i = 0
        j = 0
        k = 0

    def parityMove(self):
        pass

    def FRtoBR_Move(self):
        a = CubieCube()
        i = 0
        j = 0
        k = 0

    def URFtoDLF_Move(self):
        a = CubieCube()
        i = 0
        j = 0
        k = 0

    def URtoDF_Move(self):
        a = CubieCube()
        i = 0
        j = 0
        k = 0

    def URtoUL_Move(self):
        a = CubieCube()
        i = 0
        j = 0
        k = 0

    def UBtoDF_Move(self):
        a = CubieCube()
        i = 0
        j = 0
        k = 0

    def MergeURtoULandUBtoDF(self):
        uRtoUL = 0
        uBtoDF = 0

    def Slice_URFtoDLF_Parity_Prun(self):
        i = 0
        depth = 0
        done = 1
        i = 0
        parity = i % 2

        URFtoDLF = (i / 2) / N_SLICE2
        slice_ = (i / 2) % N_SLICE2
        j = 0
        newSlice = FRtoBR_Move[slice_][j]
        newURFtoDLF = URFtoDLF_Move[URFtoDLF][j]
        newParity = parityMove[parity][j]

    def Slice_URtoDF_Parity_Prun(self):
        i = 0
        depth = 0
        done = 1
        i = 0
        parity = i % 2
        URtoDF = (i / 2) / N_SLICE2
        slice_ = (i / 2) % N_SLICE2
        j = 0
        newSlice = FRtoBR_Move[slice_][j]
        newURtoDF = URtoDF_Move[URtoDF][j]
        newParity = parityMove[parity][j]

    def Slice_Twist_Prun(self):
        i = 0
        depth = 0
        done = 1
        i = 0
        twist = i / N_SLICE1
        slice_ = i % N_SLICE1
        j = 0
        newSlice = FRtoBR_Move[slice_ * 24][j] / 24
        newTwist = twistMove[twist][j]

    def Slice_Flip_Prun(self):
        i = 0
        depth = 0
        done = 1
        i = 0
        flip = i / N_SLICE1
        slice_ = i % N_SLICE1
        j = 0
        newSlice = FRtoBR_Move[slice_ * 24][j] / 24
        newFlip = flipMove[flip][j]

    @classmethod
    def setPruning(cls, table, index, value):
        """ generated source for method setPruning """
        if (index & 1) == 0:
            table[index / 2] &= 0xf0 | value
        else:
            table[index / 2] &= 0x0f | (value << 4)

    @classmethod
    def getPruning(cls, table, index):
        """ generated source for method getPruning """
        if (index & 1) == 0:
            return int((table[index / 2] & 0x0f))
        else:
            return int((bsr((table[index / 2] & 0xf0), 4)))
