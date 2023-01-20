import aminofix
from pyfiglet import figlet_format
from colored import fore, style
from tqdm import tqdm



print(
    f"""{fore.CADET_BLUE_1 + style.BOLD}
    Multi Transfer
Script by Lucas Day
Github : https://github.com/LucasAlgerDay"""
)
print(figlet_format("Multi Transfer", font="fourtops"))



email = input("email: ")
password = input("password: ")

client = aminofix.Client()
client.login(email, password)
disponibles = client.get_wallet_info().totalCoins
print(f"Coins disponibles: {disponibles}")





def vip():
    link =  input("Link: ")
    fok=client.get_from_code(link)
    communityid=fok.path[1:fok.path.index("/")]
    total =int(input("Cantidad a donar: "))
    count = 0
    objeto=fok.objectId
    try:
        client.join_community(comId = communityid)
    except:
        print("Asegurate de que la comunidad sea publica, si la cuenta ya se encuentra dentro de la comunidad ignora este mensaje xd")
    sub_client = aminofix.SubClient(comId=communityid, profile=client.profile)
    for i in tqdm(range(total // 500)):
        try:
            sub_client.subscribe(userId= objeto, autoRenew= False)
            count += 500
        except Exception as e:
            print(e)
    print(f"Coins enviadas {count}")


def blogs():
    link =  input("Link: ")
    fok=client.get_from_code(link)
    communityid=fok.path[1:fok.path.index("/")]
    total =int(input("Cantidad a donar: "))
    count = 0
    objeto=fok.objectId
    try:
        client.join_community(comId = communityid)
    except:
        print("Asegurate de que la comunidad sea publica, si la cuenta ya se encuentra dentro de la comunidad ignora este mensaje xd")
    sub_client = aminofix.SubClient(comId=communityid, profile=client.profile)
    for i in tqdm(range(total // 500)):
        try:
            sub_client.send_coins(coins= 500, blogId= objeto)
            count += 500
        except Exception as e:
            print(e)
    print(f"Coins enviadas {count}")


def wikis():
    link =  input("Link de la wiki: ")
    fok=client.get_from_code(link)
    communityid=fok.path[1:fok.path.index("/")]
    total =int(input("Cantidad a donar: "))
    count = 0
    objeto=fok.objectId
    try:
        client.join_community(comId = communityid)
    except:
        print("Asegurate de que la comunidad sea publica, si la cuenta ya se encuentra dentro de la comunidad ignora este mensaje xd")
    sub_client = aminofix.SubClient(comId=communityid, profile=client.profile)
    for i in tqdm(range(total // 500)):
        try:
            sub_client.send_coins(coins= 500, objectId= objeto)
            count += 500
        except Exception as e:
            print(e)
    print(f"Coins enviadas {count}")



def chats():
    link =  input("Link del chat: ")
    fok=client.get_from_code(link)
    communityid=fok.path[1:fok.path.index("/")]
    total =int(input("Cantidad a donar: "))
    print("\nSugerencia: Para evitar error a la hora de donar no se sugiere bajar de 2 segundos")
    count = 0
    objeto=fok.objectId
    try:
        client.join_community(comId = communityid)
    except:
        print("Asegurate de que la comunidad sea publica, si la cuenta ya se encuentra dentro de la comunidad ignora este mensaje xd")
    sub_client = aminofix.SubClient(comId=communityid, profile=client.profile)
    for i in tqdm(range(total // 500)):
        try:
            sub_client.send_coins(coins= 500, chatId= objeto)
            count += 500
        except Exception as e:
            print(e)
    print(f"Coins enviadas {count}")


print("1.Transfer Vip")
print("2.Transfer blog")
print("3.Transfer Wiki")
print("4.Transfer Chat")
select = input("Type Number: ")
if select == "1":
	vip()

elif select == "2":
    print("SOLO CON VALORES MULTIPLOS DE 500")
    blogs()

elif select == "3":
    print("SOLO CON VALORES MULTIPLOS DE 500")
    wikis()

elif select == "4":
    print("SOLO CON VALORES MULTIPLOS DE 500")
    chats()
