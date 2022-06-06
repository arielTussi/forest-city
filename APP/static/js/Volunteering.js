var map1;
function initMap() {
geocoder = new google.maps.Geocoder();


    map = new google.maps.Map(document.getElementById("map1"), {
    center: { lat:  32.082446260430295, lng:  34.771298377272764 },
    zoom: 10,

    mapTypeControl: false,
    fullscreenControl: false,
    scaleControl: false,
    streetViewControl: false,
    zoomControl: false
    });

const green_flag = {
    path: 'M 0,0 C -2,-20 -10,-22 -10,-30 A 10,10 0 1,1 10,-30 C 10,-22 2,-20 0,0 z',
    fillColor: "green",
    fillOpacity: 0.6,
    strokeWeight: 0,
    rotation: 0,
    scale: 3,
      };
function add_marker(cords){
var  marker = new google.maps.Marker({
    position: cords,
    map:map,
    icon: green_flag
  });
  }
var input = document.getElementById("par").innerText;
  geocoder
    .geocode({ address:input })
    .then((result) => {
      const { results } = result;
      add_marker(results[0].geometry.location);

    })
}

function ud(){

// get list of places
  var input = document.getElementById("ud").innerText;
  // clean sides
  var input=input.slice(0,-1);
    // make it a list
  var input=input.split(",");
      // loop on list
  for (let i = 0; i < input.length; i++) {
        input[i]=input[i].slice(2,-1);

        }
        return input;

}