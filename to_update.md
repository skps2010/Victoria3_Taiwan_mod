## commands
```bash
game_folder='/Users/phylla/Library/Application Support/Steam/steamapps/common/Victoria 3/game'
diff gfx/map/map_object_data/static.txt "$game_folder/gfx/map/map_object_data/static.txt"
diff gfx/map/map_object_data/generated_map_object_locators_wood.txt "$game_folder/gfx/map/map_object_data/generated_map_object_locators_wood.txt"
diff gfx/map/map_object_data/generated_map_object_locators_mine.txt "$game_folder/gfx/map/map_object_data/generated_map_object_locators_mine.txt"
diff gfx/map/map_object_data/generated_map_object_locators_port.txt "$game_folder/gfx/map/map_object_data/generated_map_object_locators_port.txt"
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

## common/history/pops/11_east_asia.txt
### s:STATE_FORMOSA
771c771
<                               size = 1470000
---
>                               size = 1480000
778,801c778,779
<                               culture = han # 南方人
<                               size = 490000
<                       }
<                       create_pop = {
<                               culture = hakka
<                               size = 270000
<                       }
<                       create_pop = {
<                               culture = yuanzhumin
<                               size = 470000
<                       }
<               }
<               region_state:FRI = {
<                       create_pop = {
<                               culture = han # 南方人
<                               size = 15000
<                       }
<                       create_pop = {
<                               culture = min
<                               size = 40000
<                       }
<                       create_pop = {
<                               culture = hakka
<                               size = 10000
---
>                               culture = han # nanfaren
>                               size = 815504
805c783
<                               size = 140000
---
>                               size = 600000