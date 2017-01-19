
def find_missing(lst1, lst2):
    print "Convert both lists to sets using inbuilt set constructor"
    set1 = set(lst1)
    set2 = set(lst2)
    print "Compare sets using the == comparison operator"
    if set1 == set2:
        print "Return 0 if they are equal"
        return 0
    else:
        print "Get the symmetric difference of the two sets and return the value in the resulting set if the are not equal"
        set_diff = set1^set2
        return set_diff.pop()

