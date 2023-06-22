import os
import asyncio

import discord
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands

from langchain import OpenAI

from ogbujipt.config import openai_emulation

load_dotenv()  # From .env file
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
PERMISSIONS_INTEGER = int(os.getenv('PERMISSIONS_INTEGER'))

LLM_HOST = os.getenv('LLM_HOST')
LLM_PORT = os.getenv('LLM_PORT')
LLM_TEMP = os.getenv('LLM_TEMP')

# Enable all standard intents, plus message content
# The bot app you set up on Discord will require this intent (Bot tab)
intents = discord.Intents.default()
intents.message_content = True

# initialize bot
# bot = discord.Client(
#     intents=intents, 
#     permissions=discord.Permissions(PERMISSIONS_INTEGER)
# )

bot = commands.Bot(
    intents=intents,
    command_prefix='/',
    description="Boss caluculator bot.")



@bot.event
async def on_ready():
    await bot.tree.sync()
    print("Bot Online!")


class Boss:
    '''
    Makes a class for a boss with a name and 3 attacks
    Hints the name of the boss as a string with the first letter capitalized
    This is so that the user can type in all lowercase and still see good formatting
    Hints each attack as an integer
    '''
    def __init__(
            self, 
            name="raidboss", 
            attack1=50000, 
            attack2=20000, 
            attack3=100000
            ):
        self.name: str = name.capitalize()
        self.attack1: int = attack1
        self.attack2: int = attack2
        self.attack3: int = attack3

    # later i'll add rounding up/down depending on what ffxiv damage formula 
    # wants
    def multiply_attack1(self, buff=1.0):
        self.attack1 = int(self.attack1 * buff)

    def list_details(self):
        print(self.name + ": first attack  " + str(self.attack1))
        print(self.name + ": second attack " + str(self.attack2))
        print(self.name + ": third attack  " + str(self.attack3))

# Wanna add a save function
boss_list = {}


@bot.tree.command(name="nothing", description="does nothing")
async def nothing(interaction: discord.Interaction):
    print("no lol")

@bot.tree.command(name="add_boss", description="adds a boss profile")
async def add_boss(
        interaction: discord.Interaction, 
        name: str, 
        attack1: int, 
        attack2: int, 
        attack3: int
        ):
    global boss_list

    await interaction.response.defer()

    new_boss = Boss(name, attack1, attack2, attack3)

    new_boss.list_details()

    await interaction.edit_original_response(
        content=f'New boss {new_boss.name} created with attacks '\
        f'{str(new_boss.attack1)}, '\
        f'{str(new_boss.attack2)}, and '\
        f'{str(new_boss.attack3)}'
        )
    
    boss_list[name] = new_boss


@bot.tree.command(name="player_debuff", description="adds a player debuff")
async def player_debuff(
        interaction: discord.Interaction, 
        name: str, 
        player_debuff: float, 
        ):
        global boss_list

        await interaction.response.defer()

        await interaction.edit_original_response(
            content=f'`Modifying {boss_list[name].name} `'
            )
        
        await interaction.channel.send(
            f'{boss_list[name].name} started with attacks '\
            f'{str(boss_list[name].attack1)}, '\
            f'{str(boss_list[name].attack2)}, and '\
            f'{str(boss_list[name].attack3)}'
            )

        boss_list[name].multiply_attack1(player_debuff)

        await interaction.channel.send(
            f'{boss_list[name].name} now has attacks '\
            f'{str(boss_list[name].attack1)}, '\
            f'{str(boss_list[name].attack2)}, and '\
            f'{str(boss_list[name].attack3)}'
            )


  
def main():
    global llm  # Ick! Ideally should be better scope/context controlled

    # Set up API connector
    openai_emulation(host=LLM_HOST, port=LLM_PORT)
    llm = OpenAI(temperature=LLM_TEMP)

    # launch Discord client event loop
    asyncio.get_event_loop().create_task(bot.run(token=DISCORD_TOKEN))


if __name__ == '__main__':
    main()
