#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Задача о выборе заявок
# Улучшенный алгоритм


def ActSel(S):
    S.sort(key=lambda x: x[1])
    result = []
    last_end = float('-inf')
    for segment in S:
        if segment[0] > last_end:
            result.append(segment)
            last_end = segment[1]
    return result


if __name__ == '__main__':
    S = [(2, 3), (2, 4), (3, 5), (4, 6), (1, 2)]
    print(ActSel(S))
