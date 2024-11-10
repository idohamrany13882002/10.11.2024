from re import match


def is_negative(a: int)-> bool:
    return True if a<0 else False

is_negative_lm = lambda a: a<0

def get_int(a):
    return a**2

get_int_lm = lambda a: a**2


def __main__():
    if __name__ == "__main__":
        print(is_negative(-5))
        print(is_negative(3))
        print(is_negative(0))

        print(is_negative_lm(-5))
        print(is_negative_lm(3))
        print(is_negative_lm(0))

        print(get_int(0))
        print(get_int(3))
        print(get_int(9))
        print(get_int_lm(0))
        print(get_int_lm(3))
        print(get_int_lm(9))

        num_list:list[int] = [-4,0,2,-1,3,9]
        result_list: list [int] = []
        for x in num_list:
            if x>0:
                result_list.append(x)
        print(result_list)
        print(list(filter(lambda x: x > 0, [-4, 0, 2, -1, 3, 9])))
        print(list(filter(lambda x: x, [-4, 0, 2, -1, 3, 9])))
        print(list(filter(lambda x: x %2==0 and x!=0, [-4, 0, 2, -1, 3, 9])))
        print(list(filter(lambda x: x %2==0 and x>0, [-4, 0, 2, -1, 3, 9])))

        print(list(filter(lambda word:len(word) > 6, ["apple", "Anaconda", "banana", "pineapple", "coconut", "Am-pm"])))
        print(list(filter(lambda word:"-" in word, ["apple", "Anaconda", "banana", "pineapple", "coconut", "Am-pm"])))

        num_list: list[int] = [-4, 0, 2, -1, 3, 9]
        result_list: list[int] = []
        for x in num_list:
            result_list.append(x**2)
        print(result_list)
        print(list(map(lambda x:x**2 , [-4, 0, 2, -1, 3, 9])))
        print(list(map(lambda word: len(word), ["zzzzz", "b", "abc", "cccc", "cc", "t"])))
        print(list(map(lambda x: x//10,[54, 20, 12, 83, 33, 99])))
        print(list(map(lambda x: "even" if x%2==0 else "odd" ,[54, 20, 12, 133, 83, 9989])))
__main__()