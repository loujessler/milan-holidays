$('.owl-carousel').owlCarousel({
  loop: true,
  margin: 30,
  dots: true,
  nav: true,
  responsiveClass: true,
  responsive: {
    0: {
      items: 1,
      margin: 10,
      stagePadding: 20,
    },
    600: {
      items: 3,
      margin: 20,
      stagePadding: 40,
    },
    1000: {
      items: 4,
      margin: 20,
      stagePadding: 40,
    }
  }
});
