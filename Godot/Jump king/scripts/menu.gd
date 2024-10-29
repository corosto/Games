extends Control

var hasSafeFile: bool # czy istnieje plik z zapisaną grą

@onready var continueButton = $ButtonsPanel/Buttons/Continue
@onready var newGamePopup = $CanvasLayer/NewGamePopup
@onready var settings = $SettingsPanel


func _ready() -> void:
	# sprawdzenie czy istnieje plik z zapisaną grą
	if(FileAccess.file_exists(Global.SAVE_PATH)):
		var file = FileAccess.open(Global.SAVE_PATH, FileAccess.READ)
		var playerPosition = file.get_var(true)
		var currentSceneIndex = file.get_var(true)
		var gameTime = file.get_var(true)
		hasSafeFile = (playerPosition != null && currentSceneIndex != null && gameTime != null)
		if(hasSafeFile):
			continueButton.disabled = false


func _on_continue_pressed() -> void:
	# wciśnięcie continue, zostanie wczytany ostatni zapis metodą loadData() w managerze
	get_tree().change_scene_to_packed(Global.GAME_SCENE)


func _on_new_game_pressed() -> void:
	# wciśnięcie new game, jeżeli istnieje zapis, to pokaże 'new game' popup z pytaniem czy na pewno chce zacząć grę od nowa
	if(hasSafeFile):
		newGamePopup.visible = true
	else:
		Global.newGame(false)


func _on_options_pressed() -> void:
	# naciśnięcie na przycisk ustawień - pokazuje ustawienia
	settings.visible = !settings.visible


func _on_exit_pressed() -> void:
	# wyjście z gry
	get_tree().quit()


func _on_new_game_popup_new_game_button_pressed(startNewGame):
	# zamknięcie popupu i opcjonalnie włączenie gry od nowa
	newGamePopup.visible = false
	if(startNewGame):
		Global.newGame(false)
