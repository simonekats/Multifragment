import math
import sys

TRAVEL_TIME = {
      ('A', 'C') : 15.976382208502129,
      ('A', 'D') : 16.402883717428008,
      ('A', 'B') : 12.754767943744977,
      ('A', 'E') : 17.947152920286506 ,
      ('C', 'D') : 12.32859981207251 ,
      ('C', 'B') : 8.808173202742672 ,
      ('C', 'E') : 14.462432168259102 ,
      ('D', 'B') : 9.273083486260663 ,
      ('D', 'E') : 14.865653168331152 ,
      ('B', 'E') : 12.440967365690549 ,
}

L = list(set([item for k in TRAVEL_TIME.keys() for item in k]))

def list_minus(L, x):
    """Returns a list of L that does not have x in it."""
    return list(set(L)-set([x,]))

def travel_time(x, y):
    """Looks up x and y in TRAVEL_TIME in a way that order does not matter, returns a time"""
    global TRAVEL_TIME
    try:
        tm = TRAVEL_TIME[(x,y)]
    except:
        tm = TRAVEL_TIME[(y,x)]
    return tm


def lighthouse_names(L):
    # Gets a list of the names of the lighthouses in dictionary L
    return list(set([item for k in TRAVEL_TIME.keys() for item in k]))


def mergeSort(tempList, indexValue):
    if len(tempList) < 2:
        return tempList
    middle = len(tempList) // 2
    left = tempList[:middle]
    right = tempList[middle:]
    mergeSort(left, indexValue)
    mergeSort(right, indexValue)
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
        if left[i][indexValue] < right[j][indexValue]:
            tempList[k] = left[i]
            i += 1
        else:
            tempList[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        tempList[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        tempList[k] = right[j]
        j += 1
        k += 1
    return tempList


def is_closing_tour(edge, tour):
    if not tour:
        return False
    for segment in tour:
        if edge[0] in [segment[0], segment[-1]] and edge[1] in [segment[0], segment[-1]]:
            return True
    return False


def is_between_tour(edge, tour):
    if not tour:
        return False
    for segment in tour:
        if edge[0] not in [segment[0], segment[-1]] and edge[1] not in [segment[0], segment[-1]]:
            return True
    return False


def add_edge(edge, tour):
    if not tour:
        tour.append(list(edge))
    else:
        for segment in tour:
            if edge[0] in segment:
                if edge[0] == segment[0]:
                    segment.insert(0, edge[1])
                else:
                    segment.append(edge[1])
            elif edge[1] in segment:
                if edge[1] == segment[0]:
                    segment.insert(0, edge[0])
                else:
                    segment.append(edge[0])
            else:
                tour.append(list(edge))
    return tour


def combine_tour(tour):
    new_tour = []
    for segment in tour:
        new_tour.extend(segment)
    return new_tour

MF_COUNT = 0

def multi_fragment(L):
    global MF_COUNT
    tour = []
    total_time = 0.0

    sorted_edges = mergeSort(TRAVEL_TIME.items(), 1)
    lights = list(set([item for k in TRAVEL_TIME.keys() for item in k]))
    list_node = lighthouse_names(L)

    for edges_list in sorted_edges:
        MF_COUNT += 1
        edge = edges_list[0]
        if (is_closing_tour(edge, tour) and len(tour) > 0 and len(tour[0]) < len(list_node)) or (is_between_tour(edge, tour)):
            continue
        if (is_closing_tour(edge, tour) and len(tour[0]) == len(list_node)):
            break

        tour = add_edge(edge, tour)
        total_time += travel_time(edge[0], edge[1])

    return total_time, combine_tour(tour)

if __name__ == '__main__':
    print(multi_fragment(TRAVEL_TIME))
