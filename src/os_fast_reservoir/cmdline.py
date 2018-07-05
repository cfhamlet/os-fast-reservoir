#!/usr/bin/env python

import argparse
import sys

from . import __version__
from .reservoir import ReservoirSampling

_PY3 = sys.version_info[0] == 3
if _PY3:
    binary_stdin = sys.stdin.buffer
    binary_stdout = sys.stdout.buffer
else:
    binary_stdin = sys.stdin
    binary_stdout = sys.stdout


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


def execute(argv=None):
    argv = argv or sys.argv
    parser = argparse.ArgumentParser(description='Reservoir sample tool.')
    parser.add_argument('-v', '--version',
                        action='version',
                        version='%(prog)s {version}'.format(version=__version__))
    parser.add_argument('-f', '--file',
                        help='file to be sampled (default: stdin)',
                        nargs='+',
                        type=argparse.FileType('rb'),
                        default=[binary_stdin],
                        dest='input')
    parser.add_argument('-n', '--num',
                        help='sample number',
                        type=check_positive,
                        action='store',
                        dest='num',
                        required=True)

    args = parser.parse_args(argv[1:])
    sample = ReservoirSampling(args.num)
    for line in args.input[0]:
        sample.sample(line)
    for line in sample:
        binary_stdout.write(line)
