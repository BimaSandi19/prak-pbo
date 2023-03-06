username = ("informatika")
password = ("12345678")

i = 1

while(i <= 3):
    inUser = input("masukkan username : ")
    inPassword = input("maskukkan password : ")

    if(inUser == username and inPassword == password):
        print("Berhasil login")
        break
    elif(i == 3):
        print("Akun diblokir")
        break
    else:
        print("Username dan password salah silahkan coba lagi")
        i += 1