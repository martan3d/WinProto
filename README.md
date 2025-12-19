# WinProto
WinProto is the latest incarnation of the Python Programmer for the ProtoThrottle Receiver

This program REQUIRES a USB Xbee 'dongle' device to talk to the Protothrottle and your android device must support OTG on the USB port. The dongle MUST use the Silicon Labs CP210x chipset. The dongle H/W can be found on Amazon, search for 'WaveShare Xbee'.

The Xbee chip for this can be ordered from Sparkfun.com.

You will also need the XCTU program from the Xbee manufacturer, Digi, it's free. If you want to play with around with Xbees, this program is essential.

As far as configuration, the Xbee must have the 802.15.4 TH firmware installed, many are shipped with the Digimesh firmware, that won't work. XCTU will let you install the latest if needed using the 'update' button at the top. Once the firmware is verified, you have to change a few configuration items in the chip. Set the ID Network PAN ID to 225. Find the API Enable and set it to API Mode without Escapes (1). Just below that, find the baud rate and set it to 38400. From there scroll down in XCTU and find the port assignments. Don't change the UART DI and DO pin configurations, you need those at defaults, but for all the other I/O pin configurations, set them to disable.

- https://www.sparkfun.com/xbee-3-module-pcb-antenna.html
- https://www.amazon.com/dp/B07DMGF28S?ref=ppx_yo2ov_dt_b_fed_asin_title
- https://www.amazon.com/dp/B0744BKDRD?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1
- https://hub.digi.com/support/products/xctu/?path=/support/asset/xctu-v-659-windows-x86x64/
