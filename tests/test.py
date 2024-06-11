import pytest
from unittest.mock import patch
from io import StringIO

def print_hello_world_multiple_times():
    num = int(input("Введите число: "))
    for _ in range(num):
        print("Hello, world")

def test_print_hello_world_multiple_times_0(capsys):
    with patch('builtins.input', side_effect=['0']):
        print_hello_world_multiple_times()
        captured = capsys.readouterr()
        assert captured.out == ""

def test_print_hello_world_multiple_times_3(capsys):
    with patch('builtins.input', side_effect=['3']):
        print_hello_world_multiple_times()
        captured = capsys.readouterr()
        assert captured.out == "Hello, world\nHello, world\nHello, world\n"

def test_print_hello_world_multiple_times_5(capsys):
    with patch('builtins.input', side_effect=['5']):
        print_hello_world_multiple_times()
        captured = capsys.readouterr()
        assert captured.out == "Hello, world\nHello, world\nHello, world\nHello, world\nHello, world\n"