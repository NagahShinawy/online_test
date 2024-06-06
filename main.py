# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def longest_alternating_subseq(x: list) -> int:

    """
    # problem #1
    compute the length of the longest subsequences within the array x that
    alternates between os and 1s.
    :param x: list of 0s and 1s.
    :return: int the len of the longest alternating subsequences
    examples:
        longest_alternating_subseq([0, 1, 0, 1, 0]) > 5
        longest_alternating_subseq([0]) > 1
    """
    max_len = 1
    current_len = 1
    for i in range(1, len(x)):
        if x[i] != x[i - 1]:
            current_len += 1
            max_len = max(max_len, current_len)

        else:
            current_len = 1

    return max_len


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    longest_alternating_subseq([0, 1, 0, 1, 0])
