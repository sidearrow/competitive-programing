#!/bin/bash

g++ \
  -std=gnu++17 \
  -Wall \
  -Wextra \
  -O2 \
  -o ./a.out \
  ${1}
