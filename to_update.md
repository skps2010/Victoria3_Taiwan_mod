## commands
```bash
game_folder='/Users/phylla/Library/Application Support/Steam/steamapps/common/Victoria 3/game'
diff gfx/map/map_object_data/static.txt "$game_folder/gfx/map/map_object_data/static.txt"
diff gfx/map/map_object_data/generated_map_object_locators_wood.txt "$game_folder/gfx/map/map_object_data/generated_map_object_locators_wood.txt"
diff gfx/map/map_object_data/generated_map_object_locators_mine.txt "$game_folder/gfx/map/map_object_data/generated_map_object_locators_mine.txt"
diff gfx/map/map_object_data/generated_map_object_locators_port.txt "$game_folder/gfx/map/map_object_data/generated_map_object_locators_port.txt"
diff localization/english/hub_names_l_english.yml "$game_folder/localization/english/hub_names_l_english.yml"
diff common/history/pops/11_east_asia.txt "$game_folder/common/history/pops/11_east_asia.txt"
```

## gfx/map/map_object_data/generated_map_object_locators_port.txt
### id=510
                      position={ 6835.833496 0.000000 2043.235962 }
                      rotation={ -0.000000 -0.571706 -0.000000 0.820459 }
---
                      position={ 6856.365234 0.000000 2040.339233 }
                      rotation={ -0.000000 0.472607 -0.000000 0.881274 }

## gfx/map/map_object_data/generated_map_object_locators_mine.txt
### id=510
                      position={ 6854.577637 0.000000 2082.012695 }
---
                      position={ 6841.034668 0.000000 2038.723389 }

## gfx/map/map_object_data/generated_map_object_locators_wood.txt
### id=510
                      position={ 6840.074707 0.000000 2056.493652 }
---
                      position={ 6837.329102 0.000000 2049.902344 }

## gfx/map/map_object_data/static.txt
### name="seagull_01" 
6833.085938 0.000000 2044.983398 0.000000 0.000000 0.000000 1.000000 1.000000 1.000000 1.000000
---
6859.128906 0.000000 2043.496582 0.000000 0.000000 0.000000 1.000000 1.000000 1.000000 1.000000

## localization/english/hub_names_l_english.yml
 HUB_NAME_STATE_FORMOSA_city:0 "Taipak"
 HUB_NAME_STATE_FORMOSA_port:0 "Tailam"
 HUB_NAME_STATE_FORMOSA_mine:0 "Sintik"
 HUB_NAME_STATE_FORMOSA_farm:0 "Tsionghua"
 HUB_NAME_STATE_FORMOSA_wood:0 "Kagi"
---
 HUB_NAME_STATE_FORMOSA_city:0 "Taipei"
 HUB_NAME_STATE_FORMOSA_port:0 "Taitung"
 HUB_NAME_STATE_FORMOSA_mine:0 "Kaohsiung"
 HUB_NAME_STATE_FORMOSA_farm:0 "Taichung"
 HUB_NAME_STATE_FORMOSA_wood:0 "Tainan"

## localization/simp_chinese/hub_names_l_simp_chinese.yml
取自正體中文模組，並改：
 HUB_NAME_STATE_FORMOSA_city:0 "臺北 Tâi-pak"
 HUB_NAME_STATE_FORMOSA_port:0 "臺南 Tâi-lâm"
 HUB_NAME_STATE_FORMOSA_mine:0 "新竹 Sin-tik"
 HUB_NAME_STATE_FORMOSA_farm:0 "彰化 Tsiong-huà"
 HUB_NAME_STATE_FORMOSA_wood:0 "嘉義 Ka-gī"

## common/history/pops/11_east_asia.txt
### s:STATE_FORMOSA
				size = 1708362
			}
			create_pop = {
				culture = manchu
				size = 492
			}
			create_pop = {
				culture = han # 南方人
				size = 499472
			}
			create_pop = {
				culture = hakka
				size = 280145
			}
			create_pop = {
				culture = formosan
				size = 239837
			}
		}
		region_state:FRI = {
			create_pop = {
				culture = han # 南方人
				size = 11462
			}
			create_pop = {
				culture = min
				size = 42483
			}
			create_pop = {
				culture = hakka
				size = 10701
			}
			create_pop = {
				culture = formosan
				size = 129837
---
				size = 1880000
			}
			create_pop = {
				culture = manchu
				size = 492
			}
			create_pop = {
				culture = han # nanfaren
				size = 1015504