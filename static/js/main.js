function updateTotal() {
  const checkboxes = document.querySelectorAll('input[name="items[]"]:checked');
  let total = 0;
  checkboxes.forEach(cb => {
    const price = parseFloat(cb.value.split('|')[1]);
    total += price;
  });
  document.getElementById('total').innerText = total.toFixed(2);
}
