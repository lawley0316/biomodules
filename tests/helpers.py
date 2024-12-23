# -*- coding: utf-8 -*-
from pathlib import Path


def data(name):
    return Path(__file__).parent / 'data' / name
