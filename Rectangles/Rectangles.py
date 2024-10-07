import re


def rectangles(strings):
    rec_counter = 0
    for i, line in enumerate(strings):
        while re.search(r"(\+-*\+)", line) != None:
            top_side = re.search(r"(\+-*\+)", line)  # Find patten '+-*-+'
            while top_side != None:  # Loop through all top sides in the 'line'
                s = top_side.start()
                e = top_side.end() - 1
                next_line_index = i + 1
                ndashes = e - s - 1
                while next_line_index < len(
                        strings):  # loop through the verticle pattens
                    next_line = strings[next_line_index]
                    if (next_line[s] in "|+"
                            and next_line[e] in "|"):  # regular sidelines
                        next_line_index += 1
                    elif next_line[s] in "|" and next_line[e] in "|+":
                        next_line_index += 1
                    elif (re.match(rf"\+[-\+]{{{ndashes}}}\+",
                                   next_line[s:e + 1]) != None):
                        # the lower side must be in the pattern of +-..--+
                        rec_counter += 1
                        next_line_index += 1
                    else:  # no box found
                        next_line_index = len(strings) + 1  # break the loop
                current_match_re = re.sub("\\+", "\+", top_side.group(0))
                next_match = f"{current_match_re}-*\\+"
                top_side = re.search(next_match, line)
            line = line[:s] + "-" + line[
                s + 1:]  # Replace the start of topside as '-'
    return rec_counter


test_string = [
    "+-+ +-+",
    "| | | |",
    "+-+-+-+",
    "  | | |",
    "+-+-+-+",
    "| | | |",
    "+-+ +-+",
]

print(rectangles(test_string))
