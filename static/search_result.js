$(document).ready(function(){

   
    if (searchItem == " "){
        $("#all_search_results").empty()
        $("#search").focus()
    }

    if (data.length == 0){
        $("#all_search_results").append("No results found")
    } else {
        $.each(data, function(i, item){
            console.log(item)

            let this_result = $("<div class = 'search_result'>")
            console.log(this_result)
            $(this_result).text(item["name"])
            $(this_result).click(function(e){
                let item_id = item["id"]
                window.location.href = "/view/"+item_id
            })

            $("#all_search_results").append(this_result)
        })
    }
})
