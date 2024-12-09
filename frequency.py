def freqency(value):
    dictionary = {}
    for i in value:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1
    print(dictionary)


if __name__ == '__main__':
    value = input("Enter the string:")
    freqency(value)
    