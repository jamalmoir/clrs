class Search(object):

    def linear_search(self, array, val):
        for i in range(0, len(array)):
            if array[i] == val:
                return i
        return None

    def binary_search(self, array, left, right, val):
        mid = int((left + right) / 2)

        if left <= right:
            if array[mid] == val:
                return mid
            elif array[mid] < val:
                return self.binary_search(array, mid + 1, right, val)
            else:
                return self.binary_search(array, left, mid - 1, val)
        else:
           return None
