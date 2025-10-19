from tqdm import tqdm
from time import sleep
 
 
for i in tqdm(range(0, 100), disable = True,
               desc ="Text You Want"):
    sleep(.1)
 
print("Iteration Successful")