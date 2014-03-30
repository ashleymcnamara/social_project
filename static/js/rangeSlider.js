/**
 * Created by Ashley on 2014.
 */



function slider_range(min,max) {
    var SlideTimeout;
    $("#sidr-id-slider-range").slider({
        range: true,
        min: 0,
        max: 1440,
        values: [ min, max ],

        slide: function (event, ui) {
            var val1 = prettyPrint(ui.values[ 0 ]);
            var val2 = prettyPrint(ui.values[ 1 ]);
            $("#sidr-id-amount").val(val1 + " - " + val2);

        },
        stop: function (event, ui) {
           $.cookie("min_", ui.values[ 0 ]);
           $.cookie("max_", ui.values[ 1 ]);
           updateTime(ui.values[ 0 ],ui.values[ 1 ]);

        }



    });
    $("#amount").val(prettyPrint($("#sidr-id-slider-range").slider("values", 0)) +
        " - " + prettyPrint($("#sidr-id-slider-range").slider("values", 1)));
}
function prettyPrint(minutes) {
    const minutesInDay = 1440;
    const minutesInHour = 60;
    var days = 0;
    var hours = 0;
    while (minutes >= minutesInDay) {
        days++;
        minutes = minutes - minutesInDay;
    }
    while (minutes >= minutesInHour) {
        hours++;
        minutes = minutes - minutesInHour;
    }
    return days + "d " + hours + "h " + minutes + "m";
}