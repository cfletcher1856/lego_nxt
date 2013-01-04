#!/usr/bin/env python

from Color import Color
from FaceCube import FaceCube
from CubieCube import CubieCube
from CoordCube import CoordCube


class Tools(object):
    """ generated source for class Tools """
    #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #  Check if the cube string s represents a solvable cube.
    #  0: Cube is solvable
    #  -1: There is not exactly one facelet of each colour
    #  -2: Not all 12 edges exist exactly once
    #  -3: Flip error: One edge has to be flipped
    #  -4: Not all corners exist exactly once
    #  -5: Twist error: One corner has to be twisted
    #  -6: Parity error: Two corners or two edges have to be exchanged
    #
    #
    # 	 * Check if the cube definition string s represents a solvable cube.
    # 	 *
    # 	 * @param s is the cube definition string , see {@link Facelet}
    # 	 * @return 0: Cube is solvable<br>
    # 	 *         -1: There is not exactly one facelet of each colour<br>
    # 	 *         -2: Not all 12 edges exist exactly once<br>
    # 	 *         -3: Flip error: One edge has to be flipped<br>
    # 	 *         -4: Not all 8 corners exist exactly once<br>
    # 	 *         -5: Twist error: One corner has to be twisted<br>
    # 	 *         -6: Parity error: Two corners or two edges have to be exchanged
    #
    @classmethod
    def verify(self, s):
        """ generated source for method verify """
        count = [None] * 6
        try:
            i = 0
            while i < 54:
                count[Color.valueOf(s.substring(i, i + 1)).ordinal()] += 1
                i += 1
        except:
            return -1

        i = 0
        while i < 6:
            if count[i] != 9:
                return -1
            i += 1
        fc = FaceCube(s)
        cc = fc.toCubieCube()
        return cc.verify()

    @classmethod
    def randomCube(self):
        import random

        """ generated source for method randomCube """
        cc = CubieCube()
        cc.setFlip(int(random.randint(0, CoordCube.N_FLIP)))
        cc.setTwist(int(random.randint(0, CoordCube.N_TWIST)))
        while True:
            cc.setURFtoDLB(random.randint(0, CoordCube.N_URFtoDLB))
            cc.setURtoBR(random.randint(0, CoordCube.N_URtoBR))
            if not (((cc.edgeParity() ^ cc.cornerParity()) != 0)):
                break
        fc = cc.toFaceCube()
        return fc.to_String()
