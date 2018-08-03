def main():
    n = int(input())
    for i in range(n):
        string_in = str(input())
        validate_email(string_in)


def validate_email(string_in):
    min_len = 4
    str_len = len(string_in)
    if str_len <= min_len:
        print('Nie')
    elif (find_last_dot(string_in) - first_word_size(string_in)) > 21:
        print('Nie')
    elif (
            first_word_size(string_in) <= 20) & \
            check_dot_and_at(string_in) & \
            is_top_level_domain_name_valid(string_in) & \
            check_spelling(string_in) & \
            (at_counter(string_in) == 1) & \
            check_spelling_of_last_three_char(string_in
                                              ):
        print('Tak')
        # show_result(string_in)
    else:
        print('Nie')
        # show_result(string_in)


def check_dot_and_at(string_in):
    length = len(string_in)
    for i in range(length):
        if (i > 0) & (i + 1 < length):
            if (
                    (string_in[i] == '@') |
                    (string_in[i] == '.')
            ) & (
                    (string_in[i + 1] == '@') |
                    (string_in[i - 1] == '@') |
                    (string_in[i + 1] == '.') |
                    (string_in[i - 1] == '.')
            ):
                return False
        elif (string_in[i] == '@') | (string_in[i] == '.'):
            return False
    return True


def check_spelling(string_in):
    for i in range(len(string_in)):
        value = ord(string_in[i])
        if not (
                (ord('a') <= value <= ord('z')) |
                (ord('A') <= value <= ord('Z')) |
                (ord('0') <= value <= ord('9')) |
                (value == ord('@')) |
                (value == ord('_')) |
                (value == ord('.'))
        ):
            return False
    return True


def is_top_level_domain_name_valid(string_in):
    max = len(string_in)
    start = max - 4
    count = 0
    dot_found = False
    for i in range(start, max):
        if dot_found:
            if string_in[i] == '.':
                return False
        elif string_in[i] == '.':
            dot_found = True
    if dot_found:
        return True
    return False


def check_spelling_of_last_three_char(string_in):
    max = len(string_in)
    start = max - 3
    for i in range(start, max):
        value = ord(string_in[i])
        if not (
                (ord('a') <= value <= ord('z')) |
                (ord('A') <= value <= ord('Z')) |
                (value == ord('.'))
        ):
            return False
    return True


def at_counter(string_in):
    count = 0
    for char in string_in:
        if char == '@':
            count += 1
    return count


def first_word_size(string_in):
    count = 0
    for char in string_in:
        if char == '@':
            return count
        count += 1
    return count


def find_last_dot(string_in):
    index = 0
    for i in range(len(string_in)):
        if string_in[i] == '.':
            index = i
    return index


def show_result(string_in):
    print('FWS {0} CDAT {1} CLTC {2} CS {3} MK {4} CSOLTC {5} FWS {6}'
          .format(first_word_size(string_in),
                  check_dot_and_at(string_in),
                  is_top_level_domain_name_valid(string_in),
                  check_spelling(string_in),
                  at_counter(string_in),
                  check_spelling_of_last_three_char(string_in),
                  first_word_size(string_in)
                  )
          )


if __name__ == '__main__':
    main()
