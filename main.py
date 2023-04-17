

import vonage
import os


def main():

    client = vonage.Client(key=os.environ['VONAGE_API_KEY'] , secret=os.environ['VONAGE_API_SECRET'])
    client.sms.send_message({
        "from": os.environ['VONAGE_BRAND_NAME'],
        "to": os.environ['TO_NUMBER'],
        "text": "A text message sent using the Vonage SMS API",
    })


if __name__ == "__main__":
    main()
