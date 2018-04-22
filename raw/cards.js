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

/*
var cardList = document.getElementById('ceres_cards').children;
var cardData = {};

for(var i = 0; i < cardList.length; i ++) {
	var id = cardList[i].id;
	var name = id.substring(id.indexOf("_") + 1);
	loadCardPage(name, function(cardName, err, data){
		cardCallback(cardName, err, data);
		createCardVue(cardName, cardData);
	});
    console.log("card data");
    console.log(cardData);
}

var updateAll = function() {
	console.log("Updating");
	for(var key in cardData) {
		updateCardData(key, cardData);
	}
}*/
// Run updateAll every 60 seconds
//window.setInterval(updateAll, 60000);
window.setInterval(updateCeres, 3000);
updateCeres();
console.log("interval set.");
