import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

while True:
	pos = mc.player.getPos()
	x = pos.x
	y = pos.y
	z = pos.z

	block = 38

	mc.setBlock(x, y, z, block)
	time.sleep(0.2)
