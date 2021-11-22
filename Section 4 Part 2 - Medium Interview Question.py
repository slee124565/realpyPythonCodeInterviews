def generate_key_to_letters():
    import string
    letters = string.ascii_lowercase
    digits = string.digits
    key_to_letters = {}
    start_letter_index = 0
    for key in digits:
        if key == '0':
            key_to_letters[key] = " "
        elif key == '1':
            key_to_letters[key] = ""
        else:
            if key in {'7', '9'}:
                letters_per_key = 4
            else:
                letters_per_key = 3
            key_to_letters[key] = (
                letters[start_letter_index:start_letter_index + letters_per_key]
            )
            start_letter_index += letters_per_key
    return key_to_letters


def keypad_string(keys):
    '''
    Given a string consisting of 0-9,
    find the string that is created using
    a standard phone keypad
    | 1        | 2 (abc) | 3 (def)  |
    | 4 (ghi)  | 5 (jkl) | 6 (mno)  |
    | 7 (pqrs) | 8 (tuv) | 9 (wxyz) |
    |     *    | 0 ( )   |     #    |
    You can ignore 1, and 0 corresponds to space
    >>> keypad_string("12345")
    'adgj'
    >>> keypad_string("4433555555666")
    'hello'
    >>> keypad_string("2022")
    'a b'
    >>> keypad_string("")
    ''
    >>> keypad_string("111")
    ''
    '''
    if keys == "":
        return keys
    key_to_letters = generate_key_to_letters()
    result = ""
    curr_key = ""
    count = 0
    for key in keys:
        if key == "1":
            pass
        elif not curr_key:
            curr_key = key
            count = 1
        else:
            letters = key_to_letters[key]
            # if pressing same key
            if key == curr_key:
                # if pressed X times already
                if count == len(letters):
                    result += letters[-1]
                    count = 1
                else:
                    count += 1
            # not pressing same key
            else:
                prev_letters = key_to_letters[curr_key]
                result += prev_letters[count - 1]
                curr_key = key
                count = 1
    # add last letter
    if curr_key:
        result += letters[count - 1]
    return result
