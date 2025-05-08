import asyncio
from bleak import BleakScanner

async def run():
    devices = await BleakScanner.discover()
    for d in devices:
        # 输出地址和特征zheng
        print(d.address, d.name)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())