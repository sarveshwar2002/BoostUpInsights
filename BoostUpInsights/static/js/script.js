function navigateTo(section) {
    if (section === 'bloggers') {
        window.location.href = '#bloggers';
    } else if (section === 'photographers') {
        window.location.href = '#photographers';
    } else if (section === 'ecommerce') {
        window.location.href = '#ecommerce';
    }
}

document.getElementById('contactForm').addEventListener('submit', function(event) {
    event.preventDefault();
    alert('Message sent!');
});
