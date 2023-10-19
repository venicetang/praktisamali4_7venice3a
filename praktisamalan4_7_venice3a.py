pi=3.142
def kira_kuboid(tinggi,panjang,lebar):
    isipadu_kuboid=tinggi*panjang*lebar
    return isipadu_kuboid
    
def kuboid(): #isipadu kuboid
    tinggi=int(input("Masukkan tinggi:"))
    panjang=int(input("Masukkan panjang:"))
    lebar=int(input("Masukkan lebar:"))
    print("isipadu_kuboid",kira_kuboid(tinggi,panjang,lebar))
    
def kira_silinder(pi,jejari,tinggi):
    isipadu_silinder=pi*(jejari**2)*(tinggi)
    return isipadu_silinder
    
def silinder():#isipadu silinder
    jejari=int(input("Masukkan jejari"))
    tinggi=int(input("Masukkan tinggi"))
    print("isipadu_silinder",kira_silinder(pi,jejari,tinggi))
    
def kira_kon(pi,jejari,tinggi):
    isipadu_kon=(1/3)*pi*(jejari**2)*(tinggi)
    return isipadu_kon
    
def kon():#isipadu kom
    jejari=float(input("Masukkan jejari:"))
    tinggi=float(input("Masukkan tinggi:"))
    print("isipadu_kon",kira_kon(pi,jejari,tinggi))
    
def kira_sfera(pi,jejari):
    isipadu_sfera=4/3*pi*(jejari**2)
    return isipadu_sfera
    
def sfera():
    jejari=float(input("Masukkan jejari:"))
    print("isipadu_sfera",kira_sfera(pi,jejari))
    
################
#Subatur cara utama
################
ulang=True

while(ulang):
    print(
'''
    #############################
    #   Menu Mengira Isi Padu   #
    #############################
    1.kuboid
    2.silinder
    3.kon
    4.sfera
    5.keluar dari program
''')
    print("")
    
    pilih=int(input("Sila masukkan pilihan anda: "))
    
    if(pilih==1):
        kuboid() #Memanggil fungsi kuboid
    elif(pilih==2):
        silinder()
    elif(pilih==3):
        kon()
    elif(pilih==4):
        sfera()
    elif(pilih==5):
        ulang=False
        print("Bye Bye")
        exit
    else:
        print("Pilihan tiada dalam senarai")
        print("")
