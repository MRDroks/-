##PYthon ^
memory_password = [

	]
message = ['Довайте мы пройдём регистрацию ?',
           'сколько вам лет ?', 'видите логин',
           'видите пороль', 'вы успешно заригистрирывались',
           'пройзошла ошыпка', 'видите всвоё имя', 'сколько вам лет ?',
           'вы не заригестрирываны', 'вы вошли в акаунт',
           'у вас нет акаунтов', 'найден акаут-ы', 'выберите книгу']

MENU = ['регистрация', 'войти', 'читать книги', 'выход']
registered_number = 0    
Index_mouse = 0           #важно
acaunt = 0
registered_acaunt = [
	
	]
while True:
	print('_' * 79)
	if len(memory_password) == 0:
		print(f'{message[8] + " " + message[10]:>59}')
	else:
		print(f'{message[11]:>59}')
	for index in range(len(MENU)):
		print(f'{MENU[index]:>16}')
	print(f'{" >":>5} {MENU[Index_mouse]:2}')
	choice = input('\nупровление w,s,q,: ')
	if choice == 'w':
		if Index_mouse == 0:
			pass
		else:
			Index_mouse -= 1
	elif choice == 's':
		if Index_mouse == 3:
			pass
		else:
			Index_mouse += 1
	elif choice == 'q':
		if Index_mouse == 0:
			while True:
				SD = int(registered_number)
				registered_number += 1
				break
			while True: 
				print('_' * 79)
				login = input(message[2] + ' ').strip()
				password = input(message[3] + ' минимум 8 ').strip()
				if int(len(password)) >= 8:
					name = input(message[6] + ' ').strip()
					if len(name) >= 2:
						age = input(message[7] + ' ').strip()
						if int(age) >= 18:
							memory_password.append({SD:[{'password':int(password),\
								'login':str(login),'name':str(name),\
								'age':int(age)}]})
							print(message[4])
							break
						elif int(age) <= 100:
							print(message[5] + '\n')
						else:
							print(message[5] + '\n')
					else:
						print(message[5] + '\n')
				else:
					print(message[5] + '\n')
		elif Index_mouse == 1:
			while True:
				print('_' * 79)
				if len(memory_password) == 0:
					print(message[10])
					break
				else:
					for Index in range(len(memory_password)):
						print(f'login.. {memory_password[Index][Index][0]["login"]:2}\
						name.. {memory_password[Index][Index][0]["name"]}')
					What = input('выбирите акаунт видите login / выход esc : ')
					if What == 'esc':
						break 
					elif What == memory_password[Index][Index][0]['login']:
						password_acaunt = int(input('видите пороль чтоб зайти : ', ))
						if password_acaunt == memory_password[Index][Index][0]['password']:
							print(message[9])
							break
						else:
							print(message[5] + '\n')
					else:
						print(message[5] + '\n')
		elif Index_mouse == 2:
			print('_' * 79)
			print('1_[хит рон] 2_[рон] 3_[кит]')#рандом 
			what_books = input(message[12])
			if what_books == '1':
				read = open('data/books_1.txt', 'r')
				ASD = read.read()
				print(ASD)
			elif what_books == '2':
				read = open('data/books_2.txt', 'r')
				ASD = read.read()
				print(ASD)
			elif what_books == '3':
				read = open('data/books_3.txt', 'r')
				ASD = read.read()
				print(ASD)
		elif Index_mouse == 3:
			break