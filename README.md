# Sunvell_R69-IR-Remote

This python script provides support for the Sunvell-R69 IR-remote w/o using lirx.

*** THIS IS WORK IN PROGRESS ***

# Installation

Set IR protocol to "nec":
```
$ sudo su
# echo nec > /sys/class/rc/rc0/protocols
# exit
```

Download script:
```
$ cd
$ git clone https://github.com/karabek/Sunvell_R69-IR-Remote
```

Find device:
```
$ ls -l /dev/input/by-path | grep ir-event
```
the last digit (e.g. "0") should be used as parameter for the "sunvell_r69-cir.py"-script

Test:
```
$ cd Sunvell_R69-IR-Remote
$ sudo sunvell_r69-cir.py
```

Hit any key on the remote to test.

# Key Codes (Sunvell R69 IR-remote)

	320 : "KEY_POWER"
	341 : "TV-Power"
	345 : "TV-Set"
	344 : "TV-TVin"
	343 : "TV-VolDown"
	342 : "TV-VolUp"
	323 : "KEY_SETUP"
	271 : "KEY_APPSELECT"
	272 : "KEY_VOLUMEDOWN"
	281 : "KEY_VOLUMEUP"
	273 : "KEY_HOME"
	280 : "KEY_BACK"
	332 : "KEY_MENU"
	256 : "BTN_MOUSE"
	278 : "KEY_UP"
	337 : "KEY_LEFT"
	336 : "KEY_RIGHT"
	282 : "KEY_DOWN"
	275 : "KEY_OK"
	334 : "KEY_1"
	269 : "KEY_2"
	268 : "KEY_3"
	330 : "KEY_4"
	265 : "KEY_5"
	264 : "KEY_6"
	326 : "KEY_7"
	261 : "KEY_8"
	260 : "KEY_9"
	257 : "KEY_0"
	321 : "KEY_MUTE"
	322 : "KEY_BACKSPACE"

# License

The MIT License (MIT)

Copyright (c) 2015 Richard Hull

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

