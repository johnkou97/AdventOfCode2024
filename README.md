# Advent Of Code 2024

This repository contains my solutions for the [Advent of Code 2024](https://adventofcode.com/2024) challenge challenge in **Python**.

![Advent of Code 2024](outputs/day14_easter_egg.png)
*Day 14: A nice easter egg generated from Day 14. The robots aligned perfectly to form a Christmas tree.*

## Advent of Code

Advent of Code is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in any programming language you like. People use them as a speed contest, interview prep, company training, university coursework, practice problems, or to challenge each other. The puzzles are released daily, and you can solve them at your own pace. You can find more information about the challenge on the [official website](https://adventofcode.com/).

## Story Arc

This year's story is about finding the missing Chief Historian in time for the the big Christmas sleigh launch, which he never misses. From the [Day 1 puzzle](https://adventofcode.com/2024/day/1):

> The Chief Historian is always present for the big Christmas sleigh launch, but nobody has seen him in months! Last anyone heard, he was visiting locations that are historically significant to the North Pole; a group of Senior Historians has asked you to accompany them as they check the places they think he was most likely to visit.

> As each location is checked, they will mark it on their list with a star. They figure the Chief Historian must be in one of the first fifty places they'll look, so in order to save Christmas, you need to help them get fifty stars on their list before Santa takes off on December 25th.

> Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

## Files
- `day[0-25].py`: Contains the solution for the respective day.
- `download.py`: Downloads the input for all days. For more instructions, keep reading.
- `run.sh`: Bash script to download the input and run the solution for all days.
- `outputs/`: Contains some output plots that I generated for some days.
- `README.md`: This file.

## Input Files

In Advent of Code, each day has its own input file. The input files are unique to each user, and you need to be logged in to download them. It is also forbidden to share the input files with others ([source](https://adventofcode.com/2024/about)). 

The input files are stored in the `inputs/` directory. The files are named `day[0-25].txt`, where `[0-25]` is the day number. The input files are not included in this repository, and you need to download them yourself. You can find more information on how to download the input files in the next section.

## Download the Input

To download the input for all days, you can run the following command:

```bash
python download.py
```

To download the input you will need your session cookie (session token). You can find this cookie in your browser after logging in to your account. The cookie is used to authenticate the request and download the input. If you don't know how to get the cookie, you can visit this [link](https://cookie-script.com/blog/chrome-cookies) for more information. After you find all the cookies, you need to find the one that is named `session` and copy its value.

You can pass the cookie directly in the script in the appropriate place, or you can store it in a `config.json` file. The file should look like this:

```json
{
    "SESSION_TOKEN": "your_session_token"
}
```

Please do not share your session token with anyone. The best practice is to store it in a safe place and use `.gitignore` to avoid uploading it to the repository. If you just want to run the code, you can pass the session token directly in the script.

If you do not want to use the script, you can download the input files manually from the [Advent of Code](https://adventofcode.com/2024) website. Please make sure to store the input files in the `inputs/` directory and name them `day[0-25].txt`.

## Requirements

The requirements are very minimal, and you probably already have them installed.

The code is written in **Python 3**. I used version `3.9.16`, but any version of Python 3 should work. The only external libraries used are `numpy` and `matplotlib`. Any version of these libraries should work.

## Run the Code

To run the code for all days, you can use the following command:

```bash
bash run.sh
```

This script will download the input and run the solution for all days. If you want to run the code for a specific day, you can run the following command:

```bash
python day1.py
```

This command will run the code for day 1. You can replace `day1.py` with any other day.

## Usage of LLMs and Code from the Internet

While solving the challenges, I tried to not use LLMs (Large Language Models) like GPT to generate the solutions. I also tried to not use code from others or find hints on the internet. I wanted to solve the challenges on my own, and I think that's the best way to learn and improve. However, I ended up using all of the above, when I got stuck on a couple of occasions. I tried to understand the code and the solution, and I learned a lot from it. I think this was a great learning experience, and I don't regret it as I expanded my knowledge and got to implement some cool algorithms. This follows the general rules of the challenge, as I was not competing for the leaderboard, and I was doing it for fun and learning ([source](https://adventofcode.com/2024/about)).

## Note

The purpose of this repository is to share my solutions for the Advent of Code challenge. The solutions are not always the most efficient or elegant, but they get the job done. This was a fun challenge, and I learned a lot of new things along the way. If you have any suggestions or improvements, feel free to open an issue or you can contact me directly.