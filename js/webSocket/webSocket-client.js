function createWebSocket(){
    let socket = new WebSocket(WEBSOCKET_URL);

    socket.onopen = function(e) {
        console.log(`connection established!`);
    };

    socket.onmessage = function(event) {
        let json = JSON.parse(event.data);
        updatePrice(json.message.id, json.message.price, json.message.majorBidder);
    };

     window.addEventListener("beforeunload", function(e){
        //call disconect socket function and delete de connectionId in the connections.config file
        socket.disconnect();
        console.log("Conneciton closed!");
     }, false);

    return socket;
}

function sendMessage(id, price){
    let message = 
    '{'+
        '"action": "sendMessage",'+
        '"message": {'+
            '"id":' + id + ','+
            '"majorBidder":"' + name + '",'+
            '"price":' + price+
        '}'+
    '}';

    socket.send(message);
}