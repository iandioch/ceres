function loadPage(url, callback){
	var xhr = new XMLHttpRequest();
	xhr.open("get", url, true);
	xhr.onload = function() {
		var status = xhr.status;
		if (status == 200) {
			callback(null, xhr.response);
		}else{
			callback(status);
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
	new Vue({
		el: "#card_" + cardName,
		data: cardData[cardName],
	});
}

function updateCardData(cardName, cardData) {
	loadPage("card/" + cardName, function(err, data){
		cardCallback(cardName, err, data);
	});
}

var cardList = document.getElementById('ceres_cards').children;
var cardData = {};

for(var i = 0; i < cardList.length; i ++) {
	var id = cardList[i].id;
	var name = id.substring(id.indexOf("_") + 1);
	loadPage("card/" + name, function(err, data){
		cardCallback(name, err, data);
		createCardVue(name, cardData);
	});
}

var updateAll = function() {
	for(var key in cardData) {
		updateCardData(key, cardData);
	}
}
window.setInterval(updateAll, 60000);
