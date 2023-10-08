from tkinter import PhotoImage
import customtkinter as customtk
import os
from PIL import Image,ImageTk
from CTkMessagebox import CTkMessagebox



customtk.set_appearance_mode("dark")
customtk.set_default_color_theme("blue")

# globalVariabel
nama=""
jeniskelamin=""
kelas=""
asalsekolah=""
emosi=""


app=customtk.CTk()
app.title("Emotion Electroencephalography Recognition")
app.geometry(f"{1150}x{580}")

#image
image_path=os.path.join(os.path.dirname(os.path.realpath(__file__)),"icon")
logo_small=customtk.CTkImage(Image.open(os.path.join(image_path,"eeg-icon-7.png")),size=(30,30))
home_image=customtk.CTkImage(Image.open(os.path.join(image_path,"home_light.png")),size=(18,18))
petunjuk_image=customtk.CTkImage(Image.open(os.path.join(image_path,"book.png")),size=(18,18))
emotion_image=customtk.CTkImage(Image.open(os.path.join(image_path,"emotion.png")),size=(18,18))
about_image=customtk.CTkImage(Image.open(os.path.join(image_path,"about.png")),size=(18,18))
exit_image=customtk.CTkImage(Image.open(os.path.join(image_path,"exit.png")),size=(21,21))
logo_image=customtk.CTkImage(Image.open(os.path.join(image_path,"eeg-icon-7.png")),size=(100,100))

muse2_image=customtk.CTkImage(Image.open(os.path.join(image_path,"muse2_headband.png")),size=(150,150))
smartphone_image=customtk.CTkImage(Image.open(os.path.join(image_path,"smartphone.png")),size=(150,150))
laptop_image=customtk.CTkImage(Image.open(os.path.join(image_path,"laptop.png")),size=(150,150))

mindmonitor_image=customtk.CTkImage(Image.open(os.path.join(image_path,"mind_monitor.png")),size=(100,100))
muse2power_image=customtk.CTkImage(Image.open(os.path.join(image_path,"muse2_power.png")),size=(200,200))
bluetooth_image=customtk.CTkImage(Image.open(os.path.join(image_path,"bluetooth.png")),size=(300,200))
cmd_image=customtk.CTkImage(Image.open(os.path.join(image_path,"commandprompt.png")),size=(520,200))
ipconfig_image=customtk.CTkImage(Image.open(os.path.join(image_path,"ipconfig.png")),size=(520,200))
ipaddress_image=customtk.CTkImage(Image.open(os.path.join(image_path,"ipaddress.png")),size=(520,240))
setting_mind_monitor_image=customtk.CTkImage(Image.open(os.path.join(image_path,"menusettingmindmonitor.png")),size=(300,600))
osctreamtarget_image=customtk.CTkImage(Image.open(os.path.join(image_path,"OSCStreamTarget.png")),size=(300,600))
osctreamtargetip_image=customtk.CTkImage(Image.open(os.path.join(image_path,"OSCStreamTargetipaddress.png")),size=(300,600))
tombolstream_image=customtk.CTkImage(Image.open(os.path.join(image_path,"tombolstream.png")),size=(300,600))
model_headband_image=customtk.CTkImage(Image.open(os.path.join(image_path,"petunjuk.png")),size=(150,150))

safrizal_image=customtk.CTkImage(Image.open(os.path.join(image_path,"safrizal.png")),size=(120,120))
pakfatchul_image=customtk.CTkImage(Image.open(os.path.join(image_path,"far.png")),size=(120,120))


# photo = PhotoImage(file = "icon/eeg-icon-7.png")
iconpath=ImageTk.PhotoImage(file=os.path.join(image_path,"eeg-icon-7.png"))
app.wm_iconbitmap()
app.iconphoto(False,iconpath)
app.resizable(False,False)
app.grid_rowconfigure(0,weight=1)
app.grid_columnconfigure(1,weight=1)

def select_frame_by_name(name):
    btnHome.configure(fg_color=("#2562a7", "#296ebc") if name == "home" else "transparent")
    btnPetunjuk.configure(fg_color=("#2562a7", "#296ebc")if name == "petunjuk" else "transparent")
    btnIsiData.configure(fg_color=("#2562a7", "#296ebc") if name == "isidata" else "transparent")
    btnAbout.configure(fg_color=("#2562a7", "#296ebc") if name == "about" else "transparent")
    # show selected frame
    if name == "home":
        home_frame.grid(row=0, column=1, sticky="nsew")
    else:
        home_frame.grid_forget()
        
    if name == "petunjuk":
        petunjuk_frame.grid(row=0, column=1, sticky="nsew")
    else:
        petunjuk_frame.grid_forget()
        
    if name == "isidata":
        isiData_frame.grid(row=0, column=1, sticky="nsew")
    else:
        isiData_frame.grid_forget()
    
    if name == "deteksiemosi":
        tesEmosi_frame.grid(row=0, column=1, sticky="nsew")
    else:
        tesEmosi_frame.grid_forget()
    
    if name == "about":
        about_frame.grid(row=0, column=1, sticky="nsew")
    else:
        about_frame.grid_forget()
    
    print(name)
    # if name == "frame_3":
    #     third_frame.grid(row=0, column=1, sticky="nsew")
    # else:
    #     third_frame.grid_forget()

def home_btn_event():
    select_frame_by_name("home")
    
def petunjuk_frame_btn_event():
    select_frame_by_name("petunjuk")
    
def isidata_frame_btn_event():
    select_frame_by_name("isidata")
    
def deteksiemosi_frame_btn_event():
    nama=namaInput.get()
    kelas=kelasInput.get()
    jenisKelamin=jenisKelaminInput.get()
    asalsekolah=sekolahInput.get()
    
    if nama=="":
        CTkMessagebox(title="Peringatan", message="Nama Siswa tidak boleh kosong", icon="warning")
    elif kelas=="":
        CTkMessagebox(title="Peringatan", message="Kelas tidak boleh kosong", icon="warning")
    elif jenisKelamin=="":
        CTkMessagebox(title="Peringatan", message="Jenis Kelamin harus dipilih", icon="warning")
    elif asalsekolah=="":
        CTkMessagebox(title="Peringatan", message="Asal Sekolah tidak boleh kosong", icon="warning")
    else:
        select_frame_by_name("deteksiemosi")
    
def about_frame_btn_event():
    select_frame_by_name("about")

def close():
    msg = CTkMessagebox(title="Exit?", message="Apakah anda ingin menutup aplikasi?",
                        icon="question", option_1="Tidak", option_2="Ya",fade_in_duration=1)
    response = msg.get()
    
    if response=="Ya":
        app.destroy()       
        


# navigation_frame
navigation_frame=customtk.CTkFrame(app,corner_radius=0)
navigation_frame.grid(row=0,column=0,sticky="nsew")
navigation_frame.grid_rowconfigure(6,weight=1)
navigation_frame.grid_columnconfigure(4,weight=2)

nfLabel=customtk.CTkLabel(navigation_frame,text="  EER Aplication",image=logo_small,compound="left",font=customtk.CTkFont(size=20,weight="bold"))
nfLabel.grid(row=0,column=0,padx=20,pady=20)

btnHome=customtk.CTkButton(navigation_frame,corner_radius=0,height=40,border_spacing=10,text="Beranda",
                                                    fg_color="transparent",text_color=("gray10","gray90"),font=customtk.CTkFont(size=14,weight="normal"),
                                                    hover_color=("#4387d6","#2e7ad1"), image=home_image,anchor="w",
                                                    command=home_btn_event)
btnHome.grid(row=1,column=0,sticky="ew")

btnPetunjuk=customtk.CTkButton(navigation_frame,corner_radius=0,height=40,border_spacing=10,text="Petunjuk",
                                                    fg_color="transparent",text_color=("gray10","gray90"),font=customtk.CTkFont(size=14,weight="normal"),
                                                    hover_color=("#4387d6","#2e7ad1"), image=petunjuk_image,anchor="w",
                                                    command=petunjuk_frame_btn_event)
btnPetunjuk.grid(row=2,column=0,sticky="ew")

btnIsiData=customtk.CTkButton(navigation_frame,corner_radius=0,height=40,border_spacing=10,text="Deteksi Emosi",
                                                    fg_color="transparent",text_color=("gray10","gray90"),font=customtk.CTkFont(size=14,weight="normal"),
                                                    hover_color=("#4387d6","#2e7ad1"),  image=emotion_image,anchor="w",
                                                    command=isidata_frame_btn_event)
btnIsiData.grid(row=3,column=0,sticky="ew")

btnAbout=customtk.CTkButton(navigation_frame,corner_radius=0,height=40,border_spacing=10,text="Tentang Aplikasi",
                                                    fg_color="transparent",text_color=("gray10","gray90"),font=customtk.CTkFont(size=14,weight="normal"),
                                                    hover_color=("#4387d6","#2e7ad1"),  image=about_image,anchor="w",
                                                    command=about_frame_btn_event)
btnAbout.grid(row=4,column=0,sticky="ew")
btnClose=customtk.CTkButton(navigation_frame,corner_radius=0,height=40,border_spacing=10,text="Tutup",
                                                    fg_color="transparent",text_color=("gray10","gray90"),font=customtk.CTkFont(size=14,weight="normal"),
                                                    hover_color=("#4387d6","#2e7ad1"),  image=exit_image,anchor="w",
                                                    command=close)
btnClose.grid(row=5,column=0,sticky="ew")



#home_frame
home_frame=customtk.CTkFrame(app,corner_radius=0,fg_color="transparent")
home_frame.grid_columnconfigure(0,weight=1)

hfLabel=customtk.CTkLabel(home_frame,text="Selamat Datang",font=customtk.CTkFont(size=20,weight='bold'))
hfLabel.grid(row=0,column=0,pady=(20,0),padx=30,sticky="ew")
hfLabel1=customtk.CTkLabel(home_frame,text="Di Aplikasi Electroenchepalography Emotion Recognition",font=customtk.CTkFont(size=20,weight='bold'))
hfLabel1.grid(row=1,column=0,pady=10,padx=30,sticky="ew")

hfLogoLabel=customtk.CTkLabel(home_frame,text="",image=logo_image)
hfLogoLabel.grid(row=2,column=0,padx=30,pady=10,sticky="ew")

btnMulai= customtk.CTkButton(home_frame, text="Deteksi Emosi",height=50,width=200,corner_radius=0,font=customtk.CTkFont(weight="bold",size=14),command=isidata_frame_btn_event)
btnMulai.grid(row=3,column=0,padx=30,pady=(30,0))

btnPetunjuk2=customtk.CTkButton(home_frame,text="Butuh petunjuk penggunaan aplikasi ?",
                                                        font=customtk.CTkFont(size=14,weight="normal"),                   
                                                        fg_color="transparent",image=petunjuk_image,
                                                        hover_color=("grey35","grey30"),corner_radius=0,
                                                        command=petunjuk_frame_btn_event)
btnPetunjuk2.grid(row=4,column=0,padx=(0,0),pady=(70,0))

#frame petunjuk
petunjuk_frame=customtk.CTkScrollableFrame(app,fg_color="transparent",corner_radius=0,scrollbar_button_color=("#2562a7", "#296ebc"),scrollbar_button_hover_color=("#4387d6","#2e7ad1"))
petunjuk_frame.grid_columnconfigure(0,weight=1)

pfLabel=customtk.CTkLabel(petunjuk_frame,text="Petunjuk Penggunaan Aplikasi",font=customtk.CTkFont(size=20,weight='bold'))
pfLabel.grid(row=0,column=0,pady=20,padx=30,sticky="ew", columnspan=3)

pfTitle1=customtk.CTkLabel(petunjuk_frame,text="A. Pengenalan Perangkat Keras",font=customtk.CTkFont(size=17,weight='bold'))
pfTitle1.grid(row=1,column=0,pady=(10,0),padx=30,sticky="w", columnspan=3)

# 1. Muse 2 Headband
pfMuse2=customtk.CTkLabel(petunjuk_frame,text="1. Muse 2 Headband",font=customtk.CTkFont(size=15,weight="normal"))
pfMuse2.grid(row=2,column=0,pady=(10,0),padx=60,sticky="w")
pfMuse2Image=customtk.CTkLabel(petunjuk_frame,text="",image=muse2_image)
pfMuse2Image.grid(row=3,column=0,pady=(5,0),padx=75,sticky="w")

# 2. Smartphone
pfSmartphone=customtk.CTkLabel(petunjuk_frame,text="2. Smartphone",font=customtk.CTkFont(size=15,weight="normal"))
pfSmartphone.grid(row=2,column=1,pady=(10,0),padx=60,sticky="w")
pfSmartphoneImage=customtk.CTkLabel(petunjuk_frame,text="",image=smartphone_image)
pfSmartphoneImage.grid(row=3,column=1,pady=(5,0),padx=75,sticky="w")


#3.Laptop
pfLaptop=customtk.CTkLabel(petunjuk_frame,text="3. Laptop/Komputer",font=customtk.CTkFont(size=15,weight="normal"))
pfLaptop.grid(row=2,column=2,pady=(10,0),padx=60,sticky="w")
pfLaptopImage=customtk.CTkLabel(petunjuk_frame,text="",image=laptop_image)
pfLaptopImage.grid(row=3,column=2,pady=(5,0),padx=75,sticky="w")

pfTitle2=customtk.CTkLabel(petunjuk_frame,text="B. Langkah Penggunaan Aplikasi",font=customtk.CTkFont(size=17,weight='bold'))
pfTitle2.grid(row=4,column=0,pady=(30,0),padx=30,sticky="w", columnspan=3)

pfL1=customtk.CTkLabel(petunjuk_frame,text="1. Install aplikasi Mind Monitor pada smartphone.",font=customtk.CTkFont(size=15,weight="normal"))
pfL1.grid(row=5,column=0,pady=(10,0),padx=60,sticky="w", columnspan=3)

#gambar
pfG1=customtk.CTkLabel(petunjuk_frame,text="",image=mindmonitor_image)
pfG1.grid(row=6,column=0,pady=(10,0),padx=80,sticky="w",columnspan=3)

pfL2=customtk.CTkLabel(petunjuk_frame,text="2. Nyalakan Muse 2 Headband dengan menekan tombol power",font=customtk.CTkFont(size=15,weight="normal"))
pfL2.grid(row=7,column=0,pady=(10,0),padx=60,sticky="w", columnspan=3)
#gambar
pfG2=customtk.CTkLabel(petunjuk_frame,text="",image=muse2power_image)
pfG2.grid(row=8,column=0,pady=(10,0),padx=80,sticky="w",columnspan=3)

pfL3=customtk.CTkLabel(petunjuk_frame,text="3. Nyalakan Bluetooth pada smartphone.",font=customtk.CTkFont(size=15,weight="normal"))
pfL3.grid(row=9,column=0,pady=(10,0),padx=60,sticky="w", columnspan=3)
#gambar
pfG3=customtk.CTkLabel(petunjuk_frame,text="",image=bluetooth_image)
pfG3.grid(row=10,column=0,pady=(10,0),padx=80,sticky="w",columnspan=3)

pfL4=customtk.CTkLabel(petunjuk_frame,text="4. Jalankan aplikasi Mind Monitor pada smartphone.",font=customtk.CTkFont(size=15,weight="normal"))
pfL4.grid(row=11,column=0,pady=(10,0),padx=60,sticky="w", columnspan=3)

#gambar

pfL5=customtk.CTkLabel(petunjuk_frame,text="5. Hubungkan aplikasi Mind Monitor dengan Muse 2 Headband.",font=customtk.CTkFont(size=15,weight="normal"))
pfL5.grid(row=13,column=0,pady=(10,0),padx=60,sticky="w", columnspan=3)
#gambar

pfL6=customtk.CTkLabel(petunjuk_frame,text="6. Hubungkan Laptop dengan smartphone dengan cara Laptop dan smartphone mengakses jaringan Akses Point yang sama.",font=customtk.CTkFont(size=15,weight="normal"))
pfL6.grid(row=15,column=0,pady=(10,0),padx=(60,0),sticky="w", columnspan=3)
#gambar

pfL7=customtk.CTkLabel(petunjuk_frame,text="7. Jalankan Command Prompt pada Laptop/Komputer. ",font=customtk.CTkFont(size=15,weight="normal"))
pfL7.grid(row=17,column=0,pady=(10,0),padx=(60,0),sticky="w", columnspan=3)
#gambar
pfG7=customtk.CTkLabel(petunjuk_frame,text="",image=cmd_image)
pfG7.grid(row=18,column=0,pady=(10,0),padx=80,sticky="w",columnspan=3)

pfL8=customtk.CTkLabel(petunjuk_frame,text="8. Ketik 'ipconfig' lalu tekan Enter.",font=customtk.CTkFont(size=15,weight="normal"))
pfL8.grid(row=19,column=0,pady=(10,0),padx=(60,0),sticky="w", columnspan=3)
#gambar
pfG8=customtk.CTkLabel(petunjuk_frame,text="",image=ipconfig_image)
pfG8.grid(row=20,column=0,pady=(10,0),padx=80,sticky="w",columnspan=3)

pfL9=customtk.CTkLabel(petunjuk_frame,text="9. Catat IP Address yang didapat oleh Laptop/Komputer.",font=customtk.CTkFont(size=15,weight="normal"))
pfL9.grid(row=21,column=0,pady=(10,0),padx=(60,0),sticky="w", columnspan=3)
#gambar
pfG9=customtk.CTkLabel(petunjuk_frame,text="",image=ipaddress_image)
pfG9.grid(row=22,column=0,pady=(10,0),padx=80,sticky="w",columnspan=3)

pfL10=customtk.CTkLabel(petunjuk_frame,text="10. Buka menu setting pada aplikasi Mind Monitor.",font=customtk.CTkFont(size=15,weight="normal"))
pfL10.grid(row=23,column=0,pady=(10,0),padx=(60,0),sticky="w", columnspan=3)
#gambar
pfG10=customtk.CTkLabel(petunjuk_frame,text="",image=setting_mind_monitor_image)
pfG10.grid(row=24,column=0,pady=(10,0),padx=80,sticky="w",columnspan=3)

pfL11=customtk.CTkLabel(petunjuk_frame,text="11. Pilih menu OSC Stream Target IP.",font=customtk.CTkFont(size=15,weight="normal"))
pfL11.grid(row=25,column=0,pady=(10,0),padx=(60,0),sticky="w", columnspan=3)
#gambar
pfG11=customtk.CTkLabel(petunjuk_frame,text="",image=osctreamtarget_image)
pfG11.grid(row=26,column=0,pady=(10,0),padx=80,sticky="w",columnspan=3)

pfL12=customtk.CTkLabel(petunjuk_frame,text="12. Masukkan IP Address Laptop/Komputer pada menu OSC Stream Target IP.",font=customtk.CTkFont(size=15,weight="normal"))
pfL12.grid(row=27,column=0,pady=(10,0),padx=(60,0),sticky="w", columnspan=3)
#gambar
pfG12=customtk.CTkLabel(petunjuk_frame,text="",image=osctreamtargetip_image)
pfG12.grid(row=28,column=0,pady=(10,0),padx=80,sticky="w",columnspan=3)

pfL13=customtk.CTkLabel(petunjuk_frame,text="13. Lalu kembali ke halaman utama Mind Monitor.",font=customtk.CTkFont(size=15,weight="normal"))
pfL13.grid(row=29,column=0,pady=(10,0),padx=(60,0),sticky="w", columnspan=3)
#gambar


pfL14=customtk.CTkLabel(petunjuk_frame,text="14. Klik tombol stream pada aplikasi Mind Monitor. ",font=customtk.CTkFont(size=15,weight="normal"))
pfL14.grid(row=31,column=0,pady=(10,0),padx=(60,0),sticky="w", columnspan=3)
#gambar
pfG14=customtk.CTkLabel(petunjuk_frame,text="",image=tombolstream_image)
pfG14.grid(row=32,column=0,pady=(10,0),padx=80,sticky="w",columnspan=3)

pfL15=customtk.CTkLabel(petunjuk_frame,text="15. Pasangkan Muse2 Headband pada siswa sesuai gambar di bawah berikut. ",font=customtk.CTkFont(size=15,weight="normal"))
pfL15.grid(row=33,column=0,pady=(10,0),padx=(60,0),sticky="w", columnspan=3)
#gambar
pfG15=customtk.CTkLabel(petunjuk_frame,text="",image=model_headband_image)
pfG15.grid(row=34,column=0,pady=(10,0),padx=80,sticky="w",columnspan=3)

pfL16=customtk.CTkLabel(petunjuk_frame,text="16. Pastikan semua sensor elektroda telah menyentuh kulit kepala. ",font=customtk.CTkFont(size=15,weight="normal"))
pfL16.grid(row=35,column=0,pady=(10,0),padx=(60,0),sticky="w", columnspan=3)
#gambar

pfL17=customtk.CTkLabel(petunjuk_frame,text="17. Klik tombol/menu 'Deteksi Emosi' pada aplikasi EER. ",font=customtk.CTkFont(size=15,weight="normal"))
pfL17.grid(row=37,column=0,pady=(10,0),padx=(60,0),sticky="w", columnspan=3)
#gambar

pfL18=customtk.CTkLabel(petunjuk_frame,text="18. Lengkapi formulir data siswa. ",font=customtk.CTkFont(size=15,weight="normal"))
pfL18.grid(row=39,column=0,pady=(10,0),padx=(60,0),sticky="w", columnspan=3)
#gambar

pfL19=customtk.CTkLabel(petunjuk_frame,text="19. Klik Tombol Selanjutnya. ",font=customtk.CTkFont(size=15,weight="normal"))
pfL19.grid(row=41,column=0,pady=(10,0),padx=(60,0),sticky="w", columnspan=3)
#gambar

pfL20=customtk.CTkLabel(petunjuk_frame,text="20. Klik Tombol Mulai. ",font=customtk.CTkFont(size=15,weight="normal"))
pfL20.grid(row=43,column=0,pady=(10,0),padx=(60,0),sticky="w", columnspan=3)
#gambar

pfL21=customtk.CTkLabel(petunjuk_frame,text="21. Tunggu beberapa detik sampai muncul hasil Deteksi Emosi. ",font=customtk.CTkFont(size=15,weight="normal"))
pfL21.grid(row=45,column=0,pady=(10,0),padx=(60,0),sticky="w", columnspan=3)


#frame input data
isiData_frame=customtk.CTkFrame(app,corner_radius=0, fg_color="transparent")
isiData_frame.grid_columnconfigure(0,weight=1)
isiData_frame.grid_columnconfigure(1,weight=1)

idLabel=customtk.CTkLabel(isiData_frame,text="Formulir Data Siswa",font=customtk.CTkFont(size=20,weight='bold'))
idLabel.grid(row=0,column=0,columnspan=2,pady=20,padx=30,sticky="ew")

namaLabel=customtk.CTkLabel(isiData_frame,text="Nama Siswa :",font=customtk.CTkFont(size=15,weight='normal'))
namaLabel.grid(row=1,column=0,pady=10,padx=30,sticky="e")
namaInput=customtk.CTkEntry(isiData_frame,placeholder_text="",width=200)
namaInput.grid(row=1,column=1,pady=10,padx=0,sticky="w")

jenisKelaminLabel=customtk.CTkLabel(isiData_frame,text="Jenis Kelamin:",font=customtk.CTkFont(size=15,weight='normal'))
jenisKelaminLabel.grid(row=2,column=0,pady=10,padx=30,sticky="e")
jenisKelaminInput=customtk.CTkComboBox(isiData_frame,values=["Laki-Laki","Perempuan"],width=200)
jenisKelaminInput.grid(row=2,column=1,pady=10,padx=0,sticky="w")

kelasLabel=customtk.CTkLabel(isiData_frame,text="Kelas:",font=customtk.CTkFont(size=15,weight='normal'))
kelasLabel.grid(row=3,column=0,pady=10,padx=30,sticky="e")
kelasInput=customtk.CTkEntry(isiData_frame,placeholder_text="", width=200)
kelasInput.grid(row=3,column=1,pady=10,padx=0,sticky="w")

sekolahLabel=customtk.CTkLabel(isiData_frame,text="Asal Sekolah:",font=customtk.CTkFont(size=15,weight='normal'))
sekolahLabel.grid(row=4,column=0,pady=10,padx=30,sticky="e")
sekolahInput=customtk.CTkEntry(isiData_frame,placeholder_text="",width=200)
sekolahInput.grid(row=4,column=1,pady=10,padx=0,sticky="w")


btnMulai= customtk.CTkButton(isiData_frame, text="Selanjutnya", compound="right",corner_radius=0,width=100,command=deteksiemosi_frame_btn_event)
btnMulai.grid(row=6,column=1,sticky="w",padx=0,pady=30)


#frametesEmosi
tesEmosi_frame=customtk.CTkFrame(app,corner_radius=0,fg_color="transparent")
tesEmosi_frame.grid_columnconfigure(0,weight=1)

teLabel=customtk.CTkLabel(tesEmosi_frame,text="Prediksi Emosi",font=customtk.CTkFont(size=20,weight='bold'))
teLabel.grid(row=0,column=0,pady=20,padx=30,sticky="ew")

labelPetunjuk1=customtk.CTkLabel(tesEmosi_frame,text="1.Untuk memprediksi Emosi, tekan tombol Prediksi",font=customtk.CTkFont(size=15,weight='normal'))
labelPetunjuk1.grid(row=1,column=0,padx=(30,0),pady=20,sticky="w")
labelPetunjuk2=customtk.CTkLabel(tesEmosi_frame,text="2.Mohon jangan terlalu banyak menggerakkan kepala, karena akan mengganggu sinyal yang direkam.",font=customtk.CTkFont(size=15,weight='normal'))
labelPetunjuk2.grid(row=2,column=0,padx=(30,0),pady=(0,10),sticky="w")

btnPrediksi= customtk.CTkButton(tesEmosi_frame, text="Prediksi Emosi", compound="right",corner_radius=0,width=100,command=deteksiemosi_frame_btn_event)
btnPrediksi.grid(row=3,column=0,padx=0,pady=30)
btnPrediksi.configure(state=customtk.DISABLED,fg_color=('grey30','grey35'))
#frameAbout
about_frame=customtk.CTkFrame(app,corner_radius=0,fg_color="transparent")
about_frame.grid_columnconfigure(0,weight=1)
about_frame.grid_columnconfigure(1,weight=1)

alabel=customtk.CTkLabel(about_frame,text="Tentang Aplikasi",font=customtk.CTkFont(size=20,weight='bold'))
alabel.grid(row=0,column=0,pady=20,padx=30,sticky="ew",columnspan=2)

abparagraph=customtk.CTkLabel(about_frame,text="Aplikasi Electroencephalography Emotion Recognition (EER) adalah aplikasi yang dikembangkan untuk mengenali\nemosi pada peserta didik berdasarkan gelombang Elektro Ensefalografi (EEG) yang diterima oleh perangkat untuk\ndinalisa dan diklasifikasikan kedalam salah satu dari 4 emosi dasar manusia. Proses pengenalan emosi ini memer-\nlukan 3 buah perangkat keras, yaitu Muse 2 Headband sebagai perangkat EEG, Smartphone sebagai media transmisi \ndata dan Laptop/Komputer untuk menjalankan aplikasi EER. Aplikasi EER menerapkan Machine Learning dengan \nAlgoritma Gradient Boosting Classifier. Skor akurasi dari algoritma ini mencapai 92% pada tahap training.",font=customtk.CTkFont(size=15,weight='normal'),justify="left")
abparagraph.grid(row=1,column=0,pady=(10,0),padx=20,columnspan=2)

lbpengembang=customtk.CTkLabel(about_frame,text="Pengembang:",font=customtk.CTkFont(size=15,weight='bold'),justify="left")
lbpengembang.grid(row=2,column=0,pady=(20,0),padx=(0,0),sticky="ew")

lbpembimbing=customtk.CTkLabel(about_frame,text="Pembimbing:",font=customtk.CTkFont(size=15,weight='bold'),justify="left")
lbpembimbing.grid(row=2,column=1,pady=(20,0),padx=(0,0),sticky="ew")

fotopengembang=customtk.CTkLabel(about_frame,text="",image=safrizal_image)
fotopengembang.grid(row=3,column=0,pady=(10,0),padx=(0,0),sticky="ew")
fotopembimbing=customtk.CTkLabel(about_frame,text="",image=pakfatchul_image)
fotopembimbing.grid(row=3,column=1,pady=(10,0),padx=(0,0),sticky="ew")

namapengembang=customtk.CTkLabel(about_frame,text="Safrizal")
namapengembang.grid(row=4,column=0,pady=(10,0),padx=(0,0),sticky="ew")
namapembimbing=customtk.CTkLabel(about_frame,text="Dr. Ir. Fatchul Arifin, M.T")
namapembimbing.grid(row=4,column=1,pady=(10,0),padx=(0,0),sticky="ew")

prodilabel=customtk.CTkLabel(about_frame,text="Program Studi Pendidikan Teknik Elektronika dan Informatika",font=customtk.CTkFont(size=18,weight='normal'),justify="center")
prodilabel.grid(row=5,column=0,pady=(30,0),padx=0,columnspan=2)

footLabel=customtk.CTkLabel(about_frame,text="FAKULTAS TEKNIK SEKOLAH PASCASARJANA \n UNIVERSITAS NEGERI YOGYAKARTA \n TAHUN 2023",font=customtk.CTkFont(size=18,weight='bold'),justify="center")
footLabel.grid(row=6,column=0,pady=(20,0),padx=0,columnspan=2)
    
select_frame_by_name("home")
app.mainloop()

