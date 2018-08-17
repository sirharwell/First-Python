def cycle():
	ans2 = input("Is this Cori yet? ")
	if(ans2 == 'yes' or ans2 == 'Yes' or ans2 == 'y' or ans2 == 'Y'):
		print(" ")
		print("Hello Cori. You're Awesome!")
	else:
		print("I don't have time for these games, go get her.")
		print(" ")
		cycle()

clear

print("Hello")
myname = input("What is your name? ")

if(myname == 'Cori' or myname == 'cori' or myname == 'corinne' or myname == 'Corinne' or myname == 'Cori Harwell' or myname == 'cori harwell'):
	print(" ")
	print("Hello Cori. You are great")
else:
	print(" ")
	print("But wait, where's Cori? I want to talk to Cori")
	ans1 = input("Do you know where Cori is? ")
	if(ans1 == 'yes' or ans1 == 'Yes' or ans1 == 'y' or ans1 == 'Y'):
		print(" ")
		print("Go and get her then!")
	elif(ans1 == 'No' or ans1 == 'no' or ans1 == 'n' or ans1 == 'N'):
		print(" ")
		print("Liar, go get her")
	else:
		print(" ")
		print("Stop being coy and go get her")
	cycle()
