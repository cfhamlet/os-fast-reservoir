# os-fast-reservoir
[![Build Status](https://www.travis-ci.org/cfhamlet/os-fast-reservoir.svg?branch=master)](https://www.travis-ci.org/cfhamlet/os-fast-reservoir)
[![codecov](https://codecov.io/gh/cfhamlet/os-fast-reservoir/branch/master/graph/badge.svg)](https://codecov.io/gh/cfhamlet/os-fast-reservoir)

Python implementation of fast approximation reservioir sampling.

# Install
  `$ pip install os-fast-reservoir`

# Usage
  ```
    from os_fast_reservoir import ReservoirSampling

    rs = ReservoirSampling(100)

    for i in range(1000):
        rs.sample(i)

    for i in rs:
        print i
  ```

# Algorithm
  * [Reservoir sampling](https://en.wikipedia.org/wiki/Reservoir_sampling)
  * [Faster Random Samples With Gap Sampling](http://erikerlandson.github.io/blog/2014/09/11/faster-random-samples-with-gap-sampling/)
  * [Very Fast Reservoir Sampling](http://erikerlandson.github.io/blog/2015/11/20/very-fast-reservoir-sampling/)
  * Implementation: [alexprengere/reservoir](https://github.com/alexprengere/reservoir)

# Unit Tests
  `$ tox`

# License
  MIT licensed.
