#import:
from tkinter import *
import random as r
import ctypes
from tkinter import messagebox

#constants and variables:

all_symbols = [u'\u269A', u'\u269A', u'\u266C', u'\u266C', u'\u25B2', u'\u25B2', u'\u2756', u'\u2756',
			u'\u265C', u'\u265C', u'\u262D', u'\u262D', u'\u2691', u'\u2691', u'\u269B', u'\u269B',
			u'\u221E', '\u221E', u'\u2746', u'\u2746', u'\u2710', u'\u2710', u'\u265B', u'\u265B',
			u'\u16ED', u'\u16ED', u'\u2672', u'\u2672', u'\u10E6', u'\u10E6', u'\u2211', u'\u2211',
			u'\uF4DE', u'\uF4DE', u'\u2615', u'\u2615', u'\u2718', u'\u2718', u'\u269C', u'\u269C', u'\u2618', u'\u2618',
			u'\u0040', u'\u0040', u'\u260F', u'\u260F', u'\u2620', u'\u2620']

_randomSymbolsMassive = []
_coords_and_idDICT = {}
_twoCardsDICT = {}
_twoCardsMASSIVE = []
_twoCardsValues = []
_firstButton_active = False
_secondButton_active = False
_moveCount = 0
_openedCardsCount = 0

#methods:

def _tapDef(x, y, diff):
	if (x, y) in _coords_and_idDICT.values():
		try:
			for key, value in _coords_and_idDICT.items():
				if value == (x, y):
					global _buttonID
					global _firstButton_active, _secondButton_active, _moveCount, _openedCardsCount
					_buttonID = key
					(ctypes.cast(_buttonID, ctypes.py_object).value)['state'] = 'disabled'
					if len(_coords_and_idDICT) > 0:
						if _firstButton_active == False and _secondButton_active == False:
							_firstButton_active = True
							_twoCardsDICT[_buttonID] = ((ctypes.cast(_buttonID, ctypes.py_object).value))['text']
						elif _firstButton_active == True and _secondButton_active == False:
							if _openedCardsCount < diff - 1:	
								_secondButton_active = True
								_twoCardsDICT[_buttonID] = ((ctypes.cast(_buttonID, ctypes.py_object).value))['text']
								_moveCount += 1
								for key, value in _twoCardsDICT.items():
									_twoCardsMASSIVE.append(key)
									_twoCardsValues.append(value)
								if _twoCardsValues[0] == _twoCardsValues[1]:
									for i in _twoCardsMASSIVE:
										del _coords_and_idDICT[i]
										((ctypes.cast(i, ctypes.py_object).value))['state'] = 'disabled'
									for i in _coords_and_idDICT:
										((ctypes.cast(i, ctypes.py_object).value))['state'] = 'normal'
									_openedCardsCount += 1
									_tapCountLABEL['text'] = 'Количество сделанных ходов(открытых пар): '+str(_openedCardsCount)
								else:
									for i in _coords_and_idDICT:
										((ctypes.cast(i, ctypes.py_object).value)).config(fg = 'yellow')
										((ctypes.cast(i, ctypes.py_object).value))['state'] = 'normal'
								_twoCardsDICT.clear()
								_twoCardsValues.clear()
								_twoCardsMASSIVE.clear()
								_firstButton_active = False
								_secondButton_active = False
							elif _openedCardsCount == diff - 1:
								_tapCountLABEL['text'] = 'Количество сделанных ходов(открытых пар): '+str(int(diff / 2))
								_coords_and_idDICT.clear()
								_twoCardsDICT.clear()
								_twoCardsMASSIVE.clear()
								_twoCardsValues.clear()
								_firstButton_active = False
								_secondButton_active = False
								_openedCardsCount = 0
								messagebox.showinfo('Игра окончена', 'Вы победили!\nОбщее количество ходов: '+str(_moveCount))
								_moveCount = 0
								if diff == 4:
									new_window_easy.destroy()
								elif diff == 12:
									new_window_normal.destroy()
								elif diff == 24:
									new_window_hard.destroy()
								else:
									print('WHAAAAAt')
						elif _firstButton_active == True and _secondButton_active == True:
								_firstButton_active = False
								_secondButton_active = False
								_moveCount += 1
		except RuntimeError:
			1+1




def _easyDef():
	while len(_randomSymbolsMassive) != 8:
		_randomSymbols = r.choice(all_symbols)
		for f in range(2):
			if _randomSymbolsMassive.count(_randomSymbols) < 2 or len(_randomSymbolsMassive) == 0:
				_randomSymbolsMassive.append(_randomSymbols)
	global new_window_easy
	new_window_easy = Toplevel()
	new_window_easy.focus_set()
	new_window_easy['bg'] = '#4b4d4b'
	new_window_easy.geometry('600x600')
	new_window_easy.resizable(False, False)

	global _tapCountLABEL
	_tapCountLABEL = Label(new_window_easy,
			bg = '#4b4d4b',
			text = 'Количество сделанных ходов(открытых пар): 0',
			font = ('Candara', 20))

	global grid_x, grid_y
	grid_x = 135 
	grid_y = 120


	for i in range(2):
		for i in range(4):
			_randELEMENT = r.choice(_randomSymbolsMassive)
			_button = Button(new_window_easy,
			width = 3,
			height = 2,
			bg = 'yellow',
			fg = 'yellow',
			bd = 2,
			text = _randELEMENT,
			font = ('Candara', 25),
			activeforeground = 'black',
			activebackground = 'yellow',
			command = lambda x = grid_x, y = grid_y: _tapDef(x, y, 4))
			_button.place(x = grid_x, y = grid_y)
			_coords_and_idDICT[id(_button)] = (grid_x, grid_y)
			_randomSymbolsMassive.remove(_randELEMENT)
			grid_x += 85
		grid_y += 130
		grid_x = 135

	_tapCountLABEL.place(x = 20, y = 400)

	_randomSymbolsMassive.clear()


def _middleDef():
	while len(_randomSymbolsMassive) != 24:
		_randomSymbols = r.choice(all_symbols)
		for f in range(2):
			if _randomSymbolsMassive.count(_randomSymbols) < 2 or len(_randomSymbolsMassive) == 0:
				_randomSymbolsMassive.append(_randomSymbols)
	global new_window_normal
	new_window_normal = Toplevel()
	new_window_normal.focus_set()
	new_window_normal['bg'] = '#4b4d4b'
	new_window_normal.geometry('600x600')
	new_window_normal.resizable(False, False)
	global _tapCountLABEL
	_tapCountLABEL = Label(new_window_normal,
			bg = '#4b4d4b',
			text = 'Количество сделанных ходов(открытых пар): 0',
			font = ('Candara', 20))

	global grid_x, grid_y
	grid_x = 140
	grid_y = 70


	for i in range(4):
		for i in range(6):
			_randELEMENT = r.choice(_randomSymbolsMassive)
			_button = Button(new_window_normal,
			width = 3,
			height = 2,
			bg = 'yellow',
			fg = 'yellow',
			bd = 2,
			text = _randELEMENT,
			font = ('Candara', 15),
			activeforeground = 'black',
			activebackground = 'yellow',
			command = lambda x = grid_x, y = grid_y: _tapDef(x, y, 12))
			_button.place(x = grid_x, y = grid_y)
			_coords_and_idDICT[id(_button)] = (grid_x, grid_y)
			_randomSymbolsMassive.remove(_randELEMENT)
			grid_x += 50
		grid_y += 80
		grid_x = 140

	_tapCountLABEL.place(x = 20, y = 400)

	_randomSymbolsMassive.clear()


def _hardDef():
	while len(_randomSymbolsMassive) != 48:
		_randomSymbols = r.choice(all_symbols)
		for f in range(2):
			if _randomSymbolsMassive.count(_randomSymbols) < 2 or len(_randomSymbolsMassive) == 0:
				_randomSymbolsMassive.append(_randomSymbols)
	global new_window_hard
	new_window_hard = Toplevel()
	new_window_hard.focus_set()
	new_window_hard['bg'] = '#4b4d4b'
	new_window_hard.geometry('600x600')
	new_window_hard.resizable(False, False)

	global _tapCountLABEL
	_tapCountLABEL = Label(new_window_hard,
			bg = '#4b4d4b',
			text = 'Количество сделанных ходов(открытых пар): 0',
			font = ('Candara', 20))

	global grid_x, grid_y
	grid_x = 80
	grid_y = 40


	for i in range(6):
		for i in range(8):
			_randELEMENT = r.choice(_randomSymbolsMassive)
			_button = Button(new_window_hard,
			width = 3,
			height = 2,
			bg = 'yellow',
			fg = 'yellow',
			bd = 2,
			text = _randELEMENT,
			font = ('Candara', 12),
			activeforeground = 'black',
			activebackground = 'yellow',
			command = lambda x = grid_x, y = grid_y: _tapDef(x, y, 24))
			_button.place(x = grid_x, y = grid_y)
			_coords_and_idDICT[id(_button)] = (grid_x, grid_y)
			_randomSymbolsMassive.remove(_randELEMENT)
			grid_x += 50
		grid_y += 70
		grid_x = 80

	_tapCountLABEL.place(x = 20, y = 500)

	_randomSymbolsMassive.clear()

#main:

root = Tk()
root.title('Memory Game.')
root.geometry('600x600')
root.resizable(False, False)
root['bg'] = '#4b4d4b'

# Difficulty Choice:

_easyDifficultyButton = Button(root,
			width = 10,
			height = 1,
			bg = '#4b4d4b',
			bd = 2,
			text = 'Легко',
			font = ('Candara', 20),
			activeforeground = '#979c97',
			activebackground = '#181a18',
			command = _easyDef)

_middleDifficultyButton = Button(root,
			width = 10,
			height = 1,
			bg = '#4b4d4b',
			text = 'Средне',
			font = ('Candara', 20),
			bd = 2,
			activeforeground = '#979c97',
			activebackground = '#181a18',
			command = _middleDef)

_hardDifficultyButton = Button(root,
			width = 10,
			height = 1,
			bg = '#4b4d4b',
			text = 'Сложно',
			font = ('Candara', 20),
			bd = 2,
			activeforeground = '#979c97',
			activebackground = '#181a18',
			command = _hardDef)

_mmLabel = Label(root,
			text = 'Memory Game.',
			fg = 'black',
			bg = '#4b4d4b',
			font = ('Candara', 35))


_rootCanv = Canvas(root,
			width = 256,
			height = 256,
			bg = '#4b4d4b',
			bd=0,
			highlightthickness=0)

# Place:

_rootCanv.place(x = 170, y = 135)
logoPath = PhotoImage(file = 'cards.gif')
logoPlace = _rootCanv.create_image(128, 135, anchor = CENTER, image = logoPath)

_mmLabel.place(x = 150, y = 50)
_easyDifficultyButton.place(x = 50, y = 450)
_middleDifficultyButton.place(x = 220, y = 450)
_hardDifficultyButton.place(x = 390, y = 450)

root.mainloop()