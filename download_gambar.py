import ssl
import urllib.request
import time
import datetime
import os
import winsound


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

folder = str(tanggal)
currnet_dir = os.getcwd() ; print(f"current dir {currnet_dir}")
os.mkdir({tanggal}) ; print(f"folder {tanggal} sudah dibuat")
os.chdir(fr'{currnet_dir}\{tanggal}') ; print(f"Pindah ke directory {currnet_dir}\{tanggal}")

# print(f"hari ini tanggal {xs}")
opener = urllib.request.URLopener()
opener.addheader('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36')
def program1(tanggal,tanggal2):
    j = ['08','14','20']
    for jam1 in j:
        ifs = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/prakiraan/Backup/RAIN/rainrate_ifs0p125_sfc_" + tanggal + jam1 + "0000.png"
        # print(ifs)
        try:
            opener.retrieve(ifs, fr'F:\KANTOR\gambar\ifs' + jam1 + '_' + tanggal + '.webp')
        except:
            print(fr"Sepertinya link IFS {tanggal}{jam1} salah, hub muhammad.alfaridzi@bmkg.go.id")

    jam02 = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/prakiraan/Backup/RAIN/rainrate_ifs0p125_sfc_" + tanggal2 + "020000.png"
    try:
        opener.retrieve(jam02, fr'F:\KANTOR\gambar\ifs' + "26" + '_' + tanggal + '.png')
    except:
        print(fr"Sepertinya link IFS 26_{tanggal} salah, hub muhammad.alfaridzi@bmkg.go.id")

    j2 = ['01','07','13','19']
    for jam2 in j2:
        wrf = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/wrf/prakiraan/RAIN/rainrate_wrf10km_sfc_" + tanggal + jam2 + "0000.png"
        # print(wrf)
        try:
            opener.retrieve(wrf, fr'F:\KANTOR\gambar\wrf' + jam2 + '_' + tanggal + '.png')
        except:
            print(fr"Sepertinya link wrf {tanggal}{jam2}, hub muhammad.alfaridzi@bmkg.go.id")

    angin = "https://web-meteo.bmkg.go.id//media/data/bmkg/Angin3000ft/Streamline_" + tanggal + "070000.jpg"
    satelit = "http://202.90.198.22/IMAGE/HIMA/H08_EH_Sulsel.png"
    sst = "http://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/Analisis/sst_anal_sea_dy.png"
    sstano = "http://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/Analisis/ssta_anal_sea_dy.png"
    ibf00 = "https://cdn.bmkg.go.id/MEWS/ibf/27_sulsel_00.png"
    ibf24 = "https://cdn.bmkg.go.id/DataMKG/MEWS/27_sulsel_24.png"
    ibf48 = "https://cdn.bmkg.go.id/DataMKG/MEWS/27_sulsel_48.png"

    try:
        opener.retrieve(angin, fr'F:\KANTOR\gambar\w_' + tanggal + '.jpg')
        opener.retrieve(sst, fr'F:\KANTOR\gambar\SST_' + tanggal + '.jpg')
        opener.retrieve(sstano, fr'F:\KANTOR\gambar\SSTANO_' + tanggal + '.jpg')
        opener.retrieve(ibf00, fr'F:\KANTOR\gambar\ibf00.jpg')
        opener.retrieve(ibf24, fr'F:\KANTOR\gambar\ibf24_KIRIM KE GRUP.jpg')
        opener.retrieve(ibf48, fr'F:\KANTOR\gambar\ibf48_KIRIM KE GRUP.jpg')
    except:
        print(color.BOLD + color.RED + "Angin " + tanggal + " gagal data belum tersedia" + color.END)

    try:
        opener.retrieve(satelit, fr'F:\KANTOR\gambar\Sulsel ' + sekarang + '.png')
    except:
        print(color.BOLD + color.RED + "Satelit gagal link salah tidak terdaftar" + color.END)


def program2(tanggal,tanggal2):
    directory = str(tanggal)
    os.mkdir(fr'F:\KANTOR\gambar\modelifs{directory}')
    os.mkdir(fr'F:\KANTOR\gambar\modelwrf{directory}')
    os.mkdir(fr'F:\KANTOR\gambar\esembeldanprobabilistic{directory}')

    #Rain Rate hourly
    j = ['08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23']
    for jam1 in j:
        ifs = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/prakiraan/Backup/RAIN/rainrate_ifs0p125_sfc_" + tanggal + jam1 + "0000.png"
        wrf = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/wrf/prakiraan/RAIN/rainrate_wrf10km_sfc_"+ tanggal + jam1 + "0000.png"
        try:
            opener.retrieve(ifs, fr'F:\KANTOR\gambar\modelifs{directory}\ifs' + jam1 + '_' + tanggal + '.png')
            opener.retrieve(wrf,fr'F:\KANTOR\gambar\modelwrf{directory}\wrf' + jam1 + '_' + tanggal + '.png')
        except:
            print(fr"Sepertinya link IFS atau wrf {tanggal}{jam1} ada yang salah, hub muhammad.alfaridzi@bmkg.go.id")

    xx = ['00', '01', '02', '03', '04', '05', '06', '07']
    for k in xx:
        jam02 = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/prakiraan/Backup/RAIN/rainrate_ifs0p125_sfc_" + tanggal2 + k + "0000.png"
        jam03 = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/wrf/prakiraan/RAIN/rainrate_wrf10km_sfc_" + tanggal + k + "0000.png"
        t = int(k) + 24
        t = str(t)
        try:
            opener.retrieve(jam02, fr'F:\KANTOR\gambar\modelifs{directory}\ifs' + t + '_' + tanggal + '.png')
            opener.retrieve(jam03, fr'F:\KANTOR\gambar\modelwrf{directory}\wrf' + k + '_' + tanggal + '.png')
        except:
            print(fr"Sepertinya link RR IFS atau wrf {tanggal}{k}, hub muhammad.alfaridzi@bmkg.go.id")

    #RH
    j = ['00', '03', '06', '09', '12', '15', '18', '21']
    for jam1 in j:
        lapisan = ["850", "700", "500"]
        for lapisan2 in lapisan:
            rhifs = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/prakiraan/Backup/RH/rh_ifs0p125_"+ lapisan2 + "mb_" + tanggal + jam1 + "0000.png"
            rhwrf = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/wrf/prakiraan/RH/rh_wrf10km_"+ lapisan2 + "mb_" + tanggal + jam1 + "0000.png"
            try:
                opener.retrieve(rhifs, fr'F:\KANTOR\gambar\modelifs{directory}\rhifs' + lapisan2 + "_" + jam1 + '_' + tanggal + '.png')
                opener.retrieve(rhwrf, fr'F:\KANTOR\gambar\modelwrf{directory}\rhwrf'  + lapisan2 + "_" + jam1 + '_' + tanggal + '.png')
            except:
                print(fr"Sepertinya link rh IFS atau wrf {tanggal}{jam1} lapisan {lapisan2}salah, hub muhammad.alfaridzi@bmkg.go.id")

    #indeks
    j = ['00', '03', '06', '09', '12', '15', '18', '21']
    for jam1 in j:
        indeks = ["KI", "LI", "SI"]
        for indeks2 in indeks:
            indeks3 = indeks2.lower()
            labilifs = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/ecmwf/prakiraan/Backup/"+indeks2+"/"+indeks3 +"_ifs0p125_sfc_" + tanggal + jam1 + "0000.png"
            labilifswrf = "https://web-meteo.bmkg.go.id//media/data/bmkg/mfy/wrf/prakiraan/"+indeks2+"/"+indeks3+"_wrf10km_sfc_" + tanggal + jam1 + "0000.png"
            try:
                opener.retrieve(labilifs,fr'F:\KANTOR\gambar\modelifs{directory}\IFS' + indeks2 + "_" + jam1 + '_' + tanggal + '.png')
                opener.retrieve(labilifswrf,fr'F:\KANTOR\gambar\modelwrf{directory}\WRF' + indeks2 + "_" + jam1 + '_' + tanggal + '.png')
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
    #         opener.retrieve(zz,fr'F:\KANTOR\gambar\{zz}_{tanggal}.png')
    #     except:
    #         print(fr"{zz} Belum ada ")

    uu = [poe20,poe10,poe24]
    for nn in uu:
        try:
            opener.retrieve(nn,fr'F:\KANTOR\gambar\esembeldanprobabilistic{directory}\{nn[61:93]}.png')
        except:
            print(fr"{nn} Belum ada ")

    yy = [emeanifs, emeangefs, emeanaccessgt]
    for nn in yy:
        try:
            opener.retrieve(nn,fr'F:\KANTOR\gambar\esembeldanprobabilistic{directory}\{nn[91:95]}.png')
        except:
            print(fr"{nn} Belum ada ")

    inawp = "https://web-meteo.bmkg.go.id//media/data/bmkg//inanwp//InaNWP_RR24hr_Indo_" + tanggal2 + "000000.png"
    try:
        opener.retrieve(inawp, fr'F:\KANTOR\gambar\inawp{tanggal2}.png')
    except:
        print(fr"Inawp belum ada Belum ada ")
while True:
    program1(tanggal,tanggal2)
    program2(tanggal, tanggal2)
    end = time.time() - start
    print(fr"Selesai dalam {end} detik")
    print(fr"Hasil download tersimpan di F:\KANTOR\gambar ")
    winsound.Beep(6000, 100)
    winsound.Beep(6000, 100)
    winsound.Beep(6000, 100)
    input("Tekan Enter ")
    break



