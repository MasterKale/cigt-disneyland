const fs = require('fs');
const axios = require('axios');

const API_URL = 'https://disneyland.disney.go.com/passes/blockout-dates/api/get-calendars/?months=14';

/**
 * Parse a response from Disney's blockout calendar API into a format supported by this site
 */
async function parseResponse(parkName) {
  let resp;
  try {
    const response = await axios.get(API_URL);
    resp = response.data;
  } catch(err) {
    console.error('Issue requesting blockout dates:', err);
    return;
  }

  console.log('- Imported API response JSON');

  const { parks, entries } = resp;

  const parkInfo = parks.find(park => park.shortName === parkName);
  if (!parkInfo) {
    console.log(
      'No park found by that name. List of parks in repsonse:',
      parks.map(park => park.shortName),
    );
    return;
  }
  const parkID = parkInfo.id;

  console.log(`- Found park matching "${parkName}": ${parkID}`);

  Object.values(entries).forEach(entry => {
    const { productType, calendars } = entry;
    const outputFilename = `${productType.id}.json`;
    const parkCalendar = calendars[parkID];

    const availabilities = {};

    // Convert
    parkCalendar.goodToGoDates.forEach(date => {
      availabilities[date] = true;
    });
    parkCalendar.blockoutDates.forEach(date => {
      availabilities[date] = false;
    });

    // Sort availabilities by date
    const ordered = {};
    Object.keys(availabilities).sort().forEach(key => {
      ordered[key] = availabilities[key];
    });

    fs.writeFileSync(
      `app/passDates/${outputFilename}`,
      JSON.stringify(ordered),
      'utf8',
    );

    console.log(`- Wrote ${outputFilename}`);
  });
}

parseResponse('Disneyland');
