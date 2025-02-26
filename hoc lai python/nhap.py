a = input("""Câu 1: bạn là 
A: nam
B: nữ
Đáp án của bạn là: """)

b = input("""Câu 2: chiều cao và trọng lượng của bạn:
A: Bạn khá nhẹ
B: Bạn có thân hình trung bình và khỏe khắn
C: Bạn có thân hình tương đối cao lớn
Đáp án của bạn là: """)

c = input("""Câu 3: Bạn thích làm tâm điểm của sân khấu ?
A: Mình thích được tỏa sáng và thoái mái với việc đó
B: Mình thoải mái nhưng không cần thiết phải là tâm điểm
C: Mình thích đóng vai trò hỗ trợ hơn
Đáp án của bạn là: """)

d = input("""Câu 4: Điểm mạnh về thể chất của bạn:
A: Mình rất dẻo dai và có thể nhào lộn
B: Mình khỏe và nâng đỡ tốt
C: Mình có phản xạ tốt và linh hoạt
Đáp án của bạn là: """ )

n =[]
n.append(a)
n.append(b)
n.append(c)
n.append(d)

if n[0] == 'a':
    if (n[1] == 'b' or n[1] == 'c') and (n[2] == 'a' or n[2] == 'b') and (n[3] == 'a' or n[3] == 'b'):
        print("bạn là BASE") 
    else:
        print("bạn là BACK")

elif n[0] == 'b':
    if (n[1] == 'a' or n[1] == 'b') and (n[2] == 'a' or n[2]=='b') and (n[3] == 'a' or n[3] == 'c'):
        print("bạn là FLYER")
    elif n[1] == 'c' and n[2] == 'a' and n[3] == 'a':
        print("bạn là FLYER")
    else:
        print("bạn là BACK")


            


