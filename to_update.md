## commands
```bash
game_folder='/Users/umi/Library/Application Support/Steam/steamapps/common/Victoria 3/game'
diff gfx/map/map_object_data/generated_map_object_locators_port.txt "$game_folder/gfx/map/map_object_data/generated_map_object_locators_port.txt"
diff gfx/map/map_object_data/generated_map_object_locators_mine.txt "$game_folder/gfx/map/map_object_data/generated_map_object_locators_mine.txt"
diff gfx/map/map_object_data/generated_map_object_locators_wood.txt "$game_folder/gfx/map/map_object_data/generated_map_object_locators_wood.txt"
diff gfx/map/map_object_data/static.txt "$game_folder/gfx/map/map_object_data/static.txt"
diff common/history/pops/11_east_asia.txt "$game_folder/common/history/pops/11_east_asia.txt"
```

## gfx/map/map_object_data/generated_map_object_locators_port.txt
### id=510
                      position={ 6835.833496 0.000000 2043.235962 }
                      rotation={ -0.000000 -0.571706 -0.000000 0.820459 }
---
                      position={ 6837.620117 0.000000 2037.625000 }
                      rotation={ -0.000000 -0.573658 -0.000000 0.819096 }

## gfx/map/map_object_data/generated_map_object_locators_mine.txt
### id=510
                      position={ 6854.577637 0.000000 2082.012695 }
---
                      position={ 6869.879395 0.000000 2092.781738 }

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
980c980
<                               size = 470000
---
>                               size = 480000
988c988
<                               size = 367500
---
>                               size = 605504
993,1026c993
<                               size = 122500
<                       }
<                       create_pop = {
<                               culture = hakka
<                               size = 202500
<                       }
<                       create_pop = {
<                               culture = hakka
<                               religion = mahayana
<                               size = 67500
<                       }
<                       create_pop = {
<                               culture = yuanzhumin
<                               size = 470000
<                       }
<               }
<               region_state:FRI = {
<                       create_pop = {
<                               culture = han # 南方人
<                               size = 11250
<                       }
<                       create_pop = {
<                               culture = han # 南方人
<                               religion = mahayana
<                               size = 3750
<                       }
<                       create_pop = {
<                               culture = min
<                               size = 30000
<                       }
<                       create_pop = {
<                               culture = min
<                               religion = mahayana
<                               size = 10000
---
>                               size = 215504
1029,1037d995
<                               culture = hakka
<                               size = 7500
<                       }
<                       create_pop = {
<                               culture = hakka
<                               religion = mahayana
<                               size = 2500
<                       }
<                       create_pop = {
1039c997
<                               size = 140000
---
>                               size = 600000