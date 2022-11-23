#!/usr/bin/python
# -*- coding: utf-8 -*-
weird_a = 127462
zero_width_space = "​"
out = zero_width_space.join(chr(weird_a + ord(c)) for c in input())
print(out)
