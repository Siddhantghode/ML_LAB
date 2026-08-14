import matplotlib.pyplot as plt
subject=["python","java","DBMS"]
marks=[50,30,60]
plt.pie(marks,labels=subject,autopct="%1.1f%%",startangle=90)
plt.title("subject Marks"  )
plt.show()
