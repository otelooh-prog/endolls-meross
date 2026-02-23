from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager
import asyncio

EMAIL = "jose.alconchel@gmx.com"
PASSWORD = "pa1pe2pi3"
DEVICE_NAME = "Marantz M-CR610"

async def prova_endoll():
    http_client = await MerossHttpClient.async_from_user_password(
        email=EMAIL,
        password=PASSWORD,
        api_base_url="https://iotx.meross.com"
    )

    manager = MerossManager(http_client=http_client)
    await manager.async_init()

    devices = manager.find_devices()

    target = None
    for d in devices:
        if d.name == DEVICE_NAME:
            target = d
            break

    if target is None:
        return "Dispositiu no trobat"

    await target.async_update()

    await target.async_turn_off()
    await asyncio.sleep(10)
    await target.async_turn_on()

    await manager.async_close()
    await http_client.async_logout()

    return "OK"

print(asyncio.run(prova_endoll()))
