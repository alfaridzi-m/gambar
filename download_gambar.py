import ssl
import urllib.request
import time
import datetime
import os
import winsound
import shutil
import requests
from gtts import gTTS
import playsound


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

now = datetime.datetime.now()
sekarang = now.strftime('%d %B %Y at %H:%M')

start =time.time()
print(f"{'Auto Download Gambar IFS,WRF,ANGIN,SATELIT!!'}")
print(f'Hari ini adalah tanggal {sekarang}')
print("Silahkan tunggu proses download gambar Model analisa")

tanggal = datetime.date.today().strftime('%Y%m%d')
xs = datetime.date.today() + datetime.timedelta(days=1)
tanggal2 = xs.strftime('%Y%m%d')
print("=====================================")
current_dir = os.getcwd()
folder_path = os.path.join(current_dir, tanggal)

print(f"Lokasi saat ini di : {current_dir}")
if os.path.exists(folder_path):
    print(f"Folder {tanggal} berhasil ada")
    shutil.rmtree(tanggal)
    print(f"Folder {tanggal} berhasil dihapus")

print(f"Membuat folder {tanggal} baru")
os.mkdir(folder_path)
print(f"Folder {tanggal} berhasil dibuat")

os.chdir(folder_path)
print(f"Pindah ke directory {folder_path}")


# print(f"hari ini tanggal {xs}")
opener = urllib.request.URLopener()
opener.addheader('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36')
opener.addheader('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')
opener.addheader('Accept-Language', 'en-US,en;q=0.5')

def program1(tanggal,tanggal2):
    j = ['08','14','20']
    for jam1 in j:
        ifs = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/prakiraan/Backup/RAIN/rainrate_ifs0p125_sfc_" + tanggal + jam1 + "0000.png"
        # print(ifs)
        try:
            filename = os.path.basename(ifs)
            filenamewithoutext = os.path.splitext(filename)[0]
            opener.retrieve(ifs, fr'{filenamewithoutext}'+'.png')
            print(f'{filenamewithoutext} berhasil di download ✅')
        except:
            print(fr"{filenamewithoutext} gagal di download Karena file {e} ❌" )

    jam02 = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/prakiraan/Backup/RAIN/rainrate_ifs0p125_sfc_" + tanggal2 + "020000.png"
    try:
        filename = os.path.basename(jam02)
        filenamewithoutext = os.path.splitext(filename)[0]
        opener.retrieve(jam02, fr'{filenamewithoutext}'+'.png')
        print(f'{filenamewithoutext} berhasil di download ✅')
    except:
        print(fr"{filenamewithoutext} gagal di download Karena file {e} ❌" )
        
    j2 = ['01','07','13','19']
    for jam2 in j2:
        wrf = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/wrf/prakiraan/RAIN/rainrate_wrf10km_sfc_" + tanggal + jam2 + "0000.png"
        # print(wrf)
        try:
            filename = os.path.basename(wrf)
            filenamewithoutext = os.path.splitext(filename)[0]
            opener.retrieve(wrf, fr'{filenamewithoutext}'+'.png')
            print(f'{filenamewithoutext} berhasil di download ✅')
        except Exception as e:
            print(fr"{filenamewithoutext} gagal di download Karena file {e} ❌" )

    angin = "https://web-meteo.bmkg.go.id//media/data/bmkg/Angin3000ft/Streamline_" + tanggal + "070000.jpg"
    satelit = "http://202.90.198.22/IMAGE/HIMA/H08_EH_Sulsel.png"
    sst = "http://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/Analisis/sst_anal_sea_dy.png"
    sstano = "http://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/Analisis/ssta_anal_sea_dy.png"

    # Loop through the list of URLs and download each file
    for url in [angin, satelit, sst, sstano]:
        try:
            filename = os.path.basename(url)
            response = requests.get(url, allow_redirects=True)
            filenamewithoutext = os.path.splitext(filename)[0]
            with open(filename, 'wb') as file:
                file.write(response.content)
            print(f'{filenamewithoutext} berhasil di download ✅')
        except Exception as e:
            print(fr"{filenamewithoutext} gagal di download Karena file {e} ❌" )

def bomfile():
	rh850_00= "http://www.bom.gov.au/charts_data/IDY20108/current/RH/850hPa/IDY20108.RH-850hPa.012.png"
	rh850_12 = "http://www.bom.gov.au/charts_data/IDY20108/current/RH/850hPa/IDY20108.RH-850hPa.024.png"
	rh700_00= "http://www.bom.gov.au/charts_data/IDY20108/current/RH/700hPa/IDY20108.RH-700hPa.012.png"
	rh700_12 = "http://www.bom.gov.au/charts_data/IDY20108/current/RH/700hPa/IDY20108.RH-700hPa.024.png"
	rh500_00= "http://www.bom.gov.au/charts_data/IDY20108/current/RH/500hPa/IDY20108.RH-500hPa.024.png"
	rh500_12 = "http://www.bom.gov.au/charts_data/IDY20108/current/RH/500hPa/IDY20108.RH-500hPa.012.png"
	rr_t12 = "http://www.bom.gov.au/charts_data/IDY20108/current/mslp-precip/IDY20108.mslp-precip.012.png"
	rr_t18 = "http://www.bom.gov.au/charts_data/IDY20108/current/mslp-precip/IDY20108.mslp-precip.018.png"
	rr_t24 = "http://www.bom.gov.au/charts_data/IDY20108/current/mslp-precip/IDY20108.mslp-precip.024.png"
	rr_t30 = "http://www.bom.gov.au/charts_data/IDY20108/current/mslp-precip/IDY20108.mslp-precip.030.png"

	# Loop through the list of BOM URLs and download each file
	for url in [rr_t12, rr_t18, rr_t24, rr_t30, rh850_00, rh850_12, rh700_00, rh700_12, rh500_00, rh500_12]:
		try:
			filename = os.path.basename(url)
			filenamewithoutext = os.path.splitext(filename)[0]
			opener.retrieve(url, fr'{filenamewithoutext}'+'.png')
			print(f'{filenamewithoutext} berhasil di download ✅')
		except Exception as e:
			print(fr"{filenamewithoutext} gagal di download Karena file {e} ❌" )

def program2(tanggal,tanggal2):
    directory = str(tanggal)
    os.mkdir(fr'{current_dir}\{tanggal}\modelifs{directory}')
    os.mkdir(fr'{current_dir}\{tanggal}\modelwrf{directory}')
    os.mkdir(fr'{current_dir}\{tanggal}\esembeldanprobabilistic{directory}')

    #Rain Rate hourly
    j = [f'{hour:02}' for hour in range(8, 24)]
    for jam1 in j:
        ifs = f"https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/prakiraan/Backup/RAIN/rainrate_ifs0p125_sfc_{tanggal}{jam1}0000.png"
        wrf = f"https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/wrf/prakiraan/RAIN/rainrate_wrf10km_sfc_{tanggal}{jam1}0000.png"
        try:
            filenameonlywrf = os.path.basename(wrf)
            filenamewithoutextwrf = os.path.splitext(filenameonlywrf)[0]
            opener.retrieve(wrf, fr"{current_dir}\{tanggal}\modelwrf{directory}\{filenamewithoutextwrf}" + '.png')
            print(fr"{filenamewithoutextwrf} berhasil di download ✅")
        except Exception as e:
            print(fr"{filenamewithoutextwrf} gagal di download Karena file {e} ❌" )
        
        try:
            filenameonlyifs = os.path.basename(ifs)
            filenamewithoutextifs = os.path.splitext(filenameonlyifs)[0]
            opener.retrieve(ifs, fr"{current_dir}\{tanggal}\modelifs{directory}\{filenamewithoutextifs}" + '.png')
            print(fr"{filenamewithoutextifs} berhasil di download ✅")
        except Exception as e:
            print(fr"{filenamewithoutextifs} gagal di download Karena file {e} ❌" )

    xx = [f'{hour:02}' for hour in range(8)]
    for k in xx:
        ifsxx = f"https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/prakiraan/Backup/RAIN/rainrate_ifs0p125_sfc_{tanggal2}{k}0000.png"
        wrfxx = f"https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/wrf/prakiraan/RAIN/rainrate_wrf10km_sfc_{tanggal}{k}0000.png"

        try:
            filenameonlywrf = os.path.basename(wrfxx)
            filenamewithoutextwrf = os.path.splitext(filenameonlywrf)[0]
            opener.retrieve(wrfxx, fr"{current_dir}\{tanggal}\modelwrf{directory}\{filenamewithoutextwrf}" + '.png')
            print(fr"{filenamewithoutextwrf} berhasil di download ✅")
        except Exception as e:            
            print(fr"{filenamewithoutextwrf} gagal di download Karena file {e} ❌" )
        
        try:
            filenameonlyifs = os.path.basename(ifsxx)
            filenamewithoutextifs = os.path.splitext(filenameonlyifs)[0]
            opener.retrieve(ifsxx, fr"{current_dir}\{tanggal}\modelifs{directory}\{filenamewithoutextifs}" + '.png')
            print(fr"{filenamewithoutextifs} berhasil di download ✅")
        except Exception as e:            
            print(fr"{filenamewithoutextifs} gagal di download Karena file {e} ❌" )

    #RH
    j =  ['00', '03', '06', '09', '12', '15', '18', '21']
    for jam1 in j:
        lapisan = ["850", "700", "500"]
        for lapisan2 in lapisan:
            rhifs = f"https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/prakiraan/Backup/RH/rh_ifs0p125_{lapisan2}mb_{tanggal}{jam1}0000.png"
            rhwrf = f"https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/wrf/prakiraan/RH/rh_wrf10km_{lapisan2}mb_{tanggal}{jam1}0000.png"
            try:
                filenameonlyifs = os.path.basename(rhifs)
                filenamewithoutextifs = os.path.splitext(filenameonlyifs)[0]
                opener.retrieve(rhifs, fr"{current_dir}\{tanggal}\modelifs{directory}\{filenamewithoutextifs}" + '.png')
                print(fr"{filenamewithoutextifs} berhasil di download ✅")
            except Exception as e:
                print(fr"{filenamewithoutextifs} gagal di download Karena file {e} ❌" )
            try:
                filenameonlywrf = os.path.basename(rhwrf)
                filenamewithoutextwrf = os.path.splitext(filenameonlywrf)[0]
                opener.retrieve(rhwrf, fr"{current_dir}\{tanggal}\modelwrf{directory}\{filenamewithoutextwrf}" + '.png')
                print(fr"{filenamewithoutextwrf} berhasil di download ✅")
            except Exception as e:
                print(fr"{filenamewithoutextwrf} gagal di download Karena file {e} ❌" )

    #indeks
    j = ['00', '03', '06', '09', '12', '15', '18', '21']
    for jam1 in j:
        indeks = ["KI", "LI", "SI"]
        for indeks2 in indeks:
            indeks3 = indeks2.lower()
            labilifs = f"https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/prakiraan/Backup/{indeks2}/{indeks3}_ifs0p125_sfc_{tanggal}{jam1}0000.png"
            labilifswrf = f"https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/wrf/prakiraan/{indeks2}/{indeks3}_wrf10km_sfc_{tanggal}{jam1}0000.png"
            try:
                filenameonlyifs = os.path.basename(labilifs)
                filenamewithoutextifs = os.path.splitext(filenameonlyifs)[0]
                opener.retrieve(labilifs, fr"{current_dir}\{tanggal}\modelifs{directory}\{filenamewithoutextifs}" + '.png')
                print(fr"{filenamewithoutextifs} berhasil di download ✅")
            except Exception as e:
                print(fr"{filenamewithoutextifs} gagal di download Karena file {e} ❌" )
            try:
                filenameonlywrf = os.path.basename(labilifswrf)
                filenamewithoutextwrf = os.path.splitext(filenameonlywrf)[0]
                opener.retrieve(labilifswrf, fr"{current_dir}\{tanggal}\modelwrf{directory}\{filenamewithoutextwrf}" + '.png')
                print(fr"{filenamewithoutextwrf} berhasil di download ✅")
            except Exception as e:
                print(fr"{filenamewithoutextwrf} gagal di download Karena file {e} ❌" )

    #probabilistic dan esembel model
    poe20 = f"https://web-meteo.bmkg.go.id//media/data/bmkg/probabilistic//POE20_24hrprec_{tanggal}000000_ifs.png"
    poe10 = f"https://web-meteo.bmkg.go.id//media/data/bmkg/probabilistic//POE10_24hrprec_{tanggal}000000_ifs.png"
    poe5 = f"https://web-meteo.bmkg.go.id//media/data/bmkg/probabilistic//POE5_24hrprec_{tanggal}000000_ifs.png"
    emeanaccessgt = f"https://web-meteo.bmkg.go.id//media/data/bmkg/probabilistic//Emean_24hrprec_{tanggal}000000_accessgt.png"
    emeangefs = f"https://web-meteo.bmkg.go.id//media/data/bmkg/probabilistic//Emean_24hrprec_{tanggal}000000_gefs.png"
    emeanifs = f"https://web-meteo.bmkg.go.id//media/data/bmkg/probabilistic//Emean_24hrprec_{tanggal}000000_ifs.png"

    uu = [poe20,poe10,poe5]
    for nn in uu:
        try:
            filenameonly = os.path.basename(nn)
            filenamewithoutext = os.path.splitext(filenameonly)[0]
            opener.retrieve(nn, fr"{current_dir}\{tanggal}\esembeldanprobabilistic{directory}\{filenamewithoutext}" + '.png')
            print(fr"{filenamewithoutext} berhasil di download ✅")
        except Exception as e:            
            print(fr"{filenamewithoutext} gagal di download Karena file {e} ❌" )

    yy = [emeanifs, emeangefs, emeanaccessgt]
    for nn in yy:
        try:
            filenameonly = os.path.basename(nn)
            filenamewithoutext = os.path.splitext(filenameonly)[0]
            opener.retrieve(nn, fr"{current_dir}\{tanggal}\esembeldanprobabilistic{directory}\{filenamewithoutext}" + '.png')
            print(fr"{filenamewithoutext} berhasil di download ✅")
        except Exception as e:            
            print(fr"{filenamewithoutext} gagal di download Karena file {e} ❌" )

while True:
    print("=====================================")
    print("Proses download file yang diperlukan analisa")
    time.sleep(1)
    teks = fr"Program {sekarang} ended, press enter to open folder. Thank you"
    tts = gTTS(text=teks, lang='en', slow=False)
    tts.save("sukses.mp3")
    print("=====================================")
    program1(tanggal,tanggal2)
    print("File analisa telah selesai di download")
    print("=====================================")
    print("Proses download file tambahan")
    program2(tanggal, tanggal2)
    print("Selesai download file tambahan")
    time.sleep(1)
    print("=====================================")
    print("Proses download file BOM")
    bomfile()
    print("=====================================")
    print("Proses download file BOM telah selesai")
    end = time.time() - start
    print(fr"Selesai dalam {end} detik")
    winsound.Beep(6000, 100)
    winsound.Beep(6000, 100)
    winsound.Beep(6000, 100)
    playsound.playsound("sukses.mp3")
    print("=====================================")
    os.remove("sukses.mp3")
    input("Tekan Enter untuk membuka folder")
    os.chdir(current_dir)
    os.startfile(fr"{current_dir}\{tanggal}")
    break



