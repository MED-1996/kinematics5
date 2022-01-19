from typing import Optional

def argCount(local: dict) -> None:
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
    
    argCount(locals())
    
    if t and t < 0:
        raise Exception(f'The time you entered is negative: [{t}]')


    if vi is None:
        vi = vf - (a * t)
    
    elif vf is None:
        vf = vi + (a * t)
    
    elif a is None:
        a = (vf - vi) / t
    
    elif t is None:  
        t = (vf - vi) / a
        
        if t < 0:
            raise Exception(f'Time is Negative: [{t}]')

    else:
        _vf = vi + (a * t)

        if abs(float(round(vf,5)) - float(round(_vf,5))) <= 0.2:
            return True
        
        return False
  
    return (float(round(vi,5)), float(round(vf,5)), float(round(a,5)), float(round(t,5)))


# SECOND KINEMATIC EQUATION: d = [(vf + vi) / 2] * t
# If 3/4 arguments are given, returns a tuple of all 4 variables.
# If 4/4 arguments are given, returns true/false if the 4 variables are actually a solution.
def eq2(d: Optional[int | float] = None,
        vi: Optional[int | float] = None,
        vf: Optional[int | float] = None,
        t: Optional[int | float] = None) -> tuple | bool:
    
    argCount(locals())
    
    if t and t < 0:
        raise Exception(f'The time you entered is negative: [{t}]')
    

    if d is None:
        d = ((vf + vi) / 2) * t
    
    elif vi is None:
        vi = ((2 * d) / t) - vf
    
    elif vf is None:
        vf = ((2 * d) / t) - vi
    
    elif t is None:  
        t = (2 * d) / (vf + vi)
        
        if t < 0:
            raise Exception(f'Time is Negative: [{t}]')

    else:
        _d = ((vf + vi) / 2) * t

        if abs(float(round(d,5)) - float(round(_d,5))) <= 0.2:
            return True
        
        return False
    
    return (float(round(d,5)), float(round(vi,5)), float(round(vf,5)), float(round(t,5)))


# THIRD KINEMATIC EQUATION: d = (vi * t) + [(0.5) * a * (t ^ 2)]
# If 3/4 arguments are given, returns a tuple of all 4 variables. If t is not know, it'll return 2 values of t.
# If 4/4 arguments are given, returns true/false if the 4 variables are actually a solution.
def eq3(d: Optional[int | float] = None,
        vi: Optional[int | float] = None,
        a: Optional[int | float] = None,
        t: Optional[int | float] = None) -> tuple | bool:
    
    argCount(locals())
    
    if t and t < 0:
        raise Exception(f'The time you entered is negative: [{t}]')
    

    if d is None:
        d = (vi * t) + (0.5 * a * t * t)

    elif vi is None:
        vi = (d - (0.5 * a * t * t)) / t
    
    elif a is None:
        a = (2 * (d - (vi * t))) / (t * t)
    
    elif t is None:  
        rad = ((vi**2) + (2 * a * d))

        if rad < 0:
            raise ValueError(f'Time Will be a Complex Number.')

        t1 = ((-1 * vi) + (rad ** 0.5)) / a
        t2 = ((-1 * vi) - (rad ** 0.5)) / a

        if t1 > t2:
            t = [t2, t1]
        else:
            t = [t1, t2]
        
        return (float(round(d,5)), float(round(vi,5)), float(round(a,5)), [float(round(t[0],5)),float(round(t[1],5))])

    else:
        _d = (vi * t) + (0.5 * a * (t ** 2))

        if abs(float(round(d,5)) - float(round(_d,5))) <= 0.2:
            return True
        
        return False

    return (float(round(d,5)), float(round(vi,5)), float(round(a,5)), float(round(t,5)))



def eq4():
    pass

