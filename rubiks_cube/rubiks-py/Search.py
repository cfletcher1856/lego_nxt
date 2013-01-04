#!/usr/bin/env python


class Search(object):
    """ generated source for class Search """
    ax = [None] * 31

    #  The axis of the move
    po = [None] * 31

    #  The power of the move
    flip = [None] * 31

    #  phase1 coordinates
    twist = [None] * 31
    slice_ = [None] * 31
    parity = [None] * 31

    #  phase2 coordinates
    URFtoDLF = [None] * 31
    FRtoBR = [None] * 31
    URtoUL = [None] * 31
    UBtoDF = [None] * 31
    URtoDF = [None] * 31
    minDistPhase1 = [None] * 31

    #  IDA* distance do goal estimations
    minDistPhase2 = [None] * 31

    #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #  generate the solution string from the array data
    @classmethod
    @overloaded
    def solutionToString(cls, length):
        """ generated source for method solutionToString """
        s = ""
        i = 0
        while i < length:
            if cls.ax[i] == 0:
                s += "U"
            elif cls.ax[i] == 1:
                s += "R"
            elif cls.ax[i] == 2:
                s += "F"
            elif cls.ax[i] == 3:
                s += "D"
            elif cls.ax[i] == 4:
                s += "L"
            elif cls.ax[i] == 5:
                s += "B"
            if cls.po[i] == 1:
                s += " "
            elif cls.po[i] == 2:
                s += "2 "
            elif cls.po[i] == 3:
                s += "' "
            i += 1
        return s

    #  ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    #  generate the solution string from the array data including a separator between phase1 and phase2 moves
    @classmethod
    @solutionToString.register(object, int, int)
    def solutionToString_0(cls, length, depthPhase1):
        """ generated source for method solutionToString_0 """
        s = ""
        i = 0
        while i < length:
            if cls.ax[i] == 0:
                s += "U"
            elif cls.ax[i] == 1:
                s += "R"
            elif cls.ax[i] == 2:
                s += "F"
            elif cls.ax[i] == 3:
                s += "D"
            elif cls.ax[i] == 4:
                s += "L"
            elif cls.ax[i] == 5:
                s += "B"
            if cls.po[i] == 1:
                s += " "
            elif cls.po[i] == 2:
                s += "2 "
            elif cls.po[i] == 3:
                s += "' "
            if i == depthPhase1 - 1:
                s += ". "
            i += 1
        return s

    #
    # 	 * Computes the solver string for a given cube.
    # 	 *
    # 	 * @param facelets
    # 	 *          is the cube definition string, see {@link Facelet} for the format.
    # 	 *
    # 	 * @param maxDepth
    # 	 *          defines the maximal allowed maneuver length. For random cubes, a maxDepth of 21 usually will return a
    # 	 *          solution in less than 0.5 seconds. With a maxDepth of 20 it takes a few seconds on average to find a
    # 	 *          solution, but it may take much longer for specific cubes.
    # 	 *
    # 	 *@param timeOut
    # 	 *          defines the maximum computing time of the method in seconds. If it does not return with a solution, it returns with
    # 	 *          an error code.
    # 	 *
    # 	 * @param useSeparator
    # 	 *          determines if a " . " separates the phase1 and phase2 parts of the solver string like in F' R B R L2 F .
    # 	 *          U2 U D for example.<br>
    # 	 * @return The solution string or an error code:<br>
    # 	 *         Error 1: There is not exactly one facelet of each colour<br>
    # 	 *         Error 2: Not all 12 edges exist exactly once<br>
    # 	 *         Error 3: Flip error: One edge has to be flipped<br>
    # 	 *         Error 4: Not all corners exist exactly once<br>
    # 	 *         Error 5: Twist error: One corner has to be twisted<br>
    # 	 *         Error 6: Parity error: Two corners or two edges have to be exchanged<br>
    # 	 *         Error 7: No solution exists for the given maxDepth<br>
    # 	 *         Error 8: Timeout, no solution within given time
    #
    @classmethod
    def solution(cls, facelets, maxDepth, timeOut, useSeparator):
        """ generated source for method solution """
        s = int()
        #  +++++++++++++++++++++check for wrong input +++++++++++++++++++++++++++++
        count = [None] * 6
        try:
            while i < 54:
                count[Color.valueOf(facelets.substring(i, i + 1)).ordinal()] += 1
                i += 1
        except Exception as e:
            return "Error 1"
        i = 0
        while i < 6:
            if count[i] != 9:
                return "Error 1"
            i += 1
        fc = FaceCube(facelets)
        cc = fc.toCubieCube()
        s = cc.verify()
        if s != 0:
            return "Error " + Math.abs(s)
        c = CoordCube(cc)
        cls.po[0] = 0
        cls.ax[0] = 0
        cls.flip[0] = c.flip
        cls.twist[0] = c.twist
        cls.parity[0] = c.parity
        cls.slice_[0] = c.FRtoBR / 24
        cls.URFtoDLF[0] = c.URFtoDLF
        cls.FRtoBR[0] = c.FRtoBR
        cls.URtoUL[0] = c.URtoUL
        cls.UBtoDF[0] = c.UBtoDF
        cls.minDistPhase1[1] = 1
        mv = 0
        n = 0
        busy = False
        depthPhase1 = 1
        tStart = System.currentTimeMillis()
        n += 1
        n += 1
        while True:
            while True:
                if (depthPhase1 - n > cls.minDistPhase1[n + 1]) and not busy:
                    if cls.ax[n] == 0 or cls.ax[n] == 3:
                        cls.ax[n] = 1
                    else:
                        cls.ax[n] = 0
                    cls.po[n] = 1
                elif (cls.po[n] += 1) > 3:
                    while True:
                        if (cls.ax[n] += 1) > 5:
                            if System.currentTimeMillis() - tStart > timeOut << 10:
                                return "Error 8"
                            if n == 0:
                                if depthPhase1 >= maxDepth:
                                    return "Error 7"
                                else:
                                    depthPhase1 += 1
                                    cls.ax[n] = 0
                                    cls.po[n] = 1
                                    busy = False
                                    break
                            else:
                                n -= 1
                                busy = True
                                break
                        else:
                            cls.po[n] = 1
                            busy = False
                        if not ((n != 0 and (cls.ax[n - 1] == cls.ax[n] or cls.ax[n - 1] - 3 == cls.ax[n]))):
                            break
                else:
                    busy = False
                if not ((busy)):
                    break
            mv = 3 * cls.ax[n] + cls.po[n] - 1
            cls.flip[n + 1] = CoordCube.flipMove[cls.flip[n]][mv]
            cls.twist[n + 1] = CoordCube.twistMove[cls.twist[n]][mv]
            cls.slice_[n + 1] = CoordCube.FRtoBR_Move[cls.slice_[n] * 24][mv] / 24
            cls.minDistPhase1[n + 1] = Math.max(CoordCube.getPruning(CoordCube.Slice_Flip_Prun, CoordCube.N_SLICE1 * cls.flip[n + 1] + cls.slice_[n + 1]), CoordCube.getPruning(CoordCube.Slice_Twist_Prun, CoordCube.N_SLICE1 * cls.twist[n + 1] + cls.slice_[n + 1]))
            if cls.minDistPhase1[n + 1] == 0 and n >= depthPhase1 - 5:
                cls.minDistPhase1[n + 1] = 10
                if n == depthPhase1 - 1 and (s = totalDepth(depthPhase1, maxDepth)) >= 0:
                    if s == depthPhase1 or (cls.ax[depthPhase1 - 1] != cls.ax[depthPhase1] and cls.ax[depthPhase1 - 1] != cls.ax[depthPhase1] + 3):
                        return cls.solutionToString(s, depthPhase1) if useSeparator else cls.solutionToString(s)
            if not ((True)):
                break

    @classmethod
    def totalDepth(cls, depthPhase1, maxDepth):
        """ generated source for method totalDepth """
        mv = 0
        d1 = 0
        d2 = 0
        maxDepthPhase2 = Math.min(10, maxDepth - depthPhase1)
        i = 0
        while i < depthPhase1:
            mv = 3 * cls.ax[i] + cls.po[i] - 1
            cls.URFtoDLF[i + 1] = CoordCube.URFtoDLF_Move[cls.URFtoDLF[i]][mv]
            cls.FRtoBR[i + 1] = CoordCube.FRtoBR_Move[cls.FRtoBR[i]][mv]
            cls.parity[i + 1] = CoordCube.parityMove[cls.parity[i]][mv]
            i += 1
        if (d1 = CoordCube.getPruning(CoordCube.Slice_URFtoDLF_Parity_Prun, (CoordCube.N_SLICE2 * cls.URFtoDLF[depthPhase1] + cls.FRtoBR[depthPhase1]) * 2 + cls.parity[depthPhase1])) > maxDepthPhase2:
            return -1
        i = 0
        while i < depthPhase1:
            mv = 3 * cls.ax[i] + cls.po[i] - 1
            cls.URtoUL[i + 1] = CoordCube.URtoUL_Move[cls.URtoUL[i]][mv]
            cls.UBtoDF[i + 1] = CoordCube.UBtoDF_Move[cls.UBtoDF[i]][mv]
            i += 1
        cls.URtoDF[depthPhase1] = CoordCube.MergeURtoULandUBtoDF[cls.URtoUL[depthPhase1]][cls.UBtoDF[depthPhase1]]
        if (d2 = CoordCube.getPruning(CoordCube.Slice_URtoDF_Parity_Prun, (CoordCube.N_SLICE2 * cls.URtoDF[depthPhase1] + cls.FRtoBR[depthPhase1]) * 2 + cls.parity[depthPhase1])) > maxDepthPhase2:
            return -1
        if (cls.minDistPhase2[depthPhase1] = Math.max(d1, d2)) == 0:
            return depthPhase1
        depthPhase2 = 1
        n = depthPhase1
        busy = False
        cls.po[depthPhase1] = 0
        cls.ax[depthPhase1] = 0
        cls.minDistPhase2[n + 1] = 1
        n += 1
        n += 1
        while True:
            while True:
                if (depthPhase1 + depthPhase2 - n > cls.minDistPhase2[n + 1]) and not busy:
                    if cls.ax[n] == 0 or cls.ax[n] == 3:
                        cls.ax[n] = 1
                        cls.po[n] = 2
                    else:
                        cls.ax[n] = 0
                        cls.po[n] = 1
                elif ((cls.po[n] += 1) > 3) if (cls.ax[n] == 0 or cls.ax[n] == 3) else ((cls.po[n] = cls.po[n] + 2) > 3):
                    while True:
                        if (cls.ax[n] += 1) > 5:
                            if n == depthPhase1:
                                if depthPhase2 >= maxDepthPhase2:
                                    return -1
                                else:
                                    depthPhase2 += 1
                                    cls.ax[n] = 0
                                    cls.po[n] = 1
                                    busy = False
                                    break
                            else:
                                n -= 1
                                busy = True
                                break
                        else:
                            if cls.ax[n] == 0 or cls.ax[n] == 3:
                                cls.po[n] = 1
                            else:
                                cls.po[n] = 2
                            busy = False
                        if not ((n != depthPhase1 and (cls.ax[n - 1] == cls.ax[n] or cls.ax[n - 1] - 3 == cls.ax[n]))):
                            break
                else:
                    busy = False
                if not ((busy)):
                    break
            mv = 3 * cls.ax[n] + cls.po[n] - 1
            cls.URFtoDLF[n + 1] = CoordCube.URFtoDLF_Move[cls.URFtoDLF[n]][mv]
            cls.FRtoBR[n + 1] = CoordCube.FRtoBR_Move[cls.FRtoBR[n]][mv]
            cls.parity[n + 1] = CoordCube.parityMove[cls.parity[n]][mv]
            cls.URtoDF[n + 1] = CoordCube.URtoDF_Move[cls.URtoDF[n]][mv]
            cls.minDistPhase2[n + 1] = Math.max(CoordCube.getPruning(CoordCube.Slice_URtoDF_Parity_Prun, (CoordCube.N_SLICE2 * cls.URtoDF[n + 1] + cls.FRtoBR[n + 1]) * 2 + cls.parity[n + 1]), CoordCube.getPruning(CoordCube.Slice_URFtoDLF_Parity_Prun, (CoordCube.N_SLICE2 * cls.URFtoDLF[n + 1] + cls.FRtoBR[n + 1]) * 2 + cls.parity[n + 1]))
            if not ((cls.minDistPhase2[n + 1] != 0)):
                break
        return depthPhase1 + depthPhase2
