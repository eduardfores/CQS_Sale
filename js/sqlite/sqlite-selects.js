
function loadProducts(number){

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

function selectProductCheckingPice(id, product){

    var command = "SELECT * FROM Products WHERE id = "+id;

    worker.onmessage = function (event) {
        var results = event.data.results[0].values;

        var bidUp = document.getElementById("bidUp"+id).value;

        if(bidUp > results[0][2]){
            product.value = results[0];
            product.onchange();
        } else {
            alert("The price has to be higher than "+ results[0][2])
        }

        if (!results) {
			error({message: event.data.error});
			return;
		}
    }

    worker.postMessage({ action: 'exec', sql: command });
}

function selectProductbyId(id){

    var command = "SELECT * FROM Products WHERE id = "+id;

    worker.onmessage = function (event) {
        var results = event.data.results[0].values[0];

        //update HTML with new price
        updatePriceOfProduct(id, results[2]);

        if (!results) {
			error({message: event.data.error});
			return;
		}
    }

    worker.postMessage({ action: 'exec', sql: command });
}