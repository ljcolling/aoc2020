var fs = require("fs");
var text = fs.readFileSync("./data.txt", "utf-8");
var textByLine = text.split('\n');

let number = 0;
let number1 = 0;

textByLine.forEach(element => {
    let replaceElement = element.replace(":", "");
    let ruleSplit = replaceElement.split(" ");
    const regex = new RegExp(ruleSplit[1], "g");
    
    let count = (ruleSplit[2].match(regex) || []).length;
    let params = ruleSplit[0].split("-");
    
    if (count >= params[0] && count <= params[1]) {
       number++;
    }

});

textByLine.forEach(element => {
    let replaceElement = element.replace(":", "");
    let ruleSplit = replaceElement.split(" ");
    
    let params = ruleSplit[0].split("-");
    
    var passwordSplit = ruleSplit[2].split("");;
    
    let param1 = parseInt(params[0]) - 1;
    let param2 = parseInt(params[1]) - 1;
    
    if ((passwordSplit[param1] === ruleSplit[1]) || (passwordSplit[param2] === ruleSplit[1])) {
    	if (passwordSplit[param1] !== passwordSplit[param2]) {
    	    number1++;
    	}
    }
});


console.log(number); // part 1
