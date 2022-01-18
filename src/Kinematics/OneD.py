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
        t: Optional[int | float] = None) -> tuple[float,float,float,float] | bool:
    
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



def eq2():
    pass

def eq3():
    pass

def eq4():
    pass

