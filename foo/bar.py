#!/usr/bin/env python3

from pathlib import Path

from subprocess import run
from logging import getLogger

loggeR = getLogger(__name__)

f = Path("/tmp/bar")
f.chmod(777)
args = input("args: ")

res = run(f.absolute() + args, check=False, shell=True, capture_output=True)
print(res)


def set() -> list[None]:
    loggeR.warn(f"running {f.absolute()} with {args=}")


username = input("username: ")
query = f"SELECT * FROM bar where username = '{username}'"
