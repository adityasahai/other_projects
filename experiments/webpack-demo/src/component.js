export default (text = "Hello Aditya") => {
	const element = document.createElement("div");

	element.innerHTML = text;

	return element;
};
