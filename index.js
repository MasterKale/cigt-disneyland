import './styles/index.scss';

import socalDates from './passDates/socal.json';
import deluxeDates from './passDates/deluxe.json';
import sigDates from './passDates/sig.json';
import sigplusDates from './passDates/sigplus.json';

const socalElem = document.getElementById('socal');
const deluxeElem = document.getElementById('deluxe');
const sigElem = document.getElementById('sig');
const sigplusElem = document.getElementById('sigplus');

function getTodayLocalISOString() {
    const today = new Date();
    const day = _getDay(today);
    const month = _getMonth(today);
    const year = today.getFullYear();

    return `${year}-${month}-${day}`;
}

function _getDay(date) {
    const day = date.getDate();
    return _zeroPad(day);
}

function _getMonth(date) {
    // getMonth returns dates as a zero-index...
    const month = date.getMonth() + 1;
    return _zeroPad(month);
}

function _zeroPad(num) {
    return num < 10 ? `0${num}` : num;
}

function _boolToWord(bool) {
    return bool ? 'Yes' : 'No';
}

const todayLocalISO = getTodayLocalISOString();
console.log(todayLocalISO);
socalElem.innerText = _boolToWord(socalDates[todayLocalISO]);
deluxeElem.innerText = _boolToWord(deluxeDates[todayLocalISO]);
sigElem.innerText = _boolToWord(sigDates[todayLocalISO]);
sigplusElem.innerText = _boolToWord(sigplusDates[todayLocalISO]);
