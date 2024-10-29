extends Control

signal saveBeforeExitingButtonPressed(startNewGame: bool)


func _on_yes_button_pressed():
	saveBeforeExitingButtonPressed.emit(true)


func _on_no_button_pressed():
	saveBeforeExitingButtonPressed.emit(false)
