# Program penggunaan dictionary, program mengubah satu kata yang tedapat diantara kalimat
message = input("masukan kalimat: ")

emoji_mapping = { #<-- dictionary

    ":)" : "😊",
    ";)" : "😉",
    ":(" : "😢",
    ":>" : "🤭"
}

# Split berfungsi untuk memecah string menjadi list pada setiap data yang dimasukan dalam variable message (aku odiv) : ['aku', 'odiv']
words = message.split(" ")

output = " "
for w in words:
    output = output + emoji_mapping.get(w, w) + " "
     # emoji_mapping.get(w, w) berarti program akan mengechek satu-persatu data yang diinput pada variable w (message), jika data yang diinput tidak terdapat pada emoji_mapping maka program akan tetap mencetak data tersebut sambil melakukan perulangan ke data yang lain dan begitu seterusnya sampai program menemukan data yang diinputkan terdapat pada emoji_mapping barulah data tersebut diganti dengan data yang terdapat pada emoji_mapping

print(output)
