class ActionKind(Enum):
    RunningLeft = 0
    RunningRight = 1
    Idle = 2
    IdleLeft = 3
    IdleRight = 4
    JumpingLeft = 5
    JumpingRight = 6
    CrouchLeft = 7
    CrouchRight = 8
    Flying = 9
    Walking = 10
    Jumping = 11
@namespace
class SpriteKind:
    Bumper = SpriteKind.create()
    Goal = SpriteKind.create()
    Coin = SpriteKind.create()
    Flier = SpriteKind.create()

def on_on_overlap(sprite, otherSprite):
    if sprite.vy > 0 and not (sprite.is_hitting_tile(CollisionDirection.BOTTOM)) or sprite.y < otherSprite.top:
        otherSprite.destroy(effects.ashes, 250)
        otherSprite.vy = -50
        sprite.vy = -2 * pixelsToMeters
        info.change_score_by(1)
        music.power_up.play()
    else:
        info.change_life_by(-1)
        sprite.say("Ow!", invincibilityPeriod)
        music.power_down.play()
    pause(invincibilityPeriod)
sprites.on_overlap(SpriteKind.player, SpriteKind.Bumper, on_on_overlap)

def initializeAnimations():
    initializeHeroAnimations()
    initializeCoinAnimation()
    initializeFlierAnimations()
def giveIntroduction():
    game.set_dialog_frame(img("""
        . 3 3 3 3 3 3 3 3 3 3 3 3 3 . . 
                3 3 d d d d d d d d d d d 3 3 . 
                3 d d 3 3 3 3 3 3 3 3 3 d d 3 . 
                3 d 3 3 d d d d d d d 3 3 d 3 . 
                3 d 3 d d d d d d d d d 3 d 3 . 
                3 d 3 d d d d d d d d d 3 d 3 . 
                3 d 3 d d d d d d d d d 3 d 3 . 
                3 d 3 d d d d d d d d d 3 d 3 . 
                3 d 3 d d d d d d d d d 3 d 3 . 
                3 d 3 d d d d d d d d d 3 d 3 . 
                3 d 3 d d d d d d d d d 3 d 3 . 
                3 d 3 3 d d d d d d d 3 3 d 3 . 
                3 d d 3 3 3 3 3 3 3 3 3 d d 3 . 
                3 3 d d d d d d d d d d d 3 3 . 
                . 3 3 3 3 3 3 3 3 3 3 3 3 3 . . 
                . . . . . . . . . . . . . . . .
    """))
    game.set_dialog_cursor(assets.image("""
        gem 1
    """))
    showInstruction("Move with the left and right buttons.")
    showInstruction("Jump with the up or A button.")
    showInstruction("Double jump by pressing jump again.")

def on_up_pressed():
    attemptJump()
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def initializeCoinAnimation():
    global coinAnimation
    coinAnimation = animation.create_animation(ActionKind.Idle, 200)
    coinAnimation.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . 3 3 . . . . . . . 
                . . . . . . 3 3 3 3 . . . . . . 
                . . . . 3 3 b 3 3 b 3 3 . . . . 
                . . . . 3 3 3 b b 3 3 3 . . . . 
                . . . 3 b 3 b 5 5 b 3 b 3 . . . 
                . . 3 3 3 b 5 5 5 5 b 3 3 3 . . 
                . . 3 3 3 b 5 5 5 5 b 3 3 3 . . 
                . . . 3 b 3 b 5 5 b 3 b 3 . . . 
                . . . . 3 3 3 b b 3 3 3 . . . . 
                . . . . 3 3 b 3 3 b 3 3 . . . . 
                . . . . . . 3 3 3 3 . . . . . . 
                . . . . . . . 3 3 . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    coinAnimation.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . 3 3 . . . . . . 
                . . . . . 3 3 3 3 3 . . . . . . 
                . . . . 3 3 3 b 3 3 . 3 . . . . 
                . . . . . 3 3 b b 3 3 3 3 . . . 
                . . 3 3 3 3 b 5 5 b 3 3 3 . . . 
                . . 3 3 3 b 5 5 5 5 b b 3 . . . 
                . . . 3 b b 5 5 5 5 b 3 3 3 . . 
                . . . 3 3 3 b 5 5 b 3 3 3 3 . . 
                . . . 3 3 3 3 b b 3 3 . . . . . 
                . . . . 3 . 3 3 b 3 3 3 . . . . 
                . . . . . . 3 3 3 3 3 . . . . . 
                . . . . . . 3 3 . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    coinAnimation.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . 3 3 . . . . . 
                . . . . . . 3 3 3 3 3 . . . . . 
                . . . . 3 3 3 3 b 3 3 3 . . . . 
                . . 3 3 3 b 3 b b 3 b 3 . . . . 
                . . 3 3 3 3 b 5 5 b 3 3 3 . . . 
                . . . 3 b b 5 5 5 5 b 3 3 . . . 
                . . . 3 3 b 5 5 5 5 b b 3 . . . 
                . . . 3 3 3 b 5 5 b 3 3 3 3 . . 
                . . . . 3 b 3 b b 3 b 3 3 3 . . 
                . . . . 3 3 3 b 3 3 3 3 . . . . 
                . . . . . 3 3 3 3 3 . . . . . . 
                . . . . . 3 3 . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    coinAnimation.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . 3 3 . . . . 
                . . . . . . 3 3 3 3 3 3 . . . . 
                . . 3 3 3 3 b 3 3 b 3 3 . . . . 
                . . 3 3 3 3 3 b b 3 3 3 . . . . 
                . . . 3 b 3 b 5 5 b 3 b 3 . . . 
                . . . 3 3 b 5 5 5 5 b 3 3 . . . 
                . . . 3 3 b 5 5 5 5 b 3 3 . . . 
                . . . 3 b 3 b 5 5 b 3 b 3 . . . 
                . . . . 3 3 3 b b 3 3 3 3 3 . . 
                . . . . 3 3 b 3 3 b 3 3 3 3 . . 
                . . . . 3 3 3 3 3 3 . . . . . . 
                . . . . 3 3 . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    coinAnimation.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . 3 3 . . . . . . . . . . 
                . . . . 3 3 3 3 3 3 . . . . . . 
                . . . . 3 3 b 3 3 b 3 3 3 3 . . 
                . . . . 3 3 3 b b 3 3 3 3 3 . . 
                . . . 3 b 3 b 5 5 b 3 b 3 . . . 
                . . . 3 3 b 5 5 5 5 b 3 3 . . . 
                . . . 3 3 b 5 5 5 5 b 3 3 . . . 
                . . . 3 b 3 b 5 5 b 3 b 3 . . . 
                . . 3 3 3 3 3 b b 3 3 3 . . . . 
                . . 3 3 3 3 b 3 3 b 3 3 . . . . 
                . . . . . . 3 3 3 3 3 3 . . . . 
                . . . . . . . . . . 3 3 . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    coinAnimation.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . 3 3 . . . . . . . . . 
                . . . . . 3 3 3 3 3 . . . . . . 
                . . . . 3 3 3 b 3 3 3 3 . . . . 
                . . . . 3 b 3 b b 3 b 3 3 3 . . 
                . . . 3 3 3 b 5 5 b 3 3 3 3 . . 
                . . . 3 3 b 5 5 5 5 b b 3 . . . 
                . . . 3 b b 5 5 5 5 b 3 3 . . . 
                . . 3 3 3 3 b 5 5 b 3 3 3 . . . 
                . . 3 3 3 b 3 b b 3 b 3 . . . . 
                . . . . 3 3 3 3 b 3 3 3 . . . . 
                . . . . . . 3 3 3 3 3 . . . . . 
                . . . . . . . . . 3 3 . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    coinAnimation.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . 3 3 . . . . . . . . 
                . . . . . . 3 3 3 3 3 . . . . . 
                . . . . 3 . 3 3 b 3 3 3 . . . . 
                . . . 3 3 3 3 b b 3 3 . . . . . 
                . . . 3 3 3 b 5 5 b 3 3 3 3 . . 
                . . . 3 b b 5 5 5 5 b 3 3 3 . . 
                . . 3 3 3 b 5 5 5 5 b b 3 . . . 
                . . 3 3 3 3 b 5 5 b 3 3 3 . . . 
                . . . . . 3 3 b b 3 3 3 3 . . . 
                . . . . 3 3 3 b 3 3 . 3 . . . . 
                . . . . . 3 3 3 3 3 . . . . . . 
                . . . . . . . . 3 3 . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))

def on_on_overlap2(sprite2, otherSprite2):
    otherSprite2.destroy(effects.trail, 250)
    otherSprite2.y += -3
    info.change_score_by(3)
    music.ba_ding.play()
sprites.on_overlap(SpriteKind.player, SpriteKind.Coin, on_on_overlap2)

def attemptJump():
    global doubleJumpSpeed, canDoubleJump
    # else if: either fell off a ledge, or double jumping
    if hero.is_hitting_tile(CollisionDirection.BOTTOM):
        hero.vy = -4 * pixelsToMeters
    elif canDoubleJump:
        doubleJumpSpeed = -3 * pixelsToMeters
        # Good double jump
        if hero.vy >= -40:
            doubleJumpSpeed = -4.5 * pixelsToMeters
            hero.start_effect(effects.trail, 500)
            scene.camera_shake(2, 250)
        hero.vy = doubleJumpSpeed
        canDoubleJump = False
def animateIdle():
    global mainIdleLeft, mainIdleRight
    mainIdleLeft = animation.create_animation(ActionKind.IdleLeft, 100)
    animation.attach_animation(hero, mainIdleLeft)
    mainIdleLeft.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . f f f f f f b f . . . . 
                . . . f f f f f f b 5 b f . . . 
                . . f f f f 4 4 4 f b f f . . . 
                . . f f f f f 4 f f f f f f . . 
                . . f f 4 6 1 4 6 1 4 f 4 f . . 
                . . . f 4 6 1 4 6 1 4 4 f f . . 
                . . . f 3 3 4 4 4 3 3 4 f 7 f . 
                . . . f 9 4 4 2 4 4 4 4 9 f f . 
                . . . 9 9 9 4 4 4 9 9 9 9 9 . . 
                . . . . 4 9 4 4 9 9 d 9 4 f . . 
                . . . . 4 d 9 9 9 9 9 9 4 f . . 
                . . . . . 9 9 9 d 9 9 9 . f . . 
                . . . . . 9 9 9 9 9 9 9 . . . . 
                . . . . 9 9 9 4 9 4 9 d 9 . . . 
                . . . . . 4 4 4 . 4 4 4 . . . .
    """))
    mainIdleRight = animation.create_animation(ActionKind.IdleRight, 100)
    animation.attach_animation(hero, mainIdleRight)
    mainIdleRight.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . f b f f f f f f . . . . 
                . . . f b 5 b f f f f f f . . . 
                . . . f f b f 4 4 4 f f f f . . 
                . . f f f f f f 4 f f f f f . . 
                . . f 4 f 4 1 6 4 1 6 4 f f . . 
                . . f f 4 4 1 6 4 1 6 4 f . . . 
                . f 7 f 4 3 3 4 4 4 3 3 f . . . 
                . f f 9 4 4 4 4 2 4 4 9 f . . . 
                . . 9 9 9 9 9 4 4 4 9 9 9 . . . 
                . . f 4 9 d 9 9 4 4 9 4 . . . . 
                . . f 4 9 9 9 9 9 9 d 4 . . . . 
                . . f . 9 9 9 d 9 9 9 . . . . . 
                . . . . 9 9 9 9 9 9 9 . . . . . 
                . . . 9 d 9 4 9 4 9 9 9 . . . . 
                . . . . 4 4 4 . 4 4 4 . . . . .
    """))
def setLevelTileMap(level: number):
    clearGame()
    if level == 0:
        tiles.set_tilemap(tilemap("""
            level
        """))
    elif level == 1:
        tiles.set_tilemap(tilemap("""
            level_0
        """))
    elif level == 2:
        tiles.set_tilemap(tilemap("""
            level_1
        """))
    elif level == 3:
        tiles.set_tilemap(tilemap("""
            level_2
        """))
    elif level == 4:
        tiles.set_tilemap(tilemap("""
            level_3
        """))
    elif level == 5:
        tiles.set_tilemap(tilemap("""
            level_4
        """))
    elif level == 6:
        tiles.set_tilemap(tilemap("""
            level_5
        """))
    elif level == 7:
        tiles.set_tilemap(tilemap("""
            level_6
        """))
    initializeLevel(level)
def initializeFlierAnimations():
    global flierFlying, flierIdle
    flierFlying = animation.create_animation(ActionKind.Flying, 100)
    flierFlying.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . f f f f f f f . . . . 
                . . . . f 4 4 4 4 4 4 4 f . . . 
                . . . f 4 5 5 4 4 4 5 5 4 f . . 
                . f . f 4 4 4 5 4 5 4 4 4 f . f 
                . f f 4 4 4 4 4 4 4 4 4 4 4 f f 
                . f 4 4 4 4 4 5 4 5 4 4 4 4 4 f 
                . f 4 4 4 4 4 5 4 5 4 4 4 4 4 f 
                . f f 4 4 4 4 4 4 4 4 4 4 4 f f 
                . . . f 4 4 5 5 5 5 5 4 4 f . . 
                . . . . f 4 5 4 4 4 5 4 f . . . 
                . . . . . f f f f f f f . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    flierFlying.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . f f f f f f f . . . . 
                . . . . f 4 4 4 4 4 4 4 f . . . 
                . . . f 4 5 5 4 4 4 5 5 4 f . . 
                . . . f 4 4 4 5 4 5 4 4 4 f . . 
                . . f 4 4 4 4 4 4 4 4 4 4 4 f . 
                . . f 4 4 4 4 5 4 5 4 4 4 4 f . 
                . f 4 4 4 4 4 5 4 5 4 4 4 4 4 f 
                . f 4 4 4 4 4 4 4 4 4 4 4 4 4 f 
                . f 4 f 4 4 5 5 5 5 5 4 4 f 4 f 
                . f f . f 4 5 4 4 4 5 4 f . f f 
                . f . . . f f f f f f f . . . f 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    flierFlying.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . f f f f f f f . . . . 
                . . . . f 4 4 4 4 4 4 4 f . . . 
                . . . f 4 5 5 4 4 4 5 5 4 f . . 
                . f . f 4 4 4 5 4 5 4 4 4 f . f 
                . f f 4 4 4 4 4 4 4 4 4 4 4 f f 
                . f 4 4 4 4 4 5 4 5 4 4 4 4 4 f 
                . f 4 4 4 4 4 5 4 5 4 4 4 4 4 f 
                . f f 4 4 4 4 4 4 4 4 4 4 4 f f 
                . . . f 4 4 5 5 5 5 5 4 4 f . . 
                . . . . f 4 5 4 4 4 5 4 f . . . 
                . . . . . f f f f f f f . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    flierIdle = animation.create_animation(ActionKind.Idle, 100)
    flierIdle.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . f f f f f f f . . . . 
                . . . . f 4 4 4 4 4 4 4 f . . . 
                . . . f 4 5 5 4 4 4 5 5 4 f . . 
                . f . f 4 4 4 5 4 5 4 4 4 f . f 
                . f f 4 4 4 4 4 4 4 4 4 4 4 f f 
                . f 4 4 4 4 4 5 4 5 4 4 4 4 4 f 
                . f 4 4 4 4 4 5 4 5 4 4 4 4 4 f 
                . f f 4 4 4 4 4 4 4 4 4 4 4 f f 
                . . . f 4 4 5 5 5 5 5 4 4 f . . 
                . . . . f 4 5 4 4 4 5 4 f . . . 
                . . . . . f f f f f f f . . . . 
                . . . . . . . . . . . . . . . . 
                . . . . . . . . . . . . . . . .
    """))

def on_a_pressed():
    attemptJump()
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def animateRun():
    global mainRunLeft, mainRunRight
    mainRunLeft = animation.create_animation(ActionKind.RunningLeft, 100)
    animation.attach_animation(hero, mainRunLeft)
    mainRunLeft.add_animation_frame(assets.image("""
        side
    """))
    mainRunLeft.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . f f f f b f f . . . . . . . 
                . . f f f b 5 b f f . . . . . . 
                . f f f 4 f b f f f f . . . . . 
                f f f 4 6 1 4 f 4 f f . . . . . 
                . f f 4 6 1 4 f f f . . . . . . 
                . f . 4 4 3 3 4 f f . . . . . . 
                . f . 2 4 4 4 4 f 7 f . . . . . 
                . . . 4 4 9 9 9 7 f f . . . . . 
                . . . 4 9 d 9 9 . f . . . . . . 
                . . . 9 9 9 9 9 . f . . . . . . 
                . . . 9 9 4 9 9 . f . . . . . . 
                . . . 9 9 9 d 9 . . . . . . . . 
                . . . d 9 9 9 9 . . . . . . . . 
                . . 9 4 9 9 4 9 9 . . . . . . . 
                . . 4 4 . 4 4 . . . . . . . . .
    """))
    mainRunLeft.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . f f f f b f f . . . . . . 
                . . . f f f b 5 b f f . . . . . 
                . . f f f 4 f b f f f f . . . . 
                . f f f 4 6 1 4 f 4 f f . . . . 
                . . f f 4 6 1 4 f f f . . . . . 
                . . f . 4 4 3 3 4 f f . . . . . 
                . . f . 2 4 4 4 4 f 7 f . . . . 
                . . . . 4 4 9 9 9 7 f f . . . . 
                . . . . 4 9 d 9 9 . f . . . . . 
                . . . . 9 9 9 9 9 . f . . . . . 
                . . . . 9 9 4 9 9 . f . . . . . 
                . . . . 9 9 9 d 9 . . . . . . . 
                . . . . d 9 9 9 9 . . . . . . . 
                . . . 9 9 4 9 9 4 9 . . . . . . 
                . . . . 4 4 . 4 4 . . . . . . .
    """))
    mainRunLeft.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . f f f f b f f . . . . . . . 
                . . f f f b 5 b f f . . . . . . 
                . f f f 4 f b f f f f . . . . . 
                f f f 4 6 1 4 f 4 f f . . . . . 
                . f f 4 6 1 4 f f f . . . . . . 
                . f . 4 4 3 3 4 f f . . . . . . 
                . f . 2 4 4 4 4 f 7 f . . . . . 
                . . . 4 4 9 9 9 7 f f . . . . . 
                . . . 4 9 d 9 9 . f . . . . . . 
                . . . 9 9 9 9 9 . f . . . . . . 
                . . . 9 4 4 9 9 . f . . . . . . 
                . . 9 9 9 9 d 9 . . . . . . . . 
                . . 9 d 9 9 9 9 . . . . . . . . 
                . 9 9 4 9 9 9 4 9 . . . . . . . 
                . . 4 4 . . 4 4 . . . . . . . .
    """))
    mainRunRight = animation.create_animation(ActionKind.RunningRight, 100)
    animation.attach_animation(hero, mainRunRight)
    mainRunRight.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . f f b f f f f . . . 
                . . . . . f f b 5 b f f f . . . 
                . . . . f f f f b f 4 f f f . . 
                . . . . f f 4 f 4 1 6 4 f f f . 
                . . . . . f f f 4 1 6 4 f f . . 
                . . . . . f f 4 3 3 4 4 . f . . 
                . . . . f 7 f 4 4 4 4 2 . f . . 
                . . . . f f 7 9 9 9 4 4 . . . . 
                . . . . . f . 9 9 d 9 4 . . . . 
                . . . . . f . 9 9 9 9 9 . . . . 
                . . . . . f . 9 9 4 9 9 . . . . 
                . . . . . . . 9 d 9 9 9 . . . . 
                . . . . . . . 9 9 9 9 d . . . . 
                . . . . . . 9 4 9 9 4 9 9 . . . 
                . . . . . . . 4 4 . 4 4 . . . .
    """))
    mainRunRight.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . f f b f f f f . . . 
                . . . . . f f b 5 b f f f . . . 
                . . . . f f f f b f 4 f f f . . 
                . . . . f f 4 f 4 1 6 4 f f f . 
                . . . . . f f f 4 1 6 4 f f . . 
                . . . . . f f 4 3 3 4 4 . f . . 
                . . . . f 7 f 4 4 4 4 2 . f . . 
                . . . . f f 7 9 9 9 4 4 . . . . 
                . . . . . f . 9 9 d 9 4 . . . . 
                . . . . . f . 9 9 9 9 9 . . . . 
                . . . . . f . 9 9 4 9 9 . . . . 
                . . . . . . . 9 d 9 9 9 . . . . 
                . . . . . . . 9 9 9 9 d . . . . 
                . . . . . . 9 9 4 9 9 4 9 . . . 
                . . . . . . . . 4 4 . 4 4 . . .
    """))
    mainRunRight.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . f f b f f f f . . . 
                . . . . . f f b 5 b f f f . . . 
                . . . . f f f f b f 4 f f f . . 
                . . . . f f 4 f 4 1 6 4 f f f . 
                . . . . . f f f 4 1 6 4 f f . . 
                . . . . . f f 4 3 3 4 4 . f . . 
                . . . . f 7 f 4 4 4 4 2 . f . . 
                . . . . f f 7 9 9 9 4 4 . . . . 
                . . . . . f . 9 9 d 9 4 . . . . 
                . . . . . f . 9 9 9 9 9 . . . . 
                . . . . . f . 9 9 4 9 9 . . . . 
                . . . . . . . 9 d 9 9 9 . . . . 
                . . . . . . . 9 9 9 9 d . . . . 
                . . . . . . 9 4 9 9 4 9 9 . . . 
                . . . . . . . 4 4 . 4 4 . . . .
    """))
    mainRunRight.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . . . f f b f f f f . . 
                . . . . . . f f b 5 b f f f . . 
                . . . . . f f f f b f 4 f f f . 
                . . . . . f f 4 f 4 1 6 4 f f f 
                . . . . . . f f f 4 1 6 4 f f . 
                . . . . . . f f 4 3 3 4 4 . f . 
                . . . . . f 7 f 4 4 4 4 2 . f . 
                . . . . . f f 7 9 9 9 4 4 . . . 
                . . . . . . f . 9 9 d 9 4 . . . 
                . . . . . . f . 9 9 9 9 9 . . . 
                . . . . . . f . 9 9 4 4 9 . . . 
                . . . . . . . . 9 d 9 9 9 9 . . 
                . . . . . . . . 9 9 9 9 d 9 . . 
                . . . . . . . 9 4 9 9 9 4 9 9 . 
                . . . . . . . . 4 4 . . 4 4 . .
    """))
def animateJumps():
    global mainJumpLeft, mainJumpRight
    # Because there isn't currently an easy way to say "play this animation a single time
    # and stop at the end", this just adds a bunch of the same frame at the end to accomplish
    # the same behavior
    mainJumpLeft = animation.create_animation(ActionKind.JumpingLeft, 100)
    animation.attach_animation(hero, mainJumpLeft)
    mainJumpLeft.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . f f f f f f b f . . . . 
                . . . f f f f f f b 5 b f . . . 
                . . f f f f 4 4 4 f b f f . . . 
                . . f f f f f 4 f f f f f f . . 
                . . f f 4 6 1 4 6 1 4 f 4 f . . 
                . . . f 4 6 1 4 6 1 4 4 f f . . 
                . . . f 3 3 4 4 4 3 3 4 f 7 f . 
                . . . f 9 4 4 2 4 4 4 4 9 f f . 
                . . . 9 9 9 4 4 4 9 9 9 9 9 . . 
                . . . . 4 9 4 4 9 9 d 9 4 f . . 
                . . . . 4 d 9 9 9 9 9 9 4 f . . 
                . . . . . 9 9 9 d 9 9 9 . f . . 
                . . . . . 9 9 9 9 9 9 9 . . . . 
                . . . . 9 9 9 4 9 4 9 d 9 . . . 
                . . . . . 4 4 4 . 4 4 4 . . . .
    """))
    mainJumpLeft.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . f f f f f f b f . . . . 
                . . . f f f f f f b 5 b f . . . 
                . . f f f f 4 4 4 f b f f . . . 
                . . f f f f f 4 f f f f f f . . 
                . . f f 4 6 1 4 6 1 4 f 4 f . . 
                . . . f 4 6 1 4 6 1 4 4 f f . . 
                . . . f 3 3 4 4 4 3 3 4 f 7 f . 
                . . . f 9 4 4 2 4 4 4 4 9 f f . 
                . . . 9 9 9 4 4 4 9 9 9 9 9 . . 
                . . . . 4 9 4 4 9 9 d 9 4 f . . 
                . . . . 4 d 9 9 9 9 9 9 4 f . . 
                . . . . . 9 9 9 d 9 9 9 . f . . 
                . . . . 9 9 9 9 9 9 9 9 9 . . . 
                . . . . . 4 4 4 . 4 4 4 . . . . 
                . . . . . . . . . . . . . . . .
    """))
    for index in range(30):
        mainJumpLeft.add_animation_frame(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . f f f f f f b f . . . . 
                        . . . f f f f f f b 5 b f . . . 
                        . . f f f f 4 4 4 f b f f . . . 
                        . . f f f f f 4 f f f f f f . . 
                        . . f f 4 6 1 4 6 1 4 f 4 f . . 
                        . . . f 4 6 1 4 6 1 4 4 f f . . 
                        . . . f 3 3 4 4 4 3 3 4 f 7 f . 
                        . . . f 9 4 4 2 4 4 4 4 9 f f . 
                        . . . 9 9 9 4 4 4 9 9 9 9 9 . . 
                        . . . . 4 9 4 4 9 9 d 9 4 f . . 
                        . . . . 4 d 9 9 9 9 9 9 4 f . . 
                        . . . . 9 9 9 9 d 9 9 9 9 f . . 
                        . . . . 9 9 9 9 9 9 9 9 9 . . . 
                        . . . . . 4 4 4 . 4 4 4 . . . . 
                        . . . . . . . . . . . . . . . .
        """))
    mainJumpRight = animation.create_animation(ActionKind.JumpingRight, 100)
    animation.attach_animation(hero, mainJumpRight)
    mainJumpRight.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . f b f f f f f f . . . . 
                . . . f b 5 b f f f f f f . . . 
                . . . f f b f 4 4 4 f f f f . . 
                . . f f f f f f 4 f f f f f . . 
                . . f 4 f 4 1 6 4 1 6 4 f f . . 
                . . f f 4 4 1 6 4 1 6 4 f . . . 
                . f 7 f 4 3 3 4 4 4 3 3 f . . . 
                . f f 9 4 4 4 4 2 4 4 9 f . . . 
                . . 9 9 9 9 9 4 4 4 9 9 9 . . . 
                . . f 4 9 d 9 9 4 4 9 4 . . . . 
                . . f 4 9 9 9 9 9 9 d 4 . . . . 
                . . f . 9 9 9 d 9 9 9 . . . . . 
                . . . . 9 9 9 9 9 9 9 . . . . . 
                . . . 9 d 9 4 9 4 9 9 9 . . . . 
                . . . . 4 4 4 . 4 4 4 . . . . .
    """))
    mainJumpRight.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . f b f f f f f f . . . . 
                . . . f b 5 b f f f f f f . . . 
                . . . f f b f 4 4 4 f f f f . . 
                . . f f f f f f 4 f f f f f . . 
                . . f 4 f 4 1 6 4 1 6 4 f f . . 
                . . f f 4 4 1 6 4 1 6 4 f . . . 
                . f 7 f 4 3 3 4 4 4 3 3 f . . . 
                . f f 9 4 4 4 4 2 4 4 9 f . . . 
                . . 9 9 9 9 9 4 4 4 9 9 9 . . . 
                . . f 4 9 d 9 9 4 4 9 4 . . . . 
                . . f 4 9 9 9 9 9 9 d 4 . . . . 
                . . f . 9 9 9 d 9 9 9 . . . . . 
                . . . 9 9 9 9 9 9 9 9 9 . . . . 
                . . . . 4 4 4 . 4 4 4 . . . . . 
                . . . . . . . . . . . . . . . .
    """))
    for index2 in range(30):
        mainJumpRight.add_animation_frame(img("""
            . . . . . . . . . . . . . . . . 
                        . . . . f b f f f f f f . . . . 
                        . . . f b 5 b f f f f f f . . . 
                        . . . f f b f 4 4 4 f f f f . . 
                        . . f f f f f f 4 f f f f f . . 
                        . . f 4 f 4 1 6 4 1 6 4 f f . . 
                        . . f f 4 4 1 6 4 1 6 4 f . . . 
                        . f 7 f 4 3 3 4 4 4 3 3 f . . . 
                        . f f 9 4 4 4 4 2 4 4 9 f . . . 
                        . . 9 9 9 9 9 4 4 4 9 9 9 . . . 
                        . . f 4 9 d 9 9 4 4 9 4 . . . . 
                        . . f 4 9 9 9 9 9 9 d 4 . . . . 
                        . . f 9 9 9 9 d 9 9 9 9 . . . . 
                        . . . 9 9 9 9 9 9 9 9 9 . . . . 
                        . . . . 4 4 4 . 4 4 4 . . . . . 
                        . . . . . . . . . . . . . . . .
        """))
def animateCrouch():
    global mainCrouchLeft, mainCrouchRight
    mainCrouchLeft = animation.create_animation(ActionKind.CrouchLeft, 100)
    animation.attach_animation(hero, mainCrouchLeft)
    mainCrouchLeft.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . f f f f f f b f . . . . . 
                . . f f f f f f b 5 b f . . . . 
                . f f f f 4 4 4 f b f f . . . . 
                . f f f f f 4 f f f f f f . . . 
                . f f 4 6 1 4 6 1 4 f 4 f . . . 
                . . f 4 6 1 4 6 1 4 4 f f . . . 
                . . f 3 3 4 4 4 3 3 4 f 7 f . . 
                . . f 9 4 4 2 4 4 4 4 9 f f . . 
                . . 9 9 9 4 4 4 9 9 9 9 9 . . . 
                . . . 4 9 4 4 9 9 d 9 4 f . . . 
                . 4 4 4 d 9 9 9 9 9 4 4 f . . . 
                . . . . 9 9 9 d 9 9 9 . f . . . 
                . . . . 9 9 9 9 9 9 9 . . . . . 
                . . . 9 9 9 4 9 4 9 d 9 . . . . 
                . . . . 4 4 4 . 4 4 4 . . . . .
    """))
    mainCrouchRight = animation.create_animation(ActionKind.CrouchRight, 100)
    animation.attach_animation(hero, mainCrouchRight)
    mainCrouchRight.add_animation_frame(img("""
        . . . . . . . . . . . . . . . . 
                . . . . . f b f f f f f f . . . 
                . . . . f b 5 b f f f f f f . . 
                . . . . f f b f 4 4 4 f f f f . 
                . . . f f f f f f 4 f f f f f . 
                . . . f 4 f 4 1 6 4 1 6 4 f f . 
                . . . f f 4 4 1 6 4 1 6 4 f . . 
                . . f 7 f 4 3 3 4 4 4 3 3 f . . 
                . . f f 9 4 4 4 4 2 4 4 9 f . . 
                . . . 9 9 9 9 9 4 4 4 9 9 9 . . 
                . . . f 4 9 d 9 9 4 4 9 4 . . . 
                . . . f 4 4 9 9 9 9 9 d 4 4 4 . 
                . . . f . 9 9 9 d 9 9 9 . . . . 
                . . . . . 9 9 9 9 9 9 9 . . . . 
                . . . . 9 d 9 4 9 4 9 9 9 . . . 
                . . . . . 4 4 4 . 4 4 4 . . . .
    """))
def clearGame():
    for value in sprites.all_of_kind(SpriteKind.Bumper):
        value.destroy()
    for value2 in sprites.all_of_kind(SpriteKind.Coin):
        value2.destroy()
    for value3 in sprites.all_of_kind(SpriteKind.Goal):
        value3.destroy()
    for value4 in sprites.all_of_kind(SpriteKind.Flier):
        value4.destroy()

def on_on_overlap3(sprite3, otherSprite3):
    info.change_life_by(-1)
    sprite3.say("Ow!", invincibilityPeriod * 1.5)
    music.power_down.play()
    pause(invincibilityPeriod * 1.5)
sprites.on_overlap(SpriteKind.player, SpriteKind.Flier, on_on_overlap3)

def on_overlap_tile(sprite4, location):
    global currentLevel
    info.change_life_by(1)
    currentLevel += 1
    if hasNextLevel():
        game.splash("Next level unlocked!")
        setLevelTileMap(currentLevel)
    else:
        game.over(True, effects.confetti)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        endpoint
    """),
    on_overlap_tile)

def createEnemies():
    global bumper, flier
    # enemy that moves back and forth
    for value5 in tiles.get_tiles_by_type(assets.tile("""
        tile4
    """)):
        bumper = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . f f f f f f . . . . . . 
                            . . . f 7 2 7 7 7 2 f . . . . . 
                            . . f 7 7 7 2 7 2 7 7 f . . . . 
                            . . f 7 7 7 7 7 7 7 7 7 f . . . 
                            . f 7 7 7 2 7 7 7 2 7 7 f . . . 
                            . f 7 7 7 2 7 7 7 2 7 7 7 f . . 
                            . f 7 7 7 7 7 7 7 7 7 7 7 7 f . 
                            . f 7 7 7 7 2 2 2 7 7 7 7 7 f . 
                            . . f 7 7 2 2 7 2 2 7 7 7 7 f . 
                            . . f 7 7 2 7 7 7 2 2 7 7 7 f . 
                            . . . f 7 7 7 7 7 7 7 7 7 7 f . 
                            . . . . f f 7 7 7 7 7 7 7 f . . 
                            . . . . . . f f f f f f f . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Bumper)
        tiles.place_on_tile(bumper, value5)
        tiles.set_tile_at(value5, assets.tile("""
            tile0
        """))
        bumper.ay = gravity
        if Math.percent_chance(50):
            bumper.vx = Math.random_range(30, 60)
        else:
            bumper.vx = Math.random_range(-60, -30)
    # enemy that flies at player
    for value6 in tiles.get_tiles_by_type(assets.tile("""
        tile7
    """)):
        flier = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . f f f f f f f . . . . 
                            . . . . f 4 4 4 4 4 4 4 f . . . 
                            . . . f 4 5 5 4 4 4 5 5 4 f . . 
                            . f . f 4 4 4 5 4 5 4 4 4 f . f 
                            . f f 4 4 4 4 4 4 4 4 4 4 4 f f 
                            . f 4 4 4 4 4 5 4 5 4 4 4 4 4 f 
                            . f 4 4 4 4 4 5 4 5 4 4 4 4 4 f 
                            . f f 4 4 4 4 4 4 4 4 4 4 4 f f 
                            . . . f 4 4 5 5 5 5 5 4 4 f . . 
                            . . . . f 4 5 4 4 4 5 4 f . . . 
                            . . . . . f f f f f f f . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Flier)
        tiles.place_on_tile(flier, value6)
        tiles.set_tile_at(value6, assets.tile("""
            tile0
        """))
        animation.attach_animation(flier, flierFlying)
        animation.attach_animation(flier, flierIdle)

def on_down_pressed():
    if not (hero.is_hitting_tile(CollisionDirection.BOTTOM)):
        hero.vy += 80
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def showInstruction(text: str):
    game.show_long_text(text, DialogLayout.BOTTOM)
    music.ba_ding.play()
    info.change_score_by(1)
def initializeHeroAnimations():
    animateRun()
    animateIdle()
    animateCrouch()
    animateJumps()
def createPlayer(player2: Sprite):
    player2.ay = gravity
    scene.camera_follow_sprite(player2)
    controller.move_sprite(player2, 100, 0)
    player2.z = 5
    info.set_life(3)
    info.set_score(0)
def initializeLevel(level2: number):
    global playerStartLocation
    effects.clouds.start_screen_effect()
    playerStartLocation = tiles.get_tiles_by_type(assets.tile("""
        tile6
    """))[0]
    tiles.place_on_tile(hero, playerStartLocation)
    tiles.set_tile_at(playerStartLocation, assets.tile("""
        tile0
    """))
    createEnemies()
    spawnGoals()
def hasNextLevel():
    return currentLevel != levelCount
def spawnGoals():
    global coin
    for value7 in tiles.get_tiles_by_type(assets.tile("""
        gem 1
    """)):
        coin = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . 3 3 . . . . . . . 
                            . . . . . . 3 3 3 3 . . . . . . 
                            . . . . 3 3 b 3 3 b 3 3 . . . . 
                            . . . . 3 3 3 b b 3 3 3 . . . . 
                            . . . 3 b 3 b 5 5 b 3 b 3 . . . 
                            . . 3 3 3 b 5 5 5 5 b 3 3 3 . . 
                            . . 3 3 3 b 5 5 5 5 b 3 3 3 . . 
                            . . . 3 b 3 b 5 5 b 3 b 3 . . . 
                            . . . . 3 3 3 b b 3 3 3 . . . . 
                            . . . . 3 3 b 3 3 b 3 3 . . . . 
                            . . . . . . 3 3 3 3 . . . . . . 
                            . . . . . . . 3 3 . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . .
            """),
            SpriteKind.Coin)
        tiles.place_on_tile(coin, value7)
        animation.attach_animation(coin, coinAnimation)
        animation.set_action(coin, ActionKind.Idle)
        tiles.set_tile_at(value7, assets.tile("""
            tile0
        """))
heroFacingLeft = False
coin: Sprite = None
playerStartLocation: tiles.Location = None
flier: Sprite = None
bumper: Sprite = None
mainCrouchRight: animation.Animation = None
mainCrouchLeft: animation.Animation = None
mainJumpRight: animation.Animation = None
mainJumpLeft: animation.Animation = None
mainRunRight: animation.Animation = None
mainRunLeft: animation.Animation = None
flierIdle: animation.Animation = None
flierFlying: animation.Animation = None
mainIdleRight: animation.Animation = None
mainIdleLeft: animation.Animation = None
doubleJumpSpeed = 0
canDoubleJump = False
coinAnimation: animation.Animation = None
currentLevel = 0
levelCount = 0
gravity = 0
pixelsToMeters = 0
invincibilityPeriod = 0
hero: Sprite = None
hero = sprites.create(assets.image("""
    main_chara
"""), SpriteKind.player)
# how long to pause between each contact with a
# single enemy
invincibilityPeriod = 600
pixelsToMeters = 30
gravity = 9.81 * pixelsToMeters
scene.set_background_image(assets.image("""
    back
"""))
initializeAnimations()
createPlayer(hero)
levelCount = 8
currentLevel = 0
setLevelTileMap(currentLevel)
giveIntroduction()
# set up hero animations

def on_on_update():
    global heroFacingLeft
    if hero.vx < 0:
        heroFacingLeft = True
    elif hero.vx > 0:
        heroFacingLeft = False
    if hero.is_hitting_tile(CollisionDirection.TOP):
        hero.vy = 0
    if controller.down.is_pressed():
        if heroFacingLeft:
            animation.set_action(hero, ActionKind.CrouchLeft)
        else:
            animation.set_action(hero, ActionKind.CrouchRight)
    elif hero.vy < 20 and not (hero.is_hitting_tile(CollisionDirection.BOTTOM)):
        if heroFacingLeft:
            animation.set_action(hero, ActionKind.JumpingLeft)
        else:
            animation.set_action(hero, ActionKind.JumpingRight)
    elif hero.vx < 0:
        animation.set_action(hero, ActionKind.RunningLeft)
    elif hero.vx > 0:
        animation.set_action(hero, ActionKind.RunningRight)
    else:
        if heroFacingLeft:
            animation.set_action(hero, ActionKind.IdleLeft)
        else:
            animation.set_action(hero, ActionKind.IdleRight)
game.on_update(on_on_update)

# Flier movement

def on_on_update2():
    for value8 in sprites.all_of_kind(SpriteKind.Flier):
        if abs(value8.x - hero.x) < 60:
            if value8.x - hero.x < -5:
                value8.vx = 25
            elif value8.x - hero.x > 5:
                value8.vx = -25
            if value8.y - hero.y < -5:
                value8.vy = 25
            elif value8.y - hero.y > 5:
                value8.vy = -25
            animation.set_action(value8, ActionKind.Flying)
        else:
            value8.vy = -20
            value8.vx = 0
            animation.set_action(value8, ActionKind.Idle)
game.on_update(on_on_update2)

# Reset double jump when standing on wall

def on_on_update3():
    global canDoubleJump
    if hero.is_hitting_tile(CollisionDirection.BOTTOM):
        canDoubleJump = True
game.on_update(on_on_update3)

# bumper movement

def on_on_update4():
    for value9 in sprites.all_of_kind(SpriteKind.Bumper):
        if value9.is_hitting_tile(CollisionDirection.LEFT):
            value9.vx = Math.random_range(30, 60)
        elif value9.is_hitting_tile(CollisionDirection.RIGHT):
            value9.vx = Math.random_range(-60, -30)
game.on_update(on_on_update4)
