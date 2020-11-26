from tkinter import *

root = Tk()
root.geometry('500x200')
root.title("JMBG Validator")
root.iconbitmap('C:/Users/Admin/Downloads/icon.ico')



def button_command():
	msg = "JMBG koji ste uneli je: " + entry1.get()
	text = Label(root, text=msg) #entry1.get()
	text.pack()
	entry1.delete(0, END)
	#print(text)
	#return None

#def button_command_pol():
#	text = "Ovde ce se prikazati pol"
#	entry2.insert(0, text)
#	return None
label_Jmbg = Label(root, text= "Unesite JMBG:")
label_Jmbg.pack()
entry1 = Entry(root, width = 30, bg="#87AF5F", fg="#0000C0", borderwidth=7)
entry1.pack(pady=10)
#entry1.insert(0, "Unesite JMBG: ")

def check_number_jmbg():
	try:
		a = entry1.get()
		prva_cifra = int(str(entry1.get())[0])
		druga_cifra = int(str(entry1.get())[1])
		treca_cifra = int(str(entry1.get())[2])
		peta_cifra = int(str(entry1.get())[4])
		sesta_cifra = int(str(entry1.get())[5])
		sedma_cifra = int(str(entry1.get())[6])
		cif1_pol = int(str(entry1.get())[9])
		cif2_pol = int(str(entry1.get())[10])
		cif3_pol = int(str(entry1.get())[11])
		radi = str('%d%d' % (prva_cifra, druga_cifra))

		if len(a) < 13:
			answer.config(text="Error. Morate uneti 13 cifara!")
			a = int(a)
		elif len(a) > 13:
			answer.config(text="Error. Morate uneti 13 cifara!")
			a = int(a)
		elif prva_cifra not in [0,1,2,3]:
			answer.config(text="Neispravna prva cifra - nije u opsegu! Mora biti između 0,1,2 i 3")
			prva_cifra = int(prva_cifra)
		elif treca_cifra not in [0,1,2]:
		    answer.config(text="Neispravna treća cifra - nije u opsegu! Mora biti između 0 i 1")
		    treca_cifra = int(treca_cifra)
		elif peta_cifra not in [0,9]:
			answer.config(text="Neispravna peta cifra - nije u opsegu! Mora biti između 0 ili 9")
			peta_cifra = int(peta_cifra)
		elif peta_cifra == 0 and int('%d%d' % (sesta_cifra, sedma_cifra)) in range(21,99,1):
			 answer.config(text="Neispravna šesta i sedma cifra - nisu u opsegu! [Do 020] ")
			 peta_cifra = int(peta_cifra)
			 sesta_cifra = int(sesta_cifra)
			 sedma_cifra = int(sedma_cifra)
		else:
			#date.config(text="Dan vaseg rodjenja:" + prva_cifra & druga_cifra + "je:")
			answer.config(text="Validan JMBG \n Dan vaseg rodjenja:" + radi + "je:")
			prva_cifra = int(prva_cifra)
			druga_cifra = int(druga_cifra)
	except ValueError:
		answer.config(text="Niste uneli brojnu vrednost!")

answer = Label(root, text=' ')
answer.pack(pady=20)

#date = Label(root, text=' ')
#date.pack(pady=20)
#entry2 = Entry(root, width = 30, bg="#87AF5F", fg="#0000C0", borderwidth=7)
#entry2.pack()

Button(root, text="Validiraj JMBG", command=check_number_jmbg).pack()

#Button(root, text="Prikaži pol", command=button_command_pol).pack()



button_exit = Button(root, text="Zatvori", bg="#C00000", command=root.quit) #.place(x=170,y=170)
button_exit.pack()
