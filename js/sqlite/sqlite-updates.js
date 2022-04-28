function updatePrice(id, price, majorBidder = name){

    var command = "UPDATE Products SET price = "+price+", majorBidder = '"+majorBidder+"' WHERE id = "+id+";";

    worker.onmessage = function (event) {
        var results = event.data.results;

        selectProductbyId(id);
        if (!results) {
			error({message: event.data.error});
			return;
		}
    }

    worker.postMessage({ action: 'exec', sql: command });
}