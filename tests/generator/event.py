import xcffib
import struct
import six
MAJOR_VERSION = 1
MINOR_VERSION = 4
key = xcffib.ExtensionKey("EVENT")
_events = {}
_errors = {}
class ScreenChangeNotifyEvent(xcffib.Event):
    def __init__(self, unpacker):
        xcffib.Event.__init__(self, unpacker)
        base = unpacker.offset
        self.rotation, self.timestamp, self.config_timestamp, self.root, self.request_window, self.sizeID, self.subpixel_order, self.width, self.height, self.mwidth, self.mheight = unpacker.unpack("xB2xIIIIHHHHHH")
        self.bufsize = unpacker.offset - base
    def pack(self):
        buf = six.BytesIO()
        buf.write(struct.pack("=B", 0))
        buf.write(struct.pack("=B2xIIIIHHHHHH", self.rotation, self.timestamp, self.config_timestamp, self.root, self.request_window, self.sizeID, self.subpixel_order, self.width, self.height, self.mwidth, self.mheight))
        buf_len = len(buf.getvalue())
        if buf_len < 32:
            buf.write(struct.pack("x" * (32 - buf_len)))
        return buf.getvalue()
_events[0] = ScreenChangeNotifyEvent
xcffib._add_ext(key, eventExtension, _events, _errors)
