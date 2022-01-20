from typing import Optional

def __argCount(local: dict) -> None:
    var_count = 0
    for key in local:
        if local[key] is not None:
            var_count += 1
    
    if var_count < 3:
        raise Exception(f'Need at least 3 args: [{var_count}]')

# FIRST KINEMATIC EQUATION: vf = vi + at
# If 3/4 arguments are given, returns a tuple of all 4 variables.
# If 4/4 arguments are given, returns true/false if the 4 variables are actually a solution.
def eq1(vi: Optional[int | float] = None,
        vf: Optional[int | float] = None,
        a: Optional[int | float] = None,
        t: Optional[int | float] = None) -> tuple | bool:
    
    __argCount(locals())
    
    if t and t < 0:
        raise Exception(f'The time you entered is negative: [{t}]')


    if vi is None:
        vi = vf - (a * t)
    
    elif vf is None:
        vf = vi + (a * t)
    
    elif a is None:
        a = (vf - vi) / float(t)
    
    elif t is None:  
        t = (vf - vi) / float(a)
        
        if t < 0:
            raise Exception(f'Time is Negative: [{t}]')

    else:
        _vf = vi + (a * t)
        err = _vf * 0.01

        if abs(vf - _vf) <= err:
            return True
        
        return False
  
    return (float(vi), float(vf), float(a), float(t))


# SECOND KINEMATIC EQUATION: d = [(vf + vi) / 2] * t
# If 3/4 arguments are given, returns a tuple of all 4 variables.
# If 4/4 arguments are given, returns true/false if the 4 variables are actually a solution.
def eq2(d: Optional[int | float] = None,
        vi: Optional[int | float] = None,
        vf: Optional[int | float] = None,
        t: Optional[int | float] = None) -> tuple | bool:
    
    __argCount(locals())
    
    if t and t < 0:
        raise Exception(f'The time you entered is negative: [{t}]')
    

    if d is None:
        d = ((vf + vi) / 2) * t
    
    elif vi is None:
        vi = ((2 * d) / float(t)) - vf
    
    elif vf is None:
        vf = ((2 * d) / float(t)) - vi
    
    elif t is None:  
        t = (2 * d) / float(vf + vi)
        
        if t < 0:
            raise Exception(f'Time is Negative: [{t}]')

    else:
        _d = ((vf + vi) / 2) * t
        err = _d * 0.01

        if abs(d - _d) <= err:
            return True
        
        return False
    
    return (float(d), float(vi), float(vf), float(t))


# THIRD KINEMATIC EQUATION: d = (vi * t) + [(0.5) * a * (t ^ 2)]
# If 3/4 arguments are given, returns a tuple of all 4 variables. If t is not know, it'll return 2 values of t.
# If 4/4 arguments are given, returns true/false if the 4 variables are actually a solution.
def eq3(d: Optional[int | float] = None,
        vi: Optional[int | float] = None,
        a: Optional[int | float] = None,
        t: Optional[int | float] = None) -> tuple | bool:
    
    __argCount(locals())
    
    if t and t < 0:
        raise Exception(f'The time you entered is negative: [{t}]')
    

    if d is None:
        d = (vi * t) + (0.5 * a * t * t)

    elif vi is None:
        vi = (d - (0.5 * a * t * t)) / float(t)
    
    elif a is None:
        a = (2 * (d - (vi * t))) / float(t * t)
    
    elif t is None:  
        rad = ((vi**2) + (2 * a * d))

        if rad < 0:
            raise ValueError(f'Time Will be a Complex Number.')

        t1 = ((-1 * vi) + (rad ** 0.5)) / float(a)
        t2 = ((-1 * vi) - (rad ** 0.5)) / float(a)

        if t1 > t2:
            t = [t2, t1]
        else:
            t = [t1, t2]
        
        return (float(d), float(vi), float(a), [float(t[0]),float(t[1])])

    else:
        _d = (vi * t) + (0.5 * a * (t ** 2))
        err = _d * 0.01

        if abs(d - _d) <= err:
            return True
        
        return False

    return (float(d), float(vi), float(a), float(t))


# FOURTH KINEMATIC EQUATION: [vf ^ 2] = [vi ^ 2] + [2 * a * d]
# If 3/4 arguments are given, returns a tuple of all 4 variables. If vi or vf are not know, it'll return 2 values of vi or vf.
# If 4/4 arguments are given, returns true/false if the 4 variables are actually a solution.
def eq4(d: Optional[int | float] = None,
        vi: Optional[int | float] = None,
        vf: Optional[int | float] = None,
        a: Optional[int | float] = None) -> tuple | bool:
    
    __argCount(locals())

    if d is None:
        d = ((vf ** 2) - (vi ** 2)) / float(2 * a)

    elif vi is None:
        rad = (vf ** 2) - (2 * a * d)

        if rad < 0:
            raise ValueError(f'Initial Velocity Will be a Complex Number.')

        vi1 = rad ** 0.5
        vi2 = -1 * (rad ** 0.5)

        if vi1 > vi2:
            vi = [vi2, vi1]
        else:
            vi = [vi1, vi2]
        
        return (float(d), [float(vi[0]),float(vi[1])], float(vf), float(a))

    elif vf is None:
        rad = (vi ** 2) + (2 * a * d)

        if rad < 0:
            raise ValueError(f'Final Velocity Will be a Complex Number.')

        vf1 = rad ** 0.5
        vf2 = -1 * (rad ** 0.5)

        if vf1 > vf2:
            vf = [vf2, vf1]
        else:
            vf = [vf1, vf2]
        
        return (float(d), float(vi), [float(vf[0]),float(vf[1])], float(a))
    
    elif a is None:
        a = ((vf ** 2) - (vi ** 2)) / float(2 * d)
    
    else:
        _d = ((vf ** 2) - (vi ** 2)) / float(2 * a)
        err = _d * 0.01
        
        if abs(d - _d) <= err:
            return True
        
        return False
    
    return (float(d), float(vi), float(vf), float(a))