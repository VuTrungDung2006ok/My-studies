def check_divisibility_and_unique_digits(p):
    # Kiểm tra xem p chia hết cho 5 hay không
    if p % 5 == 0:
        # Chuyển số p thành chuỗi để kiểm tra các chữ số đôi một khác nhau
        p_str = str(p)
        # Sử dụng set để kiểm tra số lượng chữ số duy nhất
        unique_digits = set(p_str)
        # Nếu số lượng chữ số duy nhất bằng độ dài của chuỗi p_str, tức là các chữ số đôi một khác nhau
        if len(unique_digits) == len(p_str):
            return True
    return False

# Ví dụ sử dụng hàm
p_example = 12342
if check_divisibility_and_unique_digits(p_example):
    print(f"{p_example} chia hết cho 5 và các chữ số đôi một khác nhau.")
else:
    print(f"{p_example} không thỏa mãn điều kiện.")