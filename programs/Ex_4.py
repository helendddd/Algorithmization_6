#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Непрерывный рюкзак


def Knapsack(P, w):
    result = []
    P.sort(key=lambda x: (x[1]/x[0]), reverse=True)
    bagw = 0
    cost = 0

    for item in P:
        if bagw < w:
            result.append(item)
            bagw += item[0]
            cost += item[1]

    if bagw > w:
        cost -= result[-1][1]
        result[-1][1] -= (result[-1][1] / result[-1][0] * (bagw-w))
        result[-1][0] -= (bagw - w)
        cost += result[-1][1]

    print(f"Итоговая стоимость: {cost}")

    return result


if __name__ == '__main__':
    P = [[1, 3], [1, 4], [2, 5], [3, 6], [4, 7], [10, 9], [7, 10], [5, 11]]
    W = 10

    print(Knapsack(P, W))
