import asyncio
import time
from flask import Flask


app = Flask(__name__)


async def sleep(secs):
    await asyncio.sleep(secs)
    return 123

@app.route('/sync', methods=['GET'])
def sync_handler():
    before = time.perf_counter()
    time.sleep(1)
    time.sleep(1)
    after = time.perf_counter()
    return f"Elapsed time: {after - before}"


@app.route('/async', methods=['GET'])
async def async_handler():
    before = time.perf_counter()
    await asyncio.gather(sleep(1), sleep(1))
    after = time.perf_counter()
    return f"Elapsed time: {after - before}"


if __name__ == '__main__':
    app.run(port=5002, debug=True)

