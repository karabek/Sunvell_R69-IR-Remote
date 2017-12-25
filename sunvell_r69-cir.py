#!/usr/bin/python
import struct
import time
import sys

cmds = {320 : "KEY_POWER",
		341 : "TV-Power",
		345 : "TV-Set",
		344 : "TV-TVin",
		343 : "TV-VolDown",
		342 : "TV-VolUp",
		323 : "KEY_SETUP",
		271 : "KEY_APPSELECT",
		272 : "KEY_VOLUMEDOWN",
		280 : "KEY_VOLUMEUP",
		273 : "KEY_HOME",
		280 : "KEY_BACK",
		332 : "KEY_MENU",
		256 : "BTN_MOUSE",
		278 : "KEY_UP",
		337 : "KEY_LEFT",
		336 : "KEY_RIGHT",
		282 : "KEY_DOWN",
		275 : "KEY_OK",
		334 : "KEY_1",
		269 : "KEY_2",
		268 : "KEY_3",
		330 : "KEY_4",
		265 : "KEY_5",
		264 : "KEY_6",
		326 : "KEY_7",
		261 : "KEY_8",
		260 : "KEY_9",
		257 : "KEY_0",
		321 : "KEY_MUTE",
		322 : "KEY_BACKSPACE"
}


infile_path = "/dev/input/event0"
# long int, long int, unsigned short, unsigned short, unsigned int
FORMAT = 'llHHI'
EVENT_SIZE = struct.calcsize(FORMAT)
#  binary mode
in_file = open(infile_path, "rb")
event = in_file.read(EVENT_SIZE)
while event:
	(tv_sec, tv_usec, type, code, value) = struct.unpack(FORMAT, event)
	if type != 0 or code != 0 or value != 0:
		print cmds.get(value, "KEY_unknown")
	event = in_file.read(EVENT_SIZE)
in_file.close()
