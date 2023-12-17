#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Планирование вечеринки в компании


def delete(T, leave, parents):
    result = []
    fordelete = leave | parents

    for segment in T:
        if segment[1] not in fordelete:
            result.append(segment)

    return result


def maxIndependentSet(T):
    result = set()
    vertices = set(range(1, len(T)+1))

    while len(T) != 0:
        # Определила 2 множества с родителями и детьми
        par = [segment[0] for segment in T]
        child = [segment[1] for segment in T]

        # Множество листьев
        leave = set(child).difference(set(par))
        result = result | leave

        # Определила родителей для листьев
        leave_parents = set()
        for segment in T:
            if segment[1] in leave:
                leave_parents.add(segment[0])

        # Из множества вершин удалила листья и их родителей
        vertices -= (leave | leave_parents)
        T = delete(T, leave, leave_parents)

        if len(vertices) == 1 and len(T) == 0:
            result |= vertices

    return result


if __name__ == '__main__':
    graf = ([1, 2], [1, 3], [1, 4], [2, 5], [3, 6],
            [4, 7], [4, 8], [7, 9], [7, 10], [7, 11])

    print("Ответ: ", maxIndependentSet(graf))
