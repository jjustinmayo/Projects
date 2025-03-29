
const image = document.getElementById('LOGO');
let topPosition = 0;
let leftPosition = 0;

// Event listener to detect arrow key presses
window.addEventListener('keydown', function(event) {
  const step = 10; // Number of pixels to move the image

switch(event.key) {
    case 'ArrowUp':
        topPosition -= step;
        break;
    case 'ArrowDown':
        topPosition += step;
        break;
    case 'ArrowLeft':
        leftPosition -= step;
        break;
    case 'ArrowRight':
        leftPosition += step;
        break;
}

    image.style.top = `${topPosition}px`;
    image.style.left = `${leftPosition}px`;

});
// 1. Create a dynamically fixed area based on the size of the screen
// 2. create a box; make that box a "DVD jpeg"
// 3. Make the box move in any random direction upon a refresh or load
// 4. when the box hits the wall, it will go in the opposite diagonal it hit the wall
// 5. if it hits a corner perfectly, it will push against 2 diagonals in the inverse direction (I think)