import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "https://www.flipkart.com/search?q=lapotp&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&as-backfill=on"

# Headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Send a GET request
response = requests.get(url, headers=headers)

# Parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Find all product containers
products = soup.find_all("div", class_="tUxRFH")

# Loop through each product and extract details
for product in products:
    # Extract laptop image URL
    image_tag = product.select_one("img.DByuf4")
    image_url = image_tag["src"] if image_tag else "N/A"

    # Extract laptop product name
    name_tag = product.select_one("div.KzDlHZ")
    product_name = name_tag.text if name_tag else "N/A"

    # Extract laptop product rating
    rating_tag = product.select_one("div.XQDdHH")
    product_rating = rating_tag.text if rating_tag else "N/A"

    # Extract laptop product review count
    review_tag = product.select_one("span.Wphh3N")
    review_count = review_tag.text.strip() if review_tag else "N/A"

    # Extract laptop product information
    info_tag = product.select_one("div._6NESgJ ul.G4BRas")
    product_info = [li.text for li in info_tag.find_all("li")] if info_tag else "N/A"

    # Extract laptop original price
    original_price_tag = product.select_one("div.BfVC2z div.ZYYwLA")
    original_price = original_price_tag.text if original_price_tag else "N/A"

    # Extract laptop discount
    discount_tag = product.find("div", class_="UkUFwK")
    discount = discount_tag.text if discount_tag else "N/A"

    # Extract laptop discounted price
    discounted_price_tag = product.select_one("div.BfVC2z > div.cN1yYO div._4b5DiR")
    discounted_price = discounted_price_tag.text if discounted_price_tag else "N/A"

    # Check if a bank offer is available
    bank_offer_tag = product.select_one("div.M4DNwV div.n5vj9c div.O5Fpg8")
    is_bank_offer = "Yes" if bank_offer_tag else "No"

    # Print the extracted data
    print(f"Image URL: {image_url}")
    print(f"Product Name: {product_name}")
    print(f"Rating: {product_rating}")
    print(f"Review Count: {review_count}")
    print(f"Product Info: {product_info}")
    print(f"Original Price: {original_price}")
    print(f"Discount: {discount}")
    print(f"Discounted Price: {discounted_price}")
    print(f"Bank Offer: {is_bank_offer}")
    print("-" * 50)