# WhatsApp Bot

An automated WhatsApp messaging bot built with Python.

## Features

- Sends WhatsApp messages and images to a contact list
- Reads recipients from an Excel file (`contacts.xlsx`)
- Uses PyWhatKit, PyAutoGUI and Pandas

## Setup

    pip install pandas pywhatkit pyautogui openpyxl

Create a `contacts.xlsx` file with columns:

| Number        | Message            | Image   |
|---------------|--------------------|---------|
| 923001234567  | Hello from bot!    | pic.jpg |

Then run:

    python whatsapp_bot.py

## Notes

- Numbers must include the country code (e.g. `92` for Pakistan).
- Keep your `contacts.xlsx` private - it contains personal data.
- This bot requires an active WhatsApp web session in the default browser.

## License

MIT