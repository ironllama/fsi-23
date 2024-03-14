pineapple_wiki = '''
The pineapple[2][3] (Ananas comosus) is a tropical plant with an edible fruit; it is the most economically significant plant in the family Bromeliaceae.[4]

The pineapple is indigenous to South America, where it has been cultivated for many centuries. The introduction of the pineapple to Europe in the 17th century made it a significant cultural icon of luxury. Since the 1820s, pineapple has been commercially grown in greenhouses and many tropical plantations.

Pineapples grow as a small shrub; the individual flowers of the unpollinated plant fuse to form a multiple fruit. The plant normally propagates from the offset produced at the top of the fruit[2][5] or from a side shoot, and typically matures within a year.

The pineapple is a herbaceous perennial, which grows to 1.0 to 1.5 m (3 ft 3 in to 4 ft 11 in) tall on average, although sometimes it can be taller. The plant has a short, stocky stem with tough, waxy leaves. When creating its fruit, it usually produces up to 200 flowers, although some large-fruited cultivars can exceed this. Once it flowers, the individual fruits of the flowers join together to create a multiple fruit. After the first fruit is produced, side shoots (called 'suckers' by commercial growers) are produced in the leaf axils of the main stem. These suckers may be removed for propagation, or left to produce additional fruits on the original plant.[5] Commercially, suckers that appear around the base are cultivated. It has 30 or more narrow, fleshy, trough-shaped leaves that are 30 to 100 cm (1 to 3+1⁄2 ft) long, surrounding a thick stem; the leaves have sharp spines along the margins. In the first year of growth, the axis lengthens and thickens, bearing numerous leaves in close spirals. After 12 to 20 months, the stem grows into a spike-like inflorescence up to 15 cm (6 in) long with over 100 spirally arranged, trimerous flowers, each subtended by a bract.

In the wild, pineapples are pollinated primarily by hummingbirds.[2][7] Certain wild pineapples are foraged and pollinated at night by bats.[8] Under cultivation, because seed development diminishes fruit quality, pollination is performed by hand, and seeds are retained only for breeding.[2] In Hawaii, where pineapples were cultivated and canned industrially throughout the 20th century,[9] importation of hummingbirds was prohibited.[10]

The ovaries develop into berries, which coalesce into a large, compact, multiple fruit. The fruit of a pineapple is usually arranged in two interlocking helices, often with 8 in one direction and 13 in the other, each being a Fibonacci number.[11]

The pineapple carries out CAM photosynthesis,[12] fixing carbon dioxide at night and storing it as the acid malate, then releasing it during the day aiding photosynthesis.
'''

alpha = "abcdefghijklmnopqrstuvwxyz "

filtered_string = ""
for letter in pineapple_wiki.lower():
  if letter in alpha:
    filtered_string += letter
  else:
    filtered_string += " "

filtered_list = filtered_string.split()
filtered_list = list(filter(lambda word: len(word) >= 2, filtered_list))

print("Total words:", len(filtered_list))

print("Num of \"fruit\":", filtered_list.count("fruit"))

frequencies = {}
for word in filtered_list:
  if word in frequencies:
    frequencies[word] += 1
  else:
    frequencies[word] = 1

sorted_freq = sorted(list(frequencies.items()), key=lambda word: word[1], reverse=True)

print("Top 10 most frequent words:")
for i, (word, freq) in enumerate(sorted_freq[:10]):
  print(f"[{i}] {word} ({freq})")
