const image1 = document.getElementById('image1');
const image2 = document.getElementById('image2');
const compareBtn = document.getElementById('compareBtn');
const differenceContainer = document.getElementById('differenceContainer');
const differenceImage = document.getElementById('differenceImage');

compareBtn.addEventListener('click', () => {
  // Call the Python script to compare the images
  fetch('/compare_images', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      image1Path: image1.src,
      image2Path: image2.src
    })
  })
  .then(response => response.json())
  .then(data => {
    // Display the difference image
    differenceImage.src = data.diffImagePath;
    differenceContainer.classList.remove('hidden');
  })
  .catch(error => console.error(error));
});