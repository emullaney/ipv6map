$(document).ready(function(){
    var mapData = [];
    $.getJSON('/api/addresses/?format=json&max_latitude=36&max_longitude=-78&min_latitude=34&min_longitude=-81', function( data ) {
          for(var i = 0; i < data.length; i++) {
            mapData.push({ "lat": data[i].latitude, "lng": data[i].longitude });
          }

        var testData = {
            data: mapData
        };

        // Layer for base map
        var baseLayer = L.tileLayer(
            'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
            maxZoom: 18
        });

        // configuration for the heatmap map layer
        var cfg = {
            // radius should be small ONLY if scaleRadius is true (or small radius is intended)
            "radius": 0.1,
                "maxOpacity": 0.9,
            // scales the radius based on map zoom
            "scaleRadius": true,
            // if set to false the heatmap uses the global maximum for colorization
            // if activated: uses the data maximum within the current map boundaries
            //   (there will always be a red spot with useLocalExtremas true)
            "useLocalExtrema": true,
            // which field name in your data represents the latitude - default "lat"
            latField: 'lat',
            // which field name in your data represents the longitude - default "lng"
            lngField: 'lng',
            // which field name in your data represents the data value - default "value"
            valueField: 'count'
        };

        var heatmapLayer = new HeatmapOverlay(cfg);

        // Leaflet map object
        // Start in zoomed in on Durham, NC
        var map = new L.Map('map', {
            center: new L.LatLng(36, -79),
            zoom: 10,
            layers: [baseLayer, heatmapLayer]
        });

        // place data on map
        heatmapLayer.setData(testData);

        // make accessible for debugging
        layer = heatmapLayer;

        map.on('moveend', function(e) {
           var bounds = map.getBounds();
           min_lat=bounds['_southWest']['lat'];
           min_lng=bounds['_southWest']['lng'];
           max_lat=bounds['_northEast']['lat'];
           max_lng=bounds['_northEast']['lng'];
           $.getJSON('/api/addresses/?format=json&max_latitude=' + max_lat + '&max_longitude=' + max_lng + '&min_latitude=' + min_lat + '&min_longitude=' + min_lng, function( newData ) {
             var newBoundsData = [];
             for(var i = 0; i < newData.length; i++) {
               newBoundsData.push({ "lat": newData[i].latitude, "lng": newData[i].longitude });
             }
            var testData = {
              data: newBoundsData
            };
            // place data on map
            heatmapLayer.setData(testData);
           });

        });
    });
});