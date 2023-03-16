let currentYear = () => {
	date = new Date().getFullYear();
	console.log(date);
	document.getElementById('date').innerHTML = `©️  ${date}`;
};

let onChange = () => {
	document.getElementById('profile-menu').style.display = 'block';
}

currentYear();
onChange();
