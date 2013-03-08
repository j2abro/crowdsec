/*

This file is just a test of including some datastructures (javasctipt objects) and js code in a file that can be called by flask.

// test - show alert box
setTimeout(function() { alert("OK, later, show this"); }, 200);

// another test, to test if js file was loaded. this will print as the first line of the html file for which this script was loaded.
document.write("external jrun.js loaded...."); 

*/

var listobject2 = {
	one: "hello",
	two: "world",	
	three: "bit",
	four: "star",
	five: "fish",
	six: "again",
	seven: "nowfinally"
}; 

var workoutSpeed = [
	{	name: "Idea List",	
		desc: "Create an ongoing list of tech and business model concepts. This list. Make it interactive where users could sort and add their own ideas.",	
		catgory: "Miscelaneous",
		enterprise: true,
		passion: 5,
		recurring_rev: true,
		tech_risk: 1,
		scalability: 5,
		phased: 5,
		sales_density: 5,
		big_potential: 2,				
	},
	{	name: "running app",	
		desc: "Add features to existing app.",	
		catgory: "Sports",
		enterprise: false,
		passion: 3,
		recurring_rev: true,
		tech_risk: 2,
		scalability: 3,
		phased: 4,
		sales_density: 5,
		big_potential: 1,				
	}
	
];


