/* =========================================
                Preloader
============================================ */
$(window).on("load", function () {
  // makes sure that whole site is loaded
  $("#status").fadeOut();
  $("#preloader").delay(350).fadeOut("slow");
});

/* =========================================
                Team
============================================ */
// $(function(){ }) is short for $(document).ready(function(){ })
$(function () {
  $("#team-members").owlCarousel({
    items: 2,
    autoplay: true,
    smartSpeed: 700,
    loop: true,
    autoplayHoverPause: true,
    nav: true,
    dots: false,
    // 这两个元素是向左向右箭头，是自定义的nav内容
    navText: [
      '<i class="fa fa-angle-left"></i>',
      '<i class="fa fa-angle-right"></i>',
    ],
    responsive: {
      // breakpoint from 0 up
      0: {
        items: 1,
      },
      // breakpoint from 480 up
      480: {
        items: 2,
      },
    },
  });
});

/* =========================================
                Progress Bars
============================================ */
$(function () {
  // progress-elements is for find the scroll postion for these progress-bars
  // way point means when you reach this area the following function will work
  $("#progress-elements").waypoint(
    function () {
      $(".progress-bar").each(function () {
        $(this).animate(
          {
            width: $(this).attr("aria-valuenow") + "%",
          },
          2000
        );
      });

      //   prevent the waypoint plugin to perform its action again
      this.destroy();
    },
    {
      // when the progree-bar is in the bottom of the window the waypoint will act
      offset: "bottom-in-view",
    }
  );
});

/* =========================================
               Responsive Tabs
============================================ */
// 达成效果：点击链接，跳转到相应id，规定格式参考 https://github.com/jellekralt/Responsive-Tabs
// 不需要一定是ID=services-tabs，可以自定义名称
$(function () {
  $("#services-tabs").responsiveTabs({
    // 切换效果
    animation: "slide",
  });
});

/* =========================================
               Portfolio
============================================ */
$(window).on("load", function () {
  // Initialize Isotope
  $("#isotope-container").isotope({});

  // filter items on button click
  $("#isotope-filters").on("click", "button", function () {
    // get filter value
    var filterValue = $(this).attr("data-filter");

    // filter portfolio
    $("#isotope-container").isotope({
      filter: filterValue,
    });

    // active button
    $("#isotope-filters").find(".active").removeClass("active");
    $(this).addClass("active");
  });
});
/* =========================================
               Magnifier
============================================ */
$(function () {
  $("#portfolio-wrapper").magnificPopup({
    delegate: "a", // child items selector, by clicking on it popup will open
    type: "image",
    gallery: {
      enabled: true,
    },
  });
});

/* =========================================
               Testimonials
============================================ */
$(function () {
  $("#testimonial-slider").owlCarousel({
    items: 1,
    autoplay: false,
    smartSpeed: 700,
    loop: true,
    autoplayHoverPause: true,
    nav: true,
    dots: false,
    navText: [
      '<i class="fa fa-angle-left"></i>',
      '<i class="fa fa-angle-right"></i>',
    ],
  });
});

/* =========================================
              Stats
============================================ */
$(function () {
  $(".counter").counterUp({
    delay: 10,
    time: 2000,
  });
});

/* =========================================
              Clients
============================================ */
$(function () {
  $("#clients-list").owlCarousel({
    items: 6,
    autoplay: false,
    smartSpeed: 700,
    loop: true,
    autoplayHoverPause: true,
    nav: true,
    dots: false,
    navText: [
      '<i class="fa fa-angle-left"></i>',
      '<i class="fa fa-angle-right"></i>',
    ],
    responsive: {
      // breakpoint from 0 up
      0: {
        items: 2,
      },
      // breakpoint from 480 up
      480: {
        items: 3,
      },
      // breakpoint from 768 up
      768: {
        items: 6,
      },
    },
  });
});

/* =========================================
              Google Map
============================================ */
$(window).on("load", function () {
  // Map Variables
  var addressString = "230 Broadway, NY, New York 10007, USA";
  var myLatlng = {
    lat: 40.712685,
    lng: -74.00592,
  };

  // 1. Render Map
  var map = new google.maps.Map(document.getElementById("map"), {
    zoom: 11,
    center: myLatlng,
  });

  // 2. Add Marker
  var marker = new google.maps.Marker({
    position: myLatlng,
    map: map,
    title: "Click To See Address",
  });

  // 3. Add Info Window
  var infowindow = new google.maps.InfoWindow({
    content: addressString,
  });

  // Show info window when user clicks marker
  marker.addListener("click", function () {
    infowindow.open(map, marker);
  });

  // 4. Resize Function
  google.maps.event.addDomListener(window, "resize", function () {
    var center = map.getCenter();
    google.maps.event.trigger(map, "resize");
    map.setCenter(center);
  });
});

/* =========================================
              Navigation
============================================ */

/* Show & Hide White Navigation */
$(function () {
  // show/hide nav on page load
  showHideNav();

  $(window).scroll(function () {
    // show/hide nav on window's scroll
    showHideNav();
  });

  function showHideNav() {
    if ($(window).scrollTop() > 50) {
      // Show white nav
      $("nav").addClass("white-nav-top");

      // Show dark logo
      $(".navbar-brand img").attr("src", "img/logo/logo-dark.png");

      // Show back to top button
      $("#back-to-top").fadeIn();
    } else {
      // Hide white nav
      $("nav").removeClass("white-nav-top");

      // Show logo
      $(".navbar-brand img").attr("src", "img/logo/logo.png");

      // Hide back to top button
      $("#back-to-top").fadeOut();
    }
  }
});

// 点击navbar中的link，‘顺滑地’划到相应section
// Smooth Scrolling
$(function () {
  $("a.smooth-scroll").click(function (event) {
    // 阻止 link 元素的默认操作：the link open the url
    event.preventDefault();

    // get section id like #about, #servcies, #work, #team and etc.
    var section_id = $(this).attr("href");

    // animate() 方法是 jQuery 这个 JavaScript 库中的一个方法。
    // $("html, body").animate({
    //   scrollTop: 200  // 滚动到页面顶部的距离为200像素
    // }, 1000); // 在1秒内执行动画

    $("html, body").animate(
      {
        scrollTop: $(section_id).offset().top - 64,
      },
      1250,
      "easeInOutExpo"
    );
  });
});

/* =========================================
              Mobile Menu
============================================ */
$(function () {
  // Show mobile nav
  // 点击 open button，打开 mobile nav
  $("#mobile-nav-open-btn").click(function () {
    $("#mobile-nav").css("height", "100%");
  });

  // Hide mobile nav
  // 点击 close button 或者 mobile nav中任何一个link，关闭mobile nav
  $("#mobile-nav-close-btn, #mobile-nav a").click(function () {
    $("#mobile-nav").css("height", "0%");
  });
});

/* =========================================
                Animation
============================================ */
// animate on scroll
$(function () {
  new WOW().init();
});

// 如果不写下述的内容，直接将animated fadeInDown这个类，添加给#home-heading-1，动画效果不会被展示
// 因为 page 被 load，需要一个时间（在load之前有一个preloader），动画效果与preloader的时间重合，就看不到动画效果了
// 需要在已经load之后，再添加动画类
// home animation on page load
$(window).on("load", function () {
  $("#home-heading-1").addClass("animated fadeInDown");
  $("#home-heading-2").addClass("animated fadeInLeft");
  $("#home-text").addClass("animated zoomIn");
  $("#home-btn").addClass("animated zoomIn");
  $("#arrow-down i").addClass("animated fadeInDown infinite");
});
