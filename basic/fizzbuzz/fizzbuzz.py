"""
FizzBuzz.
- 数字を文字列で返す
  - 1を渡したら文字列"1"を返す
  - 2を渡したら文字列"2"を返す
ただし、
- 3で割り切れる数の場合は「Fizz」と返す
- 5で割り切れる数の場合は「Buzz」と返す
- 3と5で割り切れる数の場合は「FizzBuzz」と返す
"""


def fizz_buzz(num):
    if num % 5 == 0 and num % 3 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return str(num)

if __name__ == "__main__":
    for i in range(1, 51):
        result = fizz_buzz(i)
        print(result)
