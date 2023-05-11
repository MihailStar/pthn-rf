# Задача A

import functools
import os
import typing


def project_stats(path: str, extensions: typing.Set[str]) -> int:
    number_of_lines = total_number_of_lines(
        with_extensions(extensions, iter_filenames(path))
    )

    return number_of_lines


def total_number_of_lines(filenames: typing.Iterable[str]) -> int:
    number_of = functools.reduce(
        lambda acc, filename: acc + number_of_lines(filename), filenames, 0
    )

    return number_of


def number_of_lines(filename: str) -> int:
    # @tutorial https://ru.stackoverflow.com/a/641692
    number_of = sum(1 for _line in open(filename, "r"))

    return number_of


def iter_filenames(path: str) -> typing.Iterable[str]:
    filenames = (
        os.path.join(dirpath, filename)
        for dirpath, _dirnames, filenames in os.walk(path)
        for filename in filenames
    )

    return filenames


def with_extensions(
    extensions: typing.Set[str], filenames: typing.Iterable[str]
) -> typing.Iterable[str]:
    filtered_filenames = filter(
        lambda filename: get_extension(filename) in extensions, filenames
    )

    return filtered_filenames


def get_extension(filename: str) -> str:
    _root, extension = os.path.splitext(filename)

    return extension


def print_usage() -> None:
    print("Usage: python project_sourse_stats_3.py <project_path>")
