#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    for item in range(len(weights)):
        difference = limit - weights[item]
        check = hash_table_retrieve(ht, difference)
        if check != None:
            return [item, check]
        hash_table_insert(ht, weights[item], item)

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
