import pandas as pd

# Sample data
data = {
    'Number': ['923166696633', '923126171516', '923370610033', '923111126927'],
    'Message': ['Hello, Zain!', '📢 خصوصی آفر! 📢🔐 دیسی لاک | نیشل لاک | محافظہ لاک | بیگ لاک | ندیم لاک |شفیق لاک📌 اب خصوصی رعایت کے ساتھ دستیاب ہیں!📍 انور ہارڈوئیر سٹور، ملتان📞 رابطہ: 03126171516 92111126927 Anwar', 'Hey, Ali!', 'Hello, Usman Anwar!'],
    'Image': ['image1.jpeg', 'image1.jpeg', 'image1.jpeg', 'image1.jpeg']
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel('contacts.xlsx', index=False)

print("contacts.xlsx file created successfully!")

