function showOrHide(input, div) {
   input = document.getElementById(input);
   div = document.getElementById(div);
   if (input.checked) {div.style.display = "flex"}
   else {
     div.style.display = "none"
   };
 }



// $(function() {
//
//           $('#btn').on('click', function() {
//         var select_value = $('#id_class_transport').val();
//           $('#id_class_transport').val()=$('#btn').value()
//                 // use the value here
//     });
// });

function selectEdit(id) {
document.getElementById("id_class_transport").value = id;
}

// Инициализация календаря
// $('#id_time_from').datepicker({
//   minDate: new Date(),
//   keyboardNav: true,
//   autoClose: true,
//   navTitles: {
//         days: '<h6>Выберете дату отправления</h6> MM, yyyy'
//     },
// })

$(function() {
  const $datepicker = $('#id_time_from');
  var disabledDates = [0, 6];

  let datepicker = $datepicker.datepicker({
    minDate: new Date(),
    keyboardNav: true,
    autoClose: false,
    navTitles: {
          days: '<h6>Выберете дату отправления</h6> MM, yyyy'
      },
    classes: 'datepicker__calendar',
    position: 'bottom left',
    offset: 22,

  }).data('datepicker');

});



// выделение класса трансфера
$('.choose_car').on('click', function(){
  $(this).addClass('activeCar').siblings().removeClass('activeCar');
  $('.finish-info-class_transport').text($("#id_class_transport option:selected").text());
});

$('.finish-info-from_transfer').text($("#id_from_transfer").text());

// Информация на правой панели
$('#id_passenger').bind('blur focus change click keyup keydown', function () {
  $('.finish-info-from_transfer').text($("#id_from_transfer").text());
})

$('#id_class_transport').change(function () {
  $('.finish-info-class_transport').text($(this).val(text))
})

$('#id_name').keyup(function () {
  $('.finish-info-name').text($(this).val())
})

$('#id_email').keyup(function () {
  $('.finish-info-email').text($(this).val())
})

$('#id_phone').keyup(function () {
  $('.finish-info-phone').text($(this).val())
})

// https://ru.stackoverflow.com/questions/812614/%D0%9A%D0%B0%D0%BA%D0%BE%D0%B5-%D1%81%D0%BE%D0%B1%D1%8B%D1%82%D0%B8%D0%B5-%D0%BF%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%BD%D0%BE-%D0%BC%D0%BE%D0%BD%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D1%82-input-%D0%BD%D0%B5%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D0%BE-%D0%BE%D1%82-%D1%84%D0%BE%D0%BA%D1%83%D1%81%D0%B0-%D0%B2-%D0%BD%D0%B5%D0%BC
var textFromTransfer = document.getElementById("id_from_transfer");
var demo = demo || document.getElementById("demo")
function doOnChange() {
  demo.innerHTML = "on Change: " + myInput.value;
}
// $('#id_from_transfer').keyup(function onchange() {
//   console.log($(this).val())
//   $('.finish-info-from_transfer').text($(this).val())
// })
//
// document.getElementById('#finish-info-from_transfer').value = document.getElementById('id_from_transfer_lng').value;
//
// document.getElementById('#id_from_transfer').onchange = function(){
//   var text =document.getElementById('id_from_transfer_lng').value;
//   console.log(text);
//   document.getElementById('#finish-info-from_transfer').value = text;
// }

$('#num-pass').change(function () {
  $('.pass').text($(this).val())
})

$('#num-child').change(function () {
  $('.chd').text($(this).val())
})
