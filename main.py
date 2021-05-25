import discord
from discord.ext import commands


    
bot = commands.Bot(command_prefix = "#", description = "Bot GTA")
Objets={}
Objets["Pistolet SNS"] = 9
Objets["Calibre 50"] = 9
Objets["SNS Mk II"] = 3
Objets["Ceramic Pistol"] = 1
Objets["Micro Smg"] = 11
Objets["bidon d'essence"] = 3
Objets["Pistolet lourd"] = 1
Objets["Pistolet"] = 1
Objets["Clés de mentottes LSDP"] = 1
Objets["pistolet"] = 4
Objets["Chargeurs"] = 393

Objets["Feuille de coca"] = 560
Objets["Capsule de cocaïne"] = 939
Objets["Produits Pharmaceutiques"] = 868
Objets["Ecstasy"] = 435
Objets["Lysergamides"] = 1160
Objets["Capsule LSD-25"] = 966
Objets["Methylamine"] = 2025
Objets["Crystal Meth"] = 1459
Objets["Weed"] = 3668 
Objets["Pochon de Weed"] = 1003
Objets["Coke"] = 8
Objets["Pavots"] = 3129
Objets["Pochons d'opium"] = 2608
Objets["Kit carosserie"] = 26
Objets["Kit réparation"] = 133

Objets["Medikit"] = 41
Objets["Kevlar"] = 3 
Objets["Bandages"] = 4
Objets["Bouteille de gaz"] = 8
Objets["outil réparation"] = 5
Objets["chalumeau"] = 4
Objets["bijoux"] = 27

liste_objectifs=[1,2,3]
@bot.event
async def on_ready():
    print("On est la !")
    

@bot.command(name="Ajouter",aliases = ["ajouter","ajt","Ajt","+"])
async def Ajouter(ctx,quantité, *,objet):
    global Objets
    quantité = int(quantité)
    Objets[objet]+=quantité
    await ctx.send (f"{quantité} de {objet} bien ajoutée, il y a {Objets[objet]} {objet}")

@bot.command(name="Retirer",aliases = ["retirer","del","Del","-"])
async def Supprimer(ctx,quantité, *,objet):
    global Objets
    quantité = int(quantité)
    Objets[objet]-=quantité
    await ctx.send (f"{quantité} de {objet} bien retirée")



@bot.command(name="Voir",aliases = ["voir"])
async def Voir(ctx):
    global Objets
    await ctx.send(Objets)

@bot.command(name="sheeeesh",aliases = ["Sheeeesh"])
async def Sheesh(ctx):
    await ctx.send("Sheeeeeeeeeeeeeeeeesh")


@bot.command(name="objectif",aliases = ["Objectif","objectifs","Objectifs"])
async def Ajouter_objectif(ctx, *,proposition):
    global liste_objectifs
    liste_objectifs.append(proposition)
    await ctx.send(liste_objectifs)


@bot.command(name="retirer_objectif",aliases = ["Retirer_objectif"])
async def Supprimer(ctx):
    global liste_objectifs
    for i in range(len[liste_objectifs]):
        await ctx.send(liste_objectifs[i])





bot.run("ODQ1NjY0MDQxNzM2NDcwNTM4.YKkQAw.xtbK5_NBKLZGVhjo0UamcnZxQ10")