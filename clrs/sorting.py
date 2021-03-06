import math


class Sort(object):

    def insertion_sort(self, array, order):
        if order > 0:
            for j, val in enumerate(array):
                key = array[j]
                i = j - 1

                while i >= 0 and array[i] > key:
                    array[i + 1] = array[i]
                    i = i - 1

                array[i + 1] = key

        elif order < 0:
            for j, val in reversed(list(enumerate(array))):
                key = array[j]
                i = j + 1

                while i < len(array) and array[i] > key:
                    array[i - 1] = array[i]
                    i = i + 1

                array[i - 1] = key

        else:
            print("Invalid order")

    def selection_sort(self, array):
        for i, val in enumerate(array):
            lowest = (i, val)

            for j, compare in enumerate(array[i:], i):
                if compare < lowest[1]:
                    lowest = (j, compare)

            array[lowest[0]] = val
            array[i] = lowest[1]

    def merge_sort(self, array, p, r):
        if p < r:
            q = int((p + r) / 2)

            self.merge_sort(array, p, q)
            self.merge_sort(array, q + 1, r)
            self.merge(array, p, q, r)

    def merge(self, array, p, q, r):
        n1 = q - p + 1
        n2 = r - q
        left = []
        right = []

        for i in range(0, n1):
            left.append(array[p + i])

        for j in range(0, n2):
            right.append(array[q + j + 1])

        left.append(math.inf)
        right.append(math.inf)
        i = 0
        j = 0

        for k in range(p, r + 1):
            if left[i] <= right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
