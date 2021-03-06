def get_longest_consecutive_repeat_s_(seq):                         # getting a DNA/RNA strand
    start = 0                                                       # setting the loop starter to zero
    repeats = []                                                    # an empty list to store the max-length repetitive segments
    max_ = 0                                                        # the max length
    while start < len(seq):
        segment = ''                                                # an empty string to store a repetitive segment at a time
        for i in range(start, len(seq)):                            # looping the strand and recording all repetitive segments
            for j in range(start + 1, len(seq) + 1):
                if j != len(seq) and seq[j] == seq[i]:
                    segment += seq[j]
                else:
                    start = j
                    if len(segment) > 0 and len(segment) > max_:    # if-elif statement to assure that only max-length repeats are stored
                        max_ = len(segment)
                        repeats = [[segment[0], i + 1]]
                    elif len(segment) > 0 and len(segment) == max_:
                        repeats.append([segment[0], i + 1])
                    break                                           # breaks once a repetitive segment ends
            break                                                   # breaks and start searching again from where it stopped till it reaches the end of the strand
    if not repeats:
        return False                                                # returns False for an empty input or for one that doesn't have any repeats at all
    return repeats, len(repeats), max_ + 1                          # returns the repeated letters and the number of occurrence and the max length
