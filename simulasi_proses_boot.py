import time
import datetime

# memori internal cek hardware
hardware_cek = [
    '  -Asus Prime H610M-CS',
    '  -RAM:       Kingston FURY™ Beast DDR5 RGB',
    '  -GPU:       Geforce® RTX 2080 Ti',
    '  -Processor: Intel® Core™ i7-1255UL Gen-12',
    '  -Storage:   Seagate FireCuda 530 SSD M.2 2280 NVMe - 1TB',
    '  -Peripheral devices'
]
# memori internal proses boot / post
booting_flow = [
    "Memulai proses booting",
    "Memeriksa Perangkat Keras",
    "Memuat Kernel Sistem Operasi",
    "Proses booting selesai"
]
# memori internal user
data_user = []
# memori internal directory user
directory_data = [
        ['27/11/2023', '28/02/2023', '04/04/2023', '15/02/2023', '16/11/2023', '14/05/2023', '06/02/2023', '22/11/2023', '16/11/2023'], 
        ['01:19', '06:20', '20:16', '01:25','09:46', '16:13', '13:51', '07:13', '11:48'], 
        ['<DIR>', '<DIR>', '<DIR>', '<DIR>', '     ', ' ', ' ', ' ','<DIR>'], 
        ['   ','   ','   ','   ','173', '193.232', '132.100', '100.032', '   '], 
        ['Documents', 'Downloads', 'Contacts', 'Dropbox','.bash_history','latihan.txt', 'asep_041.pdf', 'asep_041.docx', 'project-fix']
    ]
# memory internal directory document
direc_doc = [
    [],
    [],
    [],
    [],
    []
]
# memory internal directory download
direc_dowloads = [
    [],
    [],
    [],
    [],
    []
]
# memory internal help
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
    "- date:        Menampilkan tanggal sekarang",
    "- time:        Menampilkan waktu sekarang",
    "- exit:        Keluar dari shell."
]
# memory internal systeminfo
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
# logic lokasi direktori
loc_document = False # boolean change directory document
loc_download = False # boolean change directory download

# Function delay dot
def loadingDot(jumlah_dot):
    loading_dots = ""
    for i in range(jumlah_dot):
        loading_dots = "."
        print(loading_dots, end='', flush=True)
        time.sleep(0.3)
# fungsi OK
def verify(jumlah_spasi):
    for j in range(jumlah_spasi):
        print(" ", end='', flush=True)
        time.sleep(0.03)
    print("[OK]")
# fungsi loading    
def loadingScreen():
    for i in range(101):
        print(f"Setup System Operation                                        {i}% ", end='\r')  # Menggunakan '\r' untuk menggeser kursor ke awal baris
        time.sleep(0.05) 
# fungsi proses boot
def proses_boot():
    print(booting_flow[0], end='')
    loadingDot(5)
    time.sleep(2)
    print()
    print()
    print(booting_flow[1], end='')
    loadingDot(5)
    time.sleep(1)
    print()
    print(hardware_cek[0], end='')
    verify(40)
    time.sleep(0.5)
    print(hardware_cek[1], end='')
    verify(19)
    time.sleep(0.5)
    print(hardware_cek[2], end='')
    verify(28)
    time.sleep(0.5)
    print(hardware_cek[3], end='')
    verify(19)
    time.sleep(0.5)
    print(hardware_cek[4], end='')
    verify(4)
    time.sleep(0.5)
    print(hardware_cek[5], end='')
    verify(41)
    time.sleep(0.5)
    print(booting_flow[2], end='')
    loadingDot(5)
    time.sleep(1.5)
    print()
    loadingScreen()
    print()
    print()
    print(booting_flow[3])
    time.sleep(1.5)
    cls()

# fungsi sistem login
def login_system(data_user):
    user = {}
    while True:
        proteksi = input(r"C:\User> ")
        if proteksi == '':
            username = input("Masukan username: ")
            if username == '':
                while True:
                    print('Username tidak boleh kosong')
                    username = input("Masukan username: ")
                    if username:
                        break
            password = input("Masukan password: ")
            user['username'] = username
            user['password'] = password
            data_user.append(user)
            break
        else:
            print("Anda bukan user. Klik 'Enter' untuk melanjutan.")
    return user
# fungsi clear display (cls)
def cls():
    print('\033c', end='')
# fungsi menampilkan direktori (dir)
def all_direct(directory):
    if len(directory[0]) > 0:
        for i in range(len(directory[0])):
            print(f"{directory[0][i]}  {directory[1][i]}   {directory[2][i]}        {directory[3][i]}          {directory[4][i]}")
    else:
        print("-Direktori Kosong-")
# fungsi merubah nama (ren)
def ren(args,directory):
    if args:
        if len(args) == 2:
            for i in range(len(directory[4])):
                if args[0] == directory[4][i]:
                    directory[4][i] = args[1]
            return directory
# fungsi membuat direktori dan bisa lebih dari satu (mkdir) 
def mkdir(args, directory):
    if args:
        for i in range(len(args)):
            directory[0].append(datetime.datetime.now().strftime("%d-%m-%Y"))
            directory[1].append(datetime.datetime.now().strftime("%H:%M"))
            directory[2].append("<DIR>")
            directory[3].append("   ")
            directory[4].append(args[i])
    return directory
# fungsi remove directory (rd)
def rd(args, directory):
    found = False
    if args:
        for i in range(len(directory[0])):
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
# fungsi delete file (del)
def delete_file(args, directory):
    found = False
    if args:
        for i in range(len(directory[0])):
            if directory[4][i] == args[0]:
                if directory[2][i] != "<DIR>":
                    directory[0].remove(directory[0][i])
                    directory[1].remove(directory[1][i])
                    directory[2].remove(directory[2][i])
                    directory[3].remove(directory[3][i])
                    directory[4].remove(directory[4][i])
                    found = True
                    break
                break
        if not found:
            print("Nama File tidak valid")
        return directory
           
# Fungsi untuk menjalankan perintah di shell (CLI)
def run_command(command, args, help_data, info_data):
    global loc_document
    global loc_download
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
        elif loc_download:
            rd(args,direc_dowloads)
        else:
            rd(args, directory_data)
    elif command == "ren" or command == "rename":
        if loc_document:
            ren(args, direc_doc)
        elif loc_download:
            ren(args,direc_dowloads) 
        else:   
            ren(args,directory_data)
    elif command == "mkdir":
        if loc_document:
            mkdir(args, direc_doc) 
        elif loc_download:
            mkdir(args,direc_dowloads)
        else:   
            mkdir(args,directory_data)
    elif command == "del":
        if loc_document:
            delete_file(args, direc_doc) 
        elif loc_download:
            delete_file(args,direc_dowloads)
        else:   
            delete_file(args,directory_data)
    elif command == "dir":
        if loc_document:
            print(r"Directory of C:\Users\{}\Document:".format(data_user[0]["username"]))
            all_direct(direc_doc)
        elif loc_download:
            print(r"Directory of C:\Users\{}\Downloads:".format(data_user[0]["username"]))
            all_direct(direc_dowloads)
        else:
            print(r"Directory of C:\Users\{}:".format(data_user[0]["username"]))
            all_direct(directory_data)
    elif command == "date":
        date = datetime.datetime.now().strftime("%d/%m/%Y")
        print(f"The current date is: {date}")
    elif command == "time":
        time_now = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"The current time is: {time_now}")
    elif command == "cls" or command == "clear": 
        cls()
    elif command == "exit":
        quit()
    else:
        print("Perintah tidak dikenali. Ketik 'help' untuk bantuan.")
# fungsi simulasi cmd
def simulasi_CLI():
    global loc_document
    global loc_download
    while True:
        print()
        user_input = input(r"C:\Users\{}> ".format(data_user[0]["username"]))
        if user_input == '':
            print("Perintah tidak dikenali. Ketik 'help' untuk bantuan.")
        else:
            tokens = user_input.split()  # Memisahkan masukan pengguna berdasarkan spasi
            args = tokens[1:]  # Argumen perintah berada pada indeks setelah perintah 
            command = tokens[0]  # Perintah berada pada indeks pertama dalam list tokens
            if len(tokens) > 0:
                if args and command == 'cd' and args[0] == 'Documents':
                    while True:
                        loc_document = True
                        print()
                        user_input = str(input(r"C:\Users\{}\Documents> ".format(data_user[0]["username"])))
                        tokens = user_input.split() 
                        args = tokens[1:]
                        command = tokens[0] 
                        if command == 'cd..':
                            loc_document = False
                            break
                        else:
                            run_command(command, args, help_data, info_data) 
                elif args and command == 'cd' and args[0] == "Downloads":
                    while True:
                        loc_download = True
                        print()
                        user_input = str(input(r"C:\Users\{}\Downloads> ".format(data_user[0]["username"])))
                        tokens = user_input.split()
                        args = tokens[1:] 
                        command = tokens[0] 
                        if command == 'cd..':
                            loc_download = False
                            break
                        else:
                            run_command(command, args, help_data, info_data) 
                else:
                    run_command(command, args, help_data, info_data)
# main program
proses_boot()
print()
print(r"D3NEW-OS [Version 1.0.0.0 v1]")
print(r"(c)D3NEW-OS. All rights reserved.")
login_system(data_user)
simulasi_CLI()