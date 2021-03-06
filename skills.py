"""Skills Assessment: Lists

Edit the function bodies until all of the doctests pass when you run this file.
"""


def print_list(my_list):
    """Print each item in the input list

        >>> print_list([1, 2, 6, 3, 9])
        1
        2
        6
        3
        9

    """

    for items in my_list:
        print items 



def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    # """
    odd_list = []

    for number in number_list:
        if number%2 == 1:
            odd_list.append(number)
        else:
            pass

    return odd_list


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """

    even_list = []

    for num in number_list: 
        if num%2 == 0:
            even_list.append(num)
        else:
            pass

    return even_list


def every_other_item(my_list):
    """Return a list that contains every other item in my_list starting
       with the first item.

       >>> every_other_item([1, 2, 3, 4, 5, 6])
       [1, 3, 5]

       >>> every_other_item(["you", "friend", "are", "very", "good", " ", "at", " ", "coding"])
       ['you', 'are', 'good', 'at', 'coding']

    """

    new_list = []
    new_list_items = my_list[::2] #Move up 2 indices through entire list, starting at index[0]

    for item in new_list_items:
        new_list.append(item) 

    return new_list

def print_indexes(my_list):
    """Print the index of each item in the input_list, followed by the item itself.

    Do this without using a counting variable---that is, don't do something
    like this:

        count = 0
        for item in list:
            print count
            count = count + 1

    Output should look like this:

        >>> print_indexes(["Toyota", "Jeep", "Volvo"])
        0 Toyota
        1 Jeep
        2 Volvo

    """

    #Length of list is 3, range then creates list of numbers up to 3
    for index in range(len(my_list)): 
        print index, my_list[index]



def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """

    # Find length of word by referring to length of index

    long_char_list = []

    for word in word_list:
        if len(word) > 4: 
            long_char_list.append(word)


    return long_char_list


def n_long_words(word_list, n):
    """Return all words in input list that are longer than n characters.

    >>> n_long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"], 3)
    ['hello', 'spam', 'spam', 'bacon', 'bacon']

    >>> n_long_words(["I", "like", "apples", "bananas", "you"], 5)
    ['apples', 'bananas']
    """

    long_list = []

    for word in word_list:
        if len(word) > n:
            long_list.append(word)

    return long_list

def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

    DO NOT USE the built-in function `min`!

        >>> smallest_int([-5, 2, -5, 7])
        -5


        >>> smallest_int([3, 7, 2, 8, 4])
        2

    If the input list is empty, return None:


        >>> smallest_int([]) is None
        True

    """

    #Have each number in list check if it is smaller than the other

    if number_list == []:
        return None 

    min_number = number_list[0]
    number_list = number_list[1:]

    #If number in the list is smaller than the first element, make num the new min
    for num in number_list:
        if num < min_number: 
            min_number = num
    return min_number


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

    DO NOT USE the built-in function `max`!

        >>> largest_int([-5, 2, -5, 7])
        7

        >>> largest_int([3, 7, 2, 8, 4])
        8

    If the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """

    if number_list == []:
        return None 

    max_number = number_list[0]
    number_list = number_list[1:]

    for num in number_list:
        if num > max_number:
            max_number = num
    return max_number

def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are odd, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """

    halved_numbers = []
    

    for num in number_list: 
        new_num = float(num)
        half_num = (new_num)/2.0
        halved_numbers.append(half_num)


    return halved_numbers


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """

    length_list = []

    for word in word_list: 
        length = len(word)
        length_list.append(length)

    return length_list


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """

    if number_list == []:
        sum_num = 0
        return sum_num 

    sum_num = number_list[0]
    number_list = number_list[1:] 

    for num in number_list:
        sum_num += num 
    return sum_num 


def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """

    if number_list == []:
        product = 1
        return product 

    product = number_list[0]
    number_list = number_list[1:]

    for num in number_list:
        product *= num
    return product 


def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python has a built-in method on lists, `join`---but for this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    if word_list == []:
        return ''

    new_word = word_list[0]
    word_list = word_list[1:]

    for word in word_list: 
        new_word += word
    return new_word

def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """

    sum_num = float(number_list[0])
    length = len(number_list)
    number_list = number_list[1:]

    for num in number_list: 
        sum_num += num  
        avg_num = sum_num/length
    return avg_num


def join_strings_with_comma(list_of_words):
    """Return ['list', 'of', 'words'] like "list, of, words".

        >>> join_strings_with_comma(["Labrador", "Poodle", "French Bulldog"])
        'Labrador, Poodle, French Bulldog'

    If there's only one thing in the list, it should return just that
    thing, of course:

        >>> join_strings_with_comma(["Pretzel"])
        'Pretzel'

    """

    new_word = list_of_words[0]
    list_of_words = list_of_words[1:]

    for word in list_of_words: 
        new_word += ", {}".format(word)
    return new_word 


def foods_in_common(foods1, foods2):
    """Using ANY Python data structure presented in the last week, given 2 lists of foods, 
    return a set of items that are in common between the two. (Don't include any duplicates
    in the output collection.)
    
    For example:

    >>> foods_in_common(["cheese", "bagel", "cake"], ["hummus", "beets", "bagel", "lentils"])
    set(['bagel'])

    If there are no foods in common, return an empty set.

    >>> foods_in_common(["lamb", "chili", "cheese"], ["cake", "ice cream"])
    set([])

    """

    #Want to traverse through list of foods and match any foods together
    common_food = set([])

    total_food = foods1 + foods2 #Combine lists to create one large list 

    for food in total_food:
        if food in common_food:
            pass
        #If food appears more than once in joint list, food was in both lists
        elif total_food.count(food) > 1:
          common_food.add(food)

    return common_food


def reverse_list(my_list):
    """Return the inputted list, reversed.

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

    Do not use the python methed reverse()/reversed().

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']

    """
    new_list = []
    index = 0

    for item in my_list: 
        index = index-1
        new_item = my_list[index]
        new_list.append(new_item)

    return new_list


def reverse_list_in_place(my_list):
    """Return the inputted list reversed--WITHOUT creating a new list.
       This will involve moving the items in my_list to different positions 
       in the same list.

       Do not use the python methed reverse()/reversed()

        >>> reverse_list([1, 2, 3])
        [3, 2, 1]

        >>> reverse_list(["cookies", "love", "I"])
        ['I', 'love', 'cookies']
    """
    
    index = 0 
    reverse_index = -1

    for item in my_list: 
        my_list[index] = my_list[reverse_index] 
        index = index+1
        reverse_index = reverse_index-1

    return my_list

    #Was not able to get this error fixed but my thought process is below
    # 1. To start, set item at index 0 equal to last item of list
    # 2. Increase index by 1 to rebind the next item 
    # 3. Decrease reverse index by 1 to bind next item of list to my_list[index]

def duplicates(my_list):
    """
    "Return a list of words which are duplicated in the input list. 
    The returned list should be in ascending order." 
  
    >>> duplicates(["apple", "apple", "banana", "cherry", "banana", "apple"])
    ['apple', 'banana']

    >>> duplicates([1, 2, 2, 4, 4, 4, 7])
    [2, 4]
    

    """

    duplicate_list = []

    for item in my_list: #To prevent repeat items in new list 
        if item in duplicate_list: 
            pass 
        elif my_list.count(item) > 1: 
            duplicate_list.append(item)
            duplicate_list.sort()
        
    return duplicate_list 


def find_letter_indices(list_of_words, letter):
    """Given a list of words and a letter, return a list of integers that correspond
    to the index of the first occurance of the letter in that word.

    Do not use the .index() list method.

    >>> find_letter_indices(['odd', 'dog', 'who'], 'o')
    [0, 1, 2]

    If the letter doesn't occur in one of the words, use None for that word in
    the output list. For example:

    >>> find_letter_indices(['odd', 'dog', 'who', 'jumps'], 'o')
    [0, 1, 2, None]

    """

    occurance_list = []
    list_index = 0
    letter_index = 0

    for words in list_of_words:
        if letter == list_of_words[list_index][letter_index]:
            occurance_list.append(letter_index)
            list_index += 1
        elif letter != list_of_words[list_index][letter_index]:
            index = None
            occurance_list.append(index)
        letter_index += 1

    return occurance_list

def largest_n_items(input_list, n):
    """Given a list of integers along with an integer n, return a 
    list of the largest n numbers in the input list in ascending order. 

    You can assume that n will be less than the length of the list. 

    For example:

    >>> largest_n_items([2, 6006, 700, 42, 6, 59], 3)
    [59, 700, 6006]

    """

    new_list = []

    max_number = input_list[0]
    input_list = input_list[1:]

    #If length of new list does not equal n, keep running loop until len(new_list) = n
    for num in input_list:
        if len(new_list) != n: 
            if num > max_number:  
                max_number = num  
                new_list.append(max_number)

    return new_list
    #Output continues to give maximum number only 


#Did not pass reverse_list_in_place, largest_n_items

##############################################################################
# END OF ASSIGNMENT: You can ignore everything below.
if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print

