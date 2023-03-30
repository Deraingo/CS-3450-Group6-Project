window.addEventListener('DOMContentLoaded', function(){
    var selectedCar = null;
    var csrftoken = getCookie('csrftoken');
    var lowRange = document.getElementById("low-range");
    var medRange = document.getElementById("med-range");
    var higRange = document.getElementById("high-range");  
    // rent()
    lowRange.addEventListener("click", setPriceRange);
    medRange.addEventListener("click", setPriceRange);
    higRange.addEventListener("click", setPriceRange);

    var content = document.getElementsByClassName("car-images");
    var i;
    for (i = 0; i < content.length; i++) {
        content[i].addEventListener("click", function () {
            // console.log(carMake, carModel, carYear, carPrice);
            var carMake = this.dataset.make;
            var carModel = this.dataset.model;
            var carYear = this.dataset.year;
            var carPrice = this.dataset.price;
            console.log(carMake, carModel, carPrice, carYear);

            if(this === selectedCar){
                selectedCar.classList.toggle("active")
                var openContent = this.nextElementSibling;
                openContent.removeChild(openContent.lastChild);
                selectedCar = null
            } else if (selectedCar === null){
                selectedCar = this
                selectedCar.classList.toggle("active");
                rent(carMake, carModel, carYear, carPrice, this); // Add this line to call the rent function
            } else {
                selectedCar.classList.toggle("active");
                selectedCar = this;
                selectedCar.classList.toggle("actice");
                var oldOpenContent = selectedCar.nextElementSibling;
            }
        });
    }

    function rent(carMake, carModel, carYear, carPrice, carElement) {
        var openContent = carElement.nextElementSibling;
        var submitRental = document.createElement("form");
        submitRental.action = "/reserve-car/";
        submitRental.method = "POST";
      
        var csrfInput = document.createElement("input");
        csrfInput.type = "hidden";
        csrfInput.name = "csrfmiddlewaretoken";
        csrfInput.value = csrftoken;
      
        var makeInput = document.createElement("input");
        makeInput.type = "hidden";
        makeInput.name = "make";
        makeInput.value = carMake;
      
        var modelInput = document.createElement("input");
        modelInput.type = "hidden";
        modelInput.name = "model";
        modelInput.value = carModel;
      
        var yearInput = document.createElement("input");
        yearInput.type = "hidden";
        yearInput.name = "year";
        yearInput.value = carYear;
      
        var priceInput = document.createElement("input");
        priceInput.type = "hidden";
        priceInput.name = "cost";
        priceInput.value = carPrice;
      
        var rentButton = document.createElement("button");
        rentButton.type = "submit";
        rentButton.innerHTML = "Rent Vehicle";
        rentButton.id = "rent-button";
      
        submitRental.appendChild(csrfInput);
        submitRental.appendChild(makeInput);
        submitRental.appendChild(modelInput);
        submitRental.appendChild(yearInput);
        submitRental.appendChild(priceInput);
        submitRental.appendChild(rentButton);
        openContent.appendChild(submitRental);
    }

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
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
    
});
