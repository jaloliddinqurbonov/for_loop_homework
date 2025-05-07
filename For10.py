def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    l1=[]
    for i in list1:
        l1.append(i.capitalize())
    return l1
print(main(['sdadfa','AFAKJSFNIAJ','fiurife']))