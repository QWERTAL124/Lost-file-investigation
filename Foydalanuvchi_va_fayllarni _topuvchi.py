from winreg import *
import os
import optparse

def korzinka_user(sid):
    try:
        
        kalit = OpenKey(HKEY_LOCAL_MACHINE, "SOFTWARE\Microsoft\Windows NT\CurrentVersion\ProfileList"+'\\'+sid)
        (value,type) = QueryValue(kalit, 'ProfileImagePath')
        user = value.split('\\')[-1]
        return user

    except:
        return sid

def qaytarish(korzinka_joylashuvi):
    user_list = os.listdir(korzinka_joylashuvi)
    for sid in user_list:
        fayllar = os.listdir(korzinka_joylashuvi+sid)
        user_ismi = korzinka_user(sid)
        print("\n\n [*] Foydalanuvchi ismi -==> " + str(user_ismi))
        for fayl in fayllar:
            print(" [#] topilgan fayl: "+str(fayl))
    
def main():
    korzinka_joylashuvi = 'C:\\$Recycle.Bin\\'
    qaytarish(korzinka_joylashuvi)
    

main()
