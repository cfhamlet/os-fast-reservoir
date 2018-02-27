import os
import sys
import pytest
import shlex
import subprocess
from os_fast_reservoir.cmdline import execute


def call(cmdline, env=None, **kwargs):
    if env is None:
        env = os.environ.copy()
    if env.get('COVERAGE', None) is not None:
        env['COVERAGE_PROCESS_START'] = os.path.abspath('.coveragerc')

    cmd = 'python -u %s %s' % (os.path.abspath(__file__), cmdline)
    proc = subprocess.Popen(shlex.split(cmd),
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            cwd=os.getcwd(),
                            env=env,
                            **kwargs)
    stdout, stderr = proc.communicate()
    return stdout, stderr


def test_cmdline(tmpdir):
    f = tmpdir.join('testfile')
    f.write('\n'.join([str(i) for i in range(100)]))
    n = 10
    cmdline = '-n %d -f %s' % (n, f.strpath)
    stdout, stderr = call(cmdline)
    assert stdout.count(b'\n') == n


def test_invalid_cmdline():
    cmdline = '-n a'
    stdout, stderr = call(cmdline)
    assert b'must assign a positive int value' in stderr

    cmdline = '-f not_exist'
    stdout, stderr = call(cmdline)
    assert b'must an exist file' in stderr


if __name__ == "__main__":
    sys.path.insert(0, os.getcwd())
    if os.getenv('COVERAGE_PROCESS_START'):
        import coverage
        coverage.process_startup()
    execute()
