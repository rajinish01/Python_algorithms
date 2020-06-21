def find_mismatch(s1, s2):
    count = 0
    for i, j in zip(s1.lower(), s2.lower()):
        if i != j:
            count += 1
    if len(s1.lower()) != len(s2.lower()) or count > 2:
        return 2
    elif count == 0:
        return 0
    elif count < 2:
        return 1


def _instructor_function (s1,s2):
    if len(s1) != len(s2):
        return 2
    s1=s1.lower()
    s2=s2.lower()
    number_of_mismatches=0
    for index in range(len(s1)):
        if s1[index] != s2[index]:
            number_of_mismatches=number_of_mismatches+1
            if number_of_mismatches>1:
                return 2
    return number_of_mismatches
