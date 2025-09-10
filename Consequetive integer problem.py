def seq(lt):
    if len(set(lt)) != 5:
        return False

    for i in range(1, len(lt)):
        if lt[i] == lt[i - 1]:
            return False

    return True
print(seq([1,2,2,3,4,5,2,3,5,4,1,3,2,5]))
