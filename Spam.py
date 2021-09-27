try: import AminoLab
except:
	import os
	os.system("pip install AminoLab && clear")
	import AminoLab


client = AminoLab.Client()
email = input("Email >> ")
password = input("Password >> ")
client.auth(email=email, password=password)
print()


clients = client.my_communities()
for x, name in enumerate(clients.name, 1):
    print(f"{x}.{name}")

ndc_Id = clients.ndc_Id[int(input("Select the community >> ")) - 1]
print()


chats = client.my_chat_threads(ndc_Id=ndc_Id, size=100)

for z, title in enumerate(chats.title, 1):
    print(f"{z}.{title}")

thread_Id = chats.thread_Id[int(input("Select The Chat >> ")) - 1]
print()

			
def send_message(msg):
	while True:
		try:
			client.join_thread(ndc_Id=ndc_Id, thread_Id=thread_Id)
			client.send_message(ndc_Id=ndc_Id, thread_Id=thread_Id, message = msg)
		except BaseException:
			return


from threading import Thread
   
msg = input("Сообщение >> ")
print()


import os
os.system("mkdir spam")
    
for lol in range(int(input("Количество потоков (0-30) >> "))):
	open("spam/" + str(lol) + ".py", "w").write("""import AminoLab
from threading import Thread

client = AminoLab.Client()
client.auth(email = '""" + str(email) + """', password = '""" + str(password) + """')

ndc_Id = '""" + str(ndc_Id) + """'
thread_Id = '""" + str(thread_Id) + """'
msg = '""" + str(msg) + """'

			
def send_message(msg):
	while True:
		try:
			client.join_thread(ndc_Id=ndc_Id, thread_Id=thread_Id)
			client.send_message(ndc_Id=ndc_Id, thread_Id=thread_Id, message = msg)
		except BaseException:
			return

for x in range(50):
    Thread(target = send_message, args = (msg,)).start()""")

	os.system(f"python spam/{lol}.py & next")
        
print("\nSo bad")
