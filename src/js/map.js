var latitude_user;
var longitude_user;

let markers_array = [];

let API_IP = "http://127.0.0.1:5000"; //For testing

let magic_word = "geocatchermagicword";

function httpGet(theUrl)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.open( "GET", theUrl, false ); // false for synchronous request
    xmlHttp.send( null );
    return xmlHttp.responseText;
}

function parseGeocacheLine(line){
  line = line.split(magic_word);
  name_g = line[0];
  id_g = line[1];
  lat_g = parseFloat(line[2]);
  long_g = parseFloat(line[3]);

  if (isNaN(lat_g) == true || isNaN(long_g) == true){
    console.log("Wrong lat/lng");
    console.log(line);

  }
  else{
    let marker_desc = "<b>"+name_g+"</b><br>ID: "+id_g+"<br>"+lat_g.toFixed(7).toString()+","+long_g.toFixed(7).toString()+"<br> <a href='"+"https://www.geocaching.com/geocache/"+id_g+"' target='_blank'>Jump to GeoCaching.com</a>";

    //console.log(lat_g,long_g);
    let marker = L.marker([lat_g,long_g]).bindPopup(marker_desc).addTo(map);
    markers_array.push(marker);
    //console.log(markers_array.length);

  }

  
}

function putGeocaches(){
  for (let i = 0; i < markers_array.length; i++) {
    map.removeLayer(markers_array[i]);
  }
  markers_array = []; //Prevent memory hogging

  var popLocation= map.getCenter();
  console.log("Running putGeocaches!");
  let geocaches = httpGet(API_IP+"/api/v1/getdistance?lat="+popLocation['lat']+",long="+popLocation['lng']).split("\n");
  //console.log(geocaches.length);
  for (let i = 0; i < geocaches.length; i++) {
    if (i < 7000){
      parseGeocacheLine(geocaches[i]);
      document.getElementById('errortext').innerText = "GeoCaches:"+i.toString();
      document.getElementById('errortext').style.color = "black";
      
    }
    else{
      document.getElementById('errortext').innerText = "Error: Too many geocaches (showing 7000). Zoom in to see more!";
      document.getElementById('errortext').style.color = "red";
    }
  } 
}
const successCallback = (position) => {
    latitude_user = position.coords.latitude;
    longitude_user = position.coords.longitude;
    //map.panTo(new L.LatLng(latitude,longitude));
    map.setView([latitude_user,longitude_user], 9);
    //Weird bug: after this, all markers are removed. Rerun again
    putGeocaches();
    putGeocaches();
}
  
  const errorCallback = (error) => {
    console.log(error);
    latitude = 0;
    longitude = 0;
  };

navigator.geolocation.getCurrentPosition(successCallback, errorCallback);

//const map = L.map('map', {
 // center: [0,0],
 // zoom: 3.5
//});


//L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', { attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors' }).addTo(map);

console.log("[DEBUG] Running add markers")
putGeocaches();

console.log("[DEBUG] Adding button");
if (httpGet(API_IP+"/api/v1/ping") == "OK"){
  document.getElementById('serverconntext').innerText = "Server connection good!";
}
else{
  document.getElementById('serverconntext').style.color = "red";
  document.getElementById('serverconntext').innerText = "Backend offline";
}

