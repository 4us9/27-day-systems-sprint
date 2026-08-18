#! /bin/bash

city=Casablanca

#obtain weather info
#output the result to a file instead of the terminal
curl -s "wttr.in/$city?mT" --output weather_report 

#Next Step - Extract and load the required data
obs_temp=$(cat weather_report | grep '°C' | grep -Eo '[+-]?[0-9]+' | head -n 1)

echo "The current Temperature of $city: $obs_temp"

fc_temp=$(grep '°C' weather_report | grep -Eo '[+-]?[0-9]+' | head -n 13 | tail -n 1)
echo "The forecasted temperature for noon tomorrow for $city : $fc_temp C"

#Store the date now
day=$(TZ='Morocco/Casablanca' date +%d)
month=$(TZ='Morocco/Casablanca' date +%m)
year=$(TZ='Morocco/Casablanca' date +%Y)

record=$(echo -e "$year\t$month\t$day\t$fc_temp\t$obs_temp")
echo -e "$record" >> rx_poc.log

#Check time zone -- sub the difference to run it at their 12 noon time.
#date
#TZ='Africa/Casablanca' date

#Just job schedule it now using crontab