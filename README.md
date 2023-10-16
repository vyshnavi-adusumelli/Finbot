<hr>

![MIT license](https://img.shields.io/badge/License-MIT-green.svg)
![GitHub](https://img.shields.io/github/languages/top/vyshnavi-adusumelli/FinBot?color=red&label=Python&logo=Python&logoColor=yellow)
![GitHub contributors](https://img.shields.io/github/contributors/vyshnavi-adusumelli/FinBot)
[![DOI](https://zenodo.org/badge/431190543.svg)](https://zenodo.org/badge/latestdoi/431190543)
[![Platform](https://img.shields.io/badge/Platform-Telegram-blue)](https://desktop.telegram.org/)
[![codecov](https://codecov.io/gh/vyshnavi-adusumelli/FinBot/branch/main/graph/badge.svg?token=YCKWZTHO7O)](https://app.codecov.io/gh/vyshnavi-adusumelli/FinBot/)
[![Actions Status](https://github.com/vyshnavi-adusumelli/FinBot/workflows/CI/badge.svg)](https://github.com/vyshnavi-adusumelli/FinBot/actions)
![github workflow](https://github.com/vyshnavi-adusumelli/FinBot/actions/workflows/black.yml/badge.svg)
![Discord](https://img.shields.io/discord/879343473940107264?color=blueviolet&label=Discord%20Discussion%20Chat)
![Lines of code](https://img.shields.io/tokei/lines/:provider/:user/https%3A%2F%2Fgithub.com%2Fvyshnavi-adusumelli%2FFinBot)
![Version](https://img.shields.io/github/v/release/vyshnavi-adusumelli/FinBot?color=ff69b4&label=Version)
![GitHub issues](https://img.shields.io/github/issues-raw/vyshnavi-adusumelli/FinBot)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/vyshnavi-adusumelli/FinBot)

<hr>

# FinBot - Because your financial future deserves the best!

You wake up, brew a fresh cup of coffee, and start your day. You're excited because today is the day you take control of your finances like never before. How? Say hello to FinBot, your ultimate financial companion. With simple commands, it transforms your financial story into one of motivation, empowerment, and control. 

And the best part? FinBot is your multi-platform financial sidekick, available on both Discord and Telegram. That means no matter where you are, it's there to assist you in recording your expenses seamlessly.
<hr>
<p align="center">
<a><img width=500 
  src="https://png.pngtree.com/png-clipart/20230824/original/pngtree-chatbot-messenger-banking-services-isometric-composition-with-personal-financial-manager-providing-budget-expenses-solutions-vector-illustration-picture-image_8372509.png" ></a>
</p>
<hr>

## Demo Video

https://youtu.be/NBihyIU13pw

## :money_with_wings: About FinBot

FinBot is a user-friendly Telegram and Discord bot designed to simplify your daily expense recording on a local system effortlessly. By offering the bot on two popular messaging platforms, we tap into a larger and diverse user base, increasing the potential reach of the service and enhancing user experience. 
<p align="center">
<a><img width=500 
  src="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs/262018288/original/8676cd7fe4b730618bfd1ca4886465ca5d148708/do-telegram-or-discord-bot-for-you.jpg" ></a>
</p>


With simple commands, this bot allows you to:

📝 **Add/Record a new spending:** As you sip that morning coffee, effortlessly log your expenses, no matter how small or significant. Every expense adds up, and FinBot ensures you don't miss a thing.

💡 **Display your expenditure for the current day/month:** With FinBot, you're never in the dark about your spending. Get real-time insights on your daily and monthly expenses, motivating you to stay on budget and crush your financial goals.

🔍 **Show your spending history:** Ever wondered where your money disappears to? FinBot provides a detailed spending history that tells a story of your financial habits. It's a tale of lessons and opportunities for improvement.

🗑️ **Delete/Erase all your records:** Made an error or just want to start afresh? It's as simple as a command, a chance to correct your narrative without any hassle.

🔧 **Edit/Change any spending details:** Life is full of surprises, and sometimes expenses change. FinBot adapts with you, offering easy editing options to keep your story accurate.

📊 Set Your Budget: Take full control of your finances by defining and tracking your budget with FinBot. It's the proactive step that puts you firmly in the driver's seat of your financial journey.

📈 **Visualize your spendings:** Numbers can be daunting, but FinBot transforms them into a captivating visual experience. Use the '/chart' option to see your spending as graphs and pie charts. This punchline to your story helps you spot trends and make smarter financial choices.

# :star: What's New??

### Release Version 1.2.1

- See your total daily/monthly expenditure in differet currencies using the /displayDifferentCurrency command
- Download your spendings history CSV file using the /download command
- Email the monthly spendings history to yourself using the /sendEmail command
- User can now get a message when the monthly budget is exhausted.
- Details for testing requirements added in README.md


### Release Version 1.2.0

- Visualize your spendings in the form of graphs
- The User can now see his expenses across various categories in the form of graphs along with pie charts.
- Just go on adding multiple spendings using /add and type /chart to see the spendings in the form of graphs.
- More Badges added in Repository




<!-- [comment]: <> (## Demo) -->

<!-- [comment]: <> (https://user-images.githubusercontent.com/15325746/135395315-e234dc5e-d891-470a-b3f4-04aa1d11ed45.mp4) -->



# :rocket: Installation Guide

## 💻For developers 
1. Install Python, atleast Python3

2. Clone this repository to your local system at a suitable directory/location of your choice

3. Start a terminal session, and navigate to the directory where the repo has been cloned

4. Run the following command to install the required dependencies:
```
  pip install -r requirements.txt
```
5. Ensure that you export the PYTHONPATH variable to the main project folder in the environment variables. This is essential for your Python scripts to locate and import the project modules correctly.

### Telegram Installation
1. Begin by downloading and installing the Telegram desktop application for your system from the official website: [Telegram Desktop](https://desktop.telegram.org/).

2.  Log in to your Telegram account. In the Telegram app, search for "BotFather." Click on "Start" to initiate a conversation with BotFather. Enter the following command: /newbot

3.  Follow the on-screen instructions to choose a name for your bot. After naming your bot, select a username for your bot, which should end with "bot" (as instructed in the Telegram interface).

4.  Once you've configured your bot, BotFather will confirm the creation and provide you with an API TOKEN. Copy this token for future use.

5.  In the Telegram app, search for your newly created bot by entering its username. Open the bot's chat to access its details.

6.  Right-click on the chat with your bot in the Telegram app. Copy the chat's ID as CHAT_ID for future reference.

7.  Set both the CHAT_ID and API_TOKEN as environment variables on your computer. These variables are essential for your bot to interact with Telegram.

8.  Open your terminal and navigate to the project's root folder. Run the command: ```python src/TeleBot.py``` in the terminal. A successful run will generate a message in your terminal, indicating that "TeleBot: Started polling."

9.  After a successful run, go to your bot on Telegram. Enter the "/start" or "/menu" command to initialize your bot, and you're all set to track your expenses!

### Discord Installation

1. Start by downloading and installing the Discord desktop application for your system from the following official website: [Discord Download](https://discord.com/download).

2. Visit the [Discord Developer Portal](https://discord.com/developers/applications) and create a new application. Follow the steps in this guide to create your Discord bot: [Creating Your First Bot](https://guide.pycord.dev/getting-started/creating-your-first-bot).

3. Give your bot a unique name and customize its avatar. Important: Ensure that your bot's name does not include "Discord." Applications with "Discord" in their name may not function correctly.

4. Once you've created your bot, it will be provided with a DISCORD_TOKEN. Make sure to copy this token as you'll need it later.

5. From the Discord Developer Portal, configure your bot with the necessary permissions and rights. This ensures it can interact with servers and channels.

6. Create a server on Discord where your bot will operate. Inside this server, create a dedicated channel for your bot. Copy the CHANNEL_ID of this channel for future reference.

7. Set the DISCORD_TOKEN and CHANNEL_ID as environment variables on your computer. These variables will be used by your bot to connect to the correct server and channel.

8. Open your terminal and navigate to the project's root folder. Run the command: ```python src/DiscordBot.py``` in the terminal. A successful run will generate a message in your terminal, indicating that "Shard ID None has connected to Gateway."

9. After a successful connection, go to your bot on Discord and enter the "#menu" command. Your bot is now ready to track your expenses!

## Testing with Pytest

1. Ensure that all necessary environment variables are correctly set on your computer. These variables are crucial for the functioning of your bot and test environment:

    - DISCORD_TOKEN: Your Discord bot's token.
    - CHANNEL_ID: The ID of the Discord channel your bot operates in.
    - API_TOKEN: The API token for your Telegram bot.
    - CHAT_ID: The ID of the chat where your Telegram bot operates.
    - PYTHONPATH: Set the PYTHONPATH variable to the main project folder. This helps your Python scripts locate and import project modules correctly.

2. Navigate to the FinBot/test/unit folder in your project directory. In your terminal, run the following command:
```
  python -m pytest
```
  After running the tests, you should see a summary indicating the number of test failures and passes.

# :information_desk_person: Sample Demos

### Budget

I want to increase/decrease my monthly budget.

<p align="center"><img width="700" src="./docs/workflows/budget.gif"></p>

1. Enter the `/budget` command
2. Enter the new budget amount (must be greater than 0)


### Add

I just spent money and want to mark it as a transaction! 

<p align="center"><img width="700" src="./docs/workflows/add.gif"></p>

1. Enter the `/add` command
2. Click on the date of the transaction
3. Click on the category to add
4. Type in the amount spent

### Delete

Oh no! I entered a transaction but want to delete it! 

<p align="center"><img width="700" src="./docs/workflows/delete.gif"></p>

1. Enter the `/delete` command
2. Based on how many records you want to delete..
   1. Per day: enter the day to delete
   2. Per month: enter the month to delete
   3. All: enter All
3. The records will be display. Enter YES to confirm, or NO to cancel

### Edit

Oh no! I entered a transaction but entered the wrong category! 

<p align="center"><img width="700" src="./docs/workflows/edit.gif"></p>

1. Enter the `/edit` command
2. Specify the date, category, and value of the transaction
3. Specify what part of the transaction to edit (either date, category, or value)
4. Enter in a new value

### Adding transactions from CSV and displaying chart

I want to add transactions from a CSV my bank gave me, and visalize my spendings

<p align="center"><img width="700" src="./docs/workflows/csv_vis.gif"></p>


1. Drag the .csv file into the telegram chat, and press send
2. For each transaction, classify the category
   1. The application will remember these mappings
3. Enter the `/chart` command

### Download History

I want a CSV file of all my transactions.

<p align="center"><img width="700" src="./docs/workflows/download.gif"></p>

1. Make sure you have a transaction history.
2. Enter the `/download` command.
3. A CSV file will be sent with your history.

### See total Expenditure in different currencies

I want to convert my total daily or monthly expenditure in a different currency.

<p align="center"><img width="700" src="./docs/workflows/currencyWorking.gif"></p>

1. Enter the /displayDifferentCurrency command
2. Choose from the category of day or month
3. Next, Choose your currency from the options
4. You will get the converted price in that currency


### Visualization in the form of graphs

I want to see my spendings in the form of graphs

<p align="center"><img width="700" src="./docs/workflows/multipleVisualizations.gif"></p>

1. Make sure you have a transaction history.
2. Enter the `/chart` command.
3. You will see multiple visualizations for your spending 

### SendEmail 

I want to send myself an email for the monthly expenditure


<p align="center"><img width="700" src="./docs/workflows/email.gif"></p>

1. Make sure you have a transaction history.
2. Enter the `/sendEmail` command.
3. Type the intended email address
4. You will get an email with the history file as attachment

# :grey_question: Documentation

Thorough documentation of all methods and classes can be found at [Github Pages](https://mtkumar123.github.io/MyDollarBot/)

# :construction: Road Map

Our ideas for new features that can be implemented to make this project better can be seen in our RoadMap project board.
[Road Map](https://github.com/secheaper/slashbot/projects/1)



:heart: Acknowledgements
---
We would like to thank Dr. Timothy Menzies for helping us understand the process of building a good Software Engineering project. We would also like to thank the teaching assistants Xiao Ling, Andre Lustosa, Kewen Peng, Weichen Shi for their support throughout the project.


:page_facing_up: License
---
This project is licensed under the terms of the MIT license. Please check [License](https://github.com/secheaper/slashbot/blob/main/LICENSE) for more details.


:sparkles: Contributors
---

<table>
  <tr>
    <td align="center"><a href="http://www.shubhammankar.com/"><img src="https://avatars.githubusercontent.com/u/29366125?v=4" width="75px;" alt=""/><br /><sub><b>Shubham Mankar</b></sub></a></td>
    <td align="center"><a href="https://github.com/pratikdevnani"><img src="https://avatars.githubusercontent.com/u/43350493?v=4" width="75px;" alt=""/><br /><sub><b>Pratik Devnani</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/moksh98"><img src="https://avatars.githubusercontent.com/u/29693765?v=4" width="75px;" alt=""/><br /><sub><b>Moksh Jain</b></sub></a><br /></td>
    <td align="center"><a href="https://rahilsarvaiya.tech/"><img src="https://avatars0.githubusercontent.com/u/32304956?v=4" width="75px;" alt=""/><br /><sub><b>Rahil Sarvaiya</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/annie0467"><img src="https://avatars.githubusercontent.com/u/17164255?v=4" width="75px;" alt=""/><br /><sub><b>Anushi Keswani</b></sub></a><br /></td>
  </tr>
</table>



# :calling: Support

For any support, email us at mydollarbot@gmail.com/ secheaper@gmail.com
