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
    + [binchecker(n)](#bincheckern)
    + [decchecker(n)](#deccheckern)
    + [octchecker(n)](#octcheckern)
    + [hexchecker(n)](#hexcheckern)
    + [dectobin(x)](#dectobinx)
    + [bintodec(x)](#bintodecx)
    + [dectooct(x)](#dectooctx)
    + [octtobin(x)](#octtobinx)
    + [octtodec(x)](#octtodecx)
    + [bintooct(x)](#bintooctx)
    + [hextobin(x)](#hextobinx)
    + [hextodec(x)](#hextodecx)
    + [hextooct(x)](#hextooctx)
    + [dectohex(x)](#dectohexx)
    + [bintohex(x)](#bintohexx)
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

> :info: Try entering arguments as *String* only<br>

> ℹ Conversion functions automatically check input arguments, you don't need to check them manually

### binchecker(n)
Checks if passed argument is suitable for Binary System or not
 ```python
 >>> binchecker('11011')
True
>>> binchecker('213')
InvalidInputError: invalid Binary Number
>>>
 ```

### decchecker(n)
Checks if passed argument is suitable for Decimal System or not
 ```python
 >>> decchecker('75412')
True
>>> decchecker('a34b')
InvalidInputError: invalid Decimal Number
>>>
 ```

### octchecker(n)
Checks if passed argument is suitable for Octal System or not
 ```python
 >>> octchecker('752')
True
>>> octhecker('8249')
InvalidInputError: invalid Octal Number
>>>
 ```
### hexchecker(n)
Checks if passed argument is suitable for Hexadecimal System or not
 ```python
 >>> hexchecker('7ac2')
True
>>> hexchecker('a34jrt')
InvalidInputError: invalid Hexadecimal Number
>>>
 ```

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