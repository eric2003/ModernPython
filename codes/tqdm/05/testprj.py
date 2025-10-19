from tqdm import tqdm
from time import sleep
 
 
for i in tqdm(range(0, 100), mininterval = 3,
              desc ="Text You Want"):
    sleep(.1)