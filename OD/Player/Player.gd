extends KinematicBody2D

const PlayerHurtSound = preload("res://Player/PlayerHurtSound.tscn")

const ACCELERATION = 500
const MAX_SPEED = 80
const ROLL_SPEED = 100
const FRICTION = 500

enum { #short for enumeration, basically constants, but they're automatically made with values
	MOVE, # this is 0
	ROLL, # this is 1
	ATTACK# and so on
}

var state = MOVE
var velocity = Vector2.ZERO
var roll_vector = Vector2.DOWN
var stats = PlayerStats

onready var animationPlayer = $AnimationPlayer
onready var animationTree = $AnimationTree
onready var animationState = animationTree.get("parameters/playback")
onready var swordHitbox = $HitboxPivot/SwordHitbox
onready var hurtbox = $Hurtbox
onready var blinkAnimationPlayer = $BlinkAnimationPlayer

func _ready():
	randomize()# randomizes the seed for the game, godot uses a set seed for the game by default
	stats.connect("no_health", self, "queue_free")
	animationTree.active = true
	swordHitbox.knockback_vector = roll_vector



func _physics_process(delta):
	match state:
		MOVE:
			move_state(delta)

		ROLL:
			roll_state()

		ATTACK:
			attack_state()


func move_state(delta):
	var input_vector = Vector2.ZERO
	input_vector.x = Input.get_action_strength("move_right") - Input.get_action_strength("move_left")
	input_vector.y = Input.get_action_strength("move_down") - Input.get_action_strength("move_up")
	input_vector = input_vector.normalized()


	if input_vector != Vector2.ZERO:
		roll_vector = input_vector
		swordHitbox.knockback_vector = input_vector
		animationTree.set("parameters/Idle/blend_position", input_vector)
		animationTree.set("parameters/Run/blend_position", input_vector)
		animationTree.set("parameters/Attack/blend_position", input_vector)
		animationTree.set("parameters/Roll/blend_position", input_vector)
		animationState.travel("Run")
		velocity = velocity.move_toward(input_vector * MAX_SPEED, ACCELERATION * delta)
	else:
		animationState.travel("Idle")
		velocity = velocity.move_toward(Vector2.ZERO, FRICTION * delta)


	move()

	if Input.is_action_just_pressed("roll"):
		state = ROLL
		
	elif Input.is_action_just_pressed("attack"):
		state = ATTACK

func move():
	velocity = move_and_slide(velocity)



func roll_state():
	velocity = roll_vector * ROLL_SPEED
	animationState.travel("Roll")
	move()

func roll_animation_finished():
	velocity = velocity * 0.8
	state = MOVE



func attack_state():
	velocity = Vector2.ZERO
	animationState.travel("Attack")

func attack_animation_finished():
	state = MOVE


func _on_Hurtbox_area_entered(area):
	#if state != ROLL and not hurtbox.invincible:
	if not hurtbox.invincible:
		stats.health -= area.damage
		hurtbox.start_invincibility(0.8)
		hurtbox.create_hit_effect(area)
		var playerHurtSound = PlayerHurtSound.instance()
		get_tree().current_scene.add_child(playerHurtSound)


func _on_Hurtbox_invincibility_started():
	blinkAnimationPlayer.play("Start")
	
	
func _on_Hurtbox_invincibility_ended():
	blinkAnimationPlayer.play("Stop")
