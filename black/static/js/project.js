/* Project specific Javascript goes here. */
$(document).ready(function() {
    $('li.active').removeClass('active');
    $('a[href="' + location.pathname + '"]').closest('li').addClass('active');
    $('.carousel').each(function(){ $(this).find('.carousel-item').first().addClass('active')});
});
