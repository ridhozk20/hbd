
print("halo selamat datang!")
nama=input("nama kamu siapa? ")

if nama==("uli"):
    print(f"halo {nama} aku program yang dibuat ridho")
else:
    print("boong, aku tau kamu uli\nbtw, aku program yang dibuat ridho")
print("kamu masih inget sama ridho?")


kabar2=input("\nsekarang kabarmu gimana? (baik/ga):")

if kabar2==("baik"):
    print("allhamdulilah kalo baik")
elif kabar2==("ga"):
    print("waduh kenapa? aku doain supaya cepet baik ya")
else:
    print("kok kamu jawab nya beda dari yang kukasih sih")
print(" ")

ultah=input("kamu tanggal 20 kemaren ultah yah?(iya/ga) ")

while ultah != "iya":
    ultah=input("boong mulu, katamu waktu itu ultah loh\njawab yang bener (iya/ga): ")
print(" ")

banyak=int(input("mau diucapin berapa kali? "))
while banyak <= 0:
    banyak=int(input("serius, mau diucapin berapa kali? "))
print(" ")

for i in range(banyak):
    print("HAPPY BIRTHDAY ULI!")

    