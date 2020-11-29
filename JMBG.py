from tkinter import *
import tkinter as tk
from tkinter import ttk

root = Tk()
root.geometry('600x250')
root.title("JMBG Validator")
root.iconbitmap('C:/Users/Admin/Downloads/icon.ico')

label_Jmbg = Label(root, font=('arial', 12, 'bold'), text="Unesite JMBG:")
label_Jmbg.pack()
entry1 = Entry(root, font=('arial', 13, 'bold'), width=30, bg="#87AF5F", fg="#0000C0", borderwidth=7)
entry1.pack(pady=10)


def check_number_jmbg():
    try:
        global a
        a = entry1.get()

        if len(a) < 13:
            answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Morate uneti 13 cifara!")
            a = int(a)
        elif len(a) == 0:
            answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Niste uneli JMBG!")
            a = int(a)
        elif len(a) > 13:
            answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Morate uneti 13 cifara!")
            a = int(a)
        else:
            answer.config(font=('arial', 10, 'bold'), text="Broj unetih cifara je tačan! Provera...")
    except ValueError:
        answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Niste uneli ispravnu vrednost!")


def check_region():
    try:

        a = entry1.get()

        if len(a) < 13:
            answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Morate uneti 13 cifara!")
            a = int(a)
        elif len(a) == 0:
            answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Niste uneli JMBG!")
            a = int(a)
        elif len(a) > 13:
            answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Morate uneti 13 cifara!")
            a = int(a)
        elif len(a) == 13:

            prva_cifra = int(str(entry1.get())[0])
            druga_cifra = int(str(entry1.get())[1])
            treca_cifra = int(str(entry1.get())[2])
            cetvrta_cifra = int(str(entry1.get())[3])
            peta_cifra = int(str(entry1.get())[4])
            sesta_cifra = int(str(entry1.get())[5])
            sedma_cifra = int(str(entry1.get())[6])
            datum = str('%d%d.%d%d.%d%d%d' %
                        (prva_cifra, druga_cifra, treca_cifra, cetvrta_cifra, peta_cifra, sesta_cifra, sedma_cifra))
            osma_cifra = int(str(entry1.get())[7])
            deveta_cifra = int(str(entry1.get())[8])
            region = str('%d%d' % (osma_cifra, deveta_cifra))

            if prva_cifra not in [0, 1, 2, 3]:
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna prva cifra - nije u opsegu! Mora biti između 0,1,2 i 3")
            elif prva_cifra == 0 and druga_cifra == 0:
                answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Neispravna druga cifra!")
            elif treca_cifra not in [0, 1]:
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna treća cifra - nije u opsegu! Mora biti između 0 i 1")
            elif cetvrta_cifra == 0:
                answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Četvrta cifra ne može biti 0!")
            elif peta_cifra not in [0, 9]:
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna peta cifra - nije u opsegu! Mora biti između 0 ili 9")
            elif peta_cifra == 0 and int('%d%d' % (sesta_cifra, sedma_cifra)) in range(21, 99, 1):
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna šesta i sedma cifra - nisu u opsegu! [Do 020] ")
            elif peta_cifra != 9 and peta_cifra != 0:
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna peta cifra - nije u opsegu! [0 ili 1]")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 1:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Stranac u BiH")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 2:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Stranc u Crnoj Gori")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 3:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Stranc u Hrvatskoj")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 4:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Stranc u Makedoniji")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 5:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Stranc u Sloveniji")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 5:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Stranc u Sloveniji")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 7:
                answer.config(font=('arial', 10, 'bold'),
                              text="Region rođenja ili prebivališta: Stranc u Srbiji(bez pokrajina)")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 8:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Stranc u Vojvodini")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 9:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Stranc na KiM")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 10:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Banja Luka")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 11:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Bihać")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 12:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Doboj")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 13:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Goražde")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 14:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Livno")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 15:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Mostar")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 16:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Prijedor")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 17:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Sarajevo")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 18:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Tuzla")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 19:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Zenica")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 20:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Ne koristi se!")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 21:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Podgorica")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) in range(21, 26, 1):
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Crna Gora")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 26:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Nikšić")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) in range(26, 29, 1):
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Crna Gora")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 29:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Pljevlja")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 29:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Pljevlja")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 30:
                answer.config(font=('arial', 10, 'bold'),
                              text="Region rođenja ili prebivališta: Osijek, Slavonija regija")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 31:
                answer.config(font=('arial', 10, 'bold'),
                              text="Region rođenja ili prebivališta: Bjelovar, Virovitica, Koprivnica, Pakrac, Podravina regija")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 32:
                answer.config(font=('arial', 10, 'bold'),
                              text="Region rođenja ili prebivališta: Varaždin, Međimurje regija")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 33:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Zagreb")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 34:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Karlovac")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 35:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Gospić, Lika regija")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 36:
                answer.config(font=('arial', 10, 'bold'),
                              text="Region rođenja ili prebivališta: Rijeka, Pula, Istra i Primorje regija")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 37:
                answer.config(font=('arial', 10, 'bold'),
                              text="Region rođenja ili prebivališta: Sisak, Banovina regija")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 38:
                answer.config(font=('arial', 10, 'bold'),
                              text="Region rođenja ili prebivališta: Split, Zadar, Dubrovnik, Dalmacija regija")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 39:
                answer.config(font=('arial', 10, 'bold'),
                              text="Region rođenja ili prebivališta: Ostala mesta u Hrvatskoj")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 40:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Ne koristi se!")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 41:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Bitolj")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 42:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Kumanovo")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 43:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Ohrid")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 44:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Prilep")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 45:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Skoplje")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 46:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Strumica")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 47:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Tetovo")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 48:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Veles")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 49:
                answer.config(font=('arial', 10, 'bold'),
                              text="Region rođenja ili prebivališta: Region rođenja ili prebivališta: Štip")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 50:
                answer.config(font=('arial', 10, 'bold'),
                              text="Region rođenja ili prebivališta: Slovenija (za celu Sloveniju se koristi)")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) in range(51, 59, 1):
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Ne koristi se!")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) in range(60, 69, 1):
                answer.config(font=('arial', 10, 'bold'),
                              text="Region rođenja ili prebivališta: Građanin sa privremenim boravkom!")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 70:
                answer.config(font=('arial', 10, 'bold'),
                              text="Region rođenja ili prebivališta: Građanin upisan u MKR DKP Republike Srbije (po čl. 4 Zakona o JMBG)")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 71:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Beograd")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 72:
                answer.config(font=('arial', 10, 'bold'),
                              text="Region rođenja ili prebivališta: Kragujevac ili Jagodina")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 73:
                answer.config(font=('arial', 10, 'bold'),
                              text="Region rođenja ili prebivališta: Niš ili Pirot ili Toplica")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 74:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Leskovac ili Vranje")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 75:
                answer3.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Zaječar ili Bor")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 76:
                answer.config(font=('arial', 10, 'bold'),
                              text="Region rođenja ili prebivališta: Smederevo ili Požarevac")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 77:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Mačva ili Kolubara")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 78:
                answer.config(font=('arial', 10, 'bold'),
                              text="Region rođenja ili prebivališta: Čačak ili Kraljevo ili Kruševac")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 79:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Užice")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 80:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Novi Sad")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 81:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Sombor")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 82:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Subotica")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 83:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Vrbas")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 84:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Kikinda")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 85:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Zrenjanin")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 86:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Pančevo")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 87:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Vršac")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 88:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Ruma")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 89:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Sremska Mitrovica")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 90:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Ne koristi se!")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 91:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Priština")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 92:
                answer.config(font=('arial', 10, 'bold'), text="Kosovska Mitrovica")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 93:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Peć")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 94:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Đakovica")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 95:
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Prizren")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) == 96:
                answer.config(font=('arial', 10, 'bold'),
                              text="Region rođenja ili prebivališta: Gnjilane ili Kosovska Kamenica ili Vitine ili Novo Brdo")
            elif int('%d%d' % (osma_cifra, deveta_cifra)) in range(97, 99, 1):
                answer.config(font=('arial', 10, 'bold'), text="Region rođenja ili prebivališta: Nije u upotrebi!")
            else:
                answer.config(font=('arial', 10, 'bold'), text="Nepostojeći region!")
        else:
            answer.config(font=('arial', 10, 'bold'), text="Nepostojeći region!")
    except ValueError:
        answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Niste uneli brojnu vrednost!")


def check_pol():
    try:

        a = entry1.get()

        if len(a) < 13:
            answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Morate uneti 13 cifara!")
            a = int(a)
        elif len(a) == 0:
            answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Niste uneli JMBG!")
            a = int(a)
        elif len(a) > 13:
            answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Morate uneti 13 cifara!")
            a = int(a)
        elif len(a) == 13:
            prva_cifra = int(str(entry1.get())[0])
            druga_cifra = int(str(entry1.get())[1])
            treca_cifra = int(str(entry1.get())[2])
            cetvrta_cifra = int(str(entry1.get())[3])
            peta_cifra = int(str(entry1.get())[4])
            sesta_cifra = int(str(entry1.get())[5])
            sedma_cifra = int(str(entry1.get())[6])
            cif10_pol = int(str(entry1.get())[9])
            cif11_pol = int(str(entry1.get())[10])
            cif12_pol = int(str(entry1.get())[11])
            if prva_cifra not in [0, 1, 2, 3]:
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna prva cifra - nije u opsegu! Mora biti između 0,1,2 i 3")
            elif prva_cifra == 0 and druga_cifra == 0:
                answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Neispravna druga cifra!")
            elif treca_cifra not in [0, 1]:
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna treća cifra - nije u opsegu! Mora biti između 0 i 1")
            elif cetvrta_cifra == 0:
                answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Četvrta cifra ne može biti 0!")
            elif peta_cifra not in [0, 9]:
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna peta cifra - nije u opsegu! Mora biti između 0 ili 9")
            elif peta_cifra == 0 and int('%d%d' % (sesta_cifra, sedma_cifra)) in range(21, 99, 1):
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna šesta i sedma cifra - nisu u opsegu! [Do 020] ")
            elif peta_cifra != 9 and peta_cifra != 0:
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna peta cifra - nije u opsegu! [0 ili 1]")
            elif int('%d%d%d' % (cif10_pol, cif11_pol, cif12_pol)) in range(0, 499, 1):
                answer.config(font=('arial', 10, 'bold'), text="Pol: Muški")
            else:
                answer.config(font=('arial', 10, 'bold'), text="Pol: Ženski")
        else:
            answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Niste uneli ispravnu vrednost!")

    except ValueError:
        answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Niste uneli ispravnu vrednost!")


def datum():
    try:
        a = entry1.get()
        if len(a) < 13:
            answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Morate uneti 13 cifara!")
            a = int(a)
        elif len(a) == 0:
            answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Niste uneli JMBG!")
            a = int(a)
        elif len(a) > 13:
            answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Morate uneti 13 cifara!")
            a = int(a)
        elif len(a) == 13:

            prva_cifra = int(str(entry1.get())[0])
            druga_cifra = int(str(entry1.get())[1])
            treca_cifra = int(str(entry1.get())[2])
            cetvrta_cifra = int(str(entry1.get())[3])
            peta_cifra = int(str(entry1.get())[4])
            sesta_cifra = int(str(entry1.get())[5])
            sedma_cifra = int(str(entry1.get())[6])
            datum = str('%d%d.%d%d.%d%d%d' %
                        (prva_cifra, druga_cifra, treca_cifra, cetvrta_cifra, peta_cifra, sesta_cifra, sedma_cifra))

            if prva_cifra not in [0, 1, 2, 3]:
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna prva cifra - nije u opsegu! Mora biti između 0,1,2 i 3")
            elif treca_cifra not in [0, 1]:
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna treća cifra - nije u opsegu! Mora biti između 0 i 1")
            elif cetvrta_cifra == 0:
                answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Četvrta cifra ne može biti 0!")
            elif peta_cifra not in [0, 9]:
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna peta cifra - nije u opsegu! Mora biti između 0 ili 9")
            elif peta_cifra == 0 and int('%d%d' % (sesta_cifra, sedma_cifra)) in range(21, 99, 1):
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna šesta i sedma cifra - nisu u opsegu! [Do 020] ")
            elif peta_cifra != 9 and peta_cifra != 0:
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna peta cifra - nije u opsegu! [0 ili 1]")
            elif prva_cifra == 0 and druga_cifra == 0:
                answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Neispravna druga cifra!")
            else:
                answer.config(font=('arial', 10, 'bold'), text="Datum vašeg rođenja je:" + " " + datum + "\n")
        else:
            datum = str('%d%d.%d%d.%d%d%d' %
                        (prva_cifra, druga_cifra, treca_cifra, cetvrta_cifra, peta_cifra, sesta_cifra, sedma_cifra))
            answer.config(font=('arial', 10, 'bold'), text="Datum vašeg rođenja je:" + " " + datum + "\n")
    except ValueError:
        answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Niste uneli brojnu vrednost!")


def kontrolna_cifra():
    try:
        a = entry1.get()

        if len(a) < 13:
            answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Morate uneti 13 cifara!")
            a = int(a)
        elif len(a) == 0:
            answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Niste uneli JMBG!")
            a = int(a)
        elif len(a) > 13:
            answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Morate uneti 13 cifara!")
            a = int(a)
        elif len(a) == 13:

            prva_cifra = int(str(entry1.get())[0])
            druga_cifra = int(str(entry1.get())[1])
            treca_cifra = int(str(entry1.get())[2])
            cetvrta_cifra = int(str(entry1.get())[3])
            peta_cifra = int(str(entry1.get())[4])
            sesta_cifra = int(str(entry1.get())[5])
            sedma_cifra = int(str(entry1.get())[6])
            osma_cifra = int(str(entry1.get())[7])
            deveta_cifra = int(str(entry1.get())[8])
            cif10_pol = int(str(entry1.get())[9])
            cif11_pol = int(str(entry1.get())[10])
            cif12_pol = int(str(entry1.get())[11])
            cif13_pol = int(str(entry1.get()[12]))
            pol = str('%d%d%d' % (cif10_pol, cif11_pol, cif12_pol))
            suma = int(7 * prva_cifra + 6 * druga_cifra + 5 * treca_cifra + 4 * cetvrta_cifra + 3 * peta_cifra +
                       2 * sesta_cifra + 7 * sedma_cifra + 6 * osma_cifra + 5 * deveta_cifra + 4 * cif10_pol + 3 * cif11_pol + 2 * cif12_pol)
            kontrolna_cifra = suma % 11

            if prva_cifra not in [0, 1, 2, 3]:
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna prva cifra - nije u opsegu! Mora biti između 0,1,2 i 3")
            elif prva_cifra == 0 and druga_cifra == 0:
                answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Neispravna druga cifra!")
            elif treca_cifra not in [0, 1, 2]:
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna treća cifra - nije u opsegu! Mora biti između 0 i 1")
            elif cetvrta_cifra == 0:
                answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Četvrta cifra ne može biti 0!")
            elif peta_cifra not in [0, 9]:
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna peta cifra - nije u opsegu! Mora biti između 0 ili 9")
            elif peta_cifra == 0 and int('%d%d' % (sesta_cifra, sedma_cifra)) in range(21, 99, 1):
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna šesta i sedma cifra - nisu u opsegu! [Do 020] ")
            elif peta_cifra != 9 and peta_cifra != 0:
                answer.config(font=('arial', 10, 'bold'),
                              text="JMBG nije validan! Neispravna peta cifra - nije u opsegu! [0 ili 1]")
            elif kontrolna_cifra % 11 == 0:
                answer.config(font=('arial', 10, 'bold'), text="Kontrolna cifra je 0")
            elif kontrolna_cifra % 11 > 1:
                kontrolna_cifra = 11 - kontrolna_cifra % 11
                answer.config(font=('arial', 10, 'bold'), text="Kontrolna cifra je: " + str(kontrolna_cifra))
            elif kontrolna_cifra % 11 == 0:
                kontrolna_cifra = 0
                answer.config(font=('arial', 10, 'bold'), text="Kontrolna cifra je: " + str(kontrolna_cifra))
            elif kontrolna_cifra % 11 == 1:
                for p in pol:
                    if pol in range(0, 499, 1):
                        pol = int(pol) + 1
                        answer.config(font=('arial', 10, 'bold'),
                                      text="JMBG je pogrešan, uvećava se cifra pola za 1. Sada je: " + str(pol))
                    else:
                        pol = int(pol) + 1
                        answer.config(font=('arial', 10, 'bold'),
                                      text="JMBG je pogrešan, uvećava se cifra pola za 1. Sada je:" + str(pol))
            else:
                answer.config(font=('arial', 10, 'bold'), text="Nije ispravna kontrolna cifra !")
        else:
            answer.config(font=('arial', 10, 'bold'), text="Nije ispravna kontrolna cifra !")
    except ValueError:
        answer.config(font=('arial', 10, 'bold'), text="JMBG nije validan! Niste uneli brojnu vrednost!")


answer = Label(root, text=' ')
answer.pack(pady=20)


def main():
    check_number_jmbg()
    datum()
    check_pol()
    kontrolna_cifra()


def provera_datuma():
    check_number_jmbg()
    datum()


def provera_regiona():
    check_number_jmbg()
    datum()
    check_region()


def provera_cifre():
    check_number_jmbg()
    kontrolna_cifra()


# button_validan_jmbg = Button(root, font=('arial', 10, 'bold'),text="Validiraj JMBG",bg="lime",command=main).place(x=190,y=200)#.pack()
# button_validan_jmbg.pack(side=LEFT, padx=35,pady=30)

button_validan_jmbg = Button(root, font=('arial', 10, 'bold'), text="Datum", bg="gold",
                             command=datum)  # .place(x=190,y=200)#.pack()
button_validan_jmbg.pack(side=LEFT, padx=20, pady=15)

button_validan_jmbg = Button(root, font=('arial', 10, 'bold'), text="Region", bg="gold",
                             command=provera_regiona)  # .place(x=190,y=200)#.pack()
button_validan_jmbg.pack(side=LEFT, padx=25, pady=20)

button_validan_jmbg = Button(root, font=('arial', 10, 'bold'), text="Pol", bg="gold",
                             command=check_pol)  # lambda: [check_number_jmbg(),kontrolna_cifra()])#.place(x=190,y=200)#.pack()
button_validan_jmbg.pack(side=LEFT, padx=20, pady=15)

button_validan_jmbg = Button(root, font=('arial', 10, 'bold'), text="Kontrolna Cifra", bg="gold",
                             command=kontrolna_cifra)  # .place(x=190,y=200)#.pack()
button_validan_jmbg.pack(side=LEFT, padx=30, pady=25)

button_exit = Button(root, font=('arial', 10, 'bold'), text="Zatvori", bg="#C00000",
                     command=root.quit)  # .place(x=170,y=170)
button_exit.pack(side=RIGHT, padx=40, pady=30)

root.mainloop()

