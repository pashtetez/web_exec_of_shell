import socket
import aiofiles
import asyncio
from aiohttp import web
import subprocess


async def status(request):
    try:
        subprocess.check_output(['bash','/root/aiohttp/status.sh']).split(b'\n')
        res = True
    except:
        res = False
    return web.json_response({"status" : res})

async def do_action(request):
    subprocess.check_output(['bash','/root/aiohttp/action.sh'])
    return web.Response(text="OK")

async def run_cmd(request):
    data = await request.text()
    print(data)
    subprocess.check_output(['bash','/root/aiohttp/run_cmd.sh',data])
    return web.Response(text="OK")

if __name__ == '__main__':
    app = web.Application()
    app.add_routes([web.get('/status', status),
                    web.post('/do_action', do_action),
                    web.post('/run_cmd', run_cmd),
                    web.get('/', lambda x:web.FileResponse('static/index.html')),
                    web.static('/', 'static')])
    web.run_app(app)
