
function loadProducts(worker, number){

    var commands = "SELECT * FROM Products LIMIT " + number +";";

    worker.onmessage = function (event) {
        var results = event.data.results[0].values;

        var html = "";
        for(let i = 0; results.length > i; i++){
            html += createCard(results[i]);
        }

        addCards(html);

        if (!results) {
			error({message: event.data.error});
			return;
		}
    }

    worker.postMessage({ action: 'exec', sql: commands });

}