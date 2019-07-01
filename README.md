# CanIGoToDisneylandToday.com

## Requirements

- Node v10.16.0
- Python 3.6 (for legacy calendar parsing)

## Development

`npm install` for project dependencies, then `npm start` to access the dev server at http://localhost:1234.

## Deployment

Deployment happens via Netlify: https://app.netlify.com/sites/blissful-sinoussi-65935f/overview

## Updating Availabilities

Pass calendars used to be parsed from image files displayed at https://disneyland.disney.go.com/passes/blockout-dates/. Fortunately since the inception of this project Disney started using WebComponents and an API request to display their blockout calendars.

The **disneyAPIResponseParser.js** file contains logic needed to request these dates, and then parse them into the desired structure. It can be run with the following command:

```
$> npm run updateDates
```

Updated availabilities will be saved to **app/passDates/** as **.json** files.
