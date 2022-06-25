$(document).ready(function(){

    display_search(favList)


})

function display_search(favList){
    $("#favList").empty()
    $.each(favList, function( index, value ) {
        $("#favList").append(
            "<div> <a href= '/view/"+ value["id"] +"'> " + value["name"] + "</a> </div>"
        )
    });
    
}