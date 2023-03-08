window.onload = function(){
    var lowRange = document.getElementById("low-range");
    var medRange = document.getElementById("med-range");
    var higRange = document.getElementById("high-range");  
    rent()
    lowRange.addEventListener("click", setPriceRange);
    medRange.addEventListener("click", setPriceRange);
    higRange.addEventListener("click", setPriceRange);
    
}

function setPriceRange(){   
    var medHeader = document.getElementById("med-range-div");
    var lowHeader = document.getElementById("low-range-div");
    var highHeader = document.getElementById("high-range-div");
    if(document.getElementById("low-range").checked){
        highHeader.classList.add("hide");
        medHeader.classList.add("hide");
        lowHeader.classList.remove("hide");
    }
    else if (document.getElementById("med-range").checked){
        highHeader.classList.add("hide");
        lowHeader.classList.add("hide");
        medHeader.classList.remove("hide");
    } 
    else if (document.getElementById("high-range").checked){
        medHeader.classList.add("hide");
        lowHeader.classList.add("hide");
        highHeader.classList.remove("hide");
    }
    else if (document.getElementById("high-range").checked && document.getElementById("low-range").checked){
        medHeader.classList.add("hide");
        lowHeader.classList.remove("hide");
        highHeader.classList.remove("hide");
    } 
    else if (document.getElementById("high-range").checked && document.getElementById("med-range").checked){
        medHeader.classList.remove("hide");
        lowHeader.classList.add("hide");
        highHeader.classList.remove("hide");
    } 
    else if (document.getElementById("med-range").checked && document.getElementById("low-range").checked){
        medHeader.classList.remove("hide");
        lowHeader.classList.remove("hide");
        highHeader.classList.add("hide");
    } 
    else {
        highHeader.classList.remove("hide");
        lowHeader.classList.remove("hide");
        medHeader.classList.remove("hide");
    }
}

function rent(){
    var content = document.getElementsByClassName("car-images");
    var rentCar = document.createElement("div");
    var rentButton = document.createElement("button")
    rentButton.addEventListener("click", function(){
        window.location.href = "/reserve-car"
    })
    rentButton.innerHTML = "Rent Vehicle"
    rentButton.id = "rent-button"
    rentCar.appendChild(rentButton);
    var i;
    for(i = 0; i < content.length; i++){
        content[i].addEventListener("click", function(){
            this.classList.toggle("active");
            var openContent = this.nextElementSibling;
            if(openContent.contains(rentCar)){
                openContent.removeChild(rentButton)
            } else {
                openContent.appendChild(rentButton)
            }
        });
    }
}
