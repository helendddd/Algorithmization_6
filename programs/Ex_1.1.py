#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Покрытие точек отрезками
# Наивный алгоритм

def PointsCover(S):
    result = []
    while len(S) > 0:
        Xm = min(S)
        result.append([Xm, Xm + 1])
        while Xm in S:
            S.remove(Xm)
        while Xm+1 in S:
            S.remove(Xm+1)
    return result


if __name__ == '__main__':
    S = [3, 8, 2, 9, 1, 2, 5, 5, 6]
    print(PointsCover(S))
