#MAKE SURE TO PUT YOUR BOT TOKEN AT THE BOTTOM

import discord
import random
import asyncio

allchamp = ["Aatrox","Ahri","Akali","Alistar","Amumu","Anivia","Annie","Aphelios","Ashe","Aurelion Sol","Azir","Bard","Blitzcrank","Brand","Braum","Caitlyn","Camille","Cassiopeia","ChoGath","Corki","Darius","Diana","Dr. Mundo","Draven","Ekko","Elise","Evelynn","Ezreal","Fiddlesticks","Fiora","Fizz","Galio","Gangplank","Garen","Gnar","Gragas","Graves","Hecarim","Heimerdinger","Illaoi","Irelia","Ivern","Janna","Jarvan IV","Jax","Jayce","Jhin","Jinx","KaiSa","Kalista","Karma","Karthus","Kassadin","Katarina","Kayle","Kayn","Kennen","KhaZix","Kindred","Kled","KogMaw","LeBlanc","Lee Sin","Leona","Lissandra","Lucian","Lulu","Lux","Malphite","Malzahar","Maokai","Master Yi","Miss Fortune","Mordekaiser","Morgana","Nami","Nasus","Nautilus","Neeko","Nidalee","Nocturne","Nunu and Willump","Olaf","Orianna","Ornn","Pantheon","Poppy","Pyke","Qiyana","Quinn","Rakan","Rammus","RekSai","Renekton","Rengar","Riven","Rumble","Ryze","Sejuani","Senna","Sett","Shaco","Shen","Shyvana","Singed","Sion","Sivir","Skarner","Sona","Soraka","Swain","Sylas","Syndra","Tahm Kench","Taliyah","Talon","Taric","Teemo","Thresh","Tristana","Trundle","Tryndamere","Twisted Fate","Twitch","Udyr","Urgot","Varus","Vayne","Veigar","VelKoz","Vi","Viktor","Vladimir","Volibear","Warwick","Wukong","Xayah","Xerath","Xin Zhao","Yasuo","Yorick","Yuumi","Zac","Zed","Ziggs","Zilean","Zoe","Zyra"]
top1 = ["Aatrox","Camille","ChoGath","Darius","Dr. Mundo","Fiora","Gangplank","Garen","Gnar","Illaoi","Irelia","Jax","Jayce","Kayle","Kennen","Kled","Malphite","Maokai","Mordekaiser","Nasus","Olaf","Ornn","Pantheon","Poppy","Quinn","Renekton","Riven","Rumble","Ryze","Sett","Shen","Singed","Sion","Teemo","Trundle","Tryndamere","Urgot","Vladimir","Volibear","Wukong","Yorick"]
top2 = ["Akali","Cassiopeia","Diana","Ekko","Fizz","Galio","Gragas","Hecarim","Heimerdinger","Jarvan IV","Karma","Lissandra","Lucian","Master Yi","Nautilus","Rengar","Swain","Sylas","Vayne","Yasuo"]
top3 = ["Alistar","Amumu","Annie","Blitzcrank","Braum","Elise","Janna","Kalista","Kayn","KhaZix","Lee Sin","Leona","Lulu","Morgana","Nunu and Willump","Rammus","Sejuani","Senna","Shaco","Shyvana","Skarner","Sona","Soraka","Tahm Kench","Taric","Udyr","Vi","Warwick","Xin Zhao","Zac","Zyra"]
top4 = top1 + top2 + top3
jg1 = ["Amumu","Diana","Dr. Mundo","Ekko","Elise","Evelynn","Fiddlesticks","Gragas","Graves","Hecarim","Ivern","Jarvan IV","Jax","Kayn","KhaZix","Kindred","Lee Sin","Master Yi","Nidalee","Nocturne","Nunu and Willump","Olaf","Pantheon","Rammus","RekSai","Rengar","Sejuani","Sett","Shaco","Shyvana","Skarner","Trundle","Tryndamere","Udyr","Vi","Volibear","Warwick","Wukong","Xin Zhao","Zac"]
jg2 = ["Aurelion Sol","Camille","ChoGath","Karthus","Kled","Maokai","Malphite","Mordekaiser","Nasus","Nautilus","Poppy","Rumble","Sion","Taliyah","Twitch"]
jg3 = ["Aatrox","Brand","Darius","Ezreal","Fizz","Galio","Garen","Kalista","Morgana","Qiyana","Renekton","Riven","Shen","Singed","Sylas","Syndra","Tahm Kench","Talon","Twisted Fate","Zed","Ziggs","Zilean"]
jg4 = jg1 + jg2 + jg3
mid1 = ["Ahri","Akali","Anivia","Annie","Aurelion Sol","Azir","Cassiopeia","Corki","Diana","Ekko","Fizz","Galio","Heimerdinger","Kassadin","Katarina","LeBlanc","Lissandra","Lux","Malzahar","Neeko","Orianna","Qiyana","Ryze","Sylas","Syndra","Taliyah","Talon","Twisted Fate","Veigar","VelKoz","Viktor","Vladimir","Xerath","Yasuo","Zed","Ziggs","Zilean","Zoe"]
mid2 = ["Aatrox","Brand","ChoGath","Ezreal","Gangplank","Gragas","Irelia","Jayce","Kalista","Karma","Karthus","Kayle","Kennen","Kled","KogMaw","Lucian","Lulu","Malphite","Mordekaiser","Morgana","Nautilus","Nocturne","Ornn","Pantheon","Pyke","Quinn","Renekton","Riven","Rumble","Sett","Shyvana","Sion","Swain","Teemo","Tristana","Varus","Wukong"]
mid3 = ["Amumu","Aphelios","Bard","Blitzcrank","Caitlyn","Camille","Dr. Mundo","Draven","Fiddlesticks","Fiora","Garen","Janna","Jarvan IV","Jhin","KaiSa","KhaZix","Lee Sin","Miss Fortune","Nasus","Nidalee","Olaf","Rakan","RekSai","Shaco","Sivir","Sona","Soraka","Twitch","Urgot","Vayne","Vi","Xayah","Zyra"]
mid4 = mid1 + mid2 + mid3
adc1 = ["Aphelios","Ashe","Caitlyn","Draven","Ezreal","Jhin","Jinx","KaiSa","Kalista","KogMaw","Lucian","Miss Fortune","Senna","Sivir","Tristana","Twitch","Varus","Vayne","Xayah"]
adc2 = ["Corki","Heimerdinger","Jayce","Kennen","Kindred","Neeko","Quinn","Veigar","Yasuo","Ziggs"]
adc3 = ["Ahri","Annie","Azir","Bard","Cassiopeia","Dr. Mundo","Fiddlesticks","Gnar","Irelia","LeBlanc","Lux","Nidalee","Skarner","Soraka","Syndra","Teemo","Thresh","Twisted Fate"]
adc4 = adc1 + adc2 + adc3
sup1 = ["Alistar","Bard","Blitzcrank","Brand","Braum","Janna","Karma","Leona","Lulu","Lux","Morgana","Nami","Nautilus","Pyke","Rakan","Senna","Sona","Soraka","Tahm Kench","Taric","Thresh","Yuumi","Zilean","Zoe","Zyra"]
sup2 = ["Amumu","Anivia","Annie","ChoGath","Fiddlesticks","Galio","Gragas","Malphite","Malzahar","Maokai","Ornn","Pantheon","Sett","Shaco","Shen","Sion","Swain","Trundle","Veigar","VelKoz","Volibear","Xerath","Zac",]
sup3 = ["Ahri","Camille","Darius","Dr. Mundo","Elise","Ivern","Jarvan IV","Lissandra","Nasus","Nunu and Willump","Poppy","Rammus","RekSai","Sejuani","Singed","Syndra","Taliyah","Twisted Fate","Udyr","Vi","Ziggs"]
sup4 = sup1 + sup2 + sup3
kev1 = ["Ziggs", "Zyra"]
kev2 = ["Ziggs", "Zyra"]
kev3 = ["Ziggs", "Zyra"]
kev4 = ["Ziggs", "Zyra"]

top = [top1, top2, top3, top4, allchamp]
jg = [jg1, jg2, jg3, top4, allchamp]
mid = [mid1, mid2, mid3, mid4, allchamp]
adc = [adc1, adc2, adc3, mid4, allchamp]
sup = [sup1, sup2, sup3, sup4, allchamp]
kevin = [kev1, kev2, kev3, kev4, allchamp]
lol = [top, jg, mid, adc, sup, kevin]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('$champ'):
            rrmain = True
            while rrmain:
                await message.channel.send('Role? (1 - Top, 2 - Jungle, 3 - Mid, 4 - ADC, 5 - Support, 6 - Kevin): ')

                try:
                    role = await self.wait_for('message', timeout=5.0)
                except asyncio.TimeoutError:
                    return await message.channel.send('Sorry, you took too long, go again.')

                rrspice = True
                while rrspice:
                    await message.channel.send(
                        'Spice level? (1 - None, 2 - Low, 3 - SPICE, 4 - Random Spice, 5 - Any Champion): ')

                    try:
                        spice = await self.wait_for('message', timeout=5.0)
                    except asyncio.TimeoutError:
                        return await message.channel.send('Sorry, you took too long, go again.')

                    rrchamp = True
                    while rrchamp:
                        length = len((lol[int(role.content) - 1][int(spice.content) - 1]))
                        a = random.randint(0, int(length - 1))
                        await message.channel.send("You are playing: " + lol[int(role.content) - 1][int(spice.content) - 1][a])
                        rrmain = False
                        rrspice = False
                        rrchamp = False

                        await message.channel.send("Do you want to reroll? [y/n]: ")

                        try:
                            rer = await self.wait_for('message', timeout=5.0)
                        except asyncio.TimeoutError:
                            return await message.channel.send('Sorry, you took too long, go again.')

                        if rer.content == "y":
                            await message.channel.send(
                                "Start over at 1 - Role, 2 - Spice, 3 - Just a new champion: ")

                            try:
                                rr = await self.wait_for('message', timeout=5.0)
                            except asyncio.TimeoutError:
                                return await message.channel.send('Sorry, you took too long, go again.')

                            if int(rr.content) == 1:
                                rrmain = True
                            elif int(rr.content) == 2:
                                rrspice = True
                            elif int(rr.content) == 3:
                                rrchamp = True
                        elif rer.content == "n":
                            await message.channel.send("GLHF")


client = MyClient()
client.run('INSERT YOUR BOT TOKEN HERE')