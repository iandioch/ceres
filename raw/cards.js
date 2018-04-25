function loadURL(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open("get", url, true);
    xhr.onload = function() {
        var status = xhr.status;
        if (status == 200) callback(null, xhr.response);
        else callback(status);
    };
    xhr.send();
}

function onUpdateCeres(err, data) {
    if (err != null) {
        alert(err);
        return;
    }
    json = JSON.parse(data);
    console.log(json);
    new Vue({
        el: "#ceres",
        data: json,
    });
}

function updateCeres() {
    console.log("updateCeres()");
    loadURL("/cards", onUpdateCeres);
}

function loadCardPage(cardName, callback){
	var xhr = new XMLHttpRequest();
	xhr.open("get", "card/" + cardName, true);
	xhr.onload = function() {
		var status = xhr.status;
		if (status == 200) {
			callback(cardName, null, xhr.response);
		}else{
			callback(cardName, status);
		}
	};
	xhr.send();
}

function cardCallback(cardName, err, data) {
	if(err != null) {
		alert(err);
	}else{
		jsonData = JSON.parse(data);
		if(typeof cardData[cardName] == "undefined"){
			cardData[cardName] = jsonData;
		}
		for(var key in jsonData){
			cardData[cardName][key] = jsonData[key];
		}
	}
}

function createCardVue(cardName, cardData) {
	console.log("Creating vue " + cardName);
	new Vue({
		el: "#card_" + cardName,
		data: cardData[cardName],
	});
}

function updateCardData(cardName, cardData) {
	loadCardPage(cardName, function(cardName_, err, data){
		cardCallback(cardName_, err, data);
	});
}

// Run updateAll every 30 seconds
window.setInterval(updateCeres, 30000);
updateCeres();
console.log("interval set.");
