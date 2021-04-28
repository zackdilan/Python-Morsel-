import re


def count_words(string):
    string_list = string.lower().split(" ")
    # dict comphrehension with an if statement
    # first we loop over the list with for in ----
    # for the dict -- key will be the words
    '''(some_key if condition else default_key):(something_if_true if condition
    
              else something_if_false) for key, value in dict_.items() }
              
              
    '''
    my_dict = {}

    for key in string_list:
        if key in list(my_dict):
            my_dict[key] = my_dict[key] + 1
        else:
            my_dict[key] = 1
    return my_dict


def count_words_nopunc(string):
    regex = r'\w+'
    string_list = re.findall(regex, string.lower())
    print(string_list)
    my_dict = {}

    for key in string_list:
        if key in list(my_dict):
            my_dict[key] = my_dict[key] + 1
        else:
            my_dict[key] = 1
    return my_dict


def count_words_dict_comprehension(string):
    regex = r'\w+'
    string_list = re.findall(regex, string.lower())
    my_dict = {key: 1 for key in string_list}


def count_words_dict_get(string):
    regex = r'\w+'
    string_list = re.findall(regex, string.lower())
    print(string_list)
    my_dict = {}
    for key in string_list:
        my_dict[key] = my_dict.get(key, 0) + 1
    return my_dict


#print(count_words("Oh my god oh"))

#print(count_words_nopunc("OH oh my God god !"))

print(count_words_dict_get("OH oh my God god !"))
