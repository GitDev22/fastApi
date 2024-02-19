from fastapi import FastAPI

app = FastAPI()

@app.get(&quot;/&quot;)
async def read_root():
    return {&quot;message&quot;: &quot;Hello, FastAPI from Docker!&quot;}