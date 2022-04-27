function createWebSocket(){
    let socket = new WebSocket(WEBSOCKET_URL);

    socket.onopen = function(e) {
        console.log(`connection established!`);
    };

    socket.onmessage = function(event) {
        console.log(`[message] Data received from server: ${event.data}`);
    };

     window.addEventListener("beforeunload", function(e){
        //call disconect socket function and delete de connectionId in the connections.config file
        console.log("HELLO")
     }, false);

    return socket;
}

function sendMessage(id, price){
    let message = 
    '{'+
        '"action": "sendMessage",'+
        '"message": {'+
            '"id":id,'+
            '"majorBidder":name,'+
            '"price":price'+
        '}'+
    '}';

    socket.send(message);
}