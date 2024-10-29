extends Node2D

@onready var hit_audio = $HitAudio
@onready var fall_audio = $FallAudio
@onready var point_audio = $PointAudio

var isDead = false

func _on_top_pipe_area_2d_body_entered(body):
	if (body.name == "Player"):
		death(body)

func _on_bottom_pipe_area_2d_body_entered(body):
	if (body.name == "Player"):
		death(body)

func _on_point_body_entered(body):
	if (body.name == "Player"):
		point_audio.play()

func death(_body):
	if(!isDead):
		hit_audio.play()
		fall_audio.play()
		isDead = true
