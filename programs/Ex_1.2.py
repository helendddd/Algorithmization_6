#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Покрытие точек отрезками
# Улучшенный алгоритм


def PointsCover(S):
    S.sort()
    result = []
    i = 0
    while i < len(S):
        Xm = S[i]
        result.append([S[i], S[i] + 1])
        i += 1
        while i < len(S) and S[i] <= Xm + 1:
            i += 1
    return result


if __name__ == '__main__':
    S = [3, 8, 2, 9, 1, 2, 5, 5, 6]
    print(PointsCover(S))
