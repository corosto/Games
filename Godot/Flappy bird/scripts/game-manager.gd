extends Node

var PLAYER_SPEED = 140
var PLAYER_POINTS = 0
var isDead = false
var canStartNewGame = false
var gamePaused = true

var pipe = preload("res://scenes/pipes.tscn")
var spawnedPipes: Array
var lastPipe

@onready var score_display = $Interface/ScoreDisplay
@onready var score_display_2 = $Interface/ScoreDisplay2
@onready var score_display_3 = $Interface/ScoreDisplay3
@onready var menu = $Interface/Menu
@onready var death_screen = $Interface/DeathScreen
@onready var newGameTimer = $NewGameTimer
@onready var player = $"../Player"

func _ready():
	generateObstackles()
	
func _process(_delta):
	removeObstackles()

	if(lastPipe):
		if (!isDead && !gamePaused && (player.global_position[0] - lastPipe.global_position[0] <= 100) && spawnedPipes.size() <= 5):
			generateObstackles()

func generateObstackles():
	var newPipe = pipe.instantiate()
	var Y_position = randi_range(-250, 1)
	var X_position = getPipeXPosition()
	newPipe.position = Vector2(X_position, Y_position)
	newPipe.get_node("TopPipe").get_node("TopPipeArea2D").body_entered.connect(hit_pipe)
	newPipe.get_node("BottomPipe").get_node("BottomPipeArea2D").body_entered.connect(hit_pipe)
	newPipe.get_node("Point").body_entered.connect(point)
	add_child(newPipe)
	lastPipe = newPipe
	spawnedPipes.append(newPipe)

func removeObstackles():
	for index in range(spawnedPipes.size() - 1, -1, -1):
		var currentPipe = spawnedPipes[index]
		if (currentPipe.global_position[0] - player.global_position[0] <= -500):
			spawnedPipes.remove_at(index)
			currentPipe.queue_free()

func getPipeXPosition():
	if(lastPipe):
		return lastPipe.global_position[0] + 260
	else:
		return 730

func hit_pipe(body):
	if (body.name == "Player"):
		if (!isDead):
			death()

func death():
	if (!isDead):
		newGameTimer.start()
		isDead = true
		PLAYER_SPEED = 0
		death_screen.visible = true

func point(body):
	if (body.name == "Player" && !isDead):
		PLAYER_POINTS += 1
		if (PLAYER_POINTS < 10):
			score_display.texture = load("res://assets/UI/Numbers/%s.png" % str(PLAYER_POINTS))
		elif (PLAYER_POINTS >= 10):
			score_display_2.visible = true
			score_display.texture = load("res://assets/UI/Numbers/%s.png" % str(PLAYER_POINTS)[0])
			score_display_2.texture = load("res://assets/UI/Numbers/%s.png" % str(PLAYER_POINTS)[1])
		elif (PLAYER_POINTS >= 100):
			score_display_2.visible = true
			score_display_3.visible = true
			score_display.texture = load("res://assets/UI/Numbers/%s.png" % str(PLAYER_POINTS)[0])
			score_display_2.texture = load("res://assets/UI/Numbers/%s.png" % str(PLAYER_POINTS)[1])
			score_display_3.texture = load("res://assets/UI/Numbers/%s.png" % str(PLAYER_POINTS)[2])

func newGame():
	get_tree().reload_current_scene()

func startGame():
	gamePaused = false
	score_display.visible = true
	menu.visible = false

func _on_new_game_timer_timeout():
	canStartNewGame = true
