# Project Description

**A python package for solving 1D kinematics problems.**

## Installation

```
pip install kinematics5
```

## Inspiration

As a high school AP physics tutor, I wanted to make a python package for solving kinematics problems.

## Modules & Functions

**Below are function definitions from the ```OneD``` module. The ```OneD``` module contains 4 functions. They represent the 4 kinematic equations.**

### eq1

*Function Signature*
```
def eq1(vi: Optional[int | float] = None,
        vf: Optional[int | float] = None,
        a: Optional[int | float] = None,
        t: Optional[int | float] = None) -> tuple | bool:
```

The first kinematic equation. Below is the equation:

vf = vi + at

*Overview:*
The function needs at least 3 arguments but can take 4. If less than 3 arguments are given, the function will raise an error. If 3 arguments are given, the function will return a tuple of all 4 arguments (the arg. that wasn't given is computed and returned in the tuple). If 4 arguments are given the function will return a bool ```True/False``` letting the caller know if the 4 values they entered satisfy the equation (1% error).

### eq2

*Function Signature*
```
def eq2(d: Optional[int | float] = None,
        vi: Optional[int | float] = None,
        vf: Optional[int | float] = None,
        t: Optional[int | float] = None) -> tuple | bool:
```

The second kinematic equation. Below is the equation:

d = (vf + vi) * t/2

The function accepts integers or floats.

*Overview:*
The function needs at least 3 arguments but can take 4. If less than 3 arguments are given, the function will raise an error. If 3 arguments are given, the function will return a tuple of all 4 arguments (the arg. that wasn't given is computed and returned in the tuple). If 4 arguments are given the function will return a bool ```True/False``` letting the caller know if the 4 values they entered satisfy the equation (1% error).

### eq3

*Function Signature*
```
def eq3(d: Optional[int | float] = None,
        vi: Optional[int | float] = None,
        a: Optional[int | float] = None,
        t: Optional[int | float] = None) -> tuple | bool:
```

The third kinematic equation. Below is the equation:

### eq4

*Function Signature*
```
def eq4(d: Optional[int | float] = None,
        vi: Optional[int | float] = None,
        vf: Optional[int | float] = None,
        a: Optional[int | float] = None) -> tuple | bool:
```

The fourth kinematic equation. Below is the equation:


## PyPI Link

This is the link to the package on PyPI [PyPI - kinematics5](https://pypi.org/project/kinematics5/).

## Lastest Version

0.0.3

## License

Distributed under the terms of the MIT license, ```kinematics5``` is free and open source software.