import os
import discord
from discord.ext import commands

# ID do servidor para que o bot rode no server específico
id_do_servidor = 207972094489657344

# variável para prefixo padrão
prefix = "!"

# instância do bot com o prefixo e os intents
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.default())


# evento que é chamado quando o bot está pronto para usar
@bot.event
async def on_ready():
  print(f"Entramos como {bot.user}.")
  channel = bot.get_channel(id_do_servidor)
  await channel.send('hello')


# evento que é chamado quando uma mensagem é recebida
@bot.event
async def on_message(message):
  # Verifica se a mensagem foi enviada pelo próprio bot
  if message.author == bot.user:
    return

  # Verifica se a mensagem começa com o prefixo
  if message.content.startswith(prefix):
    await message.channel.send('Hello!')


# roda o bot usando a chave/token
bot.run(os.environ['chave_bot'])
