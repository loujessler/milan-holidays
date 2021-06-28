var options = {
 componentRestrictions: {country: "it"}
};
var output = document.getElementById('id_from_transfer');
var autocomplete = new google.maps.places.Autocomplete(output,options);

var input = document.getElementById('id_to_transfer');
var autocomplete2 = new google.maps.places.Autocomplete(input,options);
console.log(autocomplete2);

//Работа с картами

var directionsService = new google.maps.DirectionsService();
var directionsRenderer = new google.maps.DirectionsRenderer();

var map;

var map = new google.maps.Map(document.getElementById('map'), {
  mapTypeControl: false,
  center: {lat: 45.4838344197085, lng: 9.202223219708458},
  zoom: 11
});
directionsRenderer.setMap(map);



console.log(autocomplete);
console.log(autocomplete2);

function takeValue(){
  console.log(document.getElementById('id_from_transfer_lng_id').value);
  console.log(document.getElementById('id_from_transfer').value);
  console.log(document.getElementById('id_from_transfer_lng_id').value.length);
  console.log(document.getElementById('link_to_order').value);
  if (autocomplete.getPlace() == null) {
    console.log(autocomplete.getPlace());
    console.log(autocomplete2.getPlace());
  }

  if (document.getElementById('id_from_transfer').value == "" || document.getElementById('id_to_transfer').value == "") {
    if (document.getElementById('id_from_transfer').value == "") {
      document.getElementById('id_from_transfer').classList.add("mistake");
      setTimeout(
        () => document.getElementById('id_from_transfer').classList.remove("mistake"),
        1000
      );
    }
    if (document.getElementById('id_to_transfer').value == "") {
      document.getElementById('id_to_transfer').classList.add("mistake");
      setTimeout(
        () => document.getElementById('id_to_transfer').classList.remove("mistake"),
        1000
      );
    };
  }
  else {
    if (autocomplete.getPlace() == null || autocomplete2.getPlace() == null) {
      if (autocomplete.getPlace() == null) {
        document.getElementById('id_from_transfer').classList.add("mistake");
        setTimeout(
          () => document.getElementById('id_from_transfer').classList.remove("mistake"),
          1000
        );
      }
      if (autocomplete2.getPlace() == null) {
        document.getElementById('id_to_transfer').classList.add("mistake");
        setTimeout(
          () => document.getElementById('id_to_transfer').classList.remove("mistake"),
          1000
        );
      }
    }
    else {
      document.getElementById('id_from_transfer_lng_id').value = autocomplete.getPlace().place;
      document.getElementById('id_from_transfer_lng').value = autocomplete.getPlace().geometry.location;

      document.getElementById('id_to_transfer_lng_id').value = autocomplete2.getPlace().place_id;
      document.getElementById('id_to_transfer_lng').value = autocomplete2.getPlace().geometry.location;
      func(document.getElementById('link_to_order').value);
    }
  }
}


// Условие наличия значений в скрытом input
function calculateRoute(){
   if (document.getElementById('id_from_transfer_lng').value == "undefined") {
     document.getElementById('id_from_transfer').value = ""
     document.getElementById('id_to_transfer').value = ""

     var  startLat = autocomplete.getPlace().geometry.location.lat();
     var  startLng = autocomplete.getPlace().geometry.location.lng();

     var  endLat = autocomplete2.getPlace().geometry.location.lat();
     var  endLng = autocomplete2.getPlace().geometry.location.lng();

     var request = {
       origin:  {lat: startLat, lng: startLng},
       destination: {lat: endLat, lng: endLng},
       travelMode: 'DRIVING'
     };
     console.log(request);
     directionsService.route(request, function(response, status) {
       if (status == 'OK') {
         directionsRenderer.setDirections(response);
       }
     });

   } else {

     var id_from_transfer_lng_id = document.getElementById('id_from_transfer_lng_id').value;
     var id_from_transfer_lng = document.getElementById('id_from_transfer_lng').value;

     var id_to_transfer_lng_id = document.getElementById('id_to_transfer_lng_id').value;
     var id_to_transfer_lng = document.getElementById('id_to_transfer_lng').value;


     console.log(id_from_transfer_lng);

     var properties = id_from_transfer_lng.split(', ');
     properties[0] = properties[0].replace(/\(|\)/g, '');
     properties[1] = properties[1].replace(/\(|\)/g, '');
     console.log(properties);

     var  startLat = parseFloat(properties[0]);
     var  startLng = parseFloat(properties[1]);

     var properties = id_to_transfer_lng.split(', ');
     properties[0] = properties[0].replace(/\(|\)/g, '');
     properties[1] = properties[1].replace(/\(|\)/g, '');
     console.log(properties);

     var  endLat = parseFloat(properties[0]);
     var  endLng = parseFloat(properties[1]);

     var request = {
         origin:  {lat: startLat, lng: startLng},
         destination: {lat: endLat, lng: endLng},
         travelMode: 'DRIVING'
     };

     console.log(request);
     directionsService.route(request, function(response, status) {
       if (status == 'OK') {
         directionsRenderer.setDirections(response);
       }
     });
  }
}

directionsRenderer.addListener('directions_changed', function() {
  computeTotalDistance(directionsRenderer.getDirections());
});

function computeTotalDistance(result) {
  var total = 0;
  var myroute = result.routes[0];
  for (var i = 0; i < myroute.legs.length; i++) {
    total += myroute.legs[i].distance.value;
  }
  total = total / 1000;

  // document.getElementById('total').innerHTML ='Расстояние: ' + total + ' km';
  document.getElementById('total').innerHTML = total;
}

document.getElementById('route_draw').onclick=function(){
  if (document.getElementById("id_from_transfer_lng_id").value != "undefined") {
    takeValue();
    calculateRoute();
    setTimeout(calculatePrice, 700);
  }
  else {
    calculateRoute();
    setTimeout(calculatePrice, 700);
  }
};
calculateRoute();
