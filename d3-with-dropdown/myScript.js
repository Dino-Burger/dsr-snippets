d3.csv("https://raw.githubusercontent.com/chumo/Data2Serve/master/transition_clusters.csv", d3.autoType)
  .then(function(myData){
    var canv = d3.select('svg')

    var circles = canv.selectAll("circle").data(myData);

    circles.enter()
        .append("circle")
        .attr("cx",d => d.Xi) // function(d){return d.Xi;}
        .attr("cy",d => d.Yi)
        .attr("r",5)
        .attr("fill", d => d.color)

        .transition().duration(3000)

        .attr("cx",d => d.Xf)
        .attr("cy",d => d.Yf)
        
        .transition().duration(3000).ease(d3.easeElastic)

        .attr("cx",d => d.Xi)
        .attr("cy",d => d.Yi);
    
    

   });



   function changePlot(x){
    var xString = document.getElementById("radius").value;
    var xInt = parseInt(xString)
 
    console.log(xInt);
    d3.selectAll('circle').transition().duration(3000)
    .attr('r', xInt);

};

