extends Node

enum EnviromentEffects { NONE, WIND, WIND_AND_SNOW, ICE }

var currentSceneIndex := 0 # index aktualnej sceny
var gameTime := 0.0 # wartość timera

var playerPosition: Vector2 # aktualna pozycja gracza
var gameEnviroment: EnviromentEffects = EnviromentEffects.NONE

const SAVE_PATH := "user://savefile.save" # ścieżka do pliku z save'ami
const AUDIO_FILE_PATH := "user://audioSettings.save" # ścieżka do pliku z ustawieniami audio
var audioValues := [0.0, 0.0, 0.0] # wartości audio
var audioValuesRetrieved := false # flaga niepozwalająca pobierać kilkukrotnie wartości audio z pliku

var x1WindowSize: Vector2 # wektor wielkości okna dla x1
var x2WindowSize: Vector2 # wektor wielkości okna dla x2
var x3WindowSize: Vector2 # wektor wielkości okna dla x3
var currentWindowSize := 'x3' # napis na przycisku w ustawieniach obrazu
var currentWindowMode := 'Fullscreen' # napis na przycisku w ustawieniach obrazu
var hasFinishedGame := false # czy wszedł na samą górę(wyłącza timer)

var WINDOW_HEIGHT: int # wysokość okna
const PLAYER_MOVE_SPEED := 190 # prędkość chodzenia gracza
const PLAYER_HEIGHT := 36.0 # wysokość colidera gracza
const INIT_CAMERA_Y_POSITION := -360.0 # początkowa pozycja kamery
const GAME_SCENE = preload("res://scenes/game.tscn") # background
const NEW_GAME_POPUP = preload("res://scenes/new_game_popup.tscn") # popup pytający o nową grę(w menu)


func _ready() -> void:
	Engine.max_fps = 60
	
	# zapisanie wysokości okna
	WINDOW_HEIGHT = get_window().size.y
	
	# zapisanie wielkości okna dla poszczególnych mnożników
	x1WindowSize = get_window().size/1.5
	x2WindowSize = get_window().size
	x3WindowSize = get_window().size*1.5


# reset gry(wciskając New game w menu, przytrzymując R)
func newGame(reset: bool) -> void:
	# resetowanie wymaganych zmiennych(jeżeli restart przez przytrzymanie R)
	if(reset):
		hasFinishedGame = false
		currentSceneIndex = 0
		gameTime = 0.0
	
	# usuwanie pliku z save'ami
	if(FileAccess.file_exists(Global.SAVE_PATH)):
		DirAccess.remove_absolute(Global.SAVE_PATH)
	
	# wczytanie całej sceny jeszcze raz(wszystkie skrypty odpalą się jeszcze raz, oprócz Global)
	get_tree().change_scene_to_packed(Global.GAME_SCENE)
