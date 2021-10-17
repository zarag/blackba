/* Project specific Javascript goes here. */
$(document).ready(function () {
  $('li.active').removeClass('active');
  $('a[href="' + location.pathname + '"]').closest('li').addClass('active');
  $('.carousel').each(function () { $(this).find('.carousel-item').first().addClass('active') });
  // $('#id_birthday').datepicker({firstDay: 1,
  //     dateFormat: "dd/mm/yyyy",
  //     defaultDate: "16/06/2017",
  //     language: 'bs',
  //     today: "Danas",
  //     dayNamesShort: ['So','Mo','Di','Mi','Do','Fr','Sa'],
  //     days: ["Sunnday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
  // });

  let timeoutID = null;

  $("#coupon-search-text").keyup(function (e) {
    clearTimeout(timeoutID);
    var input = $('#coupon-search-text').val();

    timeoutID = setTimeout(() => {
      $.ajax({
        url: '/coupons/search',
        data: {
          'inputValue': input
        },
        dataType: 'json',
        success: function (data) {
          document.getElementById('search-results').innerHTML = data['html_from_view'];
        },
        error: function (e) {
          console.log(e);
        }
      });
    }, 500);
  });

  $("#search-results").on('click', '#couponsnext', function() {
    var search_input = $('#coupon-search-text').val();
    var page_number = $('#coupons-page-number').val();
    $.ajax({
      url: '/coupons/search',
      data: {
        'inputValue': search_input,
        'page': Number(page_number) + 1
      },
      dataType: 'json',
      success: function (data) {
        document.getElementById('search-results').innerHTML = data['html_from_view'];
      },
      error: function (e) {
        console.log(e);
      }
    });
  });


  $("#search-results").on('click', '#couponsprevious', function() {
    var search_input = $('#coupon-search-text').val();
    var page_number = $('#coupons-page-number').val();
    $.ajax({
      url: '/coupons/search',
      data: {
        'inputValue': search_input,
        'page': Number(page_number) - 1
      },
      dataType: 'json',
      success: function (data) {
        document.getElementById('search-results').innerHTML = data['html_from_view'];
      },
      error: function (e) {
        console.log(e);
      }
    });
  });
});
