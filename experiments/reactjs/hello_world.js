var cl = {
	title: "lawn",
	color: "red",
	rating: 4
}

function rateColor(color, rating) {
	color.rating = rating
	return color
}

console.log(rateColor(cl, 5).rating)
console.log(cl.rating)

function rateColor2(cl, rating) {
	return Object.assign({}, cl, {rating:rating})
}

console.log(rateColor2(cl, 2).rating)
console.log(cl.rating)

var rateColor3 = (cl, rating) => 
	({
		...cl,
	})

console.log(rateColor3(cl, 1).rating)
console.log(cl.rating)
