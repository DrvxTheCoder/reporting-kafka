var socket = new WebSocket("ws://localhost:8000/ws/jcdecaux/")

socket.onmessage = function (e) {
    console.log(e)
}