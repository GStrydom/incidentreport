$(function () {
	var introguide = introJs();
	// var startBut = $('#start-button');

	introguide.setOptions({
    steps: [
        {
          element: '#create-but',
          intro: 'Click here to create a new Incident Report.',
          position: 'bottom'
        },
        {
          element: '#incident-table',
          intro: 'Here you will find a list of all the current reported incidents. You can search and filter as needed.',
          position: 'bottom'
        },
        {
          element: '.nav-title',
          intro: 'Hover over each title to display a longer description.',
          position: 'bottom'
        },
        {
          element: '.readtutorial a',
          intro: 'Click this orange button to view the tutorial article in a new tab.',
          position: 'right'
        },
        {
          element: '.nav-menu',
          intro: "Each demo will link to the previous & next entries.",
          position: 'bottom'
        }
    ]
});
})