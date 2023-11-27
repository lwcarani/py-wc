import unittest
from unittest import TestCase
from parameterized.parameterized import parameterized
import argparse
from typing import (
    Tuple,
    List,
)

from main import (
    is_ignored,
    count_data,
)

# initialize data for unittesting
with open('test.txt', 'r', encoding='utf-8') as f:
    TEST_TEXT = f.read()


class TestPyHead(TestCase):
    """Test py-head functionality."""

    @parameterized.expand(
        [
            ['test.txt', ['.csv'], False],
            ['test.txt', ['.csv', '.xlsx', '.git', '.pdf'], False],
            ['test.txt', ['.png'], False],
            ['test.txt', ['.pdf'], False],
            ['test.txt', ['.xlsx'], False],
            ['test.txt', ['.git'], False],
            ['test.txt', ['.txt'], True],
            ['test.csv', ['.csv'], True],
            ['test.jpeg', ['.csv', '.xlsx', '.git', '.pdf'], False],
            ['test.xlsm', ['.csv', '.xlsx', '.git', '.pdf', '.xlsm'], True],
            ['test.jpeg', ['.csv', '.xlsx', '.git', '.pdf', 'jpeg'], True],
        ]
    )
    def test_is_ignored(
        self,
        file_path: str,
        ext_or_dir_to_ignore: List[str],
        expected_output: bool
    ) -> None:
        res = is_ignored(file_path=file_path, ext_or_dir_to_ignore=ext_or_dir_to_ignore)
        self.assertEqual(res, expected_output)

    @parameterized.expand(
        [
            [
                'test.txt',
                argparse.Namespace(
                    input_files_or_dirs=['test.txt'],
                    bytes=False,
                    lines=False,
                    words=False,
                    characters=False, 
                    ignore_extensions=[]
                ),
                0,
                (7145, 58164, 342185)
            ],
            [
                'test.txt',
                argparse.Namespace(
                    input_files_or_dirs=['test.txt'],
                    bytes=False,
                    lines=True,
                    words=False,
                    characters=False, 
                    ignore_extensions=[]
                ),
                1,
                (7145, )
            ],
            [
                'test.txt',
                argparse.Namespace(
                    input_files_or_dirs=['test.txt'],
                    bytes=False,
                    lines=False,
                    words=True,
                    characters=False, 
                    ignore_extensions=[]
                ),
                1,
                (58164, )
            ],
            [
                'test.txt',
                argparse.Namespace(
                    input_files_or_dirs=['test.txt'],
                    bytes=True,
                    lines=False,
                    words=False,
                    characters=False, 
                    ignore_extensions=[]
                ),
                1,
                (342185, )
            ],
            [
                'test.txt',
                argparse.Namespace(
                    input_files_or_dirs=['test.txt'],
                    bytes=False,
                    lines=False,
                    words=False,
                    characters=True, 
                    ignore_extensions=[]
                ),
                1,
                (339289, )
            ],
            [
                'test.txt',
                argparse.Namespace(
                    input_files_or_dirs=['test.txt'],
                    bytes=True,
                    lines=True,
                    words=True,
                    characters=True, 
                    ignore_extensions=[]
                ),
                4,
                (7145, 58164, 339289, 342185)
            ],
            [
                'test.txt',
                argparse.Namespace(
                    input_files_or_dirs=['test.txt'],
                    bytes=True,
                    lines=True,
                    words=False,
                    characters=False, 
                    ignore_extensions=[]
                ),
                2,
                (7145, 342185)
            ],
            [
                'test.txt',
                argparse.Namespace(
                    input_files_or_dirs=['test.txt'],
                    bytes=False,
                    lines=False,
                    words=True,
                    characters=True, 
                    ignore_extensions=[]
                ),
                2,
                (58164, 339289)
            ],
        ]
    )
    def test_count_data(
        self,
        file_name: str, 
        args: argparse.Namespace,
        optional_flags: int,
        expected_output: str
    ) -> None:
        with open(file_name, 'rb') as file:
            res: Tuple[int] = count_data(
                file=file, 
                file_name=file_name, 
                args=args, 
                optional_flags=optional_flags
            )
            self.assertEqual(res, expected_output)


if __name__ == '__main__':
    unittest.main()
