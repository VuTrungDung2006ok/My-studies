#https://youtu.be/tb6EYiHtcXU?list=PLZPZq0r_RZOOkUQbat8LyQii36cJf2SWT
#name = input()


#kq = len(name) === dung ==> 4
#kq = name.find("g") ===> Tìm vị trí của chữ cái sẽ return -1 nếu ko có
#kq = name.rfind("g") ==> tim vi tri cua chữ cái ở dòng cuối cùng có thể, sẽ return -1 nếu ko có\
#kq = name.capitalize() ===> Viết hoa chữ cái đầu tiên
#kq = name.upper() ===> viết hoa full chữ
#kq = name.lower() ==> viết thường full chữ
#kq = name.isdigit() ===> Check có phải là dãy số không, lưu ý là chỉ có mỗi số trong đoạn input(kể cả dấu cách)
#kq = name.isalpha() ===> Check có phải là full chữ không, lưu ý là chỉ có mỗi chữ trong đoạn input( kể cả dấu cách)

#number = input()
#kq = number.count("-") ==> đếm kí tự mình muốn 
#kq = number.replace("-","dog") ===> thay thế kí tự mình muốn

 
#print(kq)

#username is no more than 12 chữ
#username= input()
#if len(username) >= 12:
    #print("Your name is to long")

#username is no cotain space
#username = input()
#if username.find(" ") >=1:
    #print("Bro fk you")
#else:
    #print("Congrat")
#username is no cotain digits
username = input()
if username.isalpha():
    print("good job")
else:
    print("bro FK you") 

