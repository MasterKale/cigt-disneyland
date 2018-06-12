import './styles/index.scss';

import { getTodayLocalISOString, boolToWord } from './utils';

// JSON representations of each pass' blockout calendar
import socalDates from './passDates/socal.json';
import deluxeDates from './passDates/deluxe.json';
import sigDates from './passDates/sig.json';
import sigplusDates from './passDates/sigplus.json';

// DOM elements showing the big YES/NO
const socalElem = document.getElementById('socal');
const deluxeElem = document.getElementById('deluxe');
const sigElem = document.getElementById('sig');
const sigplusElem = document.getElementById('sigplus');

// Get the local date in YYYY-MM-DD format
const todayLocalISO = getTodayLocalISOString();

// Update the UI with whether each pass can go today
socalElem.innerText = boolToWord(socalDates[todayLocalISO]);
deluxeElem.innerText = boolToWord(deluxeDates[todayLocalISO]);
sigElem.innerText = boolToWord(sigDates[todayLocalISO]);
sigplusElem.innerText = boolToWord(sigplusDates[todayLocalISO]);

// Show the page now that JS has had a chance to figure out which passes can go
document.body.style.display = 'unset';
