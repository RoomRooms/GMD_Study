from struct import unpack

class unit_read():

    def __init__(self):
        self.pnt = 0x00

    def get_byte1(self, buf):
        tmp = buf[self.pnt]
        self.pnt += 0x01
        return tmp

    def get_byte2_be(self, buf):
        tmp = buf[self.pnt:self.pnt+0x02]
        self.pnt += 0x02
        return unpack('>H', tmp)[0]

    def get_byte2_le(self, buf):
        tmp = buf[self.pnt:self.pnt+0x02]
        self.pnt += 0x02
        return unpack('<H', tmp)[0]

    def get_byte4_be(self, buf):
        tmp = buf[self.pnt:self.pnt + 0x04]
        self.pnt += 0x04
        return unpack('>H', tmp)[0]

    def get_byte4_le(self, buf):
        tmp = buf[self.pnt:self.pnt + 0x04]
        self.pnt += 0x04
        return unpack('<H', tmp)[0]

    def move_pnt(self, ):

class Boot_Record():

    def __init__(self, buf):
        ur = unit_read()

        ur.pnt += 0x0B
        self.bps = ur.get_byte2_le(buf)
        self.spc = ur.get_byte2_le(buf)
        self.rsvd_s = ur.get_byte2_le(buf)
        self.cnt_FAT = ur.get_byte2_le(buf)

        ur.pnt += 0x13
        self.cnt_s_FAT = ur.get_byte2_le(buf)

        ur.pnt += 0x04
        self.root_dir_c = ur.get_byte2_le(buf)

    def analysis(self):
        print(self.bps)


if __name__ == '__main__':
    f = open('./Image/fat32.mdf', 'rb')
    f.seek(0x00)

    buf = bytearray(f.read(0x200))
    br = Boot_Record(buf)
    br.analysis()

    f.close()