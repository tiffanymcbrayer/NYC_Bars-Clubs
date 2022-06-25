function searchItem(search_text){
    
    if($.trim(search_text) == ""){
        $("#search_input").val("")
    } else{
        window.location.href = "/search_results/"+search_text;
    }
    
}

$(document).ready(function(){
    $("#search_input").empty()
    $("#search_input").keyup(function(e){
        if (e.which == 13){
            let search_text = $("#search_input").val()
            searchItem(search_text)
        }
    })

    $("#search_button").click(function(){
        let search_text = $("#search_input").val()
        searchItem(search_text)
    })

    
})