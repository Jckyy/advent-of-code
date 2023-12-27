var fs = require("fs");

var rawData = fs.readFileSync("input.txt").toString().split("\n");

const sumArrayByLineBreak = (rawData) => {
	return rawData.reduce((totalCalories, cal, i) => {
		if (cal === "\r" || cal === "") {
			totalCalories.push(0);
		} else {
			totalCalories[totalCalories.length - 1] += parseInt(cal);
		}
		return totalCalories;
	}, []);
};

const maxCalories = Math.max(...sumArrayByLineBreak(rawData));

console.log(maxCalories);
