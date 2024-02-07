def interleave_strings(string_1, string_2):
    interleaved_string = ''.join(a + b for a,b in zip(string_1, string_2))
    if len(string_1) > len(string_2):
        interleaved_string += string_1[len(string_2):]
    elif len(string_1) < len(string_2):
        interleaved_string += string_2[len(string_1):]
    return interleaved_string

string_1 = "AAAA"
string_2 = "1234567"
interleaved_result = interleave_strings(string_1, string_2)
print(interleaved_result)