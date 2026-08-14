import matplotlib.pyplot as plt
student=["x","y","Z"]
marks=[50,30,60]
bars=plt.bar(student, marks,color=["orange","yellow","green"])
plt.title("Student Marks"  )
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
