document.addEventListener("DOMContentLoaded", function () {
  const quantityInputs = document.querySelectorAll(".quantity-input");
  const incrementBtns = document.querySelectorAll(".btn-increment");
  const decrementBtns = document.querySelectorAll(".btn-decrement");
  const totalDisplay = document.getElementById("total-price");
  const paymentModeInput = document.getElementById("payment_mode");
  const upiQRContainer = document.getElementById("upi-qr-container");
  const placeOrderBtn = document.getElementById("place-order-btn");
  const orderForm = document.getElementById("order-form");

  function calculateTotal() {
    let total = 0;
    quantityInputs.forEach(input => {
      const qty = parseInt(input.value) || 0;
      const price = parseFloat(input.dataset.price);
      total += qty * price;
    });
    totalDisplay.textContent = "₹" + total;
  }

  incrementBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const input = btn.parentElement.querySelector(".quantity-input");
      input.value = parseInt(input.value) + 1;
      calculateTotal();
    });
  });

  decrementBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      const input = btn.parentElement.querySelector(".quantity-input");
      const current = parseInt(input.value);
      if (current > 0) {
        input.value = current - 1;
        calculateTotal();
      }
    });
  });

  if (paymentModeInput) {
    paymentModeInput.addEventListener("change", () => {
      const selected = paymentModeInput.value;
      if (selected === "UPI") {
        upiQRContainer.style.display = "block";
      } else {
        upiQRContainer.style.display = "none";
      }
    });
  }

  if (orderForm) {
    orderForm.addEventListener("submit", function (e) {
      const payment = paymentModeInput.value;
      if (!payment) {
        e.preventDefault();
        alert("Please select a payment mode before placing order.");
        return;
      }

      if (payment === "UPI") {
        const confirmed = confirm("Please complete your UPI payment before continuing. Have you paid?");
        if (!confirmed) {
          e.preventDefault();
        }
      }
    });
  }

  calculateTotal();
});
