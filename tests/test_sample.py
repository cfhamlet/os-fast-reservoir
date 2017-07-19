import pytest
from os_fast_reservoir import ReservoirSampling


def test_gap_sample():
    limit = 10
    rs = ReservoirSampling(limit)
    num = 41
    for i in range(0, num):
        rs.sample(i)
    count = 0
    for i in rs:
        count += 1
    assert count == limit
    assert rs._sample == rs._gap_sample


def test_navie_sample():
    limit = 10
    rs = ReservoirSampling(limit)
    num = 20
    for i in range(0, num):
        rs.sample(i)
    count = 0
    for i in rs:
        count += 1
    assert count == limit


def test_no_sample():

    rs = ReservoirSampling(10)
    num = 5
    for i in range(0, num):
        rs.sample(i)
    count = 0
    for i in rs:
        count += 1
    assert count == num
