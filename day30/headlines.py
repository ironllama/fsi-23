# Using Python and what you've learned so far, retrieve the "Most Popular"
# article headlines from the Korea Herald website. For this exercise, try
# to avoid using anything other package than the 'requests' package. List
# the headlines in the following format:
# [1]: Headline 1
# [2]: Headline 2
# [n]: Headline n
import requests

# Helper function that tries to extract all the html text within a tag with
# a given class. (Similar to JS's "innerHTML".) The class is assumed to be
# the only class for the tag. This will return all matches as a list.
def get_tag_contents_with_class(html, class_name):
    all_results = []
    start_find_pos = 0  # To track where we left off in previous loop.

    while True:
        # Look for the given class...
        class_pos = html.find(f"class=\"{class_name}\"", start_find_pos)

        if class_pos != -1:
            # First, search backwards to find the '<' to find the start of
            # the tag name, then forwards to find the end of the tag name.
            beg_start_tag_pos = html.rfind("<", 0, class_pos)
            end_tag_name_pos= html.find(" ", beg_start_tag_pos)
            tag_name = html[beg_start_tag_pos + 1: end_tag_name_pos]

            # Then find the end of the start tag as a starting point to find
            # the beginning of the end tag.
            end_start_tag_pos = html.find(">", beg_start_tag_pos)
            beg_close_tag_pos = html.find(f"</{tag_name}>", end_start_tag_pos + 1)

            # Now that we have the end of the start tag and beginning of the
            # end tag, we have the two bounds to get the substring we want
            inner_html = html[end_start_tag_pos + 1:beg_close_tag_pos]

            # print("HTML:", inner_html)
            all_results.append(inner_html)

            # Adjust the starting point for the next iteration of the loop.
            start_find_pos = beg_close_tag_pos + len(tag_name) + 1
        else:
            break
    return all_results

herald_html = requests.get("https://koreaherald.com").text

all_titles = get_tag_contents_with_class(herald_html, "news_title")

# Each of the results are still within a span, so we can call the same
# function to get the text from within the span, using the class. The
# function returns a list, but there should only be one item in it.
all_titles = [get_tag_contents_with_class(title, "ellipsis2")[0] for title in all_titles]

# For display
for idx, title in enumerate(all_titles):
    print(f"[{idx + 1}] {title}")
