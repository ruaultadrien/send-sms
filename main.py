import vonage
import os


def main():
    client = vonage.Client(
        key=os.environ["VONAGE_API_KEY"], secret=os.environ["VONAGE_API_SECRET"]
    )
    sms = vonage.Sms(client)
    response_data = sms.send_message(
        {
            "from": "J. Mollard",
            "to": os.environ["TO_NUMBER"],
            "text": "Bouge ton cul et va à la conf fiston !",
        }
    )

    if response_data["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(
            f"Message failed with error: {response_data['messages'][0]['error-text']}"
        )


if __name__ == "__main__":
    main()
