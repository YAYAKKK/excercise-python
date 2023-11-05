print("\nPROGRAM INPUT DATA DAFTAR PIKET")
print("="*20)

daftarPiket =[]

while True:
    print("Masukkan Data Piket")
    nama = input("Nama:")
    jadwal = input("Hari:")

    dataPiket = [nama, jadwal]
    daftarPiket.append(dataPiket)

    print('\nDAFTAR PIKET')
    print('='*20)
    for index, daftar in enumerate (daftarPiket):
        print (f"{index +1}{" "}{daftar[0]}{'~'*5}{daftar[1]}")
    
    isnext = input ("\nApakah masih ingin menambahkan? y/n: ")

    if isnext == 'y':
        continue
    elif isnext =='Y':
        continue
    else:
        print("\nTERIMAKASIH TELAH MENGGUNAKAN PROGRAM INI")
        break

    