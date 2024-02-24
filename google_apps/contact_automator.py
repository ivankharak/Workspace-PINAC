import json
from __init__ import create_service  # Assuming this is defined elsewhere


class ContactManager:
    """
    Manages contacts using Google People API and provides user-friendly functions.
    """

    def __init__(self):
        """
        Initializes the ContactManager and creates a Google People API service object.

        Raises:
            Exception: If an error occurs during Google People API service creation.
        """

        self.contact_template_path = "create_contact__template.txt"
        try:
            self.service = create_service("people", "v1")
        except Exception as e:
            raise Exception("Error creating Google People API service:", e)

    def get_phone_number(self, query):
        """
        Searches contacts for a given query and returns the phone number associated with the first match.

        Args:
            query (str): The name or phone number to search for.

        Returns:
            str: The phone number of the first matching contact, or None if no match is found.
        """

        request = self.service.people().searchContacts(
            pageSize=10, query=query, readMask="names,phoneNumbers"
        ).execute()
        results = request.get("results", [])

        if len(results) == 1:
            name = results[0]["person"]["names"][0]["displayName"]
            phone_number = results[0]["person"]["phoneNumbers"][0]["canonicalForm"]
            return phone_number

        elif len(results) > 1:
            contact_list = []
            for person in range(len(results)):
                name = results[person]['person']['names'][0]['displayName']
                ph_no = results[person]['person']['phoneNumbers'][0]['canonicalForm']
                contact_list.append([name, ph_no])
            return contact_list
        return None

    def get_email_address(self, query):
        """
        Searches contacts for a given query and returns the email address associated with the first match.

        Args:
            query (str): The name or email address to search for.

        Returns:
            str: The email address of the first matching contact, or None if no match is found.
        """

        request = self.service.people().searchContacts(pageSize=10, query=query, readMask="names,emailAddresses").execute()
        results = request.get("results", [])

        if len(results) == 1:
            name = results[0]["person"]["names"][0]["displayName"]
            email = results[0]["person"]["emailAddresses"][0]["value"]
            return email

        elif len(results) > 1:
            email_list = []
            for person in range(len(results)):
                try:
                    name = results[person]['person']['names'][0]['displayName']
                    email = results[person]['person']['emailAddresses'][0]['value']
                    email_list.append([name, email])

                except Exception as error:
                    email_list = None
                    print(f"{type(error)} for {error}")
            return email_list
        return None

    def create_contact(self, **kwargs):
        """
        Creates a new contact using the provided information and saves it to Google Contacts.

        Args:
            **kwargs: Keyword arguments specifying contact details.
                - first_name (str, required): The first name of the contact.
                - phone_number (str, required): The phone number of the contact.
                - other optional arguments include:
                    - middle_name (str)
                    - last_name (str)
                    - nickname (str)
                    - company (str)
                    - department (str)
                    - job_title (str)
                    - email (str)
                    - website (list)
                    - address (str)
                    - birthday (list)  # Format: [YYYY, MM, DD]
                    - anniversary (list)  # Format: [YYYY, MM, DD]

        Returns:
            bool: True if the contact is created successfully, False otherwise.
        """

        if "first_name" not in kwargs or "phone_number" not in kwargs:
            print("Error: Both first_name and phone_number are required.")
            return False
        
        else:
            data = {
                'names': [
                    {'familyName': kwargs.get("last_name"),
                    'givenName': kwargs.get("first_name"),
                    'middleName': kwargs.get("middle_name")}
                    ],
                "phoneNumbers": [
                    {"type": "HOME",
                    "value": kwargs.get("phone_number")}
                    ],
                'nicknames': [
                    {'value': kwargs.get("nickname")}
                    ],
                'organizations': [
                    {'name': kwargs.get("company"),
                    'department': kwargs.get("department"),
                    'title': kwargs.get("job_title")}
                    ],
                "addresses": [
                    {"formattedValue": kwargs.get("address")}
                    ],
                "urls": [
                    {"type": "WEBSITE",
                    "value": kwargs.get("website")}
                    ],
                "emailAddresses": [
                    {"value": kwargs.get("email ")}
                    ],
            }
            if "birthday" in kwargs:
                for item in kwargs.get("birthday").values():
                    value = {'date': {'year': int(item[0]), 'month': int(item[1]), 'day': int(item[2])}}
                data["birthdays"] = [value]

            if "anniversary" in kwargs:
                for item in kwargs.get("anniversary").values():
                    value = {'date': {'year': int(item[0]), 'month': int(item[1]), 'day': int(item[2])}}
                data["anniversaries"] = [value]

            # preparing the data using json module
            processed_data = json.dumps(data)
            final_data = json.loads(processed_data)
            # print(final_data)
            self.service.people().createContact(body=final_data).execute()  # saving it to google with people API
            print("Contact saved successfully")
            return True

