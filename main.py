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
            prev=lst[st]
            all_alternating=True
            for num in  lst[st+1:dr+1]:
                if(prev>=0 and num>=0):
                    all_alternating=False
                    break
                if(prev<0 and num<0):
                    all_alternating=False
                    break
                
                prev=num
            if all_alternating ==True:
                if dr-st+1>len(result):result=lst[st:dr+1]
    print (result)
    return result

def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([1,2,-3,4,-8,-8,0,0,-18,12,-1,10]) == [0,-18,12,-1,10]

def get_longest_average_below(lst: list[int], average: float) -> list[int]:
    '''
    Determina cel mai lung subsit in care media elementelor este mai mica sau egala cu numarul dat
    :param lst: lista cu numere
    :param avarage: numarul dat
    :return: lista cu cel mai lung subsir
    '''
    result=[]
    n=len(lst)
    for st in range (n):
        for dr in range (st,n):
            sum=0
            nr=0
            average_ok=True
            for num in  lst[st:dr+1]:
                sum=sum+num
                nr=nr+1
            if average<(sum/nr):
                average_ok=False
            if average_ok ==True:
                if dr-st+1>len(result):result=lst[st:dr+1]
    print (result)
    return result

def test_get_longest_average_below():
    assert get_longest_average_below([7,24,5,90,6,4],5)==[6,4]

def read_lst():
    lst=[]
    lst_str=input('Introduceti numere separate prin spatiu: ')
    lst_str_split=lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst

def showmenu():
    print("1. Citire date")
    print("2. Proprietatea 1: Numere cu semne alternante ")
    print("3. Proprietatea 2: Numere cu media mai mica decat valoarea data")
    print("x. Exit")

def main():
    while True:
        showmenu()
        opt=input('Alegeti optiunea: ')
        if opt=='1':
            lst=read_lst()
        elif opt=='2':
            get_longest_alternating_signs(lst)
        elif opt=='3':
            avrg=float(input('Introduceti valoarea mediei'))
            get_longest_average_below(lst,avrg)
        elif opt=='x':
            break


if __name__ =='__main__':
    test_get_longest_alternating_signs()
    test_get_longest_average_below()
    main()