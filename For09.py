def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    l=[]
    for i in range(1,11):
        l.append(f"{i} kg shrinlikning narxi - {i*price} so'm")
    return l
print(main(10))