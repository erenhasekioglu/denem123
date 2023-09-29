meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "ROFL" : "bir şakaya karşılık cevap",
            "SHEESH" : "onaylamamak",
            "CREEPY" : "korkunç",
            "AGGRO" : "agresifleşmek/sinirlenmek"
            }
for i in range(5):
    kelime=input("Kelime:")
    if kelime in meme_dict.keys():
        print(meme_dict[kelime])
    else:
        print("Kelime bulunamadı")