import math
import sys


def apply_rules(elementary_pyramid):
    rules = {"0000": "0000", "0001": "1000", "0010": "0001", "0011": "0010", "0100": "0000",
             "0101": "0010", "0110": "1011", "0111": "1011", "1000": "0100", "1001": "0101",
             "1010": "0111", "1011": "1111", "1100": "1101", "1101": "1110", "1110": "0111",
             "1111": "1111"}
    return rules[elementary_pyramid]


def reduce_pyramid(pyramid):
    reduced_pyramid = str()

    for elementary_pyramid in pyramid:
        reduced_pyramid += elementary_pyramid[0]

    return reduced_pyramid


def split_pyramid_on_stages(pyramid):
    """
The function takes a one-line view of the pyramid and returns a list, each element of which is a "stage" of the pyramid.
Stage - two real rows of the pyramid.
    """

    stages = []
    power_of_pyramid = math.log(len(pyramid), 4)
    amount_pyramids_in_base_stage = int(2**power_of_pyramid - 1)

    while len(pyramid) != 4:
        stages.append(pyramid[0:amount_pyramids_in_base_stage*4])
        pyramid = pyramid[amount_pyramids_in_base_stage*4:]
        amount_pyramids_in_base_stage -= 2

    stages.append(pyramid)
    return stages


def split_stage_on_elementary_pyramids(stage):
    """
The function takes a string containing one stage of the pyramid,
and returns a simple list of elementary pyramids entering this stage.
    """

    white_pyramids = []     # list of normal elementary pyramids
    black_pyramids = []     # list of upside-down elementary pyramids
    elementary_pyramids = []

    # calculate the number elementary pyramids in stage
    amount_of_white_pyramids = len(stage) // 8 + 1
    amount_of_black_pyramids = len(stage) // 8
    amount_of_base_elements = amount_of_white_pyramids*3 + amount_of_black_pyramids    # amount of elements in first row of stage

    for idx in range(0, amount_of_base_elements, 4):
        white_pyramids.append(stage[idx:idx+3]+stage[idx+amount_of_base_elements])

    for idx in range(0, amount_of_base_elements - 4, 4):
        black_pyramids.append(stage[idx+amount_of_base_elements+1:idx+amount_of_base_elements + 4] + stage[idx+3])

    for idx in range(amount_of_black_pyramids):
        elementary_pyramids.append(white_pyramids[idx])
        elementary_pyramids.append(black_pyramids[idx])

    elementary_pyramids.append(white_pyramids[-1])
    return elementary_pyramids


def assemble_pyramid_from_separated_elementary_pyramids(elementary_pyramids_separated):
    fake_stages = []    # list of lists containing joined elementary pyramids. Will be regrouped into true_stage

    for elementary_pyramids in elementary_pyramids_separated:
        fake_stages.append("".join(elementary_pyramids))
    pyramid = str()

    for fake_stage in fake_stages:
        true_stage1 = fake_stage[0:3]    # string contained first row of real pyramid's stage fetched from fake_stage
        true_stage2 = str()
        for idx in range(7, len(fake_stage), 8):
            true_stage1 += fake_stage[idx:idx+4]
        for idx in range(3, len(fake_stage), 8):
            true_stage2 += fake_stage[idx:idx+4]
        pyramid += true_stage1 + true_stage2
    print(pyramid)
    return pyramid


def main():
    if len(sys.argv) != 2:
        print('Usage: {0} <bit string>'.format(sys.argv[0]))
        sys.exit()

    actual_pyramid = sys.argv[1]  # one-line view of the current pyramid

    if set(actual_pyramid) != set(('0', '1')) and set(actual_pyramid) != set('1') and set(actual_pyramid) != set('0'):    
        print('<bit string> must be only 1 and/or 0!')
        sys.exit()
    if int(math.log(len(actual_pyramid), 4)) != math.log(len(actual_pyramid), 4):
        print('Length of the <bit string> must be power of four!')
        sys.exit()
    
    is_reducible_1 = set(['0000', '1111'])     # conditions under which one can reduce the pyramid
    is_reducible_2 = set(['1111'])
    is_reducible_3 = set(['0000'])

    print(actual_pyramid)

    while len(actual_pyramid) != 1:
        elementary_pyramids_separated = []
        stages = split_pyramid_on_stages(actual_pyramid)
        for stage in stages:
            elementary_pyramids_separated.append(list(map(apply_rules, split_stage_on_elementary_pyramids(stage))))

        elementary_pyramids = []    

        for idx in elementary_pyramids_separated:    # creation a simple list with elementary pyramids for more convenient comparation
            elementary_pyramids += idx

        pyramid_state = set(elementary_pyramids)    # conversion list of elementary pyramids to set to compare it with conditions is_reducible_1/2/3
        actual_pyramid = assemble_pyramid_from_separated_elementary_pyramids(elementary_pyramids_separated)

        if pyramid_state == is_reducible_1:
            actual_pyramid = reduce_pyramid(elementary_pyramids)
            print(actual_pyramid)
        elif (pyramid_state == is_reducible_2) or (pyramid_state == is_reducible_3):
            print(actual_pyramid[0])
            break


if __name__ == "__main__":
    main()
