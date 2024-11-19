nums = "one two three four five six seven eight nine".split()
sum_num = 0

with open("1.txt") as file:
    data = file.read()


def word_to_numeric(start):

    for j, num in enumerate(nums):
        try:
            if text[start : start + len(num)] == num:
                return j + 1
        except:
            pass

    return None


for text in data.strip().split():

    left = 0
    right = len(text) - 1

    left_num = None
    right_num = None

    while True:

        if left_num and right_num:
            break

        if not left_num:

            if text[left].isnumeric():
                left_num = int(text[left])
                continue

            left_num = word_to_numeric(left)

            left += 1

        if not right_num:

            if text[right].isnumeric():
                right_num = int(text[right])
                continue

            right_num = word_to_numeric(right)

            right -= 1

    sum_num += int(left_num * 10 + right_num)


print(sum_num)
