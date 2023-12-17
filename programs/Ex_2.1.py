#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Задача о выборе заявок
# Наивный алгоритм


def ActSel(S):
    result = []
    while len(S) != 0:
        min_right_end = min(S, key=lambda x: x[1])
        result.append(min_right_end)
        S = [segment for segment in S if segment[0] > min_right_end[1]]

    return result


if __name__ == '__main__':
    S = [(2, 3), (2, 4), (3, 5), (4, 6), (1, 2)]
    print(ActSel(S))
