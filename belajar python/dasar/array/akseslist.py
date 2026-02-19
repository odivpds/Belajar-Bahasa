#perintah untuk menampilkan list
data_siswa=[[132,133,134],[1,1,3],["putu","made","komang"]]
for x in data_siswa:
    print(x)


data_siswa=[[132,133,134],[1,1,3]]
for x in data_siswa:
    print(x)

#perintah untuk merubah data pada list
data_siswa=[[132, 133, 134],[1, 3], ["Dono", "Kasino", "Indro"]]

print(data_siswa[2][1]) # array ke 2 dan index ke 1

data_siswa[2][1]="Ketut"

print(data_siswa[2][1])