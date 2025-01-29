tkts=[1,2,3,4,5]
def show():
    print('available tkts')
    for x in tkts:
        print(x)
class bus_booking:
    def book_tkts(self):
        show()
        user=int(input('how many tkts:'))
        for x in range(user):
            tkt_no=int(input('enter seat number:'))
            if tkt_no in tkts:
                print('tkt is booked')
                tkts.remove(tkt_no)
            else:
                print('tkt is not available')
        show()
ola=bus_booking()
ola.book_tkts()