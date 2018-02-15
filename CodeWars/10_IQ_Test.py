# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)

def iq_test(numbers):
    numbers = numbers.split(' ')

    odd_numbers = filter(lambda x: int(x) % 2 == 1, numbers)
    even_numbers = filter(lambda x: int(x) % 2 == 0, numbers)

    return numbers.index(odd_numbers[0])+1 if len(even_numbers) > len(odd_numbers) else numbers.index(even_numbers[0])+1
