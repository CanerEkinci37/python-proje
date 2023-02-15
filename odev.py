def flatten_list(l):
    # Recursive
    if not isinstance(l, list):
        return [l]  # Eğer dizi elemanı değilse dizi olarak döndürecek
    elif not l:
        return []   # Eleman dizi olabilir fakat boş diziyse [l] yaparsak [[]] olacaktır bu yüzden [] döndürülür
    else:
        return flatten_list(l[0]) + flatten_list(l[1:])     # Eğer eleman dizi ise ilk eleman ve geri kalan elemanlara
                                                            # ayrılır ve kucuk parcalara ayrılır + operatoruyle liste
                                                            # birleştirilir.



def reversed_list(l):
    if isinstance(l, list):
        return [reversed_list(element) for element in l[::-1]]      # Liste ters çevrilip elemanlar                                                        
    else:                                                           # içinde liste kontrolu yapılır ve ters çevrilir
        return l                                                    # eğer eleman liste değil ise kendisi döndürülür
        


l1 = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
print(flatten_list(l1))

l2 = [[[1, 2]], [[3, 4]], [5, 6, 7]]
print(reversed_list(l2))
