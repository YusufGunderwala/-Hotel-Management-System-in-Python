class Customer:
    def __init__(self):
        self.name = ""
        self.address = ""
        self.phone = ""
        self.from_date = ""
        self.to_date = ""
        self.payment_advance = 0.0
        self.booking_id = 0


class Room:
    def __init__(self):
        self.type = ""
        self.stype = ""
        self.ac = ""
        self.roomNumber = 0
        self.rent = 0
        self.status = 0
        self.cust = Customer()

    @classmethod
    def addRoom(cls, rno):
        room = cls()
        room.roomNumber = rno
        room.ac = input("\nType AC/Non-AC (A/N) : ")
        room.type = input("\nType Comfort (S/N) : ")
        room.stype = input("\nType Size (B/S) : ")
        room.rent = int(input("\nDaily Rent : "))
        room.status = 0
        print("\n Room Added Successfully!")
        input()
        return room

    def searchRoom(self, rno):
        found = False
        for room in rooms:
            if room.roomNumber == rno:
                found = True
                break

        if found:
            print("Room Details")
            if room.status == 1:
                print("\nRoom is Reserved")
            else:
                print("\nRoom is available")
            self.displayRoom(room)
            input()
        else:
            print("\nRoom not found")
            input()

    @staticmethod
    def displayRoom(tempRoom):
        print("\nRoom Number: \t", tempRoom.roomNumber)
        print("Type AC/Non-AC (A/N) ", tempRoom.ac)
        print("Type Comfort (S/N) ", tempRoom.type)
        print("Type Size (B/S) ", tempRoom.stype)
        print("Rent: ", tempRoom.rent)


class HotelMgnt(Room):
    def guestSummaryReport(self):
        if count == 0:
            print("\n No Guest in Hotel !!")
        for room in rooms:
            if room.status == 1:
                print("\n Customer First Name : ", room.cust.name)
                print("Room Number : ", room.roomNumber)
                print("Address (only city) : ", room.cust.address)
                print("Phone : ", room.cust.phone)
                print("---------------------------------------")
        input()

    def checkIn(self):
        found = False
        rno = int(input("\nEnter Room number : "))
        for room in rooms:
            if room.roomNumber == rno:
                found = True
                break

        if found:
            if room.status == 1:
                print("\nRoom is already Booked")
                input()
                return

            room.cust.booking_id = int(input("\nEnter booking id: "))
            room.cust.name = input("\nEnter Customer Name (First Name): ")
            room.cust.address = input("\nEnter Address (only city): ")
            room.cust.phone = input("\nEnter Phone: ")
            room.cust.from_date = input("\nEnter From Date: ")
            room.cust.to_date = input("\nEnter to  Date: ")
            room.cust.payment_advance = float(
                input("\nEnter Advance Payment: "))
            room.status = 1
            print("\n Customer Checked-in Successfully..")
            input()

    def getAvailRoom(self):
        found = False
        for room in rooms:
            if room.status == 0:
                self.displayRoom(room)
                print("\n\nPress enter for next room")
                found = True
                input()
        if not found:
            print("\nAll rooms are reserved")
            input()

    def searchCustomer(self, pname):
        found = False
        for room in rooms:
            if room.status == 1 and room.cust.name.lower() == pname.lower():
                print("\nCustomer Name: ", room.cust.name)
                print("Room Number: ", room.roomNumber)
                print("\nPress enter for next record")
                found = True
                input()
        if not found:
            print("\nPerson not found.")
            input()

    def checkOut(self, roomNum):
        found = False
        days = 0
        billAmount = 0.0
        for room in rooms:
            if room.status == 1 and room.roomNumber == roomNum:
                found = True
                break

        if found:
            days = int(input("\nEnter Number of Days:\t"))
            billAmount = days * room.rent

            print("\n\t######## CheckOut Details ########\n")
            print("Customer Name : ", room.cust.name)
            print("Room Number : ", room.roomNumber)
            print("Address : ", room.cust.address)
            print("Phone : ", room.cust.phone)
            print("Total Amount Due : ", billAmount, " /")
            print("Advance Paid: ", room.cust.payment_advance, " /")
            print("*** Total Payable: ", billAmount -
                  room.cust.payment_advance, "/ only")

            room.status = 0
        input()


def manageRooms():
    opt = 0
    rno = 0
    flag = 0
    while opt != 3:
        print("\n### Manage Rooms ###")
        print("1. Add Room")
        print("2. Search Room")
        print("3. Back to Main Menu")
        opt = int(input("\nEnter Option: "))

        if opt == 1:
            rno = int(input("\nEnter Room Number: "))
            flag = 0
            for room in rooms:
                if room.roomNumber == rno:
                    flag = 1
                    break
            if flag == 1:
                print("\nRoom Number is Present.\nPlease enter a unique Number")
                flag = 0
                input()
            else:
                rooms.append(Room.addRoom(rno))
        elif opt == 2:
            rno = int(input("\nEnter room number: "))
            room.searchRoom(rno)
        elif opt == 3:
            pass
        else:
            print("\nPlease Enter correct option")


if __name__ == "__main__":
    hm = HotelMgnt()
    rooms = []
    count = 0
    opt = 0
    rno = 0
    pname = ""
    while opt != 7:
        print("######## Hotel Management #########")
        print("1. Manage Rooms")
        print("2. Check-In Room")
        print("3. Available Rooms")
        print("4. Search Customer")
        print("5. Check-Out Room")
        print("6. Guest Summary Report")
        print("7. Exit")
        opt = int(input("\nEnter Option: "))

        if opt == 1:
            manageRooms()
        elif opt == 2:
            if count == 0:
                print("\nRooms data is not available.\nPlease add the rooms first.")
                input()
            else:
                hm.checkIn()
        elif opt == 3:
            if count == 0:
                print("\nRooms data is not available.\nPlease add the rooms first.")
                input()
            else:
                hm.getAvailRoom()
        elif opt == 4:
            if count == 0:
                print("\nRooms are not available.\nPlease add the rooms first.")
                input()
            else:
                pname = input("Enter Customer Name: ")
                hm.searchCustomer(pname)
        elif opt == 5:
            if count == 0:
                print("\nRooms are not available.\nPlease add the rooms first.")
                input()
            else:
                rno = int(input("Enter Room Number : "))
                hm.checkOut(rno)
        elif opt == 6:
            hm.guestSummaryReport()
        elif opt == 7:
            print("\nTHANK YOU! FOR USING SOFTWARE")
        else:
            print("\nPlease Enter correct option")
