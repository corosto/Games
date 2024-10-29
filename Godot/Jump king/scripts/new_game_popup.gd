extends Control

signal newGameButtonPressed(startNewGame: bool)


func _on_yes_button_pressed():
	newGameButtonPressed.emit(true)


func _on_no_button_pressed():
	newGameButtonPressed.emit(false)
