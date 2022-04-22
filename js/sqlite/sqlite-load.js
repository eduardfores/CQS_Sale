/**
 * This function is called to load the SQLite today 
 * 
 * @param {worker} worker 
 * @param {promise} sqlFile 
 */
function loadSQLite(worker, sqlFile){
    var r = new FileReader();
	r.onload = function () {
		worker.onmessage = function () {
			loadProducts(worker,10);
		};
        
		try {
			worker.postMessage({ action: 'open', buffer: r.result }, [r.result]);
		}
		catch (exception) {
			worker.postMessage({ action: 'open', buffer: r.result });
		}
	}

	sqlFile.then( function (data) {
        var blob = new Blob([data.Body], {type: 'binary/octet-stream'});
        r.readAsArrayBuffer(blob);
    })
}