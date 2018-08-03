cpdef main():
    cdef int n = int(input())
    cdef int i
    for i in range(n):
        string_in = str(input())
        validate_email(string_in)


cpdef validate_email(string_in):
    cdef int min_len = 4
    cdef int str_len = len(string_in)
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


cdef check_dot_and_at(string_in):
    cdef int length = len(string_in)
    cdef int i
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


cdef check_spelling(string_in):
    cdef str_len = len(string_in)
    cdef int i
    cdef int value
    for i in range(str_len):
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


cdef is_top_level_domain_name_valid(string_in):
    cdef int max = len(string_in)
    cdef int start = max - 4
    cdef int count = 0
    cdef bint dot_found = False
    cdef int i
    for i in range(start, max):
        if dot_found:
            if string_in[i] == '.':
                return False
        elif string_in[i] == '.':
            dot_found = True
    if dot_found:
        return True
    return False


cdef check_spelling_of_last_three_char(string_in):
    cdef int max = len(string_in)
    cdef int start = max - 3
    cdef int i
    for i in range(start, max):
        value = ord(string_in[i])
        if not (
                (ord('a') <= value <= ord('z')) |
                (ord('A') <= value <= ord('Z')) |
                (value == ord('.'))
        ):
            return False
    return True


cdef at_counter(string_in):
    cdef int count = 0
    cdef int i
    for i in range(len(string_in)):
        if string_in[i] == '@':
            count += 1
    return count


cdef first_word_size(string_in):
    cdef int count = 0
    cdef int i
    for i in range(len(string_in)):
        if string_in[i] == '@':
            return count
        count += 1
    return count


cdef find_last_dot(string_in):
    cdef int index = 0
    cdef int i
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
