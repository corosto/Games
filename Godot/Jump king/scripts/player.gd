extends CharacterBody2D

class_name Player

# sygnał do emitowania danych gracza do managera
signal playerData(position: Vector2, velocity: Vector2)

const JUMP_SPEED := 330 # velocity.x dodane do skoku kierunkowego
const MAX_JUMP_VELOCITY := -890 # maksymalna wartość do jakie ładuje się skok
const WIND_STRENGTH := 2000.0

var gravity = ProjectSettings.get_setting("physics/2d/default_gravity") # grawitacja
var loadingJumpVelocity := 0.0 # zmienna do ładowania skoku
var isFlying := false # czy gracz jest w powietrzu
var isSliding := false # czy gracz zjeżdża z pochyłej powierzchi
var playerSpeedBeforeLeavingSlope := Vector2.ZERO # prędkość gracza przed opuszczenie slope'a

var currentWindDirection := 1
var waitingForWindTimer := false

@onready var playerSprite = $AnimatedSprite2D # AnimatedSprite gracza
@onready var soundHit = $Hit # dźwięk uderzenia w ścianę
@onready var soundJump = $Jump # dźwięk podskoku
@onready var wind_stop_timer = $"../HUD/Wind/WindStopTimer"
@onready var wind = $"../HUD/Wind"
@onready var wind_timer = $"../HUD/Wind/WindTimer"

func _physics_process(delta) -> void:
	
	slideAndUnderSlopeBounce()
	pushPlayerAfterLeavingSlider()
	
	# emitowanie danych gracza do managera
	playerData.emit(global_position, velocity)
	
	# odbijanie gracza przy kontakcie z ścianą
	var xVelocityBeforeHit = velocity.x
	if move_and_slide() && is_on_wall() && !is_on_floor() && velocity.y && xVelocityBeforeHit && !isSliding:
		playerBounce(xVelocityBeforeHit)
	
	if is_on_ceiling():
		soundHit.play()
	
	if Global.gameEnviroment == Global.EnviromentEffects.NONE:
		defaultMovement(delta)
		resetWind()
	
	if Global.gameEnviroment == Global.EnviromentEffects.WIND:
		defaultMovement(delta)
		windEnvEffect(delta)
		if wind_timer.is_stopped():
			wind_timer.start()
	
	if Global.gameEnviroment == Global.EnviromentEffects.WIND_AND_SNOW:
		windAndSnowEnvEffect(delta)
		if wind_timer.is_stopped():
			wind_timer.start()
	
	if Global.gameEnviroment == Global.EnviromentEffects.ICE:
		iceEnvEffect(delta)
		resetWind()

func resetWind() -> void:
	currentWindDirection = 1
	wind.process_material.direction = Vector3(1, 0, 0)
	waitingForWindTimer = false

func defaultMovement(delta: float) -> void:
	if is_on_floor():
		# żeby po wylądowaniu zawsze zerowało prędkość żeby gdzieś nie zjechał(chyba nie działa xd)
		if isFlying:
			isFlying = false
			velocity.x = 0

		var direction = Input.get_axis("move_left", "move_right")

		if Input.is_action_pressed("jump"):
			# ładowanie skoku i zatrzymanie ruchu
			playerSprite.play('jump_loading')
			loadingJumpVelocity -= 1362 * delta
			velocity.x = 0
		else:
			# poruszanie się gracza
			if direction:
				playerSprite.play('walk')
				playerSprite.flip_h = direction == -1
				velocity.x = direction * Global.PLAYER_MOVE_SPEED
			else:
				# gracz się nie rusza
				playerSprite.play('idle')
				velocity.x = 0

		if Input.is_action_just_released("jump") || loadingJumpVelocity <= MAX_JUMP_VELOCITY:
			# puszczenie skoku albo gracz osiągnał max poziom naładowania skoku
			playerSprite.play('jumping')
			soundJump.play()
			playerJump(direction)
	else:
		# jeżeli gracz nie jest na ziemi(działa na niego grawitacja)
		isFlying = true
		velocity.y += gravity * delta * 1.28


func windEnvEffect(delta: float) -> void:
	# jak nie czeka na koniec timera to przesuwa gracza w zależności czy stoi na podłodze czy nie
	if !waitingForWindTimer:
		wind.emitting = true
		if is_on_floor():
			velocity.x += currentWindDirection * WIND_STRENGTH * delta
		else:
			velocity.x += currentWindDirection * WIND_STRENGTH * delta * 0.15

func windAndSnowEnvEffect(delta: float) -> void:
	windEnvEffect(delta)

	# symulacja śniegu, gracz nie może się poruszać chodząc
	if is_on_floor():
		velocity.x = 0
		
		# żeby po wylądowaniu zawsze zerowało prędkość żeby gdzieś nie zjechał(chyba nie działa xd)
		if isFlying:
			isFlying = false
			velocity.x = 0

		var direction = Input.get_axis("move_left", "move_right")

		if Input.is_action_pressed("jump"):
			# ładowanie skoku i zatrzymanie ruchu
			playerSprite.play('jump_loading')
			loadingJumpVelocity -= 1362 * delta
		else:
			# gracz się nie rusza
			playerSprite.play('idle')

		if Input.is_action_just_released("jump") || loadingJumpVelocity <= MAX_JUMP_VELOCITY:
			# puszczenie skoku albo gracz osiągnał max poziom naładowania skoku
			playerSprite.play('jumping')
			soundJump.play()
			playerJump(direction)
	else:
		# jeżeli gracz nie jest na ziemi(działa na niego grawitacja)
		isFlying = true
		velocity.y += gravity * delta * 1.28

func iceEnvEffect(delta: float) -> void:
	if is_on_floor():
		var direction = Input.get_axis("move_left", "move_right")

		if Input.is_action_pressed("jump"):
			# ładowanie skoku i zatrzymanie ruchu
			playerSprite.play('jump_loading')
			loadingJumpVelocity -= 1362 * delta
			velocity.x = move_toward(velocity.x, 0, 450 * delta)
		else:
			# poruszanie się gracza
			if direction:
				playerSprite.play('walk')
				playerSprite.flip_h = direction == -1
				velocity.x = direction * Global.PLAYER_MOVE_SPEED
			else:
				# gracz się nie rusza
				playerSprite.play('idle')
				velocity.x = move_toward(velocity.x, 0, 450 * delta)

		if Input.is_action_just_released("jump") || loadingJumpVelocity <= MAX_JUMP_VELOCITY:
			# puszczenie skoku albo gracz osiągnał max poziom naładowania skoku
			playerSprite.play('jumping')
			soundJump.play()
			playerJump(direction)
	else:
		# jeżeli gracz nie jest na ziemi(działa na niego grawitacja)
		isFlying = true
		velocity.y += gravity * delta * 1.28

func playerJump(direction: int) -> void:
	# podskok gracza i skierowanie go w odpowiednią stronę w zależności który kierunek wybrał i z 
	# odpowiednią prędkością w zależności od tego czy jest przytulony do ściany
	velocity.x = direction * JUMP_SPEED
	velocity.y = loadingJumpVelocity
	loadingJumpVelocity = 0

func playerBounce(xVelocity: float) -> void:
	# odbicie gracza od ściany
	soundHit.play()
	velocity.x = -xVelocity*0.55

func slideAndUnderSlopeBounce() -> void:
	# funkcja sprawdzająca kąt nachylenia przylegających do gracza colliderów
	var collisionCount = get_slide_collision_count()
	var velocityBeforeHit = get_real_velocity()
	if collisionCount > 0:
		for i in range(collisionCount):
			var collision_info = get_slide_collision(i)
			var collision_normal = collision_info.get_normal()
			var angle = rad_to_deg(collision_normal.angle())
			
			if (angle >= -50 && angle <= -40) || (angle >= -140 && angle <= -130):
				# gracz jest na skosie i zjeżdża w dół
				playerSprite.play("sliding")
				isSliding = true
				return
			elif (angle <= 50 && angle >= 40) || (angle <= 140 && angle >= 130):
				# gracz uderzył w skos od dołu i go odbija
				soundHit.play()
				velocity = velocityBeforeHit.bounce(collision_normal) * .5
	
	isSliding = false

func pushPlayerAfterLeavingSlider() -> void:
	# gracz po wyjściu ze zjeżdżania musi być popchnięty z takim samym wektorem bo inaczej spadnie pionowo w dół
	if isSliding:
		playerSpeedBeforeLeavingSlope = get_real_velocity()
	elif playerSpeedBeforeLeavingSlope:
		velocity = playerSpeedBeforeLeavingSlope
		playerSpeedBeforeLeavingSlope = Vector2.ZERO


func _on_game_new_player_position(newPosition, action: Manager.AdditionalPlayerActions) -> void:
	# force'owanie nowej pozycji gracza np. po quick load
	position = newPosition
	match action:
		Manager.AdditionalPlayerActions.STOP:
			velocity = Vector2.ZERO


func _on_wind_timer_timeout():
	# zmiana kierunku wiatru
	waitingForWindTimer = true
	wind.emitting = false
	currentWindDirection = -1 * currentWindDirection
	if(currentWindDirection == 1):
		wind.process_material.direction = Vector3(1, 0, 0)
	else:
		wind.process_material.direction = Vector3(-1, 0, 0)
	wind_stop_timer.start()


func _on_wind_stop_timer_timeout():
	wind.emitting = true
	waitingForWindTimer = false
