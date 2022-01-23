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

*Kinematic Equation:*

v<sub>f</sub> = v<sub>i</sub> + at

*Overview:*
The function needs at least 3 arguments but can take 4. If 't' is less than 0, an error will be raised. If less than 3 arguments are given, an error will be raised. If 3 arguments are given, the function will return a tuple of all 4 arguments (the arg. that wasn't given is computed and returned in the tuple). If 4 arguments are given the function will return a bool letting the caller know if the 4 values they entered satisfy the equation (1% error tolerance).

### eq2

*Function Signature*
```
def eq2(d: Optional[int | float] = None,
        vi: Optional[int | float] = None,
        vf: Optional[int | float] = None,
        t: Optional[int | float] = None) -> tuple | bool:
```

*Kinematic Equation:*

d = (v<sub>f</sub> + v<sub>i</sub>)t / 2

*Overview:*
The function needs at least 3 arguments but can take 4. If 't' is less than 0, an error will be raised. If less than 3 arguments are given, an error will be raised. If 3 arguments are given, the function will return a tuple of all 4 arguments (the arg. that wasn't given is computed and returned in the tuple). If 4 arguments are given the function will return a bool letting the caller know if the 4 values they entered satisfy the equation (1% error tolerance).

### eq3

*Function Signature*
```
def eq3(d: Optional[int | float] = None,
        vi: Optional[int | float] = None,
        a: Optional[int | float] = None,
        t: Optional[int | float] = None) -> tuple | bool:
```

*Kinematic Equation:*

d = v<sub>i</sub>t + (0.5)at<sup>2</sup>

*Overview:*
The function needs at least 3 arguments but can take 4. If 't' is less than 0, an error will be raised. If less than 3 arguments are given, an error will be raised. If 3 arguments are given, the function will return a tuple of all 4 arguments (the arg. that wasn't given is computed and returned in the tuple). If 't' was the missing variable, t will be returned as a list with 2 elements. If 4 arguments are given the function will return a bool letting the caller know if the 4 values they entered satisfy the equation (1% error tolerance).

### eq4

*Function Signature*
```
def eq4(d: Optional[int | float] = None,
        vi: Optional[int | float] = None,
        vf: Optional[int | float] = None,
        a: Optional[int | float] = None) -> tuple | bool:
```

*Kinematic Equation:*

v<sub>f</sub><sup>2</sup> = v<sub>i</sub><sup>2</sup> + 2ad

*Overview:*
The function needs at least 3 arguments but can take 4. If less than 3 arguments are given, an error will be raised. If 3 arguments are given, the function will return a tuple of all 4 arguments (the arg. that wasn't given is computed and returned in the tuple). If 'vi' or 'vf' was the missing variable, they will be returned as a list with 2 elements. If 4 arguments are given the function will return a bool letting the caller know if the 4 values they entered satisfy the equation (1% error tolerance).


## PyPI Link

Link to the package [PyPI - kinematics5](https://pypi.org/project/kinematics5/).

## Lastest Version

0.0.3

## License

Distributed under the terms of the MIT license, ```kinematics5``` is free and open source software.