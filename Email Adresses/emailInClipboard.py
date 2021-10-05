#! python3
# emailInClipboard.py - Finds email addresses on the clipboard and copies them to the clipboard
# Usage: Copy some text call the program
# Example: >>> numberOnClipboard.py

import email
import pyperclip


def main():
    # Find matches in clipboard text.
    text = str(pyperclip.paste())
    matches = []
    for groups in email.regexp.findall(text):
        emails = groups[0]
        matches.append(emails)

    if len(matches) > 0:
        pyperclip.copy(' -+- '.join(matches))
        print("Email address(es) found:")
        print('\n'.join(matches))
    else:
        print('No email address found.')


if __name__ == "__main__":
    main()
