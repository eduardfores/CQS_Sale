function updatePrice(id, price, majorBidder = name){

    var command = "UPDATE Products SET price = "+price+", majorBidder = '"+majorBidder+"' WHERE id = "+id+";";

    worker.onmessage = function (event) {
        selectProductbyId(id);
        if (event.data.error) {
			error({message: event.data.error});
			return;
		}
    }

    worker.postMessage({ action: 'exec', sql: command });
}