import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()
time.sleep(60)

points = 0
hits = mc.events.pollBlockHits()

for hit in hits:
	x = hit.pos.x
	y = hit.pos.y
	z = hit.pos.z

	points = points + mc.getBlock(x, y, z)
	mc.postToChat("You got " + str(points) + " points.")
