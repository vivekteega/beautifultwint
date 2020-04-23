var d3 = require("d3");

/*d3.csv("vivekteega.csv", function(d) {
    return {
      tweet: new Date(+d.Year, 0, 1), // convert "Year" column to Date
      likes_count: d.Make,
      retweets_count: d.Model,
      length: +d.Length // convert "Length" column to number
    };
  }, function(error, rows) {
    console.log(rows);
  });*/

d3.csv("vivekteega.csv", function (data) {
  for (var i = 0; i < data.length; i++) {
    console.log(data[i].tweet);
    console.log(data[i].likes_count);
    console.log(data[i].retweets_count);
  }
});
