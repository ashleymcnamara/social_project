/**
 * Created by Ashley on 2014.
 */



function updateTime(min, max) {
   $("input[id^='LIST_time_']" ).each(function (index) {
       if($( this ).val()<min || $( this ).val()<min >max ){
           $( this ).parent().hide();
       } else {
            $( this ).parent().show();
       }
    });
}
