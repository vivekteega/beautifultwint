var spawn = require('child_process').spawn

var twitterUsernames = ["saketrx", 
                        "vivekteega", 
                        "ranchimallflo", 
                        "zee24taasnews",
                        "alexmohajer",
                        "pbns_india",
                        "wtop",
                        "live_hindustan",
                        "kashjackson2018",
                        "livemint",
                        "trivworks",
                        "jagranenglish",
                        "tommyigoe",
                        "maevemarsden",
                        "anncoulter",
                        "iamjohnales",
                        "justin_marks_",
                        "carmenbeat",
                        "asranomani",
                        "ralf_stegner",
                        "iamjohnales",
                        "iamjohnales",
                        "ericg1247",
                        "canoe",
                        "lastampa",
                        "kris6news",
                        "the_hindu" ];

// create a child process to download csv data for all the people in the list 
for(var i=0; i<twitterUsernames.length; i++){
    var child = spawn("twint", ["-u", `${twitterUsernames[i]}`, "--limit", "10", "-o", `${twitterUsernames[i]}.csv`, "--csv"])
    child.stdout.on('data', function (data) {
        console.log('Fetching data of user ', data.toString())
    })
}