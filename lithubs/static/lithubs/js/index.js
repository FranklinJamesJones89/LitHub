let currentYear = () => {
	date = new Date().getFullYear();
	console.log(date);
	document.querySelector('.copyright').innerHTML = `©️  ${date}`;
};

let editShow = () => {
	document.getElementById('profile-edit-form').style.display = 'block';
}

let editHide = () => {
	document.getElementById('profile-edit-form').style.display = 'none'
}


currentYear();
editShow();
editHide();
