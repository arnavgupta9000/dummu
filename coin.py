def solve(arr, start):
    if start >= len(arr):
        return True
    if arr[start] == 0:
        return False

    for i in range(1, arr[start] + 1):
        if solve(arr, start + i):
            return True

    return False

def main():
    print(solve([2, 2, 3, 4, 2, 0, 0, 1], 0))  # should be True

main()
print("your way is weird")