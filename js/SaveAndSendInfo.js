function checkPrice(element){
    var product = document.getElementById("product");
    selectProductCheckingPice(element, product);
}

function saveAndSendBidUp(val) {
    let product=val.split(',');

    let newPrice = document.getElementById("bidUp"+product[0]).value;
    
    updatePrice(product[0], newPrice);

    let sql = "UPDATE Products SET price = ? , majorBidder = ? WHERE id = ?;"
    let tuple = [newPrice, '"'+name+'"', product[0]]

    sendMessage(sql, tuple);
}