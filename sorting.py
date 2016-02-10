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
