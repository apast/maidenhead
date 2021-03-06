[![DOI](https://zenodo.org/badge/132653071.svg)](https://zenodo.org/badge/latestdoi/132653071)

[![Actions Status](https://github.com/space-physics/maidenhead/workflows/ci/badge.svg)](https://github.com/space-physics/maidenhead/actions)


[![pypi versions](https://img.shields.io/pypi/pyversions/maidenhead.svg)](https://pypi.python.org/pypi/maidenhead)
[![PyPi Download stats](http://pepy.tech/badge/maidenhead)](http://pepy.tech/project/maidenhead)

# Maidenhead &lt;-&gt; Lat/Lon

`maidenhead` provides a simple, yet effective location hashing
algorithm. Maidenhead allows global location precision down to 750m

Maidenhead provides 4 levels of increasing accuracy

  Level |  Precision
--------|------------
  1     |  World
  2     |  Regional
  3     |  Metropolis
  4     |  City

We also have [Maidenhead conversion for Julia](https://github.com/scivision/maidenhead-julia).


Open Location Codes a.k.a Plus Codes are in
[Python code by Google](https://github.com/google/open-location-code/tree/master/python).

## Install
```sh
pip install maidenhead
```

## Examples
All examples assume first doing
```python
import maidenhead as mh
```

### lat lon to Maidenhead locator
```python
mh.toMaiden(lat, lon, level)
```
returns a char (len = lvl*2)

### Maidenhead locator to lat lon
```python
mh.toLoc('AB01cd')
```
take any string and returns topleft lat, lon of Maidenhead grid square.

## Command Line

Python:
```sh
python Maidenhead.py 65 -148
```
