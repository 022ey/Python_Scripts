#! /usr/bin/bash

workspace_name=$1

if [[ $workspace_name == "^1" ]];then
    feh --bg-scale $HOME/Walls/firewatch.jpg & # -- dark firewatch theme
elif [[ $workspace_name == "^2" ]];then
    feh --bg-scale $HOME/Walls/sunset.jpg & # --sunset
elif [[ $workspace_name == "^3" ]];then
    feh --bg-scale $HOME/Walls/mountain.jpg & # -- mountain 
elif [[ $workspace_name == "^4" ]];then
    feh --bg-scale $HOME/Walls/desert.jpg & # -- desert
elif [[ $workspace_name == "^5" ]];then
    feh --bg-scale $HOME/Walls/clouds.jpg & # -- planet
else 
    feh --bg-scale $HOME/wallpapers/gruv_waifu.jpg & # -- gruv waifu
fi

bspc desktop -f $workspace_name

