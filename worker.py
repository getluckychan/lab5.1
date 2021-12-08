from pay import Pay
from sys import exit


def main():
    try:
        total = Pay()
        total.read()
        print(total.display())
    except BaseException:
        exit("Щось пішло не так")

main()
