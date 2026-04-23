def load_dictionary():
    file = open('./dictionary.txt')
    word_list = [word.strip() for word in file.readlines()]
    file.close()

    return word_list
