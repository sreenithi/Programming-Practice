def binarySearch(arr, num):

    start = 0
    end = len(arr)-1
    found = False

    while start <= end:

        mid = (start + end)//2

        if arr[mid] == num:
            found = True
            break
        elif num < arr[mid]:
            end = mid-1
        else:
            start = mid+1

    return found


if __name__ == '__main__':

    numbers = [int(x) for x in input("Enter a list of numbers in ascending order:\n").split()]

    continueSearch = 'y'

    while continueSearch == 'y':
        numSearch = int(input("Enter a number to be searched: "))
        print("Searching..")
        found = binarySearch(numbers, numSearch)

        if found:
            print("Number found")
        else:
            print("Number not found")

        print()
        continueSearch = input("Search for a different number? (y/n): ")
