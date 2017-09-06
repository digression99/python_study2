def safe_sum(a, b):
    if type(a) != type(b):
        print("더할수 있는 것이 아닙니다.")
        return
    else:
        result = sum(a, b)
    return result

def sum(a, b):
    return a + b


if __name__ == "__main__":
    print(safe_sum('a', 4))
    print(safe_sum(1, 4))

    
