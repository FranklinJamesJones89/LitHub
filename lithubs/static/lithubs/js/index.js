function getQuote() {
	 fetch('https://type.fit/api/quotes')
		 .then((res) => res.json())
		 .then((data) => {
		let randomNum = Math.floor(Math.random() * data.length);
		let quote = (data[randomNum])
		document.getElementById('#quote').innerHTML = quote;
			 console.log(quote);
	});
};

getQuote();
