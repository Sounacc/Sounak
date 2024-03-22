import openai
import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv()

# api-key goes here (can use .env)
client = OpenAI(
    api_key=os.environ["OPENAI_KEY"],
)


# main function
def fetch_script(task):
    # handle basic runtime issues
    try:
        # code to geenerate script from gpt (can be prompt engineered)
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            # can engineer prompt for better outputs
            messages=[
                {
                    "role": "system",
                    "content": "Answer as concisely as possible. I will be giving you a task, Give me corresponding python playwright sync script. Do not give comments in the snippet and do not explain how the code works. Do not insert wait timers. Do not put in code in function block. For basic google search the input tag should not have any condition like name or title condition",
                },
                {"role": "user", "content": task},
            ],
        )
        print(
            response["choices"][0]["message"]["content"]
        )  # debug print for gpt output
        output = response["choices"][0]["message"]["content"]
        output = output.replace("```python", "```")  # removing markdown
        # removing leftover formatting
        try:
            output = (output.split("```"))[1].split("```")[0]
            if output.startswith("python"):
                output = output.lstrip("python")
        except:
            pass
        print(output)  # debug formatted output

        # Extract the desired code portion
        start_index = output.find("page.")
        end_index = len(output)
        print(start_index, end_index)  # debug print
        extracted_code = output[start_index:end_index]
        print(extracted_code)  # debug print

        # prepare content for runner file
        if "def" in extracted_code:
            # code to remove last two lines of code
            extracted_code = extracted_code.replace(
                extracted_code[
                    extracted_code.find("if __name__") : len(extracted_code)
                ],
                "",
            )
            output = (
                """
from playwright.sync_api import sync_playwright

def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(endpoint_url="http://localhost:9222")
        context = browser.contexts[0]
        page = context.pages[0]
        """
                + extracted_code
                + """
if __name__ == "__main__":
    main()"""
            )
        else:
            output = (
                """
import time
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.connect_over_cdp(endpoint_url="http://localhost:9222")
    context = browser.contexts[0]
    page = context.pages[0]
    """
                + extracted_code
            )

        # write to runner file
        with open("runner.py", "w") as f:
            f.write(output)

        # execute runner in background
        # os.system("conda activate playwright_env")
        # os.system('pip install playwright')
        os.system("python runner.py")

    # print errors if any
    except Exception as e:
        print(e)
