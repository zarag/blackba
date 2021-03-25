/* Project specific Javascript goes here. */
$(document).ready(function() {
    $('li.active').removeClass('active');
    $('a[href="' + location.pathname + '"]').closest('li').addClass('active');
    $('.carousel').each(function(){ $(this).find('.carousel-item').first().addClass('active')});
    // $('#id_birthday').datepicker({firstDay: 1,
    //     dateFormat: "dd/mm/yyyy",
    //     defaultDate: "16/06/2017",
    //     language: 'bs',
    //     today: "Danas",
    //     dayNamesShort: ['So','Mo','Di','Mi','Do','Fr','Sa'],
    //     days: ["Sunnday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    // });
});
