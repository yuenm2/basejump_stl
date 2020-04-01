import sys
import random
from trace_gen import *

if __name__ == "__main__":
  # common parameters
  id_p = int(sys.argv[1])
  num_cache_group_p = int(sys.argv[2])
  num_subcache_p = int(sys.argv[3])
  block_size_in_words_p = int(sys.argv[4])

  #random.seed(0)
  random.seed(id_p)

  tg = TraceGen(num_subcache_p, block_size_in_words_p)
  tg.clear_tags()

  #words = (2**18)/num_cache_p # 1MB
  words = (2**17)/num_cache_group_p # 1MB

  max_range = (2**14)# 64KB

  for i in range(words):
    taddr = random.randint(0, max_range-1) << 2
    write_not_read = random.randint(0,1)
    if write_not_read:
      tg.send_write(taddr)
    else:
      tg.send_read(taddr)

  tg.done()
