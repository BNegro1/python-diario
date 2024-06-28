// Function to extract and log titles
function extractTitles() {
    const titles = document.querySelectorAll('.challengecard-title');
    titles.forEach(title => {
      const titleText = title.childNodes[0].textContent.trim();
      console.log(titleText);
    });
  }
  
  // Function to scroll the page down
  function scrollPage() {
    window.scrollBy(0, window.innerHeight);
  }
  
  // Set interval for 15 seconds
  const interval = setInterval(() => {
    extractTitles();
    scrollPage();
  }, 1000); // 1000 ms interval for 15 iterations (15 seconds)
  
  setTimeout(() => {
    clearInterval(interval);
    console.log("Scrolling and extraction complete.");
  }, 15000); // Stop after 15 seconds
  