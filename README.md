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

![equation1_image](http://www.sciweavers.org/tex2img.php?eq=%20v_%7Bf%7D%20%20%3D%20%20v_%7Bi%7D%20%20%2B%20at&bc=White&fc=Black&im=jpg&fs=18&ff=arev&edit=0)

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

![equation2_image](http://www.sciweavers.org/tex2img.php?eq=d%20%3D%20%20%5Cfrac%7B%28v_%7Bf%7D%2B%20v_%7Bi%7D%29%7D%7B2%7Dt&bc=White&fc=Black&im=jpg&fs=18&ff=arev&edit=0)

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

![equation3_image](http://www.sciweavers.org/tex2img.php?eq=d%20%3D%20%20v_%7Bi%7Dt%20%2B%20%20%5Cfrac%7B1%7D%7B2%7Da%20t%5E%7B2%7D%20%20&bc=White&fc=Black&im=jpg&fs=18&ff=arev&edit=0)

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

![equation4_image](http://www.sciweavers.org/tex2img.php?eq=%20%20v_%7Bf%7D%20%5E%7B2%7D%20%3D%20%20v_%7Bi%7D%20%5E%7B2%7D%20%2B%202ad&bc=White&fc=Black&im=jpg&fs=18&ff=arev&edit=0)

*Overview:*
The function needs at least 3 arguments but can take 4. If less than 3 arguments are given, an error will be raised. If 3 arguments are given, the function will return a tuple of all 4 arguments (the arg. that wasn't given is computed and returned in the tuple). If 'vi' or 'vf' was the missing variable, they will be returned as a list with 2 elements. If 4 arguments are given the function will return a bool letting the caller know if the 4 values they entered satisfy the equation (1% error tolerance).


## PyPI Link

This is the link to the package [PyPI - kinematics5](https://pypi.org/project/kinematics5/).

## Lastest Version

0.0.3

## License

Distributed under the terms of the MIT license, ```kinematics5``` is free and open source software.