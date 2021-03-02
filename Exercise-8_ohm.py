username = input("username :")
password = input("password :")
while username != 'admin' and password != '12345' :
    print("wrong password enter the password againe ")
    username = input("username :")
    password = input("password :")
print("Done!")
print("-------------welcome to ohm shop-------------------")
print("1.ขนมเลย์ 20 บาท")
print("2.โคล่า 15 บาท")
print("3.โกโก้ 25 บาท")
print("4.ขนมปัง 30 บาท")
print("---------------------------------------------------")
userselectmenu = int(input("ท่านต้องการสินค้าชิ้นไหนกรอกรหัสสินค้าเลยครับ :"))
if userselectmenu == 1:
    a = int(input("ขนมเลย์ 20 บาท ท่านต้องการกี่ชิ้นครับ :"))
    print("รวมค่าใช้จ่ายทั้งหมด "+str(a*20)+" THB")
elif userselectmenu == 2:
    a = int(input("โคล่า 15 บาท ท่านต้องการกี่ชิ้นครับ :"))
    print("รวมค่าใช้จ่ายทั้งหมด "+str(a*15)+" THB")
elif userselectmenu == 3:
    a = int(input("โกโก้ 25 บาท ท่านต้องการกี่ชิ้นครับ :"))
    print("รวมค่าใช้จ่ายทั้งหมด "+str(a*25)+" THB")
elif userselectmenu == 4:
    a = int(input("ขนมปัง 30 บาท :"))
    print("รวมค่าใช้จ่ายทั้งหมด "+str(a*30)+" THB")
else:
    print("ไม่รหัสสินค้าในรายการครับ")
