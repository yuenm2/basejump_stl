import sys
import random
from test_base import *


class TestRandomAFLINV(TestBase):

  def generate(self):
    # scrub tag and data
    self.clear_tag()
    for i in range(self.MAX_ADDR/4):
      self.send(SW, 4*i)

    # random SW/LW
    for iteration in range(500):

      # accessing only 10 blocks for each set.
      # 40 blocks in total; 320 word addresses
      for n in range(1000):
        tag = random.randint(0,9)
        index = random.randint(0,3)
        block_offset = random.randint(0,7)
        taddr = self.get_addr(tag, index, block_offset)
        store_not_load = random.randint(0,1)
        if store_not_load:
          self.send(SW, taddr)
        else:
          self.send(LW, taddr)

      # flush/invalidate random blocks
      for n in range(10):
        way = random.randint(0,7)
        index = random.randint(0,3)
        self.flush_inv(way, index)

      # AFLINV
      for n in range(10):
        tag = random.randint(0,9)
        index = random.randint(0,3)
        taddr = self.get_addr(tag, index)
        self.send(AFLINV, taddr)

    self.tg.done()
          
#   main()
if __name__ == "__main__":
  t = TestRandomAFLINV()
  t.generate()