#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for item in range(length):
        flight_source = tickets[item].source
        flight_destination = tickets[item].destination
        hash_table_insert(hashtable, flight_source, flight_destination)

    # looking for capital NONE
    route[0] = hash_table_retrieve(hashtable, 'NONE')
    for item in range(1, length):
        route[item] = hash_table_retrieve(hashtable, route[item - 1])

    return route
