// Форма телефона
// function phoneMask() {
//   var num = $(this).val().replace(/\D/g,'');
//   $(this).val(num.substring(0,1) + '(' + num.substring(1,4) + ')' + num.substring(4,7) + '-' + num.substring(7,11));
// }
// $('#id_phone').keyup(phoneMask);

// validate step1
$('#route_draw').on('click', function() {
    if (document.getElementById('id_from_transfer').value == "") {
        return false;
    }

    console.log('passed');

});

var email = document.getElementById("id_from_transfer");

email.addEventListener("input", function (event) {
  if (email.validity.typeMismatch) {
    email.setCustomValidity("I expect an e-mail, darling!");
  } else {
    email.setCustomValidity("");
  }
});


$( function() {
  $( "#id_time_from" ).datepicker({
    changeMonth: true,
    changeYear: true
  });
} );

$(function() {

  $('#id_time_from').datepicker($.datepicker.regional["ru"]);

});

$('#id_phone').inputmask('+7 (999) 999 99 99', {
  clearMaskOnLostFocus: true,
});

$('.js-form-validate').submit(function () {
  var form = $(this);
  var field = [];
  form.find('input[data-validate]').each(function () {
    field.push('input[data-validate]');
    var value = $(this).val(),
        line = $(this).closest('.some-form__line');
    for(var i=0;i<field.length;i++) {
      if( !value ) {
        line.addClass('some-form__line-required');
        setTimeout(function() {
          line.removeClass('some-form__line-required')
        }.bind(this),2000);
        event.preventDefault();
      }
    }
  });
});

$('#steps').steps({
       onFinish: function () { $('#main_button').click(); }
   });

// input number
jQuery('<div class="quantity-nav"><div class="quantity-button quantity-up">+</div><div class="quantity-button quantity-down">-</div></div>').insertAfter('.quantity input');
jQuery('.quantity').each(function() {
  var spinner = jQuery(this),
    input = spinner.find('input[type="number"]'),
    btnUp = spinner.find('.quantity-up'),
    btnDown = spinner.find('.quantity-down'),
    min = input.attr('min'),
    max = input.attr('max');

  btnUp.click(function() {
    var oldValue = parseFloat(input.val());
    if (oldValue >= max) {
      var newVal = oldValue;
    } else {
      var newVal = oldValue + 1;
    }
    spinner.find("input").val(newVal);
    spinner.find("input").trigger("change");
  });

  btnDown.click(function() {
    var oldValue = parseFloat(input.val());
    if (oldValue <= min) {
      var newVal = oldValue;
    } else {
      var newVal = oldValue - 1;
    }
    spinner.find("input").val(newVal);
    spinner.find("input").trigger("change");
  });

});
// input number end


// $("#step1").validate();



//
//
// var from_transfer = $('#id_from_transfer');
// console.log(from_transfer);
// console.log(from_transfer.valid());
// var from_transferValidator = from_transfer.validate();
//
// var time_from = $('#id_time_from');
// console.log(time_from);
// console.log(time_from.valid());
// var time_fromValidator = time_from.validate();
//
// var to_transfer = $('#id_to_transfer');
// var to_transferValidator = to_transfer.validate();
//
// var passenger = $('#id_passenger');
// var passengerValidator = passenger.validate();
//
// var frmLogin = $('#id_passenger');
// var frmLoginValidator = frmLogin.validate();
//
// var frmMobile = $('#frmMobile');
// var frmMobileValidator = frmMobile.validate();
//
//
// $('#steps').steps({
//   onChange: function (currentIndex, newIndex, stepDirection) {
//     // step2
//     console.log(stepDirection);
//     if (currentIndex === 0) {
//       if (stepDirection === 'forward') {
//         return frmMobile.valid();
//
//       }
//       if (stepDirection === 'backward') {
//         frmMobile.resetForm();
//       }
//     }
//     // step4
//     if (currentIndex === 3) {
//       if (stepDirection === 'forward') {
//         return frmLogin.valid();
//       }
//       if (stepDirection === 'backward') {
//         frmLoginValidator.resetForm();
//       }
//     }
//     // step5
//     if (currentIndex === 4) {
//       if (stepDirection === 'forward') {
//         return frmMobile.valid();
//       }
//       if (stepDirection === 'backward') {
//         frmMobileValidator.resetForm();
//       }
//     }
//     return true;
//   },
//     onFinish: function () { $('#main_button').click(); }
// });
//
