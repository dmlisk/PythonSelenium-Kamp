
std = []

# Aldığı isim soy isim ile listeye öğrenci ekleyen

def addStd():

    nameSurname = input("Eklemek istediğiniz öğrencinin adını soyadını giriniz...")
    std.append(nameSurname)

# Listeye birden fazla öğrenci eklemeyi mümkün kılan

def multiAddStd():
    
    cond = True
    while cond == True:
        nameSurname = input("Eklemek istediğiniz öğrencinin adını soyadını giriniz. Çıkmak için 1'e basınız...")
        if nameSurname != "1":
            std.append(nameSurname)
        else:
            cond = False

# Listedeki tüm öğrencileri tek tek ekrana yazdıran

def printStd():

    for i in range(len(std)):
        print (std[i])

#Listeden birden fazla öğrenci silmeyi mümkün kılan

def removeMultiStd():
    cond = True
    while cond == True:
        nameSurname = input("Silmek istediğiniz öğrencinin adını soyadını giriniz. Çıkmak için 1'e basınız...")
        if nameSurname != "1":
            if nameSurname not in std:
                print("Böyle bir öğrenci mevcut değil")
                cond = False
            else:
                std.remove(nameSurname)      
        else:
            cond = False
            
# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan

def stdNumber():
    nameSurname = input("Numarasını Öğrenmek İstediğiniz Öğrencinin Adını Soyadını Giriniz: ")

    if nameSurname in std:
        print(f"Öğrencinin Numarası: {std.index(nameSurname)+1}")
    else:
        print("Böyle bir öğrenci mevcut değil")

# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran

def removeStd():
    nameSurname = input("Silmek İstediğiniz Öğrencinin Adını Soyadını Giriniz: ")

    if nameSurname in std:
        std.remove(nameSurname)
    else:
        print("Böyle bir öğrenci mevcut değil")
