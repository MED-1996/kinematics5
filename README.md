# Project Description

**A python package for solving 1D kinematics problems.**

## Installation

```
pip install kinematics5
```

## Inspiration

As a high school AP physics tutor, I wanted to make a python package for solving kinematics problems.

## Examples

*Below are function definitions from the ```OneD``` module. The ```OneD``` module contains 4 functions. They represent the 4 kinematic equations.*

# eq1(vi, vf, a, t)

The first kinematic equation. Below is the equation:

vf = vi + at

The function accepts integers or floats.

The function needs at least 3 arguments but can take 4. If less than 3 arguments are given, the function will raise an error. If 3 arguments are given, the function will return a tuple of all 4 arguments (the arg. that wasn't given is computed and returned in the tuple). If 4 arguments are given the function will return a bool ```True/False``` letting the caller know if the 4 values they entered satisfy the equation (1% error).

# eq2

The second kinematic equation. Below is the equation:

d = (vf + vi) * t/2

The function accepts integers or floats.

The function needs at least 3 arguments but can take 4. If less than 3 arguments are given, the function will raise an error. If 3 arguments are given, the function will return a tuple of all 4 arguments (the arg. that wasn't given is computed and returned in the tuple). If 4 arguments are given the function will return a bool ```True/False``` letting the caller know if the 4 values they entered satisfy the equation (1% error).

# eq3

# eq4

## PyPI Link

This is the link to the package on PyPI [PyPI - kinematics5](https://pypi.org/project/kinematics5/).

## Lastest Version

0.0.3

## License

Distributed under the terms of the MIT license, ```kinematics5``` is free and open source software.