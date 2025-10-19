from tqdm import tqdm
from time import sleep
 
 
for i in tqdm(range(0, 100), initial = 50,
              desc ="Text You Want"):
    sleep(.1)