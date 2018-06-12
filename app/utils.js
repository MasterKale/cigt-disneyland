/**
 * Pad numbers less than 10 with a 0 so they're always two digits
 * Ex: "9" => "09"
 * @param {Number} num - The number to pad
 * @returns {String}
 */
export function zeroPad(num) {
  return num < 10 ? `0${num}` : `${num}`;
}

/**
 * Get the current day in ISO format
 * @param {Date} date - An instance of Date
 * @returns {String}
 */
export function getDay(date) {
  const day = date.getDate();
  return zeroPad(day);
}

/**
 * Get the current month in ISO format
 * @param {Date} date - An instance of Date
 * @returns {String}
 */
export function getMonth(date) {
  // getMonth returns dates as a zero-index...
  const month = date.getMonth() + 1;
  return zeroPad(month);
}

/**
 * Convert true/false to "Yes"/"No"
 * @param {Boolean} bool
 * @returns {String}
 */
export function boolToWord(bool) {
  return bool ? 'Yes' : 'No';
}

/**
 * Get the local, timezone-respective date in ISO format
 * @returns {String}
 */
export function getTodayLocalISOString() {
  const today = new Date();
  const day = getDay(today);
  const month = getMonth(today);
  const year = today.getFullYear();

  return `${year}-${month}-${day}`;
}
