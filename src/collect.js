//*[@id="ember103"]/div

var x = $x('//*[@id="ember103"]/div//p');
var temp = '';
var arr = []
var city,num;
for(var i=0;i<x.length;++i){
	temp = x[i].textContent;
	arr.push(temp);
}


for(var i=0;i<arr.length;++i){
	console.log(arr[i]);
}
// get population

var x = $x('//*[@id="__next"]/div/div[1]/div[3]/div[7]/div[1]/div/div/div/div/div[2]/table//tr')
var arr = []
var city,num;
for(var i=0;i<x.length;++i){
	temp = x[i].textContent;
	arr.push(temp);
}

for(var i=0;i<arr.length;++i){
	console.log(arr[i]);
}

// get density

var x = document.getElementsByClassName("wikitable");

var arr = []
var city,num;
for(var i=0;i<x.length;++i){
	temp = x[i]
	for(var k=1;k<x[i].rows.length;++k){
		city = x[i].rows[k].cells[1].textContent;
		num = x[i].rows[k].cells[2].textContent;
		arr.push([city, num]);
		console.log(city, '-', num)
	}
}







var arr = []
var city,num;
for(var i=0;i<x.length;++i){
	for(var k=1;k<x[i].rows.length;++k){
		console.log(x[i].rows[k])
	}
}


