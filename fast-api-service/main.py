
from fastapi import FastAPI
import aioredis

app = FastAPI()


@app.get('/metrics')
async def metrics():
    redis = aioredis.from_url("redis://localhost")
   
    id = await redis.get('id')
    temp = await redis.get('temp')
    hum = await redis.get('humidity')
 
    
    return {
                'ID': int(id),
                'Temp': int(temp),
                'Humidity': int(hum),
            }

