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
		console.log(jsonData);
		cardData[cardName] = jsonData;
		console.log(jsonData["time"]);
	}
}

function createCardVue(cardName, cardData) {
	console.log("Looking good");
	new Vue({
		el: "#card_" + cardName,
		data: cardData[cardName],
	});
}

function updateCardData(cardName, cardData) {
	console.log("I have been asked to update card " + cardName);
	loadPage("card/" + cardName, function(err, data){
		cardCallback(cardName, err, data);
	});
}

var cardList = document.getElementById('ceres_cards').children;
var cardData = {};
console.log("About to iterate yo");

for(var i = 0; i < cardList.length; i ++) {
	var id = cardList[i].id;
	var name = id.substring(id.indexOf("_") + 1);
	loadPage("card/" + name, function(err, data){
		console.log("Callback from loadPage #1 ayo");
		cardCallback(name, err, data);
		createCardVue(name, cardData);
	});
}

var updateAll = function() {
	console.log("Updating all.");
	for(var key in cardData) {
		console.log("should update #" + key + " lol");
		updateCardData(key, cardData);
	}
}

window.setInterval(updateAll, 10000);
