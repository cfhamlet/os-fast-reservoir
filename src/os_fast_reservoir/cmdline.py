#!/usr/bin/env python
from __future__ import print_function
import os
import sys
import argparse
from .reservoir import ReservoirSampling


def check_exist(value):
    if not value:
        return value
    if not os.path.isfile(value):
        raise argparse.ArgumentTypeError('must an exist file')
    return value


def check_positive(value):
    try:
        ivalue = int(value)
        assert ivalue > 0
    except:
        raise argparse.ArgumentTypeError(
            'must assign a positive int value.')
    return ivalue


def execute(argv=None):
    argv = argv or sys.argv
    parser = argparse.ArgumentParser(description='Reservoir sample tool.')
    parser.add_argument(
        '-f', '--file', help='file to be sampled (default: stdin)',
        type=check_exist, action='store', dest='input_file')
    parser.add_argument('-n', '--num', help='sample number',
                        type=check_positive, action='store', dest='num',
                        required=True)
    args = parser.parse_args(argv[1:])
    sample = ReservoirSampling(args.num)
    input_file = sys.stdin
    if args.input_file:
        input_file = open(args.input_file, 'r')
    for line in input_file:
        sample.sample(line)
    for line in sample:
        print(line, end='')
