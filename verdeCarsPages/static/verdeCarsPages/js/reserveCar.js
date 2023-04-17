
window.addEventListener('DOMContentLoaded', function(){
    let carDetails = document.getElementById('car-id');
    let carMake = carDetails.dataset.carMake;
    let carModel = carDetails.dataset.carModel;
    let carYear = carDetails.dataset.carYear;
    let carCost = carDetails.dataset.carCost;
    let homeButton = document.getElementById('homeButton');
    let catalogButton = document.getElementById('catalogButton');
    homeButton.type="submit";
    catalogButton.type="submit";
    let submitButton = document.getElementById("submit");
    let agreeCheckbox = document.getElementById("agree");
    let csrftoken = getCookie('csrftoken');
    console.log(carMake);
    console.log(carModel);

    homeButton.addEventListener('click', function() {
        alert("WARNING: you are about to leave this page your reservation progress will be lost");
        unrentCar(carMake, carModel, carYear);
    });
    catalogButton.addEventListener('click', function() {
        alert("WARNING: you are about to leave this page your reservation progress will be lost");
        unrentCar(carMake, carModel, carYear);
    });
    window.addEventListener('popstate', function() {
        alert("WARNING: you are about to leave this page your reservation progress will be lost");
        unrentCar(carMake, carModel, carYear);
    });
      
    window.addEventListener('unload', function() {
        alert("WARNING: you are about to leave this page your reservation progress will be lost");
        unrentCar(carMake, carModel, carYear);
    });

    window.addEventListener('beforeunload', function() {
        alert("WARNING: you are about to leave this page your reservation progress will be lost");
        unrentCar(carMake, carModel, carYear);
    });


    submitButton.disabled = true;

    agreeCheckbox.addEventListener("click", function() {
        if (agreeCheckbox.checked) {
            submitButton.disabled = false;
        } else {
            submitButton.disabled = true;
        }
    });

    let agree = this.document.getElementById("agree");
    let confirm = this.document.getElementById("submit");
    let reserve = document.getElementById("reserve");
    reserve.disabled = true;
    confirm.addEventListener("click", confirmPayment);
    agree.addEventListener("change", enableButton);

    function enableButton() {
        if (agree.checked) {
            reserve.disabled = false;
        } else {
            reserve.disabled = true;
        }
    }

    function confirmation() {
        window.location='/checkout-confirmation';
    }

    function confirmPayment() {
        let moneyInput = document.getElementById("money");
        if (moneyInput.value === null || moneyInput.value === "" || moneyInput.value < carCost) {
            alert("Please enter valid payment information.");
            console.log("error");
        } else if (parseFloat(moneyInput.value) < parseFloat(reserve.dataset.price)) {
            alert("You do not have enough money to rent the car. Please add more money to your account and try again.");
            console.log("error");
        } else if (reserve.value === "") {
            alert("Please enter in enough to pay for the car.");
            console.log("error");
        } else {
            confirmation();
        }
    }

    function unrentCar(carMake, carModel, carYear) {
        const xhr = new XMLHttpRequest();
        xhr.open('POST', '../unrent-car');
        xhr.setRequestHeader('Content-Type', 'application/json;charset=UTF-8');
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
        xhr.onload = function() {
          if (xhr.status === 200) {
            console.log('Car rental status updated successfully.');
          } else {
            console.log('Error updating car rental status.');
          }
        };
        xhr.onerror = function() {
          console.log('Error updating car rental status.');
        };
        xhr.send(JSON.stringify({
            'make': carMake,
            'model': carModel,
            'year': carYear,
        }));
        // var submitRental = document.createElement("form");
        // submitRental.action = "/unrent-car/";
        // submitRental.method = "POST";
      
        // var csrfInput = document.createElement("input");
        // csrfInput.type = "hidden";
        // csrfInput.name = "csrfmiddlewaretoken";
        // csrfInput.value = csrftoken;
      
        // var makeInput = document.createElement("input");
        // makeInput.type = "hidden";
        // makeInput.name = "make";
        // makeInput.value = carMake;
      
        // var modelInput = document.createElement("input");
        // modelInput.type = "hidden";
        // modelInput.name = "model";
        // modelInput.value = carModel;
      
        // var yearInput = document.createElement("input");
        // yearInput.type = "hidden";
        // yearInput.name = "year";
        // yearInput.value = carYear;
      
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
    
});

