import rqdatac
from indicator import calc_max_drawback


def main():
    print("max_drawback: ", calc_max_drawback("600519.XSHG"))
    print("max_drawback: ", calc_max_drawback("000300.XSHG"))


if __name__ == "__main__":
    rqdatac.init()
    main()
