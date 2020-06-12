// With JQuery
$('#length').slider({
	formatter: function(value) {
		return 'Current value: ' + value;
	}
});
