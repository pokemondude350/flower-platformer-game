namespace SpriteKind {
    export const Bumper = SpriteKind.create()
    export const Goal = SpriteKind.create()
    export const Coin = SpriteKind.create()
    export const Flier = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Bumper, function (sprite, otherSprite) {
    if (sprite.vy > 0 && !(sprite.isHittingTile(CollisionDirection.Bottom)) || sprite.y < otherSprite.top) {
        otherSprite.destroy(effects.ashes, 250)
        otherSprite.vy = -50
        sprite.vy = -2 * pixelsToMeters
        info.changeScoreBy(1)
        music.powerUp.play()
    } else {
        info.changeLifeBy(-1)
        sprite.say("Ow!", invincibilityPeriod)
        music.powerDown.play()
    }
    pause(invincibilityPeriod)
})
function initializeAnimations () {
    initializeHeroAnimations()
    initializeCoinAnimation()
    initializeFlierAnimations()
}
function giveIntroduction () {
    game.setDialogFrame(img`
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
        `)
    game.setDialogCursor(assets.image`gem 1`)
    showInstruction("Move with the left and right buttons.")
    showInstruction("Jump with the up or A button.")
    showInstruction("Double jump by pressing jump again.")
}
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    attemptJump()
})
function initializeCoinAnimation () {
    coinAnimation = animation.createAnimation(ActionKind.Idle, 200)
    coinAnimation.addAnimationFrame(img`
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
        `)
    coinAnimation.addAnimationFrame(img`
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
        `)
    coinAnimation.addAnimationFrame(img`
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
        `)
    coinAnimation.addAnimationFrame(img`
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
        `)
    coinAnimation.addAnimationFrame(img`
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
        `)
    coinAnimation.addAnimationFrame(img`
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
        `)
    coinAnimation.addAnimationFrame(img`
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
        `)
}
function attemptJump () {
    // else if: either fell off a ledge, or double jumping
    if (hero.isHittingTile(CollisionDirection.Bottom)) {
        hero.vy = -4 * pixelsToMeters
    } else if (canDoubleJump) {
        doubleJumpSpeed = -3 * pixelsToMeters
        // Good double jump
        if (hero.vy >= -40) {
            doubleJumpSpeed = -4.5 * pixelsToMeters
            hero.startEffect(effects.trail, 500)
            scene.cameraShake(2, 250)
        }
        hero.vy = doubleJumpSpeed
        canDoubleJump = false
    }
}
function animateIdle () {
    mainIdleLeft = animation.createAnimation(ActionKind.IdleLeft, 100)
    animation.attachAnimation(hero, mainIdleLeft)
    mainIdleLeft.addAnimationFrame(img`
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
        `)
    mainIdleRight = animation.createAnimation(ActionKind.IdleRight, 100)
    animation.attachAnimation(hero, mainIdleRight)
    mainIdleRight.addAnimationFrame(img`
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
        `)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Flier, function (sprite3, otherSprite3) {
    info.changeLifeBy(-1)
    sprite3.say("Ow!", invincibilityPeriod * 1.5)
    music.powerDown.play()
    pause(invincibilityPeriod * 1.5)
})
function setLevelTileMap (level: number) {
    clearGame()
    if (level == 0) {
        tiles.setTilemap(tilemap`level`)
    } else if (level == 1) {
        tiles.setTilemap(tilemap`level_0`)
    } else if (level == 2) {
        tiles.setTilemap(tilemap`level_1`)
    } else if (level == 3) {
        tiles.setTilemap(tilemap`level_2`)
    } else if (level == 4) {
        tiles.setTilemap(tilemap`level_3`)
    } else if (level == 5) {
        tiles.setTilemap(tilemap`level_4`)
    } else if (level == 6) {
        tiles.setTilemap(tilemap`level_5`)
    } else if (level == 7) {
        tiles.setTilemap(tilemap`level_6`)
    }
    initializeLevel(level)
}
function initializeFlierAnimations () {
    flierFlying = animation.createAnimation(ActionKind.Flying, 100)
    flierFlying.addAnimationFrame(img`
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
        `)
    flierFlying.addAnimationFrame(img`
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
        `)
    flierFlying.addAnimationFrame(img`
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
        `)
    flierIdle = animation.createAnimation(ActionKind.Idle, 100)
    flierIdle.addAnimationFrame(img`
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
        `)
}
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    attemptJump()
})
function animateRun () {
    mainRunLeft = animation.createAnimation(ActionKind.RunningLeft, 100)
    animation.attachAnimation(hero, mainRunLeft)
    mainRunLeft.addAnimationFrame(assets.image`side`)
    mainRunLeft.addAnimationFrame(img`
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
        `)
    mainRunLeft.addAnimationFrame(img`
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
        `)
    mainRunLeft.addAnimationFrame(img`
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
        `)
    mainRunRight = animation.createAnimation(ActionKind.RunningRight, 100)
    animation.attachAnimation(hero, mainRunRight)
    mainRunRight.addAnimationFrame(img`
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
        `)
    mainRunRight.addAnimationFrame(img`
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
        `)
    mainRunRight.addAnimationFrame(img`
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
        `)
    mainRunRight.addAnimationFrame(img`
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
        `)
}
function animateJumps () {
    // Because there isn't currently an easy way to say "play this animation a single time
    // and stop at the end", this just adds a bunch of the same frame at the end to accomplish
    // the same behavior
    mainJumpLeft = animation.createAnimation(ActionKind.JumpingLeft, 100)
    animation.attachAnimation(hero, mainJumpLeft)
    mainJumpLeft.addAnimationFrame(img`
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
        `)
    mainJumpLeft.addAnimationFrame(img`
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
        `)
    for (let index = 0; index < 30; index++) {
        mainJumpLeft.addAnimationFrame(img`
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
            `)
    }
    mainJumpRight = animation.createAnimation(ActionKind.JumpingRight, 100)
    animation.attachAnimation(hero, mainJumpRight)
    mainJumpRight.addAnimationFrame(img`
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
        `)
    mainJumpRight.addAnimationFrame(img`
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
        `)
    for (let index = 0; index < 30; index++) {
        mainJumpRight.addAnimationFrame(img`
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
            `)
    }
}
function animateCrouch () {
    mainCrouchLeft = animation.createAnimation(ActionKind.CrouchLeft, 100)
    animation.attachAnimation(hero, mainCrouchLeft)
    mainCrouchLeft.addAnimationFrame(img`
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
        `)
    mainCrouchRight = animation.createAnimation(ActionKind.CrouchRight, 100)
    animation.attachAnimation(hero, mainCrouchRight)
    mainCrouchRight.addAnimationFrame(img`
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
        `)
}
function clearGame () {
    for (let value of sprites.allOfKind(SpriteKind.Bumper)) {
        value.destroy()
    }
    for (let value2 of sprites.allOfKind(SpriteKind.Coin)) {
        value2.destroy()
    }
    for (let value3 of sprites.allOfKind(SpriteKind.Goal)) {
        value3.destroy()
    }
    for (let value4 of sprites.allOfKind(SpriteKind.Flier)) {
        value4.destroy()
    }
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`endpoint`, function (sprite4, location) {
    info.changeLifeBy(1)
    currentLevel += 1
    if (hasNextLevel()) {
        game.splash("Next level unlocked!")
        setLevelTileMap(currentLevel)
    } else {
        game.over(true, effects.confetti)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Coin, function (sprite2, otherSprite2) {
    otherSprite2.destroy(effects.trail, 250)
    otherSprite2.y += -3
    info.changeScoreBy(3)
    music.baDing.play()
})
function createEnemies () {
    // enemy that moves back and forth
    for (let value5 of tiles.getTilesByType(assets.tile`tile4`)) {
        bumper = sprites.create(img`
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
            `, SpriteKind.Bumper)
        tiles.placeOnTile(bumper, value5)
        tiles.setTileAt(value5, assets.tile`tile0`)
        bumper.ay = gravity
        if (Math.percentChance(50)) {
            bumper.vx = Math.randomRange(30, 60)
        } else {
            bumper.vx = Math.randomRange(-60, -30)
        }
    }
    // enemy that flies at player
    for (let value6 of tiles.getTilesByType(assets.tile`tile7`)) {
        flier = sprites.create(img`
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
            `, SpriteKind.Flier)
        tiles.placeOnTile(flier, value6)
        tiles.setTileAt(value6, assets.tile`tile0`)
        animation.attachAnimation(flier, flierFlying)
        animation.attachAnimation(flier, flierIdle)
    }
}
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    if (!(hero.isHittingTile(CollisionDirection.Bottom))) {
        hero.vy += 80
    }
})
function showInstruction (text: string) {
    game.showLongText(text, DialogLayout.Bottom)
    music.baDing.play()
    info.changeScoreBy(1)
}
function initializeHeroAnimations () {
    animateRun()
    animateIdle()
    animateCrouch()
    animateJumps()
}
function createPlayer (player2: Sprite) {
    player2.ay = gravity
    scene.cameraFollowSprite(player2)
    controller.moveSprite(player2, 100, 0)
    player2.z = 5
    info.setLife(3)
    info.setScore(0)
}
function initializeLevel (level2: number) {
    effects.clouds.startScreenEffect()
    playerStartLocation = tiles.getTilesByType(assets.tile`tile6`)[0]
    tiles.placeOnTile(hero, playerStartLocation)
    tiles.setTileAt(playerStartLocation, assets.tile`tile0`)
    createEnemies()
    spawnGoals()
}
function hasNextLevel () {
    return currentLevel != levelCount
}
function spawnGoals () {
    for (let value7 of tiles.getTilesByType(assets.tile`gem 1`)) {
        coin = sprites.create(img`
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
            `, SpriteKind.Coin)
        tiles.placeOnTile(coin, value7)
        animation.attachAnimation(coin, coinAnimation)
        animation.setAction(coin, ActionKind.Idle)
        tiles.setTileAt(value7, assets.tile`tile0`)
    }
}
let heroFacingLeft = false
let coin: Sprite = null
let playerStartLocation: tiles.Location = null
let flier: Sprite = null
let bumper: Sprite = null
let mainCrouchRight: animation.Animation = null
let mainCrouchLeft: animation.Animation = null
let mainJumpRight: animation.Animation = null
let mainJumpLeft: animation.Animation = null
let mainRunRight: animation.Animation = null
let mainRunLeft: animation.Animation = null
let flierIdle: animation.Animation = null
let flierFlying: animation.Animation = null
let mainIdleRight: animation.Animation = null
let mainIdleLeft: animation.Animation = null
let doubleJumpSpeed = 0
let canDoubleJump = false
let coinAnimation: animation.Animation = null
let currentLevel = 0
let levelCount = 0
let gravity = 0
let pixelsToMeters = 0
let invincibilityPeriod = 0
let hero: Sprite = null
class ActionKind {
    static RunningLeft = 0
    static RunningRight = 1
    static Idle = 2
    static IdleLeft = 3
    static IdleRight = 4
    static JumpingLeft = 5
    static JumpingRight = 6
    static CrouchLeft = 7
    static CrouchRight = 8
    static Flying = 9
    static Walking = 10
    static Jumping = 11
}
hero = sprites.create(assets.image`main_chara`, SpriteKind.Player)
// how long to pause between each contact with a
// single enemy
invincibilityPeriod = 600
pixelsToMeters = 30
gravity = 9.81 * pixelsToMeters
scene.setBackgroundImage(assets.image`back`)
initializeAnimations()
createPlayer(hero)
levelCount = 8
currentLevel = 0
setLevelTileMap(currentLevel)
giveIntroduction()
// set up hero animations
game.onUpdate(function () {
    if (hero.vx < 0) {
        heroFacingLeft = true
    } else if (hero.vx > 0) {
        heroFacingLeft = false
    }
    if (hero.isHittingTile(CollisionDirection.Top)) {
        hero.vy = 0
    }
    if (controller.down.isPressed()) {
        if (heroFacingLeft) {
            animation.setAction(hero, ActionKind.CrouchLeft)
        } else {
            animation.setAction(hero, ActionKind.CrouchRight)
        }
    } else if (hero.vy < 20 && !(hero.isHittingTile(CollisionDirection.Bottom))) {
        if (heroFacingLeft) {
            animation.setAction(hero, ActionKind.JumpingLeft)
        } else {
            animation.setAction(hero, ActionKind.JumpingRight)
        }
    } else if (hero.vx < 0) {
        animation.setAction(hero, ActionKind.RunningLeft)
    } else if (hero.vx > 0) {
        animation.setAction(hero, ActionKind.RunningRight)
    } else if (heroFacingLeft) {
        animation.setAction(hero, ActionKind.IdleLeft)
    } else {
        animation.setAction(hero, ActionKind.IdleRight)
    }
})
// Flier movement
game.onUpdate(function () {
    for (let value8 of sprites.allOfKind(SpriteKind.Flier)) {
        if (Math.abs(value8.x - hero.x) < 60) {
            if (value8.x - hero.x < -5) {
                value8.vx = 25
            } else if (value8.x - hero.x > 5) {
                value8.vx = -25
            }
            if (value8.y - hero.y < -5) {
                value8.vy = 25
            } else if (value8.y - hero.y > 5) {
                value8.vy = -25
            }
            animation.setAction(value8, ActionKind.Flying)
        } else {
            value8.vy = -20
            value8.vx = 0
            animation.setAction(value8, ActionKind.Idle)
        }
    }
})
// Reset double jump when standing on wall
game.onUpdate(function () {
    if (hero.isHittingTile(CollisionDirection.Bottom)) {
        canDoubleJump = true
    }
})
// bumper movement
game.onUpdate(function () {
    for (let value9 of sprites.allOfKind(SpriteKind.Bumper)) {
        if (value9.isHittingTile(CollisionDirection.Left)) {
            value9.vx = Math.randomRange(30, 60)
        } else if (value9.isHittingTile(CollisionDirection.Right)) {
            value9.vx = Math.randomRange(-60, -30)
        }
    }
})
