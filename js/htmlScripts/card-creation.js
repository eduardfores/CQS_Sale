function createCard(element){

    var html = '<div class="col-xl-3 col-md-6 mb-4">'+
                    '<div class="card border-left-primary shadow h-100 py-2">'+
                        '<div class="card-body">'+
                            '<div class="row no-gutters align-items-center">'+
                                '<div class="col mr-2">'+
                                    '<div class="text-xs font-weight-bold text-primary text-uppercase mb-1">';
                        
    html += element[1]  
    
    html += '</div><div class="h5 mb-0 font-weight-bold text-gray-800">$';
    
    html+=element[2]
    
    html += '</div></div><div class="col-auto"><img src="'
    
    html += element[3]
    
    html +='" class="rounded mx-auto d-block" width="264" height="156"></i></div>'+
                '<div class="input-group mt-3">'+
                    '<input type="number" class="form-control" placeholder="Bid value" aria-label="Recipients username" aria-describedby="basic-addon2">'+
                    '<div class="input-group-append">'+
                      '<button class="btn btn-outline-secondary" type="button">Bid Up</button>'+
                    '</div>'+
                '</div>'+
            '</div>'+
        '</div>'+
    '</div></div>';

    return html;
}

function addCards(html){
    console.log(html)
    document.getElementById("cards").innerHTML += html;
}