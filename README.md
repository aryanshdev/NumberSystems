# Number Systems
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://instagram.com/_aryansh.gupta_)

**Python Module To Quickly Convert One Number System to Another.**


- [Number Systems](#number-systems)
  * [Installations](#installations)
  * [Usage](#usage)
  * [Functions](#functions)
    + [Functions To Check Input :](#functions-to-check-input--)
    + [Conversion Functions :](#conversion-functions--)
  * [Using Functions](#using-functions)
    + [binchecker(n)](#binchecker)
    + [decchecker(n)](#decchecker)
    + [octchecker(n)](#octchecker)
    + [hexchecker(n)](#hexchecker)
    + [dectobin(x)](#dectobin)
    + [bintodec(x)](#bintodec)
    + [dectooct(x)](#dectooct)
    + [octtobin(x)](#octtobin)
    + [octtodec(x)](#octtodec)
    + [bintooct(x)](#bintooct)
    + [hextobin(x)](#hextobin)
    + [hextodec(x)](#hextodec)
    + [hextooct(x)](#hextooct)
    + [dectohex(x)](#dectohex)
    + [bintohex(x)](#bintohex)
  * [Errors](#errors)


## Installations
Install using ```pip```

```shell
pip install numbersystems
```

## Usage


> :warning: Use ```converter```  while importing the module, not ```numbersystems```


To start using this Module, import it 

```shell
import converter
```

or Wildcard import 

```shell
from converter import *
```
## Functions

### Functions To Check Input :

- ```binchecker():```
- ```octchecker()```
- ```decchecker()```
- ```hexchecker()```

### Conversion Functions :

- ```dectobin()```
- ```bintodec()```
- ```dectooct()```
- ```octtobin()```
- ```octtodec()```
- ```bintooct()```
- ```hextobin()```
- ```hextodec()```
- ```hextooct()```
- ```dectohex()```
- ```bintohex()```

## Using Functions


### binchecker(n)
Checks if passed argument is sutiable for Binary System or not

### decchecker(n)
Checks if passed argument is sutiable for Decimal System or not

### octchecker(n)
Checks if passed argument is sutiable for Octal System or not

### hexchecker(n)
Checks if passed argument is sutiable for Hexadecimal System or not


### dectobin(x)
 It Converts Decimal to Binary, takes Decimal value as Parameter, returns Binary equivalent

 ```python
 >>> dectobin(2)
10
>>>
 ```
 
### bintodec(x)
 It Converts Binary to Decimal, takes Binary value as Parameter, returns Decimal equivalent

 ```python
 >>> dectobin(101)
5
>>>
 ```
 
### dectooct(x)
 It Converts Decimal to Octal, takes Decimal value as Parameter, returns Octal equivalent

 ```python
 >>> dectooct(12)
14
>>>
 ```

 ### octtobin(x)
 It Converts Octal to Binary, takes Octal value as Parameter, returns Binary equivalent

 ```python
 >>> octtobin(12)
1010
>>>
 ```

 ### octtodec(x)
 It Converts Octal to Decimal, takes Octal value as Parameter, returns Decimal equivalent

 ```python
 >>> dectooct(12)
10
>>>
 ```

 ### bintooct(x)
 It Converts Binary to Octal, takes Binary value as Parameter, returns Octal equivalent

 ```python
 >>> bintooct(10101)
25
>>>
 ```
 
 ### hextobin(x)
 It Converts Hexadecimal to Binary, takes Hexadecimal value as Parameter, returns Binary equivalent

 ```python
 >>> hextobin(15)
10101
>>>
 ```
  
 ### hextodec(x)
 It Converts Hexadecimal to Decimal, takes Hexadecimal value as Parameter, returns Decimal equivalent

 ```python
 >>> hextodec(15)
21
>>>
```
 
 ### hextooct(x)
 It Converts Hexadecimal to Octal, takes Hexadecimal value as Parameter, returns Octal equivalent

 ```python
 >>> hextooct(15)
25
>>>
```
 
 ### dectohex(x)
 It Converts Decimal to Hexadecimal, takes Decimal value as Parameter, returns Hexadecimal equivalent

 ```python
 >>> hextobin(15)
10101
>>>
```
 
 ### bintohex(x)
 It Converts Binary to Hexadecimal, takes Binary value as Parameter, returns Hexadecimal equivalent

 ```python
 >>> bintohex(10101)
15
>>>
```
## Errors

In case of the Wrong Type of Data given as an input to the Function, **InvalidInputError** is raised.

It is suggested to check the input value again if the Error is raised.

**If the input value to the function is fine, still Error rises, please open a new *Issue* on Github**.