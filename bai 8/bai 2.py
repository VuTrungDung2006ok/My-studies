n = int(input("Nhập số lượng phần tử của dãy số: "))

# Đọc các phần tử của dãy số
print("Nhập các phần tử của dãy số:")
a = list(map(int, input().split()))

# Biến đổi các thành phần trong danh sách a
for i in range(len(a)):
    # Thực hiện phép biến đổi mong muốn ở đây, ví dụ nhân mỗi phần tử với 2
    a[i] *= 2

# In ra danh sách đã được biến đổi
print("Dãy số sau khi biến đổi:", a)