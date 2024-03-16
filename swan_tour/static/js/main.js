!(function () {
  "use strict";
  (window.App = {}),
    (App.html = document.querySelector("html")),
    (App.body = document.querySelector("body")),
    (App.SMcontroller = new ScrollMagic.Controller()),
    (window.onload = function () {
      document.fonts.ready.then(function () {
        !(function () {
          const e = document.querySelector(".js-preloader");
          if (!e) return;
          setTimeout(() => {
            e.classList.add("-is-hidden"), s.init();
          }, 300);
        })(),
          document.querySelector(".js-lazy") &&
            new LazyLoad({ elements_selector: ".js-lazy" }),
          t.init(),
          n.init(),
          (function () {
            const e = document.querySelectorAll(".js-section-slider");
            if (e.length)
              for (let t = 0; t < e.length; t++) {
                const n = e[t];
                let s = n.querySelector(".js-prev"),
                  i = n.querySelector(".js-next");
                n.getAttribute("data-nav-prev") &&
                  (s = document.querySelector(
                    `.${n.getAttribute("data-nav-prev")}`
                  )),
                  n.getAttribute("data-nav-next") &&
                    (i = document.querySelector(
                      `.${n.getAttribute("data-nav-next")}`
                    ));
                let r = 0,
                  l = !1,
                  o = !1,
                  c = !1,
                  a = !1;
                if (
                  (n.getAttribute("data-gap") &&
                    (r = n.getAttribute("data-gap")),
                  n.hasAttribute("data-loop") && (l = !0),
                  n.hasAttribute("data-center") && (o = !0),
                  n.getAttribute("data-pagination"))
                ) {
                  let e = document.querySelector(
                    `.${n.getAttribute("data-pagination")}`
                  );
                  c = {
                    el: e,
                    bulletClass: "pagination__item",
                    bulletActiveClass: "is-active",
                    bulletElement: "div",
                    clickable: !0,
                  };
                }
                n.hasAttribute("data-scrollbar") &&
                  (a = { el: ".js-scrollbar", draggable: !0 });
                const d = n.getAttribute("data-slider-cols").split(" ");
                let u = 1,
                  p = 1,
                  v = 1,
                  g = 1,
                  m = 1;
                d.forEach((e) => {
                  e.includes("base") && (u = e.slice(-1)),
                    e.includes("xl") && (p = e.slice(-1)),
                    e.includes("lg") && (v = e.slice(-1)),
                    e.includes("md") && (g = e.slice(-1)),
                    e.includes("sm") && (m = e.slice(-1));
                }),
                  new Swiper(n, {
                    speed: 600,
                    autoHeight: !0,
                    centeredSlides: o,
                    parallax: !0,
                    watchSlidesVisibility: !0,
                    loop: l,
                    loopAdditionalSlides: 1,
                    preloadImages: !1,
                    lazy: !0,
                    width: 250,
                    scrollbar: a,
                    pagination: c,
                    spaceBetween: 10,
                    slidesPerView: parseInt(u),
                    breakpoints: {
                      1199: {
                        slidesPerView: parseInt(p),
                        width: null,
                        spaceBetween: parseInt(r),
                      },
                      991: {
                        slidesPerView: parseInt(v),
                        width: null,
                        spaceBetween: parseInt(r),
                      },
                      767: {
                        slidesPerView: parseInt(g),
                        width: null,
                        spaceBetween: parseInt(r),
                      },
                      574: {
                        slidesPerView: parseInt(m),
                        width: null,
                        spaceBetween: parseInt(r),
                      },
                    },
                    lazy: { loadPrevNext: !0 },
                    navigation: { prevEl: s, nextEl: i },
                  });
              }
          })(),
          i.init(".js-select"),
          document.querySelector("[data-parallax]") &&
            document.querySelectorAll("[data-parallax]").forEach((e) => {
              jarallax(e, {
                speed: e.getAttribute("data-parallax"),
                imgElement: "[data-parallax-target]",
              });
            }),
          r.init(),
          r.ddInit(),
          l.init(),
          l.headerSticky(),
          (function () {
            const e = new Swiper(".js-testimonials-slider", {
                speed: 700,
                loop: !0,
                lazy: { loadPrevNext: !0 },
              }),
              t = document.querySelectorAll(
                ".js-testimonials-slider .js-testimonials-pagination > * > *"
              );
            t.forEach((t, n) => {
              t.addEventListener("click", () => {
                document
                  .querySelector(
                    ".js-testimonials-slider .js-testimonials-pagination .is-active"
                  )
                  .classList.remove("is-active"),
                  t.classList.add("is-active"),
                  e.slideTo(n + 1);
              });
            }),
              e.on("slideChangeTransitionEnd", () => {
                document
                  .querySelector(
                    ".js-testimonials-slider .js-testimonials-pagination .is-active"
                  )
                  .classList.remove("is-active"),
                  t[e.realIndex].classList.add("is-active");
              });
          })(),
          new Swiper(".js-testimonials-slider-2", {
            speed: 800,
            effect: "cards",
            cardsEffect: { slideShadows: !0 },
            grabCursor: !0,
            lazy: { loadPrevNext: !0 },
            navigation: { prevEl: ".js-prev", nextEl: ".js-next" },
            pagination: {
              el: ".js-pagination",
              bulletClass: "pagination__item",
              bulletActiveClass: "is-active",
              bulletElement: "div",
              clickable: !0,
            },
          }),
          new Swiper(".js-cardImage-slider", {
            speed: 400,
            loop: !0,
            lazy: { loadPrevNext: !0 },
            navigation: { prevEl: ".js-prev", nextEl: ".js-next" },
            pagination: {
              el: ".js-pagination",
              bulletClass: "pagination__item",
              bulletActiveClass: "is-active",
              bulletElement: "div",
              clickable: !0,
            },
          }),
          new Swiper(".js-masthead-slider-4", {
            speed: 600,
            navigation: { prevEl: ".js-prev", nextEl: ".js-next" },
          }),
          new Swiper(".js-masthead-slider-7", {
            speed: 600,
            loop: !0,
            lazy: { loadPrevNext: !0 },
            navigation: { prevEl: ".js-prev", nextEl: ".js-next" },
          }),
          new Swiper(".js-masthead-slider-8", {
            speed: 600,
            loop: !0,
            lazy: { loadPrevNext: !0 },
            navigation: { prevEl: ".js-prev", nextEl: ".js-next" },
          }),
          (function () {
            const e = document.querySelectorAll(".js-dropdown");
            e &&
              e.forEach((e) => {
                const t = e.querySelectorAll(
                    ".js-dropdown-list .js-dropdown-link"
                  ),
                  n = e.querySelector(".js-dropdown-title");
                t.forEach((e) => {
                  e.addEventListener("click", (t) => {
                    t.preventDefault(), (n.innerHTML = e.innerHTML);
                    const s = document.querySelectorAll(
                      ".js-click-dropdown.-is-el-visible"
                    );
                    s &&
                      s.forEach((e) => {
                        e.classList.remove("-is-el-visible");
                      });
                    const i = document.querySelectorAll(".-is-dd-active");
                    i && i.forEach((e) => e.classList.remove("-is-dd-active"));
                  });
                });
              });
          })(),
          (function () {
            const e = document.querySelectorAll("[data-el-toggle]");
            e &&
              e.forEach((e) => {
                const t = e.getAttribute("data-el-toggle"),
                  n = document.querySelector(t),
                  s = e.getAttribute("data-el-toggle-active"),
                  i = document.querySelector(s);
                e.addEventListener("click", () => {
                  const e = document.querySelectorAll(
                    ".js-click-dropdown.-is-el-visible"
                  );
                  e && e.forEach((e) => e.classList.remove("-is-el-visible"));
                  const t = document.querySelectorAll(".-is-dd-active");
                  t && t.forEach((e) => e.classList.remove("-is-dd-active")),
                    n.classList.toggle("-is-el-visible"),
                    i && i.classList.toggle("-is-dd-active");
                });
              });
          })(),
          (function () {
            const e = new Swiper(".js-cars-slider", {
                speed: 600,
                lazy: { loadPrevNext: !0 },
              }),
              t = document.querySelectorAll(".js-cars-slides > *");
            t.forEach((t, n) => {
              t.addEventListener("click", () => {
                document
                  .querySelector(".js-cars-slides .-is-active")
                  .classList.remove("-is-active"),
                  t.classList.add("-is-active"),
                  e.slideTo(n);
              });
            }),
              e.on("slideChangeTransitionEnd", () => {
                document
                  .querySelector(".js-cars-slides .-is-active")
                  .classList.remove("-is-active"),
                  t[e.realIndex].classList.add("-is-active");
              });
          })(),
          (function () {
            const e = new Swiper(".js-cruise-slider", {
                speed: 600,
                navigation: { prevEl: ".js-prev", nextEl: ".js-next" },
              }),
              t = document.querySelectorAll(".js-cruise-slides .js-item");
            t.forEach((t, n) => {
              t.addEventListener("click", () => {
                document
                  .querySelector(".js-cruise-slides .-is-active")
                  .classList.remove("-is-active"),
                  t.classList.add("-is-active"),
                  e.slideTo(n);
              });
            }),
              e.on("slideChangeTransitionEnd", () => {
                document
                  .querySelector(".js-cruise-slides .-is-active")
                  .classList.remove("-is-active"),
                  t[e.realIndex].classList.add("-is-active");
              });
          })(),
          (function () {
            const e = document.querySelector(".js-singleMenu");
            e &&
              new ScrollMagic.Scene({ offset: "250px" })
                .setClassToggle(e, "-is-active")
                .addTo(App.SMcontroller);
          })(),
          (function () {
            const e = document.querySelectorAll(".js-calendar");
            function t(e) {
              return parseInt(e.getAttribute("data-index"));
            }
            e &&
              e.forEach((e) => {
                const n = e.querySelectorAll(".table-calendar__grid > *"),
                  s = e.querySelector(".js-first-date"),
                  i = e.querySelector(".js-last-date");
                let r = !1,
                  l = !1,
                  o = !1;
                n.forEach((n, c) => {
                  n.addEventListener("click", () => {
                    if (
                      (n.classList.add("-is-active"),
                      l && t(l) > t(n) && ((o = l), (l = n)),
                      l && !o && (o = n),
                      l || (l = n),
                      r)
                    ) {
                      (l = !1), (o = !1);
                      const t = e.querySelectorAll(".-is-active");
                      t.forEach((e) => {
                        e.classList.remove("-is-active");
                      });
                      const n = e.querySelectorAll(".-is-in-path");
                      n.forEach((e) => {
                        e.classList.remove("-is-in-path");
                      }),
                        (r = !1);
                    } else if (l && o) {
                      const n = Math.abs(t(l) - t(o));
                      for (let s = 1; s < n; s++) {
                        const n = e.querySelector(`[data-index="${t(l) + s}"]`);
                        n.classList.add("-is-in-path");
                      }
                      (s.innerHTML = `${l.getAttribute("data-week")} ${
                        l.querySelector(".js-date").innerHTML
                      } ${l.getAttribute("data-month")}`),
                        (i.innerHTML = `${o.getAttribute("data-week")} ${
                          o.querySelector(".js-date").innerHTML
                        } ${o.getAttribute("data-month")}`),
                        (r = !0);
                    }
                  });
                });
              });
          })(),
          (function () {
            const e = new Swiper(".js-testimonials-slider-3", {
              speed: 800,
              cardsEffect: { slideShadows: !0 },
              grabCursor: !0,
              lazy: { loadPrevNext: !0 },
              scrollbar: { el: ".js-scrollbar", draggable: !0 },
            });
            if (document.querySelector(".js-testimonials-slider-3")) {
              const t = document.querySelector(".js-testimonials-slider-pag"),
                n = t.querySelector(".js-current"),
                s = t.querySelector(".js-all");
              (s.innerHTML = `0${e.slides.length}`),
                e.on(
                  "slideChangeTransitionEnd",
                  () => (n.innerHTML = `0${e.realIndex + 1}`)
                );
            }
          })(),
          new Swiper(".js-calendar-slider", {
            speed: 600,
            autoHeight: !0,
            gap: 60,
            slidesPerView: 1,
            breakpoints: { 991: { slidesPerView: 2 } },
            navigation: {
              prevEl: ".js-calendar-prev",
              nextEl: ".js-calendar-next",
            },
          }),
          new Swiper(".js-masthead-slider-9", {
            speed: 600,
            loop: !0,
            lazy: { loadPrevNext: !0 },
            navigation: { prevEl: ".js-prev", nextEl: ".js-next" },
          }),
          GLightbox({
            selector: ".js-gallery",
            touchNavigation: !0,
            loop: !1,
            autoplayVideos: !0,
          }),
          (function () {
            const e = document.querySelectorAll(".js-pin-container");
            e &&
              e.forEach((e) => {
                let t;
                (t = e
                  .querySelector(".js-pin-content")
                  .getAttribute("data-offset")
                  ? e
                      .querySelector(".js-pin-content")
                      .getAttribute("data-offset")
                  : 300),
                  console.log(t);
                const n = e.offsetHeight + parseInt(t),
                  s =
                    e.querySelector(".js-pin-content").offsetHeight +
                    parseInt(t),
                  i = new ScrollMagic.Scene({
                    duration: n - s,
                    offset: s,
                    triggerElement: e,
                    triggerHook: "onEnter",
                  })
                    .setPin(".js-pin-content")
                    .addTo(App.SMcontroller);
                let r =
                  window.innerWidth > 0 ? window.innerWidth : screen.width;
                r < 992
                  ? (i.duration("1px"), i.refresh())
                  : (i.duration(n - s), i.refresh()),
                  window.addEventListener("resize", () => {
                    let e =
                      window.innerWidth > 0 ? window.innerWidth : screen.width;
                    e < 992
                      ? (i.duration("1px"), i.refresh())
                      : (i.duration(n - s), i.refresh());
                  });
              });
          })(),
          (function () {
            const e = document.getElementById("lineChart");
            e &&
              new Chart(e, {
                type: "line",
                data: {
                  labels: [
                    "Jan",
                    "Feb",
                    "Marc",
                    "April",
                    "May",
                    "Jun",
                    "July",
                    "Agust",
                    "Sept",
                    "Oct",
                    "Now",
                    "Dec",
                  ],
                  datasets: [
                    {
                      label: "#",
                      data: [
                        148, 100, 205, 110, 165, 145, 180, 156, 148, 220, 180,
                        245,
                      ],
                      tension: 0.4,
                      backgroundColor: "#336CFB",
                      borderColor: "#336CFB",
                      borderWidth: 2,
                    },
                  ],
                },
                options: {
                  responsive: !0,
                  plugins: { legend: { display: !1 } },
                  scales: { y: { min: 0, max: 300, ticks: { stepSize: 50 } } },
                },
              });
          })(),
          document.querySelectorAll(".js-mouse-move-container").forEach((e) => {
            const t = e,
              n = e.querySelectorAll(".js-mouse-move");
            n.forEach((e) => {
              const n = e.getAttribute("data-move");
              document.addEventListener("mousemove", (s) => {
                const i = s.pageX - t.offsetLeft,
                  r = s.pageY - t.offsetTop;
                gsap.to(e, {
                  x: ((i - t.offsetWidth / 2) / t.offsetWidth) * n,
                  y: ((r - t.offsetHeight / 2) / t.offsetHeight) * n,
                  duration: 0.2,
                });
              });
            });
          }),
          document.querySelectorAll(".js-time-rangeSlider").forEach((e) => {
            const t = e.querySelector(".js-slider");
            noUiSlider.create(t, {
              start: [6, 11.5],
              step: 0.5,
              connect: !0,
              range: { min: 1, max: 12 },
              format: {
                to: function (e) {
                  const t = e.toString();
                  let n;
                  return (
                    (n = t.includes(".5")
                      ? t.substr(0, t.indexOf(".")) + ":30"
                      : parseInt(t).toFixed(0) + ":00"),
                    t.substr(0, 2) > 9 ? (n += " PM") : (n += " AM"),
                    n
                  );
                },
                from: function (e) {
                  return e;
                },
              },
            });
            const n = [
              e.querySelector(".js-lower"),
              e.querySelector(".js-upper"),
            ];
            t.noUiSlider.on("update", function (e, t) {
              n[t].innerHTML = e[t];
            });
          }),
          document.querySelectorAll(".js-price-rangeSlider").forEach((e) => {
            const t = e.querySelector(".js-slider");
            noUiSlider.create(t, {
              start: [0, 500],
              step: 100,
              connect: !0,
              range: { min: 0, max: 2e3 },
              format: {
                to: function (e) {
                  return "$" + e;
                },
                from: function (e) {
                  return e;
                },
              },
            });
            const n = [
              e.querySelector(".js-lower"),
              e.querySelector(".js-upper"),
            ];
            t.noUiSlider.on("update", function (e, t) {
              n[t].innerHTML = e[t];
            });
          }),
          (function () {
            const e = document.querySelectorAll(".js-form-counters");
            e &&
              e.forEach((e) => {
                const t = e.querySelectorAll(".js-counter");
                t.forEach((t) => {
                  const n = t.querySelector(".js-count"),
                    s = t.querySelector(".js-down"),
                    i = t.querySelector(".js-up");
                  s.addEventListener("click", () => {
                    0 != n.innerHTML &&
                      ((n.innerHTML = parseInt(n.innerHTML) - 1),
                      t.getAttribute("data-value-change") &&
                        (e.querySelector(
                          t.getAttribute("data-value-change")
                        ).innerHTML = parseInt(n.innerHTML)));
                  }),
                    i.addEventListener("click", () => {
                      (n.innerHTML = parseInt(n.innerHTML) + 1),
                        t.getAttribute("data-value-change") &&
                          (e.querySelector(
                            t.getAttribute("data-value-change")
                          ).innerHTML = parseInt(n.innerHTML));
                    });
                });
              });
          })(),
          (function () {
            const e = document.querySelectorAll(".js-liverSearch");
            if (!e) return;
            const t = [
              { city: "London", country: "Greater London, United Kingdom" },
              { city: "New York", country: "New York State, United States" },
              { city: "Paris", country: "France" },
              { city: "Madrid", country: "Spain" },
              { city: "Santorini", country: "Greece" },
            ];
            e.forEach((e) => {
              const t = e.querySelector(".js-search"),
                s = e.querySelector(".js-results");
              let i = "";
              s.querySelectorAll(".js-search-option").forEach((n) => {
                const s = n.querySelector(".js-search-option-target").innerHTML;
                n.addEventListener("click", () => {
                  (t.value = s),
                    e
                      .querySelector(".js-popup-window")
                      .classList.remove("-is-active");
                });
              }),
                t.addEventListener("input", (r) => {
                  (i = r.target.value.toLowerCase()),
                    n(i, s),
                    s.querySelectorAll(".js-search-option").forEach((n) => {
                      const s = n.querySelector(
                        ".js-search-option-target"
                      ).innerHTML;
                      n.addEventListener("click", () => {
                        (t.value = s),
                          e
                            .querySelector(".js-popup-window")
                            .classList.remove("-is-active");
                      });
                    });
                });
            });
            const n = (e, n) => {
              (n.innerHTML = ""),
                t
                  .filter((t) => t.city.toLowerCase().includes(e))
                  .forEach((e) => {
                    const t = document.createElement("div");
                    (t.innerHTML = `\n          <button class="-link d-block col-12 text-left rounded-4 px-20 py-15 js-search-option">\n            <div class="d-flex">\n              <div class="icon-location-2 text-light-1 text-20 pt-4"></div>\n              <div class="ml-10">\n                <div class="text-15 lh-12 fw-500 js-search-option-target">${e.city}</div>\n                <div class="text-14 lh-12 text-light-1 mt-5">${e.country}</div>\n              </div>\n            </div>\n          </button>\n        `),
                      n.appendChild(t);
                  });
            };
          })(),
          (function () {
            if (!document.querySelector(".js-map")) return;
            const t = new google.maps.Map(document.querySelector(".js-map"), {
                zoom: 12,
                center: { lat: 40.69, lng: -73.88 },
              }),
              n = [
                { lat: 40.80061, lng: -74.035242 },
                { lat: 40.73061, lng: -73.935242 },
                { lat: 40.74061, lng: -73.825242 },
                { lat: 40.70061, lng: -73.885242 },
                { lat: 40.67061, lng: -73.785242 },
                { lat: 40.68061, lng: -73.905242 },
              ].map((n) => {
                const s = new e({
                    latlng: n,
                    map: t,
                    html: '\n        <div class="mapMarker bg-white rounded-100 border-dark-1 px-20 py-10">\n          <div class="text-14 fw-500">US$72</div>\n        </div>\n      ',
                  }),
                  i = new google.maps.InfoWindow({
                    content:
                      '\n    <div class="mapItem d-flex">\n      <img src="img/lists/hotel/1/1.png" alt="image" class="mapItem__img size-100 rounded-4">\n\n      <div class="mapItem__content d-flex flex-column justify-between ml-15">\n        <div>\n          <div class="fw-500">Great Northern Hotel, a Tribute</div>\n          <div class="d-flex items-center mt-10">\n            <i class="icon-star text-yellow-1 text-10"></i>\n            <i class="icon-star text-yellow-1 text-10 ml-4"></i>\n            <i class="icon-star text-yellow-1 text-10 ml-4"></i>\n            <i class="icon-star text-yellow-1 text-10 ml-4"></i>\n            <i class="icon-star text-yellow-1 text-10 ml-4"></i>\n          </div>\n        </div>\n\n        <div class="d-flex items-center">\n          <div class="d-flex items-center">\n            <div class="size-30 flex-center rounded-4 bg-blue-1 text-white">\n              <div class="text-12 fw-600">4.8</div>\n            </div>\n\n            <div class="text-14 fw-500 ml-10">Exceptional</div>\n          </div>\n\n          <div class="text-14 text-light-1 ml-10">3,014 reviews</div>\n        </div>\n      </div>\n    </div>\n  ',
                  });
                return (
                  google.maps.event.addListener(t, "click", function () {
                    i.close();
                  }),
                  s.addListener("click", () => {
                    setTimeout(() => {
                      i.open({ anchor: s, map: t, shouldFocus: !1 });
                    }, 50);
                  }),
                  s
                );
              });
            new markerClusterer.MarkerClusterer({ map: t, markers: n });
          })(),
          (function () {
            if (!document.querySelector(".js-map-places")) return;
            const t = new google.maps.Map(
                document.querySelector(".js-map-places"),
                { zoom: 10, center: { lat: 40.8, lng: -74.02 } }
              ),
              n = [
                { lat: 40.80061, lng: -74.035242 },
                { lat: 41.00061, lng: -74.135242 },
                { lat: 40.70061, lng: -73.835242 },
              ].map((n) => {
                const s = new e({
                    latlng: n,
                    map: t,
                    html: '\n        <div class="mapMarker flex-center bg-white rounded-100 border-dark-1 size-40">\n          <div class="text-14 fw-500">3</div>\n        </div>\n      ',
                  }),
                  i = new google.maps.InfoWindow({
                    content:
                      '\n    <div class="d-flex">\n      <div class="px-5 py-5">\n        <div class="text-16 fw-500">The Roman Baths</div>\n      </div>\n    </div>\n  ',
                  });
                return (
                  google.maps.event.addListener(t, "click", function () {
                    i.close();
                  }),
                  s.addListener("click", () => {
                    setTimeout(() => {
                      i.open({ anchor: s, map: t, shouldFocus: !1 });
                    }, 50);
                  }),
                  s
                );
              });
            new markerClusterer.MarkerClusterer({ map: t, markers: n });
          })(),
          (function () {
            if (!document.querySelector(".js-map-single")) return;
            const t = new google.maps.Map(
                document.querySelector(".js-map-single"),
                { zoom: 12, center: { lat: 40.8, lng: -74.02 } }
              ),
              n = [{ lat: 40.80061, lng: -74.035242 }].map((n) => {
                const s = new e({
                  latlng: n,
                  map: t,
                  html: '\n        <div class="mapMarker flex-center bg-white rounded-100 bg-dark-1 size-40">\n          <svg width="20" height="20" viewBox="0 0 20 20" fill="none" xmlns="http://www.w3.org/2000/svg">\n            <g clip-path="url(#clip0_238_16072)">\n            <path d="M10.0003 9.58022C11.8081 9.58022 13.2789 8.10963 13.2789 6.30205C13.2789 4.49447 11.8081 3.02393 10.0003 3.02393C8.19246 3.02393 6.72168 4.49447 6.72168 6.30205C6.72168 8.10963 8.19246 9.58022 10.0003 9.58022ZM10.0003 4.19565C11.1619 4.19565 12.107 5.14061 12.107 6.30205C12.107 7.46354 11.162 8.4085 10.0003 8.4085C8.83859 8.4085 7.89355 7.46354 7.89355 6.30205C7.89355 5.14061 8.83863 4.19565 10.0003 4.19565Z" fill="white"/>\n            <path d="M6.43022 12.1926C7.31831 13.3948 6.96151 12.9273 9.51952 16.5795C9.75202 16.9127 10.2464 16.9143 10.4803 16.58C13.0498 12.9105 12.6963 13.3752 13.5699 12.1926C14.4549 10.9945 15.37 9.75555 15.8715 8.30375C16.5973 6.20215 16.2836 4.12273 14.9882 2.44852C14.9881 2.44852 14.9881 2.44848 14.9881 2.44848C13.8014 0.915312 11.9367 0 10.0001 0C8.06338 0 6.1987 0.915312 5.01201 2.44855C3.71658 4.12277 3.40283 6.20223 4.12869 8.30383C4.6301 9.75559 5.54526 10.9945 6.43022 12.1926ZM5.93881 3.16559C6.90514 1.91711 8.42338 1.17172 10.0001 1.17172C11.5767 1.17172 13.095 1.91711 14.0613 3.16559L14.0612 3.16555C15.1068 4.5168 15.3563 6.20578 14.7638 7.92133C14.3208 9.20367 13.4599 10.3693 12.6273 11.4965C11.979 12.3741 12.173 12.1057 10.0001 15.2204C7.8294 12.1088 8.02096 12.3738 7.37288 11.4965C6.54026 10.3693 5.67928 9.20363 5.23635 7.92133C4.64385 6.20574 4.8933 4.5168 5.93881 3.16559Z" fill="white"/>\n            <path d="M6.91156 14.7331C6.73875 14.4596 6.37687 14.3779 6.10328 14.5507L4.43726 15.6029C4.07382 15.8325 4.07347 16.3638 4.43726 16.5936L9.68726 19.9095C9.8784 20.0303 10.122 20.0302 10.3131 19.9095L15.5631 16.5936C15.9266 16.364 15.9269 15.8327 15.5631 15.6029L13.8971 14.5507C13.6234 14.3779 13.2616 14.4596 13.0888 14.7331C12.9159 15.0067 12.9977 15.3685 13.2713 15.5413L14.153 16.0983L10.0002 18.7212L5.8473 16.0983L6.7291 15.5413C7.00269 15.3686 7.08437 15.0067 6.91156 14.7331Z" fill="white"/>\n            </g>\n            <defs>\n            <clipPath id="clip0_238_16072">\n            <rect width="20" height="20" fill="white"/>\n            </clipPath>\n            </defs>\n          </svg>\n        </div>\n      ',
                });
                return s;
              });
            new markerClusterer.MarkerClusterer({ map: t, markers: n });
          })(),
          (function () {
            if (!document.querySelector(".js-langMenu")) return;
            const e = document.querySelector(".js-language-mainTitle"),
              t = document.querySelector(".js-langMenu");
            t.querySelectorAll(".js-item").forEach((n) => {
              const s = n.querySelector(".js-title");
              n.addEventListener("click", () => {
                t.querySelector(".-is-active") &&
                  (t
                    .querySelector(".-is-active")
                    .classList.remove("-is-active"),
                  console.log("some")),
                  n.classList.toggle("-is-active"),
                  (e.innerHTML = s.innerHTML);
              });
            });
          })(),
          (function () {
            if (!document.querySelector(".js-currencyMenu")) return;
            const e = document.querySelector(".js-currencyMenu-mainTitle"),
              t = document.querySelector(".js-currencyMenu");
            t.querySelectorAll(".js-item").forEach((n) => {
              const s = n.querySelector(".js-title");
              n.addEventListener("click", () => {
                t.querySelector(".-is-active") &&
                  (t
                    .querySelector(".-is-active")
                    .classList.remove("-is-active"),
                  console.log("some")),
                  n.classList.toggle("-is-active"),
                  (e.innerHTML = s.innerHTML);
              });
            });
          })();
      });
    }),
    (window.onclick = function (e) {
      if (
        (e.target.closest("[data-x-dd-click]") ||
          e.target.closest("[data-x-dd]") ||
          r.closeAllDropdowns(),
        !e.target.classList.contains("dropdown__button") &&
          !e.target.classList.contains("js-dropdown-title"))
      ) {
        const e = document.querySelectorAll(
          ".js-click-dropdown.-is-el-visible"
        );
        e &&
          e.forEach((e) => {
            e.classList.remove("-is-el-visible");
          });
        const t = document.querySelectorAll(".-is-dd-active");
        t && t.forEach((e) => e.classList.remove("-is-dd-active"));
      }
      if (!e.target.closest(".js-select")) {
        const e = document.querySelectorAll(".js-select");
        if (!e) return;
        e.forEach((e) => {
          e.querySelector(".-is-visible") &&
            e.querySelector(".-is-visible").classList.remove("-is-visible");
        });
      }
      if (!e.target.closest(".js-multiple-select")) {
        const e = document.querySelectorAll(".js-multiple-select");
        if (!e) return;
        e.forEach((e) => {
          e.querySelector(".-is-visible") &&
            e.querySelector(".-is-visible").classList.remove("-is-visible");
        });
      }
    });
  class e extends google.maps.OverlayView {
    constructor(e) {
      super(),
        (this.latlng = e.latlng),
        (this.html = e.html),
        this.setMap(e.map);
    }
    createDiv() {
      (this.div = document.createElement("div")),
        (this.div.style.position = "absolute"),
        this.html && (this.div.innerHTML = this.html),
        google.maps.event.addDomListener(this.div, "click", (e) => {
          google.maps.event.trigger(this, "click");
        });
    }
    appendDivToOverlay() {
      this.getPanes().overlayMouseTarget.appendChild(this.div);
    }
    positionDiv() {
      const e = this.getProjection().fromLatLngToDivPixel(this.latlng);
      e &&
        ((this.div.style.left = `${e.x}px`), (this.div.style.top = `${e.y}px`));
    }
    draw() {
      this.div || (this.createDiv(), this.appendDivToOverlay()),
        this.positionDiv();
    }
    remove() {
      this.div &&
        (this.div.parentNode.removeChild(this.div), (this.div = null));
    }
    getVisible() {
      return this.latlng;
    }
    getPosition() {
      return new google.maps.LatLng(this.latlng);
    }
    getDraggable() {
      return !1;
    }
  }
  const t = (function () {
      return {
        init: function () {
          const e = document.querySelectorAll(".js-accordion");
          if (e)
            for (let t = 0; t < e.length; t++) {
              const n = e[t].querySelectorAll(".accordion__item");
              for (let e = 0; e < n.length; e++) {
                const t = n[e].querySelector(".accordion__button"),
                  s = n[e].querySelector(".accordion__content"),
                  i = n[e].querySelector("[data-open-change-title]");
                let r, l;
                n[e].classList.contains("js-accordion-item-active") &&
                  (n[e].classList.toggle("is-active"),
                  (s.style.maxHeight = s.scrollHeight + "px")),
                  i &&
                    ((r = i.innerHTML),
                    (l = i.getAttribute("data-open-change-title"))),
                  t.addEventListener("click", (t) => {
                    n[e].classList.toggle("is-active"),
                      i &&
                        (n[e].classList.contains("is-active")
                          ? (i.innerHTML = l)
                          : (i.innerHTML = r)),
                      s.style.maxHeight
                        ? (s.style.maxHeight = null)
                        : (s.style.maxHeight = s.scrollHeight + "px");
                  });
              }
            }
        },
      };
    })(),
    n =
      ((function () {})(),
      (function () {
        return {
          init: function () {
            const e = document.querySelectorAll(".js-tabs");
            e &&
              e.forEach((e) => {
                !(function (e) {
                  const t = e.querySelector(".js-tabs-controls"),
                    n = e.querySelectorAll(".js-tabs-controls .js-tabs-button"),
                    s = e.querySelector(".js-tabs-content");
                  for (let e = 0; e < n.length; e++) {
                    const i = n[e];
                    i.addEventListener("click", (e) => {
                      const n = i.getAttribute("data-tab-target");
                      t
                        .querySelector(".is-tab-el-active")
                        .classList.remove("is-tab-el-active"),
                        s
                          .querySelector(".is-tab-el-active")
                          .classList.remove("is-tab-el-active"),
                        i.classList.add("is-tab-el-active"),
                        s.querySelector(n).classList.add("is-tab-el-active");
                    });
                  }
                })(e);
              });
          },
        };
      })()),
    s = (function () {
      function e(e) {
        let t, n, s;
        (t = e.getAttribute("data-anim")
          ? e.getAttribute("data-anim")
          : e.getAttribute("data-anim-child")).includes("delay-") &&
          (n = (s = t.split(" ").pop()).substr(s.indexOf("-") + 1) / 10),
          t.includes("counter")
            ? (function (e, t = 0) {
                const n = e.getAttribute("data-counter"),
                  s = e.getAttribute("data-counter-add"),
                  i = t;
                let r = "",
                  l = { count: 0 };
                const o = e.querySelector(".js-counter-num");
                s && (r = s);
                gsap.to(l, {
                  count: n,
                  delay: i,
                  duration: 1.8,
                  ease: "power3.inOut",
                  onUpdate: function () {
                    o.innerHTML = Math.round(l.count) + r;
                  },
                });
              })(e, n)
            : t.includes("line-chart")
            ? (function (e, t = 0) {
                const n = e.getAttribute("data-percent");
                gsap.fromTo(
                  e.querySelector(".js-bar"),
                  { scaleX: 0 },
                  {
                    delay: 0.45 + t,
                    duration: 1,
                    ease: "power3.inOut",
                    scaleX: n / 100,
                  }
                );
                let s = { count: 0 };
                const i = e.querySelector(".js-number");
                gsap.to(s, {
                  count: n,
                  delay: 0.45 + t,
                  duration: 1,
                  ease: "power3.inOut",
                  onUpdate: function () {
                    i.innerHTML = Math.round(s.count);
                  },
                });
              })(e, n)
            : t.includes("pie-chart")
            ? (function (e, t = 0) {
                const n = e.getAttribute("data-percent"),
                  s = e.querySelector(".js-chart-bar");
                n < 0 && (n = 0);
                n > 100 && (n = 100);
                gsap.fromTo(
                  s,
                  { drawSVG: "0%" },
                  {
                    delay: 0.3 + t,
                    duration: 1.4,
                    ease: "power3.inOut",
                    drawSVG: `${n}%`,
                    onStart: () => {
                      s.classList.remove("bar-stroke-hidden");
                    },
                  }
                );
                let i = { count: 0 };
                const r = e.querySelector(".js-chart-percent");
                gsap.to(i, {
                  count: n,
                  delay: 0.45 + t,
                  duration: 1,
                  ease: "power3.inOut",
                  onUpdate: function () {
                    r.innerHTML = Math.round(i.count) + "%";
                  },
                });
              })(e, n)
            : t.includes("split-lines")
            ? splitLines(e, n)
            : e.classList.add("is-in-view");
      }
      return {
        init: function () {
          !(function () {
            const t = document.querySelectorAll("[data-anim]");
            if (t.length)
              for (let n = 0; n < t.length; n++) {
                const s = t[n];
                new ScrollMagic.Scene({
                  offset: "350px",
                  triggerElement: s,
                  triggerHook: "onEnter",
                  reverse: !1,
                })
                  .on("enter", function (t) {
                    e(s);
                  })
                  .addTo(App.SMcontroller);
              }
          })(),
            (function () {
              const t = document.querySelectorAll("[data-anim-wrap]");
              if (t.length)
                for (let n = 0; n < t.length; n++) {
                  const s = t[n];
                  new ScrollMagic.Scene({
                    offset: "350px",
                    triggerElement: s,
                    triggerHook: "onEnter",
                    reverse: !1,
                  })
                    .on("enter", function (t) {
                      const n = s.querySelectorAll("[data-anim-child]");
                      s.classList.add("animated"), n.forEach((t) => e(t));
                    })
                    .addTo(App.SMcontroller);
                }
            })();
        },
      };
    })(),
    i = (function () {
      function e() {
        const e = document.querySelectorAll(".js-select, .js-multiple-select");
        e &&
          e.forEach((e) => {
            e.querySelector(".-is-visible") &&
              e.querySelector(".-is-visible").classList.remove("-is-visible");
          });
      }
      return {
        init: function (t) {
          document.querySelectorAll(t).forEach((t) =>
            (function (t) {
              const n = t.querySelector(".js-button"),
                s = n.querySelector(".js-button-title");
              t.classList.contains("js-liveSearch") &&
                (function (e) {
                  const t = e.querySelector(".js-search"),
                    n = e.querySelectorAll(".js-options > *");
                  t.addEventListener("input", (e) => {
                    let t = e.target.value.toLowerCase();
                    n.forEach((e) => {
                      e.classList.add("d-none"),
                        e.getAttribute("data-value").includes(t) &&
                          e.classList.remove("d-none");
                    });
                  });
                })(t),
                n.addEventListener("click", () => {
                  let n = t.querySelector(".js-dropdown");
                  n.classList.contains("-is-visible")
                    ? n.classList.remove("-is-visible")
                    : (e(), n.classList.add("-is-visible")),
                    t.classList.contains("js-liveSearch") &&
                      t.querySelector(".js-search").focus();
                });
              const i = t.querySelector(".js-dropdown");
              i.querySelectorAll(".js-options > *").forEach((e) => {
                e.addEventListener("click", () => {
                  (s.innerHTML = e.innerHTML),
                    t.setAttribute(
                      "data-select-value",
                      e.getAttribute("data-value")
                    ),
                    i.classList.toggle("-is-visible");
                });
              });
            })(t)
          ),
            document.querySelectorAll(".js-multiple-select").forEach((t) =>
              (function (t) {
                console.log(t);
                const n = t.querySelector(".js-button"),
                  s = n.querySelector(".js-button-title");
                n.addEventListener("click", () => {
                  let n = t.querySelector(".js-dropdown");
                  n.classList.contains("-is-visible")
                    ? n.classList.remove("-is-visible")
                    : (e(), n.classList.add("-is-visible"));
                });
                const i = t.querySelector(".js-dropdown");
                i.querySelectorAll(".js-options > *").forEach((e) => {
                  e.addEventListener("click", () => {
                    let n = [];
                    e.classList.toggle("-is-choosen");
                    const r = i.querySelectorAll(
                      ".-is-choosen .js-target-title"
                    );
                    r.forEach((e) => {
                      n.push(e.innerHTML);
                    }),
                      r.length
                        ? ((s.innerHTML = n.join(", ")),
                          t.setAttribute("data-select-value", n.join(", ")))
                        : ((s.innerHTML = "Default"),
                          t.setAttribute("data-select-value", ""));
                    const l = e.querySelector("input");
                    l.checked = !l.checked;
                  });
                });
              })(t)
            );
        },
      };
    })();
  const r = (function () {
      function e() {
        const e = document.querySelectorAll(".-is-dd-wrap-active");
        e &&
          e.forEach((e) => {
            e.classList.remove("-is-dd-wrap-active");
          });
        const t = document.querySelectorAll(".js-form-dd");
        t &&
          t.forEach((e) => {
            const t = e.querySelector("[data-x-dd]");
            e.querySelector("[data-x-dd-click]")
              .getAttribute("data-x-dd-click")
              .split(", ")
              .forEach((e) => {
                t.classList.remove("-is-active");
                const n = document.querySelector(`[data-x-dd=${e}]`),
                  s = n.getAttribute("data-x-dd-toggle");
                n.classList.remove(s);
              });
          });
      }
      return {
        ddInit: function () {
          const t = document.querySelectorAll(".js-form-dd");
          t &&
            t.forEach((t) => {
              const n = t.querySelector("[data-x-dd-click]");
              n.getAttribute("data-x-dd-click")
                .split(", ")
                .forEach((s) => {
                  const i = t.querySelector(`[data-x-dd=${s}]`),
                    r = i.getAttribute("data-x-dd-toggle");
                  n.addEventListener("click", () => {
                    n.querySelector(".js-dd-focus") &&
                      n.querySelector(".js-dd-focus").focus(),
                      i.classList.contains(r)
                        ? (i.classList.remove(r),
                          t.classList.remove("-is-dd-wrap-active"))
                        : (e(),
                          i.classList.add(r),
                          t.classList.add("-is-dd-wrap-active"));
                  });
                });
            });
        },
        closeAllDropdowns: e,
        init: function () {
          const e = document.querySelectorAll("[data-x-click]");
          e &&
            e.forEach((e) => {
              e.getAttribute("data-x-click")
                .split(", ")
                .forEach((t) => {
                  const n = document.querySelector(`[data-x=${t}]`);
                  e.addEventListener("click", () => {
                    const e = n.getAttribute("data-x-toggle");
                    n.classList.toggle(e);
                  });
                });
            });
        },
      };
    })(),
    l = (function () {
      let e,
        t,
        n,
        s = gsap.timeline();
      function i(e) {
        return e;
      }
      function r(e, n, r) {
        let l = e.children;
        const o = (l = Array.from(l)).map((e) => e.querySelector("li > a"));
        let c = n.children;
        const a = (c = Array.from(c)).map((e) => e.querySelector("li > a"));
        ((window.innerWidth > 0 ? window.innerWidth : screen.width) < 1199 ||
          document.querySelector(".js-desktopMenu")) &&
          (s.clear(),
          i(r) ||
            gsap.to(t, { ease: "quart.inOut", duration: 0.6, opacity: 0 }),
          s.to(o, {
            ease: "quart.out",
            stagger: -0.04,
            duration: 0.8,
            y: "100%",
            onStart: () => {
              n.classList.add("-is-active");
            },
            onComplete: () => {
              e.classList.remove("-is-active");
            },
          }),
          i(r) &&
            s.to(
              t,
              { ease: "quart.inOut", duration: 0.6, y: "0px", opacity: 1 },
              ">-0.5"
            ),
          s.to(
            a,
            { ease: "quart.out", stagger: 0.08, duration: 0.9, y: "0%" },
            ">-0.6"
          ));
      }
      return {
        headerSticky: function () {
          const e = document.querySelector(".js-header");
          if (!e) return;
          let t = "";
          e.getAttribute("data-add-bg") && (t = e.getAttribute("data-add-bg")),
            new ScrollMagic.Scene({ offset: "6px" })
              .setClassToggle(e, t)
              .addTo(App.SMcontroller),
            new ScrollMagic.Scene({ offset: "6px" })
              .setClassToggle(e, "is-sticky")
              .addTo(App.SMcontroller);
        },
        init: function () {
          (e = document.querySelector(".js-navList")),
            (t = document.querySelectorAll(".js-nav-list-back")),
            (n = 0),
            (function () {
              const s = document.querySelectorAll(
                ".js-navList .menu-item-has-children"
              );
              s.length &&
                (t.forEach((t) => {
                  t.addEventListener("click", () => {
                    const t = e.querySelector("ul.-is-active"),
                      s = t.parentElement.parentElement;
                    r(
                      t,
                      s,
                      --n,
                      s.parentElement.querySelector("li > a").innerHTML
                    );
                  });
                }),
                s.forEach((e) => {
                  const t = e.querySelector("li > a");
                  t.removeAttribute("href"),
                    t.addEventListener("click", () => {
                      const s = e.parentElement,
                        i = e.lastElementChild;
                      r(s, i, ++n, t.innerHTML);
                    });
                }));
            })();
        },
      };
    })();
})();
