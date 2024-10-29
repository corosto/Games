extends Control


@onready var pause = $"." # odnośnik do samego siebie(pauzy)
@onready var settings = $SettingsPanel # odnośnik do panelu ustawień
@onready var saveGameBeforeClosePopup = $SaveGameBeforeClosePopup # odnośnik do modala


func _process(_delta) -> void:
	# pauza po wciśnięciu klawisza escape
	if Input.is_action_just_pressed("pause"):
		menuClose()


func _on_resume_pressed() -> void:
	# przycisk 'resume' - koniec pauzy po wciśnięciu
	menuClose()


func _on_options_pressed() -> void:
	# przycisk 'settings' - otwarcie ustawień
	settings.visible = !settings.visible


func _on_exit_pressed() -> void:
	# przycisk 'exit' - pokazanie modala 'czy zapisać przed wyjściem'
	saveGameBeforeClosePopup.visible = true


func _on_save_game_before_close_popup_save_before_exiting_button_pressed(saveGame):
	if(saveGame):
		# wciśnięcie 'tak' w modalu 'czy zapisać przed wyjściem'
		var file = FileAccess.open(Global.SAVE_PATH, FileAccess.WRITE)
		file.store_var(Global.playerPosition, true)
		file.store_var(Global.currentCameraPositionIndex, true)

	# wyjście z gry
	get_tree().quit()


func menuClose():
	# zamknięcie menu, odpauzowanie gry
	get_tree().paused = !get_tree().paused
	pause.visible = !pause.visible
	settings.visible = false
	saveGameBeforeClosePopup.visible = false
