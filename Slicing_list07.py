def main(list1,n):
    """
    A list of several elements is given. Return all items from the beginning in n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    return list1[::n]
print(main(['a', 1, 'b', 2, 'c', 3, 'd', 4],2))
print(main([5,4,3,2,1,0],-1))