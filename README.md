# os-fast-reservoir
[![Build Status](https://www.travis-ci.org/cfhamlet/os-fast-reservoir.svg?branch=master)](https://www.travis-ci.org/cfhamlet/os-fast-reservoir)
[![codecov](https://codecov.io/gh/cfhamlet/os-fast-reservoir/branch/master/graph/badge.svg)](https://codecov.io/gh/cfhamlet/os-fast-reservoir)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/os-fast-reservoir.svg)](https://pypi.python.org/pypi/os-fast-reservoir)
[![PyPI](https://img.shields.io/pypi/v/os-fast-reservoir.svg)](https://pypi.python.org/pypi/os-fast-reservoir)

Python implementation of fast approximation reservioir sampling.

# Install
  `$ pip install os-fast-reservoir`

# Usage
  * API
  ```
    from os_fast_reservoir import ReservoirSampling

    rs = ReservoirSampling(100)

    for i in range(1000):
        rs.sample(i)

    for i in rs:
        print i
  ```
  * Command line
  ```
    $ os-fast-reservoir -h
    usage: os-fast-reservoir [-h] [-f INPUT_FILE] -n NUM

    Reservoir sample tool.

    optional arguments:
      -h, --help            show this help message and exit
      -f INPUT_FILE, --file INPUT_FILE
                            file to be sampled (default: stdin)
      -n NUM, --num NUM     sample number
  ```

# Algorithm
  * [Reservoir sampling](https://en.wikipedia.org/wiki/Reservoir_sampling)
  * [Faster Random Samples With Gap Sampling](http://erikerlandson.github.io/blog/2014/09/11/faster-random-samples-with-gap-sampling/)
  * [Very Fast Reservoir Sampling](http://erikerlandson.github.io/blog/2015/11/20/very-fast-reservoir-sampling/)
  * Another implementation: [alexprengere/reservoir](https://github.com/alexprengere/reservoir)

# Unit Tests
  `$ tox`

# License
  MIT licensed.
