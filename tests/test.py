from io import StringIO
from contextlib import redirect_stdout
import pytest

def print_hello_world(times):
    for _ in range(times):
        print("Hello, world")


def test_print_hello_world(capsys):
    times = 3
    expected_output = "Hello, world\n" * times
    print_hello_world(times)
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_print_hello_world_zero_times(capsys):
    times = 0
    expected_output = ""
    print_hello_world(times)
    captured = capsys.readouterr()
    assert captured.out == expected_output


def test_print_hello_world_one_time(capsys):
    times = 1
    expected_output = "Hello, world\n"
    print_hello_world(times)
    captured = capsys.readouterr()
    assert captured.out == expected_output