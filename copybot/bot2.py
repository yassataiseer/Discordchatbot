import discord
from discord.ext import commands
import smtplib



client = commands.Bot(command_prefix= '.')

@client.event
async def on_ready():
    print("bot is ready,")

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("test@gmail.com", "password")
    server.sendmail(
        "test@gmail.com", 
        "test@gmail.com", 
        f"{member} has joined the server")
    print("done")

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server')
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("test@gmail.com", "test@gmail.com")
    server.sendmail(
        "test@gmail.com", 
        "test@gmail.com", 
        f"{member} has left the server")
    print("done")


client.run('yourid')



