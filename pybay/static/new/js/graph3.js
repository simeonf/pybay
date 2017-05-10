////////////
//Pie charts
////////////

 var data =[
          { origin: 'In Bay Area', label: 'Outside', count: 6 },
          { origin: 'In Bay Area', label: 'Local', count: 94 },
          { origin: 'Gender', label: 'Female', count: 25 },
          { origin: 'Gender', label: 'Male', count: 75 },
          { origin: 'Expertise Level', label: 'Beginner', count: 13 },
          { origin: 'Expertise Level', label: 'Intermediate', count: 53 },
          { origin: 'Expertise Level', label: 'Advance', count: 30 },
          { origin: 'Expertise Level', label: 'Non-Technical', count: 4 },
        ];
 //Chart size vars
var	m = 30,
	radius = 120,
	color = d3.scaleOrdinal(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);
//Pie Canvas
var pie = d3.pie()
    .value(function(d) { return +d.count; })
    .sort(function(a, b) { return b.count - a.count; });

var arc = d3.arc()
    .innerRadius(0) //radius / 2 for dougnut
    .outerRadius(radius);

//Groupby
var rports = d3.nest()
      .key(function(d) { return d.origin; })
      .entries(data);

var svg = d3.select("#pie1").selectAll("div")
    .data(rports)
    .enter().append("div")
      .style("display", "inline-block")
      .style("width", (radius + m) * 2 + "px")
      .style("height", (radius + m) * 2 + "px")
    .append("svg")
      .attr("width", (radius + m) * 2)
      .attr("height", (radius + m) * 2)
    .append("g")
      .attr("transform", "translate(" + (radius + m) + "," + (radius + m) + ")");

// titles
svg.append("text")
      .attr("dy", -(radius+10))
      .attr("text-anchor", "middle")
      .style("font", "bold 14px Arial")
      .text(function(d) { return d.key; });

//pass vals
var g = svg.selectAll("g")
    .data(function(d) { return pie(d.values); })
    .enter().append("g");

//colors + mouseover
 g.append("path")
      .attr("d", arc)
      .style("fill", function(d) { return color(d.data.label); })
    .append("title")
      .text(function(d) { return d.data.label + ":\n" + d.data.count +"%"; });

 g.filter(function(d) { return d.endAngle - d.startAngle > .35; }).append("text")
      .attr("dy", ".35em")
      .attr("text-anchor", "middle")
      .attr("transform", function(d) { return "translate(" + arc.centroid(d) + ")rotate(" + angle(d) + ")"; })
      .text(function(d) { return d.data.label; });

 function angle(d) {
    var a = (d.startAngle + d.endAngle) * 90 / Math.PI - 90;
    return a > 90 ? a - 180 : a;
  }
