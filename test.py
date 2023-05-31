my_male = '''Mayaw #Amis 陳鏞基
		Yohani #Bunun 尤哈尼·伊斯卡卡夫特
		Uong'e #Cou 高一生
		Anguu #Hla'alua 謝垂耀
		Kilash #Thau 石阿松
		Danapan #Puyuma 孫大川
		Mona #Seediq 莫那·魯道
		Taiban #Drekay 台邦·撒沙勒
		Tahas #SaySiyat 打赫史·達印·改擺刨
		Bokeh #Truku 徐詣帆
		Uliw #Paiwan 簡東明
		Siaman #Tao 夏曼·藍波安
		Tiway #Sakizaya 帝瓦伊·撒耘'''.replace('\t', '').replace('\'', '').split('\n')
my_male = list(map(lambda d: d.split()[0], my_male))
my_female = '''Baqah #Kebalan 潘金榮
		Yungai #Atayal 溫嵐
		Apu'u #Kanakanavu 阿布娪‧卡阿斐依亞那
		Kuhap #Amis
		Pinaz #Bunun
		Apu'u #Cou
		Inguru #Hla'alua
		Shapzay #Thau
		Ainuay #Puyuma
		Robaw #Seediq
		Daremedeme #Drekay
		Kawkel #SaySiyat
		Miing #Truku'''.replace('\t', '').replace('\'', '').split('\n')
my_female = list(map(lambda d: d.split()[0], my_female))
my_common = '''Ciru #Amis
		Isqaqavut #Bunun
		Yatauyungana #Cou
		Siqeyu #Kebalan
		Hiilala #Hla'alua
		Shiqatafatu #Thau
		Paelabang #Puyuma
		Rudo #Seediq
		Sasala #Drekay
		Kaybaybaw #SaySiyat
		Hayung #Atayal
		Kosang #Truku
		Kaaviana #Kanakanavu
		Qaljupayare #Paiwan
		Rapongan #Tao
		Sayion #Sakizaya'''.replace('\t', '').replace('\'', '').split('\n')
my_common = list(map(lambda d: d.split()[0], my_common))
real_male = 'Alizu Attun Suniuo Baqah Bokeh Kilash Maraos Mona Paelabang Pelin Rapongan Sorong Tahas Taiban Uyongu Walis WaLiSsu Yohani YuKan Yungai Toril Botel Tawu Kanas Difang'.split(
)
real_female = 'Giwas Mavivo Sorong Mona Tain Hulijun Sumay Kacaw Mayaw Biho Peishan Xinyi Panai Kusui Ado Kalitiang Pacidal Jiahui Gewas Mevevo Iami Igay'.split(
)
real_common = 'Shiqatafu Hayung Rudao Kosang Pacidal Tuwana Ciro Kaybaybaw Isqaqavut Yatauyungana Siqeya Qaljupayare Sasala Danapan SiNan SiApenKotan SiAman Ryuzo Tao Thao Palalin Kociang'.split(
)

i = 0
j = 0
for p in my_male:
    print(p, p in real_male, p in real_female)
    if p in real_male:
        i += 1
    if p in real_female:
        j += 1
print(f'{i}/{len(my_male)} {j}/{len(my_male)}')

i = 0
j = 0
for p in my_female:
    print(p, p in real_female)
    if p in real_male:
        i += 1
    if p in real_female:
        j += 1
# print(f'{i}/{len(my_female)} {j}/{len(my_female)}')

i = 0
for p in my_common:
    # print(p, p in real_common)
    if p in real_common:
        i += 1

print(f'{i}/{len(my_common)}')
