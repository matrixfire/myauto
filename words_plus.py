import pyperclip as p

import itertools

def generate_product(template, *lists):
    results = []
    # Generate all combinations of elements from the provided lists
    for combination in itertools.product(*lists):
        # Create a formatted string by replacing placeholders in the template
        formatted_string = template
        for i, value in enumerate(combination, 1):
            formatted_string = formatted_string.replace(f"{{{{{i}}}}}", value)
        results.append(formatted_string)
    return results
# t1 = p.paste()

# tl1 = t1.split("\r\n")



template  = '''Hi ,

{{1}}, where we create innovative {{2}} sold worldwide. We admire your creative work in the {{3}} community and would love to explore a potential collaboration with you.

{{4}} We’re excited about the possibility of you creating something unique with our sets or help promote our sets.

{{5}}

Best,'''

tp1 = ["I'm Bill from Reobrix", "This is Bill from Reobrix.com"]
tp2 = ["building sets", "building blocks"]
tp3 = ["building sets", "building blocks"]
tp4 = ["Could you take a look at our products at reobrix.com and let us know if any models catch your eye?", 
"We invite you to explore our products at reobrix.com. If any models stand out to you, we'd love to hear your thoughts!",
"Please visit reobrix.com to view our product range. Feel free to let us know if any specific models grab your attention.",
"Could you browse through our offerings at reobrix.com and tell us if there are any models that you find particularly appealing?",
"We'd appreciate it if you could check out our products on reobrix.com and inform us about any models that pique your interest.",
"Take a moment to review our products at reobrix.com. If any models catch your eye, please share your impressions with us!"]

tp5 = ["If you’re interested, please reply so we can discuss this further.",
"Should this catch your interest, feel free to respond and we can explore this in more detail.",
"I’d love to hear your thoughts on this, so please reply if you’d like to discuss it further.",
"If this sounds interesting to you, please let me know, and we can delve deeper into the conversation.",
"Please respond if you're keen to discuss this opportunity further.",
"If you find this intriguing, I encourage you to reply so we can talk more about it.",
"I look forward to your feedback if you're interested in discussing this further.",
"Should you be interested, please get back to me, and we can go into more details.",
"Feel free to reach out if this appeals to you and you’d like to discuss it further.",
"Let’s chat more if this piques your interest—just send me a reply.",
"If you’re curious to learn more, please respond, and we can continue this conversation."]

lists =[]
lists.append(tp1)
lists.append(tp2)
lists.append(tp3)
lists.append(tp4)
lists.append(tp5)



resulting_strings = generate_product(template, *lists)
# print(resulting_strings[:3])

# for i in resulting_strings[:3]:
#     print(i, end='\n'*5)