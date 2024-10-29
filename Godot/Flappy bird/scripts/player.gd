extends CharacterBody2D

const JUMP_VELOCITY = -400.0
const ROTATION_ANGLE_MAX = 40.0

var gravity = ProjectSettings.get_setting("physics/2d/default_gravity")
var target_rotation = 0.0

@onready var player_sprite = $AnimatedSprite2D
@onready var game_manager = %GameManager
@onready var camera = $Camera
@onready var wing_audio = $WingAudio
@onready var hit_audio = $HitAudio

func _physics_process(delta):
	if (Input.is_action_just_pressed("jump")):
		game_manager.startGame()

	if (game_manager.gamePaused): return

	# Grawitacja
	velocity.y += gravity * delta
	
	# Latanie (w bok)
	velocity.x = game_manager.PLAYER_SPEED
	
	# Ustawianie max rotacji w zależności w wzlatuje czy spada
	if velocity.y >= 0:
		target_rotation = ROTATION_ANGLE_MAX
	elif velocity.y < 0:
		target_rotation = -ROTATION_ANGLE_MAX
		
	# Płynna rotacja
	player_sprite.rotation_degrees = lerp(player_sprite.rotation_degrees, target_rotation, 0.2)
	
	# Animacja bycia martwym
	if (game_manager.isDead):
		player_sprite.play("dead")

	# Skok
	if (Input.is_action_just_pressed("jump")&&player_sprite.global_position[1] > 25&&!game_manager.isDead):
		velocity.y = JUMP_VELOCITY
		wing_audio.play()

	# Restart
	if (Input.is_action_just_pressed("jump") && game_manager.isDead && game_manager.canStartNewGame):
		game_manager.newGame()

	move_and_slide()

func _on_killzone_body_entered(_body):
	if(!game_manager.isDead):
		game_manager.death()
		hit_audio.play()
