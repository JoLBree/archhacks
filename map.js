google.charts.load('current', { 'packages': ['map'] });
google.charts.setOnLoadCallback(drawMap);

var vis_data = [['Lat', 'Lng', 'School', 'Marker']]
var wash_U_index = 0;

$.getJSON("school_locs5.json", function(json) {
	for (var i = 0; i < json.length; i++){
		var marker = 'default';
		if (json[i].school == 'Washington University in St. Louis'){
			wash_U_index = i;
			marker = 'washu'
		}
		vis_data.push([json[i].lat, json[i].lng, json[i].school+" ("+json[i].application_count+")", marker]);
	}
	if (vis_data.length > 400){
		console.log("Too many schools, over API limit");
	}
});

function drawMap() {
	var data = google.visualization.arrayToDataTable(vis_data);
	var options = {
		showTip: true,
		zoomLevel: 4,
		enableScrollWheel: true,
		mapType: 'normal',
		icons: {
			'washu': {
					normal: 'http://icons.iconarchive.com/icons/icons-land/vista-map-markers/48/Map-Marker-Ball-Azure-icon.png',
					selected: 'http://icons.iconarchive.com/icons/icons-land/vista-map-markers/48/Map-Marker-Ball-Right-Azure-icon.png'
			}
			// 'washu': {
			//     normal: 'http://archhacks.io/static/images/archhackslogo-title.png',
			//     selected: 'http://archhacks.io/static/images/archhackslogo-title.png'
			// }
		}
	 };
	var map = new google.visualization.Map(document.getElementById('map_div'));
	google.visualization.events.addOneTimeListener(map, 'ready', function(){ 
		map.setSelection([{row:wash_U_index, column:null}]);
	});
	map.draw(data, options);
};