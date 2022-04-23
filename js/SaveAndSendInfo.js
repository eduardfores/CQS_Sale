function checkPrice(element){
    var product = document.getElementById("product");
    selectProductCheckingPice(element, product);
}

function saveAndSendBidUp(val) {
    let product=val.split(',');

    let newPrice = document.getElementById("bidUp"+product[0]).ariaValueMax;

    updatePrice(product[0], newPrice)
}