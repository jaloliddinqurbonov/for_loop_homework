def main(A,B):
    """
    Return the numbers from B to A in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    l=[]
    for i in range(A,B):
        l.append(i)
    return l[-1::-1]
print(main(12,34))