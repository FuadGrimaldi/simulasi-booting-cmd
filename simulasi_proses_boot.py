import time
import datetime
import os

booting_flow = [
    "Starting the booting process", 
    "Hardware Checking", 
    "Firmware Checking (BIOS/UEFI)", 
    "Bootloader Checking", 
    "Loading Operating System Kernel", 
    "Hardware Initialization", 
    "Starting Services and Drivers", 
    "Booting completed. Please login to continue.   "
    ]

def loadingDot(jumlah_dot):
    loading_dots = ""
    for i in range(jumlah_dot):
        loading_dots = "."
        print(loading_dots, end='', flush=True)
        time.sleep(0.5)

def verify(jumlah_spasi):
    loading_dots = ""
    for i in range(jumlah_spasi):
        loading_dots = " "
        print(loading_dots, end='', flush=True)
    print("OK")

def loadingScreen():
    for i in range(101):
        print(f"Setup System Operation                    {i}% ", end='\r')  # Menggunakan '\r' untuk menggeser kursor ke awal baris
        time.sleep(0.1)  # Mengatur kecepatan pembaruan

def proses_boot():
    print(booting_flow[0], end='', flush=True)
    loadingDot(5)
    time.sleep(2)
    print()
    print()
    print(booting_flow[1], end='', flush=True)
    loadingDot(5)
    verify(20)
    time.sleep(1.5)
    print(booting_flow[2], end='', flush=True)
    loadingDot(5)
    verify(8)
    time.sleep(1.5)
    print(booting_flow[3], end='', flush=True)
    loadingDot(5)
    verify(18)
    time.sleep(1.5)
    print(booting_flow[4], end='', flush=True)
    loadingDot(5)
    verify(6)
    time.sleep(1.5)
    print(booting_flow[5], end='', flush=True)
    loadingDot(5)
    verify(14)
    time.sleep(1.5)
    print(booting_flow[6], end='', flush=True)
    loadingDot(5)
    verify(8)
    time.sleep(2)
    print()
    loadingScreen()
    print(booting_flow[7])


def login_system():
    # Dictionary untuk menyimpan username dan password
    daftar_user = {
        "D3":"SO"
    }
    print("username: D3 & password: SO")
    while True:
        username = input("Masukkan username: ")
        password = input("Masukkan password: ")
        # cek apakah username terdaftar dan password sesuai
        if username in daftar_user and daftar_user[username] == password:
            print("----- Login berhasil! -----")
            break  # break looping jika login berhasil
        else:
            print("----- Username atau Password salah! -----")

# def power_on():
#     print('ketik on untuk menyalakan device')
#     while True:
#         po = input("> ")
#         if po == "on":
#             proses_post()
#             break  # break looping jika kondisi awal terpenuhi
#         else:
#             print('Perintah tidak diketahui. Coba lagi.')

# power_on()
directory_data = [
        ['27/11/2023', '28/02/2023', '04/04/2023', '15/02/2023', '16/11/2023', '14/05/2023', '06/02/2023', '22/11/2023', '16/11/2023'], 
        ['01:19', '06:20', '20:16', '01:25','09:46', '16:13', '13:51', '07:13', '11:48'], 
        ['<DIR>', '<DIR>', '<DIR>', '<DIR>', '     ', ' ', ' ', ' ','<DIR>'], 
        ['   ','   ','   ','   ','173', '193.232', '132.100', '100.032', '   '], 
        ['Documents', 'Downloads', 'Contacts', 'Dropbox','.bash_history','latihan.txt', 'asep_041.pdf', 'asep_041.docx', 'project fix']
    ]
direc_doc = [
    ['28/02/2023', '28/02/2023'],
    ['01:19', '06:20'],
    [' ', ' '],
    ['132.322','213.222'],
    ['D3-SO-T1.docx', 'D3-SO-T1.pdf']
]
help_data = [
    "- help:        Menampilkan daftar perintah yang tersedia.",
    "- systeminfo:  Menampilkan informasi sistem.",
    "- cd:          Beralih directory",
    "- dir:         Menampilkan daftar file dalam direktori.",
    "- mkdir:       Membuat direktori baru.",
    "- rename/ren:  Mengubah nama file dalam direktori.",
    "- rd:          Menghapus direktori",
    "- del:         Menghapus file",
    "- cls:         Membersihkan layar",
    "- exit:        Keluar dari shell."
]
info_data = [
    "Nama Sistem Operasi:   D3NEW-OS",
    "Versi Sistem Operasi:  1.0.0.0 v1",
    "Pemilik Terdaftar:     D3",
    "Tipe Sistem:           x64-based PC",
    "Prosessor:             Intel® Core™ i7-1255UL Gen-12",
    "",
    "Versi BIOS:            AMI F.13",
    "Direktori Windows:     C:\WINDOWS",
    "Direktori Sistem:      C:\WINDOWS\system32",
    "Time Zone:             (UTC+07:00) Bangkok, Hanoi, Jakarta"
]
loc_document = False

def all_direct(directory):
    for i in range(len(directory[0])):
        print(f"{directory[0][i]}  {directory[1][i]}   {directory[2][i]}        {directory[3][i]}          {directory[4][i]}")
    print("         1 File(s)          173 bytes")
    print("         4 dir(s)          2.343.434 bytes")
def dir(args):
    if args:
        if args[0] == "2":
            print("jeruk")
            return 
def ren(args,directory):
    if args:
        if len(args) == 2:
            for i in range(len(directory[4])):
                if args[0] == directory[4][i]:
                    directory[4][i] = args[1]
            return directory
def mkdir(args, directory):
    if args:
        directory[0].append(datetime.datetime.now().strftime("%d-%m-%Y"))
        directory[1].append(datetime.datetime.now().strftime("%H:%M"))
        directory[2].append("<DIR>")
        directory[3].append("   ")
        directory[4].append(args[0])
    return directory
def rd(args, directory):
    found = False
    if args:
        for i in range(len(directory)):
            if directory[4][i] == args[0]:
                if directory[2][i] == "<DIR>":
                    directory[0].remove(directory[0][i])
                    directory[1].remove(directory[1][i])
                    directory[2].remove(directory[2][i])
                    directory[3].remove(directory[3][i])
                    directory[4].remove(directory[4][i])
                    found = True
                    break
        if not found:
            print("Nama direktori tidak valid")
        return directory
def delete_file(args, directory):
    found = False
    if args:
        print("True")
        for i in range(len(directory)):
            if directory[4][i] == args[0]:
                if directory[2][i] != "<DIR>":
                    print("True2")
                    directory[0].remove(directory[0][i])
                    directory[1].remove(directory[1][i])
                    directory[2].remove(directory[2][i])
                    directory[3].remove(directory[3][i])
                    directory[4].remove(directory[4][i])
                    found = True
                    break
        if not found:
            print("Nama File tidak valid")
        return directory

            

# Fungsi untuk menjalankan perintah di shell (CLI)
def run_command(command, args, help_data, info_data):
    global loc_document
    print(args)
    if command == "help":
        print("Daftar perintah yang tersedia:")
        for i in range(len(help_data)):
            print(help_data[i])
    elif command == "systeminfo":
        for i in range(len(info_data)):
            print(info_data[i])
    elif command == "rd":
        if loc_document:
            rd(args, direc_doc)
        else:
            rd(args, directory_data)
    elif command == "ren" or command == "rename":
        if loc_document:
            ren(args, direc_doc) 
        else:   
            ren(args,directory_data)
    elif command == "mkdir":
        if loc_document:
            mkdir(args, direc_doc) 
        else:   
            mkdir(args,directory_data)
    elif command == "del":
        if loc_document:
            delete_file(args, direc_doc) 
        else:   
            delete_file(args,directory_data)
    elif command == "dir":
        if loc_document:
            print(r"Directory of C:\Users\Kelompok3\document:")
            all_direct(direc_doc)
        else:
            print(r"Directory of C:\Users\Kelompok3:")
            all_direct(directory_data)
    elif command == "date":
        date = datetime.datetime.now().strftime("%d-%m-%Y")
        print(f"The current date is: {date}")
    elif command == "cls" or command == "clear": 
        os.system('cls' if command == "cls" else 'clear')
    elif command == "exit":
        print("Menutup sistem operasi", end="")
        loadingDot(5)
        time.sleep(1)
        print("\nSistem operasi berhasil dimatikan.")
        quit()
    else:
        print("Perintah tidak dikenali. Ketik 'help' untuk bantuan.")

# main program
proses_boot()
login_system()
print(r"D3NEW-OS [Version 1.0.0.0 v1]")
print(r"(c) D3NEW-OS. All rights reserved.")
while True:
    user_input = str(input(r"C:\User\kelompok3> "))
    if not user_input:  # Jika tidak ada input
        print("Masukkan perintah.")
    tokens = user_input.split()  # Memisahkan masukan pengguna berdasarkan spasi
    args = tokens[1:]  # Argumen perintah berada pada indeks setelah perintah itu sendiri
    command = tokens[0]  # Perintah berada pada indeks pertama dalam list tokens
    print(tokens)
    if len(tokens) > 0:
        if args and command == 'cd' and args[0] == 'document':
            while True:
                loc_document = True
                user_input = str(input(r"C:\User\kelompok3\document> "))
                tokens = user_input.split()  # Memisahkan masukan pengguna berdasarkan spasi
                args = tokens[1:]
                command = tokens[0]  # Perintah berada pada indeks pertama dalam list tokens
                if command == 'cd..':
                    loc_document = False
                    break
                else:
                    run_command(command, args, help_data, info_data) 
        else:
            run_command(command, args, help_data, info_data)

