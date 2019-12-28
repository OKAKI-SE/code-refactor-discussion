"""
2つの値の足し算と引き算の結果を表示する
"""

def calc_add(num1, num2):
    result_add = num1 + num2
    return result_add

def calc_sub(num1, num2):
    result_sub = num1 - num2
    return result_sub


if __name__ == "__main__":
    add = calc_add(10, 5)
    sub = calc_sub(10, 5)

    print(f"{add}")
    print(f"{sub}")
