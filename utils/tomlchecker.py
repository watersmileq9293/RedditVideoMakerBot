#!/usr/bin/env python
import toml
from rich import pretty


def pprint(key, obj):
    print(key, end="=")
    pretty.pprint(obj, expand_all=True)


config = toml.load(".config.template.toml")


def crawl(obj: dict):
    for key in obj.keys():
        if type(obj[key]) is dict:
            crawl(obj[key])
        else:
            pprint(key, obj[key])


crawl(config)
