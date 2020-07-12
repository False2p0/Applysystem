import discord
from discord_webhook import DiscordWebhook

client = discord.Client()

@client.event
async def on_ready():
    print('Logged on as', format(client.user.name))
    client.loop.create_task(status_task())
    print("Bot started")
   
@client.event
@client.event
async def on_message(message,):
    if message.author.bot:
        return
        
    if message.content.startswith("!bewerben"):
        await message.channel.send("Der Bot schickt dir eine Nachricht")
        await message.author.send("**Wie bewerbe ich mich** \n  *§ Discordnamen  Eigenen text mit angaben zu über dich z.B Name, Alter und warum du bei uns Supporter werden wilst.* \n \n Wen du keine antwort direkt vom Bot bekommst nachdem du deine Bewerbung abgeschickt hast überprüfe ob du das § davor geschrieben hast.")
        print(message.author, "Hat sich beworben ")

    if message.content.startswith("!apply"):
        Bewerbung = message.content
        bewerber = message.author
        print(Bewerbung, bewerber)
        await message.author.send("Danke für deine Bewerbung")

        webhook = DiscordWebhook(url="Webhook", content=Bewerbung)
        response = webhook.execute()

    client.run('token')
