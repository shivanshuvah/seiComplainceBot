from complianceParser import llm_client, stripe_compliance_policy
import requests
from bs4 import BeautifulSoup
import os

def schedule_compliance_task(target_website, file_path):
    file_path = os.path.expanduser(file_path)
    print("executing queued up tasks ::: ", file_path)
    response = requests.get(target_website)
    soup = BeautifulSoup(response.content, "html.parser")
    webpage_text = soup.get_text()
    llm_response = llm_client.get_response(f"""    Check the following webpage content for compliance with the policy:
    Policy: {stripe_compliance_policy}
    Webpage content: {webpage_text}
    List any non-compliant issues you find.""")
    with open(file_path, "a") as text_file:
        text_file.write(llm_response)