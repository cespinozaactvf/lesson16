import random
import time

print()
print('*' * 70)

print("A wild Jigglypuff appears!")
print()
time.sleep(1)

print('You only have one Pokemon, Pikachu.')
print()
time.sleep(1)

pikachu_hp = 200
jigglypuff_hp = 125

print(">> Pikachu has " + str(pikachu_hp) + " HP.")
print(">> Jigglypuff has " + str(jigglypuff_hp) + " HP.")

print()

while pikachu_hp > 0 and jigglypuff_hp > 0:
	print("Battle Options:")
	time.sleep(1)

	print("> [1] Tackle")
	print("> [2] Thunder Bolt")
	print("> [3] Shock")
	print("> [4] Slash")
	print("> [5] Capture")

	time.sleep(2)

	print()

	print(">> What should Pikachu do?") 
	playermove = input(">> Choose a move using the corresponding number: ")

	if playermove == "1":
		print()
		jigglypuff_hp = jigglypuff_hp - 20
		print(">> Pikachu used Tackle.")
		print()
		time.sleep(1)
		print(">> Jigglypuff is hit!")
		time.sleep(1)
		print(">> Jigglypuff's HP is decreased to " + str(jigglypuff_hp) + ".")
		print()

	elif playermove == "2":
		print()
		jigglypuff_hp = jigglypuff_hp - 30
		print(">> Pikachu used Thunder Boly.")
		print()
		time.sleep(1)
		print(">> Jigglypuff is hit!")
		time.sleep(1)
		print(">> Jigglypuff's HP is decreased to " + str(jigglypuff_hp) + ".")
		print()

	elif playermove == "3":
		print()
		jigglypuff_hp = jigglypuff_hp - 20
		print(">> Pikachu used Shock.")
		print()
		time.sleep(1)
		print(">> Jigglypuff is hit!")
		time.sleep(1)
		print(">> Jigglypuff's HP is decreased to " + str(jigglypuff_hp) + ".")
		print()

	elif playermove == "4": 
		print()
		jigglypuff_hp = jigglypuff_hp - 15
		print(">> Pikachu used Slash.")
		print()
		time.sleep(1)
		print(">> Jigglypuff is hit!")
		time.sleep(1)
		print(">> Jigglypuff's HP is decreased to " + str(jigglypuff_hp) + ".")
		print()

	elif playermove == "5": 
		capture = random.randint(1,125)
	
		if capture > jigglypuff_hp: 
			print()
			time.sleep(2)
			print("...")

			print()
			time.sleep(2)
			print("...")

			print()
			time.sleep(2)
			print("...")
			print()
			
			print("You captured Jigglypuff!")
			break

		else: 
			print()
			time.sleep(2)
			print("...")

			print()
			time.sleep(2)
			print("...")

			print()
			time.sleep(2)
			print("...")
			print()

			print("Jigglypuff escaped!")

	jigglypuff_move = random.randint(1,4)
	jigglypuff_move = str(jigglypuff_move)

	if jigglypuff_move == "1":
		print()
		pikachu_hp = pikachu_hp - 30
		print(">> Jigglypuff uses Headbutt.")
		print()
		time.sleep(1)
		print(">> Pikachu is hit!")
		time.sleep(1)
		print(">> Pikachu's HP is decreased to " + str(pikachu_hp) + ".")
		print()

	elif jigglypuff_move == "2": 
		print()
		pikachu_hp = pikachu_hp - 20
		print(">> Jigglypuff used Body Slam.")
		print()
		time.sleep(1)
		print(">> Pikachu is hit!")
		time.sleep(1)
		print(">> Pikachu's HP is decreased to " + str(pikachu_hp) + ".")
		print()

	elif jigglypuff_move == "3":
		print()
		pikachu_hp = pikachu_hp - 50
		print(">> Jigglypuff used Ice Beam.")
		print()
		time.sleep(1)
		print(">> Pikachu is hit!")
		time.sleep(1)
		print(">> Pikachu's HP is decreased to " + str(pikachu_hp) + ".")
		print()

	elif jigglypuff_move == "4": 
		print()
		pikachu_hp = pikachu_hp - 40
		print(">> Jigglypuff used Double Slap.")
		print()
		time.sleep(1)
		print(">> Pikachu is hit!")
		time.sleep(1)
		print(">> Pikachu's HP is decreased to " + str(pikachu_hp) + ".")
		print()

	print()
	print(">> Pikachu has " + str(pikachu_hp) + " HP.")
	print(">> Jigglypuff has " + str(jigglypuff_hp) + " HP.")
	print()
	print()

	if pikachu_hp < 0: 
		pikachu_hp = 0

	if jigglypuff_hp < 0:
		jigglypuff_hp = 0

if pikachu_hp == 0:
	time.sleep(2)
	print("Pikachu fainted!")
	time.sleep(1)
	print("You lose.")

elif jigglypuff_hp == 0:
	time.sleep(2)
	print("Jigglypuff fainted!")
	time.sleep(1)
	print("You win!")

print('*' * 70)