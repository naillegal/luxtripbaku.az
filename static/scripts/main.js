// languange-menu
document.querySelector(".rightside").addEventListener("click", function (e) {
  const languageMenu = document.querySelector(".language-open-menu");

  if (
    e.target.classList.contains("fa-chevron-down") ||
    e.target.id === "select-current"
  ) {
    $(languageMenu).slideToggle(300);
  }
});

document
  .getElementById("select-english")
  ?.addEventListener("click", function (e) {
    e.preventDefault();
    document.getElementById("lang-select").value = "en";
    document.getElementById("lang-form").submit();
  });

document
  .getElementById("select-russian")
  ?.addEventListener("click", function (e) {
    e.preventDefault();
    document.getElementById("lang-select").value = "ru";
    document.getElementById("lang-form").submit();
  });

document
  .getElementById("responsive-english")
  ?.addEventListener("click", function () {
    document.getElementById("lang-select").value = "en";
    document.getElementById("lang-form").submit();
  });

document
  .getElementById("responsive-russian")
  ?.addEventListener("click", function () {
    document.getElementById("lang-select").value = "ru";
    document.getElementById("lang-form").submit();
  });

// responsive-navbar
$(document).ready(function () {
  $(".inside-ul").hide();

  function hideResponsiveMenu() {
    $(".fa-bars")
      .removeClass("fa-x")
      .addClass("fa-bars")
      .css("transform", "rotate(0deg)");
    $("body").removeClass("overflow-hidden");
    $(".responsive-openmenu").animate({ left: "-100%" }, 400, function () {
      $(this).hide();
    });
  }

  if ($(window).width() >= 992) {
    hideResponsiveMenu();
  }

  $(".isopenmenu").click(function () {
    var $chevronIcon = $(this).find(".fa-chevron-down");
    $(this).siblings(".inside-ul").slideToggle();
    $(this)
      .siblings(".isopenmenu")
      .find(".fa-chevron-down")
      .removeClass("rotate")
      .css("transform", "rotate(0deg)");
    $chevronIcon.toggleClass("rotate");

    if ($chevronIcon.hasClass("rotate")) {
      $chevronIcon.css("transform", "rotate(180deg)");
    } else {
      $chevronIcon.css("transform", "rotate(0deg)");
    }
  });

  $(".fa-bars").click(function () {
    $(this).toggleClass("fa-bars fa-x");

    if ($(this).hasClass("fa-x")) {
      $(this).css("transform", "rotate(180deg)");
      $("body").addClass("overflow-hidden");
      $(".responsive-openmenu")
        .css("overflow", "auto")
        .show()
        .animate({ left: "0" }, 400);
    } else {
      $(".responsive-openmenu").animate({ left: "-100%" }, 400, function () {
        $(this).hide();
      });
      $("body").removeClass("overflow-hidden");
      $(this)
        .removeClass("fa-x")
        .addClass("fa-bars")
        .css("transform", "rotate(0deg)");
    }
  });

  $(window).on("resize", function () {
    if ($(window).width() >= 992) {
      hideResponsiveMenu();
    }
  });
});

// #main-forms
$(document).ready(function () {
  $(".fleet-form").show();
  $(".transfers-form").hide();
  $(".tour-fleet-form").hide();
  $(".tour-transfers-form").show();

  $(".category1").click(function () {
    $(".fleet-form").show();
    $(".transfers-form").hide();
    $(".tour-fleet-form").show();
    $(".tour-transfers-form").hide();

    $(".category1").addClass("active-category");
    $(".category2").removeClass("active-category");
  });

  $(".category3").click(function () {
    $(".fleet-form").show();
    $(".transfers-form").hide();
    $(".tour-fleet-form").show();
    $(".tour-transfers-form").hide();

    $(".category3").addClass("active-category");
    $(".category4").removeClass("active-category");
  });

  $(".category2").click(function () {
    $(".transfers-form").show();
    $(".fleet-form").hide();
    $(".tour-transfers-form").show();
    $(".tour-fleet-form").hide();

    $(".category2").addClass("active-category");
    $(".category1").removeClass("active-category");
  });

  $(".category4").click(function () {
    $(".transfers-form").show();
    $(".fleet-form").hide();
    $(".tour-transfers-form").show();
    $(".tour-fleet-form").hide();

    $(".category4").addClass("active-category");
    $(".category3").removeClass("active-category");
  });

  $(".category").click(function () {
    $(".category").removeClass("active-category");
    $(this).addClass("active-category");
  });
});

// main forms More details functionality
$(document).ready(function () {
  $(".toggle-btn button").click(function () {
    $(".hiddeninputs").slideToggle(300);
    var icon = $(this).find("i");
    icon.toggleClass("fa-chevron-down fa-chevron-up");
  });
});

// main forms change image
document.addEventListener("DOMContentLoaded", function () {
  const category1 = document.querySelector(".category1");
  const category2 = document.querySelector(".category2");
  const category3 = document.querySelector(".category3");
  const category4 = document.querySelector(".category4");
  const transferBg = document.querySelector(".transfer-bg");
  const tourBg = document.querySelector(".tour-bg");

  category1.addEventListener("click", function () {
    transferBg.style.display = "block";
    tourBg.style.display = "none";
  });
  category2.addEventListener("click", function () {
    transferBg.style.display = "none";
    tourBg.style.display = "block";
  });
  category3.addEventListener("click", function () {
    transferBg.style.display = "block";
    tourBg.style.display = "none";
  });
  category4.addEventListener("click", function () {
    transferBg.style.display = "none";
    tourBg.style.display = "block";
  });
});

// copyright autochange year
document.getElementById("year").textContent = new Date().getFullYear();

// FAQ
document.querySelectorAll(".faqs .click").forEach((flex) => {
  flex.addEventListener("click", function () {
    const faq = this.parentElement;
    const p = faq.querySelector("p");
    const plusIcon = this.querySelector(".fa-plus");
    const minusIcon = this.querySelector(".fa-minus");

    if (p.style.display === "none" || p.style.display === "") {
      $(p).slideDown(300);
      plusIcon.style.display = "none";
      minusIcon.style.display = "inline-block";
    } else {
      $(p).slideUp(300);
      plusIcon.style.display = "inline-block";
      minusIcon.style.display = "none";
    }
  });
});

// tours dropdown menu
$(document).ready(function () {
  $(".clickdown").click(function () {
    var $icon = $(this).find("i");
    var $showinfo = $(this).closest(".box").find(".showinfo");

    // Toggle the icon
    if ($icon.hasClass("fa-plus")) {
      $icon.removeClass("fa-plus").addClass("fa-minus");
    } else {
      $icon.removeClass("fa-minus").addClass("fa-plus");
    }

    $showinfo.slideToggle(300);
  });
});

// tourbytour
var swiper = new Swiper(".mySwiper", {
  slidesPerView: 1,
  spaceBetween: 30,
  loop: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

// Custom car select
document.addEventListener("DOMContentLoaded", function () {
  document.querySelectorAll(".custom-select").forEach((select) => {
    const selectedOption = select.querySelector(".selected-option");
    const optionsList = select.querySelector(".options");
    const hiddenSelect = select.querySelector("select");

    const options = optionsList.querySelectorAll("li");
    const secondOption = options[1];

    if (secondOption) {
      hiddenSelect.value = secondOption.getAttribute("data-value");
      selectedOption.innerHTML = secondOption.innerHTML;
    }

    selectedOption.addEventListener("click", () => {
      select.classList.toggle("open");
    });

    options.forEach((option) => {
      option.addEventListener("click", () => {
        const value = option.getAttribute("data-value");
        selectedOption.innerHTML = option.innerHTML;
        hiddenSelect.value = value;
        select.classList.remove("open");
      });
    });
  });
});

// tour form and fleet form change h2 at click
document.addEventListener("DOMContentLoaded", function () {
  function setupCategoryToggle(formId, startCategory) {
    const formSection = document.querySelector(`#${formId}`);

    if (!formSection) {
      console.error(`Element with ID #${formId} not found!`);
      return;
    }

    const category1 = formSection.querySelector(`.${startCategory}`);
    const category2 = formSection.querySelector(
      `.${startCategory === "category1" ? "category2" : "category1"}`
    );
    const headings = formSection.querySelectorAll("h2");

    if (category1 && category2 && headings.length === 2) {
      if (category1.classList.contains("active-category")) {
        headings[0].classList.remove("hide");
        headings[1].classList.add("hide");
      } else {
        headings[0].classList.add("hide");
        headings[1].classList.remove("hide");
      }

      category1.addEventListener("click", function () {
        category1.classList.add("active-category");
        category2.classList.remove("active-category");
        headings[0].classList.remove("hide");
        headings[1].classList.add("hide");
      });

      category2.addEventListener("click", function () {
        category2.classList.add("active-category");
        category1.classList.remove("active-category");
        headings[1].classList.remove("hide");
        headings[0].classList.add("hide");
      });
    } else {
      console.error(`Missing one or more elements in #${formId}`);
    }
  }

  if (document.querySelector("#include-tour-form")) {
    setupCategoryToggle("include-tour-form", "category2");
  }

  if (document.querySelector("#include-fleet-form")) {
    setupCategoryToggle("include-fleet-form", "category1");
  }
});

// All phone inputs start with +
document.addEventListener('DOMContentLoaded', function() {
  const phoneInput = document.querySelector('input[name="phone"]');

  phoneInput.addEventListener('input', function(event) {
      if (!event.target.value.startsWith('+')) {
          event.target.value = '+' + event.target.value.replace(/^\+/, '');
      }
  });

  if (!phoneInput.value.startsWith('+')) {
      phoneInput.value = '+' + phoneInput.value;
  }
});


// phone flag icons 
document.querySelectorAll('#country-code').forEach(function(selectElement) {
  selectElement.addEventListener('change', function() {
    const selectedCode = this.value;
    const parentFormGroup = this.closest('.form-group');
    
    const flags = parentFormGroup.querySelectorAll('.flag-icon'); 
    
    flags.forEach(function(flag) {
      flag.classList.remove('active');
    });

    const activeFlag = parentFormGroup.querySelector(`.flag-icon[data-code="${selectedCode}"]`);
    if (activeFlag) {
      activeFlag.classList.add('active');
    }
  });
});



