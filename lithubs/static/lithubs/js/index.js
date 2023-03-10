let currentYear = () => {
	date = new Date().getFullYear();
	console.log(date);
	document.getElementById('date').innerHTML = `©️  ${date}`;
};

currentYear();
