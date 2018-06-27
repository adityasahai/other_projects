var morning = {
	breakfast: "oatmeal",
	lunch: "peanut butter and jelly"
}

var dinner = "mac"
var lunch = "what else!"

var bpm = {
	dinner,
	lunch, // this changes the original value of lunch. A variable named that! this is crazy!
	...morning
}

console.log(bpm)
