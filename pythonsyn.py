# Python3-by-practice
# A repo to learn Python programming
on: [push, pull_request]
name: Python Syntax
jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: cclauss/Find-Python-syntax-errors-action@master
