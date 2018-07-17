def positive_divide(numerator, denominator):

    try:
        total = numerator / denominator
        if total < 0:
            raise ValueError
        else:
            return total
    except ZeroDivisionError:
        return 0
    except Exception as e:
        raise e


if __name__ == '__main__':
    positive_divide(10, 0)

