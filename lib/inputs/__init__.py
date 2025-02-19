def readInt(txt: str) -> int:
    """
    -> Read a int
    :param txt: Text that be used to ask or require to user
    :return: The number that user typed
    """
    while True:
        try:
            num = int(input(txt))
        except (TypeError, ValueError):
            print('\033[0;31mERRO: Digite um número inteiro!\033[0m')
        else:
            break
    return num
