from typing import List


def longest_alternating_subseq(x: List[int]) -> int:
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


def problem2(wood):
    wood_count = {}
    for p in wood:
        if p not in wood_count:
            wood_count[p] = 0

        wood_count[p] += 1

    max_plank_len = max(wood_count.keys())
    max_planks = wood_count[max_plank_len]
    for length in range(1, max_plank_len):
        if length in wood_count:
            combined_len = max_plank_len - length
            if combined_len in wood_count:
                combination_count = min(wood_count[length], wood_count[combined_len])
                if length != combined_len:
                    max_planks += combination_count

                max_planks += combination_count

    return max_planks


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    print(longest_alternating_subseq([0, 1, 0, 1, 0]))
    print(problem2([22, 12, 13, 22, 22, 22, 14, 22, 17, 22]))
    print(problem2([8, 13, 7, 13, 5, 13, 4, 13, 6, 13]))

