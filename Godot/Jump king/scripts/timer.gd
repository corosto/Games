extends Panel

var minutes := 0
var seconds := 0
var milliseconds:= 0


func _process(delta) -> void:
	if !Global.hasFinishedGame:
		# zwykły timer
		Global.gameTime += delta
		milliseconds = fmod(Global.gameTime, 1) * 100
		seconds = fmod(Global.gameTime, 60)
		minutes = fmod(Global.gameTime, 3600) / 60
		$Minutes.text = "%02d:" % minutes
		$Seconds.text = "%02d." % seconds
		$Miliseconds.text = "%02d" % milliseconds
