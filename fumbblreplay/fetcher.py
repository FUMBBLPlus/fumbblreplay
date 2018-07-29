import asyncio
import copy
import json
import pathlib

try:
  from . import lzstring
except ImportError:
  import lzstring

import websockets

LZString = lzstring.LZString()

SCHEME = "ws"
NETLOC = "fumbbl.com:22223"
PATH = "/command"

JSON_SEPARATORS = ",", ":"  # more compressed without spaces

try:
  mydirpath = pathlib.Path(__file__).parent
except NameError:
  mydirpath = pathlib.Path(".")


# The objects below are mutable!
# Never change them without copying first!
with (mydirpath / "clientReplay.json").open() as f:
  clientReplay = json.load(f)
with (mydirpath / "clientCloseSession.json").open() as f:
  clientCloseSession = json.load(f)


def obj2msg(obj):
  _json = json.dumps(obj, separators=JSON_SEPARATORS)
  _msg =  LZString.compressToUTF16(_json)
  return _msg


def msg2obj(msg):
  _json = LZString.decompressFromUTF16(msg)
  _obj = json.loads(_json)
  return _obj


async def async_get_replay_data(replay_id):
  clientReplay_ = copy.deepcopy(clientReplay)
  clientReplay_["gameId"] = int(replay_id)
  url = f'{SCHEME}://{NETLOC}{PATH}'
  async with websockets.connect(url) as websocket:
    msg = obj2msg(clientReplay_)
    await websocket.send(msg)
    responses = []
    prev_obj = ...
    while True:
      msg = await websocket.recv()
      obj = msg2obj(msg)
      # At end, server repeats the same data endlessly.
      if obj != prev_obj:
        responses.append(obj)
        prev_obj = obj
      else:
        break
    msg = obj2msg(clientCloseSession)
    await websocket.send(msg)
  return responses


def get_replay_data(replay_id):
  return asyncio.get_event_loop().run_until_complete(
      async_get_replay_data(replay_id)
  )
