function createWebSocket(websocket){
    let socket = new WebSocket(websocket);

    socket.onopen = function(e) {
        console.log(`connection established!`);
    };

    socket.onmessage = function(event) {
        let json = JSON.parse(event.data);
        console.log(json);
        if(json.action){
            updatePrice(json.message.data[2], json.message.data[0], json.message.data[1]);
        }
    };

     window.addEventListener("beforeunload", function(e){
        //call disconect socket function and delete de connectionId in the connections.config file
        socket.disconnect();
        console.log("Conneciton closed!");
     }, false);

    return socket;
}

function sendMessage(sql, tuple){
    let message = 
    '{'+
        '"action": "sendMessage",'+
        '"message": {'+
            '"sql":"' + sql + '",'+
            '"data": [' + tuple +']'+ 
        '}'+
    '}';

    socket.send(message);
}