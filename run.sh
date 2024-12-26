echo "Welcome to Advent of Code 2024"
echo "--------------------------------"
sleep 3

echo "Downloading input"
echo "Make sure to have the SESSION_TOKEN to the config.json file"
echo "Or input the session token manually in the download.py file"
echo "For more information, follow the README.md file"
python download.py
echo "Input downloaded"
echo "--------------------------------"

total_time=0
for i in {15..25}
do
    echo "Day $i"
    start_time=$(date +%s)
    python day$i.py
    end_time=$(date +%s)
    time_diff=$((end_time-start_time))
    total_time=$((total_time+time_diff))
    echo "Day $i took $time_diff seconds"
    echo "--------------------------------"
done

sleep 3
echo "All days completed"
echo "Total time: $(($total_time / 60)) minutes and $(($total_time % 60)) seconds"
echo "--------------------------------"

sleep 3
echo "Merry Christmas!"
echo "--------------------------------"