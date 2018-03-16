#!/usr/bin/env python
from __future__ import print_function

import argparse
import os
import sys

from .reservoir import ReservoirSampling

PY3 = sys.version_info[0] == 3


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


def _get_input(args):
    io_input = sys.stdin
    if PY3:
        io_input = sys.stdin.buffer

    if args.input_file:
        io_input = open(args.input_file, 'rb')

    return io_input


def _get_output(args):
    io_output = sys.stdout
    if PY3:
        io_output = sys.stdout.buffer
    return io_output


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
    io_input = _get_input(args)
    for line in io_input:
        sample.sample(line)
    io_output = _get_output(args)
    for line in sample:
        io_output.write(line)
