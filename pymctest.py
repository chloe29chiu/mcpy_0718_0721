from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    pos = mc.player.getTilePos()
    mc.postToChat(str(pos.x) + ' ' + str(pos.y) + ' ' + str(pos.z))