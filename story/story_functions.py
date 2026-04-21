import time
import textwrap

def story_print(text):
    if len(text) < 80:
        print(text)
    else:
        wrapped_text = textwrap.wrap(text, width= 60)
        for line in wrapped_text:
            print(line)
            time.sleep(1.5)