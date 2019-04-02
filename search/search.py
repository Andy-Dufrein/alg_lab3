#!/usr/bin/env python
# -*- coding: utf-8 -*-


def linear_search(data, value):
    for i, v in enumerate(data):
        if v > value:
            return None
        if v == value:
            return i
    return None


def binary_search(data, value):
    l=0
    h=len(data)-1
    while l<=h:
        m=(h+l)//2
        v=data[m]
        if v==value:
            return m
        elif v<value:
            l=m+1
        else:
            h=m-1
    return None

