def main(list1):
    """
    A list of several elements is given. Return this list by adding the reverse.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
    l=list1[::-1]
    return list1+l
print(main(list1=['a','b','c','d']))