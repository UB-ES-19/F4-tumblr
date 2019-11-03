
'use strict';

/**
 * List of content types admitted by tumblr
 */
const TYPES = [
    'text',
    'image',
    'quote',
    'link',
    'chat',
    'audio',
    'video',
];

/**
 * Hides the upload buttons and displays the given upload "modal" form.
 * Accepted types are text, image, quote, link, chat, audio and video.
 */
function displayUpload(type) {

    // Check this is a valid type
    if (!TYPES.includes(type)) {
        throw new Error('Type of content '+type+' not recognized.');
    }

    // Display the upload modal
    document.getElementById(type+'Modal').style.display = 'block';

    // Hide the buttons
    for(let div of document.getElementsByClassName('upload-button')) {
        div.style.display = 'none';
    }

    // Display the curtain
    document.getElementById('curtain').style.display = 'block';

}

/**
 * Hides any open upload form and displays the upload buttons.
 */
function hideUploads() {

    // Hide the upload forms
    for (let type of TYPES) {
        document.getElementById(type+'Modal').style.display = 'none';
    }

    // Display the buttons
    for(let div of document.getElementsByClassName('upload-button')) {
        div.style.display = 'inline';
    }

    // Hide the curtain
    document.getElementById('curtain').style.display = 'none';

}