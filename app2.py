from tkinter import PhotoImage
import customtkinter as customtk
import os
from PIL import Image,ImageTk
from CTkMessagebox import CTkMessagebox

import threading
import time
import csv
import datetime

import pandas as pd
import pickle

from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import ThreadingOSCUDPServer

from library.EEG_generate_training_matrix import gen_training_matrix

customtk.set_appearance_mode("dark")
customtk.set_default_color_theme("blue")

# globalVariabel
nama=""
jenisKelamin=""
kelas=""
asalsekolah=""
emosi=""
strAnger=""
strJoy=""
strSad=""
strFear=""

namaFile='uji/uji-predict-0.csv'
ip="0.0.0.0"
port=5000
tp9=0
tp10=0
af7=0
af8=0
au=0

waktuRekam=10

app=customtk.CTk()
app.title("Emotion Electroencephalography Recognition")
app.geometry(f"{1150}x{620}")

#image
image_path=os.path.join(os.path.dirname(os.path.realpath(__file__)),"icon")
logo_small=customtk.CTkImage(Image.open(os.path.join(image_path,"eeg-icon-7.png")),size=(30,30))
home_image=customtk.CTkImage(Image.open(os.path.join(image_path,"home_light.png")),size=(18,18))
petunjuk_image=customtk.CTkImage(Image.open(os.path.join(image_path,"book.png")),size=(18,18))
emotion_image=customtk.CTkImage(Image.open(os.path.join(image_path,"emotion.png")),size=(18,18))
emotion1_image=customtk.CTkImage(Image.open(os.path.join(image_path,"emotion.png")),size=(25,25))
next_image=customtk.CTkImage(Image.open(os.path.join(image_path,"next-icon.png")),size=(18,18))
sine_wave_image=customtk.CTkImage(Image.open(os.path.join(image_path,"sine-waves-analysis.png")),size=(18,18))
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
    global nama,kelas,jenisKelamin,asalsekolah
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
        
def mulai():
    labelEmosi.configure(state=customtk.DISABLED)
    lbl0.configure(text="Emosi Takut: 0 %")
    lbl1.configure(text="Emosi Sedih: 0 %")
    lbl2.configure(text="Emosi Senang: 0 %")
    lbl3.configure(text="Emosi Marah: 0 %")
    
    pb0.set(0)
    pb1.set(0)
    pb2.set(0)
    pb3.set(0)
    
    btnPrediksi.configure(state=customtk.DISABLED,fg_color=('grey30','grey35'),text="Menunggu selama "+ str(waktuRekam) +" detik")
    thread=threading.Thread(target=fungsiBacaEEG)
    thread.start()
    checkThread(thread)
    
def checkThread(thread):
    if thread.is_alive():
        app.after(500,lambda:checkThread(thread))
    else:
        btnPrediksi.configure(state=customtk.NORMAL,text="Prediksi Emosi",fg_color=("#4387d6","#2e7ad1"))        

def fungsiBacaEEG():
    global listJoin
    listJoin=[]
    dispatcher=Dispatcher()
    dispatcher.map("/muse/eeg",eeg_handler)
    
    global server
    server=ThreadingOSCUDPServer((ip,port),dispatcher)
    print("Listening on UDP port "+str(port))
    
    threading.Thread(target=startServer).start()
    threading.Thread(target=writeCSV).start()
    time.sleep(waktuRekam)
    threading.Thread(target=stopServer).start()
    print("selesai rekam")
    try:
        print("Membuat Dataset")
        buatDataset()
        print("buat dataset berhasil")
        prediksi()
        print("prediksi berhasil")
    except:
        CTkMessagebox(title="Informasi", message="Terjadi Kesalahan, Silahkan Coba Lagi",icon="info")
       
    
def startServer():
    server.serve_forever(poll_interval=0.5)

def stopServer():
    server.shutdown()
    server.server_close()
    
def eeg_handler( address, *args):
    data=[]
    global tp9,tp10,af7,af8,au
    tp9,af7,af8,tp10,au=args
    
    timeStamps=time.time()
    data=list(args)
    data.insert(0,timeStamps)
    listJoin.append(data)
    
def writeCSV():
    fieldnames=["timestamps","tp9","af7","af8","tp10","right aux"]
    start=time.time()
    
    with open(namaFile,'w',newline='')as csvFile:
        csvWriter=csv.DictWriter(csvFile,fieldnames=fieldnames)
        csvWriter.writeheader()
    
    while True:
        # print(tp9,' ',af7,' ',af8,' ',tp10)
        if tp9!=0 and tp10!=0 and af7!=0 and af8!=0:
            
            with open(namaFile,'a',newline='') as csvFile:
                str_waktu=time.time()
                csvWriter=csv.DictWriter(csvFile,fieldnames=fieldnames)
                info={
                    "timestamps":str_waktu,
                    "tp9":tp9,
                    "af7":af7,
                    "af8":af8,
                    "tp10":tp10,
                    "right aux":au
                }
                
                csvWriter.writerow(info)
            time.sleep(0.0001)
            elapse=str_waktu-start
            print(elapse)
            if (elapse>=waktuRekam):
                break

def buatDataset():
    inputDirectory='uji/'
    outputFile='test.csv'
    gen_training_matrix(inputDirectory,outputFile,cols_to_ignore=-1)

def prediksi():
    modelName='modelGB1.sav'
    dataset=pd.read_csv('test.csv')
    dataset=dataset.dropna()
    header=dataset.columns[[54,659,657,66,358,478,2,870,526,145,138,90,558,590,147,142,124,918,62,643,141,55,359,650,723,436,525,427,102,645,871,732,917,286,498,542,428,63,360,873,284,543,648,65,0,1,355,562,39,429,262,133,550,97,332,538,844,729,605,136,945,131,425,798,53,216,46,641,91,730,868,726,477,794,285,128,215,553,10,731,353,773,865,292,856,489,283,348,220,134,61,533,139,214,279,135,127,640,265,426,610,932,411,14,606,867,534,218,208,602,561,552,129,654,171,554,45,611,653,89,524,494,551,859,805,37,405,854,876,589,476,639,701,845,490,263,270,591,651,608,935,724,125,9,777,921,636,267,50,722,100,497,101,711,779,356,939,846,778,60,361,725,527,599,272,714,720,213,790,700,864,51,793,863,277,785,132,866,556,948,872,559,848,219,362,541,333,780,563,352,597,707,281,188,644,357,784,335,717,288,204,774,52,287,424,266,800,781,334,922,734,947,38,719,721,874,423,340,772,144,434,637,652,98,944,194,539,776,668,795,797,796,716,140,861,103,860,607,337,609,665,260,926,646,3,775,788,638,211,363,555,143,433,940,146,88]]
    
    X=dataset[header]
    
    loadModel=pickle.load(open(modelName,'rb'))
    prediksi=loadModel.predict(X)
    print(prediksi)
    
    total=len(prediksi)
    print(total)
    anger=0
    joy=0
    sad=0
    fear=0
    
    
    for emosi in prediksi:
        if emosi == 'anger':
            anger +=1
        elif emosi == 'joy':
            joy +=1
        elif emosi =='sad':
            sad +=1
        elif emosi =='fear':
            fear +=1

    print("hitung emosi")
    lbl0.configure(text="Emosi Takut: "+str(int(fear/total*100))+" %")
    lbl1.configure(text="Emosi Sedih: "+str(int(sad/total*100))+"%")
    
    lbl2.configure(text="Emosi Senang: "+str(int(joy/total*100))+"%")
    
    lbl3.configure(text="Emosi Marah: "+str(int(anger/total*100))+"%")
    
    global strFear,strAnger,strJoy,strSad
    strFear=str(int(fear/total*100))+" %"
    strAnger=str(int(anger/total*100))+"%"
    strJoy=str(int(joy/total*100))+"%"
    strSad=str(int(sad/total*100))+"%"
    print("set text selesai")
    
    pb0.set(fear/total)
    pb1.set(sad/total)
    pb2.set(joy/total)
    pb3.set(anger/total)
    print("set progress bar selesai")
    
    data={'anger':anger,'joy':joy,'sad':sad,'fear':fear}
    ser=pd.Series(data=data,index=['anger','joy','sad','fear'])
    print ("buat data")
    print(ser)
    # kesimpulan
    emosiKesimpulan=ser.idxmax()        
    print(emosiKesimpulan)
    
    if emosiKesimpulan=='anger':
        emosi_image=customtk.CTkImage(Image.open(os.path.join(image_path,"anger.png")),size=(198,150))
    elif emosiKesimpulan=='joy':
        emosi_image=customtk.CTkImage(Image.open(os.path.join(image_path,"joy.png")),size=(198,150))
    elif emosiKesimpulan=='sad':
        emosi_image=customtk.CTkImage(Image.open(os.path.join(image_path,"sad.png")),size=(198,150))
    elif emosiKesimpulan=='fear':
        emosi_image=customtk.CTkImage(Image.open(os.path.join(image_path,"fear.png")),size=(198,150))
        
    global labelEmosi
    labelEmosi=customtk.CTkLabel(tesEmosi_frame,image=emosi_image)
    labelEmosi.grid(row=12,column=0,pady=10)
    simpanDataCSV(emosiKesimpulan)
    
    
def simpanDataCSV(emosi):
    with open('dataemosi.csv','a',newline='')as f:
        writer=csv.writer(f,lineterminator='\n')
        data=[datetime.datetime.now(),nama,jenisKelamin,kelas,asalsekolah,strAnger,strFear,strJoy,strSad,emosi]
        writer.writerow(data)


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

btnMulai= customtk.CTkButton(home_frame, text="Deteksi Emosi",height=50,width=200,corner_radius=0,font=customtk.CTkFont(weight="bold",size=14),command=isidata_frame_btn_event,image=emotion1_image,compound="left")
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
namaInput=customtk.CTkEntry(isiData_frame,placeholder_text="cth. Budi Syahputra",width=200)
namaInput.grid(row=1,column=1,pady=10,padx=0,sticky="w")

jenisKelaminLabel=customtk.CTkLabel(isiData_frame,text="Jenis Kelamin:",font=customtk.CTkFont(size=15,weight='normal'))
jenisKelaminLabel.grid(row=2,column=0,pady=10,padx=30,sticky="e")
jenisKelaminInput=customtk.CTkComboBox(isiData_frame,values=["Laki-Laki","Perempuan"],width=200)
jenisKelaminInput.grid(row=2,column=1,pady=10,padx=0,sticky="w")

kelasLabel=customtk.CTkLabel(isiData_frame,text="Kelas:",font=customtk.CTkFont(size=15,weight='normal'))
kelasLabel.grid(row=3,column=0,pady=10,padx=30,sticky="e")
kelasInput=customtk.CTkEntry(isiData_frame,placeholder_text="cth. X RPL 1", width=200)
kelasInput.grid(row=3,column=1,pady=10,padx=0,sticky="w")

sekolahLabel=customtk.CTkLabel(isiData_frame,text="Asal Sekolah:",font=customtk.CTkFont(size=15,weight='normal'))
sekolahLabel.grid(row=4,column=0,pady=10,padx=30,sticky="e")
sekolahInput=customtk.CTkEntry(isiData_frame,placeholder_text="cth. SMKN 1 Karang Baru",width=200)
sekolahInput.grid(row=4,column=1,pady=10,padx=0,sticky="w")


btnMulai= customtk.CTkButton(isiData_frame, text="Selanjutnya",image=next_image, compound="right",corner_radius=0,width=110,command=deteksiemosi_frame_btn_event)
btnMulai.grid(row=6,column=1,sticky="w",padx=0,pady=30)


#frametesEmosi
tesEmosi_frame=customtk.CTkFrame(app,corner_radius=0,fg_color="transparent")
tesEmosi_frame.grid_columnconfigure(0,weight=1)

teLabel=customtk.CTkLabel(tesEmosi_frame,text="Prediksi Emosi",font=customtk.CTkFont(size=20,weight='bold'))
teLabel.grid(row=0,column=0,pady=20,padx=30,sticky="ew")

labelPetunjuk1=customtk.CTkLabel(tesEmosi_frame,text="1.Untuk memprediksi Emosi, tekan tombol Prediksi",font=customtk.CTkFont(size=15,weight='normal'))
labelPetunjuk1.grid(row=1,column=0,padx=(30,0),pady=(0,5),sticky="w")
labelPetunjuk2=customtk.CTkLabel(tesEmosi_frame,text="2.Mohon jangan terlalu banyak menggerakkan kepala, karena akan mengganggu sinyal yang direkam.",font=customtk.CTkFont(size=15,weight='normal'))
labelPetunjuk2.grid(row=2,column=0,padx=(30,0),pady=(0,5),sticky="w")

btnPrediksi= customtk.CTkButton(tesEmosi_frame, text="Prediksi Emosi",image=sine_wave_image, compound="left",corner_radius=0,width=100,command=mulai)
btnPrediksi.grid(row=3,column=0,padx=0,pady=(15,5))

labelEmosi=customtk.CTkLabel(tesEmosi_frame,text="")
lbl0=customtk.CTkLabel(tesEmosi_frame,text="Emosi Takut: 0%")
lbl0.grid(row=4,column=0,padx=(30,0),pady=(10,1), sticky="w")
pb0=customtk.CTkProgressBar(tesEmosi_frame,orientation="horizontal",width=900, height=15,mode="determinate",determinate_speed=.5)
pb0.grid(row=5,column=0,padx=(30,30),pady=0,sticky="w")
pb0.set(0)

lbl1=customtk.CTkLabel(tesEmosi_frame,text="Emosi Sedih: 0%")
lbl1.grid(row=6,column=0,padx=(30,0),pady=(20,1), sticky="w")
pb1=customtk.CTkProgressBar(tesEmosi_frame,orientation="horizontal",width=900, height=15,mode="determinate",determinate_speed=.5)
pb1.grid(row=7,column=0,padx=(30,30),pady=0,sticky="w")
pb1.set(0)

lbl2=customtk.CTkLabel(tesEmosi_frame,text="Emosi Senang: 0%")
lbl2.grid(row=8,column=0,padx=(30,0),pady=(20,1), sticky="w")
pb2=customtk.CTkProgressBar(tesEmosi_frame,orientation="horizontal",width=900, height=15,mode="determinate",determinate_speed=.5)
pb2.grid(row=9,column=0,padx=(30,30),pady=0,sticky="w")
pb2.set(0)

lbl3=customtk.CTkLabel(tesEmosi_frame,text="Emosi Marah: 0%")
lbl3.grid(row=10,column=0,padx=(30,0),pady=(20,1), sticky="w")
pb3=customtk.CTkProgressBar(tesEmosi_frame,orientation="horizontal",width=900, height=15,mode="determinate",determinate_speed=.5)
pb3.grid(row=11,column=0,padx=(30,30),pady=0,sticky="w")
pb3.set(0)



#frameAbout
about_frame=customtk.CTkFrame(app,corner_radius=0,fg_color="transparent")
about_frame.grid_columnconfigure(0,weight=1)
about_frame.grid_columnconfigure(1,weight=1)

alabel=customtk.CTkLabel(about_frame,text="Tentang Aplikasi",font=customtk.CTkFont(size=20,weight='bold'))
alabel.grid(row=0,column=0,pady=20,padx=30,sticky="ew",columnspan=2)

abparagraph=customtk.CTkLabel(about_frame,text="Aplikasi Electroencephalography Emotion Recognition (EER) adalah aplikasi yang dikembangkan untuk mengenali\nemosi pada peserta didik berdasarkan gelombang Elektro Ensefalografi (EEG) yang diterima oleh perangkat untuk\ndinalisa dan diklasifikasikan kedalam salah satu dari 4 emosi dasar manusia. Proses pengenalan emosi ini memer-\nlukan 3 buah perangkat keras, yaitu Muse 2 Headband sebagai perangkat EEG, Smartphone sebagai media transmisi \ndata dan Laptop/Komputer untuk menjalankan aplikasi EER. Aplikasi EER menerapkan Machine Learning dengan \nAlgoritma Gradient Boosting Classifier.",font=customtk.CTkFont(size=15,weight='normal'),justify="left")
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

