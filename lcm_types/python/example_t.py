"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class example_t(object):
    __slots__ = ["counter"]

    __typenames__ = ["int64_t"]

    __dimensions__ = [None]

    def __init__(self):
        self.counter = 0

    def encode(self):
        buf = BytesIO()
        buf.write(example_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">q", self.counter))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != example_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return example_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = example_t()
        self.counter = struct.unpack(">q", buf.read(8))[0]
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if example_t in parents: return 0
        tmphash = (0x304d5fa4873b382c) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if example_t._packed_fingerprint is None:
            example_t._packed_fingerprint = struct.pack(">Q", example_t._get_hash_recursive([]))
        return example_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

