import pandas as pd
import pywhatkit as kit
import time

# Read Excel File
contacts_df = pd.read_excel("contacts.xlsx")

# Remove extra spaces from column names
contacts_df.columns = contacts_df.columns.str.strip()

# Message
notification_message = """
Hello, this is an automated notification system demo.
"""

for index, row in contacts_df.iterrows():

    phone = str(row['MOBIL NUMBER'])

    try:
        kit.sendwhatmsg_instantly(
            f"+91{phone}",
            notification_message,
            wait_time=15,
            tab_close=True
        )

        print(f"Message sent to {phone}")

        time.sleep(20)

    except Exception as e:
        print(f"Failed for {phone}")
        print(e)