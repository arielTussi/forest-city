let map;
let marker;
let geocoder;
let loc_arr = [];
let tags_arr = [];

function s(){
// get list of places
  var input = document.getElementById("par").innerText;
  var tags = document.getElementById("tags").innerText;
  // clean sides
  var input=input.slice(0,-1);
  var tags=tags.slice(0,-1);
    // make it a list
  var input=input.split(",");
  var tags=tags.split(",");
      // loop on list
  for (let i = 0; i < input.length; i++) {
        input[i]=input[i].slice(2,-1);
        tags[i]=tags[i].slice(2,-1);
        }
   loc_arr = input;
   tags_arr = tags;

}




function initMap() {
    geocoder = new google.maps.Geocoder();
    map = new google.maps.Map(document.getElementById("map"), {
    center: { lat:  32.0825, lng:  34.7713 },
    zoom: 14,
    mapTypeControl: false,
    fullscreenControl: false,
    scaleControl: false,
    streetViewControl: false,
    zoomControl: false


  });
// search only
  const green_flag = {
    path: 'M 0,0 C -2,-20 -10,-22 -10,-30 A 10,10 0 1,1 10,-30 C 10,-22 2,-20 0,0 z',
    fillColor: "green",
    fillOpacity: 0.6,
    strokeWeight: 0,
    rotation: 0,
    scale: 3,
      };

// search only
marker = new google.maps.Marker({
    map:map,
    icon: green_flag
  });

//  const inputText = document.getElementById("search");
//  map.controls[google.maps.ControlPosition.TOP_CENTER].push(inputText);

//  inputText.style.width= "94%";
//  inputText.style.background= "white";
//  inputText.style.top="30px";


//  inputText.addEventListener("keyup", function(event) {
//  if (event.keyCode === 13) {
//    geocode({ address: inputText.value });
//  }
//});
}



// geocode the search bar input and tags
function geocode(request) {
  geocoder
    .geocode(request)
    .then((result) => {
      const { results } = result;
      map.setCenter(results[0].geometry.location);
      marker.setPosition(results[0].geometry.location);
      marker.setMap(map);
      return results;
    })
    .catch((e) => {
      alert("Geocode was not successful for the following reason: " + e);
    });

}



// when button clicked marker shown on map
//get color from html(onclick),every color belong to a tag, loop over tag, locs arr that is known
//check what color is clicked and add_marker()
function make_marker(color)
{
    const my_marker = {
    path: 'M 0,0 C -2,-20 -10,-22 -10,-30 A 10,10 0 1,1 10,-30 C 10,-22 2,-20 0,0 z',
    fillColor: color,
    fillOpacity: 0.6,
    strokeWeight: 0,
    rotation: 0,
    scale: 3,
      };

// add  new marker to the map
function add_marker(cords){

var  marker = new google.maps.Marker({
    position: cords,
    map:map,
    icon: my_marker
  });
 }
if (color=="red"){
for(var i =0; i< loc_arr.length; i++){
    if (tags_arr[i]=="גינה קהילתית"){
         geocoder
           .geocode({ address:loc_arr[i] })
           .then((result) => {
             const { results } = result;
             add_marker(results[0].geometry.location);
            })
    }
}
}
if (color=="green"){
for(var i =0; i< loc_arr.length; i++){

    if (tags_arr[i]=="גינה שיקומית"){
         geocoder
           .geocode({ address:loc_arr[i] })
           .then((result) => {
             const { results } = result;
             add_marker(results[0].geometry.location);
            })
    }
}
}
if (color=="blue"){
    for(var i =0; i< loc_arr.length; i++){
        if (tags_arr[i]=="יער מאכל"){
             geocoder
               .geocode({ address:loc_arr[i] })
               .then((result) => {
                 const { results } = result;
                 add_marker(results[0].geometry.location);
                })
        }
    }
}
if (color=="yellow"){
    for(var i =0; i< loc_arr.length; i++){
        if (tags_arr[i]=="קבוצות וואטסאפ"){
             geocoder
               .geocode({ address:loc_arr[i] })
               .then((result) => {
                 const { results } = result;
                 add_marker(results[0].geometry.location);
                })
        }
    }
}
if (color=="purple"){
    for(var i =0; i< loc_arr.length; i++){
        if (tags_arr[i]=="החלפת זרעים ויחוריים"){
             geocoder
               .geocode({ address:loc_arr[i] })
               .then((result) => {
                 const { results } = result;
                 add_marker(results[0].geometry.location);
                })
        }
    }
}
if (color=="orange"){
    for(var i =0; i< loc_arr.length; i++){
        if (tags_arr[i]=="התנדבות"){
             geocoder
               .geocode({ address:loc_arr[i] })
               .then((result) => {
                 const { results } = result;
                 add_marker(results[0].geometry.location);
                })
        }
    }
}
if (color=="maroon"){
    for(var i =0; i< loc_arr.length; i++){
        if (tags_arr[i]=="נטיעות"){
             geocoder
               .geocode({ address:loc_arr[i] })
               .then((result) => {
                 const { results } = result;
                 add_marker(results[0].geometry.location);
                })
        }
    }
}
if (color=="black"){
    for(var i =0; i< loc_arr.length; i++){
        if (tags_arr[i]=="חוג בית"){
             geocoder
               .geocode({ address:loc_arr[i] })
               .then((result) => {
                 const { results } = result;
                 add_marker(results[0].geometry.location);
                })
        }
    }
}
if (color=="#F31AB9"){
    for(var i =0; i< loc_arr.length; i++){
        if (tags_arr[i]=="סיורים והדרכות"){
             geocoder
               .geocode({ address:loc_arr[i] })
               .then((result) => {
                 const { results } = result;
                 add_marker(results[0].geometry.location);
                })
        }
    }
}
if (color=="brown"){
    for(var i =0; i< loc_arr.length; i++){
        if (tags_arr[i]=="קורסים "){
             geocoder
               .geocode({ address:loc_arr[i] })
               .then((result) => {
                 const { results } = result;
                 add_marker(results[0].geometry.location);
                })
        }
    }
}
}