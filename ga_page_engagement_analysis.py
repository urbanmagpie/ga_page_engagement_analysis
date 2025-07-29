# Mock data for pages with views and average time on page (in seconds)
pages_data = [
    {'page': '/', 'views': 3370, 'avg_time': 10},
    {'page': '/canada', 'views': 228, 'avg_time': 7},
    {'page': '/search', 'views': 133, 'avg_time': 29},
    {'page': '/shop/new', 'views': 77, 'avg_time': 16},
    {'page': '/shop/apparel', 'views': 19, 'avg_time': 7},
    {'page': '/shop/clearance', 'views': 16, 'avg_time': 10},
    {'page': '/shop/lifestyle/bags', 'views': 14, 'avg_time': 23},
    {'page': '/shop/lifestyle', 'views': 13, 'avg_time': 8},
    {'page': '/shop/shop-by-brand/google', 'views': 13, 'avg_time': 96},
    {'page': '/canada/search', 'views': 12, 'avg_time': 17},
]

# Calculate overall average time on page
total_time = sum(page['avg_time'] for page in pages_data)
average_time = total_time / len(pages_data)

print(f"Average engagement time across all pages: {average_time:.2f} second")

# Find and sort pages with above-average engagement time (highest to lowest)
above_average_pages = sorted(
    [page for page in pages_data if page['avg_time'] > average_time],
    key=lambda page: page['avg_time'],
    reverse=True
)

# Print the sorted results
print("\nPages with above_average engagement time:")
for page in above_average_pages:
    print(f"{page['page']}: {page['avg_time']} seconds")
