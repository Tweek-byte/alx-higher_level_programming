#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def mrd(element):
        return (element if element != search else replace)
    return list(map(mrd, my_list))
