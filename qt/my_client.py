from aiocoap import *
import asyncio
run=asyncio.get_event_loop().run_until_complete
protocol=run(Context.create_client_context())
msg = Message(code=GET, uri="coap://192.168.141.143/receive")
response = run(protocol.request(msg).response)
print(response.payload.decode('utf-8'))
