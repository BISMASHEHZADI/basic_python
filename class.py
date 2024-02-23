
op = library()

    

import random
class library:
    def __init__(self):
        ser = input(
            """
            enter any choice below it
            1.loan of book
            2.add book
            3.show books
            4.choose book

            
            
            
            
            """
        )
        if ser == '2':
            self.add()
        elif ser=='1':
            self.loan()
        elif ser=='3':
            self.show()
        else:
            self.chhose()



        # elif ser=='3':
            # self.show()







    def add(t):
        li = ['think befor you speak','my life my hero','romeo juliet','love story','poetry allama iqbal']
        t = input('enter the name of book : ')
        li.append(t)
        print('book added successfully')
        u = input("if you want to show all books write there 's' : ")
        if u=='s':
            for i in li:
                print(i)        
    def loan(self):
        li = ['think befor you speak','my life my hero','romeo juliet','love story','poetry allama iqbal']
        o = input('enter the name of book that you want to borrow: ')
        if o in li:
            li.remove(o)
            print(f'you have borrowed book that is {o}')
            print('now i have list of books that are given below please come again')
            for i in li:
                print(f'{i}')


    def show(self):
        li = ['think befor you speak Rs:500','my life my hero Rs:300','romeo juliet Rs:400','love story Rs:600','poetry allama iqbal Rs:700']
        
        # k = random.choice([100,200,600,500])
        # print(f'Price {k}')
        # print(f'Price {k}')
        # print(f'Price {k}')
        # print(f'Price {k}')
        for i in li:
            print(f'Book {i}')
    def chhose(self):
        li = ['think befor you speak Rs:500','my life my hero Rs:300','romeo juliet Rs:400','love story Rs:600','poetry allama iqbal Rs:700']
        for y in li:
            print(y)
        g = input('choose any book: ')
        print(f'here is a deteil of this book {g}')
        j = input('if you want any type of discount y/n ')
        p = [50,100,40,80,60]
        r = random.choice(p)
        if j=='y':
            print(f'i have gave you discout of Rs: {r}%')
        else:
            print(f'you have bought the that is {g}')


            

            
        
