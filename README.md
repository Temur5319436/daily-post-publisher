# daily-post-publisher

## Overview

The project designed to automate the process of publishing videos to Instagram.

This package utilizes the aiogram library for the project's admin panel, which communicates with a Telegram bot for managing and configuring the daily video publishing.


## Features

- Scheduled publishing of videos to Instagram using cron jobs.
- Integration with the Telegram API through aiogram for the admin panel.
- Easy configuration and customization.

## Getting Started

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/usmonaliyev/daily-post-publisher.git

cd daily-post-publisher
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Configure the bot:

- Create a new Telegram bot on [BotFather](https://t.me/BotFather).
- Create a new Instagram account on [Instagram](https://instagram.com).
- Obtain the bot token and login and password of instagram account.
- Copy the provided environment variable template:

```bash
cp .env.example .env
```

4. Open the .env file and replace variables with the actual variables.

```bash
TELEGRAM_BOT_TOKEN=<YOUR_TELEGRAM_BOT_TOKEN>

INSTAGRAM_USERNAME=<YOUR_INSTAGRAM_USERNAME>
INSTAGRAM_PASSWORD=<YOUR_INSTAGRAM_PASSWORD>
```

### Usage

1. Run the bot:

```bash
python main.py
```

2. Load videos to the server via the admin panel.

3. View the stored videos using the `/videos` command in the Telegram bot.

4. Add videos to the daily videos list using the admin panel. The bot will move the added videos to the `assets/daily` folder for scheduled publishing.


### Setting up Linux Crontab

To schedule the execution of the bot at specific intervals, you can use the Linux crontab. Open the crontab editor by running:

```bash
crontab -e
```

Add the following line to run the bot script every day at a specified time (replace /path/to/project and python3 with the actual path to your project and Python executable):

```bash
0 0 * * * cd /path/to/project && /usr/bin/python3 daily.py
```

The daily.py script will publish the videos from the assets/daily folder to the Instagram account.

This example schedules the daily.py script to run daily at midnight. Adjust the timing according to your requirements.
Save the crontab file, and the script will be executed automatically at the scheduled time.

### Setup project with systemd

* [Setup a python script as a service through systemctl/systemd](https://medium.com/codex/setup-a-python-script-as-a-service-through-systemctl-systemd-f0cc55a42267)

### License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).
