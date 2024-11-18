''' All these questions are generated by ChatGPT '''

from collections import OrderedDict


class ordereddicts():

    '''Question : 1 
Suppose you’re using an OrderedDict to store data with integer values. 
Write a function that takes this OrderedDict and returns a new OrderedDict ,
with items sorted by their values in ascending order while preserving the original keys.'''

    def sort_data_by_values(ordered_data):
        sorted_ordered_dict = OrderedDict(sorted(ordered_data.items() ,key = lambda item:item[1]))

        return sorted_ordered_dict

    '''Question 2: You have an OrderedDict containing items with string keys and integer values. 
    Write a function to rotate the dictionary’s elements by n positions to the right,
    so that the last n items appear at the beginning of the dictionary while preserving the relative order of all elements.'''

    def rotate_dictionary(ordered_data,n):
        # Convert OrderedDict to a list of items for easier manipulation
        items = list(ordered_data.items())

        # Calculate the effective rotation by taking n modulo the length of the dictionary
        n = n % len(items)

        # Perform the rotation
        rotated_items = items[-n:] + items[:-n]

        # Convert the rotated list of items back into an OrderedDict
        return OrderedDict(rotated_items)

    '''Question 3 :You have an OrderedDict where each key is a product name (string),
      and each value is the product price (integer). 
      Write a function that updates the price of each product by applying a discount, 
      where the discount percentage is provided as a parameter to the function. 
      The function should return a new OrderedDict with the updated prices, while keeping the original order intact.'''

    def calculate_discount(ordered_data,percentage):
        for index,(key,value) in enumerate(ordered_data.items()):
            price = ordered_data[key]
            new_price = round(price*((100-percentage)/100),2)
            ordered_data[key] = new_price

        return ordered_data
    
    '''Question 4 : Given an OrderedDict where each key represents a student's name 
       and each value is a list of their grades (integers), write a function that calculates 
      the average grade for each student and returns a new OrderedDict with students' names
      as keys and their average grade as values. The order of students should remain the 
      same as in the original dictionary.'''

def main():
    data_dict = OrderedDict([('a', 3), ('b', 1), ('c', 2)])
    sorted_dicts = ordereddicts.sort_data_by_values(data_dict)
    print(sorted_dicts)

    price_dicts = OrderedDict([('Book', 100), ('Pencil', 20), ('Ruler',10 )])
    new_price_dicts = ordereddicts.calculate_discount(price_dicts,10)
    print(new_price_dicts)

if __name__ == "__main__":
    main()