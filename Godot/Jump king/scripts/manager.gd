extends Node

class_name Manager

enum AdditionalPlayerActions { STOP }

signal newPlayerPosition(position: Vector2, action: AdditionalPlayerActions)

var playerVelocity: Vector2

@onready var resetGameTimer = $ResetGameTimer
@onready var camera = $Camera2D
@onready var saveIcon = $HUD/SaveIcon
@onready var wind_start = $Background/WindStart
@onready var snow_start = $Background/SnowStart
@onready var wind_and_snow_stop = $Background/WindAndSnowStop
@onready var ice_start = $Background/IceStart
@onready var ice_stop = $Background/IceStop
@onready var wind = $HUD/Wind

func _ready() -> void:
	loadData()

func _process(_delta) -> void:
	# zapisanie gry jeżeli gracz się nie rusza
	if Input.is_action_just_pressed("quick_save"):
		if(!playerVelocity):
			saveData()
	
	# wczytanie zapisanej gry, jeżeli takowa istnieje
	if Input.is_action_just_pressed("quick_load"):
		loadData()
	
	# start timera do resetu gry
	if Input.is_action_just_pressed("reset"):
		resetGameTimer.start()
	
	# stop timera do resetu gry
	if Input.is_action_just_released("reset"):
		resetGameTimer.stop()
	
	# przesunięcie kamery w górę lub w dół po przekroczeniu odpowiedniej wysokości Y przez gracza
	if(Global.playerPosition.y <= -(Global.WINDOW_HEIGHT*(Global.currentSceneIndex+1) + Global.PLAYER_HEIGHT/2)):
		Global.currentSceneIndex += 1
		setNewCameraPosition()
	elif(Global.playerPosition.y >= -((Global.currentSceneIndex * Global.WINDOW_HEIGHT) - Global.PLAYER_HEIGHT/2)):
		Global.currentSceneIndex -= 1
		setNewCameraPosition()

func saveData() -> void:
	# zapisanie gry w pliku
	var file = FileAccess.open(Global.SAVE_PATH, FileAccess.WRITE)
	file.store_var(Global.playerPosition, true)
	file.store_var(Global.currentSceneIndex, true)
	file.store_var(Global.gameTime, true)
	saveIcon.get_node('SaveAnimation').play('move')

func loadData() -> void:
	# wczytanie gry jeżeli istnieje zapis
	if(FileAccess.file_exists(Global.SAVE_PATH)):
		var file = FileAccess.open(Global.SAVE_PATH, FileAccess.READ)
		Global.playerPosition = file.get_var(true)
		Global.currentSceneIndex = file.get_var(true)
		Global.gameTime = file.get_var(true)
		setNewCameraPosition()
		newPlayerPosition.emit(Global.playerPosition, AdditionalPlayerActions.STOP)

func setNewCameraPosition() -> void:
	camera.position.y = -(Global.currentSceneIndex*Global.WINDOW_HEIGHT)+Global.INIT_CAMERA_Y_POSITION

func _on_reset_game_timer_timeout() -> void:
	# po przytrzymaniu klawisza 'R' - restart gry
	Global.newGame(true)

func _on_player_player_data(playerPosition, velocity) -> void:
	# odbieranie danych o graczu
	Global.playerPosition = playerPosition
	playerVelocity = velocity
	
	if playerPosition.y < ice_start.global_position.y && playerPosition.y > ice_stop.global_position.y:
		wind.visible = false
		Global.gameEnviroment = Global.EnviromentEffects.ICE
	elif playerPosition.y < snow_start.global_position.y && playerPosition.y > wind_and_snow_stop.global_position.y:
		wind.visible = true
		Global.gameEnviroment = Global.EnviromentEffects.WIND_AND_SNOW
	elif playerPosition.y < wind_start.global_position.y && playerPosition.y > wind_and_snow_stop.global_position.y:
		wind.visible = true
		Global.gameEnviroment = Global.EnviromentEffects.WIND
	else:
		wind.visible = false
		Global.gameEnviroment = Global.EnviromentEffects.NONE


func _on_princess_body_entered(body):
	Global.hasFinishedGame = true
