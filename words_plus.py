import pyperclip as p

import itertools
import json

from pathlib import Path

def generate_product(template, *lists):
    results = []
    # Generate all combinations of elements from the provided lists
    for combination in itertools.product(*lists):
        # Create a formatted string by replacing placeholders in the template
        formatted_string = template
        for i, value in enumerate(combination, 0): # or enumerate(combination, 1)
            formatted_string = formatted_string.replace(f"{{{{{i}}}}}", value)
        results.append(formatted_string)
    return results
# t1 = p.paste()

# tl1 = t1.split("\r\n")



# template1  = '''{{0}} ,
# {{1}}, where we create innovative {{2}} sold worldwide. We admire your creative work in the {{3}} community and would love to explore a potential collaboration with you.
# {{4}} We’re excited about the possibility of you creating something unique with our sets or help promote our sets.
# {{5}}

# Best,
# Bill Zou

# Marketing Director

# Email: bill@reobrix.com

# Tel: +86 177 4863 3055

# Web: www.reobrix.com
# '''

# tp0 = ["Hi", "Hello"]
# tp1 = ["I'm Bill from Reobrix", "This is Bill from Reobrix.com"]
# tp2 = ["building sets", "building blocks"]
# tp3 = ["building sets", "building blocks"]
# tp4 = ["Could you take a look at our products at reobrix.com and let us know if any models catch your eye?", 
# "We invite you to explore our products at reobrix.com. If any models stand out to you, we'd love to hear your thoughts!",
# "Please visit reobrix.com to view our product range. Feel free to let us know if any specific models grab your attention.",
# "Could you browse through our offerings at reobrix.com and tell us if there are any models that you find particularly appealing?",
# "We'd appreciate it if you could check out our products on reobrix.com and inform us about any models that pique your interest.",
# "Take a moment to review our products at reobrix.com. If any models catch your eye, please share your impressions with us!"]

# tp5 = ["If you’re interested, please reply so we can discuss this further.",
# "Should this catch your interest, feel free to respond and we can explore this in more detail.",
# "I’d love to hear your thoughts on this, so please reply if you’d like to discuss it further.",
# "If this sounds interesting to you, please let me know, and we can delve deeper into the conversation.",
# "Please respond if you're keen to discuss this opportunity further.",
# "If you find this intriguing, I encourage you to reply so we can talk more about it.",
# "I look forward to your feedback if you're interested in discussing this further.",
# "Should you be interested, please get back to me, and we can go into more details.",
# "Feel free to reach out if this appeals to you and you’d like to discuss it further.",
# "Let’s chat more if this piques your interest—just send me a reply.",
# "If you’re curious to learn more, please respond, and we can continue this conversation."]

# lists =[]
# lists.append(tp1)
# lists.append(tp2)
# lists.append(tp3)
# lists.append(tp4)
# lists.append(tp5)



# resulting_strings = generate_product(template, *lists)
# print(resulting_strings[:3])

# for i in resulting_strings[:3]:
#     print(i, end='\n'*5)



template2 = '''
{{0}},

{{1}} {{2}}

1. {{3}}

2. {{4}}

3. {{5}}

{{6}}

Best Regards,

'''
template2 = template2.strip()

tp0 = ["Hi there", "Hello there", "Hi", "Hello"]
tp1 = ["Hope you're doing great!", "I hope this email finds you well."]
tp2 = ["I’m Bill from Reobrix, where creativity meets quality in building block design. We're reaching out to explore opportunities for collaboration in several exciting areas:", "We're all about sparking creativity with our building blocks at Reobrix. There's something for everyone, whether you're looking for a new project or a gift. Check out our latest at Reobrix.com and start building!"]
tp3 = ["For Customers & Distributors: Explore our innovative building blocks and consider joining our global network. Check out our products at https://reobrix.com/.", "For Our Customers: Discover special collections and start your creative journey. It's all fun and inspiration."]
tp4 = ["For Influencers: Love building and sharing? Let's work together and spread the joy of building. Exciting rewards await!", "For Influencers: Help us inspire builders by showcasing our models. We offer exclusive access to our latest products for your creative showcases."]
tp5 = ["For MOC Fans: Got cool designs? We'd love to see and possibly collaborate. Show us what you've got!", "For MOC Fans: We’re eager to discover and purchase unique building block designs to turn them into commercial models that inspire globally."]
tp6 = ["If you’re interested in buying, promoting, or partnering with us, please reply to this email. Let’s create something amazing together!", "Interested in any of these? Just hit us up at Reobrix. Can't wait to build something amazing together."]


lists =[]
for i in range(6+1):
    lists.append(locals()[f"tp{i}"])



resulting_strings = generate_product(template2, *lists)

path = Path('words1.json')
words = json.dumps(resulting_strings)
path.write_text(words)
print(len(resulting_strings))