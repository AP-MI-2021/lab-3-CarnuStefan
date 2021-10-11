'''
Lab-3

3.Numerele au semne alternante.
Funcția de calcul: get_longest_alternating_signs(lst: list[int]) -> list[int]

17.Media numerelor nu depășește o valoare citită.
Funcția de calcul: get_longest_average_below(lst: list[int], average: float) -> list[int]
'''
def  get_longest_alternating_signs(lst: list[int]) -> list[int]:
    '''
    Determina cel mai lung subsir in care numerele au semne alternante
    :param lst: lista de numere
    :return: lista cu subsirul cel mai lung
    '''
    result=[]
    n=len(lst)
    for st in range (n):
        for dr in range (st,n):
            prev=st
            all_alternating=True
            for num in lst[st:dr+1]:
                if(prev>0 & num>0):
                    all_alternating=False
                    break
                elif(prev<0 & num<0):
                    all_alternating=False
                    break
                else: prev=num
            if all_alternating:
                if dr-st+1>len(result):result=lst[st:dr+1]
    return result

def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([1,2,-3,4,-8,-9,20,-18,12,-1,10]) == [20,-18,12,-1]


def read_lst():
    lst=[]
    lst_str=input('Introduceti numere separate prin spatiu: ')
    lst_str_split=lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst

def showmenu():
    print("1. Citire date")
    print("2. Proprietatea 1: Numere alternante ")
    print("3. ")
    print("x. Exit")

def main():
    while True:
        print("1. Citire date")
        print("2. Proprietatea 1: Numere alternante ")
        print("3. ")
        print("x. Exit")
        opt=input('Alegeti optiunea: ')
        if opt=='1':
            lst=read_lst()
        elif opt=='2':
            get_longest_alternating_signs(lst)
        elif opt=='x':
            break


    if __name__ =='__main__':
        main()