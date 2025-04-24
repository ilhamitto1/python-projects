print("🔍WEBSITE URL CHECKER")
url = input("\nEnter the website url:")
if url.startswith("https://"):
  print("🔒This website is secure")
elif url.startswith("http://"):
  print("💀This website is unsecure")
else:
  print("❌ This doesn't look like a valid url")
  