window.onload = function(){
    var csrftoken = getCookie('csrftoken');
    var lowRange = document.getElementById("low-range");
    var medRange = document.getElementById("med-range");
    var higRange = document.getElementById("high-range");  
    rent()
    lowRange.addEventListener("click", setPriceRange);
    medRange.addEventListener("click", setPriceRange);
    higRange.addEventListener("click", setPriceRange);

  function rent(carMake, carModel, carYear, carPrice) {
  var form = document.createElement("form");
  form.action = "/reserve-car/";
  form.method = "POST";

  var csrfInput = document.createElement("input");
  csrfInput.type = "hidden";
  csrfInput.name = "csrfmiddlewaretoken";
  csrfInput.value = csrftoken;

  var carMakeInput = document.createElement("input");
  carMakeInput.type = "hidden";
  carMakeInput.name = "car_make";
  carMakeInput.value = carMake;

  var carModelInput = document.createElement("input");
  carModelInput.type = "hidden";
  carModelInput.name = "car_model";
  carModelInput.value = carModel;

  var carYearInput = document.createElement("input");
  carYearInput.type = "hidden";
  carYearInput.name = "car_year";
  carYearInput.value = carYear;

  var carPriceInput = document.createElement("input");
  carPriceInput.type = "hidden";
  carPriceInput.name = "car_price";
  carPriceInput.value = carPrice;

  form.appendChild(csrfInput);
  form.appendChild(carMakeInput);
  form.appendChild(carModelInput);
  form.appendChild(carYearInput);
  form.appendChild(carPriceInput);

  var rentButton = document.createElement("button");
  rentButton.type = "submit";
  rentButton.innerHTML = "Rent Vehicle";
  rentButton.id = "rent-button";

  form.appendChild(rentButton);

  var content = document.getElementsByClassName("car-images");
  var i;
  for (i = 0; i < content.length; i++) {
    content[i].addEventListener("click", function() {
      var openContent = this.nextElementSibling;

      // Remove any existing rent buttons
      var existingRentButton = openContent.querySelector('#rent-button');
      if (existingRentButton) {
        openContent.removeChild(existingRentButton);
      }

      // Add rent button to the active car's description section
      if (this.classList.contains("active")) {
        this.classList.remove("active");
      } else {
        this.classList.add("active");
        var carMake = this.dataset.make;
        var carModel = this.dataset.model;
        var carYear = this.dataset.year;
        var carPrice = this.dataset.price;
        carMakeInput.value = carMake;
        carModelInput.value = carModel;
        carYearInput.value = carYear;
        carPriceInput.value = carPrice;
        form.action = "/reserve-car/?car_make=" + carMake + "&car_model=" + carModel + "&car_year=" + carYear + "&car_price=" + carPrice;
        openContent.appendChild(form);
      }
    });
  }
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
    
}