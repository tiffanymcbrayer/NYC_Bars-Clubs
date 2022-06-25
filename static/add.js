$(document).ready(function(){
    $("#name").focus()

    // left it like this because would not show on the screen when updated
    // $("#viewPlace").append("<div> previous page made </div>")
    // $("#viewPlace").append("<a href= /view/"+ current_id+"> View Page <a>")
    
    
    $("#typeButton").click(function(){
        $("#nameInvalid").empty()
        $("#walkInvalid").empty()
        $("#neighborhoodInvalid").empty()
        $("#addressInvalid").empty()
        $("#websiteInvalid").empty()
        $("#phoneInvalid").empty()
        $("#pictureInvalid").empty()
        $("#mondayInvalid").empty()
        $("#tuesdayInvalid").empty()
        $("#wednesdayInvalid").empty()
        $("#thursdayInvalid").empty()
        $("#fridayInvalid").empty()
        $("#saturdayInvalid").empty()
        $("#sundayInvalid").empty()
   
        let name = $.trim($("#name").val());
        let subwayStop = $.trim($("#subwayStop").val());
        let walk = $.trim($("#walk").val());
        let neighborhood = $.trim($("#neighborhood").val());
        let type = $.trim($("#type").val());
        let address = $.trim($("#address").val());
        let website = $.trim($("#website").val());
        let phone = $.trim($("#phone").val());
        let picture = $.trim($("#picture").val());
        let monday = $.trim($("#monday").val());
        let tuesday = $.trim($("#tuesday").val());
        let wednesday = $.trim($("#wednesday").val());
        let thursday = $.trim($("#thursday").val());
        let friday = $.trim($("#friday").val());
        let saturday = $.trim($("#saturday").val());
        let sunday = $.trim($("#sunday").val());
        
        console.log(subwayStop)

        if (name == ''){
            $("#nameInvalid").empty()
            $("#nameInvalid").append("<div> Please choose a name </div>")
            console.log("error name")
        } 
        else if (walk == '' || $.isNumeric(walk) == false){
            $("#walkInvalid").empty()
            $("#walkInvalid").append("<div> Please choose a distance </div>")
            console.log("error walk")
        } 
        else if (neighborhood == ''){
            $("#neighborhoodInvalid").empty()
            $("#neighborhoodInvalid").append("<div> Please choose a neighborhood </div>")
            console.log("error neighborhood")
        }
        else if (address == ''){
            $("#addressInvalid").empty()
            $("#addressInvalid").append("<div> Please choose an address </div>")
            console.log("error address")
        }
        else if (website == ''){
            $("#websiteInvalid").empty()
            $("#websiteInvalid").append("<div> Please choose a website url </div>")
            console.log("error website")
        }
        else if (phone == ''){
            $("#phoneInvalid").empty()
            $("#phoneInvalid").append("<div> Please choose a phone number </div>")
            console.log("error phone")
        }
        else if (picture == ''){
            $("#pictureInvalid").empty()
            $("#pictureInvalid").append("<div> Please choose a picture url </div>")
            console.log("error picture")
        }
        else if (monday == ''){
            $("#mondayInvalid").empty()
            $("#mondayInvalid").append("<div> Please enter time for Monday </div>")
            console.log("error monday")
        }
        else if (tuesday == ''){
            $("#tuesdayInvalid").empty()
            $("#tuesdayInvalid").append("<div> Please enter time for Tuesday </div>")
            console.log("error tuesday")
        }
        else if (wednesday == ''){
            $("#wednesdayInvalid").empty()
            $("#wednesdayInvalid").append("<div> Please enter time for Wednesday </div>")
            console.log("error wednesday")
        }
        else if (thursday == ''){
            $("#thursdayInvalid").empty()
            $("#thursdayInvalid").append("<div> Please enter time for Thursday </div>")
            console.log("error thursday")
        }
        else if (friday == ''){
            $("#fridayInvalid").empty()
            $("#fridayInvalid").append("<div> Please enter time for Friday </div>")
            console.log("error friday")
        }
        else if (saturday == ''){
            $("#saturdayInvalid").empty()
            $("#saturdayInvalid").append("<div> Please enter time for Saturday </div>")
            console.log("error saturday")
        }
        else if (sunday == ''){
            $("#sundayInvalid").empty()
            $("#sundayInvalid").append("<div> Please enter time for Sunday </div>")
            console.log("error sunday")
        }
        else {
            console.log("okay with no missing info")
            save_place()
        }

        


        // can put this in the save place later 
        // $("#name").val('')
    })
   
    
})



function save_place(){
       

    let name = $.trim($("#name").val());
    let subwayStop = $.trim($("#subwayStop").val());
    let walk = $.trim($("#walk").val());
    let neighborhood = $.trim($("#neighborhood").val());
    let type = $.trim($("#type").val());
    let address = $.trim($("#address").val());
    let website = $.trim($("#website").val());
    let phone = $.trim($("#phone").val());
    let picture = $.trim($("#picture").val());

    let monday = $.trim($("#monday").val());
    let tuesday = $.trim($("#tuesday").val());
    let wednesday = $.trim($("#wednesday").val());
    let thursday = $.trim($("#thursday").val());
    let friday = $.trim($("#friday").val());
    let saturday = $.trim($("#saturday").val());
    let sunday = $.trim($("#sunday").val());

    let hours = [
        "Monday: " + monday,
        "Tuesday: " + tuesday, 
        "Wednesday: " + wednesday,
        "Thursday: " + thursday,
        "Friday: " + friday,
        "Saturday: " + saturday,
        "Sunday: " + sunday 
    ]

    let data_to_save = {
        "name": name, 
        "hoursOperation": hours, 
        "wesbite": website,
        "picture": picture,
        "address": address,
        "closestSubway": subwayStop,
        "walk": walk + " mi",
        "neighborhood": neighborhood,
        "phone": phone,
        "type": type
    }

    $.ajax({
		type: "POST",
        url: "add_place",                
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            $("#name").focus()
            $("#name").val('')
            $("#walk").val('')
            $("#neighborhood").val('')
            $("#address").val('')
            $("#website").val('')
            $("#phone").val('')
            $("#picture").val('')
            $("#monday").val('')
            $("#tuesday").val('')
            $("#wednesday").val('')
            $("#thursday").val('')
            $("#friday").val('')
            $("#saturday").val('')
            $("#sunday").val('')
            console.log(result)
            id = result["current_id"]
            console.log(result["current_id"])

            $("#newItemSaved").append("<div> Your new place is saved! </div>")
            $("#viewPlace").append("<a href = /view/" +id + " </a> here </div>")

          

        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }

	});
}
