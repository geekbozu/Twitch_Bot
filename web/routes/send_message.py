import socket
from os import getenv

from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()


@router.post("/post_message")
def twitch_webhook_follow_post(body: dict):

    if body.get("message", False):
        try:
            s = socket.socket()
            s.connect(("bot", 13337))

            # We don't actually need this, but we have to read it before the bot will accept commands
            s.recv(300).decode("utf8")

            # Send the channel that we are connecting to
            s.send(f"{getenv('TWITCH_CHANNEL')}\n".encode("utf8"))
            s.send(f"🤖 {body['message']}\n".encode("utf8"))

            # Close the socket
            s.shutdown(socket.SHUT_RD)
            return JSONResponse({"success": True})

        except ConnectionRefusedError:
            print("Unable to connect to bot.")
            return JSONResponse({"success": False, "response": "Unable to connect to bot."})
