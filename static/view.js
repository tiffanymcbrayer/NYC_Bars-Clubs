

$(document).ready(function(){

    var elem = document.getElementById('typeButton');
    var type = elem.innerText;
    
    $("#typeButton").click(function(){
        window.location.href = "/search_results/"+type;
    })

    var elem = document.getElementById('neighborhoodButton');
    var neigh = elem.innerText;
    
    $("#neighborhoodButton").click(function(){
        window.location.href = "/search_results/"+neigh;
    })

    var elem = document.getElementById('subwayButton');
    var subway = elem.innerText;
    
    $("#subwayButton").click(function(){
        window.location.href = "/search_results/"+subway;
    })
   
    
})