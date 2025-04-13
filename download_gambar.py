import ssl
import urllib.request
import time
import datetime
import os
import winsound
import shutil


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
sekarang = now.strftime('%d %B %Y jam %H.%M')

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

print(f"Current dir: {current_dir}")
if os.path.exists(folder_path):
    print(f"Folder {tanggal} sudah ada")
    shutil.rmtree(tanggal)
    print(f"Folder {tanggal} sudah dihapus")

print(f"Membuat folder {tanggal} baru")
os.mkdir(folder_path)
print(f"Folder {tanggal} sudah dibuat")

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
            filenameonly = os.path.basename(ifs)
            print(fr"Sedang Download {filenameonly}")
            opener.retrieve(ifs, fr'ifs' + jam1 + '_' + tanggal + '.webp')
            print(fr"ifs" + jam1 + '_' + tanggal + '.png' + " sudah di download")
        except:
            print(fr"Sepertinya link IFS {tanggal}{jam1} gagal di download")

    jam02 = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/prakiraan/Backup/RAIN/rainrate_ifs0p125_sfc_" + tanggal2 + "020000.png"
    try:
        filenameonly = os.path.basename(jam02)
        print(fr"Sedang Download {filenameonly}")
        opener.retrieve(jam02, fr'ifs' + "26" + '_' + tanggal + '.png')
        print(fr'ifs' + "26" + '_' + tanggal + '.webp' +  "sudah di download")
    except:
        print(fr"Sepertinya link IFS 26_{tanggal} gagal di download")
        
    j2 = ['01','07','13','19']
    for jam2 in j2:
        wrf = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/wrf/prakiraan/RAIN/rainrate_wrf10km_sfc_" + tanggal + jam2 + "0000.png"
        # print(wrf)
        try:
            filenameonly = os.path.basename(wrf)
            print(fr"Sedang Download {filenameonly}")
            opener.retrieve(wrf, fr'wrf' + jam2 + '_' + tanggal + '.png')
            print(fr'wrf' + jam2 + '_' + tanggal + '.png' + " sudah di download")
        except:
            print(fr"Sepertinya link wrf {tanggal}{jam2} gagal di download")

    angin = "https://web-meteo.bmkg.go.id//media/data/bmkg/Angin3000ft/Streamline_" + tanggal + "070000.jpg"
    satelit = "http://202.90.198.22/IMAGE/HIMA/H08_EH_Sulsel.png"
    sst = "http://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/Analisis/sst_anal_sea_dy.png"
    sstano = "http://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/Analisis/ssta_anal_sea_dy.png"
    ibf00 = "https://cdn.bmkg.go.id/MEWS/ibf/27_sulsel_00.png"
    ibf24 = "https://cdn.bmkg.go.id/DataMKG/MEWS/27_sulsel_24.png"
    ibf48 = "https://cdn.bmkg.go.id/DataMKG/MEWS/27_sulsel_48.png"

    try:
        opener.retrieve(angin, fr'\w_' + tanggal + '.jpg')
        opener.retrieve(sst, fr'\SST_' + tanggal + '.jpg')
        opener.retrieve(sstano, fr'\SSTANO_' + tanggal + '.jpg')
        opener.retrieve(ibf00, fr'\ibf00.jpg')
        opener.retrieve(ibf24, fr'\ibf24_KIRIM KE GRUP.jpg')
        opener.retrieve(ibf48, fr'\ibf48_KIRIM KE GRUP.jpg')
    except:
        print(color.BOLD + color.RED + "Angin " + tanggal + " gagal data belum tersedia" + color.END)

    try:
        opener.retrieve(satelit, fr'\Sulsel ' + sekarang + '.png')
    except:
        print(color.BOLD + color.RED + "Satelit gagal link salah tidak terdaftar" + color.END)


def program2(tanggal,tanggal2):
    directory = str(tanggal)
    os.mkdir(fr'\modelifs{directory}')
    os.mkdir(fr'\modelwrf{directory}')
    os.mkdir(fr'\esembeldanprobabilistic{directory}')

    #Rain Rate hourly
    j = ['08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
    for jam1 in j:
        ifs = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/prakiraan/Backup/RAIN/rainrate_ifs0p125_sfc_" + tanggal + jam1 + "0000.png"
        wrf = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/wrf/prakiraan/RAIN/rainrate_wrf10km_sfc_"+ tanggal + jam1 + "0000.png"
        try:
            opener.retrieve(ifs, fr'\modelifs{directory}\ifs' + jam1 + '_' + tanggal + '.png')
            opener.retrieve(wrf,fr'\modelwrf{directory}\wrf' + jam1 + '_' + tanggal + '.png')
        except:
            print(fr"Sepertinya link IFS atau wrf {tanggal}{jam1} gagal di download")

    xx = ['00', '01', '02', '03', '04', '05', '06', '07']
    for k in xx:
        jam02 = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/prakiraan/Backup/RAIN/rainrate_ifs0p125_sfc_" + tanggal2 + k + "0000.png"
        jam03 = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/wrf/prakiraan/RAIN/rainrate_wrf10km_sfc_" + tanggal + k + "0000.png"
        t = int(k) + 24
        t = str(t)
        try:
            opener.retrieve(jam02, fr'\modelifs{directory}\ifs' + t + '_' + tanggal + '.png')
            opener.retrieve(jam03, fr'\modelwrf{directory}\wrf' + k + '_' + tanggal + '.png')
        except:
            print(fr"Sepertinya link RR IFS atau wrf {tanggal}{k} gagal di download")

    #RH
    j = ['00', '03', '06', '09', '12', '15', '18', '21']
    for jam1 in j:
        lapisan = ["850", "700", "500"]
        for lapisan2 in lapisan:
            rhifs = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/prakiraan/Backup/RH/rh_ifs0p125_"+ lapisan2 + "mb_" + tanggal + jam1 + "0000.png"
            rhwrf = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/wrf/prakiraan/RH/rh_wrf10km_"+ lapisan2 + "mb_" + tanggal + jam1 + "0000.png"
            try:
                opener.retrieve(rhifs, fr'\modelifs{directory}\rhifs' + lapisan2 + "_" + jam1 + '_' + tanggal + '.png')
                opener.retrieve(rhwrf, fr'\modelwrf{directory}\rhwrf'  + lapisan2 + "_" + jam1 + '_' + tanggal + '.png')
            except:
                print(fr"Sepertinya link rh IFS atau wrf {tanggal}{jam1} lapisan {lapisan2}gagal di download")

    #indeks
    j = ['00', '03', '06', '09', '12', '15', '18', '21']
    for jam1 in j:
        indeks = ["KI", "LI", "SI"]
        for indeks2 in indeks:
            indeks3 = indeks2.lower()
            labilifs = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/prakiraan/Backup/"+indeks2+"/"+indeks3 +"_ifs0p125_sfc_" + tanggal + jam1 + "0000.png"
            labilifswrf = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/wrf/prakiraan/"+indeks2+"/"+indeks3+"_wrf10km_sfc_" + tanggal + jam1 + "0000.png"
            try:
                opener.retrieve(labilifs,fr'\modelifs{directory}\IFS' + indeks2 + "_" + jam1 + '_' + tanggal + '.png')
                opener.retrieve(labilifswrf,fr'\modelwrf{directory}\WRF' + indeks2 + "_" + jam1 + '_' + tanggal + '.png')
            except:
                print(f"indeks {indeks2} wrf jam {jam1} kosong")

    #probabilistic dan esembel model
    poe20 = "https://web-meteo.bmkg.go.id//media/data/bmkg/probabilistic//POE20_24hrprec_" + tanggal + "000000_ifs.png"
    poe10 = "https://web-meteo.bmkg.go.id//media/data/bmkg/probabilistic//POE10_24hrprec_" + tanggal + "000000_ifs.png"
    poe24 = "https://web-meteo.bmkg.go.id//media/data/bmkg/probabilistic//POE5_24hrprec_" + tanggal + "000000_ifs.png"
    emeanaccessgt = "https://web-meteo.bmkg.go.id//media/data/bmkg/probabilistic//Emean_24hrprec_" + tanggal + "000000_accessgt.png"
    emeangefs = "https://web-meteo.bmkg.go.id//media/data/bmkg/probabilistic//Emean_24hrprec_" + tanggal + "000000_gefs.png"
    emeanifs = "https://web-meteo.bmkg.go.id//media/data/bmkg/probabilistic//Emean_24hrprec_" + tanggal + "000000_ifs.png"

    # bom850_00= "http://www.bom.gov.au/charts_data/IDY20108/current/RH/850hPa/IDY20108.RH-850hPa.012.png?1716465600"
    # bom850_12 = "http://www.bom.gov.au/charts_data/IDY20108/current/RH/850hPa/IDY20108.RH-850hPa.024.png?1716465600"
    # bom700_00= "http://www.bom.gov.au/charts_data/IDY20108/current/RH/700hPa/IDY20108.RH-700hPa.012.png?1716465600"
    # bom700_12 = "http://www.bom.gov.au/charts_data/IDY20108/current/RH/700hPa/IDY20108.RH-700hPa.024.png?1716465600"
    # bom500_00= "http://www.bom.gov.au/charts_data/IDY20108/current/RH/500hPa/IDY20108.RH-500hPa.024.png?1716465600"
    # bom500_12 = "http://www.bom.gov.au/charts_data/IDY20108/current/RH/500hPa/IDY20108.RH-500hPa.012.png?1716465600"
    #
    # bom = [bom500_00, bom500_12, bom700_12, bom700_00, bom850_12, bom850_00]
    # for zz in bom:
    #     try:
    #         opener.retrieve(zz,fr'\{zz}_{tanggal}.png')
    #     except:
    #         print(fr"{zz} Belum ada ")

    uu = [poe20,poe10,poe24]
    for nn in uu:
        try:
            opener.retrieve(nn,fr'\esembeldanprobabilistic{directory}\{nn[ta]}.png')
        except:
            print(fr"{nn} Belum ada ")

    yy = [emeanifs, emeangefs, emeanaccessgt]
    for nn in yy:
        try:
            opener.retrieve(nn,fr'\esembeldanprobabilistic{directory}\{nn[91:95]}.png')
        except:
            print(fr"{nn} Belum ada ")

    inawp = "https://web-meteo.bmkg.go.id//media/data/bmkg//inanwp//InaNWP_RR24hr_Indo_" + tanggal2 + "000000.png"
    try:
        opener.retrieve(inawp, fr'\inawp{tanggal2}.png')
    except:
        print(fr"Inawp belum ada Belum ada ")
while True:
    program1(tanggal,tanggal2)
    program2(tanggal, tanggal2)
    end = time.time() - start
    print(fr"Selesai dalam {end} detik")
    winsound.Beep(6000, 100)
    winsound.Beep(6000, 100)
    winsound.Beep(6000, 100)
    input("Tekan Enter untuk membuka folder")
    os.startfile(fr"{currnet_dir}\{tanggal}")
    break



