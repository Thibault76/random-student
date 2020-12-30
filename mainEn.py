# Ce programme a été réalisé par Thibault MAGNIER, en classe de 2nd 2

from tkinter.filedialog import *
import os
import random
from tkinter.messagebox import *


class Screen:
    def __init__(self, canva, frame_0, frame_1, frame_2, frame_3):
        self.canvas = canva
        self.filepath = ""
        self.student_list = []
        self.student_list2 = []
        self.var_supp = IntVar()
        self.label_0 = Label(width=25)
        self.police = "Georgia"
        self.fontTitre = "Pacifico"
        self.mod_file = ""
        self.initialFile = r"classe"

        # page menu
        self.copyright = Label(text=texte[langue][23], font=(self.police, 10), bg='white').pack(side=BOTTOM, pady=15)
        self.titre_menu = Label(frame_3, text=texte[langue][0], font=(self.fontTitre, 50), bg='white')
        self.bt_chs_classe = Button(frame_2, text=texte[langue][1], font=(self.police, 20), borderwidth=1,
                                    command=self.random_student)

        # bt_aide = Button(frame_2, text='Aide', font=(self.police, 20), borderwidth=1)
        self.bt_option = Button(frame_2, text=texte[langue][11], font=(self.police, 20), borderwidth=1, command=self.option)
        self.bt_quit = Button(frame_2, text=texte[langue][3], font=(self.police, 20), borderwidth=1, command=window.quit)
        self.frame_0 = frame_0
        self.frame_1 = frame_1
        self.frame_2 = frame_2
        self.frame_3 = frame_3

        # page option
        self.frame_0_opt = Frame(window, bg='white')
        self.frame_1_opt = Frame(self.frame_0_opt, bg="white")
        self.titre_H1_opt = Label(self.frame_0_opt, text=texte[langue][0], font=(self.fontTitre, 50), bg='white')
        self.titre_H2_opt = Label(self.frame_0_opt, text=texte[langue][11], font=(self.police, 25), bg='white')
        self.bt_choisi_classe_opt = Button(self.frame_1_opt, text=texte[langue][12], font=(self.police, 20), borderwidth=1,
                                           command=self.class_edit)
        self.bt_creer_classe_opt = Button(self.frame_1_opt, text=texte[langue][13], font=(self.police, 20), borderwidth=1,
                                          command=self.new_class)
        self.bt_menu_opt = Button(self.frame_1_opt, text=texte[langue][14], font=(self.police, 20), borderwidth=1,
                                  command=self.menu)

        # page random student
        self.menubar = Menu(window)
        menu1 = Menu(self.menubar, tearoff=0)
        menu1.add_command(label=texte[langue][7], command=self.changer_classe)
        menu1.add_separator()
        menu1.add_command(label=texte[langue][3], command=window.quit)
        self.menubar.add_cascade(label=texte[langue][6], menu=menu1)
        self.frame0_rdst = Frame(window, bg='white')
        self.frame1_rdst = Frame(self.frame0_rdst, bg='white')
        self.frame2_rdst = Frame(self.frame0_rdst, bg='white')
        self.tk_student_list = Listbox(self.frame1_rdst, font=(self.police, 15), bg='white')
        self.bouton = Button(self.frame2_rdst, text=texte[langue][8], font=(self.police, 15),
                             command=self.choice_random_student)
        self.bouton_ch_class = Button(self.frame2_rdst, text=texte[langue][7], font=(self.police, 15),
                                      command=self.changer_classe)
        self.remise_a_zero = Button(self.frame1_rdst, text=texte[langue][10], font=(self.police, 15),
                                    command=self.remise_a_zero_classe)
        self.titre = Label(self.frame0_rdst, text=texte[langue][0], font=(self.fontTitre, 50), bg='white')
        self.label_0 = Label(self.frame2_rdst, text="", font=(self.police, 15), bg='white')
        self.check_supp = Checkbutton(self.frame1_rdst, text=texte[langue][5], font=(self.police, 15),
                                      variable=self.var_supp, bg='white')
        self.bt_retour_rdst = Button(self.frame2_rdst, text=texte[langue][14], font=(self.police, 15),
                                     command=self.menu)

        # class edit
        self.frame_0_class_edit = Frame(window, bg="white")
        self.frame_1_class_edit = Frame(self.frame_0_class_edit, bg="white")
        self.frame_2_class_edit = Frame(self.frame_0_class_edit, bg="white")
        self.text_box_class_edit = Text(self.frame_1_class_edit, bg="white", insertborderwidth=2, height=28, width=25,
                                        font=(self.police, 12))
        self.button_0_class_edit = Button(self.frame_2_class_edit, text=texte[langue][14], font=(self.police, 20),
                                          borderwidth=1, command=self.menu)
        self.button_1_class_edit = Button(self.frame_2_class_edit, text=texte[langue][15], font=(self.police, 20),
                                          borderwidth=1, command=self.save)
        self.label_0_class_edit = Label(self.frame_1_class_edit, text=texte[langue][16], font=(self.police, 15),
                                        borderwidth=1, bg="white")

        # new class
        self.frame_0_new_class = Frame(window, bg="white")
        self.frame_1_new_class = Frame(self.frame_0_new_class, bg="white")
        self.frame_2_new_class = Frame(self.frame_0_new_class, bg="white")
        self.text_box_new_class = Text(self.frame_1_new_class, bg="white", insertborderwidth=2, height=28, width=25,
                                       font=(self.police, 12))
        self.button_0_new_class = Button(self.frame_2_new_class, text=texte[langue][14], font=(self.police, 20),
                                         borderwidth=1, command=self.menu)
        self.button_1_new_class = Button(self.frame_2_new_class, text=texte[langue][20], font=(self.police, 20),
                                         borderwidth=1, command=self.save_as)
        self.label_0_new_class = Label(self.frame_1_new_class, text=texte[langue][16], font=(self.police, 15),
                                       borderwidth=1, bg="white")
        self.get_name_of_class = StringVar
        self.className_0_new_class = Entry(self.frame_2_new_class, font=(self.police, 15), borderwidth=1, bg="white")

    def class_edit(self):
        self.mod_file = askopenfilename(title=texte[langue][2], filetypes=[('text files', '.txt'), ('all files', '.*')],
                                        initialdir=self.initialFile)
        class_text = ""

        if self.mod_file != "":
            self.close_menu()
            self.close_option()
            self.close_rd()
            self.close_new_class()

            if os.path.exists(self.mod_file):
                with open(self.mod_file, "r+") as file:
                    file_text = file.readlines()
                    for i in file_text:
                        class_text = class_text + i
            else:
                class_text = "ERREUR de chargement de la classe"

            self.text_box_class_edit.delete('1.0', 'end')
            self.text_box_class_edit.insert('1.0', class_text)

            self.text_box_class_edit.grid(row=1)
            self.label_0_class_edit.grid(row=0, pady=15)
            self.button_1_class_edit.pack(padx=20, pady=20)
            self.button_0_class_edit.pack(padx=20)
            self.frame_2_class_edit.pack(side=RIGHT)
            self.frame_1_class_edit.pack(side=LEFT)
            self.frame_0_class_edit.pack(expand=YES)

    def close_class_edit(self):
        self.frame_0_class_edit.pack_forget()
        self.frame_1_class_edit.pack_forget()
        self.frame_2_class_edit.pack_forget()
        self.text_box_class_edit.pack_forget()
        self.button_0_class_edit.pack_forget()
        self.button_1_class_edit.pack_forget()
        self.label_0_class_edit.pack_forget()

    def save(self):
        if os.path.exists(self.mod_file) and alerte.save_new_class(True):
            text = self.text_box_class_edit.get('1.0', 'end')
            file = open(self.mod_file, "w+")
            file.write(text)
            file.close()

    def new_class(self):
        self.close_menu()
        self.close_option()
        self.close_rd()
        self.close_class_edit()

        self.className_0_new_class.delete(0, END)
        self.className_0_new_class.insert(0, texte[langue][21])

        self.text_box_new_class.delete('1.0', 'end')

        self.label_0_new_class.grid(row=0, pady=15)
        self.text_box_new_class.grid(row=1)
        self.className_0_new_class.grid(padx=20, row=0)
        self.button_1_new_class.grid(padx=20, pady=20, row=1)
        self.button_0_new_class.grid(padx=20, row=2)
        self.frame_2_new_class.pack(side=RIGHT)
        self.frame_1_new_class.pack(side=LEFT)
        self.frame_0_new_class.pack(expand=YES)

    def save_as(self):
        if alerte.save_new_class(False):
            text = self.text_box_new_class.get('1.0', 'end')
            name = self.className_0_new_class.get()
            if os.path.exists(r"classe\%s.txt" % name):
                alerte.file_exist()
            else:
                file = open(r'classe\%s.txt' % name, 'w')
                file.write(text)
                file.close()

    def close_new_class(self):
        self.text_box_new_class.pack_forget()
        self.label_0_new_class.pack_forget()
        self.className_0_new_class.pack_forget()
        self.button_1_new_class.pack_forget()
        self.button_0_new_class.pack_forget()
        self.frame_2_new_class.pack_forget()
        self.frame_1_new_class.pack_forget()
        self.frame_0_new_class.pack_forget()

    def option(self):
        self.close_menu()
        self.close_rd()
        self.close_class_edit()
        self.close_new_class()

        self.titre_H1_opt.grid(row=0)
        self.titre_H2_opt.grid(row=1, pady=15)
        self.bt_choisi_classe_opt.grid(row=0, column=0)
        self.bt_creer_classe_opt.grid(row=1, pady=10)
        self.bt_menu_opt.grid(row=2, pady=20)
        self.frame_1_opt.grid(row=2)
        self.frame_0_opt.pack(expand=YES)

    def close_option(self):
        self.titre_H2_opt.pack_forget()
        self.titre_H1_opt.pack_forget()
        self.bt_choisi_classe_opt.pack_forget()
        self.bt_creer_classe_opt.pack_forget()
        self.bt_menu_opt.pack_forget()
        self.frame_1_opt.pack_forget()
        self.frame_0_opt.pack_forget()

    def menu(self):
        self.close_option()
        self.close_rd()
        self.close_class_edit()
        self.close_new_class()

        self.titre_menu.pack(pady=30)
        self.canvas.pack(pady=40)
        self.bt_chs_classe.grid(row=0, column=0)
        # bt_aide.grid(row=1, column=0, pady=7)
        self.bt_option.grid(row=2, column=0, pady=7)
        self.bt_quit.grid(row=3, column=0, pady=10)
        self.frame_2.pack(side=BOTTOM)
        self.frame_1.grid(row=1)
        self.frame_3.grid(row=0)
        self.frame_0.pack(expand=YES)

    def close_menu(self):
        self.canvas.pack_forget()
        self.titre.pack_forget()
        self.bt_chs_classe.pack_forget()
        # bt_aide.pack_forget()
        self.bt_option.pack_forget()
        self.bt_quit.pack_forget()
        self.frame_2.pack_forget()
        self.frame_1.pack_forget()
        self.frame_3.pack_forget()
        self.frame_0.pack_forget()

    def random_student(self):
        self.filepath = askopenfilename(title=texte[langue][2], filetypes=[('text files', '.txt'), ('all files', '.*')],
                                        initialdir=self.initialFile)

        if self.filepath != "":
            self.close_menu()
            self.close_option()
            self.close_class_edit()
            self.close_new_class()
            window.config(menu=self.menubar)

            self.remise_a_zero_classe()

            # pack
            self.tk_student_list.grid(row=0, column=0)
            self.check_supp.grid(row=1, column=0, pady=10)
            self.bouton.grid(row=0)
            self.bouton_ch_class.grid(row=1, pady=15)
            self.label_0.grid(row=2, pady=25)
            self.titre.pack(side=TOP, pady=25)
            self.remise_a_zero.grid(row=2)
            self.bt_retour_rdst.grid(row=3)
            self.frame1_rdst.pack(side=LEFT)
            self.frame2_rdst.pack(side=RIGHT, padx=30)
            self.frame0_rdst.pack(expand=YES)

    def close_rd(self):
        self.tk_student_list.pack_forget()
        self.check_supp.pack_forget()
        self.bouton.pack_forget()
        self.bouton_ch_class.pack_forget()
        self.label_0.pack_forget()
        self.titre.pack_forget()
        self.remise_a_zero.pack_forget()
        self.bt_retour_rdst.pack_forget()
        self.frame1_rdst.pack_forget()
        self.frame2_rdst.pack_forget()
        self.frame0_rdst.pack_forget()
        window.config(menu="")

    def choice_random_student(self):
        y = len(self.student_list)
        if y > 0:
            x = random.randint(0, y - 1)
            student_choice = self.student_list[x]
            if self.var_supp.get() == 1:
                del self.student_list[x]
            self.tk_student_list.delete(0, END)
            x = 0
            for i in self.student_list:
                self.tk_student_list.insert(x, i)
                x += 1
            self.label_0['text'] = texte[langue][4] % student_choice
        else:
            self.remise_a_zero_classe()

    def changer_classe(self):
        self.filepath = askopenfilename(title=texte[langue][1], filetypes=[('text files', '.txt'), ('all files', '.*')],
                                        initialdir=self.initialFile)
        self.tk_student_list.delete(0, END)
        if os.path.exists(self.filepath):
            with open(self.filepath, "r+") as file:
                self.student_list = file.readlines()
                x = 0
                for i in self.student_list:
                    self.tk_student_list.insert(x, i)
                    x += 1

    def remise_a_zero_classe(self):
        if os.path.exists(self.filepath):
            self.tk_student_list.delete(0, END)
            with open(self.filepath, "r+") as file:
                self.student_list = file.readlines()
                x = 0
                self.tk_student_list.delete(0, 'end')
                delete = []
                for i in self.student_list:
                    if i == '\n' or i == ' \n' or i == '  \n' or i == "   \n" or i == "    \n" or i == "     \n" \
                            or i == "      \n" or i == "       \n":
                        delete.append(x)
                    x += 1
                x = 0
                for i in delete:
                    del self.student_list[i - x]
                    x += 1
                x = 0
                for i in self.student_list:
                    self.tk_student_list.insert(x, i)
                    x += 1


class Alerte:
    def __init__(self, show):
        self.show = show

    def save_new_class(self, option):
        if self.show:
            if askyesno(texte[langue][17], (texte[langue][18])):
                if option:
                    showinfo(texte[langue][17], texte[langue][19])
                return True
            else:
                return False

    def file_exist(self):
        if self.show:
            showerror(texte[langue][17], texte[langue][22])


texte = [
    # texte version anglaise
    ["Random Student", "Select classroom", "Select classroom", "Quit", "%s it's your go !",
     "Different student, every time", "file", "Select another classroom", "Choice a student", "Random Student V.0.0",
     "Redisplay classroom", "Edit", "Select classroom", 'New classroom', "Home", "Save modifications", "Students list :",
     "Look out", "Do you want save modifications", "The data had save", "Save new classroom", "Name of classroom",
     "Your classroom exist already.", "Copyright © all rights reserved\n Realized by Thibault MAGNIER"],
    # texte version française
    ["Random Student", "Choisir une classe", "Choisissez une classe", "Quitter", "%s c'est ton tour !",
     "élève différent, à chaque tour", "fichier", "Choisir une autre classe", "Choisir un élève", "Random Student V.0.0",
     "Réaffficher la classe", "Options", "Editer une classe", "Créer une classe", "Menu", "Enregistrer les modifications",
     "Liste d'élèves :", 'Attention', 'Êtes-vous sûr de vouloir enregistrer les modifications ?', 'Les données ont bien été enregistrés',
     "Enregistrer la nouvelle classe", "Nom de la classe", "Votre classe existe déjà.", "Copyright ©, tous droits réservés\n Réalisé par Thibault MAGNIER"]
]

langue = 0  # 0 = anglais / 1 = français

# pages configuration
window = Tk()
window.geometry("1080x780")
window.title(texte[langue][9])
window.config(background='white')

# frame
frame_0_d = Frame(window, bg='white')
frame_1_d = Frame(frame_0_d, bg='white')
frame_2_d = Frame(frame_1_d, bg='white')
frame_3_d = Frame(frame_0_d, bg='white')

# image
photo = PhotoImage(file=r"images\logo.png")
canvas = Canvas(frame_3_d, width=photo.width(), height=photo.height(), bg='white', bd=0, highlightthickness=0)
canvas.create_image(0, 0, anchor=NW, image=photo)

# démarage du logiciel
ecran = Screen(canvas, frame_0_d, frame_1_d, frame_2_d, frame_3_d)
alerte = Alerte(True)
ecran.menu()
window.mainloop()
