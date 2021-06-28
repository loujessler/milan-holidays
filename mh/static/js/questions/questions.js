function selectEdit(id) {
  var el = document.getElementById('config-btn-'+id);
  el.style.display === 'none' ? el.style.display = 'initial' : el.style.display = 'none';
  var el = document.getElementById('config-btn1-'+id);
  el.style.display === 'none' ? el.style.display = 'initial' : el.style.display = 'none';
  var el = document.getElementById('config-btn2-'+id);
  el.style.display === 'none' ? el.style.display = 'initial' : el.style.display = 'none';
}
