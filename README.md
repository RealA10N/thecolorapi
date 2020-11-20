# The Color API - In Python!

Your python project involves some colors? We got you! Now, its easier then ever to manipulate colors, and even get color names, just with a couple commands.

## thecolorapi.com

This module is simply a python wrapper for the API provided by [thecolorapi.com](thecolorapi.com), and created by [Josh Beckman](https://www.joshbeckman.org/) - he did the hard work!

## A simple example

```python
>>> from thecolorapi import color

>>> dark_green = color(hex="#158f2b") 

>>> dark_green.hex
'#158F2B'
>>> dark_green.hex_clean
'158F2B'
>>> dark_green.rgb      
(21, 143, 43)
>>> dark_green.rgb_fraction
(0.08235294117647059, 0.5607843137254902, 0.16862745098039217)
>>> dark_green.hsl         
(131, 74, 32)
>>> dark_green.hsl_fraction
(0.36338797814207646, 0.7439024390243902, 0.3215686274509804)
>>> dark_green.hsv         
(131, 85, 56)
>>> dark_green.hsv_fraction
(0.36338797814207646, 0.8531468531468531, 0.5607843137254902)
>>> dark_green.cmyk        
(85, 0, 70, 44)
>>> dark_green.cmyk_fraction
(0.8531468531468531, 0, 0.6993006993006992, 0.4392156862745098)
>>> dark_green.contrast_hex 
'#000000'
>>> dark_green.name        
'Slimy Green'
```

## Installation

It can not get easier! Just run:
```
$ (sudo) pip install thecolorapi
```




