def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        if_swap = False
        for j in range(length - i - 1):
            yield {"type": "compare", "first": j, "second": j + 1}
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                if_swap = True
                yield {"type": "swap", "first": j, "second": j + 1}
        if not if_swap:
            yield {"type": "early_finished"}
            return
        else:
            yield {"type": "finished_cut", "index": i}
    yield {"type": "finished"}
    return

def output_algo():
    return bubble_sort
            