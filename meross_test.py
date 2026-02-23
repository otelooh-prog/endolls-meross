from meross_iot.http_api import MerossHttpClient
from meross_iot.manager import MerossManager
import asyncio

EMAIL = "jose.alconchel@gmx.com"
PASSWORD = "pa1pe2pi3"
DEVICE_NAME = "Marantz M-CR610"   # Canvia-ho si cal

async def prova_endoll():
    # Connexió al Cloud de Meross
    http_client = await MerossHttpClient.async_from_user_password(
        email=EMAIL,
        password=PASSWORD,
        api_base_url="https://iotx.meross.com"
    )

    manager = MerossManager(http_client=http_client)
    await manager.async_init()

    # Obtenir tots els dispositius del compte
    devices = manager.find_devices()

    # MOSTRAR ELS NOMS REALS QUE VEU LA API
    for d in devices:
        print("TROBAT:", d.name)

    # Buscar el dispositiu pel nom
    target = None
    for d in devices:
        if d.name == DEVICE_NAME:
            target = d
            break

    if target is None:
        print("Dispositiu no trobat")
        return

    # Encendre i apagar per provar
    await target.async_turn_off()
    print("OFF")
    await asyncio.sleep(10)
    await target.async_turn_on()
    print("ON")

    # Tancar connexió
    await manager.async_close()
    await http_client.async_logout()

# Executar la funció
asyncio.run(prova_endoll())
