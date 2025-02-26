s = int(input("so giay ban muon nhap:  "))
ngay = s // 86400
gio = (s %86400) // 3600
phut = (s %86400) % 3600 // 60
giay = (s %86400) % 3600 % 60
print(ngay, gio, phut, giay)