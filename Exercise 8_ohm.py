usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "ohm" and passwordInput == "1234":
    print("Login Success")
    print("----- Welcome to ohm Shop -----")
    print("1.ขนมเลย์ 20 THB")
    print("2.โค๊ก 22 THB")
    print("3.กาว 30 THB")
    print("4.โอเลี้ยง 20 THB")
    print("--------------------------------------------------------")
    userSelected = int(input("ท่านลูกค้าต้องการสินค้าหมายเลข >> "))
    if userSelected == 1:
        amout = int(input("คุณต้องการ ขนมเลย์ 20 THB จำนวนกี่ชิ้นครับ >> "))
        print("ราคารวมทั้งหมด คือ "+str(amout*20)+" บาท")
    elif userSelected == 2:
        amout = int(input("คุณต้องการโค๊ก 22 THB จำนวนกี่ชิ้นครับ >> "))
        print("ราคารวมทั้งหมด คือ " + str(amout * 22 ) + " บาท")
    elif userSelected == 3:
        amout = int(input("คุณต้องการกาว 30 THB จำนวนกี่ชิ้นครับ >> "))
        print("ราคารวมทั้งหมด คือ " + str(amout * 30) + " บาท")
    elif userSelected == 4:
        amout = int(input("คูณต้องการโอเลี้ยง 20 THB จำนวนกี่ชิ้นครับ >> "))
        print("ราคารวมทั้งหมด คือ " + str(amout * 20) + " บาท")
    else :
        print("ไม่มีรหัสสินค้าในรายการ")
else:
    print("ท่านยังไม่เป็นสมาชิกของเราครับ")
