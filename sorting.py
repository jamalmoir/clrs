class Sort:

    def insertion_sort(self, array, order):
        if order > 0:
            for j in range(1, len(array)):
                key = array[j]
                i = j - 1
                while i >= 0 and array[i] > key:
                    array[i + 1] = array[i]
                    i = i - 1
                array[i + 1] = key
        elif order < 0:
            for j in range(len(array) - 1, -1, -1):
                key = array[j]
                i = j + 1
                while i < len(array) and array[i] > key:
                    array[i - 1] = array[i]
                    i = i + 1
                array[i - 1] = key
        return array

    def selection_sort(self, array):
        for i in range(0, len(array)):
            lowest = (array[i], i)
            for j in range (i, len(array)):
                if array[j] < lowest[0]:
                    lowest = (array[j], j)
            array[lowest[1]] = array[i]
            array[i] = lowest[0]
        return array
