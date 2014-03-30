$(function () {
    var values = [0, 1, 3, 5, 10, 15, 30, 45, 60, 75, 90, 105, 120,150, 180,210, 240,270, 300,220, 360,290, 420,450, 480,510,540,570, 600,630,660,690,720,750,780];
    $("#slider").slider({
        range: true,
        min: 0,
        max: 780,
        slide: function (event, ui) {
            $("#id_timeString").val(prettyPrint(ui.value));
        }
    });
    $("#id_timeString").val(prettyPrint($("#slider").slider("values", 0)));
});