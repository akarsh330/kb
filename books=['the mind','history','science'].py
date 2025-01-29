books=['the mind','history','science']
class lib:
    def request_books(self):
        for x in books:
            print(x)
        req=input('enter name :')
        return req
    def lending_book(self,catcher):
        if catcher in books:
            print('the book is available and take it')
        else:
            print('the book is not availble')
l1=lib()
catcher=l1.request_books()
print(catcher)
l1.lending_book(catcher)

