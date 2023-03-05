def longest_stretch(numbers):
    if not numbers:
        return 0

    current_num = numbers[0]
    current_stretch = 1
    longest_stretch = 1

    for num in numbers[1:]:
        if num == current_num:
            current_stretch += 1
        else:
            current_num = num
            current_stretch = 1
        longest_stretch = max(longest_stretch, current_stretch)

    return longest_stretch