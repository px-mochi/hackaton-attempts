def test():
    s = "CDDCCCCCCDDDD"
    n = len(s)  # Number of animals
    d = 10 # Dog food portions
    c = 20 # Cat food portions
    m = 2 # Additional Cat food portions

def any_dogs_left(s):
        if "D" in s:
            return True
        else:
            return False

def process_test_case(test_case, test_case_num):
    info = test_case[0]
    scenario = test_case[1]

    info = [int(i) for i in info.split()]
    n = info[0]
    d = info[1]
    c = info[2]
    m = info[3]

    y = "YES"
    for i, animal in enumerate(scenario):
        if any_dogs_left(scenario[i:]) == False:
            break
        if animal == "C":
            c -= 1
            if c < 0:
                y = "NO"
                break
        else:
            d -= 1
            if d < 0:
                y = "NO"
                break
            else:
                c += m

    print(f"Case #{test_case_num}: {y}")



def main():
    T = int(input())  # Number of test cases

    test_case_num = 1
    for line in range(T*2):
        if line % 2 == 0:
            test_case = []
            T_1 = input()
            test_case.append(T_1)
        else:
            T_2 = input()
            test_case.append(T_2)
            process_test_case(test_case, test_case_num)
            test_case_num += 1

if __name__ == "__main__":
    main()